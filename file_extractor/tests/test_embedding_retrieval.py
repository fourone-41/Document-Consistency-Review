# file_extractor/tests/test_embedding_retrieval.py
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

import embedding_retrieval as er


def _mock_embedding_response(vectors: list[list[float]]):
    mock_response = MagicMock()
    mock_response.data = [MagicMock(embedding=v) for v in vectors]
    return mock_response


def test_build_multi_aspect_queries_includes_description_and_value():
    node = {"description": "体温测量范围", "value": "35-42", "unit": "℃"}

    queries = er.build_multi_aspect_queries(node, "requirements")

    assert "体温测量范围" in queries
    assert any("35-42" in q for q in queries)


def test_build_multi_aspect_queries_dedupes_empty_aspects():
    node = {"description": "", "value": "", "unit": ""}

    queries = er.build_multi_aspect_queries(node, "requirements")

    assert queries == []


@patch("embedding_retrieval.dashscope_client.embeddings.create")
def test_get_embeddings_batch_calls_dashscope_with_correct_model(mock_create):
    mock_create.return_value = _mock_embedding_response([[0.1, 0.2, 0.3]])

    result = er.get_embeddings_batch(["体温测量范围"])

    assert result == [[0.1, 0.2, 0.3]]
    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == er.DASHSCOPE_EMBEDDING_MODEL
    assert call_kwargs["input"] == ["体温测量范围"]


@patch("embedding_retrieval.dashscope_client.embeddings.create")
def test_get_embeddings_batch_respects_batch_size_limit(mock_create):
    mock_create.return_value = _mock_embedding_response([[0.1]] * 10)

    texts = [f"text-{i}" for i in range(15)]
    er.get_embeddings_batch(texts)

    # DashScope text-embedding-v3 单批最多 10 条
    assert mock_create.call_count == 2
    assert len(mock_create.call_args_list[0].kwargs["input"]) == 10
    assert len(mock_create.call_args_list[1].kwargs["input"]) == 5


@patch("embedding_retrieval.GraphDatabase")
@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_queries_neo4j_vector_index_and_maps_results_back(
    mock_get_embeddings, mock_graph_db
):
    node_a = {"hazard": "传感器漂移", "_source": "doc_a.md"}
    node_b = {"item": "高温线性度验证", "_source": "doc_b.md"}
    nodes = {"risks": [node_a], "tests": [node_b]}

    mock_get_embeddings.return_value = [[0.1, 0.2], [0.1, 0.2]]

    mock_session = MagicMock()
    mock_graph_db.driver.return_value.session.return_value.__enter__.return_value = mock_session

    risk_key = "risks::0::0"
    test_key = "tests::0::0"

    # 按调用顺序预设向量索引查询的返回结果：
    # 第1次查询（risks::0::0 的检索）命中 tests::0::0；
    # 第2次查询（tests::0::0 的检索）命中 risks::0::0 —— 这一对应该与第1次去重为同一对，不是两对。
    queryNodes_results = [
        [{"key": test_key, "score": 0.9}],
        [{"key": risk_key, "score": 0.9}],
    ]

    def run_side_effect(query, **kwargs):
        mock_result = MagicMock()
        if "CALL db.index.vector.queryNodes" in query:
            records = queryNodes_results.pop(0) if queryNodes_results else []
            mock_result.__iter__.return_value = iter(records)
        else:
            mock_result.__iter__.return_value = iter([])
        return mock_result

    mock_session.run.side_effect = run_side_effect

    pairs = er.find_similar_pairs(nodes, top_k=10, threshold=0.5)

    assert len(pairs) == 1
    assert pairs[0] in [(node_a, node_b), (node_b, node_a)]
    # 确认创建了向量索引
    create_index_calls = [
        c for c in mock_session.run.call_args_list
        if "CREATE VECTOR INDEX" in c.args[0]
    ]
    assert len(create_index_calls) == 1


@patch("embedding_retrieval.GraphDatabase")
@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_returns_empty_when_no_candidate_nodes(mock_get_embeddings, mock_graph_db):
    result = er.find_similar_pairs({"requirements": []})

    assert result == []
    mock_get_embeddings.assert_not_called()
    mock_graph_db.driver.assert_not_called()
