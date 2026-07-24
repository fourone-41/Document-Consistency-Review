# Canonical Node Merge Skill

## Purpose

识别跨文档中确定指向同一对象的节点，建立 canonical link 或聚合层，减少重复节点，同时避免错误合并。

## Inputs

- Neo4j 图谱。
- 节点属性。
- 文档来源。
- 名称、编号、版本、物料号、测试编号等匹配键。

## Outputs

- canonical link Cypher。
- canonical group 报告。
- 需要人工确认的候选合并列表。

## What Can Be Merged

可以考虑合并：

- 同一份文档的不同文件名引用。
- 同一物料号 / BOM item。
- 同一测试编号 / 测试报告。
- 同一软件版本项。
- 同一风险编号。
- 同一设计输入编号。
- 同一法规条款编号。

## What Must Not Be Auto-Merged

- Claim 不自动合并。
- 只有相似文本但无编号/证据支撑的节点不合并。
- 语义相近但可能来自不同文档上下文的 ReviewItem 不合并。
- candidate relation 不能作为强合并证据。

## Merge Strategy

推荐使用 canonical link，而不是直接删除节点：

```text
(n)-[:CANONICAL_OF {reason, confidence, evidence}]->(c:CanonicalNode)
```

或者：

```text
(n1)-[:SAME_AS_CONFIRMED]->(n2)
```

## Workflow

1. 先用确定性 key 匹配：
   - document_id
   - risk_id
   - test_id
   - material_no
   - software_version
   - standard_clause
2. 再用严格规则归一化名称。
3. 输出候选组。
4. 对高风险合并进入人工确认。
5. 只对 confirmed 组写入 canonical link。
6. 审查前查询时优先使用 canonical group，但原始节点保留。

## Current Project Artifact

```text
_convert/company_full_run/audit/canonical_links_company_full_v2.cypher
```

## Guardrails

- 聚合是审查辅助层，不是销毁原始证据。
- Claim 不合并是硬规则。
- 弱相似只进入候选，不进入 confirmed。
- 每个 canonical group 必须有 reason。
