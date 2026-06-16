# 项目迁移文档：医疗器械项目文档一致性审查系统

> 生成日期：2026-06-12  
> 项目路径：`D:\项目文档一致性审查`  
> 产品：PT9L 红外体温计 DHF/DMR 文档一致性审查  
> 用途：本文档用于将项目上下文迁移到新的 AI 助手工具

---

## 一、项目概述

### 1.1 项目目标

为医疗器械（PT9L 红外体温计）的设计历史文件（DHF）和设计制造记录（DMR）建立**自动化一致性审查系统**。

核心能力：
1. 读入全部 ~254 份过程文档（doc/xls/pdf 已预转为 Markdown）
2. 自动发现文件间的冲突、矛盾与遗漏
3. 输出审查报告，列出每条问题及精确双向定位

### 1.2 核心技术思路

> 把每份文件中的事实性陈述，抽取并归一化为统一格式的"结构化断言（Claim）"，然后通过结构化字段做精确匹配来实现跨文件对齐，最后在对齐结果上执行一致性规则检查。

类比：雇 100 个助理把 254 份文件信息抄到统一格式的索引卡片，按"主题+属性"分组后比对数值。

### 1.3 技术栈

| 组件 | 选型 |
|------|------|
| LLM | Claude Sonnet 4 (via 九安 AI Gateway) |
| API 接口 | OpenAI 兼容格式 (`https://ai-gateway.ailab.jiuan.com/v1`) |
| 数据模型 | LinkML schema + Pydantic |
| 图数据库 | Neo4j Community 5 (Docker) |
| 语言 | Python 3.11 |
| 核心库 | openai, pydantic, instructor, pyyaml, python-dotenv, neo4j |

---

## 二、项目目录结构

```
D:\项目文档一致性审查\
├── .env                         # 环境变量（API Key 等）
├── .gitignore
├── terminology.yaml             # 术语归一化表 v0.4（30+ 标准主题词）
├── 需求文档.md                  # 项目技术路线说明书 v0.2
├── 20260603周报.docx
│
├── schema/                      # ★ 唯一可信源：系统 Schema
│   ├── schema.yaml              # LinkML 格式 节点/字段/枚举 定义
│   ├── edges.yaml               # 边（关系）类型目录
│   ├── terminology.yaml         # 术语归一表
│   ├── profiles.yaml            # 14 类文档的抽取 profile
│   ├── models.py                # Pydantic 模型（自动生成）
│   └── README.md                # Schema 设计方法论
│
├── file_extractor/              # ★ 核心抽取管道 V3
│   ├── config.py                # 配置（API、路径、chunk 大小）
│   ├── schema.py                # Pydantic 数据模型
│   ├── step1_extract_nodes.py   # Step1: LLM 节点抽取
│   ├── step2_extract_edges.py   # Step2: 规则+LLM 边抽取
│   ├── step3_generate_claims.py # Step3: Claims 生成
│   ├── step4_cross_doc_edges.py # Step4: 跨文档关系发现
│   ├── merge_results.py         # 合并为 merged_graph.json
│   ├── import_neo4j.py          # 导入 Neo4j
│   ├── generate_review_html.py  # 生成对比审查 HTML
│   ├── test_api.py              # API 连通性测试
│   ├── requirements.txt         # Python 依赖
│   ├── WORK_SUMMARY.md          # 工作总结
│   ├── ARCHITECTURE_ISSUES.md   # 架构问题分析与改进方向
│   └── output/                  # 抽取结果
│       ├── per_file/            # 每个文件的独立 JSON
│       ├── merged_graph.json    # 合并后的完整图
│       ├── cross_doc_edges.json # 跨文档关系
│       ├── cross_doc_report.md  # 跨文档关系分析报告
│       └── review_comparison.html
│
├── verification/                # POC 验证模块（早期原型）
│   ├── config.py
│   ├── schema.py
│   ├── step1_extract.py
│   ├── step2_normalize.py
│   ├── step3_neo4j_import.py
│   ├── generate_detailed_report.py
│   ├── generate_report.py
│   ├── gen_graph_report.py
│   ├── requirements.txt
│   ├── terminology.yaml
│   └── output/                  # 验证结果
│
├── data/                        # 原始文件（DHF + DMR）
│   ├── DHF -红外额温/           # 12 阶段 DHF 文档
│   └── DMR-全-20260421/         # DMR 生产文件
│
└── pt9l_markdown_output/        # ★ 预转换的 Markdown 文件（470 份）
    ├── 01 立项批准书E0 23.11/
    ├── 02 开发计划E0 23.11/
    ├── 03 风险分析/
    ├── 04 设计输入E0 23.11/
    ├── 05 结构设计方案E0 23.11/
    ├── 06 硬件设计方案E0 23.11/
    ├── 07 软件设计方案E0 23.11/
    ├── ...（共 19 个 DHF 阶段目录）
    ├── PT9结构DHF/
    ├── 实验报告/
    ├── 历史记录/
    └── _assets/
```

---

## 三、数据模型（Schema）

### 3.1 节点分 4 层

| 层级 | 名称 | 节点类型 | 用途 |
|------|------|---------|------|
| 层1 | 结构层 | Document, Section | 定位溯源 |
| 层2 | 锚点层 | Product, Identifier, Person | 确定性身份，可合并去重 |
| 层3 | 领域层 | Requirement, DesignInput, Risk, RiskControl, Test, TestReport, Regulation, Function, Component, ReviewRecord | 业务实体 |
| 层3 | 补充层 | RevisionRecord, ReviewItem, DocIndexEntry, TestMeasurement, SoftwareItem, SoftwareConfigItem, IssueItem, PlanTask, Resource | 过程/记录类型 |
| 层4 | 裁决层 | Claim, Statement, SemanticFragment | 对齐主干，不合并 |

### 3.2 合并铁律

- **锚点类**（有唯一编号的实体）：同一个东西多份文件出现 → 合并成 1 个节点，用 MERGE
- **断言类**（Claim/SemanticFragment）：哪怕说的是同一件事也各自独立成节点，用 CORRESPONDS_TO 边连接，**绝不合并**

### 3.3 边类型

**抽取期边**（LLM 从文件中识别）：
- PART_OF, STATED_IN, DECLARES, DERIVES_FROM, MUST_BE_GEQ, CONSTRAINED_BY
- MITIGATED_BY, VERIFIED_BY, REPORTED_IN, ADDRESSED_IN, SIGNED
- IMPLEMENTED_IN, REFERENCES, COVERS, RELATES_TO
- HAS_REVISION, HAS_REVIEW_ITEM, REVIEWS, LISTS_FILE, INDEXES
- HAS_MEASUREMENT, MEASURES, DESCRIBES_SOFTWARE, TRACKS_ISSUE, ABOUT
- SCHEDULES, DEPENDS_ON, USES_RESOURCE

**推理期边**（对齐/检查引擎产生）：
- CORRESPONDS_TO：两个 Claim 说同一件事（relation ∈ equal/geq/lt/sub_allocation/condition_mismatch）
- CONFLICTS_WITH：检出的冲突
- POTENTIALLY_CONFLICTS：LLM 判定的潜在矛盾

### 3.4 文档类型分类（14 类 profile）

立项_需求 / 设计输入 / 设计输出_清单 / BOM_物料 / 开发计划 / 风险分析 / 软件设计 / 测试_验证 / 评审检查表 / 图样方案 / 说明书_标签 / 设计确认 / 作业指导 / 其它

---

## 四、术语归一化体系

### 4.1 设计原则

- 把不同文件里同义表述归到同一个 subject 标准词
- `direction` 决定不退化检查的比较方向

### 4.2 已覆盖的标准主题词（30+）

| subject | 方向 | 单位 | 典型别名 |
|---------|------|------|---------|
| measurement_accuracy | smaller_is_better | ℃ | 测量误差/精度/允差/accuracy |
| display_range | wider_is_better | ℃ | 温度显示范围/量程 |
| operating_temperature | wider_is_better | ℃ | 工作环境温度 |
| storage_temperature | wider_is_better | ℃ | 存储环境温度 |
| display_resolution | smaller_is_better | ℃ | 显示分辨率 |
| service_life | larger_is_better | 年/次 | 产品寿命/使用寿命 |
| battery_life | larger_is_better | 次 | 电池寿命/测量使用次数 |
| product_dimensions | exact_match | mm | 整机外形尺寸 |
| product_weight | exact_match | g | 整机重量/净重 |
| response_time | smaller_is_better | s | 响应时间/测量时间 |
| ip_rating | exact_match | - | 防尘防水/IP等级 |
| fever_alarm_threshold | exact_match | ℃ | 发热报警阈值 |
| humidity_range | wider_is_better | %RH | 相对湿度 |
| pressure_range | wider_is_better | kPa | 大气压力 |
| battery_voltage | exact_match | V | 电池电压 |
| supply_voltage | exact_match | V | 电源电压/供电电压 |
| sleep_current | smaller_is_better | µA | 休眠电流/待机电流 |
| operating_current | smaller_is_better | mA | 工作电流/动态电流 |
| ...（完整列表见 terminology.yaml） |

### 4.3 歧义术语消歧规则

对于"温度"/"湿度"/"压力"/"重量"/"电压"/"尺寸"等需结合上下文消歧后再归一。

### 4.4 单位换算

- °F → ℃：`(F - 32) * 5 / 9`
- in → cm：`in * 2.54`
- mmHg → kPa：`mmHg * 0.133322`

---

## 五、抽取管道详细设计

### 5.1 运行步骤

```bash
# 完整管道执行
python step1_extract_nodes.py   # ~20 min for 10 files（LLM 节点抽取）
python step2_extract_edges.py   # ~7 min（规则+LLM 边抽取）
python step3_generate_claims.py # ~2 min（Claims 生成）
python step4_cross_doc_edges.py # ~5 min（跨文档关系发现）
python merge_results.py         # 即时（合并所有 per_file JSON）
python import_neo4j.py          # ~30s（导入 Neo4j）
python generate_review_html.py  # 即时（生成对比审查 HTML）
```

### 5.2 配置参数

```python
LLM_BASE_URL = "https://ai-gateway.ailab.jiuan.com/v1"
LLM_MODEL = "claude-sonnet-4-6"
MAX_CHUNK_CHARS = 6000
LLM_MAX_TOKENS = 16000
EXCLUDE_FOLDERS = {"历史记录"}
```

### 5.3 文档类型检测逻辑

优先级：文件名关键词 > 目录名匹配 > 通用 fallback

```
"评审"/"检查表" → review_checklist
"检测报告"/"测试报告" → test_report  
"bom"/"组件清单" → bom
目录名映射（01~18 阶段）
文件名其他关键词 → 对应类型
兜底 → general
```

### 5.4 Step4 跨文档关系发现（法规知识引导）

基于 ISO 13485 / ISO 14971 / IEC 62304 / DHF 流程的**法规知识指南**，搜索跨文档关系：

| 关系类型 | 依据标准 | 匹配策略 |
|---------|---------|---------|
| 需求 → 设计输入 追溯 | ISO 13485 7.3.3 | 描述相似度 |
| 设计输入 → 测试 验证 | ISO 13485 7.3.6 | 值+描述匹配 |
| 风险 → 控制措施 缓解 | ISO 14971 7.1 | 同文档内直接匹配 |
| 控制措施 → 测试 验证 | ISO 14971 8 | 关键词匹配 |
| 需求 → 测试 覆盖 | ISO 13485 7.3.6/7 | 值+功能匹配 |
| 软件项 → 测试 验证 | IEC 62304 5.7 | 关键词 |
| 计划任务 → 文档 产出 | ISO 13485 7.3.2 | 名称匹配 |
| DHF条目 → 文档 对应 | DHF Process | 精确+模糊匹配 |
| 法规 → 需求 实现 | ISO 13485 7.1 | 标准号 |
| 法规 → 设计输入 实现 | ISO 13485 7.3.3 | 标准号 |
| 功能 → 测试 验证 | ISO 13485 7.3.6 | 关键词 |
| 人员跨文档身份 | Process | 姓名精确匹配 |

---

## 六、当前进度与成果

### 6.1 已完成

- ✅ POC 可行性验证（3 份文件，验证术语归一化 + 知识图谱可行性）
- ✅ Schema v0.2（21 种节点 + 完整边目录 + 14 类 profile）
- ✅ 术语归一表 v0.4（30+ 标准主题词，全量审计覆盖 470 份语料）
- ✅ 抽取管道 V3（10 个样本文件完整跑通）
- ✅ 跨文档关系发现（379 条关系，12 种类型）
- ✅ Neo4j 图数据库导入与查询验证
- ✅ 对比审查 HTML 生成

### 6.2 当前抽取结果（10 个样本文件）

| 指标 | 数值 |
|------|------|
| 节点总数 | 902 |
| 边总数 | 1183 |
| Claims | 50 |
| Test 节点 | 20 |
| PlanTask 节点 | 128 |
| DocIndexEntry | 112 |
| ReviewItem | 14 |
| SemanticFragment | 161 |
| 跨文档关系 | 379 |

### 6.3 覆盖率分析

| 追溯链 | 覆盖率 |
|--------|--------|
| 需求 → 设计输入 | 88% |
| 需求 → 测试 | 60% |
| 设计输入 → 测试 | 60% |
| 法规 → 需求 | 77% |
| 功能 → 测试 | 151% |

---

## 七、已知问题与待办事项

### 7.1 已解决的核心问题

1. **LLM JSON 解析失败**：完全重写 `try_parse_json`，加入状态机修复未转义字符
2. **巨大文件 Chunk 分割失败**：多级分割策略（标题→表格行→强制按行切割）
3. **文档类型识别错误**：文件名关键词优先于目录名
4. **Neo4j Test 节点属性为空**：修复抽取 + 属性映射

### 7.2 待办事项（按优先级）

| 优先级 | 改进项 | 预期收益 | 工作量 |
|--------|--------|---------|--------|
| P0 | 抽取失败自动重试 + 质量校验 | 避免静默丢失数据 | 0.5天 |
| P0 | 实体去重（Person/Product） | Neo4j 图可用性提升 | 1天 |
| P1 | 跨文件关系推导 | 实现一致性检查的前提 | 2天 |
| P1 | 表格型文件专用 chunk 策略 | 减少 API 调用、提升完整性 | 1天 |
| P2 | LLM 预分类文档类型 | 提升泛化能力 | 0.5天 |
| P2 | SemanticFragment 合并与标签化 | 减少噪音 | 1天 |
| P3 | 抽取覆盖率报告 | 可视化信息损失 | 1天 |
| P3 | 全量文件处理 + 增量更新 | 生产可用 | 2天 |

### 7.3 架构层面的根本问题

1. **过度依赖 LLM 一次性正确输出** → 需要容错层 + 自动重试
2. **Chunk 策略与文档结构脱节** → 需要表格感知的分割
3. **信息抽取的结构化陷阱** → SemanticFragment 兜底 + 粒度控制
4. **关系抽取不足** → 规则引擎 + LLM 双轨 + 跨文件推导
5. **实体去重缺失** → 115 个重复 Person 节点待合并
6. **缺乏质量验证环节** → 需要断言/校验层

---

## 八、环境配置

### 8.1 环境变量（.env）

```
GPT55_API_KEY=***REDACTED-API-KEY***
GPT55_API_URL=https://ai-gateway.ailab.jiuan.com/v1
GPT55_MODEL=claude-sonnet-4-6
DATA_DIR=./data
GPT55_DISABLE_SSL_VERIFY=false
GPT55_ENABLE_VISION=true
```

### 8.2 Python 依赖

```
openai>=1.0.0
pydantic>=2.0.0
instructor>=1.0.0
python-dotenv>=1.0.0
pyyaml>=6.0
neo4j (用于图数据库导入)
```

### 8.3 Neo4j

```bash
docker run -d --name neo4j-poc \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/test1234 \
  neo4j:5-community
```

---

## 九、Cursor 项目记忆与规则

### 9.1 Cursor 规则文件

本项目**未创建** `.cursorrules` 或 `.cursor/rules/` 配置文件。所有项目规则和约定均记录在文档中。

### 9.2 Cursor Plans（历史计划）

| 计划名称 | 最后更新 | 状态 |
|---------|---------|------|
| POC feasibility verification | 2026-06-10 | 已完成 |
| 全量一致性审查 | 2026-06-11 | 进行中 |

### 9.3 Agent 对话历史摘要

项目有 12 次 Agent 对话记录（2026-06-09 ~ 2026-06-12），主要工作线程：

1. **POC 验证阶段**（06-09 ~ 06-10）：用 3 份文件验证 LLM 抽取 + 术语归一化可行性
2. **Schema 设计阶段**（06-10）：从 v0.1 到 v0.2，分类 470 份文件、抽样 42 份、无约束抽取补盲点
3. **管道开发阶段**（06-10 ~ 06-11）：file_extractor V3 完整实现，解决 JSON 解析 bug
4. **跨文档分析阶段**（06-11 ~ 06-12）：step4_cross_doc_edges 实现，法规知识引导的关系发现

---

## 十、核心设计决策记录

### 10.1 为什么用知识图谱而非关系数据库

文件间关系是**网状**的：一条需求对应多个设计输入、一个设计输入受多条法规约束、一个风险需要多个控制措施。图数据库天然适合表达多对多关系，且审查规则本质是"在图上找特定形状的路径"。

### 10.2 为什么 Claim 不合并

两个文件说"精度 ±0.2℃"和"精度 ±0.3℃"——如果合并成一个节点就丢失了冲突信息。所以断言类永远独立，用 CORRESPONDS_TO 边连接，在边上标注 relation（equal/geq/lt）。

### 10.3 为什么 Schema 分 4 层

- 层1（结构）：定位"这条信息在哪个文件哪个章节"
- 层2（锚点）：跨文件去重的关键——同一个产品/人员/编号
- 层3（领域）：承载业务语义的实体
- 层4（裁决）：实际做比对的"卡片"

### 10.4 为什么术语归一表手动维护

LLM 对术语归一不可靠（可能把不同物理量混淆），所以用人工维护的 `terminology.yaml` 作为可信映射，LLM 只负责提取原文。

### 10.5 Schema 的方法论

不是"读完 470 份再设计"，而是"分类 → 抽样 → 无约束抽取 → 回填"：
1. 按文件名关键词把 470 份归入 14 类
2. 每类抽 2-3 份代表（共 42 份）
3. 给 LLM 文档但**不给 schema**，让它自底向上发现字段
4. 对比结果与 v0.1 的缺口，补全为 v0.2

---

## 十一、快速启动指南（给新 AI 助手）

### 你需要知道的最关键信息

1. **这是一个医疗器械 DHF 文档一致性审查系统**，核心是"抽取 → 归一化 → 对齐 → 检查"
2. **Schema 是唯一可信源**：所有改动先改 `schema/schema.yaml` + `schema/edges.yaml`
3. **当前状态**：10 个样本文件已跑通全管道，下一步是全量处理 + 一致性规则编写
4. **核心 Bug 已修复**：JSON 解析、chunk 分割、文档分类
5. **主要待做**：实体去重、质量校验、全量文件处理

### 用户的工作习惯

- 用户偏好先提问确认需求再给方案
- 项目使用 Python 3.11 + Pydantic 2.x
- LLM 调用通过九安内部 AI Gateway（OpenAI 兼容接口）
- 开发环境：Windows 10，Cursor IDE

### 项目关键文件速查

| 需求 | 看哪个文件 |
|------|-----------|
| 系统整体设计 | `需求文档.md`（根目录） |
| 数据模型 | `schema/schema.yaml` + `schema/edges.yaml` |
| 术语归一 | `terminology.yaml` 或 `schema/terminology.yaml` |
| 管道代码 | `file_extractor/step1~4*.py` |
| 当前结果 | `file_extractor/output/cross_doc_report.md` |
| 架构反思 | `file_extractor/ARCHITECTURE_ISSUES.md` |
| 工作总结 | `file_extractor/WORK_SUMMARY.md` |
| 抽取 profile | `schema/profiles.yaml` |

---

*本文档由 Cursor AI 助手自动生成，基于项目目录结构、代码文件、文档内容和 Cursor 历史记录整理。*
