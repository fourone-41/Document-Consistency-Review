from __future__ import annotations

from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os
import sys
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
PORT = int(os.getenv("LANGSMITH_FLOW_PORT", "8792"))

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

try:
    from langsmith import Client
except ImportError as exc:
    raise SystemExit("Install langsmith first: python -m pip install langsmith") from exc


def main() -> None:
    if load_dotenv:
        load_dotenv(REPO_ROOT / ".env")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), LangSmithFlowHandler)
    print(f"LangSmith trace flow dashboard: http://127.0.0.1:{PORT}/")
    print("Requires LANGSMITH_API_KEY and LANGSMITH_PROJECT in this shell.")
    server.serve_forever()


class LangSmithFlowHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.send_html()
            return
        if parsed.path == "/api/trace":
            self.send_json(self.get_trace_payload(parse_qs(parsed.query)))
            return
        self.send_error(404)

    def log_message(self, format: str, *args) -> None:
        return

    def send_html(self) -> None:
        body = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def get_trace_payload(self, query: dict[str, list[str]]) -> dict:
        project = first(query.get("project")) or os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT")
        if not project:
            return {"ok": False, "error": "Missing LANGSMITH_PROJECT"}
        if not os.getenv("LANGSMITH_API_KEY"):
            return {"ok": False, "error": "Missing LANGSMITH_API_KEY"}

        client = Client()
        root_run_id = first(query.get("run_id"))
        try:
            if root_run_id:
                root = client.read_run(root_run_id)
            else:
                roots = list(
                    client.list_runs(
                        project_name=project,
                        is_root=True,
                        limit=10,
                        select=["id", "name", "run_type", "trace_id", "start_time", "end_time", "error", "inputs", "outputs"],
                    )
                )
                if not roots:
                    return {"ok": True, "project": project, "runs": [], "nodes": [], "edges": []}
                roots.sort(key=lambda run: getattr(run, "start_time", datetime.min.replace(tzinfo=timezone.utc)), reverse=True)
                root = roots[0]

            trace_id = getattr(root, "trace_id", None) or getattr(root, "id")
            runs = list(
                client.list_runs(
                    project_name=project,
                    trace_id=trace_id,
                    limit=100,
                    select=[
                        "id",
                        "name",
                        "run_type",
                        "trace_id",
                        "parent_run_id",
                        "dotted_order",
                        "start_time",
                        "end_time",
                        "error",
                        "inputs",
                        "outputs",
                        "tags",
                        "extra",
                    ],
                )
            )
            runs.sort(key=sort_key)
            nodes = [run_to_node(run) for run in runs]
            known = {node["id"] for node in nodes}
            edges = [
                {"source": node["parent_run_id"], "target": node["id"]}
                for node in nodes
                if node.get("parent_run_id") in known
            ]
            return {
                "ok": True,
                "project": project,
                "root_run_id": str(getattr(root, "id")),
                "trace_id": str(trace_id),
                "run_url": client.get_run_url(run=root, project_name=project),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "nodes": nodes,
                "edges": edges,
            }
        except Exception as exc:
            return {"ok": False, "project": project, "error": str(exc), "type": exc.__class__.__name__}


def first(values: list[str] | None) -> str | None:
    return values[0] if values else None


def sort_key(run) -> tuple[str, str]:
    dotted = getattr(run, "dotted_order", "") or ""
    start = getattr(run, "start_time", None)
    return (dotted, start.isoformat() if start else "")


def run_to_node(run) -> dict:
    start = getattr(run, "start_time", None)
    end = getattr(run, "end_time", None)
    latency_ms = None
    if start and end:
        latency_ms = round((end - start).total_seconds() * 1000, 1)
    inputs = safe_json(getattr(run, "inputs", None))
    outputs = safe_json(getattr(run, "outputs", None))
    return {
        "id": str(getattr(run, "id")),
        "name": getattr(run, "name", ""),
        "run_type": getattr(run, "run_type", ""),
        "trace_id": str(getattr(run, "trace_id", "")),
        "parent_run_id": str(getattr(run, "parent_run_id", "") or ""),
        "dotted_order": getattr(run, "dotted_order", "") or "",
        "start_time": start.isoformat() if start else None,
        "end_time": end.isoformat() if end else None,
        "latency_ms": latency_ms,
        "error": getattr(run, "error", None),
        "tags": list(getattr(run, "tags", []) or []),
        "extra": safe_json(getattr(run, "extra", None)),
        "inputs": trim(inputs),
        "outputs": trim(outputs),
        "input_keys": sorted(inputs.keys()) if isinstance(inputs, dict) else [],
        "output_keys": sorted(outputs.keys()) if isinstance(outputs, dict) else [],
    }


def safe_json(value):
    if value is None:
        return {}
    try:
        json.dumps(value, ensure_ascii=False)
        return value
    except TypeError:
        return json.loads(json.dumps(value, default=str, ensure_ascii=False))


def trim(value):
    if isinstance(value, dict):
        return {key: trim(item) for key, item in list(value.items())[:30]}
    if isinstance(value, list):
        return [trim(item) for item in value[:20]]
    if isinstance(value, str) and len(value) > 1200:
        return value[:1200] + "...[trimmed]"
    return value


HTML = r"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>LangSmith Trace Flow Dashboard</title>
  <style>
    :root { --ink:#172033; --muted:#667085; --line:#d8e0ea; --page:#eef3f8; --blue:#2563eb; --green:#15803d; --red:#b91c1c; --panel:#fff; }
    * { box-sizing:border-box; }
    body { margin:0; background:var(--page); color:var(--ink); font-family:"Microsoft YaHei",Arial,sans-serif; }
    header { height:68px; background:#111827; color:#fff; display:flex; align-items:center; justify-content:space-between; padding:0 22px; }
    h1 { margin:0; font-size:20px; }
    .sub { color:#cbd5e1; font-size:13px; margin-top:4px; }
    button, input { font:inherit; }
    button { height:36px; border:0; border-radius:8px; background:var(--blue); color:#fff; padding:0 12px; cursor:pointer; font-weight:700; }
    input { height:36px; border:1px solid var(--line); border-radius:8px; padding:0 10px; min-width:230px; }
    main { display:grid; grid-template-columns:minmax(760px,1.2fr) minmax(390px,.8fr); gap:16px; padding:16px; }
    .panel { background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; box-shadow:0 12px 28px rgba(15,23,42,.09); }
    .head { padding:12px 14px; border-bottom:1px solid var(--line); display:flex; align-items:center; justify-content:space-between; gap:10px; background:#fbfdff; }
    .head h2 { margin:0; font-size:15px; }
    .body { padding:14px; }
    .graph { position:relative; height:660px; overflow:auto; background:linear-gradient(#edf2f7 1px,transparent 1px),linear-gradient(90deg,#edf2f7 1px,transparent 1px),#fff; background-size:28px 28px; }
    .canvas { position:relative; width:1280px; min-height:640px; margin:12px; }
    svg { position:absolute; inset:0; width:1280px; height:640px; pointer-events:none; }
    path { stroke:#94a3b8; stroke-width:2; fill:none; marker-end:url(#arrow); }
    .node { position:absolute; width:210px; min-height:86px; border:2px solid var(--line); border-radius:8px; background:#fff; padding:10px; cursor:pointer; transition:.15s ease; }
    .node:hover, .node.active { border-color:var(--blue); box-shadow:0 14px 24px rgba(37,99,235,.15); transform:translateY(-2px); }
    .node.error { border-color:var(--red); }
    .kind { color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:.04em; }
    .name { font-weight:800; margin-top:5px; font-size:13px; overflow-wrap:anywhere; }
    .meta { color:var(--muted); font-size:12px; margin-top:6px; }
    .list { display:grid; gap:8px; max-height:230px; overflow:auto; }
    .item { border:1px solid var(--line); border-radius:8px; background:#fff; padding:9px; cursor:pointer; }
    .item.active { border-color:var(--blue); background:#eff6ff; }
    .item-title { font-weight:800; font-size:13px; }
    .item-meta { color:var(--muted); font-size:12px; margin-top:4px; overflow-wrap:anywhere; }
    pre { margin:0; background:#0b1220; color:#e5e7eb; border-radius:8px; padding:12px; max-height:540px; overflow:auto; white-space:pre-wrap; overflow-wrap:anywhere; font-size:12px; }
    .status { color:var(--muted); font-size:13px; }
    @media(max-width:1180px){ main{grid-template-columns:1fr} }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>LangSmith Trace Flow Dashboard</h1>
      <div class="sub" id="sub">从 LangSmith API 轮询最新 trace，回放 Agent 数据流</div>
    </div>
    <div>
      <input id="project" placeholder="project name" />
      <input id="runId" placeholder="root run id 可选" />
      <button id="refresh">Refresh</button>
      <button id="auto">Auto: off</button>
    </div>
  </header>
  <main>
    <section class="panel">
      <div class="head"><h2>Trace 数据流</h2><div class="status" id="status">idle</div></div>
      <div class="graph"><div class="canvas" id="canvas"></div></div>
    </section>
    <aside>
      <div class="panel" style="margin-bottom:16px">
        <div class="head"><h2>Runs</h2><span class="status" id="count">0</span></div>
        <div class="body"><div class="list" id="runs"></div></div>
      </div>
      <div class="panel">
        <div class="head"><h2 id="detailTitle">Run Detail</h2><span class="status" id="latency"></span></div>
        <div class="body"><pre id="detail">{}</pre></div>
      </div>
    </aside>
  </main>
  <script>
    const $ = s => document.querySelector(s);
    const esc = v => String(v ?? "").replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#039;"}[ch]));
    let payload = null, active = null, timer = null;

    $("#refresh").onclick = fetchTrace;
    $("#auto").onclick = () => {
      if (timer) { clearInterval(timer); timer = null; $("#auto").textContent = "Auto: off"; return; }
      fetchTrace(); timer = setInterval(fetchTrace, 2000); $("#auto").textContent = "Auto: on";
    };

    async function fetchTrace(){
      const qs = new URLSearchParams();
      if($("#project").value.trim()) qs.set("project", $("#project").value.trim());
      if($("#runId").value.trim()) qs.set("run_id", $("#runId").value.trim());
      $("#status").textContent = "fetching...";
      const res = await fetch("/api/trace?" + qs.toString());
      payload = await res.json();
      if(!payload.ok){
        $("#status").textContent = payload.error || "error";
        $("#detail").textContent = JSON.stringify(payload,null,2);
        document.querySelector(".graph").innerHTML = `<div style="padding:28px;color:#667085;line-height:1.6">${esc(payload.error || "Failed to load LangSmith trace")}</div>`;
        return;
      }
      $("#status").textContent = `${payload.project} · ${payload.nodes.length} runs · ${payload.fetched_at}`;
      $("#sub").textContent = payload.run_url || "LangSmith trace";
      render();
    }

    function render(){
      const nodes = payload.nodes || [];
      $("#count").textContent = nodes.length;
      const levels = layout(nodes);
      const width = 1280;
      const height = Math.max(640, Math.max(...nodes.map(n => levels[n.id].y + 120), [640]));
      const paths = (payload.edges || []).map(e => {
        const a = levels[e.source], b = levels[e.target];
        if(!a || !b) return "";
        return `<path d="M${a.x+210} ${a.y+43} C${a.x+260} ${a.y+43}, ${b.x-50} ${b.y+43}, ${b.x} ${b.y+43}"></path>`;
      }).join("");
      $("#canvas").style.height = height + "px";
      $("#canvas").innerHTML = `<svg viewBox="0 0 ${width} ${height}">
        <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#94a3b8"/></marker></defs>
        ${paths}
      </svg>${nodes.map(n => nodeHtml(n, levels[n.id])).join("")}`;
      $("#runs").innerHTML = nodes.map(n => `<div class="item" data-id="${n.id}" onclick="selectRun('${n.id}')">
        <div class="item-title">${esc(n.name)}</div>
        <div class="item-meta">${esc(n.run_type)} · ${esc(n.latency_ms ?? "")}ms</div>
      </div>`).join("");
      if(!active && nodes[0]) selectRun(nodes[0].id);
    }

    function layout(nodes){
      const children = {};
      nodes.forEach(n => { (children[n.parent_run_id || "root"] ||= []).push(n); });
      const pos = {};
      let row = 0;
      function walk(node, depth){
        pos[node.id] = {x: 30 + depth * 250, y: 30 + row * 115};
        row += 1;
        (children[node.id] || []).forEach(child => walk(child, depth + 1));
      }
      (children["root"] || nodes.filter(n => !n.parent_run_id)).forEach(root => walk(root, 0));
      return pos;
    }

    function nodeHtml(n, p){
      return `<div class="node ${n.error ? "error" : ""} ${active===n.id ? "active" : ""}" style="left:${p.x}px;top:${p.y}px" onclick="selectRun('${n.id}')">
        <div class="kind">${esc(n.run_type)} · ${esc(n.latency_ms ?? "")}ms</div>
        <div class="name">${esc(n.name)}</div>
        <div class="meta">in: ${esc(n.input_keys.join(", ")) || "-"}<br>out: ${esc(n.output_keys.join(", ")) || "-"}</div>
      </div>`;
    }

    window.selectRun = function(id){
      active = id;
      const n = (payload.nodes || []).find(item => item.id === id);
      if(!n) return;
      $("#detailTitle").textContent = n.name;
      $("#latency").textContent = n.latency_ms ? `${n.latency_ms}ms` : "";
      $("#detail").textContent = JSON.stringify(n, null, 2);
      document.querySelectorAll(".node").forEach(el => el.classList.toggle("active", el.getAttribute("onclick")?.includes(id)));
      document.querySelectorAll(".item").forEach(el => el.classList.toggle("active", el.dataset.id === id));
    }

    fetchTrace();
  </script>
</body>
</html>"""


if __name__ == "__main__":
    main()
