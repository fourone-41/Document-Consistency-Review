# Conflict And Risk Audit Skill

## Purpose

在知识图谱上查找潜在矛盾、风险链断裂、数值规格不一致、版本漂移、Claim 缺证据、孤立节点等跨文档问题，并输出可人工复核的审查报告。

## Inputs

- Neo4j 图谱。
- canonical links。
- schema 关系定义。
- 审查规则。
- 原始证据。

## Outputs

- `conflict_report_*.md`
- `final_risk_conflict_analysis_*.md`
- `risk_traceability_report_*.md`
- `potential_conflicts_*.cypher`
- `risk_traceability_*.cypher`
- `audit_summary_*.json`

## Audit Dimensions

### 1. 风险闭环

检查：

```text
Risk -> RiskControl -> Test
```

典型问题：

- Risk 没有控制措施。
- RiskControl 没有验证测试。
- RiskControl 找不到上游 Risk。
- 测试存在但关系置信度弱。

### 2. Claim / 数值规格一致性

检查：

- 说明书声明。
- 标签声明。
- 测试报告结果。
- 设计输入规格。

输出候选冲突时必须包含数值、单位、来源和证据。

### 3. 软件版本一致性

检查：

- 软件配置清单。
- 软件验证报告。
- 软件确认报告。
- 发布记录。

典型问题：

- 同一软件项多版本并存。
- 验证报告版本和配置清单版本不一致。
- 文档引用旧版本。

### 4. 法规/说明书证据

检查：

- 标准条款是否有测试或符合性结论。
- 说明书 Claim 是否有证据支撑。
- 标签/包装声明是否与说明书一致。

### 5. 孤立节点

检查：

- 没有 Document 连接的节点。
- 没有任何业务关系的高价值节点。
- 有关系但无法连到主审查链的节点。

## Workflow

1. 先跑确定性 Cypher 查询。
2. 对候选问题按类型分组。
3. 对每组绑定证据链。
4. 区分：
   - confirmed_issue
   - candidate_issue
   - information_gap
5. 输出 Markdown 报告。
6. 同时输出 JSON/HTML 数据供可视化使用。

## Current Project Artifacts

```text
_convert/company_full_run/audit/conflict_report_company_full_v2.md
_convert/company_full_run/audit/final_risk_conflict_analysis_company_full_v2.md
_convert/company_full_run/audit/risk_traceability_report_company_full_v2.md
_convert/company_full_run/audit/audit_summary_company_full_v2.json
_convert/company_full_run/audit/potential_conflicts_company_full_v2.cypher
_convert/company_full_run/audit/risk_traceability_company_full_v2.cypher
```

## Guardrails

- 不能瞎审查，所有规则必须能解释。
- “缺关系”不等于“真实缺证据”，可能是抽取漏掉。
- 报告中必须标注 evidence confidence。
- 不能只看风险法规，要覆盖数值、版本、Claim、孤立节点等维度。
- 最终报告必须说清楚哪里矛盾、为什么矛盾、证据在哪里、是否需要人工确认。
