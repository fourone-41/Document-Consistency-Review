# file_extractor/tests/test_graph_pattern_propagation.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import graph_pattern_propagation as gpp


def test_count_two_hop_patterns_counts_type_sequences():
    edges = [
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-01", "to_id": "CM-01"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-01", "to_id": "T-01"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-02", "to_id": "CM-02"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-02", "to_id": "T-02"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-03", "to_id": "CM-03"},
    ]

    patterns = gpp.count_two_hop_patterns(edges)

    assert patterns[("MITIGATED_BY", "VERIFIED_BY")] == 2


def test_find_missing_next_hop_finds_node_without_second_hop():
    edges = [
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-01", "to_id": "CM-01"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-01", "to_id": "T-01"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-02", "to_id": "CM-02"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-02", "to_id": "T-02"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-03", "to_id": "CM-03"},
        # CM-03 没有 VERIFIED_BY 出边 -> 缺失的下一跳
    ]
    nodes = {
        "risk_controls": [{"control_id": "CM-01"}, {"control_id": "CM-02"}, {"control_id": "CM-03"}],
        "tests": [{"test_id": "T-01"}, {"test_id": "T-02"}, {"test_id": "T-03"}],
    }

    missing = gpp.find_missing_next_hop(nodes, edges, min_frequency=2)

    cm03_candidates = [m for m in missing if m["from_id"] == "CM-03"]
    assert len(cm03_candidates) == 1
    assert cm03_candidates[0]["expected_relation"] == ("MITIGATED_BY", "VERIFIED_BY")
    assert cm03_candidates[0]["pattern_frequency"] == 2
    assert len(cm03_candidates[0]["candidate_targets"]) == 3  # 全部 Test 节点作为候选


def test_find_missing_next_hop_ignores_low_frequency_patterns():
    edges = [
        # 一条完整的 A->B->C 链，建立 (SCHEDULES, DEPENDS_ON) 模式，但只出现 1 次
        {"type": "SCHEDULES", "from_type": "documents", "to_type": "plan_tasks", "from_id": "D1", "to_id": "P1"},
        {"type": "DEPENDS_ON", "from_type": "plan_tasks", "to_type": "plan_tasks", "from_id": "P1", "to_id": "P2"},
        # P3 也完成了第一跳（同样的 SCHEDULES），但缺第二跳——
        # 如果频次过滤失效，P3 会被错误地标记为候选；
        # 但该模式频次只有 1（不算 P3 这条，因为 P3 还没有完成第二跳，不计入模式频次），
        # 低于 min_frequency=3，应该被过滤，不应该把 P3 标出来。
        {"type": "SCHEDULES", "from_type": "documents", "to_type": "plan_tasks", "from_id": "D2", "to_id": "P3"},
    ]
    nodes = {"plan_tasks": [{"name": "P1"}, {"name": "P2"}, {"name": "P3"}]}

    missing = gpp.find_missing_next_hop(nodes, edges, min_frequency=3)

    assert missing == []


def test_find_missing_next_hop_treats_unrelated_outgoing_edge_as_still_missing():
    edges = [
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-01", "to_id": "CM-01"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-01", "to_id": "T-01"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-02", "to_id": "CM-02"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-02", "to_id": "T-02"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-03", "to_id": "CM-03"},
        {"type": "REFERENCES_DOC", "from_type": "risk_controls", "to_type": "documents", "from_id": "CM-03", "to_id": "D-01"},
    ]
    nodes = {
        "risk_controls": [{"control_id": "CM-03"}],
        "tests": [{"test_id": "T-01"}],
    }

    missing = gpp.find_missing_next_hop(nodes, edges, min_frequency=2)

    assert [m["from_id"] for m in missing] == ["CM-03"]
