# Agent YAML Config Split Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move each audit agent's retrieval strategy, input schema, output schema, and routing rules out of `m-agent/run_pt9l_full_audit_langgraph.py` into editable YAML files.

**Architecture:** Add `m-agent/agent_configs/` with one YAML per agent plus `routing.yaml`. The Python script loads those YAML files at runtime, builds task packages from config, and uses `routing.yaml` for mandatory audit matrix and candidate-to-agent routing.

**Tech Stack:** Python 3.11, PyYAML 6.0.3, LangGraph, pytest.

## Global Constraints

- Scope is limited to `m-agent/` code and config, plus this implementation plan.
- Each agent gets its own YAML file.
- `routing.yaml` owns routing rules and mandatory audit matrix.
- Tools only provide evidence context; agents decide candidate hypotheses.
- No old mechanical-review compatibility branches.

---

### Task 1: Config Files And Loaders

**Files:**
- Create: `m-agent/agent_configs/*.yaml`
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Produces: `load_agent_config(agent_id: str) -> dict`
- Produces: `load_routing_config() -> dict`
- Produces: `DOMAIN_AGENT_IDS: dict[str, str]`

- [x] **Step 1: Write failing tests**

Add tests that require YAML loading and routing matrix construction from config.

- [x] **Step 2: Verify tests fail**

Run: `python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`

- [x] **Step 3: Implement config files and loaders**

Create YAML files and add loader helpers using `yaml.safe_load`.

- [x] **Step 4: Verify tests pass**

Run: `python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`

### Task 2: Agent Task Construction From YAML

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Produces: `build_agent_task_from_config(config: dict, evidence: list[dict], **overrides) -> dict`
- Produces: `build_domain_agent_specs() -> dict[str, dict]`

- [x] **Step 1: Write failing tests**

Add tests that ensure the Hardware Agent task uses YAML role, goal, retrieval patterns, input schema, and output schema.

- [x] **Step 2: Verify tests fail**

Run: `python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`

- [x] **Step 3: Implement task builder and update scout/candidate/domain nodes**

Replace hard-coded role/goal/schema blocks with YAML-driven task construction.

- [x] **Step 4: Verify tests pass**

Run: `python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`

### Task 3: Routing From YAML

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Modify: `m-agent/agent_configs/routing.yaml`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Updates: `build_mandatory_audit_matrix(project_profile: dict) -> list[dict]`
- Updates: `route_candidate_discovery_results(candidates, mandatory_audit_matrix, routing_config=None) -> dict[str, list[dict]]`

- [x] **Step 1: Write failing tests**

Add tests that assert matrix and candidate routing are sourced from `routing.yaml`.

- [x] **Step 2: Verify tests fail**

Run: `python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`

- [x] **Step 3: Implement routing config usage**

Replace hard-coded matrix and candidate-type expansion with YAML rules.

- [x] **Step 4: Verify tests pass and graph compiles**

Run:
`python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py`
`python -X utf8 -c "import run_pt9l_full_audit_langgraph as m; m.build_graph(); print('graph compiled')"`
