# 设计文档：Step2/Step4 关系抽取增强

> 日期：2026-06-16
> 关联项目：PT9L 红外体温计 DHF/DMR 文档一致性审查系统
> 状态：待用户审阅

## 1. 背景与目标

当前管道的 Step2（单文档内关系抽取）和 Step4（跨文档关系发现）存在以下问题：

1. **Step2**：[step2_extract_edges.py](../../../file_extractor/step2_extract_edges.py) 一次性把 19 种关系类型全部摆给 LLM 判断，候选过多导致误判（尤其是 VERIFIED_BY / COVERS / REPORTED_IN 等语义相近类型容易混淆）。
2. **Step4**：[step4_cross_doc_edges.py](../../../file_extractor/step4_cross_doc_edges.py) 完全依赖 `REGULATORY_GUIDES` 这张 12 条人工预定义规则表。规则外的关系永远发现不了；规则内的判断又因为 prompt 里只有"标准编号"没有条款内容，准确率受限（跨文档边目前导入图成功率仅 37%）。
3. **逻辑相关 vs 语义相关的区分**：向量/语义相似度只能找到"措辞像"的关系对，找不到"逻辑上应该相关但措辞完全不同"的关系对（如"电池续航测试"与"待机功耗设计输入"）。需要规则匹配和图结构传播来补足这一类发现路径。

**目标**：
- 提升 Step2 关系判断准确率（AutoRE 任务分解 + HCRE 层级分类）
- 让 Step4 既能覆盖法规预定义的关系，又能主动发现规则外的关系（4 层候选生成机制）
- 主动发现图中已存在追溯链的缺失环节（Think-on-Graph 图模式传播）

**不在本次范围**：DREEAM 证据溯源（evidence_spans）、GraphRAG 社区检测、KG Embedding 链接预测——留给后续阶段。

---

## 2. 总体架构

```
                    ┌─────────────── Step2（单文档内）───────────────┐
                    │  Step2a: 关系类型检测（AutoRE任务1，低成本过滤） │
                    │  Step2b: 层级分类配对（HCRE粗分→细分，按组调用） │
                    └──────────────────────────────────────────────┘
                                        │
                                merge_results.py
                                        │
                    ┌─────────────── Step4（跨文档）─────────────────┐
                    │                                                │
                    │   候选生成（4层，互补，按依赖顺序执行）：        │
                    │   ① 规则匹配层 — REGULATORY_GUIDES（+条款引用）│
                    │   ② 图模式传播层 — Think-on-Graph（依赖①的边） │
                    │   ③ 向量召回层 — DashScope embedding + MAQD    │
                    │   ④ 桥接实体层 — 共享实体发现（CodRED）        │
                    │                                                │
                    │   候选去重合并 → LLM 开放式验证（KXDocRE 注入）│
                    │                                                │
                    └──────────────────────────────────────────────┘
                                        │
                          cross_doc_edges.json + Neo4j + 中文报告
```

---

## 3. Step2 详细设计

### 3.1 关系类型层级分组（新增配置）

新增 `schema/relation_groups.yaml`，把现有 19 种边类型分成 5 组：

```yaml
relation_groups:
  structural:    [PART_OF, STATED_IN, INDEXES, LISTS_FILE, HAS_DETAIL]
  traceability:  [DERIVES_FROM, IMPLEMENTS, REFERENCES, CONSTRAINED_BY]
  verification:  [VERIFIED_BY, COVERS, REPORTED_IN, HAS_MEASUREMENT]
  risk_control:  [MITIGATED_BY, RESPONSIBLE_FOR, DEPENDS_ON, SCHEDULES]
  admin:         [SIGNED, REVIEWS, HAS_REVIEW_ITEM, HAS_REVISION, PRODUCES, DESCRIBES_SOFTWARE]
```

### 3.2 Step2a — 关系类型检测

新函数 `detect_relation_types_llm(data) -> list[str]`，替换 [extract_edges_llm](../../../file_extractor/step2_extract_edges.py#L151-L185) 现有的一次性调用第一步：

- 输入：节点摘要（精简，仅类型+数量+少量样例）+ 19 种关系类型简介
- 输出：该文档中可能存在的关系类型列表（如 `["MITIGATED_BY", "SIGNED", "HAS_DETAIL"]`）
- 该调用 token 量小，目的是过滤而非抽取

### 3.3 Step2b — 层级分类配对

新函数 `match_within_group(data, group_name, candidate_types) -> list[dict]`：

- 按 3.1 分组归类 3.2 筛出的类型，每个命中的组发一次 LLM 调用
- 输入：该组候选关系类型 + 相关节点（仅涉及该组类型的节点，缩小范围）
- 输出：实体配对 + 细分关系类型

### 3.4 规则推导部分

[derive_rule_based_edges](../../../file_extractor/step2_extract_edges.py#L69-L148) 保持不变，与 Step2b 结果合并去重（复用现有 [deduplicate_edges](../../../file_extractor/step2_extract_edges.py#L188-L197)）。

### 3.5 成本变化

每文档 LLM 调用次数：原 1 次 → 现 1（Step2a）+ N 次（Step2b，N = 命中组数，通常 2-4）。预计 token 总量增加 1.5-2x，但单次候选范围更小，准确率应提升。

---

## 4. Step4 详细设计

### 4.1 候选生成层① — 规则匹配（补充条款引用）

保留 [REGULATORY_GUIDES](../../../file_extractor/step4_cross_doc_edges.py#L29-L138) 结构，新增：

1. 新增 `file_extractor/regulatory_clauses.yaml`，存放条款转述要点（非逐字引用，见下方内容），每条 `REGULATORY_GUIDES` 规则关联一个 `clause_summary` 字段
2. 现有 12 条规则中，10 条可关联到下表 7 条转述条款（部分规则共用同一条款，如"需求→测试"与"设计输入→测试"都关联 7.3.6），其余 2 条（DocIndexEntry↔Document、Person 去重）本身是流程/数据治理逻辑，不需要条款支撑，保留原状不变
3. 本次设计保留现有 12 条规则数量不变，仅补充条款引用；是否继续扩充到 20+ 条新规则，留给下一轮迭代评估，不在本次实施范围内

`regulatory_clauses.yaml` 初始内容（基于公开资料转述，非标准原文逐字引用）：

```yaml
clauses:
  "ISO 13485 7.3.3":
    summary: >
      设计输入应基于预期用途确定功能、性能、可用性和安全要求，
      并需经评审确认完整、明确、可验证、不自相矛盾。
  "ISO 13485 7.3.6":
    summary: >
      设计验证用于确认设计输出满足设计输入的要求，应制定验证计划
      （方法、接收准则），并保留验证记录。
  "ISO 14971 7.1":
    summary: >
      针对评估为不可接受的风险，应采取风险控制措施降低风险，
      控制措施应与风险产生原因相对应。
  "ISO 14971 8":
    summary: >
      风险控制措施实施后，应验证其有效性，确认剩余风险是否
      降到可接受水平。
  "IEC 62304 5.7":
    summary: >
      软件系统测试阶段应针对软件需求规格中的功能、性能要求执行测试，
      确认软件实现满足需求。
  "ISO 13485 7.3.2":
    summary: >
      设计开发策划应规定开发阶段、评审/验证/确认活动、职责和接口关系，
      并形成文件。
  "ISO 13485 7.1":
    summary: >
      组织应确定适用的法规要求，并将其融入质量管理体系和产品实现过程。
```

> 注：DocIndexEntry↔Document、Person 去重两条规则属于流程/数据治理逻辑，无对应 ISO 条款，不需要 clause_summary。

### 4.2 候选生成层② — 图模式传播（Think-on-Graph）

新模块 `file_extractor/graph_pattern_propagation.py`，依赖层①已生成的边（执行顺序：①→②）：

1. 查询 Neo4j 中已有边，统计二跳模式出现频次，频次 ≥3 视为"高频模式"（如 `Risk -MITIGATED_BY-> RiskControl -VERIFIED_BY-> Test` 出现 5 次以上）
2. 对只完成第一跳、缺第二跳的节点（如某 RiskControl 没有连到任何 Test），提取该类型全部候选目标节点作为候选对
3. 这是发现"已知应存在但缺失"的追溯链断口的核心机制
4. 样本量较小时（当前仅 10 个样本文件）此层可能找不到足够频次的模式，属于预期内的冷启动限制，全量跑完 254 份文件后效果会更明显

### 4.3 候选生成层③ — 向量召回（MAQD + DashScope）

新模块 `file_extractor/embedding_retrieval.py`：

- 调用阿里云 DashScope `text-embedding-v3`（OpenAI 兼容接口：`base_url=https://dashscope.aliyuncs.com/compatible-mode/v1`），1024 维，单批最多 10 条文本
- 对每个节点生成多角度查询文本（原描述 + 数值指标 + 术语归一主题词），分别检索 Top-K（K=10）近邻后取并集（MAQD 思路）
- 向量结果存入 Neo4j 5.x 向量索引（`CREATE VECTOR INDEX`），供检索复用
- 相似度阈值：候选对 cosine similarity ≥ 0.5 才纳入候选集，避免噪声候选过多

### 4.4 候选生成层④ — 桥接实体（CodRED）

新函数 `find_bridge_entities(nodes) -> list[tuple]`：扫描所有节点的 `description`/`name`，找出被两个以上不同来源文档共同提及的实体名（人名、产品型号、标准编号），将共同提及该实体的节点两两配对，作为候选。

### 4.5 候选去重合并 + LLM 开放式验证

四层候选合并去重后统一验证，改造 [llm_batch_match](../../../file_extractor/step4_cross_doc_edges.py#L490-L524)：

- 命中已知规则的候选：注入对应 `clause_summary` 辅助判断（KXDocRE）
- 未命中已知规则的候选：允许 Claude 输出"存在关系，类型为：xxx（新发现）"，不强制套用预定义关系名
- 输出边新增 `discovery_layer` 字段（`rule`/`graph_pattern`/`embedding`/`bridge`），用于追踪各层贡献

---

## 5. 数据结构变更

| 文件/字段 | 变更 |
|---|---|
| `output/per_file/*.json` 的 `_edges` | 结构不变，生成逻辑改为两阶段 |
| `output/merged_graph.json` 节点 | 新增 `embedding` 字段（向量召回需要） |
| `output/cross_doc_edges.json` | 新增 `discovery_layer` 字段 |
| 新增 `schema/relation_groups.yaml` | Step2 层级分组定义 |
| 新增 `file_extractor/regulatory_clauses.yaml` | ISO 条款转述要点库 |
| `.env` | 新增 `DASHSCOPE_API_KEY`、`DASHSCOPE_EMBEDDING_MODEL`（已添加） |

---

## 6. 错误处理与降级策略

| 风险点 | 降级方案 |
|---|---|
| DashScope embedding 调用失败/超限 | 跳过层③，仅用层①②④候选，记录警告，不阻塞流程 |
| 图模式传播查询 Neo4j 超时/失败 | 跳过层②，记录警告 |
| LLM 验证调用失败 | 维持现状：捕获异常返回空列表，不中断主流程 |
| 候选数量过多 | 按相似度/置信度分数截断 Top-N，避免 token 爆炸 |

---

## 7. 验证方法

1. **Step2 改造**：抽 3 个样本文件，对比改造前后边数量与人工抽查 10 条边的准确率
2. **Step4 改造**：核心指标是"规则外发现边"数量（衡量本次改造价值），以及现有覆盖率指标（需求→设计输入、需求→测试等）是否提升
3. 不做大规模自动化测试（LLM 输出有随机性），以人工抽样审查为主

---

## 8. 已确认的技术决策

1. **Embedding 模型**：阿里云 DashScope `text-embedding-v3`，OpenAI 兼容接口，1024 维默认，API Key 已配置在 `.env`
2. **ISO 条款来源**：项目 `data/` 目录下未找到 ISO 标准原文文件（仅有 PT9L 产品自身的 DHF/DMR 文档），改为基于公开资料转述条款要点（非逐字引用，避免版权问题），见第 4.1 节内容
