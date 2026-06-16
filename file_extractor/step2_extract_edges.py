"""Step 2: Extract edges (relationships) from already-extracted nodes.
Enhanced version: covers all extraction_edges types + rule-based implicit edges."""
import json
import re
import time
from pathlib import Path
from openai import OpenAI

from config import API_KEY, LLM_BASE_URL, LLM_MODEL, PER_FILE_DIR, LLM_MAX_TOKENS

client = OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL)

EDGE_PROMPT = """你是医疗器械DHF文档一致性审查的关系抽取专家。

以下是从一份文档中抽取的节点信息（JSON）。请尽可能多地识别节点之间的语义关系。

===== 可用关系类型（尽量多找，只要有依据就输出）=====

1. DERIVES_FROM: DesignInput → Requirement（设计输入来源于需求）
2. CONSTRAINED_BY: Requirement → Regulation（需求受法规约束）
3. MITIGATED_BY: Risk → RiskControl（风险被措施控制）
4. VERIFIED_BY: RiskControl/DesignInput → Test（被测试验证）
5. REPORTED_IN: Test → TestReport（测试结果记录在报告中）
6. COVERS: DesignInput/Requirement/Function → IntendedUseItem（覆盖预期用途）
7. HAS_MEASUREMENT: Test → TestMeasurement（测试包含实测数据）
8. DEPENDS_ON: PlanTask → PlanTask（任务前置依赖）
9. SCHEDULES: Document → PlanTask（计划文件包含任务）
10. HAS_REVISION: Document → RevisionRecord（文件的版本历史）
11. HAS_REVIEW_ITEM: Document/ReviewRecord → ReviewItem（评审包含检查项）
12. REVIEWS: ReviewItem → Requirement/DesignInput/Document（检查项评审对象）
13. LISTS_FILE: Document → DocIndexEntry（清单包含文件条目）
14. DESCRIBES_SOFTWARE: Document → SoftwareItem/SoftwareConfigItem
15. SIGNED: Person → Document/ReviewRecord（人员签署文件，role=编写人/审批人/评审员）
16. IMPLEMENTED_IN: Function → Document（功能在文件中实现）
17. HAS_DETAIL: 任意节点 → SemanticFragment（结构化节点的补充文本）
18. RESPONSIBLE_FOR: Person → PlanTask（人员负责该任务）
19. PRODUCES: PlanTask → Document/Identifier（任务产出文件）

===== 输出格式 =====
JSON数组：
[{"type": "关系类型", "from": "起点标识", "to": "终点标识", "properties": {}}]

===== 规则 =====
1. from/to 用节点的 id、name、seq、test_id、req_id 等唯一标识
2. 尽量多找关系！不确定的也可以输出，我们宁可多找一些
3. 同一对节点可以有多条不同类型的边
4. 没有关系则输出 []
5. 严格输出 JSON，不要加 markdown 标记
"""


def try_parse_json(text: str) -> list | dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r'^```\w*\n?', '', text)
        text = re.sub(r'\n?```$', '', text)
        text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        for suffix in [']', '"}]', '"}]}', '}]']:
            try:
                return json.loads(text + suffix)
            except json.JSONDecodeError:
                continue
    return []


def derive_rule_based_edges(data: dict) -> list[dict]:
    """Generate edges from rules without LLM (structural/obvious relationships)."""
    edges = []
    source = data.get("_meta", {}).get("source_file", "")
    doc_title = ""
    if isinstance(data.get("document"), dict):
        doc_title = data["document"].get("title", "")

    # SCHEDULES: Document → PlanTask
    for task in data.get("plan_tasks", []):
        task_name = task.get("name") or task.get("wbs", "")
        if task_name and doc_title:
            edges.append({"type": "SCHEDULES", "from": doc_title, "to": task_name, "properties": {}})

    # HAS_REVISION: Document → RevisionRecord
    for rev in data.get("revision_records", []):
        rev_id = rev.get("seq") or rev.get("version", "")
        if rev_id and doc_title:
            edges.append({"type": "HAS_REVISION", "from": doc_title, "to": str(rev_id), "properties": {}})

    # LISTS_FILE: Document → DocIndexEntry
    for entry in data.get("doc_index_entries", []):
        entry_name = entry.get("file_name", "")
        if entry_name and doc_title:
            edges.append({"type": "LISTS_FILE", "from": doc_title, "to": entry_name, "properties": {}})

    # HAS_REVIEW_ITEM: Document → ReviewItem
    for item in data.get("review_items", []):
        item_id = item.get("seq") or item.get("content", "")[:20]
        if item_id and doc_title:
            edges.append({"type": "HAS_REVIEW_ITEM", "from": doc_title, "to": str(item_id), "properties": {}})

    # DESCRIBES_SOFTWARE: Document → SoftwareItem
    for sw in data.get("software_items", []):
        sw_name = sw.get("name", "")
        if sw_name and doc_title:
            edges.append({"type": "DESCRIBES_SOFTWARE", "from": doc_title, "to": sw_name, "properties": {}})

    # HAS_DETAIL: parent nodes → SemanticFragment
    for frag in data.get("semantic_fragments", []):
        related = frag.get("related_subjects", [])
        frag_id = (frag.get("topic_tags") or [""])[0] or frag.get("content", "")[:20]
        for subj in related:
            if subj:
                edges.append({"type": "HAS_DETAIL", "from": subj, "to": frag_id, "properties": {}})
        if not related and doc_title:
            edges.append({"type": "HAS_DETAIL", "from": doc_title, "to": frag_id, "properties": {}})

    # RESPONSIBLE_FOR: Person → PlanTask (from owner field)
    for task in data.get("plan_tasks", []):
        owner = task.get("owner", "")
        task_name = task.get("name", "")
        if owner and task_name:
            persons = [p.strip() for p in re.split(r'[;；、,，]', owner) if p.strip()]
            for p in persons[:3]:
                edges.append({"type": "RESPONSIBLE_FOR", "from": p, "to": task_name, "properties": {}})

    # SIGNED: Person → Document
    for person in data.get("persons", []):
        if person.get("signed") and doc_title:
            edges.append({"type": "SIGNED", "from": person["name"], "to": doc_title,
                         "properties": {"role": person.get("title", "")}})

    # REPORTED_IN: Test → TestReport (if both exist in same file)
    test_reports = data.get("test_reports", [])
    if test_reports:
        report_id = test_reports[0].get("report_id") or doc_title
        for t in data.get("tests", []):
            t_id = t.get("test_id", "")
            if t_id:
                edges.append({"type": "REPORTED_IN", "from": str(t_id), "to": report_id, "properties": {}})

    # HAS_MEASUREMENT: Test → TestMeasurement
    for m in data.get("test_measurements", []):
        t_id = m.get("test_id", "")
        m_id = m.get("test_point") or m.get("meas_id", "")
        if t_id and m_id:
            edges.append({"type": "HAS_MEASUREMENT", "from": str(t_id), "to": m_id, "properties": {}})

    return edges


def extract_edges_llm(data: dict) -> list[dict]:
    """Use LLM to find semantic edges that rules can't catch."""
    node_summary = {}
    for key, val in data.items():
        if key.startswith("_"):
            continue
        if isinstance(val, list) and val:
            node_summary[key] = val[:25]
        elif isinstance(val, dict):
            node_summary[key] = val

    if not node_summary:
        return []

    user_msg = json.dumps(node_summary, ensure_ascii=False, indent=1)
    if len(user_msg) > 14000:
        user_msg = user_msg[:14000] + "\n...(truncated)"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=LLM_MAX_TOKENS,
            messages=[
                {"role": "system", "content": EDGE_PROMPT},
                {"role": "user", "content": user_msg},
            ],
        )
        content = response.choices[0].message.content or "[]"
        edges = try_parse_json(content)
        if isinstance(edges, list):
            return edges
        return []
    except Exception as e:
        print(f"    LLM ERROR: {e}", flush=True)
        return []


def deduplicate_edges(edges: list[dict]) -> list[dict]:
    """Remove duplicate edges."""
    seen = set()
    result = []
    for e in edges:
        key = (e.get("type", ""), str(e.get("from", "")), str(e.get("to", "")))
        if key not in seen:
            seen.add(key)
            result.append(e)
    return result


def main():
    json_files = sorted(PER_FILE_DIR.glob("*.json"))
    print(f"=== Step 2: Extract Edges (Enhanced) ===", flush=True)
    print(f"Processing {len(json_files)} files\n", flush=True)

    total_start = time.time()

    for i, fp in enumerate(json_files, 1):
        print(f"[{i}/{len(json_files)}] {fp.stem[:50]}...", flush=True)
        t0 = time.time()

        data = json.loads(fp.read_text(encoding="utf-8"))

        # Rule-based edges
        rule_edges = derive_rule_based_edges(data)
        print(f"    rule-based: {len(rule_edges)} edges", flush=True)

        # LLM-based edges
        print(f"    LLM extraction...", end="", flush=True)
        llm_edges = extract_edges_llm(data)
        elapsed = time.time() - t0
        print(f" {len(llm_edges)} edges ({elapsed:.1f}s)", flush=True)

        # Merge and deduplicate
        all_edges = deduplicate_edges(rule_edges + llm_edges)
        print(f"    total (dedup): {len(all_edges)} edges", flush=True)

        # Save back
        data["_edges"] = all_edges
        fp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    total_elapsed = time.time() - total_start
    total_edges = sum(
        len(json.loads(fp.read_text(encoding="utf-8")).get("_edges", []))
        for fp in json_files
    )
    print(f"\n=== Step 2 Complete === ({total_elapsed:.0f}s, {total_edges} total edges)", flush=True)


if __name__ == "__main__":
    main()
