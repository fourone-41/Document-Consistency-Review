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
