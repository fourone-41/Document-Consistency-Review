# file_extractor/embedding_retrieval.py
"""Step4 候选生成层③：向量召回（MAQD 多角度查询 + 阿里云 DashScope embedding）。

相似度计算完全在 Python 内存中完成（numpy 余弦相似度矩阵），不依赖 Neo4j
向量索引——Neo4j 向量索引是异步填充的，创建节点后立刻查询会无限等待索引
ONLINE，是导致 Step4 反复卡死的根本原因。
"""
import numpy as np
from openai import OpenAI

from config import (
    DASHSCOPE_API_KEY, DASHSCOPE_EMBEDDING_MODEL, DASHSCOPE_BASE_URL,
)

dashscope_client = OpenAI(api_key=DASHSCOPE_API_KEY, base_url=DASHSCOPE_BASE_URL, timeout=30.0)

EMBEDDING_BATCH_SIZE = 10  # text-embedding-v3 单批最多 10 条文本
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

    desc_parts = [str(node.get(f, "") or "") for f in fields]
    desc = " ".join(p for p in desc_parts if p).strip()

    queries = []
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
    """对所有节点生成多角度查询向量，用 numpy 余弦相似度矩阵找跨文档候选对。

    不使用 Neo4j 向量索引——Neo4j 向量索引异步填充，创建节点后立刻查询
    会阻塞等待索引 ONLINE，是导致 Step4 卡死的根本原因。
    直接在 Python 内存中一次矩阵乘法完成全量相似度计算，速度快几百倍。
    """
    entries = []  # (key, node, node_type, query_text)
    for node_type in NODE_SUMMARY_FIELDS:
        for idx, node in enumerate(nodes.get(node_type, [])):
            for q_idx, query in enumerate(build_multi_aspect_queries(node, node_type)):
                entries.append((f"{node_type}::{idx}::{q_idx}", node, node_type, query))

    if not entries:
        return []

    print(f"    [embedding] {len(entries)} 条文本 → DashScope...", end="", flush=True)
    texts = [e[3] for e in entries]
    embeddings = get_embeddings_batch(texts)
    print(f" done. 计算相似度矩阵...", end="", flush=True)

    # 余弦相似度矩阵：一次矩阵乘法，O(N²) 但 N≤500 完全可接受
    emb = np.array(embeddings, dtype=np.float32)
    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    emb_norm = emb / np.where(norms > 0, norms, 1.0)
    sim_matrix = emb_norm @ emb_norm.T  # shape: (N, N)

    pairs = []
    seen = set()
    for i, (_, node_i, _, _) in enumerate(entries):
        sims = sim_matrix[i].copy()
        sims[i] = 0.0  # 排除自身
        top_indices = np.argpartition(sims, -min(top_k, len(sims) - 1))[-top_k:]
        for j in top_indices:
            if sims[j] < threshold:
                continue
            _, node_j, _, _ = entries[j]
            if node_i.get("_source") == node_j.get("_source"):
                continue
            pair_id = tuple(sorted([id(node_i), id(node_j)]))
            if pair_id in seen:
                continue
            seen.add(pair_id)
            pairs.append((node_i, node_j))

    print(f" {len(pairs)} 对候选.", flush=True)
    return pairs


# 节点文本字段优先级表（不依赖节点类型，用于 graph_pattern 候选排序）
_TEXT_FIELDS = ["description", "measure", "item", "expected_value",
                "hazard", "hazardous_situation", "name", "title", "content"]


def _node_to_text(node: dict) -> str:
    parts = [str(node.get(f, "") or "") for f in _TEXT_FIELDS]
    return " ".join(p for p in parts if p).strip()[:300]


def rank_candidate_pairs_by_embedding(pairs: list[tuple], top_n: int) -> list[tuple]:
    """对 (node_a, node_b, layer) 候选对按 embedding 余弦相似度排序，返回 top_n。

    专门用于 graph_pattern 候选的二次筛选：图模式传播产出的候选不携带语义证据，
    通过 embedding 相似度排序后截断，让 LLM 只验证最有可能存在关系的 top_n 对。
    相比 find_similar_pairs 的全量矩阵，这里只对这批特定候选对计算，开销小。
    """
    if len(pairs) <= top_n:
        return pairs

    # 收集唯一节点，避免重复 embedding
    node_by_id: dict[int, dict] = {}
    for node_a, node_b, _ in pairs:
        node_by_id[id(node_a)] = node_a
        node_by_id[id(node_b)] = node_b

    valid_nids = []
    valid_texts = []
    for nid, node in node_by_id.items():
        t = _node_to_text(node)
        if t:
            valid_nids.append(nid)
            valid_texts.append(t)

    if not valid_nids:
        return pairs[:top_n]

    print(f"    [embedding排序] {len(valid_texts)} 节点 → DashScope...", end="", flush=True)
    raw_embs = get_embeddings_batch(valid_texts)
    print(" done.", flush=True)

    emb = np.array(raw_embs, dtype=np.float32)
    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    emb_norm = emb / np.where(norms > 0, norms, 1.0)
    nid_to_emb = {nid: emb_norm[i] for i, nid in enumerate(valid_nids)}

    scored = []
    for node_a, node_b, layer in pairs:
        ea = nid_to_emb.get(id(node_a))
        eb = nid_to_emb.get(id(node_b))
        score = float(np.dot(ea, eb)) if ea is not None and eb is not None else 0.0
        scored.append((node_a, node_b, layer, score))

    scored.sort(key=lambda x: x[3], reverse=True)
    top = scored[:top_n]
    print(f"    graph_pattern 候选 {len(pairs)} → embedding排序后保留 top {len(top)}", flush=True)
    return [(a, b, lay) for a, b, lay, _ in top]
