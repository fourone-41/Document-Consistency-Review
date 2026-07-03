# m-agent Agent Instructions

## Core Collaboration Principles

1. Always address the user as `fourone` at the start of each reply.
2. Ask before uncertain design decisions; do not silently choose a risky architecture.
3. Do not add compatibility branches for old logic unless explicitly requested.

## Project Background

This folder contains the current PT9L DHF/DMR consistency-audit system. The active architecture is a dynamic Orchestrator-led multi-agent flow over converted Markdown documents.

The current flow is:

```text
bootstrap
  -> Project Scout Agent
  -> Orchestrator dynamic dispatch loop
  -> Evidence Gate
  -> Challenge Agent
  -> Context Recovery
  -> Report
```

## Current Architecture Rules

- `routing.yaml` is an Orchestrator policy package, not a deterministic Python router.
- Orchestrator LLM generates `route_plan` and decides which Agent to call next.
- Only Agents assigned by Orchestrator are called.
- Assigned Agents must call the LLM and must not read previous Agent-output cache.
- All Agent calls are recorded in `agent_runs[]`.
- Evidence tools locate context only; they do not create candidates or final errors.
- Candidate Discovery proposes hypotheses only; domain Agents review them.
- Challenge suppresses false positives and can send uncertain items to Context Recovery.

## Common Paths

- Main script: `m-agent/run_pt9l_full_audit_langgraph.py`
- Agent configs: `m-agent/agent_configs/*.yaml`
- Routing policy: `m-agent/agent_configs/routing.yaml`
- Dynamic architecture doc: `m-agent/动态Orchestrator多智能体调度技术文档.md`
- Tests: `m-agent/tests/test_v6_audit_semantics.py`

## Commands

```powershell
python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py
python -X utf8 -m py_compile m-agent/run_pt9l_full_audit_langgraph.py
```
