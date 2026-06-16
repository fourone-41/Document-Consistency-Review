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
# 连续中文字符片段（中文不分词，用于切出候选实体短语的候选窗口）
HAN_RUN_PATTERN = re.compile(r'[一-鿿]+')

# 中文实体短语的 n-gram 窗口长度范围（如"红外传感器"长度为5）
CN_NGRAM_MIN = 4
CN_NGRAM_MAX = 6

NODE_TEXT_FIELDS = {
    "risks": ["hazard", "hazardous_situation"],
    "risk_controls": ["measure"],
    "tests": ["item", "expected_value"],
    "requirements": ["description"],
    "design_inputs": ["description"],
    "regulations": ["requirement_text"],
}


def extract_entity_mentions(text: str) -> set:
    """从文本中提取候选桥接实体（产品型号、标准编号、中文实体短语）。"""
    if not text:
        return set()
    mentions = set()
    mentions.update(PRODUCT_PATTERN.findall(text))
    mentions.update(m.strip() for m in STANDARD_PATTERN.findall(text))

    # 中文没有空格分词，用连续汉字片段上的滑动窗口 n-gram 作为候选实体短语；
    # 是否真正构成"桥接实体"由 find_bridge_entities 中要求至少两个不同来源
    # 节点共同命中来过滤，因此这里允许召回较泛的候选片段。
    for run in HAN_RUN_PATTERN.findall(text):
        max_n = min(CN_NGRAM_MAX, len(run))
        for n in range(CN_NGRAM_MIN, max_n + 1):
            for i in range(len(run) - n + 1):
                mentions.add(run[i:i + n])

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
