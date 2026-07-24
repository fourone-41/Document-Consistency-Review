# KG Audit End-to-End Orchestrator Skill

## Purpose

把医疗器械 DHF/DMR 文档从原始 Markdown/JSON 语料，编排成完整知识图谱，并输出跨文档审查报告。

使用场景：

- 用户要“全量知识图谱”。
- 用户要“从抽节点到建图再到矛盾报告”。
- 用户要复用之前 PT9L / company_full_run 的完整链路。
- 用户要把流程接入 Agent Workbench。

## Inputs

- 文档集合目录，例如 `清洗后md文件/` 或转换后的 JSON/Markdown 目录。
- Schema 文件：
  - `schema/schema.yaml`
  - `schema/edges.yaml`
  - `schema/profiles.yaml`
  - `schema/terminology.yaml`
  - `schema/models.py`
- LLM 配置，例如 `.env` 中的公司网关或模型配置。
- 可选：已有抽取结果目录，例如 `_convert/company_full_run/extractions/`。

## Outputs

- Schema gap 报告。
- 节点/关系抽取 JSON。
- Neo4j Cypher 导入脚本。
- Canonical link Cypher。
- 潜在冲突 Cypher。
- 风险链条审查报告。
- 全维度审查看板。
- 最终矛盾分析文档。

## Workflow

1. 运行 schema discovery，确认当前 schema 是否覆盖文档里的主要实体和关系。
2. 对 gap 做聚类和人工定夺，更新 YAML 和模型定义。
3. 按最新 schema 抽取所有文档节点和关系。
4. 对失败文件、空抽取文件、超长规则型文件进行恢复和补跑。
5. 生成 Neo4j 导入脚本并导入图数据库。
6. 建立 canonical link，只聚合确定同一对象。
7. 运行跨文档审查：
   - 风险闭环
   - 数值规格
   - 软件版本
   - Claim 证据
   - 孤立节点
   - 关系断链
8. 输出 Markdown/JSON/HTML 报告。
9. 所有候选问题进入人工审核，不直接写成最终结论。

## Stage Gates

- Schema gate：新增 schema 后必须能被 YAML 和 `models.py` 表达。
- Extraction gate：每份文档必须有抽取状态，不能静默漏掉。
- Graph gate：Neo4j 导入后节点数、关系数、Document 数要可核对。
- Merge gate：Claim 不合并，弱相似不合并。
- Audit gate：每条矛盾必须有证据路径、节点、关系或原文引用。

## Current Project Paths

```text
_convert/rule_llm_qwen/schema_discovery_qwen.json
_convert/rule_llm_qwen/gap_report_clustered_review.md
_convert/company_full_run/extractions/
_convert/company_full_run/neo4j/import_company_full_v2.cypher
_convert/company_full_run/audit/conflict_report_company_full_v2.md
_convert/company_full_run/audit/full_audit_view/index.html
```

## Guardrails

- 不要把“没有找到证据”直接写成“没有证据存在”，应写成 information_gap。
- 不要把 LLM 抽取失败当成文档没有内容。
- 不要为了让图更连通而强行聚合节点。
- 不要把候选边当作强事实边。
