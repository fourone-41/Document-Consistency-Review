# file_extractor/graph_pattern_propagation.py
"""Step4 候选生成层②：图模式传播（Think-on-Graph 思路）。

从已有边（文档内边 + 层①已发现的跨文档边）出发，统计高频二跳模式，
对只完成第一跳、缺第二跳的节点，把该类型全部候选目标节点纳入候选对。
"""
from collections import defaultdict

NODE_ID_FIELD = {
    "requirements": "req_id",
    "design_inputs": "di_id",
    "risks": "risk_id",
    "risk_controls": "control_id",
    "tests": "test_id",
    "plan_tasks": "name",
    "documents": "title",
}


def count_two_hop_patterns(edges: list[dict]) -> dict:
    """统计二跳边类型序列出现频次：(edge1_type, edge2_type) -> count。

    二跳指：edge1 的 to_id 等于某条 edge2 的 from_id（同一个中间节点）。
    """
    by_from = defaultdict(list)
    for e in edges:
        by_from[e["from_id"]].append(e)

    pattern_counts = defaultdict(int)
    for e1 in edges:
        for e2 in by_from.get(e1["to_id"], []):
            if e1 is e2:
                continue
            pattern_counts[(e1["type"], e2["type"])] += 1

    return dict(pattern_counts)


def find_missing_next_hop(nodes: dict, edges: list[dict], min_frequency: int = 3) -> list[dict]:
    """对高频二跳模式，找出只完成第一跳、缺第二跳的节点，把第二跳候选目标节点纳入候选。

    返回格式：[{"from_id": ..., "from_type": ..., "expected_relation": (type1, type2),
                "candidate_targets": [node, ...], "target_type": ...}, ...]
    """
    pattern_counts = count_two_hop_patterns(edges)
    high_freq_patterns = {p: c for p, c in pattern_counts.items() if c >= min_frequency}
    if not high_freq_patterns:
        return []

    # 为每个高频模式找出 edge1/edge2 的实际 from_type/to_type
    pattern_types = {}
    for e1 in edges:
        for e2 in edges:
            key = (e1["type"], e2["type"])
            if key in high_freq_patterns and key not in pattern_types:
                if e1["to_id"] == e2["from_id"]:
                    pattern_types[key] = (e1["to_type"], e2["to_type"])

    # 找出已完成第一跳的中间节点
    second_hop_from_ids = {e["from_id"] for e in edges}

    completed_first_hop_by_pattern = defaultdict(set)
    for e in edges:
        for (t1, t2), count in high_freq_patterns.items():
            if e["type"] == t1:
                completed_first_hop_by_pattern[(t1, t2)].add(e["to_id"])

    results = []
    for pattern, intermediate_ids in completed_first_hop_by_pattern.items():
        if pattern not in pattern_types:
            continue
        intermediate_type, target_type = pattern_types[pattern]
        candidate_targets = nodes.get(target_type, [])

        for mid_id in intermediate_ids:
            if mid_id in second_hop_from_ids:
                continue  # 第二跳已存在，不缺
            results.append({
                "from_id": mid_id,
                "from_type": intermediate_type,
                "expected_relation": pattern,
                "candidate_targets": candidate_targets,
                "target_type": target_type,
            })

    return results
