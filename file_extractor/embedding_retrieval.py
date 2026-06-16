# file_extractor/embedding_retrieval.py
"""Step4 候选生成层③：向量召回（MAQD 多角度查询 + 阿里云 DashScope embedding + Neo4j 向量索引检索）。"""
from openai import OpenAI
from neo4j import GraphDatabase

from config import (
    DASHSCOPE_API_KEY, DASHSCOPE_EMBEDDING_MODEL, DASHSCOPE_BASE_URL,
    NEO4J_URI, NEO4J_AUTH,
)

dashscope_client = OpenAI(api_key=DASHSCOPE_API_KEY, base_url=DASHSCOPE_BASE_URL)

EMBEDDING_BATCH_SIZE = 10  # text-embedding-v3 单批最多 10 条文本
EMBEDDING_DIMENSIONS = 1024
SIMILARITY_THRESHOLD = 0.5
TOP_K = 10

NODE_SUMMARY_FIELDS = {
    "requirements": ["description"],
    "design_inputs": ["description"],
    "risks": ["hazard", "hazardous_situation"],
    "risk_controls": ["measure"],
    "tests": ["item", "expected_value"],
}


def build_multi_aspect_queries(node: dict, node_type: str) -> list[str]:
    """为节点生成多角度查询文本（MAQD：原描述 + 数值指标）。"""
    fields = NODE_SUMMARY_FIELDS.get(node_type, [])
    queries = []

    desc_parts = [str(node.get(f, "") or "") for f in fields]
    desc = " ".join(p for p in desc_parts if p).strip()
    if desc:
        queries.append(desc)

    value = str(node.get("value", "") or "")
    unit = str(node.get("unit", "") or "")
    if value:
        queries.append(f"{desc} {value}{unit}".strip())

    return [q for q in queries if q]


def get_embeddings_batch(texts: list[str]) -> list[list[float]]:
    """调用 DashScope text-embedding-v3，按 10 条/批分批请求。"""
    if not texts:
        return []
    all_embeddings = []
    for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[i:i + EMBEDDING_BATCH_SIZE]
        response = dashscope_client.embeddings.create(
            model=DASHSCOPE_EMBEDDING_MODEL,
            input=batch,
        )
        all_embeddings.extend([item.embedding for item in response.data])
    return all_embeddings


def find_similar_pairs(nodes: dict, top_k: int = TOP_K,
                        threshold: float = SIMILARITY_THRESHOLD) -> list[tuple]:
    """对所有节点生成多角度查询向量，写入 Neo4j 向量索引，再用该索引检索语义相近的跨文档候选对。

    每个节点的每个查询角度对应一个临时 :EmbeddingRef 节点（key 格式
    "{node_type}::{node_index}::{query_index}"），查询时用 key 反查回
    Python 端的原始节点对象。每次运行先清空上一轮的 :EmbeddingRef 节点，
    避免跨运行残留干扰检索结果。
    """
    entries = []  # (key, node, node_type, query_text)
    for node_type in NODE_SUMMARY_FIELDS:
        for idx, node in enumerate(nodes.get(node_type, [])):
            for q_idx, query in enumerate(build_multi_aspect_queries(node, node_type)):
                entries.append((f"{node_type}::{idx}::{q_idx}", node, node_type, query))

    if not entries:
        return []

    texts = [e[3] for e in entries]
    embeddings = get_embeddings_batch(texts)
    key_to_node = {e[0]: e[1] for e in entries}

    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    try:
        with driver.session() as session:
            session.run("""
                CREATE VECTOR INDEX embeddingRefIndex IF NOT EXISTS
                FOR (n:EmbeddingRef) ON (n.embedding)
                OPTIONS {indexConfig: {`vector.dimensions`: %d, `vector.similarity_function`: 'cosine'}}
            """ % EMBEDDING_DIMENSIONS)
            session.run("MATCH (n:EmbeddingRef) DETACH DELETE n")

            for (key, _node, node_type, _query), embedding in zip(entries, embeddings):
                session.run(
                    "CREATE (n:EmbeddingRef {key: $key, node_type: $node_type, embedding: $embedding})",
                    key=key, node_type=node_type, embedding=embedding,
                )

            pairs = []
            seen = set()
            for (key, node, _node_type, _query), embedding in zip(entries, embeddings):
                result = session.run(
                    """
                    CALL db.index.vector.queryNodes('embeddingRefIndex', $top_k, $embedding)
                    YIELD node, score
                    RETURN node.key AS key, score
                    """,
                    top_k=top_k + 1, embedding=embedding,  # +1 因为会查到自己
                )
                for record in result:
                    other_key, score = record["key"], record["score"]
                    if other_key == key or score < threshold:
                        continue
                    other_node = key_to_node.get(other_key)
                    if other_node is None or other_node.get("_source") == node.get("_source"):
                        continue
                    pair_id = tuple(sorted([id(node), id(other_node)]))
                    if pair_id in seen:
                        continue
                    seen.add(pair_id)
                    pairs.append((node, other_node))
    finally:
        driver.close()

    return pairs
