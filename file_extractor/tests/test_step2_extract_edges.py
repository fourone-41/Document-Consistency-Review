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
