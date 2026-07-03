from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "run_pt9l_full_audit_langgraph.py"
sys.path.insert(0, str(MODULE_PATH.parent))
spec = importlib.util.spec_from_file_location("run_pt9l_full_audit_langgraph", MODULE_PATH)
audit = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit)

def test_weak_challenge_reason_downgrades_confirming_decisions():
    assert audit.is_weak_challenge_reason("keep", "璇佹嵁鏄剧ず")
    assert audit.is_weak_challenge_reason("revise", "璇ユ枃浠跺紩鐢?PT9C锛屼笖")
    assert not audit.is_weak_challenge_reason(
        "keep",
        "璇ュ彂鐜版湁鍙洖婧瘉鎹敮鎸侊紝寮曠敤鏂囦欢鍙蜂笌 PT9L 涓诲鑼冨洿涓嶄竴鑷达紝涓旇瘉鎹潵鑷寮忔姤鍛婃鏂囷紝寤鸿淇濈暀杩涘叆浜哄伐澶嶆牳銆?",
    )
    assert not audit.is_weak_challenge_reason("needs_more_context", "璇佹嵁涓嶈冻")


def test_parameter_alignment_evidence_rows_group_numeric_conflicts():
    params = [
        {
            "doc_id": "D1",
            "rel_path": "04 design input.md",
            "stage": "Stage 04",
            "doc_type": "design_input",
            "line": 10,
            "canonical_slots": ["measurement_accuracy"],
            "values": [{"value_type": "temperature_value", "raw_value": "卤0.2鈩?"}],
            "source_text": "娴嬮噺绮惧害 卤0.2鈩?",
        },
        {
            "doc_id": "D2",
            "rel_path": "18 validation report.md",
            "stage": "Stage 18",
            "doc_type": "validation_report",
            "line": 20,
            "canonical_slots": ["measurement_accuracy"],
            "values": [{"value_type": "temperature_value", "raw_value": "卤0.3鈩?"}],
            "source_text": "accuracy 卤0.3鈩?",
        },
        {
            "doc_id": "D3",
            "rel_path": "07 software.md",
            "stage": "Stage 07",
            "doc_type": "software_requirements",
            "line": 5,
            "canonical_slots": ["software_version"],
            "values": [{"value_type": "voltage_value", "raw_value": "V1.0"}],
            "source_text": "杞欢鐗堟湰 V1.0",
        },
    ]

    evidence_rows = audit.build_parameter_alignment_evidence_rows(params)

    assert len(evidence_rows) == 1
    candidate = evidence_rows[0]
    assert candidate["evidence_type"] == "parameter_alignment_signal"
    assert candidate["term"] == "parameter_alignment:measurement_accuracy:temperature_value:temperature"
    assert len(candidate["parameter_alignment_evidence"]) == 2
    assert "卤0.2" in candidate["source_text"]
    assert "卤0.3" in candidate["source_text"]


def test_result_summary_uses_semantic_confirmed_total():
    summary = audit.build_result_count_summary(
        semantic_rows=[
            {"challenge_status": "keep"},
            {"challenge_status": "revise"},
            {"challenge_status": "needs_more_context"},
            {"challenge_status": "drop"},
        ],
        all_findings=[{}] * 223,
    )

    assert summary["semantic_confirmed_keep_revise"] == 2
    assert summary["merged_findings_rows"] == 223
    assert summary["current_confirmed_error_total"] == 2


def test_context_recovery_collects_semantic_gaps():
    state = {
        "semantic_findings": [
            {
                "finding_id": "LLM-1",
                "agent": "Software Agent",
                "finding_type": "software_traceability_gap",
                "challenge_status": "needs_more_context",
                "claim": "software traceability is blank",
                "evidence_refs": [{"rel_path": "sw.md", "line": 8, "source_text": "trace table"}],
            },
            {
                "finding_id": "LLM-2",
                "agent": "Hardware Agent",
                "finding_type": "parameter_alignment_review",
                "challenge_status": "keep",
                "claim": "already decided",
            },
        ],
    }

    tasks = audit.build_context_recovery_tasks(state)

    assert [task["gap_source"] for task in tasks] == ["semantic"]
    assert tasks[0]["source_id"] == "LLM-1"
    assert tasks[0]["target_agent"] == "Software Agent"
    assert tasks[0]["context_need_type"] == "traceability_context"


def test_context_recovery_second_pass_converges_remaining_semantic_items(tmp_path, monkeypatch):
    monkeypatch.setattr(
        audit,
        "call_context_recovery_llm",
        lambda task, context, round_no, output_root: {"task_id": task["task_id"], "round": round_no, "context_package": context},
    )
    monkeypatch.setattr(
        audit,
        "call_context_orchestrator_llm",
        lambda task, recovery, round_no, output_root: {
            "task_id": task["task_id"],
            "round": round_no,
            "assigned_agent": task["target_agent"],
            "review_focus": "continue review",
            "agent_input": recovery,
        },
    )
    monkeypatch.setattr(
        audit,
        "call_context_review_agent_llm",
        lambda task, assignment, recovery, round_no, output_root: {
            "task_id": task["task_id"],
            "round": round_no,
            "agent": assignment["assigned_agent"],
            "decision": "needs_more_context",
            "severity": task["severity"],
            "error_type": "still_unclear",
            "claim": task["claim"],
            "reason": "still unclear after recovered context",
        },
    )
    state = {
        "input_root": str(tmp_path),
        "output_root": str(tmp_path),
        "page_index": [],
        "params": [],
        "semantic_findings": [
            {
                "finding_id": "LLM-1",
                "agent": "Software Agent",
                "finding_type": "software_traceability_gap",
                "challenge_status": "needs_more_context",
                "claim": "software traceability is blank",
                "severity": "P2",
                "evidence_refs": [{"rel_path": "sw.md", "line": 8, "source_text": "trace table"}],
            }
        ],
        "all_findings": [],
    }

    updated = audit.context_recovery_node(state)

    final_statuses = {row["final_status"] for row in updated["context_recovery_results"]}
    assert final_statuses <= {"confirm", "dismiss", "human_review"}
    assert "needs_more_context" not in final_statuses
    assert updated["semantic_findings"][0]["challenge_status"] == "human_review"
    assert (tmp_path / "14_context_recovery" / "context_recovery_tasks.json").exists()
    assert (tmp_path / "14_context_recovery" / "context_recovery_results.jsonl").exists()


def test_context_recovery_llm_loop_reassigns_to_agents_until_decided(tmp_path, monkeypatch):
    calls: list[tuple[str, str, int]] = []

    def fake_context_recovery(task, context, round_no, output_root):
        calls.append(("context", task["source_id"], round_no))
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "context_summary": f"round {round_no} recovered context",
            "evidence_gaps": [],
            "additional_search_queries": [],
            "agent_instruction": "review again with recovered context",
            "context_package": context,
        }

    def fake_orchestrator(task, recovery, round_no, output_root):
        calls.append(("orchestrator", task["source_id"], round_no))
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "assigned_agent": task["target_agent"],
            "review_focus": "decide whether the issue is real",
            "agent_input": recovery,
        }

    def fake_review(task, assignment, recovery, round_no, output_root):
        calls.append(("review", task["source_id"], round_no))
        if round_no == 1:
            return {
                "task_id": task["task_id"],
                "round": round_no,
                "agent": assignment["assigned_agent"],
                "decision": "needs_more_context",
                "severity": task["severity"],
                "error_type": "still_unclear",
                "claim": task["claim"],
                "reason": "first round still unclear",
            }
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "agent": assignment["assigned_agent"],
            "decision": "confirm",
            "severity": task["severity"],
            "error_type": "v9_agent_review",
            "claim": task["claim"],
            "reason": "second round can decide",
        }

    monkeypatch.setattr(audit, "call_context_recovery_llm", fake_context_recovery, raising=False)
    monkeypatch.setattr(audit, "call_context_orchestrator_llm", fake_orchestrator, raising=False)
    monkeypatch.setattr(audit, "call_context_review_agent_llm", fake_review, raising=False)

    state = {
        "input_root": str(tmp_path),
        "output_root": str(tmp_path),
        "page_index": [],
        "params": [],
        "semantic_findings": [
            {
                "finding_id": "LLM-1",
                "agent": "Software Agent",
                "finding_type": "software_traceability_gap",
                "challenge_status": "needs_more_context",
                "claim": "software traceability is blank",
                "severity": "P2",
                "evidence_refs": [{"rel_path": "sw.md", "line": 8, "source_text": "trace table"}],
            }
        ],
        "all_findings": [],
    }

    updated = audit.context_recovery_node(state)

    assert ("context", "LLM-1", 1) in calls
    assert ("orchestrator", "LLM-1", 1) in calls
    assert ("review", "LLM-1", 1) in calls
    assert ("review", "LLM-1", 2) in calls
    assert updated["semantic_findings"][0]["challenge_status"] == "keep"
    assert updated["context_recovery_summary"]["rounds_executed"] == 2
    assert updated["context_recovery_summary"]["by_final_status"]["confirm"] == 1

def test_context_recovery_llm_loop_caps_at_five_rounds(tmp_path, monkeypatch):
    review_rounds: list[int] = []

    monkeypatch.setattr(
        audit,
        "call_context_recovery_llm",
        lambda task, context, round_no, output_root: {"task_id": task["task_id"], "round": round_no, "context_package": context},
        raising=False,
    )
    monkeypatch.setattr(
        audit,
        "call_context_orchestrator_llm",
        lambda task, recovery, round_no, output_root: {
            "task_id": task["task_id"],
            "round": round_no,
            "assigned_agent": task["target_agent"],
            "review_focus": "缁х画澶嶅銆?",
            "agent_input": recovery,
        },
        raising=False,
    )

    def always_needs_more_context(task, assignment, recovery, round_no, output_root):
        review_rounds.append(round_no)
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "agent": assignment["assigned_agent"],
            "decision": "needs_more_context",
            "severity": task["severity"],
            "error_type": "still_unclear",
            "claim": task["claim"],
            "reason": "浠嶉渶琛ヨ瘉銆?",
        }

    monkeypatch.setattr(audit, "call_context_review_agent_llm", always_needs_more_context, raising=False)

    state = {
        "input_root": str(tmp_path),
        "output_root": str(tmp_path),
        "page_index": [],
        "params": [],
        "semantic_findings": [
            {
                "finding_id": "LLM-1",
                "agent": "Risk Traceability Agent",
                "finding_type": "risk_control_gap",
                "challenge_status": "needs_more_context",
                "claim": "risk link unclear",
                "severity": "P2",
                "evidence_refs": [{"rel_path": "risk.md", "line": 8, "source_text": "risk table"}],
            }
        ],
        "all_findings": [],
    }

    updated = audit.context_recovery_node(state)

    assert review_rounds == [1, 2, 3, 4, 5]
    assert updated["semantic_findings"][0]["challenge_status"] == "human_review"
    assert updated["context_recovery_results"][0]["final_status"] == "human_review"
    assert updated["context_recovery_results"][0]["rounds_used"] == 5
    assert updated["context_recovery_summary"]["max_rounds"] == 5


def test_context_recovery_loop_survives_truncated_llm_json(tmp_path, monkeypatch):
    calls: list[tuple[str, int]] = []

    def truncated_context_recovery(task, context, round_no, output_root):
        calls.append(("context", round_no))
        raise audit.json.JSONDecodeError("Unterminated string", '{"context_summary": "cut', 20)

    def fake_orchestrator(task, recovery, round_no, output_root):
        calls.append(("orchestrator", round_no))
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "assigned_agent": task["target_agent"],
            "review_focus": "缁х画澶嶅銆?",
            "agent_input": recovery,
        }

    def fake_review(task, assignment, recovery, round_no, output_root):
        calls.append(("review", round_no))
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "agent": assignment["assigned_agent"],
            "decision": "needs_more_context",
            "severity": task["severity"],
            "error_type": "still_unclear",
            "claim": task["claim"],
            "reason": "浠嶇己灏戝彲瑙ｆ瀽鐨勮ˉ璇佽緭鍑恒€?",
        }

    monkeypatch.setattr(audit, "call_context_recovery_llm", truncated_context_recovery, raising=False)
    monkeypatch.setattr(audit, "call_context_orchestrator_llm", fake_orchestrator, raising=False)
    monkeypatch.setattr(audit, "call_context_review_agent_llm", fake_review, raising=False)

    task = {
        "task_id": "CTX-S-0001",
        "gap_source": "semantic",
        "source_id": "LLM-1",
        "target_agent": "Regulatory Agent",
        "context_need_type": "controlled_document_context",
        "severity": "P2",
        "claim": "鍙屽椋庨櫓鏂囦欢鍙楁帶鐘舵€佷笉娓呫€?",
    }
    result = audit.run_context_recovery_loop(task, {"same_item_evidence": [], "parameter_context": [], "page_context": []}, tmp_path, max_rounds=2)

    assert result["final_status"] == "human_review"
    assert result["rounds_used"] == 2
    assert result["final_review_decision"]["error_type"] == "llm_parse_or_call_failed"
    assert calls == [("context", 1), ("orchestrator", 1), ("review", 1), ("context", 2), ("orchestrator", 2), ("review", 2)]


def test_context_llm_call_reuses_existing_raw_without_client(tmp_path, monkeypatch):
    raw_path = tmp_path / "11_llm_raw" / "context_review_agent_CTX-S-0001_round_01.json"
    raw_path.parent.mkdir(parents=True)
    raw_path.write_text('{"decision": "confirm", "reason": "cached decision"}', encoding="utf-8")

    def fail_make_client():
        raise AssertionError("cached raw JSON should be reused without an LLM client")

    monkeypatch.setattr(audit, "make_client", fail_make_client)

    parsed = audit.llm_json_call(raw_path, "system", {"payload": "new request"}, max_tokens=10)

    assert parsed["decision"] == "confirm"
    assert parsed["reason"] == "cached decision"


def test_resume_context_recovery_loads_existing_outputs_and_reports(tmp_path, monkeypatch):
    output_root = tmp_path / "audit_output"
    (output_root / "00_manifest").mkdir(parents=True)
    (output_root / "01_page_index").mkdir(parents=True)
    (output_root / "03_ssot_parameters").mkdir(parents=True)
    (output_root / "04_relation_index").mkdir(parents=True)
    (output_root / "05_agent_notes").mkdir(parents=True)
    (output_root / "06_evidence_tools").mkdir(parents=True)
    (output_root / "07_findings").mkdir(parents=True)
    (output_root / "10_task_packages").mkdir(parents=True)

    (output_root / "00_manifest" / "full_manifest.jsonl").write_text(
        audit.json.dumps({"doc_id": "DOC-1", "excluded_from_primary_scope": False}, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output_root / "01_page_index" / "page_index.jsonl").write_text("", encoding="utf-8")
    (output_root / "03_ssot_parameters" / "parameter_instances.jsonl").write_text("", encoding="utf-8")
    (output_root / "04_relation_index" / "nodes.jsonl").write_text("", encoding="utf-8")
    (output_root / "04_relation_index" / "edges.jsonl").write_text("", encoding="utf-8")
    (output_root / "05_agent_notes" / "agent_runs.jsonl").write_text(
        audit.json.dumps({"run_id": "RUN-0001", "agent": "Software Agent"}, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output_root / "06_evidence_tools" / "evidence_tool_hits.jsonl").write_text("", encoding="utf-8")
    (output_root / "07_findings" / "candidate_discovery_results.jsonl").write_text("", encoding="utf-8")
    (output_root / "07_findings" / "semantic_findings_llm_challenged.jsonl").write_text(
        audit.json.dumps(
            {
                "finding_id": "LLM-1",
                "agent": "Software Agent",
                "challenge_status": "needs_more_context",
                "severity": "P2",
                "claim": "software evidence unclear",
            },
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (output_root / "10_task_packages" / "orchestrator_route_plans.json").write_text(
        audit.json.dumps({"route_plans": [{"cycle": 1, "decision": "stop"}]}, ensure_ascii=False),
        encoding="utf-8",
    )
    (output_root / "10_task_packages" / "mandatory_audit_matrix.json").write_text(
        audit.json.dumps({"matrix": [{"id": "MATRIX-1"}]}, ensure_ascii=False),
        encoding="utf-8",
    )

    seen = {}

    def fake_context_recovery_node(state):
        seen["semantic_findings"] = state["semantic_findings"]
        assert state["agent_runs"][0]["run_id"] == "RUN-0001"
        return {
            **state,
            "semantic_findings": [{**state["semantic_findings"][0], "challenge_status": "human_review"}],
            "all_findings": [{**state["semantic_findings"][0], "challenge_status": "human_review"}],
            "context_recovery_summary": {"total": 1, "by_final_status": {"human_review": 1}},
        }

    def fake_report_node(state):
        assert state["context_recovery_summary"]["total"] == 1
        return {**state, "summary": {"resumed": True, "llm_semantic_findings": len(state["semantic_findings"])}}

    monkeypatch.setattr(audit, "context_recovery_node", fake_context_recovery_node)
    monkeypatch.setattr(audit, "report_node", fake_report_node)

    summary = audit.run_context_recovery_resume(tmp_path, output_root)

    assert seen["semantic_findings"][0]["finding_id"] == "LLM-1"
    assert summary == {"resumed": True, "llm_semantic_findings": 1}


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


def test_orchestrator_builds_stage_dimension_audit_matrix():
    matrix = audit.build_mandatory_audit_matrix({"target_model": "PT9L"})

    keys = {(row["stage_axis"], row["dimension_axis"], row["assigned_agent"]) for row in matrix}
    assert ("design_input_to_output", "parameter_consistency", "Hardware Agent") in keys
    assert ("risk_to_verification", "risk_traceability", "Risk Traceability Agent") in keys
    assert ("software_lifecycle", "software_traceability", "Software Agent") in keys
    assert ("dmr_chain", "dmr_sop_consistency", "DMR/SOP Agent") in keys
    assert ("all_stages", "document_control", "Regulatory Agent") in keys


def test_agent_config_loads_domain_schema_and_retrieval_strategy():
    config = audit.load_agent_config("hardware")

    assert config["agent_id"] == "hardware"
    assert config["display_name"] == "Hardware Agent"
    assert "retrieval_strategy" in config
    assert config["input_schema"]["required_fields"]
    assert config["output_schema"]["required_fields"]


def test_agent_task_uses_yaml_config_fields():
    config = audit.load_agent_config("hardware")
    task = audit.build_agent_task_from_config(
        config,
        evidence_catalog=[{"id": "EV-HW-0001", "source_text": "accuracy ±0.2℃"}],
        project_profile={"target_model": "PT9L"},
        mandatory_audit_matrix=[{"matrix_id": "MATRIX-001"}],
    )

    assert task["role"] == "Hardware Agent"
    assert task["goal"] == config["goal"]
    assert task["retrieval_strategy"] == config["retrieval_strategy"]
    assert task["input_schema"] == config["input_schema"]
    assert task["required_schema"] == config["output_schema"]


def test_routing_yaml_is_orchestrator_policy_not_direct_router():
    routing = audit.load_routing_config()

    assert "orchestrator_policy" in routing
    policy = routing["orchestrator_policy"]
    assert "mandatory_coverage" in policy
    assert "candidate_routing_guidance" in policy
    assert "context_recovery_guidance" in policy
    assert "decision_values" in policy
    assert set(policy["decision_values"]) == {"continue", "stop", "human_review"}


def test_dynamic_orchestrator_runs_only_assigned_agents_and_records_agent_runs(tmp_path, monkeypatch):
    calls: list[str] = []

    def fake_route_plan(state, cycle_no, output_root):
        if cycle_no == 1:
            return {
                "decision": "continue",
                "reason": "hardware review is needed",
                "assignments": [
                    {
                        "assignment_id": "ASG-0001",
                        "target_agent": "Hardware Agent",
                        "task_type": "domain_review",
                        "review_focus": "Review hardware consistency.",
                        "input_refs": [],
                        "evidence_strategy": {"use_full_text": True},
                    }
                ],
            }
        return {"decision": "stop", "reason": "all assigned reviews completed", "assignments": []}

    def fake_run_agent(output_root, key, agent_name, task):
        calls.append(agent_name)
        return {
            "agent": agent_name,
            "summary": "reviewed",
            "findings": [
                {
                    "finding_type": "hardware_gap",
                    "severity": "P2",
                    "claim": "hardware issue",
                    "rationale": "because evidence says so",
                    "evidence_ids": [],
                    "challenge_questions": [],
                }
            ],
        }

    monkeypatch.setattr(audit, "call_orchestrator_route_plan", fake_route_plan, raising=False)
    monkeypatch.setattr(audit, "run_agent_llm", fake_run_agent, raising=False)

    state = {
        "input_root": str(tmp_path),
        "output_root": str(tmp_path),
        "manifest": [],
        "evidence_catalog": {},
        "evidence_tool_hits": [],
        "scout_output": {"summary": "PT9L project"},
        "project_profile": {"target_model": "PT9L"},
    }

    updated = audit.orchestrator_node(state)

    assert calls == ["Hardware Agent"]
    assert [row["agent"] for row in updated["agent_runs"]] == ["Hardware Agent"]
    assert updated["agent_runs"][0]["assignment_id"] == "ASG-0001"
    assert updated["agent_runs"][0]["llm_output"]["findings"][0]["claim"] == "hardware issue"
    assert [plan["decision"] for plan in updated["orchestrator_route_plans"]] == ["continue", "stop"]
    assert "hardware_output" not in updated


def test_run_agent_llm_ignores_existing_cache(tmp_path, monkeypatch):
    cache = tmp_path / "05_agent_notes" / "hardware_agent_llm.json"
    cache.parent.mkdir(parents=True)
    cache.write_text('{"agent":"Hardware Agent","summary":"stale","findings":[]}', encoding="utf-8")

    monkeypatch.setattr(
        audit,
        "llm_json",
        lambda agent_name, task, output_root, raw_key=None: {
            "agent": agent_name,
            "summary": "fresh",
            "findings": [],
        },
        raising=False,
    )

    result = audit.run_agent_llm(tmp_path, "hardware", "Hardware Agent", {"role": "Hardware Agent", "goal": "review"})

    assert result["summary"] == "fresh"


def test_collect_semantic_findings_uses_agent_runs():
    state = {
        "evidence_catalog": {},
        "agent_runs": [
            {
                "run_id": "RUN-0001",
                "agent": "Hardware Agent",
                "llm_output": {
                    "agent": "Hardware Agent",
                    "findings": [
                        {
                            "finding_type": "hardware_gap",
                            "severity": "P2",
                            "claim": "hardware issue",
                            "rationale": "evidence based",
                            "evidence_ids": [],
                            "challenge_questions": [],
                        }
                    ],
                },
            }
        ],
    }

    rows = audit.collect_semantic_findings(state)

    assert len(rows) == 1
    assert rows[0]["agent"] == "Hardware Agent"
    assert rows[0]["source_run_id"] == "RUN-0001"


def test_candidate_discovery_normalizes_agent_candidates():
    raw = {
        "agent": "Candidate Discovery Agent",
        "candidates": [
            {
                "candidate_type": "product_identity_inconsistency",
                "claim": "BOM contains a suspicious non-PT9L material number.",
                "why_suspicious": "The material number appears in a primary-scope BOM.",
                "recommended_agent": "Hardware Agent",
                "confidence": "medium",
                "evidence_refs": [{"rel_path": "bom.md", "line": 3, "source_text": "PT9C-CNTP01"}],
                "missing_context": ["design output list", "change history"],
            }
        ],
    }

    rows = audit.normalize_candidate_discovery_output(raw, package_id="PKG-001")

    assert rows[0]["candidate_id"] == "CD-PKG-001-0001"
    assert rows[0]["source"] == "candidate_discovery_agent"
    assert rows[0]["review_status"] == "candidate"
    assert rows[0]["recommended_agent"] == "Hardware Agent"


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


def test_orchestrator_route_plan_only_routes_without_deciding_truth():
    plan = audit.normalize_orchestrator_route_plan(
        {
            "decision": "continue",
            "reason": "candidate needs domain review",
            "assignments": [
                {
                    "assignment_id": "ASG-0001",
                    "target_agent": "DMR/SOP Agent",
                    "task_type": "domain_review",
                    "review_focus": "review candidate",
                    "input_refs": ["CD-DMR-0001"],
                }
            ],
        },
        available_agents={"DMR/SOP Agent"},
        cycle_no=1,
    )

    assignment = plan["assignments"][0]
    assert plan["decision"] == "continue"
    assert assignment["routing_source"] == "orchestrator_llm"
    assert assignment["review_status"] == "candidate"
    assert assignment.get("final_decision") is None


def test_context_recovery_round_strategy_progressively_expands_context():
    strategies = [audit.context_recovery_round_strategy(i) for i in range(1, 6)]

    assert strategies[0]["focus"] == "local_context"
    assert strategies[1]["focus"] == "same_entity_context"
    assert strategies[2]["focus"] == "lifecycle_context"
    assert strategies[3]["focus"] == "document_control_context"
    assert strategies[4]["focus"] == "counter_evidence_and_human_review_pack"


def test_m_agent_has_no_legacy_fixed_routing_residue():
    root = MODULE_PATH.parent
    legacy_patterns = [
        "mechanical_review",
        "mechanical_candidate",
        "机械候选复审",
        "机械规则层",
        "机械扫描",
        "routed_candidate_review_packages",
        "candidate_discovery -> candidate_routing",
        "candidate_routing ->",
        '"assigned_agents"',
        "regulatory_output:",
        "hardware_output:",
        "software_output:",
        "risk_output:",
        "vv_output:",
        "dmr_output:",
    ]
    checked_suffixes = {".py", ".md", ".html", ".yaml"}
    offenders: list[str] = []
    for path in root.rglob("*"):
        if path.suffix not in checked_suffixes:
            continue
        if "__pycache__" in path.parts or "tests" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in legacy_patterns:
            if pattern in text:
                offenders.append(f"{path.relative_to(root)} contains {pattern}")

    assert offenders == []
