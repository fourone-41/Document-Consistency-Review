# file_extractor/tests/test_step4_cross_doc_edges.py
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

import step4_cross_doc_edges as s4


def _mock_llm_response(content: str):
    mock_choice = MagicMock()
    mock_choice.message.content = content
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


def test_load_regulatory_clauses_returns_dict_keyed_by_standard():
    clauses = s4.load_regulatory_clauses()

    assert "ISO 13485 7.3.3" in clauses
    assert "summary" in clauses["ISO 13485 7.3.3"]
    assert len(clauses["ISO 13485 7.3.3"]["summary"]) > 10


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_llm_match_batch_injects_clause_summary_into_prompt(mock_create):
    mock_create.return_value = _mock_llm_response("无")
    guide = {
        "name": "Requirement -> DesignInput traceability",
        "standard": "ISO 13485 7.3.3",
        "rationale": "Each customer requirement should trace to at least one design input",
    }
    src_batch = [(0, "[R-01] 体温测量范围 35-42℃")]
    tgt_batch = [(0, "[DI-01] 温度显示范围 32-42.9℃")]

    s4._llm_match_batch(src_batch, tgt_batch, [{"req_id": "R-01"}], [{"di_id": "DI-01"}], guide, "requirements", "design_inputs")

    sent_prompt = mock_create.call_args.kwargs["messages"][0]["content"]
    assert "设计输入应基于预期用途确定功能" in sent_prompt


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_llm_match_batch_handles_unknown_standard_gracefully(mock_create):
    mock_create.return_value = _mock_llm_response("无")
    guide = {
        "name": "Person identity across documents",
        "standard": "Process",  # 不在 regulatory_clauses.yaml 里
        "rationale": "Same person appearing across different documents",
    }
    src_batch = [(0, "张三")]
    tgt_batch = [(0, "张三")]

    # 不应抛异常
    s4._llm_match_batch(src_batch, tgt_batch, [{"name": "张三"}], [{"name": "张三"}], guide, "persons", "persons")

    sent_prompt = mock_create.call_args.kwargs["messages"][0]["content"]
    assert "法规条款要点" not in sent_prompt


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_llm_match_batch_warns_when_standard_has_no_clause_data(mock_create, capsys):
    mock_create.return_value = _mock_llm_response("无")
    guide = {
        "name": "Person identity across documents",
        "standard": "Process",
        "rationale": "Same person appearing across different documents",
    }
    s4._llm_match_batch([(0, "张三")], [(0, "张三")], [{"name": "张三"}], [{"name": "张三"}], guide, "persons", "persons")

    captured = capsys.readouterr()
    assert "No clause summary found for standard 'Process'" in captured.out


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_llm_match_batch_no_warning_when_standard_has_clause_data(mock_create, capsys):
    mock_create.return_value = _mock_llm_response("无")
    guide = {
        "name": "Requirement -> DesignInput traceability",
        "standard": "ISO 13485 7.3.3",
        "rationale": "Each customer requirement should trace to at least one design input",
    }
    s4._llm_match_batch([(0, "R-01")], [(0, "DI-01")], [{"req_id": "R-01"}], [{"di_id": "DI-01"}], guide, "requirements", "design_inputs")

    captured = capsys.readouterr()
    assert "No clause summary found" not in captured.out


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_verify_candidates_open_llm_parses_known_and_new_relations(mock_create):
    mock_create.return_value = _mock_llm_response(
        "1. VERIFIED_BY\n2. 无关系\n3. 新关系：COMPONENT_OF"
    )
    candidates = [
        ({"control_id": "CM-01", "measure": "校准补偿"}, {"test_id": "T-12", "item": "线性度验证"}, "graph_pattern"),
        ({"control_id": "CM-02", "measure": "无关措施"}, {"test_id": "T-15", "item": "电池续航"}, "embedding"),
        ({"name": "下盖"}, {"name": "主机壳体"}, "bridge"),
    ]

    result = s4.verify_candidates_open_llm(candidates)

    assert result[0]["type"] == "VERIFIED_BY"
    assert result[0]["discovery_layer"] == "graph_pattern"
    assert len(result) == 2  # 第2条"无关系"被过滤
    assert result[1]["type"] == "COMPONENT_OF"
    assert result[1]["discovery_layer"] == "bridge"


def test_verify_candidates_open_llm_empty_candidates_returns_empty():
    assert s4.verify_candidates_open_llm([]) == []
