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


def test_build_id_to_type_index_maps_ids_to_node_types():
    nodes = {
        "risk_controls": [{"control_id": "CM-01"}],
        "tests": [{"test_id": "T-12"}],
    }

    index = s4._build_id_to_type_index(nodes)

    assert index["CM-01"] == "risk_controls"
    assert index["T-12"] == "tests"


def test_normalize_step2_edges_resolves_types_and_skips_unresolvable():
    id_to_type = {"CM-01": "risk_controls", "T-12": "tests"}
    existing_edges = [
        {"type": "VERIFIED_BY", "from": "CM-01", "to": "T-12", "properties": {}},
        {"type": "SIGNED", "from": "某个查不到类型的标识符", "to": "也查不到", "properties": {}},
    ]

    normalized = s4._normalize_step2_edges(existing_edges, id_to_type)

    assert len(normalized) == 1
    assert normalized[0] == {
        "type": "VERIFIED_BY",
        "from_id": "CM-01", "from_type": "risk_controls",
        "to_id": "T-12", "to_type": "tests",
    }


@patch("step4_cross_doc_edges.verify_candidates_open_llm")
@patch("step4_cross_doc_edges.gpp.find_missing_next_hop")
@patch("step4_cross_doc_edges.er.find_similar_pairs")
@patch("step4_cross_doc_edges.be.find_bridge_entities")
def test_discover_open_candidates_merges_and_dedupes_all_layers(
    mock_bridge, mock_embedding, mock_graph_pattern, mock_verify
):
    node_a = {"control_id": "CM-01"}
    node_b = {"test_id": "T-12"}
    node_c = {"test_id": "T-15"}

    mock_bridge.return_value = [(node_a, node_b)]
    mock_embedding.return_value = [(node_a, node_b)]  # 与桥接层产出同一对，去重后应只算一次
    mock_graph_pattern.return_value = [
        {"from_id": "CM-01", "from_type": "risk_controls",
         "expected_relation": ("MITIGATED_BY", "VERIFIED_BY"),
         "candidate_targets": [node_c], "target_type": "tests"},  # 指向不同节点，应保留为独立候选
    ]
    mock_verify.return_value = [
        {"from": node_a, "to": node_c, "type": "VERIFIED_BY", "discovery_layer": "graph_pattern"},
    ]

    result = s4.discover_open_candidates(
        {"risk_controls": [node_a], "tests": [node_b, node_c]}, []
    )

    assert len(result) == 2
    assert result[0]["discovery_layer"] == "bridge"
    assert result[0]["type"] == "SEMANTICALLY_RELATED"
    # bridge/embedding 直接输出；验证函数只收到 graph_pattern 候选。
    verify_call_candidates = mock_verify.call_args.args[0]
    assert len(verify_call_candidates) == 1
    assert verify_call_candidates[0] == (node_a, node_c, "graph_pattern")


@patch("step4_cross_doc_edges.er.rank_candidate_pairs_by_embedding")
def test_select_graph_pattern_candidates_recall_first_does_not_require_embedding_rank(mock_rank):
    from_node_a = {"control_id": "CM-01", "measure": "防反接结构"}
    from_node_b = {"control_id": "CM-02", "measure": "软件异常处理"}
    candidates = []
    for i in range(8):
        candidates.append({
            "from": from_node_a if i < 6 else from_node_b,
            "to": {"test_id": f"T-{i}", "item": f"测试项{i}"},
            "expected_relation": ("MITIGATED_BY", "VERIFIED_BY"),
            "pattern_frequency": 12,
        })

    selected = s4._select_graph_pattern_candidates_recall_first(
        candidates,
        budget=4,
        per_from_node=1,
    )

    mock_rank.assert_not_called()
    assert len(selected) == 4
    selected_from_ids = {item[0].get("control_id") for item in selected}
    assert selected_from_ids == {"CM-01", "CM-02"}


@patch("step4_cross_doc_edges.verify_candidates_open_llm")
@patch("step4_cross_doc_edges.gpp.find_missing_next_hop")
@patch("step4_cross_doc_edges.er.find_similar_pairs")
@patch("step4_cross_doc_edges.be.find_bridge_entities")
def test_discover_open_candidates_propagates_verification_failure(
    mock_bridge, mock_embedding, mock_graph_pattern, mock_verify
):
    # 三层候选生成都正常返回，但最后的开放式验证调用本身抛异常 ——
    # 这种异常发生在 discover_open_candidates 内部唯一没有 try/except 包裹的地方，
    # 应该原样向外传播，由调用方（main()）的 try/except 兜底，而不是在这里被吞掉。
    mock_bridge.return_value = []
    mock_embedding.return_value = []
    mock_graph_pattern.return_value = []
    mock_verify.side_effect = RuntimeError("LLM verification blew up")

    import pytest
    with pytest.raises(RuntimeError, match="LLM verification blew up"):
        s4.discover_open_candidates({}, [])
