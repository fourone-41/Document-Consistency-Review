# Neo4j Graph Import Skill

## Purpose

把抽取出的文档、节点、关系导入 Neo4j，生成可查询、可审查、可视化的知识图谱。

## Inputs

- extraction JSON 文件。
- schema 中的 node labels 和 edge types。
- Neo4j 连接配置。
- 可选：pilot 名称，例如 `company_full_v2`。

## Outputs

- Neo4j Cypher 导入脚本。
- 导入统计。
- Document 节点。
- Entity 节点。
- Evidence/关系属性。

## Current Project Artifacts

```text
_convert/company_full_run/neo4j/import_company_full_v2.cypher
_convert/company_full_run/audit/risk_traceability_company_full_v2.cypher
_convert/company_full_run/audit/canonical_links_company_full_v2.cypher
_convert/company_full_run/audit/potential_conflicts_company_full_v2.cypher
```

## Import Model

推荐至少包含：

```text
(d:Document)
(n:Risk | RiskControl | Test | Claim | SoftwareItem | ReviewItem | ...)
(d)-[:CONTAINS]->(n)
(n)-[:RELATION {confidence, evidence, source_doc}]->(m)
```

## Workflow

1. 读取 extraction JSON。
2. 为每个源文件创建 Document 节点。
3. 为每个抽取节点生成稳定 node_key。
4. 为每条关系生成 relation_key。
5. 关系属性保留：
   - source_file
   - evidence
   - confidence
   - extraction_method
   - pilot/run_id
6. 输出 Cypher。
7. 导入 Neo4j。
8. 运行统计查询，核对 Document、节点、关系数量。

## Validation Queries

示例：

```cypher
MATCH (d:Document {pilot:'company_full_v2'})
RETURN count(d);

MATCH (n {pilot:'company_full_v2'})
RETURN labels(n), count(n)
ORDER BY count(n) DESC;

MATCH ()-[r {pilot:'company_full_v2'}]->()
RETURN type(r), count(r)
ORDER BY count(r) DESC;
```

## Guardrails

- 不要把所有节点都变成同一种 GenericNode。
- 不要丢失 source document。
- 不要在导入阶段做模糊聚合。
- 候选关系必须保留 confidence。
- 导入前最好生成脚本，方便审计和回滚。
