# Knowledge Graph Audit Pipeline Skills

这组 Skill 沉淀的是从 DHF/DMR 文档到知识图谱，再到跨文档矛盾审查报告的完整链路。

它们不是一次性脚本说明，而是可复用方法资产。后续可以接入 Agent Workbench 的 Capability / Skill Registry。

## Pipeline

```text
文档集合
-> Schema Discovery
-> 节点/关系抽取
-> 抽取质量恢复
-> Neo4j 图谱导入
-> Canonical Node 聚合
-> Conflict / Risk Audit
-> Report & Visualization
```

## Skills

| 目录 | Skill | 作用 |
| --- | --- | --- |
| `00_end_to_end_orchestrator` | KG 全链路总编排 | 串起全流程，定义阶段闸门 |
| `01_schema_discovery` | Schema 发现与补全 | 从文档中发现 node/edge/profile/terminology gap |
| `02_extraction` | 全量节点关系抽取 | 按 schema 抽取节点、关系、证据 |
| `03_extraction_quality_recovery` | 抽取质量恢复 | 补跑失败文件、修复 raw JSON、统计覆盖率 |
| `04_graph_import` | Neo4j 图谱导入 | 生成/执行 Cypher，导入文档、节点、关系 |
| `05_canonical_merge` | 确定同一节点聚合 | 对确定同一实体做 canonical link，不合并 Claim |
| `06_conflict_audit` | 矛盾与风险关系审查 | 查数值、版本、风险链、孤立节点等问题 |
| `07_report_visualization` | 报告与可视化 | 输出 HTML/Markdown/JSON 可读审查产物 |

## Current Project Artifacts

当前项目中已有的全量图谱与审查产物主要位于：

```text
D:\driven-ai\_convert\company_full_run
D:\driven-ai\_convert\company_full_run\audit
D:\driven-ai\_convert\company_full_run\neo4j
```

关键产物：

- `audit/full_audit_view/index.html`
- `audit/full_audit_view/full_audit_data.json`
- `audit/conflict_report_company_full_v2.md`
- `audit/final_risk_conflict_analysis_company_full_v2.md`
- `audit/risk_traceability_report_company_full_v2.md`
- `audit/risk_chain_view/board.html`
- `neo4j/import_company_full_v2.cypher`

## Non-Negotiable Rules

- Claim 不自动聚合。
- 只有确定同一对象、同一物料、同一测试、同一软件项、同一文档时才建立 canonical link。
- 候选关系不能写成最终事实。
- 候选矛盾不能写成最终矛盾，必须保留证据和人工确认状态。
- 所有 finding 必须可追溯到文档、节点、关系或 evidence。
- Schema 发现、节点抽取、矛盾审查要分阶段保存中间产物，避免一次失败全链路不可恢复。
