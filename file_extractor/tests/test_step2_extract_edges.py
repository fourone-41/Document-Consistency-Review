# file_extractor/tests/test_step2_extract_edges.py
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import step2_extract_edges as s2


def _mock_llm_response(content: str):
    """构造一个假的 OpenAI ChatCompletion 响应对象。"""
    mock_choice = MagicMock()
    mock_choice.message.content = content
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_parses_multiple_types(mock_create):
    mock_create.return_value = _mock_llm_response("MITIGATED_BY\nSIGNED\nHAS_DETAIL")
    data = {"risks": [{"risk_id": "R-01"}], "persons": [{"name": "张三", "signed": True}]}

    result = s2.detect_relation_types_llm(data)

    assert result == ["MITIGATED_BY", "SIGNED", "HAS_DETAIL"]


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_handles_none_found(mock_create):
    mock_create.return_value = _mock_llm_response("无")
    data = {"persons": [{"name": "张三"}]}

    result = s2.detect_relation_types_llm(data)

    assert result == []


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_filters_hallucinated_types(mock_create):
    # LLM 可能编造出列表外的类型名，必须被过滤掉
    mock_create.return_value = _mock_llm_response("MITIGATED_BY\nFAKE_TYPE\nSIGNED")
    data = {"risks": [{"risk_id": "R-01"}]}

    result = s2.detect_relation_types_llm(data)

    assert result == ["MITIGATED_BY", "SIGNED"]


@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_parses_valid_edges(mock_create):
    mock_create.return_value = _mock_llm_response(
        '[{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]'
    )
    data = {"risks": [{"risk_id": "R-01"}], "risk_controls": [{"control_id": "CM-03"}]}

    result = s2.match_within_group(data, "risk_control", ["MITIGATED_BY", "DEPENDS_ON"])

    assert result == [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]


@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_filters_edges_outside_candidate_types(mock_create):
    # LLM 可能跑出候选范围之外的类型，必须被过滤
    mock_create.return_value = _mock_llm_response(
        '[{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}},'
        '{"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}}]'
    )
    data = {"risks": [{"risk_id": "R-01"}]}

    result = s2.match_within_group(data, "risk_control", ["MITIGATED_BY", "DEPENDS_ON"])

    assert result == [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]


@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_empty_candidates_skips_llm_call(mock_create):
    result = s2.match_within_group({"risks": []}, "risk_control", [])

    assert result == []
    mock_create.assert_not_called()


def test_build_node_summary_filters_and_truncates():
    data = {
        "_meta": {"source_file": "x.md"},
        "risks": [{"risk_id": f"R-{i}"} for i in range(5)],
        "document": {"title": "doc"},
        "empty_list": [],
    }

    result = s2.build_node_summary(data, max_items=2)

    assert result == {
        "risks": [{"risk_id": "R-0"}, {"risk_id": "R-1"}],
        "document": {"title": "doc"},
    }


@patch("step2_extract_edges.match_within_group")
@patch("step2_extract_edges.detect_relation_types_llm")
def test_extract_edges_llm_v2_groups_candidates_and_merges_results(mock_detect, mock_match):
    mock_detect.return_value = ["MITIGATED_BY", "SIGNED"]

    def fake_match(data, group_name, candidate_types):
        if group_name == "risk_control":
            return [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]
        if group_name == "admin":
            return [{"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}}]
        return []

    mock_match.side_effect = fake_match
    relation_groups = {
        "structural":    ["LISTS_FILE", "DESCRIBES_SOFTWARE", "HAS_DETAIL"],
        "traceability":  ["DERIVES_FROM", "CONSTRAINED_BY", "IMPLEMENTED_IN"],
        "verification":  ["VERIFIED_BY", "REPORTED_IN", "COVERS", "HAS_MEASUREMENT"],
        "risk_control":  ["MITIGATED_BY", "DEPENDS_ON", "SCHEDULES", "RESPONSIBLE_FOR"],
        "admin":         ["SIGNED", "REVIEWS", "HAS_REVIEW_ITEM", "HAS_REVISION", "PRODUCES"],
    }

    result = s2.extract_edges_llm_v2({"risks": [{"risk_id": "R-01"}]}, relation_groups)

    assert {"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}} in result
    assert {"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}} in result
    assert len(result) == 2
    assert mock_match.call_count == 2


@patch("step2_extract_edges.detect_relation_types_llm")
def test_extract_edges_llm_v2_no_types_detected_skips_all_groups(mock_detect):
    mock_detect.return_value = []
    relation_groups = {"risk_control": ["MITIGATED_BY"]}

    result = s2.extract_edges_llm_v2({"risks": []}, relation_groups)

    assert result == []
