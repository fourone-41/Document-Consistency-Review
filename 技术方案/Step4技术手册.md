# Step4 跨文档关系发现——技术手册

> 版本：2026-06-17  
> 适用模块：`file_extractor/step4_cross_doc_edges.py`

---

## 1. 背景与目标

PT9L DHF/DMR 文档一致性审查系统从 254 份医疗器械设计文件中提取结构化知识图谱，共 7 个步骤。**Step4** 是其中最复杂的一步：发现分散在不同文档中的节点之间的跨文档关系，例如：

- 某份需求文档里的需求条目 → 另一份设计说明书里的设计输入
- 某份风险管理文档里的风险控制措施 → 某份测试报告里的测试用例

这些关系是合规审查（ISO 13485、ISO 14971、IEC 62304）的核心证据链。Step4 的输出是 `cross_doc_edges.json`，以及写入 Neo4j 图数据库的边集合。

---

## 2. 四层候选生成架构

Step4 采用四层级联的候选生成策略，每层独立运行，失败不影响其他层：

```
层① 规则匹配（Rule）
层② 图模式传播（Graph Pattern Propagation）
层③ 向量召回（Embedding Retrieval）
层④ 桥接实体发现（Bridge Entities）
```

### 层① — 规则匹配（Rule）

依据 12 条医疗器械标准条款定义预期关系类型（REGULATORY_GUIDES），每条规则指定：

- 源节点类型（如 `requirements`）→ 目标节点类型（如 `design_inputs`）
- 匹配策略：ID 前缀精确匹配 → LLM 批量语义匹配（先精确后模糊）
- 关系类型（如 `TRACES_TO`、`MITIGATED_BY`、`VERIFIED_BY`）
- 依据标准（如 ISO 13485 7.3.3）

输出置信度：精确匹配为 high，LLM 语义匹配为 medium。

**12 条规则覆盖的关系：**

| # | 规则 | 依据标准 |
|---|------|---------|
| 1 | 需求 → 设计输入 | ISO 13485 7.3.3 |
| 2 | 设计输入 → 测试验证 | ISO 13485 7.3.6 |
| 3 | 风险 → 控制措施 | ISO 14971 7.1 |
| 4 | 控制措施 → 测试验证 | ISO 14971 8 |
| 5 | 需求 → 测试覆盖 | ISO 13485 7.3.6/7.3.7 |
| 6 | 软件项 → 测试验证 | IEC 62304 5.7 |
| 7 | 计划任务 → 文档产出 | ISO 13485 7.3.2 |
| 8 | DHF清单条目 → 文档存在性 | DHF Process |
| 9 | 法规标准 → 需求实现 | ISO 13485 7.1 |
| 10 | 法规标准 → 设计输入实现 | ISO 13485 7.3.3 |
| 11 | 功能 → 测试验证 | ISO 13485 7.3.6 |
| 12 | 人员跨文档身份识别 | Process |

### 层② — 图模式传播（Graph Pattern Propagation）

基于 Think-on-Graph 思路：统计已有边中高频出现的二跳模式，例如 `A→B→C` 这种三节点链路出现 3 次以上则视为高频模式。对已完成第一跳（`A→B` 存在）但缺第二跳（`B→C` 缺失）的节点，生成候选对送后续验证。

**关键参数：** `min_frequency=3`（模式至少出现 3 次才触发候选生成）

### 层③ — 向量召回（Embedding Retrieval）

对所有节点的文本字段调用阿里云 DashScope `text-embedding-v3` 接口，得到 1024 维向量，在 Python 内存中用 numpy 一次矩阵乘法计算全量余弦相似度，取跨文档、相似度 ≥ 0.5 的节点对作为候选。

**设计要点：** 相似度计算完全在 Python 内存中完成，**不依赖 Neo4j 向量索引**（Neo4j 向量索引异步填充，创建节点后立刻查询会阻塞等待，是早期版本反复挂死的根本原因之一）。

MAQD（多角度查询）：对每个节点生成"原始描述"和"描述+数值单位"两个查询文本，提升召回率。

### 层④ — 桥接实体发现（Bridge Entities）

识别在多份文档中共同出现的桥接实体（如人员姓名、风险编号、设备型号），通过共现关系发现不同文档节点之间的潜在联系。

---

## 3. 验证策略

四层候选生成后，按置信度分两路处理：

| 候选来源 | 处理方式 | 理由 |
|---------|---------|------|
| 层③ embedding | 直接输出，标记 `SEMANTICALLY_RELATED` | 余弦相似度 ≥ 0.5 已是语义过滤 |
| 层④ bridge | 直接输出，标记 `SEMANTICALLY_RELATED` | 共现是显式证据 |
| 层② graph_pattern | 送 LLM 做开放式验证 | 结构动机但无语义证据，需 LLM 判断关系是否真实存在并给出关系类型 |

**LLM 开放式验证** (`verify_candidates_open_llm`)：每批 20 对，让 LLM 判断每对节点之间是否存在关系，若存在则给出具体关系类型（已知类型直接返回，未知类型输出"新关系：XXX"）。

---

## 4. 运行模式

Step4 支持三种运行模式，通过 `--mode` 参数切换：

### recall 模式（默认，推荐审查使用）

```bash
python step4_cross_doc_edges.py --mode recall
```

recall 模式用于解决 fast 模式的召回不足问题：graph_pattern 层的价值在于发现“结构上应该有但语义上不明显”的断链，因此不再用 embedding 相似度作为唯一截断条件。该模式对 graph_pattern 候选做结构优先选择，默认保留 **top 800** 送 LLM 验证。

选择逻辑：

- 优先覆盖每个缺第二跳的中间节点，避免少数语义相似节点占满预算
- 优先保留高频二跳模式，例如多次出现的 `风险 → 控制措施 → 测试`
- 对合规关键链路加权，例如风险控制验证、需求测试覆盖
- 编号、标准号、数值单位等锚点只作为加分项
- embedding 只保留为独立的层③召回，不再作为 graph_pattern 的硬过滤器

该模式比 fast 更慢，但更适合正式审查，因为它优先降低结构性断链漏检风险。

### fast 模式（快速冒烟/控时使用）

```bash
python step4_cross_doc_edges.py --mode fast
```

graph_pattern 候选数量可能达到数千对（全量 254 份文档下实测约 8000+ 对）。fast 模式对这批候选先用 embedding 相似度排序，取 **top 200** 送 LLM 验证。

- embedding 排序额外耗时：约 30–60 秒（DashScope API + numpy）
- LLM 验证：200 / 20 = 10 批，约 2–3 分钟
- **总耗时：约 10–15 分钟**（层①规则匹配主要耗时）

排序逻辑：对每个节点提取所有文本字段（`description`、`measure`、`item` 等），调用 DashScope 得到向量，计算每对候选的余弦相似度，由高到低排列，保留相似度最高的 200 对。该模式运行时间最可控，但会牺牲一部分“结构上成立、语义上不明显”的断链召回，因此不建议作为正式审查的唯一结果。

### full 模式（适合离线批处理）

```bash
python step4_cross_doc_edges.py --mode full
```

全部候选不截断，全量送 LLM 验证。8000+ 对 / 20 = 400+ 次 LLM 调用，每次 10–60 秒，**预计耗时 1–7 小时**，视 AI Gateway 延迟而定。适合夜间离线运行后查看完整结果。

---

## 5. 已解决的挂死问题

开发过程中 Step4 出现过三次根本原因不同的挂死，记录如下供参考：

### 挂死 #1 — Neo4j 向量索引异步填充

**现象：** 程序在向量召回阶段挂起约 30 分钟无响应。

**根因：** 旧版向量召回模块创建 EmbeddingRef 节点后，立刻执行 Neo4j `db.index.vector.queryNodes`。Neo4j 向量索引是异步在后台填充的，节点创建完成不代表索引就绪，查询会阻塞等待索引进入 ONLINE 状态，而这个等待没有超时限制。

**修复：** 完全移除 Neo4j 向量索引依赖，改为在 Python 内存中用 numpy 余弦相似度矩阵完成全量计算（一次矩阵乘法 O(N²)，N≤500 完全可接受）。

### 挂死 #2 — LLM 客户端无超时

**现象：** 程序在 LLM 语义匹配阶段挂起约 16 分钟。

**根因：** `OpenAI` 客户端初始化时未设置 `timeout` 参数，九安 AI Gateway 偶发延迟时单次请求会无限等待，没有任何超时退出机制。

**修复：** 主 LLM 客户端和 DashScope embedding 客户端均设置 `timeout=60.0` 和 `timeout=30.0`，超时后抛出异常由上层 try/except 处理。

### 挂死 #3 — graph_pattern 候选数量爆炸

**现象：** 程序完成层①后在开放候选发现阶段挂起超过 13 分钟（实际若不中断将挂数小时）。

**根因：** `find_missing_next_hop` 对每个缺第二跳的中间节点，把整个目标类型的节点列表全部加入候选（`candidate_targets = nodes.get(target_type, [])`）。全量数据集下产出 8000+ 对 graph_pattern 候选，送 LLM 验证需要 400+ 次串行调用。

**修复：** 增加分级运行模式。fast 模式用 embedding 相似度对 graph_pattern 候选排序后截断到 top 200，适合快速冒烟；recall 模式改用结构优先选择，默认保留 top 800，适合正式审查；full 模式保留原始全量行为供离线使用。

---

## 6. 输出文件

| 文件 | 说明 |
|------|------|
| `output/cross_doc_edges.json` | 全量跨文档边，含 `discovery_layer` 字段标注来源层 |
| `output/cross_doc_report.md` | 中文分析报告，按关系类型汇总统计 |
| Neo4j 图数据库 | high/medium 置信度边写入，low 置信度仅保留在 JSON |

`discovery_layer` 取值：`rule`（层①）、`graph_pattern`（层②）、`embedding`（层③）、`bridge`（层④）。

---

## 7. 配置项

主要配置在 `config.py`（API Key、模型名等）和各模块顶部常量：

| 常量 | 位置 | 默认值 | 说明 |
|------|------|--------|------|
| `MAX_GRAPH_PATTERN_CANDIDATES` | step4 | 200 | fast 模式 graph_pattern 截断上限 |
| `RECALL_GRAPH_PATTERN_CANDIDATES` | step4 | 800 | recall 模式 graph_pattern 结构优先保留上限 |
| `RECALL_PER_FROM_NODE` | step4 | 3 | recall 模式每个缺边中间节点优先保留候选数 |
| `OPEN_VERIFY_BATCH_SIZE` | step4 | 20 | LLM 验证每批对数 |
| `SIMILARITY_THRESHOLD` | embedding_retrieval | 0.5 | 层③余弦相似度阈值 |
| `TOP_K` | embedding_retrieval | 10 | 每个节点最多取多少近邻 |
| `EMBEDDING_BATCH_SIZE` | embedding_retrieval | 10 | DashScope 单批最大文本数 |
