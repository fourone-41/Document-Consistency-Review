"""Step 4: Cross-document relationship discovery.

Combines:
1. Regulatory knowledge guide (ISO 13485, ISO 14971, IEC 62304, DHF process)
2. Three-layer matching: exact -> fuzzy -> LLM semantic
3. Tiered output: high/medium/low confidence
"""
import argparse
import json
import re
import time
import sys
import yaml
from pathlib import Path
from difflib import SequenceMatcher
from openai import OpenAI

sys.path.insert(0, str(Path(__file__).parent))
from config import API_KEY, LLM_BASE_URL, LLM_MODEL, LLM_MAX_TOKENS
import bridge_entities as be
import embedding_retrieval as er
import graph_pattern_propagation as gpp

client = OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL, timeout=60.0)

MERGED_PATH = Path(__file__).parent / "output" / "merged_graph.json"
OUTPUT_DIR = Path(__file__).parent / "output"
REGULATORY_CLAUSES_PATH = Path(__file__).parent / "regulatory_clauses.yaml"

# graph_pattern 候选送 LLM 前的上限（fast 模式）。
# 图模式传播在全量数据集下可能产出数千候选，全部送 LLM 需要数百次调用、数小时。
# fast 模式先用 embedding 相似度排序，取 top N 送 LLM；full 模式不截断。
MAX_GRAPH_PATTERN_CANDIDATES = 200
RECALL_GRAPH_PATTERN_CANDIDATES = 800
RECALL_PER_FROM_NODE = 3
RECALL_LOW_SEMANTIC_EXPLORATION_RATIO = 0.10


def load_regulatory_clauses() -> dict:
    """加载 regulatory_clauses.yaml 中的 ISO 条款转述要点，按标准编号索引。"""
    with open(REGULATORY_CLAUSES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["clauses"]


# ============================================================
# Regulatory Knowledge Guide
# These define EXPECTED relationships per standards/process
# Used to GUIDE search, not to audit compliance
# ============================================================
REGULATORY_GUIDES = [
    {
        "name": "Requirement -> DesignInput traceability",
        "standard": "ISO 13485 7.3.3",
        "source_type": "requirements",
        "target_type": "design_inputs",
        "edge_type": "TRACES_TO",
        "match_strategy": "description_similarity",
        "rationale": "Each customer requirement should trace to at least one design input",
    },
    {
        "name": "DesignInput -> Test verification",
        "standard": "ISO 13485 7.3.6",
        "source_type": "design_inputs",
        "target_type": "tests",
        "edge_type": "VERIFIED_BY",
        "match_strategy": "value_and_description",
        "rationale": "Each design input should have verification test evidence",
    },
    {
        "name": "Risk -> RiskControl mitigation",
        "standard": "ISO 14971 7.1",
        "source_type": "risks",
        "target_type": "risk_controls",
        "edge_type": "MITIGATED_BY",
        "match_strategy": "id_prefix_match",
        "rationale": "Each identified risk should have control measures",
    },
    {
        "name": "RiskControl -> Test validation",
        "standard": "ISO 14971 8",
        "source_type": "risk_controls",
        "target_type": "tests",
        "edge_type": "VALIDATED_BY",
        "match_strategy": "description_similarity",
        "rationale": "Risk control measures should have verification evidence",
    },
    {
        "name": "Requirement -> Test coverage",
        "standard": "ISO 13485 7.3.6/7.3.7",
        "source_type": "requirements",
        "target_type": "tests",
        "edge_type": "TESTED_BY",
        "match_strategy": "value_and_description",
        "rationale": "Product requirements should be verified by tests",
    },
    {
        "name": "SoftwareItem -> Test verification",
        "standard": "IEC 62304 5.7",
        "source_type": "software_items",
        "target_type": "tests",
        "edge_type": "VERIFIED_BY",
        "match_strategy": "description_similarity",
        "rationale": "Software requirements need verification testing",
    },
    {
        "name": "PlanTask -> Document output",
        "standard": "ISO 13485 7.3.2",
        "source_type": "plan_tasks",
        "target_type": "documents",
        "edge_type": "PRODUCES",
        "match_strategy": "name_contains",
        "rationale": "Plan tasks should produce documented outputs",
    },
    {
        "name": "DocIndexEntry -> Document existence",
        "standard": "DHF Process",
        "source_type": "doc_index_entries",
        "target_type": "documents",
        "edge_type": "REFERENCES_DOC",
        "match_strategy": "filename_match",
        "rationale": "DHF index entries should correspond to actual documents",
    },
    {
        "name": "Regulation -> Requirement implementation",
        "standard": "ISO 13485 7.1",
        "source_type": "regulations",
        "target_type": "requirements",
        "edge_type": "IMPLEMENTED_BY",
        "match_strategy": "description_similarity",
        "rationale": "Applicable regulations should have implementing requirements",
    },
    {
        "name": "Regulation -> DesignInput implementation",
        "standard": "ISO 13485 7.3.3",
        "source_type": "regulations",
        "target_type": "design_inputs",
        "edge_type": "IMPLEMENTED_BY",
        "match_strategy": "description_similarity",
        "rationale": "Regulatory requirements should be reflected in design inputs",
    },
    {
        "name": "Function -> Test verification",
        "standard": "ISO 13485 7.3.6",
        "source_type": "functions",
        "target_type": "tests",
        "edge_type": "VERIFIED_BY",
        "match_strategy": "name_similarity",
        "rationale": "Product functions should be tested",
    },
    {
        "name": "Person identity across documents",
        "standard": "Process",
        "source_type": "persons",
        "target_type": "persons",
        "edge_type": "SAME_AS",
        "match_strategy": "person_dedup",
        "rationale": "Same person appearing across different documents",
    },
]


def load_graph():
    data = json.loads(MERGED_PATH.read_text(encoding="utf-8"))
    return data["nodes"], data.get("edges", []), data.get("claims", [])


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    a_lower = a.lower().strip()
    b_lower = b.lower().strip()
    if a_lower == b_lower:
        return 1.0
    if a_lower in b_lower or b_lower in a_lower:
        return 0.85
    return SequenceMatcher(None, a_lower, b_lower).ratio()


def tokenize_chinese(text: str) -> set:
    if not text:
        return set()
    words = set(re.findall(r'[\u4e00-\u9fff]{2,}', text))
    words.update(re.findall(r'[a-zA-Z0-9]+', text))
    return words


def keyword_overlap(a: str, b: str) -> float:
    tokens_a = tokenize_chinese(a)
    tokens_b = tokenize_chinese(b)
    if not tokens_a or not tokens_b:
        return 0.0
    common = tokens_a & tokens_b
    return len(common) / min(len(tokens_a), len(tokens_b))


# ============================================================
# Layer 1: Exact matching
# ============================================================
def match_exact_id(source_items, target_items, src_id_field, tgt_id_field):
    """Match by exact ID field."""
    edges = []
    tgt_by_id = {}
    for t in target_items:
        tid = t.get(tgt_id_field, "")
        if tid:
            tgt_by_id[tid] = t

    for s in source_items:
        sid = s.get(src_id_field, "")
        if sid and sid in tgt_by_id:
            edges.append((s, tgt_by_id[sid], "high"))
    return edges


def match_id_prefix(source_items, target_items, src_id_field, tgt_id_field):
    """Match by ID prefix (e.g., RC-R1 -> R1)."""
    edges = []
    for s in source_items:
        sid = s.get(src_id_field, "")
        if not sid:
            continue
        for t in target_items:
            tid = t.get(tgt_id_field, "")
            if not tid:
                continue
            if tid in sid or sid in tid:
                edges.append((s, t, "high"))
    return edges


def match_filename(source_items, target_items):
    """Match DHF index entries to documents by filename."""
    edges = []
    for s in source_items:
        fname = s.get("file_name", "")
        if not fname:
            continue
        for t in target_items:
            title = t.get("title", "")
            if not title:
                continue
            if similarity(fname, title) > 0.6 or fname in title or title in fname:
                conf = "high" if similarity(fname, title) > 0.8 else "medium"
                edges.append((s, t, conf))
                break
    return edges


def match_person_dedup(persons):
    """Find same person across different source files."""
    edges = []
    seen = {}
    for p in persons:
        name = (p.get("name") or "").strip()
        source = p.get("_source", "")
        if not name or len(name) < 2:
            continue
        if name in seen:
            if seen[name]["_source"] != source:
                edges.append((seen[name], p, "high"))
        else:
            seen[name] = p
    return edges


# ============================================================
# Layer 2: Fuzzy matching
# ============================================================
def match_description_similarity(source_items, target_items,
                                  src_desc_field="description",
                                  tgt_desc_field="description",
                                  threshold=0.5):
    """Match by description text similarity."""
    edges = []
    for s in source_items:
        s_desc = s.get(src_desc_field, "") or ""
        if not s_desc or len(s_desc) < 4:
            continue
        best_score = 0
        best_target = None
        for t in target_items:
            if t.get("_source") == s.get("_source"):
                continue
            t_desc = t.get(tgt_desc_field, "") or ""
            if not t_desc:
                continue
            score = keyword_overlap(s_desc, t_desc)
            if score > best_score:
                best_score = score
                best_target = t

        if best_target and best_score >= threshold:
            conf = "high" if best_score > 0.7 else "medium" if best_score > 0.5 else "low"
            edges.append((s, best_target, conf))
    return edges


def match_value_and_description(source_items, target_items,
                                 src_desc="description", tgt_desc="item"):
    """Match by combining value/unit match and description similarity."""
    edges = []
    for s in source_items:
        s_desc = s.get(src_desc, "") or ""
        s_val = str(s.get("value", "") or "")
        if not s_desc and not s_val:
            continue

        best_score = 0
        best_target = None
        for t in target_items:
            if t.get("_source") == s.get("_source"):
                continue
            t_desc = t.get(tgt_desc, "") or ""
            t_val = str(t.get("expected_value", "") or t.get("value", "") or "")

            desc_score = keyword_overlap(s_desc, t_desc) if s_desc and t_desc else 0
            val_score = 0.4 if (s_val and t_val and s_val in t_val) else 0
            combined = desc_score * 0.7 + val_score * 0.3

            if combined > best_score:
                best_score = combined
                best_target = t

        if best_target and best_score >= 0.35:
            conf = "high" if best_score > 0.6 else "medium" if best_score > 0.4 else "low"
            edges.append((s, best_target, conf))
    return edges


def match_name_contains(source_items, target_items):
    """Match PlanTask names to Document titles."""
    edges = []
    for s in source_items:
        note = s.get("note", "") or ""
        name = s.get("name", "") or ""
        combined = note + " " + name
        if not combined.strip():
            continue
        for t in target_items:
            title = t.get("title", "") or ""
            if not title or len(title) < 4:
                continue
            if title in combined or any(
                kw in combined for kw in tokenize_chinese(title) if len(kw) >= 3
            ):
                edges.append((s, t, "medium"))
                break
    return edges


def match_name_similarity(source_items, target_items):
    """Match functions to tests by name/item similarity."""
    edges = []
    for s in source_items:
        s_name = s.get("name", "") or ""
        if not s_name or len(s_name) < 2:
            continue
        for t in target_items:
            if t.get("_source") == s.get("_source"):
                continue
            t_item = t.get("item", "") or ""
            if not t_item:
                continue
            score = keyword_overlap(s_name, t_item)
            if score >= 0.4:
                conf = "high" if score > 0.7 else "medium"
                edges.append((s, t, conf))
                break
    return edges


# ============================================================
# Layer 3: LLM semantic matching (batch)
# ============================================================
def match_llm_semantic(source_items, target_items, guide, max_pairs=30):
    """Use LLM to validate candidate pairs with low rule-based scores."""
    candidates = []
    for s in source_items:
        s_desc = s.get("description", "") or s.get("name", "") or s.get("item", "") or ""
        if not s_desc or len(s_desc) < 4:
            continue
        for t in target_items:
            if t.get("_source") == s.get("_source"):
                continue
            t_desc = t.get("description", "") or t.get("item", "") or t.get("name", "") or ""
            if not t_desc or len(t_desc) < 4:
                continue
            score = keyword_overlap(s_desc, t_desc)
            if 0.2 <= score < 0.5:
                candidates.append((s, t, s_desc, t_desc))

    if not candidates:
        return []
    candidates = candidates[:max_pairs]

    prompt = f"""你是医疗器械文档关系分析专家。
根据{guide['standard']}的要求，判断以下节点对之间是否存在"{guide['name']}"的关系。

对每一对，输出 Y（有关系）或 N（无关系），一行一个，只输出 Y 或 N。

"""
    for i, (s, t, sd, td) in enumerate(candidates):
        prompt += f"{i+1}. [{sd[:80]}] <-> [{td[:80]}]\n"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content or ""
        lines = [l.strip() for l in content.strip().split("\n") if l.strip()]

        edges = []
        for i, line in enumerate(lines):
            if i >= len(candidates):
                break
            if "Y" in line.upper() and "N" not in line.upper():
                s, t, _, _ = candidates[i]
                edges.append((s, t, "low"))
        return edges
    except Exception as e:
        print(f"    LLM error: {e}")
        return []


# ============================================================
# Main orchestration
# ============================================================
def get_node_id(node, node_type):
    """Generate a readable ID for a node."""
    if node_type == "requirements":
        return node.get("req_id", "") or node.get("description", "")[:30]
    if node_type == "design_inputs":
        return node.get("di_id", "") or node.get("description", "")[:30]
    if node_type == "tests":
        return f"TEST-{node.get('test_id', '')}: {(node.get('item', '') or '')[:30]}"
    if node_type == "risks":
        return node.get("hazard", "") or node.get("risk_id", "") or ""
    if node_type == "risk_controls":
        return node.get("measure", "") or node.get("control_id", "") or ""
    if node_type == "plan_tasks":
        return f"WBS-{node.get('wbs', '')}: {(node.get('name', '') or '')[:30]}"
    if node_type == "doc_index_entries":
        return node.get("file_name", "") or f"#{node.get('seq', '')}"
    if node_type == "documents":
        return node.get("title", "")
    if node_type == "regulations":
        return f"{node.get('std_id', '')} {node.get('clause', '') or ''}"
    if node_type == "persons":
        return node.get("name", "")
    if node_type == "functions":
        return node.get("name", "")
    if node_type == "software_items":
        return node.get("name", "")
    return str(node)[:40]


def get_node_summary(node, node_type):
    """Get a concise text representation for LLM matching."""
    if node_type == "requirements":
        desc = node.get("description", "") or ""
        val = node.get("value", "") or ""
        unit = node.get("unit", "") or ""
        rid = node.get("req_id", "") or ""
        return f"[{rid}] {desc}" + (f" ({val}{unit})" if val else "")
    if node_type == "design_inputs":
        desc = node.get("description", "") or ""
        val = node.get("value", "") or ""
        unit = node.get("unit", "") or ""
        did = node.get("di_id", "") or ""
        return f"[{did}] {desc}" + (f" ({val}{unit})" if val else "")
    if node_type == "tests":
        item = node.get("item", "") or ""
        exp = node.get("expected_value", "") or ""
        tid = node.get("test_id", "") or ""
        return f"[T{tid}] {item}" + (f": {exp[:60]}" if exp else "")
    if node_type == "risks":
        hazard = node.get("hazard", "") or ""
        situation = node.get("hazardous_situation", "") or ""
        rid = node.get("risk_id", "") or ""
        return f"[{rid}] {hazard}" + (f" - {situation[:50]}" if situation else "")
    if node_type == "risk_controls":
        measure = node.get("measure", "") or ""
        cid = node.get("control_id", "") or ""
        evidence = node.get("evidence_type", "") or ""
        return f"[{cid}] {measure}" + (f" (evidence: {evidence[:40]})" if evidence else "")
    if node_type == "regulations":
        std = node.get("std_id", "") or ""
        clause = node.get("clause", "") or ""
        text = node.get("requirement_text", "") or ""
        return f"[{std} {clause}] {text[:80]}"
    if node_type == "functions":
        return node.get("name", "") or ""
    if node_type == "software_items":
        name = node.get("name", "") or ""
        desc = node.get("description", "") or ""
        return f"{name}: {desc}" if desc else name
    if node_type == "plan_tasks":
        name = node.get("name", "") or ""
        note = node.get("note", "") or ""
        wbs = node.get("wbs", "") or ""
        return f"[WBS-{wbs}] {name}" + (f" (output: {note[:50]})" if note else "")
    if node_type == "documents":
        return node.get("title", "") or ""
    if node_type == "doc_index_entries":
        return node.get("file_name", "") or ""
    return str(node)[:60]


def llm_batch_match(source_items, target_items, guide, src_type, tgt_type):
    """Use LLM to find matching pairs between source and target lists.
    
    Sends batches to LLM with full context of both lists,
    asks it to return matching pairs directly.
    """
    # Build concise representations
    src_list = []
    for i, s in enumerate(source_items):
        summary = get_node_summary(s, src_type)
        if summary.strip():
            src_list.append((i, summary[:120]))

    tgt_list = []
    for i, t in enumerate(target_items):
        summary = get_node_summary(t, tgt_type)
        if summary.strip():
            tgt_list.append((i, summary[:120]))

    if not src_list or not tgt_list:
        return []

    # Batch if lists are too large (max ~40 items per side per call)
    BATCH_SIZE = 40
    all_edges = []

    src_batches = [src_list[i:i+BATCH_SIZE] for i in range(0, len(src_list), BATCH_SIZE)]
    tgt_batches = [tgt_list[i:i+BATCH_SIZE] for i in range(0, len(tgt_list), BATCH_SIZE)]

    for sb in src_batches:
        for tb in tgt_batches:
            edges = _llm_match_batch(sb, tb, source_items, target_items, guide, src_type, tgt_type)
            all_edges.extend(edges)

    return all_edges


def _llm_match_batch(src_batch, tgt_batch, source_items, target_items, guide, src_type, tgt_type):
    """Single LLM call to match a batch of source vs target items."""
    clauses = load_regulatory_clauses()
    clause_summary = clauses.get(guide['standard'], {}).get('summary', '').strip()
    if not clause_summary:
        print(f"    [WARN] No clause summary found for standard '{guide['standard']}' "
              f"(guide: {guide['name']}) — proceeding without clause injection", flush=True)
    clause_block = f"\n法规条款要点：{clause_summary}\n" if clause_summary else ""

    prompt = f"""你是医疗器械文档关系分析专家。

任务：根据 {guide['standard']} 的要求，找出【源列表】和【目标列表】之间存在"{guide['name']}"关系的配对。

{guide['rationale']}
{clause_block}
【源列表 ({src_type})】:
"""
    for idx, (i, summary) in enumerate(src_batch):
        prompt += f"  S{idx+1}. {summary}\n"

    prompt += f"\n【目标列表 ({tgt_type})】:\n"
    for idx, (i, summary) in enumerate(tgt_batch):
        prompt += f"  T{idx+1}. {summary}\n"

    prompt += """
请输出所有匹配对，格式为每行一个：S编号-T编号
例如：S1-T3 表示源列表第1项与目标列表第3项存在关系。
只输出有明确对应关系的配对，不确定的不要输出。如果没有任何匹配，输出"无"。
"""

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content or ""

        edges = []
        for line in content.strip().split("\n"):
            line = line.strip()
            if not line or line == "无":
                continue
            m = re.match(r'S(\d+)\s*[-–—]\s*T(\d+)', line)
            if m:
                si = int(m.group(1)) - 1
                ti = int(m.group(2)) - 1
                if 0 <= si < len(src_batch) and 0 <= ti < len(tgt_batch):
                    src_orig_idx = src_batch[si][0]
                    tgt_orig_idx = tgt_batch[ti][0]
                    edges.append((source_items[src_orig_idx], target_items[tgt_orig_idx], "medium"))
        return edges
    except Exception as e:
        print(f"    LLM batch error: {e}")
        return []


OPEN_VERIFY_BATCH_SIZE = 20


def verify_candidates_open_llm(candidates: list[tuple]) -> list[dict]:
    """对层②③④产出的候选对做开放式 LLM 验证。

    candidates: [(node_a, node_b, discovery_layer), ...]
    未命中已知规则的候选，允许 LLM 直接给出"新关系：XXX"，不强制套用预定义类型。
    返回 [{"from": node_a, "to": node_b, "type": ..., "discovery_layer": ...}, ...]
    """
    if not candidates:
        return []

    all_results = []
    for i in range(0, len(candidates), OPEN_VERIFY_BATCH_SIZE):
        batch = candidates[i:i + OPEN_VERIFY_BATCH_SIZE]
        all_results.extend(_verify_batch_open_llm(batch))
    return all_results


def _verify_batch_open_llm(batch: list[tuple]) -> list[dict]:
    prompt = """你是医疗器械文档关系分析专家。

以下每一对节点是候选关系对，请判断它们之间是否存在关系：
- 如果存在已知关系类型（如 VERIFIED_BY、MITIGATED_BY、COVERS 等），直接输出该类型
- 如果存在关系但不属于已知类型，输出"新关系：你认为合适的类型名"
- 如果没有关系，输出"无关系"

按顺序逐条判断，格式：编号. 判断结果

"""
    for idx, (node_a, node_b, _layer) in enumerate(batch):
        desc_a = node_a.get("description") or node_a.get("measure") or node_a.get("item") or node_a.get("hazard") or node_a.get("name") or str(node_a)[:60]
        desc_b = node_b.get("description") or node_b.get("measure") or node_b.get("item") or node_b.get("hazard") or node_b.get("name") or str(node_b)[:60]
        prompt += f"{idx + 1}. [{desc_a[:80]}] <-> [{desc_b[:80]}]\n"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content or ""
    except Exception as e:
        print(f"    verify_candidates_open_llm ERROR: {e}", flush=True)
        return []

    results = []
    for line in content.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r'(\d+)\.\s*(.+)', line)
        if not m:
            continue
        idx = int(m.group(1)) - 1
        verdict = m.group(2).strip()
        if idx < 0 or idx >= len(batch):
            continue
        if "无关系" in verdict:
            continue
        node_a, node_b, layer = batch[idx]
        if "新关系" in verdict:
            rel_type = verdict.split("：", 1)[-1].split(":", 1)[-1].strip()
        else:
            rel_type = verdict
        if not rel_type:
            continue
        results.append({
            "from": node_a,
            "to": node_b,
            "type": rel_type,
            "discovery_layer": layer,
        })

    return results


# 节点类型 -> 唯一标识字段。用于把 Step2 的 {type, from, to} 边（只有字符串
# 标识符，没有类型信息）反查回节点类型，供图模式传播使用。
NODE_ID_FIELD = {
    "requirements": "req_id",
    "design_inputs": "di_id",
    "risks": "risk_id",
    "risk_controls": "control_id",
    "tests": "test_id",
    "plan_tasks": "name",
    "documents": "title",
}


def _node_id_field_for(node_type: str) -> str:
    return NODE_ID_FIELD.get(node_type, "name")


def _build_id_to_type_index(nodes: dict) -> dict:
    """构建 id值 -> node_type 的反查表。

    Step2 产出的文档内边（existing_edges）只有 {type, from, to}，没有携带
    节点类型信息；图模式传播需要知道每条边两端是什么类型才能统计模式，
    这里通过节点的唯一标识字段反查回类型。
    """
    index = {}
    for node_type, items in nodes.items():
        id_field = NODE_ID_FIELD.get(node_type)
        if not id_field:
            continue
        for item in items:
            id_val = str(item.get(id_field, "") or "")
            if id_val:
                index[id_val] = node_type
    return index


def _normalize_step2_edges(existing_edges: list[dict], id_to_type: dict) -> list[dict]:
    """把 Step2 的 {type, from, to} 边转换成图模式传播需要的
    {type, from_id, from_type, to_id, to_type} 形状。两端标识符查不到类型的边跳过
    （查不到通常是因为 from/to 不是某个已知节点类型的唯一标识，无法参与模式统计）。
    """
    normalized = []
    for e in existing_edges:
        from_id = str(e.get("from", "") or "")
        to_id = str(e.get("to", "") or "")
        from_type = id_to_type.get(from_id)
        to_type = id_to_type.get(to_id)
        if not from_type or not to_type:
            continue
        normalized.append({
            "type": e.get("type", ""),
            "from_id": from_id, "from_type": from_type,
            "to_id": to_id, "to_type": to_type,
        })
    return normalized


_ANCHOR_FIELDS = [
    "req_id", "di_id", "risk_id", "control_id", "test_id", "std_id", "clause",
    "description", "measure", "item", "expected_value", "hazard",
    "hazardous_situation", "name", "title", "file_name", "content", "value", "unit",
]

_STRUCTURAL_RELATION_PRIORITY = {
    ("MITIGATED_BY", "VERIFIED_BY"): 5,
    ("MITIGATED_BY", "VALIDATED_BY"): 5,
    ("TRACES_TO", "VERIFIED_BY"): 5,
    ("TRACES_TO", "TESTED_BY"): 5,
    ("IMPLEMENTED_BY", "VERIFIED_BY"): 4,
    ("IMPLEMENTED_BY", "TESTED_BY"): 4,
    ("PRODUCES", "REFERENCES_DOC"): 3,
}


def _node_text_for_anchors(node: dict) -> str:
    parts = [str(node.get(field, "") or "") for field in _ANCHOR_FIELDS]
    return " ".join(part for part in parts if part).lower()


def _extract_anchor_tokens(node: dict) -> set[str]:
    text = _node_text_for_anchors(node)
    tokens = set(re.findall(r"[A-Za-z]{1,10}-?\d+(?:[-.]\d+)*", text, re.I))
    tokens.update(re.findall(r"\d+(?:\.\d+)?\s*(?:℃|°c|c|mm|cm|kg|g|hz|mhz|v|ma|a|h|hour|小时|次|%)", text, re.I))
    tokens.update(tok for tok in tokenize_chinese(text) if len(tok) >= 2)
    return {tok.lower().strip() for tok in tokens if tok.strip()}


def _anchor_overlap_score(node_a: dict, node_b: dict) -> float:
    anchors_a = _extract_anchor_tokens(node_a)
    anchors_b = _extract_anchor_tokens(node_b)
    if not anchors_a or not anchors_b:
        return 0.0
    common = anchors_a & anchors_b
    return min(1.0, len(common) / max(1, min(len(anchors_a), len(anchors_b))))


def _candidate_structural_score(candidate: dict) -> float:
    pattern = tuple(candidate.get("expected_relation") or ())
    frequency = int(candidate.get("pattern_frequency") or 0)
    relation_priority = _STRUCTURAL_RELATION_PRIORITY.get(pattern, 2)
    anchor_score = _anchor_overlap_score(candidate["from"], candidate["to"])

    # 结构证据是主信号；锚点只作为加分，避免回到纯文本相似度筛选。
    return relation_priority * 10 + min(frequency, 20) + anchor_score * 5


def _select_graph_pattern_candidates_recall_first(
    candidates: list[dict],
    budget: int = RECALL_GRAPH_PATTERN_CANDIDATES,
    per_from_node: int = RECALL_PER_FROM_NODE,
) -> list[tuple]:
    """结构优先选择 graph_pattern 候选，embedding 只保留给 fast 模式使用。

    recall 模式的目标是减少结构性断链漏检：先保证每个缺第二跳的中间节点、
    每种高频模式都有候选进入 LLM，再把剩余预算给结构分最高的候选。
    """
    if len(candidates) <= budget:
        return [(c["from"], c["to"], "graph_pattern") for c in candidates]

    scored = []
    for idx, candidate in enumerate(candidates):
        candidate = dict(candidate)
        candidate["_idx"] = idx
        candidate["_score"] = _candidate_structural_score(candidate)
        candidate["_from_key"] = id(candidate["from"])
        candidate["_pattern_key"] = tuple(candidate.get("expected_relation") or ())
        scored.append(candidate)

    selected = []
    selected_ids = set()

    def add(candidate: dict) -> bool:
        if len(selected) >= budget:
            return False
        idx = candidate["_idx"]
        if idx in selected_ids:
            return False
        selected.append(candidate)
        selected_ids.add(idx)
        return True

    # 1) 覆盖每个缺边中间节点，避免少数语义相似节点吃掉所有预算。
    by_from = {}
    for candidate in sorted(scored, key=lambda c: c["_score"], reverse=True):
        bucket = by_from.setdefault(candidate["_from_key"], [])
        if len(bucket) < per_from_node:
            bucket.append(candidate)

    for bucket in by_from.values():
        for candidate in bucket:
            add(candidate)

    # 2) 覆盖每种高频二跳模式，保留 graph_pattern 的结构多样性。
    by_pattern = {}
    for candidate in sorted(scored, key=lambda c: c["_score"], reverse=True):
        by_pattern.setdefault(candidate["_pattern_key"], []).append(candidate)

    per_pattern_budget = max(per_from_node, budget // max(1, len(by_pattern)))
    for bucket in by_pattern.values():
        kept = 0
        for candidate in bucket:
            if kept >= per_pattern_budget:
                break
            if add(candidate):
                kept += 1

    # 3) 预留少量预算给“结构强但锚点/语义不明显”的探索样本。
    exploration_budget = int(budget * RECALL_LOW_SEMANTIC_EXPLORATION_RATIO)
    low_anchor = sorted(
        scored,
        key=lambda c: (int(c.get("pattern_frequency") or 0), _STRUCTURAL_RELATION_PRIORITY.get(c["_pattern_key"], 2)),
        reverse=True,
    )
    kept = 0
    for candidate in low_anchor:
        if kept >= exploration_budget:
            break
        if _anchor_overlap_score(candidate["from"], candidate["to"]) > 0:
            continue
        if add(candidate):
            kept += 1

    # 4) 剩余预算给综合结构分最高的候选。
    for candidate in sorted(scored, key=lambda c: c["_score"], reverse=True):
        if not add(candidate):
            if len(selected) >= budget:
                break

    print(
        f"    [recall模式] graph_pattern 候选 {len(candidates)} 对 → "
        f"结构优先保留 {len(selected)} 对 "
        f"(覆盖节点={len(by_from)}, 模式={len(by_pattern)})",
        flush=True,
    )
    return [(c["from"], c["to"], "graph_pattern") for c in selected]


def discover_open_candidates(nodes: dict, layer1_edges: list[dict],
                             graph_pattern_mode: str = "fast",
                             rank_graph_pattern: bool | None = None) -> list[dict]:
    """合并层②③④候选，去重后送开放式 LLM 验证，返回最终边列表。

    每一层独立失败不应中断整体流程（设计文档第6节降级策略）：
    某层抛异常时跳过该层，记录警告，继续用其余层的候选。
    """
    if rank_graph_pattern is not None:
        graph_pattern_mode = "fast" if rank_graph_pattern else "full"

    raw_candidates = []  # (node_a, node_b, layer)
    graph_pattern_candidates = []

    try:
        for a, b in be.find_bridge_entities(nodes):
            raw_candidates.append((a, b, "bridge"))
    except Exception as e:
        print(f"    [WARN] bridge_entities layer failed, skipping: {e}", flush=True)

    try:
        for a, b in er.find_similar_pairs(nodes):
            raw_candidates.append((a, b, "embedding"))
    except Exception as e:
        print(f"    [WARN] embedding_retrieval layer failed, skipping: {e}", flush=True)

    try:
        missing_hops = gpp.find_missing_next_hop(nodes, layer1_edges, min_frequency=3)
    except Exception as e:
        print(f"    [WARN] graph_pattern_propagation layer failed, skipping: {e}", flush=True)
        missing_hops = []

    for m in missing_hops:
        from_node = next(
            (n for n in nodes.get(m["from_type"], [])
             if str(n.get(_node_id_field_for(m["from_type"]), "")) == str(m["from_id"])),
            None,
        )
        if from_node is None:
            continue
        for target in m["candidate_targets"]:
            graph_pattern_candidates.append({
                "from": from_node,
                "to": target,
                "layer": "graph_pattern",
                "expected_relation": m.get("expected_relation"),
                "pattern_frequency": m.get("pattern_frequency", 0),
                "from_type": m.get("from_type"),
                "target_type": m.get("target_type"),
            })

    if graph_pattern_mode == "recall":
        raw_candidates.extend(_select_graph_pattern_candidates_recall_first(graph_pattern_candidates))
    else:
        raw_candidates.extend(
            (c["from"], c["to"], "graph_pattern") for c in graph_pattern_candidates
        )

    # 去重：同一对节点（不分先后顺序）只保留一次，优先保留先出现的层标签
    seen = set()
    deduped = []
    for a, b, layer in raw_candidates:
        key = tuple(sorted([id(a), id(b)]))
        if key in seen:
            continue
        seen.add(key)
        deduped.append((a, b, layer))

    # embedding / bridge 候选已经过相似度或共现过滤，直接输出 medium 置信度，
    # 不再送 LLM 验证——这些候选数量大（本次 391 对），全部走 LLM 会累积
    # 20 次连续调用，gateway 偶发延迟即导致无限挂起。
    # 只有 graph_pattern（图模式传播发现的断链）才送 LLM 做开放式验证，
    # 因为断链候选本身不携带语义相似度证据，需要 LLM 判断关系是否真实存在。
    no_verify = []
    need_verify = []
    for a, b, layer in deduped:
        if layer in ("embedding", "bridge"):
            no_verify.append((a, b, layer))
        else:
            need_verify.append((a, b, layer))

    # fast 模式：graph_pattern 候选先用 embedding 相似度排序，取 top N 送 LLM，
    # 保证 LLM 只看最有可能有关系的候选对，避免数千次串行调用导致程序挂起。
    # recall 模式：已在去重前做结构优先选择，embedding 只作为独立的层③候选，
    # 不再作为 graph_pattern 的硬截断条件。
    # full 模式：保留全量候选送 LLM（适合离线批处理，可能耗时数小时）。
    if graph_pattern_mode == "fast" and len(need_verify) > MAX_GRAPH_PATTERN_CANDIDATES:
        print(f"    [fast模式] graph_pattern 候选 {len(need_verify)} 对 → embedding排序取 top {MAX_GRAPH_PATTERN_CANDIDATES}", flush=True)
        need_verify = er.rank_candidate_pairs_by_embedding(need_verify, MAX_GRAPH_PATTERN_CANDIDATES)

    direct_edges = [
        {"from": a, "to": b, "type": "SEMANTICALLY_RELATED", "discovery_layer": layer}
        for a, b, layer in no_verify
    ]

    print(f"    层②③④候选：{len(no_verify)} 对直接输出，{len(need_verify)} 对送 LLM 验证", flush=True)
    verified_edges = verify_candidates_open_llm(need_verify)
    return direct_edges + verified_edges


def run_guide(guide, nodes):
    """Execute one regulatory guide's matching."""
    src_type = guide["source_type"]
    tgt_type = guide["target_type"]
    strategy = guide["match_strategy"]

    src_items = nodes.get(src_type, [])
    tgt_items = nodes.get(tgt_type, [])

    if not src_items or not tgt_items:
        return []

    edges = []

    # Layer 1: Exact rule-based matching (ID, filename, person dedup)
    if strategy == "id_prefix_match":
        src_id = "risk_id" if src_type == "risks" else "control_id"
        tgt_id = "control_id" if tgt_type == "risk_controls" else "risk_id"
        edges = match_id_prefix(src_items, tgt_items, src_id, tgt_id)
    elif strategy == "filename_match":
        edges = match_filename(src_items, tgt_items)
    elif strategy == "person_dedup":
        edges = match_person_dedup(src_items)
        return [(guide, s, t, conf) for s, t, conf in edges]

    # For ID-matched items, mark as high confidence
    id_matched = set()
    for s, t, conf in edges:
        id_matched.add(id(s))

    # Layer 2: LLM batch semantic matching (for items not already matched by ID)
    # Filter out already-matched source items
    unmatched_src = [s for s in src_items if id(s) not in id_matched]
    if unmatched_src and strategy != "filename_match":
        print(f"    LLM matching {len(unmatched_src)} src x {len(tgt_items)} tgt...", end="", flush=True)
        llm_edges = llm_batch_match(unmatched_src, tgt_items, guide, src_type, tgt_type)
        print(f" {len(llm_edges)} found", flush=True)
        edges.extend(llm_edges)

    return [(guide, s, t, conf) for s, t, conf in edges]


def main():
    parser = argparse.ArgumentParser(description="Step4: 跨文档关系发现")
    parser.add_argument(
        "--mode", choices=["fast", "recall", "full"], default="recall",
        help=(
            "fast：graph_pattern候选先用embedding相似度排序，取top200送LLM；"
            "recall（默认）：结构优先保留graph_pattern候选，尽量减少断链漏检；"
            "full：全量候选送LLM，结果最完整但可能耗时数小时"
        ),
    )
    args = parser.parse_args()
    print(f"运行模式：{args.mode}")

    print("=== Step 4: Cross-Document Relationship Discovery ===")
    print(f"Loading {MERGED_PATH.name}...")
    nodes, existing_edges, claims = load_graph()

    all_cross_edges = []
    for i, guide in enumerate(REGULATORY_GUIDES):
        print(f"\n[{i+1}/{len(REGULATORY_GUIDES)}] {guide['name']}")
        print(f"    Standard: {guide['standard']}")
        print(f"    {guide['source_type']} -> {guide['target_type']}")
        t0 = time.time()
        edges = run_guide(guide, nodes)
        elapsed = time.time() - t0

        high = sum(1 for _, _, _, c in edges if c == "high")
        medium = sum(1 for _, _, _, c in edges if c == "medium")
        low = sum(1 for _, _, _, c in edges if c == "low")
        print(f"    Found: {len(edges)} (high={high}, medium={medium}, low={low}) [{elapsed:.1f}s]")
        all_cross_edges.extend(edges)

    # Open-ended candidate discovery (layers ②③④)
    print(f"\n=== Open candidate discovery (graph pattern + embedding + bridge entities) ===")
    id_to_type = _build_id_to_type_index(nodes)
    layer1_edges_for_pattern = [
        {
            "type": guide["edge_type"],
            "from_id": get_node_id(s, guide["source_type"]),
            "from_type": guide["source_type"],
            "to_id": get_node_id(t, guide["target_type"]),
            "to_type": guide["target_type"],
        }
        for guide, s, t, conf in all_cross_edges
    ] + _normalize_step2_edges(existing_edges, id_to_type)
    try:
        open_edges = discover_open_candidates(nodes, layer1_edges_for_pattern,
                                              graph_pattern_mode=args.mode)
        print(f"    Found {len(open_edges)} edges from open candidate discovery")
    except Exception as e:
        print(f"    [WARN] Open candidate discovery failed entirely, skipping: {e}", flush=True)
        open_edges = []

    # Deduplicate
    seen = set()
    unique_edges = []
    for guide, s, t, conf in all_cross_edges:
        key = (get_node_id(s, guide["source_type"]),
               get_node_id(t, guide["target_type"]),
               guide["edge_type"])
        if key not in seen:
            seen.add(key)
            unique_edges.append((guide, s, t, conf))

    print(f"\n=== Total cross-doc edges: {len(unique_edges)} (dedup from {len(all_cross_edges)}) ===")
    high_total = sum(1 for _, _, _, c in unique_edges if c == "high")
    med_total = sum(1 for _, _, _, c in unique_edges if c == "medium")
    low_total = sum(1 for _, _, _, c in unique_edges if c == "low")
    print(f"    High confidence: {high_total}")
    print(f"    Medium confidence: {med_total}")
    print(f"    Low confidence: {low_total}")

    # Save results
    output_edges = []
    for guide, s, t, conf in unique_edges:
        output_edges.append({
            "type": guide["edge_type"],
            "from_type": guide["source_type"],
            "from_id": get_node_id(s, guide["source_type"]),
            "from_source": s.get("_source", ""),
            "to_type": guide["target_type"],
            "to_id": get_node_id(t, guide["target_type"]),
            "to_source": t.get("_source", ""),
            "confidence": conf,
            "cross_doc": True,
            "standard": guide["standard"],
            "guide_name": guide["name"],
            "discovery_layer": "rule",
        })

    for oe in open_edges:
        from_node, to_node = oe["from"], oe["to"]
        output_edges.append({
            "type": oe["type"],
            "from_type": "",
            "from_id": str(from_node.get("description") or from_node.get("measure") or from_node.get("item") or from_node.get("hazard") or from_node.get("name") or "")[:80],
            "from_source": from_node.get("_source", ""),
            "to_type": "",
            "to_id": str(to_node.get("description") or to_node.get("measure") or to_node.get("item") or to_node.get("hazard") or to_node.get("name") or "")[:80],
            "to_source": to_node.get("_source", ""),
            "confidence": "medium",
            "cross_doc": True,
            "standard": "",
            "guide_name": f"开放发现（{oe['discovery_layer']}）",
            "discovery_layer": oe["discovery_layer"],
        })

    output_path = OUTPUT_DIR / "cross_doc_edges.json"
    output_path.write_text(json.dumps(output_edges, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSaved to: {output_path}")

    # Generate report
    generate_report(unique_edges, nodes)

    # Import to Neo4j
    import_to_neo4j(output_edges)

    print("\n=== Step 4 Complete! ===")


GUIDE_NAME_CN = {
    "Requirement -> DesignInput traceability": "需求 → 设计输入 追溯",
    "DesignInput -> Test verification": "设计输入 → 测试 验证",
    "Risk -> RiskControl mitigation": "风险 → 控制措施 缓解",
    "RiskControl -> Test validation": "控制措施 → 测试 验证",
    "Requirement -> Test coverage": "需求 → 测试 覆盖",
    "SoftwareItem -> Test verification": "软件项 → 测试 验证",
    "PlanTask -> Document output": "计划任务 → 文档 产出",
    "DocIndexEntry -> Document existence": "DHF清单条目 → 文档 对应",
    "Regulation -> Requirement implementation": "法规标准 → 需求 实现",
    "Regulation -> DesignInput implementation": "法规标准 → 设计输入 实现",
    "Function -> Test verification": "功能 → 测试 验证",
    "Person identity across documents": "人员跨文档身份识别",
}

RATIONALE_CN = {
    "Requirement -> DesignInput traceability": "每个客户需求应追溯到至少一个设计输入",
    "DesignInput -> Test verification": "每个设计输入应有对应的验证测试证据",
    "Risk -> RiskControl mitigation": "每个已识别的风险应有控制措施",
    "RiskControl -> Test validation": "风险控制措施应有验证证据",
    "Requirement -> Test coverage": "产品需求应通过测试进行验证",
    "SoftwareItem -> Test verification": "软件需求需要验证测试",
    "PlanTask -> Document output": "计划任务应产出对应的文档输出物",
    "DocIndexEntry -> Document existence": "DHF清单中的条目应对应实际存在的文档",
    "Regulation -> Requirement implementation": "适用的法规标准应有对应的需求来实现",
    "Regulation -> DesignInput implementation": "法规要求应体现在设计输入中",
    "Function -> Test verification": "产品功能应通过测试进行验证",
    "Person identity across documents": "识别在不同文档中出现的同一人员",
}


def generate_report(edges, nodes):
    """Generate Chinese markdown analysis report."""
    report_path = OUTPUT_DIR / "cross_doc_report.md"
    lines = ["# 跨文档关系分析报告\n"]
    lines.append(f"> 生成时间：{time.strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"> 发现的跨文档关系总数：{len(edges)}\n\n")

    # Group by guide
    by_guide = {}
    for guide, s, t, conf in edges:
        gname = guide["name"]
        if gname not in by_guide:
            by_guide[gname] = {"guide": guide, "edges": []}
        by_guide[gname]["edges"].append((s, t, conf))

    lines.append("## 总览\n")
    lines.append("| # | 关系类型 | 依据标准 | 发现数 | 高置信 | 中置信 | 低置信 |")
    lines.append("|---|---------|---------|:------:|:------:|:------:|:------:|")
    for i, (gname, info) in enumerate(by_guide.items(), 1):
        g = info["guide"]
        es = info["edges"]
        h = sum(1 for _, _, c in es if c == "high")
        m = sum(1 for _, _, c in es if c == "medium")
        l = sum(1 for _, _, c in es if c == "low")
        cn_name = GUIDE_NAME_CN.get(gname, gname)
        lines.append(f"| {i} | {cn_name} | {g['standard']} | {len(es)} | {h} | {m} | {l} |")
    lines.append("\n")

    # Detail sections
    for gname, info in by_guide.items():
        g = info["guide"]
        es = info["edges"]
        cn_name = GUIDE_NAME_CN.get(gname, gname)
        cn_rationale = RATIONALE_CN.get(gname, g["rationale"])
        lines.append(f"## {cn_name}\n")
        lines.append(f"**依据标准**：{g['standard']}  ")
        lines.append(f"**关系含义**：{cn_rationale}\n")

        if g["source_type"] == "persons" and g["target_type"] == "persons":
            lines.append("| 人员姓名 | 来源文件A | 来源文件B | 置信度 |")
            lines.append("|---------|----------|----------|--------|")
            for s, t, conf in es[:30]:
                conf_cn = "高" if conf == "high" else "中" if conf == "medium" else "低"
                lines.append(f"| {s.get('name','')} | {Path(s.get('_source','')).stem[:25]} | {Path(t.get('_source','')).stem[:25]} | {conf_cn} |")
        else:
            src_cn = {"requirements": "需求", "design_inputs": "设计输入", "tests": "测试",
                      "risks": "风险", "risk_controls": "控制措施", "regulations": "法规标准",
                      "functions": "功能", "software_items": "软件项", "plan_tasks": "计划任务",
                      "documents": "文档", "doc_index_entries": "DHF条目", "persons": "人员"}
            lines.append(f"| 源节点 ({src_cn.get(g['source_type'], g['source_type'])}) | 目标节点 ({src_cn.get(g['target_type'], g['target_type'])}) | 置信度 |")
            lines.append("|" + "-" * 45 + "|" + "-" * 45 + "|--------|")
            for s, t, conf in es[:30]:
                sid = get_node_id(s, g["source_type"])[:43]
                tid = get_node_id(t, g["target_type"])[:43]
                conf_cn = "高" if conf == "high" else "中" if conf == "medium" else "低"
                lines.append(f"| {sid} | {tid} | {conf_cn} |")
            if len(es) > 30:
                lines.append(f"\n*... 还有 {len(es) - 30} 条*\n")
        lines.append("\n")

    # Coverage analysis
    lines.append("## 覆盖率分析\n")

    req_count = len(nodes.get("requirements", []))
    di_count = len(nodes.get("design_inputs", []))
    test_count = len(nodes.get("tests", []))
    risk_count = len(nodes.get("risks", []))
    reg_count = len(nodes.get("regulations", []))
    func_count = len(nodes.get("functions", []))

    req_to_di = sum(1 for g, s, t, c in edges
                    if g["name"] == "Requirement -> DesignInput traceability")
    req_to_test = sum(1 for g, s, t, c in edges
                      if g["name"] == "Requirement -> Test coverage")
    di_to_test = sum(1 for g, s, t, c in edges
                     if g["name"] == "DesignInput -> Test verification")
    reg_to_req = sum(1 for g, s, t, c in edges
                     if g["name"] == "Regulation -> Requirement implementation")
    func_to_test = sum(1 for g, s, t, c in edges
                       if g["name"] == "Function -> Test verification")

    lines.append("| 追溯链 | 已覆盖 | 总数 | 覆盖率 |")
    lines.append("|--------|:------:|:----:|:------:|")
    lines.append(f"| 需求 → 设计输入 | {req_to_di} | {req_count} | {req_to_di*100//max(req_count,1)}% |")
    lines.append(f"| 需求 → 测试 | {req_to_test} | {req_count} | {req_to_test*100//max(req_count,1)}% |")
    lines.append(f"| 设计输入 → 测试 | {di_to_test} | {di_count} | {di_to_test*100//max(di_count,1)}% |")
    lines.append(f"| 法规 → 需求 | {reg_to_req} | {reg_count} | {reg_to_req*100//max(reg_count,1)}% |")
    lines.append(f"| 功能 → 测试 | {func_to_test} | {func_count} | {func_to_test*100//max(func_count,1)}% |")
    lines.append("")

    lines.append("\n## 节点统计\n")
    lines.append(f"- 需求数量：{req_count}")
    lines.append(f"- 设计输入数量：{di_count}")
    lines.append(f"- 测试项数量：{test_count}")
    lines.append(f"- 风险数量：{risk_count}")
    lines.append(f"- 法规标准数量：{reg_count}")
    lines.append(f"- 功能数量：{func_count}")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report saved: {report_path}")


def import_to_neo4j(output_edges):
    """Import cross-doc edges to Neo4j."""
    try:
        from neo4j import GraphDatabase
    except ImportError:
        print("  neo4j driver not installed, skipping import")
        return

    high_med = [e for e in output_edges if e["confidence"] in ("high", "medium")]
    print(f"\nImporting {len(high_med)} high/medium confidence edges to Neo4j...")

    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test1234"))
    created = 0

    # Map source_type to Neo4j label
    TYPE_TO_LABEL = {
        "requirements": "Requirement",
        "design_inputs": "DesignInput",
        "tests": "Test",
        "risks": "Risk",
        "risk_controls": "RiskControl",
        "plan_tasks": "PlanTask",
        "documents": "Document",
        "doc_index_entries": "DocIndexEntry",
        "regulations": "Regulation",
        "persons": "Person",
        "functions": "Function",
        "software_items": "SoftwareItem",
    }

    # Map node type to search property (based on actual Neo4j properties)
    TYPE_TO_PROP = {
        "requirements": "req_id",
        "design_inputs": "di_id",
        "tests": "item",
        "risks": "hazard",
        "risk_controls": "measure",
        "plan_tasks": "name",
        "documents": "title",
        "doc_index_entries": "file_name",
        "regulations": "std_id",
        "persons": "name",
        "functions": "name",
        "software_items": "name",
    }

    with driver.session() as session:
        for e in high_med:
            from_label = TYPE_TO_LABEL.get(e["from_type"], "")
            to_label = TYPE_TO_LABEL.get(e["to_type"], "")
            from_prop = TYPE_TO_PROP.get(e["from_type"], "name")
            to_prop = TYPE_TO_PROP.get(e["to_type"], "name")

            if not from_label or not to_label:
                continue

            from_id = e["from_id"][:80]
            to_id = e["to_id"][:80]

            # For test nodes, from_id is like "TEST-1: xxx", extract the item part
            if e["from_type"] == "tests" and ": " in from_id:
                from_id = from_id.split(": ", 1)[1]
            if e["to_type"] == "tests" and ": " in to_id:
                to_id = to_id.split(": ", 1)[1]
            # For plan_tasks, from_id is like "WBS-1: xxx"
            if e["from_type"] == "plan_tasks" and ": " in from_id:
                from_id = from_id.split(": ", 1)[1]
            if e["to_type"] == "plan_tasks" and ": " in to_id:
                to_id = to_id.split(": ", 1)[1]

            edge_type = e["type"]

            try:
                if len(from_id) <= 10:
                    from_clause = f"a.{from_prop} = $from_id OR a.uid CONTAINS $from_id"
                else:
                    from_clause = f"a.{from_prop} CONTAINS $from_id"

                if len(to_id) <= 10:
                    to_clause = f"b.{to_prop} = $to_id OR b.uid CONTAINS $to_id"
                else:
                    to_clause = f"b.{to_prop} CONTAINS $to_id"

                query = (
                    f"MATCH (a:{from_label}) WHERE {from_clause} "
                    f"MATCH (b:{to_label}) WHERE {to_clause} "
                    f"WITH a, b WHERE a <> b "
                    f"MERGE (a)-[r:{edge_type}]->(b) "
                    f"SET r.confidence = $confidence, r.cross_doc = true, r.standard = $standard "
                    f"RETURN count(r) as cnt"
                )
                result = session.run(query,
                                     from_id=from_id,
                                     to_id=to_id,
                                     confidence=e["confidence"],
                                     standard=e["standard"])
                cnt = result.single()["cnt"]
                if cnt > 0:
                    created += 1
            except Exception as ex:
                pass

    driver.close()
    print(f"  Successfully created {created}/{len(high_med)} cross-doc edges in Neo4j")


if __name__ == "__main__":
    main()
