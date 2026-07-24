# 项目交接文档：医疗器械文档一致性审查系统

> 生成日期：2026-06-16
> 项目路径：`D:\项目文档一致性审查`
> 产品：PT9L 红外体温计 DHF/DMR 文档一致性审查

---

## 1. 项目概览

**项目名称**：医疗器械项目文档一致性审查系统

**核心目标**：为 PT9L 红外体温计的设计历史文件（DHF）和设计制造记录（DMR）建立自动化一致性审查系统，自动发现跨文件的冲突、矛盾与遗漏。

**解决的具体问题**：
- 约 254 份过程文档（doc/xls/pdf 已预转为 Markdown）中存在大量需要人工核对的交叉引用
- 手工审查耗时巨大且容易遗漏
- 需要自动发现：需求-测试追溯缺失、风险-控制措施覆盖不全、参数数值不一致、人员签名不一致等

**最终交付物**：
- Python 脚本管道（Step1-4 + merge + import）
- Neo4j 知识图谱数据库
- 交互式 HTML 图可视化
- 跨文档关系分析报告（中文 Markdown）
- 技术调研报告

**当前阶段**：开发中（POC 完成，10 个样本文件验证通过，尚未全量运行 254 份文件）

**使用对象**：医疗器械项目质量工程师、法规注册人员

---

## 2. 技术栈与环境

### 2.1 核心技术栈

| 组件 | 选型 |
|------|------|
| 语言 | Python 3.11（通过 Miniconda） |
| LLM | Claude Sonnet 4 (via 九安 AI Gateway) |
| API 接口 | OpenAI 兼容格式 |
| 数据模型 | LinkML schema + Pydantic v2 |
| 图数据库 | Neo4j Community 5 (Docker) |
| 可视化 | vis-network.js（HTML 独立文件） |
| 核心库 | openai>=1.0.0, pydantic>=2.0.0, instructor>=1.0.0, python-dotenv>=1.0.0, pyyaml>=6.0 |

### 2.2 环境配置

**API 配置**（`.env` 文件）：
```
GPT55_API_KEY=通过公司安全渠道获取
GPT55_API_URL=https://ai-gateway.ailab.jiuan.com/v1
GPT55_MODEL=claude-sonnet-4-6
```

**Neo4j**：Docker 运行，端口 7474(HTTP) / 7687(Bolt)，用户名 neo4j，密码 test1234

**Miniconda 位置**：`D:\miniconda3`

### 2.3 安装过程中执行的命令

```bash
# Miniconda 安装
# Docker Desktop 安装（用于 Neo4j）
docker pull neo4j:5
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/test1234 neo4j:5

# Python 依赖
pip install openai pydantic instructor python-dotenv pyyaml neo4j
```

---

## 3. 项目结构

### 3.1 目录结构

```
D:\项目文档一致性审查\
├── .env                         # API Key 等环境变量
├── .gitignore
├── terminology.yaml             # 术语归一化表（30+ 标准主题词）
├── CrossDocRE_技术详解.md       # 技术论文笔记
├── 技术调研报告_跨文档关系抽取.md # 技术调研报告
│
├── schema/                      # LinkML Schema 定义
│   ├── schema.yaml              # 节点类型与属性定义
│   └── edges.yaml               # 边类型与规则定义
│
├── file_extractor/              # ★ 核心代码目录
│   ├── config.py                # 配置（API、路径、chunk大小、文档类型映射）
│   ├── schema.py                # Pydantic 数据模型（21种节点类型）
│   ├── step1_extract_nodes.py   # Step1: LLM 节点抽取
│   ├── step2_extract_edges.py   # Step2: 规则+LLM 边抽取
│   ├── step3_generate_claims.py # Step3: Claims 事实断言生成
│   ├── step4_cross_doc_edges.py # Step4: 跨文档关系发现
│   ├── merge_results.py         # 合并所有 per_file JSON
│   ├── import_neo4j.py          # 导入 Neo4j
│   ├── generate_review_html.py  # 左右对比审查 HTML
│   ├── generate_graph_html.py   # 交互式图可视化（仿 Neo4j UI）
│   ├── terminology.yaml         # 术语归一化表
│   ├── requirements.txt         # Python 依赖
│   ├── WORK_SUMMARY.md          # 工作总结
│   ├── ARCHITECTURE_ISSUES.md   # 架构问题分析
│   └── output/
│       ├── per_file/            # 每个文件的独立 JSON 输出
│       ├── merged_graph.json    # 合并后的完整图
│       ├── cross_doc_edges.json # 跨文档关系
│       ├── cross_doc_report.md  # 跨文档分析报告（中文）
│       ├── review_comparison.html
│       └── graph_visualization.html  # 交互式图可视化
│
├── pt9l_markdown_output/        # ★ 源文档（已转为 Markdown）
│   ├── 01 立项批准书E0 23.11/
│   ├── 02 开发计划E0 23.11/
│   ├── 03 风险分析E0 23.11/
│   ├── 04 设计输入E0 23.11/
│   ├── 07 软件设计方案E0 23.11/
│   ├── 11 T1样机E0 23.11/
│   ├── 12 设计输出E0 23.11/
│   ├── 18 设计确认E0 23.11/
│   └── ...
│
├── data/                        # 原始数据/参考资料
├── verification/                # 验证相关
└── 相关过程文档/                # ISO/法规参考
```

### 3.2 数据流向

```
pt9l_markdown_output/*.md（源文档）
    │
    ▼ Step1: step1_extract_nodes.py
    │  对每个文件：detect_doc_type → chunk_text → LLM抽取 → try_parse_json
    ▼
output/per_file/{filename}.json（每文件的节点JSON）
    │
    ▼ Step2: step2_extract_edges.py
    │  规则推导 + LLM补充 → 写入 _edges 字段
    ▼
    ▼ Step3: step3_generate_claims.py
    │  从实体生成事实断言 → 写入 _claims 字段
    ▼
output/per_file/{filename}.json（含 nodes + edges + claims）
    │
    ▼ merge_results.py
    ▼
output/merged_graph.json（完整图：912节点 + 1183边）
    │
    ├──▶ import_neo4j.py → Neo4j 图数据库
    ├──▶ step4_cross_doc_edges.py → cross_doc_edges.json + cross_doc_report.md
    ├──▶ generate_review_html.py → review_comparison.html
    └──▶ generate_graph_html.py → graph_visualization.html
```

---

## 4. 核心功能与实现细节

### 4.1 Step1: 节点抽取 (`step1_extract_nodes.py`)

**逻辑**：
1. 遍历 `pt9l_markdown_output/` 下所有 `.md` 文件
2. 通过 `detect_doc_type()` 判断文档类型（优先文件名关键词，其次目录名）
3. `chunk_text()` 分割文档（多级策略：`##` → `#/|` → 按行强制切割）
4. 每个 chunk 发送 LLM，使用该类型对应的 prompt
5. `try_parse_json()` 健壮解析返回的 JSON
6. 合并所有 chunk 结果写入 `output/per_file/{filename}.json`

**关键函数**：
- `detect_doc_type(filepath: str) -> str`：文档类型识别
- `chunk_text(text: str, max_chars: int = 6000) -> list[str]`：分割文档
- `try_parse_json(text: str) -> dict`：健壮 JSON 解析（含 `_fix_json_string_issues` 状态机）
- `extract_file(filepath: Path) -> None`：单文件抽取入口

**关键参数**：
- `MAX_CHUNK_CHARS = 6000`
- `LLM_MAX_TOKENS = 16000`

**Prompt 模板**（每种文档类型一个，以 project_approval 为例）：
```
你是医疗器械DHF文档信息抽取专家。当前文件是【立项批准书/客户需求书】。
请从中抽取以下字段（JSON格式）：
- document: {title, doc_type, dhf_stage, version, date}
- requirements: [{req_id, category, description, value, unit, tolerance, condition}]
- markets: [{region, certification, selected, registrant, registration_path}]
- intended_use_items: [{seq, content}]
- functions: [{name, value, exists}]
- persons: [{name, title, signed}]
- regulations: [{std_id, clause, title, applicability}]
- semantic_fragments: [{fragment_type, content, topic_tags, related_subjects}]

严格输出 JSON，不要加 markdown 代码块标记。
字段为 null 或空数组时省略该字段。只抽取文档中明确存在的信息，不要编造。

【重要-SemanticFragment兜底规则】：
对于文档中有实质信息但无法放入上述结构化字段的长段落，
请整段放入 semantic_fragments 数组。
```

支持的文档类型：project_approval, dev_plan, risk_analysis, design_input, test_report, bom, review_checklist, software_design, dhf_index, general

### 4.2 Step2: 边抽取 (`step2_extract_edges.py`)

**逻辑**：双轨策略
1. **规则推导**：从节点字段自动生成边（如 Person 出现在 PlanTask.owner → RESPONSIBLE_FOR）
2. **LLM 补充**：将节点列表发给 LLM，让其发现隐式关系

**支持的边类型**（19种）：
HAS_DETAIL, RESPONSIBLE_FOR, LISTS_FILE, SCHEDULES, COVERS, DERIVES_FROM, CONSTRAINED_BY, DEPENDS_ON, HAS_REVIEW_ITEM, SIGNED, REVIEWS, REPORTED_IN, IMPLEMENTED_IN, DESCRIBES_SOFTWARE, HAS_REVISION, VERIFIED_BY, HAS_MEASUREMENT, MITIGATED_BY, PRODUCES

### 4.3 Step3: Claims 生成 (`step3_generate_claims.py`)

**逻辑**：从 Requirement/Risk/Test 等实体中提取事实断言（Claim），格式：
```json
{"subject": "自由文本", "predicate": "has_value/passes_test/...", "object_value": "...", "confidence": 0.9}
```

### 4.4 Step4: 跨文档关系发现 (`step4_cross_doc_edges.py`)

**逻辑**：
1. 加载 merged_graph.json 中所有节点
2. 定义 `REGULATORY_GUIDES`（法规知识引导表）指定期望的跨文档关系
3. 对每种期望关系，使用 LLM 批量语义匹配（`llm_batch_match`）
4. 结果写入 `cross_doc_edges.json` + Neo4j + 中文报告

**关键 Prompt**：
```
你是医疗器械文档关系分析专家。
任务：根据 {standard} 的要求，找出【源列表】和【目标列表】之间存在"{name}"关系的配对。
【源列表 ({src_type})】:
  S1. {summary}
  ...
【目标列表 ({tgt_type})】:
  T1. {summary}
  ...
请输出所有匹配对，格式为每行一个：S编号-T编号
```

**结果**：发现 397 条跨文档边，286 条成功导入 Neo4j

### 4.5 交互式图可视化 (`generate_graph_html.py`)

**功能**：生成仿 Neo4j Browser UI 的 HTML 文件
- 左侧标签面板（Node Labels + Relationship Types，点击筛选）
- 顶部查询栏（支持 Cypher-like 查询语法）
- 主图区域（vis-network 力导向布局）
- 底部属性面板（点击节点/边查看详情）
- 区分文档内边（灰蓝虚线）和跨文档边（橙黄实线）
- 设计开发计划表已从可视化中排除（节点过多）

**支持的查询语句**：
- `MATCH (n:Requirement) RETURN n`
- `MATCH (n:Risk)-[r]->(m:RiskControl) RETURN n,r,m`
- `MATCH (n)-[r:TRACES_TO]->(m) RETURN n,r,m`
- `MATCH (n)-[r]->(m) WHERE r.confidence='high' RETURN n,r,m`
- `MATCH (n) WHERE n.label CONTAINS '温度' RETURN n`
- `MATCH (n) RETURN n LIMIT 50`

---

## 5. 完整的问题与解决过程

### 5.1 LLM JSON 解析失败（核心 Bug）

**问题**：LLM 返回的 JSON 约 60% 存在格式问题，导致多个文件节点全部丢失。

**子问题**：
1. Markdown 代码块包裹（` ```json...``` `）
2. 字符串值内未转义换行符（`"note": "第一行\n第二行"`）
3. 字符串值内未转义双引号（`"content": "依据为\"PT9L标准\"进行测试"`）

**解决方案**：完全重写 `try_parse_json`，加入 `_fix_json_string_issues()` 状态机函数。

### 5.2 巨大文件 Chunk 分割失败

**问题**：`设计开发计划表E0 23.11`（85798 chars）是纯表格，无 `##` 标题，整体作为一个 chunk 导致 LLM 截断。

**解决方案**：`chunk_text` 增加多级分割策略 + `MAX_CHUNK_CHARS` 从 4000 调到 6000。

### 5.3 文档类型识别优先级错误

**问题**：评审检查表在"软件设计方案"目录下被误分类为 software_design。

**解决方案**：`detect_doc_type` 文件名关键词（评审/检查表/检测报告/BOM）优先于目录名。

### 5.4 Neo4j 导入问题

| 问题 | 解决 |
|------|------|
| Person name 为 null | 跳过空 name 节点 |
| CypherSyntaxError WHERE 位置 | 使用 `WITH a, b WHERE a <> b` |
| Test 节点属性为空 | 修复 try_parse_json 后 Test 正确抽取 |
| Risk/RiskControl 属性名不匹配 | TYPE_TO_PROP 映射用 hazard/measure |
| 边匹配率低 | CONTAINS + uid 灵活匹配 |

### 5.5 instructor 库弃用

**问题**：instructor 库在 token 截断时无限重试。

**解决方案**：移除 instructor，改用裸 OpenAI API + 手动 JSON 解析。

### 5.6 被放弃的方案

| 方案 | 放弃原因 |
|------|----------|
| 使用 instructor 库自动结构化 | token 截断时无限重试，且掩盖了 JSON 格式问题 |
| 固定阈值的关键词匹配跨文档关系 | 英文风险报告 vs 中文需求/测试完全无法匹配 |
| 按目录名做文档类型识别 | 文件组织结构不等于文档语义类型 |
| 一次 LLM 调用抽取所有关系 | 关系密度极低（仅 31 条），需要规则引擎补充 |
| 将所有文本强行结构化 | 大段描述性文字丢失，引入 SemanticFragment 兜底 |

---

## 6. 已完成内容

### 6.1 功能列表

- [x] 10 个样本文件的完整抽取管道（Step1-3）
- [x] 21 种节点类型 + 19 种边类型支持
- [x] 健壮的 JSON 解析（处理 LLM 输出格式问题）
- [x] 多级文档分割策略
- [x] 文档类型智能识别
- [x] Neo4j 图数据库导入
- [x] 跨文档关系发现（法规知识引导 + LLM 语义匹配）
- [x] 跨文档关系报告（中文）
- [x] 交互式 HTML 图可视化（仿 Neo4j UI）
- [x] 查询功能（Cypher-like 语法）
- [x] 技术调研报告

### 6.2 关键设计决策

| 决策 | 原因 |
|------|------|
| 用 raw OpenAI API 而非 instructor | 需要对截断/格式错误做自定义处理 |
| SemanticFragment 兜底机制 | 不丢失任何有意义的文本信息 |
| 规则引擎 + LLM 双轨边抽取 | LLM 对隐式关系不敏感，规则补充结构性关系 |
| LLM 批量语义匹配跨文档关系 | 关键词匹配太刻板，无法跨语言 |
| 法规知识引导表 | 利用 ISO/DHF 规定的文件对应关系提高关系召回率 |
| 报告输出中文 | the user 明确要求中文 |

---

## 7. 未解决的问题与挑战

### 7.1 当前限制

| 问题 | 说明 |
|------|------|
| 仅跑了 10 个样本文件 | 完整 DHF 可能有 50+ 文件需处理 |
| 实体去重缺失 | 同一 Person 在 17 个 chunk 中被抽取 17 次（115 个 Person 节点） |
| 边匹配率 79% | Neo4j 导入边成功率 931/1183，因 from/to 标识符匹配不精确 |
| SemanticFragment 过多 | 开发计划表产出 122 个 Fragment，需合并策略 |
| 跨文档边匹配率 37% | 149/397 成功导入 Neo4j |
| LLM 耗时 | 设计开发计划表 17 chunks 需 ~13 分钟 |
| Claims 质量 | 部分文件未生成 Claims（纯表格型文件） |

### 7.2 已知 Bug

- 部分 intra-doc edges 的 from/to 是 dict 而非 string（4/1183），需跳过
- 大型文件（>80000 chars）的 chunk 边界可能切断表格行

### 7.3 待定技术方案

- 是否引入向量索引做语义检索（Neo4j 5.x 支持）
- 是否使用 Leiden 社区检测组织审查报告
- 是否微调小模型替代 Claude 降低成本

---

## 8. 下一步计划（按优先级）

### P0（立即）
1. 抽取失败自动重试 + 质量校验
2. 实体去重（Person/Product 合并）
3. 改进 Step2 prompt（附加共现上下文，参考 ATLOP）
4. Step4 prompt 注入 ISO 法规条款（参考 KXDocRE）
5. 所有步骤输出 evidence_spans 证据定位（参考 DREEAM）

### P1（2-4 周）
6. 文本路径构建，通过桥接实体串联跨文档关系（参考 CodRED）
7. Step2 改为两步分解：先枚举关系类型，再按类型配对（参考 AutoRE）
8. 层级树分类替代一步到位的关系判断（参考 HCRE）
9. 多角度候选召回提高语义匹配覆盖率（参考 MAQD）

### P2（4-8 周）
10. Neo4j 向量索引 + 混合检索
11. Leiden 社区检测，按审查单元组织报告
12. 全量 254 份文件处理 + 增量更新

### P3（远期）
13. 远程监督数据生成 + 小模型微调
14. KG Embedding 链接预测

---

## 9. 工作偏好与协作规则

### 9.1 明确规则

- **Always**：回复使用中文
- **Always**：报告、文档内容写中文
- **Always**：代码中变量名/函数名用英文，注释可中文
- **Never**：不要在用户没要求时自行提交 git commit
- **Prefer**：遇到不确定时先问用户一个问题再继续（一次只问一个）

### 9.2 偏好

- the user 喜欢先看到方案选项，自己选择方向后再让 AI 执行
- the user 偏好简洁直接的回复，不需要过多解释
- 当 the user 说"你自己决定就行"时，可以自主选择最优方案执行
- the user 对 LLM 输出质量有较高要求，发现空结果会立即追问

### 9.3 决策点（需询问用户）

- 新增功能模块的架构方案选择
- 是否需要全量重跑管道
- 方案涉及较大改动时
- 输出文件的格式和位置

---

## 10. 使用方式

```bash
# 激活环境
conda activate base

# 完整管道执行
cd D:\项目文档一致性审查\file_extractor
python step1_extract_nodes.py   # ~20 min for 10 files
python step2_extract_edges.py   # ~7 min
python step3_generate_claims.py # ~2 min
python merge_results.py         # 即时
python import_neo4j.py          # ~30s
python step4_cross_doc_edges.py # ~5 min
python generate_graph_html.py   # 即时

# Neo4j 查看
# 浏览器打开 http://localhost:7474
# 用户名: neo4j / 密码: test1234

# 交互式图查看
# 直接浏览器打开 output/graph_visualization.html
```

---

*本文档由 AI 助手自动生成，基于项目全部历史对话和代码分析*
