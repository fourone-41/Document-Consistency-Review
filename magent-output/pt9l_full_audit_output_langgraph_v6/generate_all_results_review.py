import html
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "all-results-review.html"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False)


def evidence_from_row(row: dict) -> list[dict]:
    refs = row.get("evidence_refs")
    if isinstance(refs, list) and refs:
        return refs

    parameter_refs = row.get("parameter_alignment_evidence")
    if isinstance(parameter_refs, list) and parameter_refs:
        return parameter_refs[:12]

    rel_path = row.get("rel_path")
    if rel_path:
        return [
            {
                "doc_id": row.get("doc_id", ""),
                "rel_path": rel_path,
                "line": row.get("line", ""),
                "source_text": row.get("source_text", ""),
                "verified": row.get("evidence_status") == "verified",
            }
        ]
    return []


def normalize_mechanical(row: dict, bucket: str, source: str, index: int) -> dict:
    status = row.get("mechanical_review_status") or {
        "confirmed": "confirm",
        "needs_context": "needs_more_context",
        "dismissed": "dismiss",
    }.get(bucket, "")
    return {
        "id": row.get("finding_id") or row.get("original_candidate_id") or f"MR-{index:04d}",
        "source": source,
        "bucket": bucket,
        "status": status,
        "severity": row.get("severity", ""),
        "agent": row.get("review_agent") or row.get("agent", ""),
        "display_agent": row.get("agent", ""),
        "finding_type": row.get("finding_type", ""),
        "claim": row.get("claim", ""),
        "reason": row.get("context_recovery_reason") or row.get("mechanical_review_reason") or row.get("rationale") or "",
        "challenge_reason": row.get("challenge_reason", ""),
        "context_recovery_status": row.get("context_recovery_status", ""),
        "context_recovery_reason": row.get("context_recovery_reason", ""),
        "doc_id": row.get("doc_id", ""),
        "rel_path": row.get("rel_path", ""),
        "line": row.get("line", ""),
        "term": row.get("term", ""),
        "stage": row.get("stage", ""),
        "doc_type": row.get("doc_type", ""),
        "cluster_key": row.get("mechanical_review_cluster_id") or row.get("cluster_key", ""),
        "primary_scope": row.get("primary_scope"),
        "evidence_status": row.get("evidence_status", ""),
        "challenge_status": row.get("challenge_status", ""),
        "source_text": row.get("source_text", ""),
        "nearby_context": row.get("nearby_context", ""),
        "parameter_values": row.get("parameter_alignment_distinct_values", []),
        "evidence": evidence_from_row(row),
    }


def normalize_semantic(row: dict, index: int) -> dict:
    challenge_status = row.get("challenge_status", "")
    if challenge_status in {"keep", "revise"}:
        bucket = "confirmed"
    elif challenge_status == "drop":
        bucket = "dismissed"
    else:
        bucket = "needs_context"

    return {
        "id": row.get("finding_id") or f"LLM-{index:04d}",
        "source": "语义 Agent Finding",
        "bucket": bucket,
        "status": challenge_status,
        "severity": row.get("severity", ""),
        "agent": row.get("agent", ""),
        "display_agent": row.get("agent", ""),
        "finding_type": row.get("finding_type", ""),
        "claim": row.get("claim", ""),
        "reason": row.get("context_recovery_reason") or row.get("rationale", ""),
        "challenge_reason": row.get("challenge_reason", ""),
        "context_recovery_status": row.get("context_recovery_status", ""),
        "context_recovery_reason": row.get("context_recovery_reason", ""),
        "doc_id": "",
        "rel_path": "",
        "line": "",
        "term": "",
        "stage": "",
        "doc_type": "",
        "cluster_key": "",
        "primary_scope": None,
        "evidence_status": row.get("evidence_status", ""),
        "challenge_status": challenge_status,
        "source_text": "",
        "nearby_context": "",
        "parameter_values": [],
        "evidence": evidence_from_row(row),
    }


def build_records(root: Path = ROOT) -> list[dict]:
    records: list[dict] = []
    confirmed = read_jsonl(root / "13_mechanical_agent_review" / "mechanical_confirmed_findings.jsonl")
    recovered_needs = read_jsonl(root / "14_context_recovery" / "mechanical_after_context_recovery.jsonl")
    needs = recovered_needs or read_jsonl(root / "13_mechanical_agent_review" / "mechanical_needs_context.jsonl")
    dismissed = read_jsonl(root / "13_mechanical_agent_review" / "mechanical_dismissed_candidates.jsonl")
    semantic = read_jsonl(root / "07_findings" / "semantic_findings_llm_challenged.jsonl")

    for i, row in enumerate(confirmed, start=1):
        records.append(normalize_mechanical(row, "confirmed", "机械复审确认", i))
    for i, row in enumerate(needs, start=1):
        source = "机械/数值 Context Recovery 人工复核" if recovered_needs else "机械/数值待补证"
        records.append(normalize_mechanical(row, "needs_context", source, i))
    for i, row in enumerate(dismissed, start=1):
        records.append(normalize_mechanical(row, "dismissed", "机械复审驳回", i))
    for i, row in enumerate(semantic, start=1):
        records.append(normalize_semantic(row, i))

    for idx, row in enumerate(records, start=1):
        row["review_no"] = idx
        row["search_text"] = " ".join(
            as_text(row.get(key))
            for key in [
                "id",
                "source",
                "bucket",
                "status",
                "severity",
                "agent",
                "finding_type",
                "claim",
                "reason",
                "challenge_reason",
                "context_recovery_status",
                "context_recovery_reason",
                "rel_path",
                "term",
                "source_text",
                "nearby_context",
            ]
        ).lower()
    return records


def counter_dict(records: list[dict], key: str) -> dict:
    return dict(Counter(row.get(key, "") or "未标注" for row in records))


def top_counter(records: list[dict], key: str, limit: int = 12) -> list[tuple[str, int]]:
    return Counter(row.get(key, "") or "未标注" for row in records).most_common(limit)


def option_values(records: list[dict], key: str) -> list[str]:
    return sorted({row.get(key, "") for row in records if row.get(key, "")})


def json_script(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False).replace("</", "<\\/")


def esc(value) -> str:
    return html.escape(as_text(value), quote=True)


def render_html(records: list[dict], summary: dict) -> str:
    bucket_counts = counter_dict(records, "bucket")
    severity_counts = counter_dict(records, "severity")
    status_values = option_values(records, "status")
    severity_values = option_values(records, "severity")
    agent_values = option_values(records, "agent")
    type_values = option_values(records, "finding_type")

    total = len(records)
    confirmed = bucket_counts.get("confirmed", 0)
    needs_context = bucket_counts.get("needs_context", 0)
    dismissed = bucket_counts.get("dismissed", 0)

    def options(values: list[str]) -> str:
        return "\n".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in values)

    agent_rows = "\n".join(
        f"<tr><td>{esc(name)}</td><td>{count}</td></tr>" for name, count in top_counter(records, "agent", 16)
    )
    type_rows = "\n".join(
        f"<tr><td>{esc(name)}</td><td>{count}</td></tr>" for name, count in top_counter(records, "finding_type", 16)
    )
    severity_cards = "\n".join(
        f'<div class="mini"><strong>{esc(name)}</strong><span>{count}</span></div>'
        for name, count in sorted(severity_counts.items())
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PT9L 全量审查结果逐条审阅</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #17212b;
      --muted: #5e6c7a;
      --line: #d9e0e8;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --red: #b42318;
      --orange: #b45309;
      --green: #15803d;
      --blue: #1d4ed8;
      --teal: #0f766e;
      --purple: #6d28d9;
      --gray: #64748b;
      --shadow: 0 10px 28px rgba(23, 33, 43, .08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Microsoft YaHei", "PingFang SC", Arial, sans-serif;
      line-height: 1.55;
    }}
    .shell {{ width: min(1480px, calc(100vw - 40px)); margin: 0 auto; }}
    header {{ background: #fff; border-bottom: 1px solid var(--line); }}
    .topbar {{ display: flex; justify-content: space-between; gap: 24px; align-items: flex-end; padding: 28px 0 22px; }}
    h1 {{ margin: 0; font-size: clamp(28px, 4vw, 46px); line-height: 1.12; letter-spacing: 0; }}
    .subtitle {{ margin: 10px 0 0; max-width: 860px; color: var(--muted); font-size: 16px; }}
    .badge {{ display: inline-flex; align-items: center; min-height: 34px; padding: 6px 12px; border: 1px solid var(--line); color: var(--muted); white-space: nowrap; }}
    main {{ padding: 24px 0 48px; }}
    .stats {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; margin-bottom: 18px; }}
    .stat {{ background: var(--panel); border: 1px solid var(--line); box-shadow: var(--shadow); padding: 16px 14px; min-height: 104px; }}
    .stat .num {{ font-size: 32px; line-height: 1; font-weight: 900; margin-bottom: 8px; }}
    .stat .label {{ color: var(--muted); font-size: 13px; }}
    .confirmed {{ color: var(--red); }}
    .needs {{ color: var(--orange); }}
    .dismissed {{ color: var(--gray); }}
    section {{ background: var(--panel); border: 1px solid var(--line); box-shadow: var(--shadow); padding: 20px; margin-top: 18px; }}
    h2 {{ margin: 0 0 16px; font-size: 22px; letter-spacing: 0; }}
    h3 {{ margin: 0 0 8px; font-size: 16px; letter-spacing: 0; }}
    .filters {{ display: grid; grid-template-columns: 1.4fr repeat(4, minmax(140px, 1fr)); gap: 10px; align-items: end; }}
    label {{ display: grid; gap: 6px; color: var(--muted); font-size: 12px; font-weight: 700; }}
    input, select {{
      width: 100%;
      min-height: 40px;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 8px 10px;
      font: inherit;
    }}
    .filter-actions {{ display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }}
    button {{
      min-height: 38px;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 8px 12px;
      font: inherit;
      cursor: pointer;
    }}
    button.active {{ background: var(--ink); color: #fff; border-color: var(--ink); }}
    .layout {{ display: block; }}
    .side {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; position: static; min-width: 0; max-width: 100%; margin-bottom: 18px; }}
    .side > div {{ min-width: 0; }}
    .mini-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }}
    .mini {{ border: 1px solid var(--line); background: #f9fafb; padding: 10px; min-height: 62px; }}
    .mini strong {{ display: block; font-size: 13px; color: var(--muted); margin-bottom: 4px; }}
    .mini span {{ font-size: 22px; font-weight: 850; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; table-layout: fixed; }}
    th, td {{ padding: 8px 10px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; overflow-wrap: anywhere; }}
    th {{ color: var(--muted); font-size: 11px; text-transform: uppercase; }}
    .list-meta {{ display: flex; justify-content: space-between; gap: 14px; align-items: center; margin-bottom: 12px; color: var(--muted); font-size: 14px; }}
    .result-pane {{ min-width: 0; overflow: visible; }}
    .cards {{ display: grid; gap: 12px; min-width: 0; }}
    .card {{ border: 1px solid var(--line); background: #fff; padding: 14px; min-width: 0; overflow-wrap: anywhere; }}
    .card-head {{ display: flex; justify-content: space-between; gap: 12px; align-items: flex-start; margin-bottom: 10px; }}
    .tags {{ display: flex; gap: 6px; flex-wrap: wrap; }}
    .tag {{ display: inline-flex; min-height: 24px; align-items: center; padding: 2px 8px; font-size: 12px; font-weight: 800; border: 1px solid var(--line); background: #f8fafc; color: var(--muted); }}
    .tag.confirmed {{ background: #fee2e2; border-color: #fecaca; color: #991b1b; }}
    .tag.needs_context {{ background: #ffedd5; border-color: #fed7aa; color: #9a3412; }}
    .tag.dismissed {{ background: #f1f5f9; border-color: #cbd5e1; color: #475569; }}
    .tag.P1 {{ background: #fee2e2; border-color: #fecaca; color: #991b1b; }}
    .tag.P2 {{ background: #fff7ed; border-color: #fed7aa; color: #9a3412; }}
    .tag.P3 {{ background: #ecfdf5; border-color: #bbf7d0; color: #166534; }}
    .id {{ font-family: Consolas, "Courier New", monospace; font-weight: 900; }}
    .claim {{ font-size: 16px; font-weight: 800; margin: 8px 0; }}
    .meta {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin: 10px 0; }}
    .meta div {{ background: #f9fafb; border: 1px solid var(--line); padding: 8px 10px; color: var(--muted); font-size: 12px; overflow-wrap: anywhere; }}
    .meta strong {{ display: block; color: var(--ink); font-size: 13px; margin-bottom: 3px; }}
    details {{ border-top: 1px solid var(--line); margin-top: 10px; padding-top: 10px; }}
    summary {{ cursor: pointer; font-weight: 800; color: var(--blue); }}
    .text-block {{ white-space: pre-wrap; overflow-wrap: anywhere; background: #f9fafb; border: 1px solid var(--line); padding: 10px 12px; margin-top: 8px; font-size: 13px; color: #334155; }}
    .evidence {{ display: grid; gap: 8px; margin-top: 8px; }}
    .ev {{ border: 1px solid var(--line); background: #fbfdff; padding: 10px 12px; font-size: 13px; }}
    .ev code {{ overflow-wrap: anywhere; color: #111827; font-family: Consolas, "Courier New", monospace; }}
    .ev p {{ margin: 6px 0 0; color: #334155; white-space: pre-wrap; overflow-wrap: anywhere; }}
    .empty {{ padding: 26px; text-align: center; color: var(--muted); border: 1px dashed var(--line); background: #f9fafb; }}
    footer {{ color: var(--muted); font-size: 13px; padding: 22px 0 36px; }}
    @media (max-width: 1180px) {{
      .stats {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
      .side {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .filters {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 720px) {{
      .shell {{ width: min(100% - 24px, 1480px); }}
      .topbar {{ display: block; }}
      .badge {{ margin-top: 14px; white-space: normal; }}
      .stats, .filters, .meta, .side {{ grid-template-columns: 1fr; }}
      section {{ padding: 14px; }}
      h1 {{ font-size: 30px; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="shell topbar">
      <div>
        <h1>PT9L 全量审查结果逐条审阅</h1>
        <p class="subtitle">包含确认错误、未确认但待补证疑点、已驳回/误报候选。每条结果展开显示 Agent、状态、严重度、裁决理由、证据路径、行号和原文片段。</p>
      </div>
      <div class="badge">数据源：magent-output/pt9l_full_audit_output_langgraph_v6</div>
    </div>
  </header>

  <main class="shell">
    <div class="stats">
      <div class="stat"><div class="num">{total}</div><div class="label">页面收录结果总数</div></div>
      <div class="stat"><div class="num confirmed">{confirmed}</div><div class="label">确认错误/确认候选</div></div>
      <div class="stat"><div class="num needs">{needs_context}</div><div class="label">未确认，待补证/人工复核</div></div>
      <div class="stat"><div class="num dismissed">{dismissed}</div><div class="label">驳回/误报候选</div></div>
      <div class="stat"><div class="num">{summary.get("current_confirmed_error_total", "")}</div><div class="label">汇总口径确认错误</div></div>
      <div class="stat"><div class="num">{summary.get("evidence_verified", "")}</div><div class="label">证据可回溯 finding 行</div></div>
    </div>

    <section>
      <h2>筛选与搜索</h2>
      <div class="filters">
        <label>关键词搜索
          <input id="searchBox" type="search" placeholder="输入型号、文件名、Agent、claim、证据文本...">
        </label>
        <label>状态
          <select id="statusFilter"><option value="">全部状态</option>{options(status_values)}</select>
        </label>
        <label>严重度
          <select id="severityFilter"><option value="">全部严重度</option>{options(severity_values)}</select>
        </label>
        <label>Agent
          <select id="agentFilter"><option value="">全部 Agent</option>{options(agent_values)}</select>
        </label>
        <label>类型
          <select id="typeFilter"><option value="">全部类型</option>{options(type_values)}</select>
        </label>
      </div>
      <div class="filter-actions">
        <button class="active" data-bucket="">全部</button>
        <button data-bucket="confirmed">确认错误/确认候选</button>
        <button data-bucket="needs_context">待补证/人工复核</button>
        <button data-bucket="dismissed">驳回/误报</button>
        <button id="resetBtn">重置筛选</button>
      </div>
    </section>

    <section class="layout">
      <aside class="side">
        <div>
          <h2>严重度</h2>
          <div class="mini-grid">{severity_cards}</div>
        </div>
        <div>
          <h2>Agent Top</h2>
          <table><thead><tr><th>Agent</th><th>数量</th></tr></thead><tbody>{agent_rows}</tbody></table>
        </div>
        <div>
          <h2>类型 Top</h2>
          <table><thead><tr><th>类型</th><th>数量</th></tr></thead><tbody>{type_rows}</tbody></table>
        </div>
      </aside>
      <div class="result-pane">
        <div class="list-meta">
          <div>当前显示 <strong id="visibleCount">0</strong> / {total} 条</div>
          <div>点击“证据与上下文”可展开原文片段。</div>
        </div>
        <div id="cards" class="cards"></div>
      </div>
    </section>
  </main>

  <footer class="shell">
    说明：confirmed 表示系统当前确认或机械复审确认；needs_context 表示尚未确认，需要补证；dismissed 表示当前证据下被驳回或判断为误报。最终 DHF/DMR 整改仍需人工裁决。
  </footer>

  <script>
    const REVIEW_RECORDS = {json_script(records)};

    const state = {{
      q: "",
      bucket: "",
      status: "",
      severity: "",
      agent: "",
      type: ""
    }};

    const els = {{
      cards: document.getElementById("cards"),
      visibleCount: document.getElementById("visibleCount"),
      searchBox: document.getElementById("searchBox"),
      statusFilter: document.getElementById("statusFilter"),
      severityFilter: document.getElementById("severityFilter"),
      agentFilter: document.getElementById("agentFilter"),
      typeFilter: document.getElementById("typeFilter"),
      resetBtn: document.getElementById("resetBtn")
    }};

    function escapeHtml(value) {{
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
    }}

    function bucketLabel(bucket) {{
      return {{
        confirmed: "确认",
        needs_context: "待补证/人工复核",
        dismissed: "驳回"
      }}[bucket] || bucket || "未标注";
    }}

    function evidenceHtml(row) {{
      const evidence = Array.isArray(row.evidence) ? row.evidence : [];
      if (!evidence.length) return '<div class="empty">无结构化证据片段</div>';
      return evidence.map((ev, idx) => `
        <div class="ev">
          <div><strong>证据 ${{idx + 1}}</strong> <code>${{escapeHtml(ev.rel_path || "")}}${{ev.line ? ":" + escapeHtml(ev.line) : ""}}</code></div>
          <div>doc_id：${{escapeHtml(ev.doc_id || "")}} | verified：${{escapeHtml(ev.verified ?? "")}}</div>
          <p>${{escapeHtml(ev.source_text || ev.actual_text || ev.raw_value || "")}}</p>
        </div>
      `).join("");
    }}

    function cardHtml(row) {{
      return `
        <article class="card">
          <div class="card-head">
            <div class="tags">
              <span class="tag ${{escapeHtml(row.bucket)}}">${{bucketLabel(row.bucket)}}</span>
              <span class="tag ${{escapeHtml(row.severity)}}">${{escapeHtml(row.severity || "未标注")}}</span>
              <span class="tag">${{escapeHtml(row.status || "未标注状态")}}</span>
              <span class="tag id">${{escapeHtml(row.id)}}</span>
            </div>
            <div class="id">#${{escapeHtml(row.review_no)}}</div>
          </div>
          <div class="claim">${{escapeHtml(row.claim || "(无 claim)")}}</div>
          <div class="meta">
            <div><strong>Agent</strong>${{escapeHtml(row.agent || row.display_agent || "")}}</div>
            <div><strong>类型</strong>${{escapeHtml(row.finding_type || "")}}</div>
            <div><strong>来源</strong>${{escapeHtml(row.source || "")}}</div>
            <div><strong>文件</strong>${{escapeHtml(row.rel_path || "")}}</div>
            <div><strong>阶段 / 类型</strong>${{escapeHtml(row.stage || "")}} / ${{escapeHtml(row.doc_type || "")}}</div>
            <div><strong>术语 / Cluster</strong>${{escapeHtml(row.term || "")}} ${{row.cluster_key ? " / " + escapeHtml(row.cluster_key) : ""}}</div>
            <div><strong>Context Recovery</strong>${{escapeHtml(row.context_recovery_status || "")}}</div>
          </div>
          <details open>
            <summary>裁决理由 / 审查理由</summary>
            <div class="text-block">${{escapeHtml(row.reason || row.challenge_reason || "(无理由文本)")}}</div>
            ${{row.challenge_reason ? `<div class="text-block"><strong>Challenge：</strong> ${{escapeHtml(row.challenge_reason)}}</div>` : ""}}
          </details>
          <details>
            <summary>证据与上下文</summary>
            <div class="evidence">${{evidenceHtml(row)}}</div>
            ${{row.nearby_context ? `<div class="text-block">${{escapeHtml(row.nearby_context)}}</div>` : ""}}
          </details>
        </article>
      `;
    }}

    function applyFilters() {{
      const q = state.q.trim().toLowerCase();
      const rows = REVIEW_RECORDS.filter(row => {{
        if (state.bucket && row.bucket !== state.bucket) return false;
        if (state.status && row.status !== state.status) return false;
        if (state.severity && row.severity !== state.severity) return false;
        if (state.agent && row.agent !== state.agent) return false;
        if (state.type && row.finding_type !== state.type) return false;
        if (q && !(row.search_text || "").includes(q)) return false;
        return true;
      }});
      els.visibleCount.textContent = rows.length;
      els.cards.innerHTML = rows.length ? rows.map(cardHtml).join("") : '<div class="empty">没有符合当前筛选条件的结果</div>';
    }}

    els.searchBox.addEventListener("input", event => {{ state.q = event.target.value; applyFilters(); }});
    els.statusFilter.addEventListener("change", event => {{ state.status = event.target.value; applyFilters(); }});
    els.severityFilter.addEventListener("change", event => {{ state.severity = event.target.value; applyFilters(); }});
    els.agentFilter.addEventListener("change", event => {{ state.agent = event.target.value; applyFilters(); }});
    els.typeFilter.addEventListener("change", event => {{ state.type = event.target.value; applyFilters(); }});

    document.querySelectorAll("[data-bucket]").forEach(button => {{
      button.addEventListener("click", () => {{
        document.querySelectorAll("[data-bucket]").forEach(btn => btn.classList.remove("active"));
        button.classList.add("active");
        state.bucket = button.dataset.bucket || "";
        applyFilters();
      }});
    }});

    els.resetBtn.addEventListener("click", () => {{
      state.q = "";
      state.bucket = "";
      state.status = "";
      state.severity = "";
      state.agent = "";
      state.type = "";
      els.searchBox.value = "";
      els.statusFilter.value = "";
      els.severityFilter.value = "";
      els.agentFilter.value = "";
      els.typeFilter.value = "";
      document.querySelectorAll("[data-bucket]").forEach(btn => btn.classList.toggle("active", btn.dataset.bucket === ""));
      applyFilters();
    }});

    applyFilters();
  </script>
</body>
</html>
"""


def main() -> None:
    summary = read_json(ROOT / "08_reports" / "run_summary_full_langgraph.json")
    records = build_records(ROOT)
    OUT.write_text(render_html(records, summary), encoding="utf-8")
    print(json.dumps({"output": str(OUT), "records": len(records)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
