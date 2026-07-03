# Agent-Led Candidate Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current mechanical word-list candidate-generation narrative with an Agent-led candidate discovery architecture while preserving Orchestrator stage-axis and dimension-axis coverage.

**Architecture:** The updated design keeps Orchestrator as the audit coordinator. `Project Scout Agent` builds the project profile, Orchestrator generates a mandatory audit task matrix from lifecycle stages and cross-cutting dimensions, `Candidate Discovery Agent` performs open-ended semantic candidate discovery inside assigned document packages, then `Orchestrator Candidate Router` standardizes, deduplicates, merges, binds, and routes those candidates to one or more domain agents. Domain agents perform final professional review. PageIndex, full-text search, file reading, and Relation Index remain evidence-location tools only; they do not decide candidate existence.

**Tech Stack:** Markdown technical documentation, static HTML visualization, Python LangGraph audit pipeline, GPT55/OpenAI-compatible LLM calls, pytest.

## Global Constraints

- Address the user's concern that fixed word-list matching looks result-driven and may miss semantic issues.
- Do not remove the original Orchestrator stage-axis and dimension-axis audit coverage.
- Do not let a pattern-matching tool directly decide candidate findings.
- Keep PageIndex, full-text search, file reading, and Relation Index as evidence retrieval and location capabilities.
- Keep the architecture multi-agent oriented, not a rigid workflow-only design.
- Do not add compatibility branches for old logic unless explicitly requested.
- For code changes, use TDD: add failing tests first, then minimal implementation, then verification.

---

## Target File Structure

### Documentation

- Modify: `m-agent/最新多智能体DHF-DMR一致性审查技术文档.md`
  - Replace "mechanical layer / preset word-list" wording with Agent-led candidate discovery.
  - Rename `Scout Agent` to `Project Scout Agent`.
  - Add Orchestrator dual-track task generation: mandatory audit matrix plus discovery candidates.
  - Add Orchestrator Candidate Router: route discovery candidates back through Orchestrator before domain review.
  - Add Context Recovery round-by-round evidence expansion design.

- Modify: `m-agent/最新多智能体DHF-DMR流程架构可视化.html`
  - Update architecture diagram labels and flow.
  - Remove visual emphasis on mechanical word-list scanning.
  - Add `Project Scout Agent`, `Candidate Discovery Agent`, `Orchestrator Candidate Router`, mandatory audit matrix, and evidence retrieval tools.

- Optionally modify if still used by the team: `multiagent/最新多智能体DHF-DMR一致性审查技术文档.md` and `multiagent/最新多智能体DHF-DMR流程架构可视化.html`
  - Only if those files remain part of the current deliverable set. Current source of truth should be `m-agent/`.

### Code

- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
  - Replace mechanical candidate generation as a direct candidate source with Agent-led candidate discovery.
  - Keep deterministic extractors as evidence retrieval helpers only.
  - Add candidate discovery node and data contracts.
  - Add candidate routing node and routed review package contracts.
  - Preserve Orchestrator stage-axis and dimension-axis task packages.

- Modify: `m-agent/tests/test_v6_audit_semantics.py`
  - Add tests for `Project Scout Agent` profile output normalization.
  - Add tests for Orchestrator mandatory audit matrix generation.
  - Add tests that pattern/tool evidence does not directly become final candidates.
  - Add tests for Candidate Discovery Agent output contract.
  - Add tests for Orchestrator Candidate Router routing without confirm/dismiss decisions.
  - Add tests for Context Recovery progressive evidence rounds.

### Outputs

- Future output root after implementation: `magent-output/pt9l_full_audit_output_langgraph_v8/`
  - This should be used for the first full run after code changes to avoid mixing v7 and v8 semantics.

---

### Task 1: Update The Technical Design Language

**Files:**
- Modify: `m-agent/最新多智能体DHF-DMR一致性审查技术文档.md`

**Interfaces:**
- Consumes: Current confirmed design direction from this conversation.
- Produces: A revised design document that no longer says fixed word-list scanning decides candidates.

- [ ] **Step 1: Find all mechanical-word-list wording**

Run:

```powershell
rg -n "机械|词表|预设|逐词|模式匹配|Mechanical|mechanical|候选" m-agent
```

Expected:

- Locations in the technical document that describe mechanical candidate generation.
- Locations in the HTML may also appear; leave HTML for Task 2.

- [ ] **Step 2: Replace the old mechanical-layer framing**

Replace wording equivalent to:

```text
机械层遍历所有 Markdown 文件的每一行，在预设词表中逐词匹配并生成候选。
```

With:

```text
系统不再由固定词表或模式匹配工具直接生成候选。候选发现改为 Agent-led Candidate Discovery：Project Scout Agent 先建立项目画像，Orchestrator 基于阶段轴和维度轴生成必查任务矩阵，Candidate Discovery Agent 在文档包中进行语义候选发现，并按需调用 PageIndex、全文检索、文件读取和 Relation Index 补充证据。工具只负责定位和取证，不负责判断候选是否存在。
```

- [ ] **Step 3: Add the new role definition**

Add this role definition near the agent list:

```markdown
### Project Scout Agent

Project Scout Agent 是项目侦察与画像智能体，承接原 Scout Agent 的市场/品类/法规基线能力，并扩展为项目级画像建立者。它负责识别目标型号、产品族线索、主审范围、辅助范围、文件编号体系、文档阶段分布、关键实体、法规/品类基线和候选发现提示。它不直接判定错误，也不直接输出最终 Finding。
```

- [ ] **Step 4: Add Candidate Discovery Agent definition**

Add:

```markdown
### Candidate Discovery Agent

Candidate Discovery Agent 是候选发现智能体。它读取 Orchestrator 分配的文档包，结合 Project Scout Agent 输出的项目画像，主动发现潜在一致性问题。它可以调用 PageIndex、全文检索、文件读取和 Relation Index 获取证据，但这些工具只返回证据位置和上下文，不直接生成候选。Candidate Discovery Agent 输出的是候选假设，不是确认错误；候选必须回到 Orchestrator Candidate Router，再分派给领域 Agent。
```

- [ ] **Step 5: Add dual-track Orchestrator design**

Add:

```markdown
Orchestrator 的任务生成采用双轨机制：

1. 规划性审查任务：基于阶段轴和维度轴生成必查任务矩阵，保证生命周期闭环和横向维度覆盖。
2. 发现性候选任务：将同一批文档包交给 Candidate Discovery Agent 进行开放式语义候选发现，用于补充规划性任务之外的异常线索。

Candidate Discovery Agent 输出的候选先回到 Orchestrator Candidate Router。Router 负责候选标准化、去重、合并、字段完整性检查、绑定必查任务矩阵、分派一个或多个领域 Agent，并生成复审问题；Router 不做 confirm/dismiss，不直接输出 finding。两类输入会被合并为统一的 routed review package，再分派给领域 Agent 复审。
```

- [ ] **Step 6: Add Context Recovery round design**

Add:

```markdown
Context Recovery 不重复运行同一 prompt，而是逐轮扩大证据范围：

1. 第 1 轮：补充原证据邻近上下文，包括当前行前后文、表格完整行列、小节标题和文件基本信息。
2. 第 2 轮：补充同实体跨文件上下文，包括同一型号、料号、参数、文件编号、需求编号或风险编号的全项目出现位置。
3. 第 3 轮：补充生命周期上下游上下文，包括设计输入到输出、风险到控制到验证、BOM 到工艺到检验等链路。
4. 第 4 轮：补充受控状态和版本上下文，包括封面、修订历史、签批页、文件清单、变更记录和归档/废止信息。
5. 第 5 轮：补充反证和人工复核包，包括支持 confirm 的证据、支持 dismiss 的证据、仍缺证据和人工复核建议。
```

- [ ] **Step 7: Verify document wording**

Run:

```powershell
rg -n "预设词表|逐词匹配|机械层遍历|固定词表直接生成候选" m-agent/最新多智能体DHF-DMR一致性审查技术文档.md
```

Expected:

- No wording that says fixed word lists directly decide candidates.
- It is acceptable to mention old wording only as "被替换/不再采用".

---

### Task 2: Update The Visualization Page

**Files:**
- Modify: `m-agent/最新多智能体DHF-DMR流程架构可视化.html`

**Interfaces:**
- Consumes: Updated terminology from Task 1.
- Produces: A visual architecture page matching the Agent-led candidate discovery design.

- [ ] **Step 1: Locate old labels**

Run:

```powershell
rg -n "Scout|Mechanical|机械|词表|Candidate|Context Recovery|Orchestrator" m-agent/最新多智能体DHF-DMR流程架构可视化.html
```

Expected:

- Current architecture labels and section IDs.

- [ ] **Step 2: Rename Scout**

Replace user-facing labels:

```text
Scout Agent
Market & Category Scout Agent
```

With:

```text
Project Scout Agent
```

- [ ] **Step 3: Add Candidate Discovery Agent lane**

Add a new lane/card with this content:

```html
<h3>Candidate Discovery Agent</h3>
<p>基于项目画像和文档包进行语义候选发现；可调用 PageIndex、全文检索、文件读取和 Relation Index 补证，但工具不直接决定候选。</p>
```

- [ ] **Step 4: Rename mechanical tool area**

Replace mechanical-candidate wording with:

```text
Evidence Retrieval Tools
PageIndex / 全文检索 / 文件读取 / Relation Index
仅定位证据，不决定候选
```

- [ ] **Step 5: Add dual-track flow visual**

Represent:

```text
Project Scout Agent
  -> Orchestrator
      -> 必查任务矩阵（阶段轴 × 维度轴）
      -> Candidate Discovery Agent（开放式候选发现）
      -> Orchestrator Candidate Router（候选路由治理）
  -> Domain Review Agents
  -> Evidence Gate
  -> Challenge Agent
  -> Context Recovery
  -> Report
```

- [ ] **Step 6: Validate layout from disk**

Run:

```powershell
rg -n "Project Scout Agent|Candidate Discovery Agent|Evidence Retrieval Tools|必查任务矩阵" m-agent/最新多智能体DHF-DMR流程架构可视化.html
```

Expected:

- All four phrases appear.

---

### Task 3: Introduce Candidate Discovery Data Contracts In Code

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Produces: `project_profile`, `mandatory_audit_matrix`, `candidate_discovery_results`.
- Consumes later: domain review packages.

- [ ] **Step 1: Write failing test for project profile normalization**

Add to `m-agent/tests/test_v6_audit_semantics.py`:

```python
def test_project_scout_profile_normalizes_project_identity():
    raw = {
        "agent": "Project Scout Agent",
        "project_profile": {
            "target_model": "PT9L",
            "product_family": ["PT9"],
            "document_id_patterns": ["PT9L-*", "IFT-*"],
            "primary_scope_rules": ["exclude archived folders"],
        },
    }

    profile = audit.normalize_project_profile(raw)

    assert profile["target_model"] == "PT9L"
    assert "PT9" in profile["product_family"]
    assert "PT9L-*" in profile["document_id_patterns"]
    assert profile["profile_source"] == "Project Scout Agent"
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_project_scout_profile_normalizes_project_identity
```

Expected:

- FAIL because `normalize_project_profile` does not exist.

- [ ] **Step 3: Implement minimal normalizer**

Add to `m-agent/run_pt9l_full_audit_langgraph.py`:

```python
def normalize_project_profile(raw: dict) -> dict:
    profile = raw.get("project_profile") if isinstance(raw.get("project_profile"), dict) else {}
    return {
        "profile_source": "Project Scout Agent",
        "target_model": str(profile.get("target_model") or ""),
        "product_family": profile.get("product_family") if isinstance(profile.get("product_family"), list) else [],
        "document_id_patterns": profile.get("document_id_patterns") if isinstance(profile.get("document_id_patterns"), list) else [],
        "primary_scope_rules": profile.get("primary_scope_rules") if isinstance(profile.get("primary_scope_rules"), list) else [],
        "key_entities": profile.get("key_entities") if isinstance(profile.get("key_entities"), dict) else {},
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_project_scout_profile_normalizes_project_identity
```

Expected:

- PASS.

---

### Task 4: Add Orchestrator Mandatory Audit Matrix

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Consumes: `project_profile`, manifest/readiness/page_index summaries.
- Produces: `mandatory_audit_matrix: list[dict]`.

- [ ] **Step 1: Write failing test**

Add:

```python
def test_orchestrator_builds_stage_dimension_audit_matrix():
    profile = {"target_model": "PT9L"}
    matrix = audit.build_mandatory_audit_matrix(profile)

    keys = {(row["stage_axis"], row["dimension_axis"], row["assigned_agent"]) for row in matrix}
    assert ("design_input_to_output", "parameter_consistency", "Hardware Agent") in keys
    assert ("risk_to_verification", "risk_traceability", "Risk Traceability Agent") in keys
    assert ("software_lifecycle", "software_traceability", "Software Agent") in keys
    assert ("dmr_chain", "dmr_sop_consistency", "DMR/SOP Agent") in keys
    assert ("all_stages", "document_control", "Regulatory Agent") in keys
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_orchestrator_builds_stage_dimension_audit_matrix
```

Expected:

- FAIL because `build_mandatory_audit_matrix` does not exist.

- [ ] **Step 3: Implement minimal matrix**

Add:

```python
def build_mandatory_audit_matrix(project_profile: dict) -> list[dict]:
    target_model = project_profile.get("target_model", "")
    return [
        {
            "matrix_id": "MATRIX-001",
            "stage_axis": "design_input_to_output",
            "dimension_axis": "parameter_consistency",
            "assigned_agent": "Hardware Agent",
            "check_goal": f"确认 {target_model} 设计输入中的关键参数是否被设计输出承接，并与验证条件保持一致。",
        },
        {
            "matrix_id": "MATRIX-002",
            "stage_axis": "risk_to_verification",
            "dimension_axis": "risk_traceability",
            "assigned_agent": "Risk Traceability Agent",
            "check_goal": "确认风险、控制措施和验证活动之间是否形成闭环。",
        },
        {
            "matrix_id": "MATRIX-003",
            "stage_axis": "software_lifecycle",
            "dimension_axis": "software_traceability",
            "assigned_agent": "Software Agent",
            "check_goal": "确认软件需求、软件设计、软件测试和软件确认之间是否可追溯。",
        },
        {
            "matrix_id": "MATRIX-004",
            "stage_axis": "dmr_chain",
            "dimension_axis": "dmr_sop_consistency",
            "assigned_agent": "DMR/SOP Agent",
            "check_goal": "确认 BOM、工艺、检验、包装和标签文件之间是否一致。",
        },
        {
            "matrix_id": "MATRIX-005",
            "stage_axis": "all_stages",
            "dimension_axis": "document_control",
            "assigned_agent": "Regulatory Agent",
            "check_goal": "确认全阶段文件版本、签批、评审记录和受控状态是否完整一致。",
        },
    ]
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_orchestrator_builds_stage_dimension_audit_matrix
```

Expected:

- PASS.

---

### Task 5: Add Candidate Discovery Agent Output Contract

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Consumes: LLM output from Candidate Discovery Agent.
- Produces: normalized candidate rows for domain review.

- [ ] **Step 1: Write failing test**

Add:

```python
def test_candidate_discovery_normalizes_agent_candidates():
    raw = {
        "agent": "Candidate Discovery Agent",
        "candidates": [
            {
                "candidate_type": "product_identity_inconsistency",
                "claim": "BOM 中出现疑似非 PT9L 料号。",
                "why_suspicious": "出现在主审范围 BOM，且与目标型号命名不一致。",
                "recommended_agent": "Hardware Agent",
                "confidence": "medium",
                "evidence_refs": [{"rel_path": "bom.md", "line": 3, "source_text": "PT9C-CNTP01"}],
                "missing_context": ["设计输出清单", "变更记录"],
            }
        ],
    }

    rows = audit.normalize_candidate_discovery_output(raw, package_id="PKG-001")

    assert rows[0]["candidate_id"] == "CD-PKG-001-0001"
    assert rows[0]["source"] == "candidate_discovery_agent"
    assert rows[0]["review_status"] == "candidate"
    assert rows[0]["recommended_agent"] == "Hardware Agent"
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_candidate_discovery_normalizes_agent_candidates
```

Expected:

- FAIL because `normalize_candidate_discovery_output` does not exist.

- [ ] **Step 3: Implement normalizer**

Add:

```python
def normalize_candidate_discovery_output(raw: dict, package_id: str) -> list[dict]:
    candidates = raw.get("candidates") if isinstance(raw.get("candidates"), list) else []
    rows = []
    for idx, item in enumerate(candidates, start=1):
        if not isinstance(item, dict):
            continue
        evidence_refs = item.get("evidence_refs") if isinstance(item.get("evidence_refs"), list) else []
        missing_context = item.get("missing_context") if isinstance(item.get("missing_context"), list) else []
        rows.append(
            {
                "candidate_id": f"CD-{package_id}-{idx:04d}",
                "source": "candidate_discovery_agent",
                "package_id": package_id,
                "candidate_type": str(item.get("candidate_type") or "semantic_candidate"),
                "claim": str(item.get("claim") or ""),
                "why_suspicious": str(item.get("why_suspicious") or ""),
                "recommended_agent": str(item.get("recommended_agent") or "Regulatory Agent"),
                "confidence": str(item.get("confidence") or "medium"),
                "evidence_refs": evidence_refs,
                "missing_context": missing_context,
                "review_status": "candidate",
            }
        )
    return rows
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_candidate_discovery_normalizes_agent_candidates
```

Expected:

- PASS.

---

### Task 6: Prevent Evidence Tools From Directly Producing Final Candidates

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Consumes: deterministic evidence rows from old mechanical checks.
- Produces: evidence-only records, not final candidate findings.

- [ ] **Step 1: Write failing test**

Add:

```python
def test_evidence_tool_rows_do_not_become_candidate_findings_directly():
    row = {
        "finding_type": "residue_candidate",
        "term": "PT9C",
        "rel_path": "bom.md",
        "line": 3,
        "source_text": "PT9C-CNTP01",
    }

    evidence = audit.normalize_evidence_tool_hit(row, source_tool="legacy_residue_scan")

    assert evidence["source_tool"] == "legacy_residue_scan"
    assert evidence["record_type"] == "evidence_hit"
    assert "candidate_id" not in evidence
    assert evidence["matched_text"] == "PT9C"
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_evidence_tool_rows_do_not_become_candidate_findings_directly
```

Expected:

- FAIL because `normalize_evidence_tool_hit` does not exist.

- [ ] **Step 3: Implement evidence normalizer**

Add:

```python
def normalize_evidence_tool_hit(row: dict, source_tool: str) -> dict:
    return {
        "record_type": "evidence_hit",
        "source_tool": source_tool,
        "matched_text": str(row.get("term") or row.get("matched_text") or ""),
        "rel_path": row.get("rel_path", ""),
        "line": row.get("line", ""),
        "source_text": row.get("source_text", ""),
        "note": "Evidence retrieval output only; Candidate Discovery Agent must decide whether this becomes a candidate.",
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_evidence_tool_rows_do_not_become_candidate_findings_directly
```

Expected:

- PASS.

---

### Task 7: Add Progressive Context Recovery Round Planning

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Consumes: task, context, round number.
- Produces: round-specific recovery strategy.

- [ ] **Step 1: Write failing test**

Add:

```python
def test_context_recovery_round_strategy_progressively_expands_context():
    strategies = [audit.context_recovery_round_strategy(i) for i in range(1, 6)]

    assert strategies[0]["focus"] == "local_context"
    assert strategies[1]["focus"] == "same_entity_context"
    assert strategies[2]["focus"] == "lifecycle_context"
    assert strategies[3]["focus"] == "document_control_context"
    assert strategies[4]["focus"] == "counter_evidence_and_human_review_pack"
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_context_recovery_round_strategy_progressively_expands_context
```

Expected:

- FAIL because `context_recovery_round_strategy` does not exist.

- [ ] **Step 3: Implement round strategy**

Add:

```python
def context_recovery_round_strategy(round_no: int) -> dict:
    strategies = {
        1: {
            "focus": "local_context",
            "instruction": "补充原证据邻近上下文，包括当前行前后文、表格完整行列、小节标题和文件基本信息。",
        },
        2: {
            "focus": "same_entity_context",
            "instruction": "补充同一型号、料号、参数、文件编号、需求编号或风险编号在全项目中的出现位置。",
        },
        3: {
            "focus": "lifecycle_context",
            "instruction": "补充生命周期上下游链路，包括设计输入到输出、风险到控制到验证、BOM 到工艺到检验。",
        },
        4: {
            "focus": "document_control_context",
            "instruction": "补充受控状态和版本上下文，包括封面、修订历史、签批页、文件清单、变更记录和归档/废止信息。",
        },
        5: {
            "focus": "counter_evidence_and_human_review_pack",
            "instruction": "补充支持 confirm 的证据、支持 dismiss 的反证、仍缺证据和人工复核建议。",
        },
    }
    return strategies.get(round_no, strategies[5])
```

- [ ] **Step 4: Include strategy in Context Recovery prompt payload**

Modify `call_context_recovery_llm` payload:

```python
"round_strategy": context_recovery_round_strategy(round_no),
```

- [ ] **Step 5: Run related tests**

Run:

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_context_recovery_round_strategy_progressively_expands_context
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py::test_context_recovery_llm_loop_caps_at_five_rounds
```

Expected:

- Both tests pass.

---

### Task 8: Wire The New Nodes Into LangGraph

**Files:**
- Modify: `m-agent/run_pt9l_full_audit_langgraph.py`
- Test: `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Adds state fields:
  - `project_profile: dict`
  - `mandatory_audit_matrix: list[dict]`
  - `candidate_discovery_results: list[dict]`
  - `routed_review_packages: dict[str, list[dict]]`

- [ ] **Step 1: Add state fields**

Modify `FullAuditState`:

```python
project_profile: dict
mandatory_audit_matrix: list[dict]
candidate_discovery_results: list[dict]
routed_review_packages: dict
```

- [ ] **Step 2: Change scout node to produce project profile**

In `scout_node`, after loading LLM output:

```python
project_profile = normalize_project_profile(output)
```

Return it in state:

```python
"project_profile": project_profile
```

- [ ] **Step 3: Add orchestrator audit matrix**

In `orchestrator_node`, compute:

```python
mandatory_audit_matrix = build_mandatory_audit_matrix(state.get("project_profile", {}))
```

Write:

```python
write_json(output_root / "10_task_packages" / "mandatory_audit_matrix.json", {"matrix": mandatory_audit_matrix})
```

- [ ] **Step 4: Add candidate discovery node skeleton**

Add:

```python
def candidate_discovery_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    packages = state.get("task_packages", {})
    discovery_rows = []
    for package_id, package in packages.items():
        if package_id not in {"hardware", "software", "risk", "vv", "dmr", "regulatory"}:
            continue
        raw = load_or_run_agent(output_root, f"candidate_discovery_{package_id}", "Candidate Discovery Agent", {
            "project_profile": state.get("project_profile", {}),
            "mandatory_audit_matrix": state.get("mandatory_audit_matrix", []),
            "document_package": package,
            "instruction": "阅读该文档包，提出候选一致性问题。可以要求 PageIndex/全文检索补证，但不得把工具命中直接当作候选。",
        })
        discovery_rows.extend(normalize_candidate_discovery_output(raw, package_id=package_id.upper()))
    write_jsonl(output_root / "07_findings" / "candidate_discovery_results.jsonl", discovery_rows)
    return {**state, "candidate_discovery_results": discovery_rows}
```

- [ ] **Step 5: Add Orchestrator Candidate Router**

Add:

```python
def route_candidate_discovery_results(
    candidates: list[dict],
    mandatory_audit_matrix: list[dict],
) -> dict[str, list[dict]]:
    packages: dict[str, list[dict]] = defaultdict(list)
    matrix_by_agent: dict[str, list[str]] = defaultdict(list)
    for row in mandatory_audit_matrix:
        matrix_by_agent[row.get("assigned_agent", "")].append(row.get("matrix_id", ""))

    for candidate in candidates:
        recommended = candidate.get("recommended_agent") or "Regulatory Agent"
        assigned_agents = [recommended]
        if candidate.get("candidate_type") in {"product_identity_inconsistency", "bom_dmr_inconsistency"}:
            assigned_agents = sorted(set(assigned_agents + ["Hardware Agent", "DMR/SOP Agent"]))
        if candidate.get("candidate_type") in {"risk_reference_inconsistency", "verification_reference_gap"}:
            assigned_agents = sorted(set(assigned_agents + ["Risk Traceability Agent", "V&V Agent"]))

        for agent in assigned_agents:
            packages[agent].append(
                {
                    **candidate,
                    "assigned_agent": agent,
                    "assigned_agents": assigned_agents,
                    "routing_source": "orchestrator_candidate_router",
                    "routing_decision": "route_for_domain_review",
                    "linked_mandatory_tasks": matrix_by_agent.get(agent, []),
                    "review_questions": [
                        "该候选是否构成可确认的一致性问题？",
                        "是否存在共用件、历史引用、模板或变更记录可以解释？",
                        "还需要哪些证据才能 confirm 或 dismiss？",
                    ],
                }
            )
    return dict(packages)
```

- [ ] **Step 6: Write failing test for router boundary**

Add:

```python
def test_orchestrator_candidate_router_routes_without_deciding_truth():
    candidates = [
        {
            "candidate_id": "CD-DMR-0001",
            "candidate_type": "product_identity_inconsistency",
            "claim": "BOM 中出现疑似非 PT9L 料号。",
            "recommended_agent": "Hardware Agent",
            "evidence_refs": [],
        }
    ]
    matrix = [
        {
            "matrix_id": "MATRIX-001",
            "assigned_agent": "Hardware Agent",
        },
        {
            "matrix_id": "MATRIX-004",
            "assigned_agent": "DMR/SOP Agent",
        },
    ]

    packages = audit.route_candidate_discovery_results(candidates, matrix)

    assert "Hardware Agent" in packages
    assert "DMR/SOP Agent" in packages
    routed = packages["Hardware Agent"][0]
    assert routed["routing_source"] == "orchestrator_candidate_router"
    assert routed["routing_decision"] == "route_for_domain_review"
    assert "confirm" not in routed.values()
    assert "dismiss" not in routed.values()
```

- [ ] **Step 7: Add candidate routing node**

Add:

```python
def candidate_routing_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    routed = route_candidate_discovery_results(
        state.get("candidate_discovery_results", []),
        state.get("mandatory_audit_matrix", []),
    )
    write_json(output_root / "10_task_packages" / "routed_candidate_review_packages.json", routed)
    return {**state, "routed_review_packages": routed}
```

- [ ] **Step 8: Wire Candidate Discovery back through Orchestrator router**

Initial implementation should place candidate discovery after Orchestrator, then route candidates through Orchestrator Candidate Router before domain review:

```python
graph.add_node("candidate_discovery", candidate_discovery_node)
graph.add_node("candidate_routing", candidate_routing_node)
graph.add_edge("orchestrator", "candidate_discovery")
graph.add_edge("candidate_discovery", "candidate_routing")
graph.add_edge("candidate_routing", "regulatory_agent")
graph.add_edge("candidate_routing", "hardware_agent")
graph.add_edge("candidate_routing", "software_agent")
graph.add_edge("candidate_routing", "risk_agent")
graph.add_edge("candidate_routing", "vv_agent")
graph.add_edge("candidate_routing", "dmr_agent")
```

Remove direct edges from `orchestrator` to those domain agents.

- [ ] **Step 9: Ensure domain agents receive routed discovery candidates**

Add candidate rows into each relevant task package before domain agent call:

```python
package["candidate_discovery_inputs"] = state.get("routed_review_packages", {}).get(agent_name, [])
```

- [ ] **Step 10: Run compile and tests**

Run:

```powershell
python -X utf8 -m py_compile m-agent\run_pt9l_full_audit_langgraph.py
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py
```

Expected:

- Compilation succeeds.
- Tests pass.

---

### Task 9: Run A Small Validation Before Full v8

**Files:**
- Modify only if tests reveal issues:
  - `m-agent/run_pt9l_full_audit_langgraph.py`
  - `m-agent/tests/test_v6_audit_semantics.py`

**Interfaces:**
- Consumes: PT9L Markdown source.
- Produces: quick validation output.

- [ ] **Step 1: Run syntax and unit tests**

Run:

```powershell
python -X utf8 -m py_compile m-agent\run_pt9l_full_audit_langgraph.py
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py
```

Expected:

- Both pass.

- [ ] **Step 2: Run a cached/small-scope validation if available**

If the script supports full-only execution, skip this step and proceed to Task 10. If a sample runner is adapted, run:

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py --input pt9l_markdown_output --output magent-output\pt9l_full_audit_output_langgraph_v8_sample
```

Expected:

- `10_task_packages/mandatory_audit_matrix.json` exists.
- `07_findings/candidate_discovery_results.jsonl` exists.
- `08_reports/run_summary_full_langgraph.json` exists.

---

### Task 10: Run Full v8 And Compare Against v7

**Files:**
- Output: `magent-output/pt9l_full_audit_output_langgraph_v8/`

**Interfaces:**
- Consumes: `pt9l_markdown_output`
- Produces: v8 full audit report.

- [ ] **Step 1: Run full v8**

Run:

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output\pt9l_full_audit_output_langgraph_v8
```

Expected:

- Script exits with code 0.
- Summary JSON is printed.

- [ ] **Step 2: Verify key outputs**

Run:

```powershell
Test-Path magent-output\pt9l_full_audit_output_langgraph_v8\08_reports\run_summary_full_langgraph.json
Test-Path magent-output\pt9l_full_audit_output_langgraph_v8\08_reports\PT9L_full_audit_report_langgraph.md
Test-Path magent-output\pt9l_full_audit_output_langgraph_v8\10_task_packages\mandatory_audit_matrix.json
Test-Path magent-output\pt9l_full_audit_output_langgraph_v8\07_findings\candidate_discovery_results.jsonl
```

Expected:

- All return `True`.

- [ ] **Step 3: Compare v8 to v7**

Run:

```powershell
python -X utf8 - <<'PY'
import json
from pathlib import Path
for name in ["v7", "v8"]:
    root = Path("magent-output") / f"pt9l_full_audit_output_langgraph_{name}"
    summary = json.loads((root / "08_reports" / "run_summary_full_langgraph.json").read_text(encoding="utf-8"))
    print(name, {
        "merged_findings": summary.get("merged_findings"),
        "current_confirmed_error_total": summary.get("current_confirmed_error_total"),
        "context_recovery_total": summary.get("context_recovery_total"),
    })
PY
```

Expected:

- v8 includes candidate discovery outputs.
- v8 counts may differ from v7; review the delta manually before treating it as better or worse.

---

## Acceptance Criteria

- Technical documentation no longer claims fixed preset word lists directly generate candidates.
- `Project Scout Agent` is the unified name for the Scout/profile role.
- Orchestrator still explicitly generates stage-axis and dimension-axis mandatory audit tasks.
- `Candidate Discovery Agent` is responsible for semantic candidate discovery.
- Evidence tools only retrieve and locate evidence; they do not decide candidate existence.
- Context Recovery has explicit round-by-round evidence expansion strategy.
- Unit tests cover the new data contracts and guard against tool hits becoming direct candidates.
- Full v8 run creates a report and candidate discovery outputs under `magent-output/pt9l_full_audit_output_langgraph_v8/`.

## Self-Review Notes

- Spec coverage: The plan covers naming, documentation, visualization, Orchestrator logic preservation, Candidate Discovery Agent, evidence-tool downgrade, Context Recovery rounds, tests, and v8 run.
- Placeholder scan: No TBD/TODO placeholders remain.
- Type consistency: New functions referenced by tests are defined in corresponding tasks with exact names.
