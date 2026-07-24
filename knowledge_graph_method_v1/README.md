# Knowledge Graph Method V1

This folder is the entry point for the earlier knowledge-graph-centered method.
It keeps V1 separate from the new V2 experience/skill database direction.

## Positioning

V1 answers: how do we model document relationships as explicit entities and
edges so agents can trace upstream and downstream evidence?

Core ideas:

- Document nodes: DHF/DMR files, reports, drawings, BOMs, labels, risk files.
- Entity nodes: requirements, parameters, risks, controls, tests, versions,
  materials, standards, people, signatures.
- Edges: derives_from, verifies, controls, references, conflicts_with,
  same_as, version_of, owned_by.
- Queries: trace a review point upstream and downstream, find missing edges,
  detect contradictions across linked files.

## Assets Already In Workspace

These files and folders belong to the V1 family and should be treated as
reference assets, not as the current product runtime:

- `../NEO4J_SETUP.md`
- `../scripts/start_neo4j.ps1`
- `../scripts/import_neo4j.ps1`
- `../_convert/build_company_batch_neo4j.py`
- `../_convert/build_company_pilot_neo4j.py`
- `../_convert/build_test_record_neo4j.py`
- `../_convert/build_test_record_kg.py`
- `../pilot_3files/kg_view.html`
- `../pilot_3files/company_llm_pilot/kg_test_record/kg_test_record.html`
- `../schema/`

## Relationship To V2

V1 is not discarded. It becomes one reusable method inside V2:

- Skill: knowledge-graph trace review.
- Experience: when a point is found, trace upstream source, downstream
  verification, and lateral contradictions.
- Tool candidate: Neo4j query or graph extraction tool.

V2 should call V1 only when the task benefits from explicit multi-hop trace
paths. The Orchestrator should not force every project into KG first.

