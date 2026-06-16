# 文件抽取管道 V3 工作总结

> 更新日期：2026-06-11
> 项目路径：`D:\项目文档一致性审查\file_extractor\`

---

## 一、完成的工作

### 1.1 核心功能

基于新的 LinkML Schema（`schema.yaml` + `edges.yaml`），构建了完整的三步抽取管道：

| 步骤 | 脚本 | 功能 |
|------|------|------|
| Step 1 | `step1_extract_nodes.py` | 按文档类型使用 LLM 抽取结构化节点 |
| Step 2 | `step2_extract_edges.py` | 规则推导 + LLM 抽取关系边 |
| Step 3 | `step3_generate_claims.py` | 从领域实体生成事实断言 (Claims) |
| Merge | `merge_results.py` | 合并所有 per_file JSON 为 `merged_graph.json` |
| Import | `import_neo4j.py` | 导入 Neo4j 图数据库 |
| Review | `generate_review_html.py` | 生成左右对比审查 HTML |

### 1.2 支持的节点类型 (21 种)

```
Document, Requirement, DesignInput, Risk, RiskControl, 
Function, Regulation, Person, Product, Component,
SoftwareItem, Market, IntendedUse, Identifier, 
PlanTask, Test, TestMeasurement, TestReport, 
ReviewItem, DocIndexEntry, SemanticFragment, RevisionRecord
```

### 1.3 支持的文档类型分类

| doc_type | 适用文件 | 特化策略 |
|----------|---------|----------|
| project_approval | 立项批准书、客户需求书 | 抽取需求、市场、预期用途 |
| dev_plan | 开发计划 | 抽取 PlanTask、资源、质量要求→Fragment |
| risk_analysis | 风险分析报告 | 抽取 Risk + RiskControl |
| design_input | 设计输入 | 抽取 DesignInput 及溯源 |
| test_report | 检测报告/测试报告 | 抽取 Test + TestMeasurement |
| bom | BOM 组件清单 | 抽取 Component |
| review_checklist | 评审检查表 | 抽取 ReviewItem（含未勾选项） |
| software_design | 软件设计文档 | 抽取 SoftwareItem + 架构Fragment |
| dhf_index | DHF清单 | 抽取 DocIndexEntry |
| general | 其他 | 通用抽取 |

### 1.4 最终抽取结果（10 个样本文件）

| 指标 | V1 (初版) | V2 (改进) | V3 (当前) |
|------|-----------|-----------|-----------|
| 节点总数 | ~540 | 437 | **902** |
| 边总数 | 31 | 293 | **1183** |
| Claims | - | 56 | **50** |
| Test 节点 | 0 | 0 | **20** |
| PlanTask 节点 | 0 | 0 | **128** |
| DocIndexEntry | 0 | 0 | **112** |
| ReviewItem | 0 | 0 | **14** |
| SemanticFragment | 1 | 35 | **161** |

---

## 二、遇到的问题及解决方案

### 2.1 LLM 返回 JSON 解析失败（核心 Bug）

**问题描述**：LLM 返回的 JSON 被 `try_parse_json` 解析为空 `{}`，导致多个文件（检测报告、开发计划表、DHF清单、评审检查表）的节点全部丢失。

**根因分析**（三个子问题叠加）：

| # | 子问题 | 具体表现 |
|---|--------|---------|
| 1 | Markdown 代码块包裹 | LLM 返回 ` ```json\n{...}\n``` `，旧代码用 `re.sub` 行级处理不够健壮 |
| 2 | 字符串值内未转义换行符 | JSON 值中出现 literal `\n`，如 `"note": "第一行\n第二行"` |
| 3 | 字符串值内未转义双引号 | LLM 把原文引号带入 JSON 值，如 `"content": "依据为"PT9L标准"进行测试"`，其中 `"PT9L标准"` 的引号未转义 |

**解决方案**：完全重写 `try_parse_json`，加入 `_fix_json_string_issues()` 状态机函数：
- 用正则提取 ` ```json...``` ` 中间的内容
- 状态机逐字符扫描，在 JSON 字符串内部：
  - `\n` → `\\n`，`\r` → `\\r`，`\t` → `\\t`
  - 遇到 `"` 时通过前瞻判断：如果后面紧跟 `:,}]\n` 则视为字符串结束符，否则转义为 `\\"`
- 截断修复：尝试多种闭合后缀

### 2.2 巨大文件 Chunk 分割失败

**问题描述**：`设计开发计划表E0 23.11`（85798 chars）是一个巨大的表格，没有 `## ` 标题，`chunk_text` 无法分割，整体作为一个 chunk 发送给 LLM 导致截断。

**解决方案**：
- 改进 `chunk_text`：增加多级分割策略（`## ` → `# /| ` → 按行强制切割）
- `MAX_CHUNK_CHARS` 从 4000 调到 6000
- 该文件现在被正确分割为 17 个 chunk

### 2.3 文档类型识别优先级错误

**问题描述**：`软件需求规格书评审检查表E0 23.11.via_xlsx.clean.md` 在 `07 软件设计方案` 目录下，被 `detect_doc_type` 优先匹配到 `software_design`，导致使用了错误的 prompt（没有 `review_items` 字段）。

**解决方案**：调整 `detect_doc_type` 优先级——文件名关键词（"评审"/"检查表"/"检测报告"/"BOM"）优先于目录名匹配。

### 2.4 Neo4j Test 节点属性为空

**问题描述**：在 Neo4j 中查询 `MATCH (n:Test) RETURN n.item, n.expected_value` 显示 `UnknownPropertyKeyWarning`。

**根因**：
1. V2 阶段由于 `try_parse_json` bug，Test 节点就没有被正确抽取出来（从源头就是 0 个）
2. `import_neo4j.py` 中 Test 节点的字段映射也有问题

**解决方案**：
1. 修复 `try_parse_json` 后 Test 节点正确抽取（20个）
2. 确认 `import_neo4j.py` 中 Test 属性映射正确（`item`、`expected_value`、`actual_result`、`condition`、`pass_criteria`）

### 2.5 Neo4j 导入其他问题

| 问题 | 解决方案 |
|------|---------|
| Person 节点 name 为 null | 跳过 name 为空的 Person |
| CypherSyntaxError（WHERE 子句位置） | 重排 MATCH/WHERE 顺序 |
| 边匹配率低（931/1183） | 使用 CONTAINS + STARTS WITH 灵活匹配 |

---

## 三、关键文件清单

```
D:\项目文档一致性审查\file_extractor\
├── config.py                  # 配置（API、路径、chunk 大小、文档类型映射）
├── schema.py                  # Pydantic 数据模型
├── step1_extract_nodes.py     # Step1: LLM 节点抽取（含 try_parse_json 修复）
├── step2_extract_edges.py     # Step2: 规则+LLM 边抽取
├── step3_generate_claims.py   # Step3: Claims 生成
├── merge_results.py           # 合并为 merged_graph.json
├── import_neo4j.py            # 导入 Neo4j
├── generate_review_html.py    # 生成对比审查 HTML
└── output/
    ├── per_file/              # 每个文件的独立 JSON 输出
    ├── merged_graph.json      # 合并后的完整图
    └── review_comparison.html # 对比审查页面
```

---

## 四、当前限制与后续建议

| 项目 | 说明 |
|------|------|
| 样本覆盖 | 当前仅跑了 10 个代表性文件，完整 DHF 可能有 50+ 文件 |
| 边匹配率 | Neo4j 导入边成功率 79%（931/1183），因 from/to 标识符匹配不精确 |
| Claims 数量 | 部分文件未生成 Claims（如纯表格型文件），可优化 prompt |
| LLM 耗时 | 设计开发计划表 17 chunks 需要 ~13 分钟，全量跑需预留时间 |
| Person 去重 | 115 个 Person 节点存在大量重复（同一人在不同 chunk 重复出现） |
| SemanticFragment 粒度 | 开发计划表产出 122 个 Fragments，可能过细，考虑合并策略 |

---

## 五、使用方式

```bash
# 完整管道
python step1_extract_nodes.py   # ~20 min for 10 files
python step2_extract_edges.py   # ~7 min
python step3_generate_claims.py # ~2 min
python merge_results.py         # 即时
python import_neo4j.py          # ~30s
python generate_review_html.py  # 即时

# Neo4j 查看
# 浏览器打开 http://localhost:7474
# 用户名: neo4j / 密码: test1234
```
