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


@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_uses_numpy_similarity_and_dedupes_pairs(mock_get_embeddings):
    node_a = {"hazard": "传感器漂移", "_source": "doc_a.md"}
    node_b = {"item": "高温线性度验证", "_source": "doc_b.md"}
    nodes = {"risks": [node_a], "tests": [node_b]}

    mock_get_embeddings.return_value = [[0.1, 0.2], [0.1, 0.2]]

    pairs = er.find_similar_pairs(nodes, top_k=10, threshold=0.5)

    assert len(pairs) == 1
    assert pairs[0] in [(node_a, node_b), (node_b, node_a)]
    mock_get_embeddings.assert_called_once()


@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_returns_empty_when_no_candidate_nodes(mock_get_embeddings):
    result = er.find_similar_pairs({"requirements": []})

    assert result == []
    mock_get_embeddings.assert_not_called()
