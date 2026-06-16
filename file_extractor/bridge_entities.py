# file_extractor/bridge_entities.py
"""Step4 候选生成层④：桥接实体发现（CodRED 思路）。

扫描节点文本字段，找出被两个以上不同来源文档共同提及的实体名
（产品型号、标准编号等），把共同提及该实体的节点两两配对，
作为不依赖文字相似度的候选关系来源。
"""
import re
from itertools import combinations

# 产品型号：大写字母+数字组合（如 PT9L）
PRODUCT_PATTERN = re.compile(r'\b[A-Z]{2,}[0-9]+[A-Z0-9]*\b')
# 标准编号：ISO/IEC/ASTM 等 + 数字
STANDARD_PATTERN = re.compile(r'\b(?:ISO|IEC|ASTM|GB|YY)\s?[\d\-\.]+(?:[:\-]\d+)?\b')

NODE_TEXT_FIELDS = {
    "risks": ["hazard", "hazardous_situation"],
    "risk_controls": ["measure"],
    "tests": ["item", "expected_value"],
    "requirements": ["description"],
    "design_inputs": ["description"],
    "regulations": ["requirement_text"],
}


def extract_entity_mentions(text: str) -> set:
    """从文本中提取候选桥接实体（产品型号、标准编号）。"""
    if not text:
        return set()
    mentions = set()
    mentions.update(PRODUCT_PATTERN.findall(text))
    mentions.update(m.strip() for m in STANDARD_PATTERN.findall(text))
    return mentions


def find_bridge_entities(nodes: dict) -> list[tuple]:
    """找出被两个以上不同来源文档共同提及实体的节点对。

    返回 [(node_a, node_b), ...]，只包含来源文档不同的配对。
    """
    # entity -> list of (node, node_type)
    entity_to_nodes = {}

    for node_type, fields in NODE_TEXT_FIELDS.items():
        for node in nodes.get(node_type, []):
            text = " ".join(str(node.get(f, "") or "") for f in fields)
            mentions = extract_entity_mentions(text)
            for entity in mentions:
                entity_to_nodes.setdefault(entity, []).append(node)

    pairs = []
    seen = set()
    for entity, node_list in entity_to_nodes.items():
        if len(node_list) < 2:
            continue
        for a, b in combinations(node_list, 2):
            if a.get("_source") == b.get("_source"):
                continue
            key = (id(a), id(b))
            if key in seen:
                continue
            seen.add(key)
            pairs.append((a, b))

    return pairs
