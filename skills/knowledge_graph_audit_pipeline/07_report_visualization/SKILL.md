# Report And Visualization Skill

## Purpose

把知识图谱审查结果输出为人能看懂、能复核、能演示的 Markdown/HTML/JSON 报告和可视化看板。

## Inputs

- finding JSON。
- conflict report。
- risk traceability report。
- graph query results。
- evidence links。
- Neo4j 节点/关系。

## Outputs

- 全维度审查总览 HTML。
- 风险链条审查 HTML。
- Markdown 审查报告。
- JSON 数据文件。
- 可导入/复现的 Cypher。

## Current Project Artifacts

```text
_convert/company_full_run/audit/full_audit_view/index.html
_convert/company_full_run/audit/full_audit_view/full_audit_data.json
_convert/company_full_run/audit/risk_chain_view/board.html
_convert/company_full_run/audit/risk_chain_view/risk_chain_audit_data.json
_convert/company_full_run/audit/conflict_report_company_full_v2.md
_convert/company_full_run/audit/final_risk_conflict_analysis_company_full_v2.md
```

## Report Structure

推荐报告包含：

1. 总览摘要。
2. 数据范围：
   - 文档数。
   - 节点数。
   - 关系数。
   - 抽取失败数。
3. 问题分类：
   - 风险闭环。
   - 数值规格。
   - 软件版本。
   - Claim/说明书/标签。
   - 孤立节点。
   - schema / extraction 信息缺口。
4. 每条问题：
   - issue_id
   - type
   - severity
   - status
   - source documents
   - involved nodes
   - involved relations
   - evidence
   - recommendation
5. 人工复核建议。

## Visualization Requirements

- 高风险链条用红色标记。
- 候选问题用橙色。
- 信息缺口用灰色。
- 点击问题能看到证据和节点链条。
- 不要一次把 1w 节点直接铺满页面，必须有筛选、分组和聚焦视图。
- 全图可以给总览，审查必须给子图和链条视图。

## Guardrails

- 报告不能只输出模型结论，要输出证据。
- 可视化不能为了炫而牺牲可读性。
- 红色只表示待复核风险，不表示最终定罪。
- HTML 应该尽量自包含，方便发给 mentor 或业务方。
