# Schema Discovery Skill

## Purpose

从全量文档中发现当前 schema 覆盖不到的节点类型、关系类型、术语、profile 和字段缺口，并生成可人工定夺的 gap 报告。

## Inputs

- 文档集合。
- 当前 schema：
  - `schema/schema.yaml`
  - `schema/edges.yaml`
  - `schema/profiles.yaml`
  - `schema/terminology.yaml`
  - `schema/models.py`
- 规则扫描结果，例如 `_convert/rule_llm_qwen/rule_scan.json`。
- LLM schema discovery 输出，例如 `_convert/rule_llm_qwen/schema_discovery_qwen.json`。

## Outputs

- `schema_discovery_*.json`
- `schema_discovery_*.md`
- `gap_report.md`
- `gap_report_clustered_review.md`
- 推荐新增/修改的 YAML 项。

## Method

1. 先跑规则扫描，覆盖高频确定性模式。
2. 将规则无法覆盖、分类为 long tail 的文档交给 LLM。
3. LLM 不直接改 schema，只输出候选：
   - node_candidates
   - edge_candidates
   - terminology_candidates
   - profile_candidates
   - field_candidates
4. 对候选按语义和频率聚类。
5. 输出人工定夺报告，按优先级排序。
6. 人工确认后，再更新 YAML 和 `models.py`。

## Review Criteria

新增 schema 需要满足：

- 是否多文档复用。
- 是否对应真实业务概念。
- 是否能稳定从文档中抽取。
- 是否能参与后续关系审查。
- 是否已有相近类型可以承载。

## Current Project Artifacts

```text
_convert/rule_llm_qwen/rule_scan.json
_convert/rule_llm_qwen/long_tail_queue.json
_convert/rule_llm_qwen/schema_discovery_qwen.json
_convert/rule_llm_qwen/schema_discovery_qwen.md
_convert/rule_llm_qwen/gap_report.md
_convert/rule_llm_qwen/gap_report_clustered_review.md
```

## Guardrails

- LLM 输出只是候选，不直接进入正式 schema。
- “其他”过多说明 schema 或 prompt 需要迭代。
- 低频但高风险概念可以保留，但要标注适用范围。
- 不要为单个偶然表述创建过细 schema。
