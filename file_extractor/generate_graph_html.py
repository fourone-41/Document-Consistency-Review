"""Generate interactive HTML graph visualization mimicking Neo4j Browser UI."""
import json
from pathlib import Path

MERGED_PATH = Path(__file__).parent / "output" / "merged_graph.json"
CROSS_DOC_PATH = Path(__file__).parent / "output" / "cross_doc_edges.json"
OUTPUT_HTML = Path(__file__).parent / "output" / "graph_visualization.html"

# Neo4j-style color palette for node types
COLORS = {
    "documents": "#4C8EDA",
    "requirements": "#57C7E3",
    "design_inputs": "#F79767",
    "tests": "#FB95AF",
    "risks": "#D9C8AE",
    "risk_controls": "#8DCC93",
    "regulations": "#ECB5C9",
    "functions": "#4C8EDA",
    "plan_tasks": "#C990C0",
    "persons": "#F16667",
    "software_items": "#57C7E3",
    "doc_index_entries": "#FFC454",
    "products": "#8DCC93",
    "review_items": "#DA7194",
    "semantic_fragments": "#569480",
    "components": "#D9C8AE",
    "test_measurements": "#FB95AF",
    "markets": "#C990C0",
    "identifiers": "#4C8EDA",
    "intended_use_items": "#F79767",
    "revision_records": "#ECB5C9",
}

LABELS_CN = {
    "documents": "Document",
    "requirements": "Requirement",
    "design_inputs": "DesignInput",
    "tests": "Test",
    "risks": "Risk",
    "risk_controls": "RiskControl",
    "regulations": "Regulation",
    "functions": "Function",
    "plan_tasks": "PlanTask",
    "persons": "Person",
    "software_items": "SoftwareItem",
    "doc_index_entries": "DocIndexEntry",
    "products": "Product",
    "review_items": "ReviewItem",
    "semantic_fragments": "SemanticFragment",
    "components": "Component",
    "test_measurements": "TestMeasurement",
    "markets": "Market",
    "identifiers": "Identifier",
    "intended_use_items": "IntendedUseItem",
    "revision_records": "RevisionRecord",
}


def get_node_label(node, node_type):
    if node_type == "requirements":
        return node.get("req_id") or (node.get("description") or "")[:20]
    if node_type == "design_inputs":
        return node.get("di_id") or (node.get("description") or "")[:20]
    if node_type == "tests":
        return f"T{node.get('test_id', '')}"
    if node_type == "risks":
        return (node.get("hazard") or "")[:18]
    if node_type == "risk_controls":
        return (node.get("measure") or "")[:18]
    if node_type == "documents":
        return (node.get("title") or "")[:18]
    if node_type == "regulations":
        return f"{node.get('std_id', '')} {node.get('clause', '') or ''}"[:18]
    if node_type == "functions":
        return (node.get("name") or "")[:15]
    if node_type == "persons":
        return node.get("name") or ""
    if node_type == "plan_tasks":
        return (node.get("name") or "")[:15]
    if node_type == "software_items":
        return (node.get("name") or "")[:15]
    if node_type == "doc_index_entries":
        return (node.get("file_name") or "")[:15]
    if node_type == "products":
        return node.get("name") or node.get("model") or ""
    if node_type == "review_items":
        return (node.get("content") or "")[:15]
    return str(node)[:12]


def build_properties(node, node_type):
    """Build property dict for detail panel."""
    props = {}
    for k, v in node.items():
        if k.startswith("_") or v is None or v == "":
            continue
        props[k] = str(v)[:200]
    return props


def main():
    data = json.loads(MERGED_PATH.read_text(encoding="utf-8"))
    nodes_data = data["nodes"]
    cross_edges = json.loads(CROSS_DOC_PATH.read_text(encoding="utf-8"))

    vis_nodes = []
    node_id_map = {}
    vis_id = 0

    all_types = [t for t in nodes_data.keys() if isinstance(nodes_data[t], list)]

    # Filter out 设计开发计划表 source
    EXCLUDED_SOURCES = ["02 开发计划E0 23.11/设计开发计划表E0  23.11.via_xlsx.clean.md"]

    for ntype in all_types:
        items = nodes_data[ntype]
        for i, node in enumerate(items):
            if node.get("_source", "") in EXCLUDED_SOURCES:
                continue
            vis_id += 1
            node_id_map[(ntype, i)] = vis_id
            label = get_node_label(node, ntype)
            color = COLORS.get(ntype, "#cbd5e0")
            props = build_properties(node, ntype)
            vis_nodes.append({
                "id": vis_id,
                "label": label,
                "group": ntype,
                "color": color,
                "properties": props,
            })

    # Node lookup for edge matching - build comprehensive index
    node_lookup = {}
    for ntype, items in nodes_data.items():
        if not isinstance(items, list):
            continue
        for i, node in enumerate(items):
            vid = node_id_map.get((ntype, i))
            if not vid:
                continue
            for field in ["req_id", "di_id", "risk_id", "control_id", "test_id",
                          "name", "title", "hazard", "measure", "item", "file_name",
                          "description", "content", "std_id", "topic", "model",
                          "clause", "role"]:
                val = node.get(field)
                if val and isinstance(val, str) and len(val) > 1:
                    if val not in node_lookup:
                        node_lookup[val] = vid
                    node_lookup[(ntype, val)] = vid
            # Also index by uid if present
            uid = node.get("uid")
            if uid and isinstance(uid, str):
                node_lookup[uid] = vid
            # For revision_records, index by version number
            if ntype == "revision_records":
                ver = node.get("version")
                if ver:
                    node_lookup[str(ver)] = vid

    # Build edges from BOTH intra-doc and cross-doc
    vis_edges = []
    edge_id = 0

    # 1) Intra-document edges (from merged_graph.json)
    intra_edges = data.get("edges", [])
    intra_matched = 0
    for ie in intra_edges:
        if ie.get("_source", "") in EXCLUDED_SOURCES:
            continue
        fr = ie.get("from")
        to = ie.get("to")
        if not isinstance(fr, str) or not isinstance(to, str):
            continue
        from_id = node_lookup.get(fr)
        to_id = node_lookup.get(to)
        if from_id and to_id and from_id != to_id:
            edge_id += 1
            intra_matched += 1
            vis_edges.append({
                "id": edge_id,
                "from": from_id,
                "to": to_id,
                "type": ie["type"],
                "cross_doc": False,
                "properties": {
                    "type": ie["type"],
                    "source": ie.get("_source", ""),
                },
            })

    # 2) Cross-document edges
    cross_matched = 0
    for ce in cross_edges:
        from_key = (ce["from_type"], ce["from_id"])
        from_id = node_lookup.get(from_key) or node_lookup.get(ce["from_id"])
        to_key = (ce["to_type"], ce["to_id"])
        to_id = node_lookup.get(to_key) or node_lookup.get(ce["to_id"])
        if from_id and to_id and from_id != to_id:
            edge_id += 1
            cross_matched += 1
            vis_edges.append({
                "id": edge_id,
                "from": from_id,
                "to": to_id,
                "type": ce["type"],
                "cross_doc": True,
                "properties": {
                    "type": ce["type"],
                    "confidence": ce.get("confidence", ""),
                    "standard": ce.get("standard", ""),
                    "rationale": ce.get("rationale", ""),
                },
            })

    print(f"  Intra-doc edges matched: {intra_matched}/{len(intra_edges)}")
    print(f"  Cross-doc edges matched: {cross_matched}/{len(cross_edges)}")

    # Count by type for sidebar
    type_counts = {}
    for ntype in all_types:
        type_counts[ntype] = len(nodes_data[ntype])

    # Relationship type counts
    rel_type_counts = {}
    for e in vis_edges:
        t = e["type"]
        rel_type_counts[t] = rel_type_counts.get(t, 0) + 1

    html = generate_html(vis_nodes, vis_edges, type_counts, rel_type_counts, all_types)
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"Generated: {OUTPUT_HTML}")
    print(f"  Nodes: {len(vis_nodes)}, Edges: {len(vis_edges)}")
    print(f"  File size: {OUTPUT_HTML.stat().st_size / 1024:.0f} KB")


def generate_html(vis_nodes, vis_edges, type_counts, rel_type_counts, all_types):
    nodes_json = json.dumps(vis_nodes, ensure_ascii=False)
    edges_json = json.dumps(vis_edges, ensure_ascii=False)
    type_counts_json = json.dumps(type_counts, ensure_ascii=False)
    rel_type_counts_json = json.dumps(rel_type_counts, ensure_ascii=False)
    colors_json = json.dumps(COLORS, ensure_ascii=False)
    labels_json = json.dumps(LABELS_CN, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Neo4j Browser - PT9L DHF Knowledge Graph</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
:root {{
    --neo4j-bg: #2a2c34;
    --neo4j-sidebar: #20222a;
    --neo4j-header: #2a2c34;
    --neo4j-border: #3a3c44;
    --neo4j-text: #bcc0c9;
    --neo4j-text-light: #858a93;
    --neo4j-highlight: #4c8eda;
    --neo4j-panel: #31333c;
    --neo4j-input: #40424b;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: "Open Sans", -apple-system, "Microsoft YaHei", sans-serif; background: var(--neo4j-bg); color: var(--neo4j-text); overflow: hidden; height: 100vh; }}

/* Header - mimics Neo4j top bar */
#neo-header {{
    height: 50px; background: var(--neo4j-header); border-bottom: 1px solid var(--neo4j-border);
    display: flex; align-items: center; padding: 0 16px; gap: 12px;
}}
#neo-header .logo {{
    display: flex; align-items: center; gap: 8px; color: #fff; font-weight: 600;
}}
#neo-header .logo svg {{ width: 24px; height: 24px; }}
#neo-header .logo span {{ font-size: 14px; letter-spacing: 0.5px; }}
#neo-query-bar {{
    flex: 1; max-width: 700px; height: 34px; background: var(--neo4j-input);
    border: 1px solid var(--neo4j-border); border-radius: 4px;
    display: flex; align-items: center; padding: 0 12px; gap: 8px;
    color: var(--neo4j-text); font-family: "Fira Code", monospace; font-size: 13px;
}}
#neo-query-bar input {{
    flex: 1; background: transparent; border: none; outline: none;
    color: #e8e8e8; font-family: "Fira Code", monospace; font-size: 13px;
}}
#neo-query-bar input::placeholder {{ color: #666; }}
#neo-query-bar button {{
    background: var(--neo4j-highlight); border: none; color: #fff; padding: 4px 10px;
    border-radius: 3px; cursor: pointer; font-size: 11px; white-space: nowrap;
}}
#neo-query-bar button:hover {{ background: #3a7bd5; }}
#query-help {{
    position: fixed; left: 260px; top: 55px; width: 500px; background: var(--neo4j-panel);
    border: 1px solid var(--neo4j-border); border-radius: 6px; padding: 16px;
    z-index: 100; display: none; font-size: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);
}}
#query-help h4 {{ color: var(--neo4j-highlight); margin-bottom: 8px; font-size: 13px; }}
#query-help .qex {{ color: #8DCC93; font-family: monospace; cursor: pointer; padding: 3px 6px;
    display: block; margin: 4px 0; border-radius: 3px; }}
#query-help .qex:hover {{ background: var(--neo4j-input); }}
#query-help .qdesc {{ color: var(--neo4j-text-light); margin-left: 8px; }}

/* Left Sidebar - mimics Neo4j DB info panel */
#neo-sidebar {{
    position: fixed; left: 0; top: 50px; bottom: 0; width: 240px;
    background: var(--neo4j-sidebar); border-right: 1px solid var(--neo4j-border);
    overflow-y: auto; padding: 16px 0; z-index: 10;
}}
#neo-sidebar::-webkit-scrollbar {{ width: 6px; }}
#neo-sidebar::-webkit-scrollbar-thumb {{ background: #555; border-radius: 3px; }}
.sidebar-section {{ padding: 0 16px; margin-bottom: 20px; }}
.sidebar-section h4 {{
    font-size: 11px; text-transform: uppercase; letter-spacing: 1px;
    color: var(--neo4j-text-light); margin-bottom: 10px; font-weight: 600;
}}
.node-label {{
    display: inline-flex; align-items: center; gap: 4px;
    padding: 4px 10px; margin: 3px 4px; border-radius: 12px;
    font-size: 12px; cursor: pointer; transition: all 0.15s;
    border: 1px solid transparent; white-space: nowrap;
}}
.node-label:hover {{ opacity: 0.85; transform: scale(1.03); }}
.node-label.active {{ border-color: rgba(255,255,255,0.4); }}
.node-label .count {{
    font-size: 10px; opacity: 0.7; margin-left: 2px;
}}
.rel-type {{
    display: inline-block; padding: 3px 8px; margin: 3px 4px;
    font-size: 11px; color: var(--neo4j-text); background: var(--neo4j-input);
    border-radius: 3px; cursor: pointer; font-family: monospace;
    border: 1px solid var(--neo4j-border); transition: all 0.15s;
}}
.rel-type:hover {{ border-color: var(--neo4j-highlight); color: #fff; }}

/* Main graph area */
#neo-graph {{
    position: fixed; left: 240px; top: 50px; right: 0; bottom: 0;
    background: var(--neo4j-bg);
}}

/* Bottom detail panel - mimics Neo4j row inspector */
#neo-detail {{
    position: fixed; left: 240px; right: 0; bottom: 0; height: 0;
    background: var(--neo4j-panel); border-top: 1px solid var(--neo4j-border);
    transition: height 0.2s ease; overflow: hidden; z-index: 20;
}}
#neo-detail.open {{ height: 220px; }}
#neo-detail-inner {{
    padding: 16px 24px; height: 100%; overflow-y: auto;
}}
#neo-detail-inner::-webkit-scrollbar {{ width: 6px; }}
#neo-detail-inner::-webkit-scrollbar-thumb {{ background: #555; border-radius: 3px; }}
.detail-header {{
    display: flex; align-items: center; gap: 12px; margin-bottom: 12px;
}}
.detail-header .node-badge {{
    display: inline-block; padding: 4px 12px; border-radius: 12px;
    font-size: 12px; font-weight: 600; color: #fff;
}}
.detail-header .close-btn {{
    margin-left: auto; cursor: pointer; opacity: 0.6; font-size: 18px;
    transition: opacity 0.15s;
}}
.detail-header .close-btn:hover {{ opacity: 1; }}
.detail-props {{
    display: grid; grid-template-columns: 150px 1fr; gap: 6px 16px;
    font-size: 13px;
}}
.detail-props .prop-key {{
    color: var(--neo4j-text-light); font-weight: 500; text-align: right;
    padding: 2px 0;
}}
.detail-props .prop-val {{
    color: #e8e8e8; word-break: break-all; padding: 2px 0;
    font-family: "Fira Code", monospace; font-size: 12px;
}}

/* Floating buttons (zoom/fit) - mimics Neo4j controls */
.graph-controls {{
    position: fixed; right: 20px; top: 70px; display: flex;
    flex-direction: column; gap: 2px; z-index: 15;
}}
.graph-controls button {{
    width: 32px; height: 32px; background: var(--neo4j-panel);
    border: 1px solid var(--neo4j-border); color: var(--neo4j-text);
    font-size: 16px; cursor: pointer; display: flex; align-items: center;
    justify-content: center; transition: all 0.15s;
}}
.graph-controls button:first-child {{ border-radius: 4px 4px 0 0; }}
.graph-controls button:last-child {{ border-radius: 0 0 4px 4px; }}
.graph-controls button:hover {{ background: var(--neo4j-input); color: #fff; }}

/* Status bar */
#neo-status {{
    position: fixed; left: 240px; bottom: 0; right: 0; height: 28px;
    background: var(--neo4j-sidebar); border-top: 1px solid var(--neo4j-border);
    display: flex; align-items: center; padding: 0 16px; z-index: 25;
    font-size: 11px; color: var(--neo4j-text-light);
}}
#neo-status.has-detail {{ bottom: 220px; }}
</style>
</head>
<body>

<!-- Header -->
<div id="neo-header">
    <div class="logo">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/>
            <line x1="12" y1="8" x2="5" y2="16"/><line x1="12" y1="8" x2="19" y2="16"/>
        </svg>
        <span>Neo4j Browser</span>
    </div>
    <div id="neo-query-bar">
        <span style="opacity:0.6;font-size:16px">$</span>
        <input id="query-input" type="text" placeholder="输入查询... (按 ? 查看帮助)" onkeydown="if(event.key==='Enter')runQuery()" onfocus="showHelp()" onblur="setTimeout(hideHelp,200)">
        <button onclick="runQuery()">Run</button>
    </div>
</div>

<!-- Query Help Panel -->
<div id="query-help">
    <h4>可用查询语句 (点击填入)</h4>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Requirement) RETURN n</span><span class="qdesc">显示所有需求节点</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Risk) RETURN n</span><span class="qdesc">显示所有风险节点</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Test) RETURN n</span><span class="qdesc">显示所有测试节点</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Requirement)-[r]->(m) RETURN n,r,m</span><span class="qdesc">需求及其关联</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Risk)-[r]->(m:RiskControl) RETURN n,r,m</span><span class="qdesc">风险-控制措施</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n)-[r:TRACES_TO]->(m) RETURN n,r,m</span><span class="qdesc">所有追溯关系</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n)-[r:VERIFIED_BY]->(m) RETURN n,r,m</span><span class="qdesc">所有验证关系</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n)-[r]->(m) WHERE r.confidence='high' RETURN n,r,m</span><span class="qdesc">高置信度关系</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n) WHERE n.label CONTAINS '温度' RETURN n</span><span class="qdesc">搜索包含"温度"的节点</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n:Document)-[r]->(m) RETURN n,r,m</span><span class="qdesc">文档及其关联</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n) RETURN n LIMIT 50</span><span class="qdesc">显示前50个节点</span>
    <span class="qex" onclick="setQuery(this)">MATCH (n)-[r]->(m) RETURN n,r,m</span><span class="qdesc">显示全部有关系的节点</span>
</div>

<!-- Left Sidebar -->
<div id="neo-sidebar">
    <div class="sidebar-section">
        <h4>Node Labels</h4>
        <div id="label-list"></div>
    </div>
    <div class="sidebar-section">
        <h4>Relationship Types</h4>
        <div id="rel-list"></div>
    </div>
</div>

<!-- Graph -->
<div id="neo-graph"></div>

<!-- Graph Controls -->
<div class="graph-controls">
    <button onclick="zoomIn()" title="Zoom In">+</button>
    <button onclick="zoomOut()" title="Zoom Out">&minus;</button>
    <button onclick="fitGraph()" title="Fit to Screen">&#8644;</button>
</div>

<!-- Status Bar -->
<div id="neo-status">
    <span id="status-text"></span>
</div>

<!-- Detail Panel -->
<div id="neo-detail">
    <div id="neo-detail-inner"></div>
</div>

<script>
var rawNodes = {nodes_json};
var rawEdges = {edges_json};
var typeCounts = {type_counts_json};
var relTypeCounts = {rel_type_counts_json};
var nodeColors = {colors_json};
var nodeLabels = {labels_json};

// Active filters
var activeLabels = new Set(Object.keys(typeCounts));
var activeRelTypes = new Set(Object.keys(relTypeCounts));

// Build sidebar
(function buildSidebar() {{
    var labelList = document.getElementById("label-list");
    var sorted = Object.entries(typeCounts).sort((a,b) => b[1] - a[1]);
    sorted.forEach(function([type, count]) {{
        var el = document.createElement("span");
        el.className = "node-label active";
        el.style.background = nodeColors[type] || "#666";
        el.style.color = "#fff";
        el.dataset.type = type;
        el.innerHTML = (nodeLabels[type] || type) + ' <span class="count">(' + count + ')</span>';
        el.onclick = function() {{
            toggleLabel(type, el);
        }};
        labelList.appendChild(el);
    }});

    var relList = document.getElementById("rel-list");
    Object.entries(relTypeCounts).sort((a,b) => b[1] - a[1]).forEach(function([type, count]) {{
        var el = document.createElement("span");
        el.className = "rel-type";
        el.dataset.type = type;
        el.textContent = ":" + type + " (" + count + ")";
        el.onclick = function() {{
            toggleRelType(type, el);
        }};
        relList.appendChild(el);
    }});
}})();

function toggleLabel(type, el) {{
    if (activeLabels.has(type)) {{
        activeLabels.delete(type);
        el.classList.remove("active");
        el.style.opacity = "0.4";
    }} else {{
        activeLabels.add(type);
        el.classList.add("active");
        el.style.opacity = "1";
    }}
    rebuildGraph();
}}

function toggleRelType(type, el) {{
    if (activeRelTypes.has(type)) {{
        activeRelTypes.delete(type);
        el.style.opacity = "0.4";
        el.style.borderColor = "transparent";
    }} else {{
        activeRelTypes.add(type);
        el.style.opacity = "1";
        el.style.borderColor = "";
    }}
    rebuildGraph();
}}

// vis.js network
var network = null;
var nodes, edges;

function buildVisData() {{
    var visibleNodeIds = new Set();
    var vn = rawNodes.filter(function(n) {{
        if (!activeLabels.has(n.group)) return false;
        visibleNodeIds.add(n.id);
        return true;
    }}).map(function(n) {{
        return {{
            id: n.id,
            label: n.label,
            group: n.group,
            color: {{
                background: n.color,
                border: n.color,
                highlight: {{ background: lighten(n.color), border: "#fff" }},
                hover: {{ background: lighten(n.color), border: "#ccc" }},
            }},
            font: {{ color: "#fff", size: 11, face: "Open Sans, Microsoft YaHei" }},
            shape: "dot",
            size: getNodeSize(n.group),
            borderWidth: 2,
            shadow: {{ enabled: true, size: 6, color: "rgba(0,0,0,0.3)" }},
        }};
    }});

    var ve = rawEdges.filter(function(e) {{
        return visibleNodeIds.has(e.from) && visibleNodeIds.has(e.to) && activeRelTypes.has(e.type);
    }}).map(function(e) {{
        var edgeColor = e.cross_doc ? "#e8a838" : "#5a6a7a";
        return {{
            id: e.id, from: e.from, to: e.to, label: e.type,
            color: {{ color: edgeColor, highlight: "#fff", hover: "#aab4be" }},
            font: {{ size: 9, color: "#8c939c", strokeWidth: 0, face: "monospace" }},
            arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }},
            width: e.cross_doc ? 1.8 : 1,
            smooth: {{ enabled: true, type: "curvedCW", roundness: 0.12 }},
            dashes: e.cross_doc ? false : [5, 5],
            chosen: {{ edge: function(values) {{ values.width = 2.5; values.color = "#fff"; }} }},
        }};
    }});

    return {{ nodes: vn, edges: ve }};
}}

function getNodeSize(group) {{
    if (group === "documents") return 20;
    if (group === "requirements" || group === "risks") return 14;
    if (group === "semantic_fragments" || group === "plan_tasks") return 7;
    return 10;
}}

function lighten(hex) {{
    var r = parseInt(hex.slice(1,3),16), g = parseInt(hex.slice(3,5),16), b = parseInt(hex.slice(5,7),16);
    r = Math.min(255, r + 40); g = Math.min(255, g + 40); b = Math.min(255, b + 40);
    return "#" + [r,g,b].map(x => x.toString(16).padStart(2,"0")).join("");
}}

function rebuildGraph() {{
    var d = buildVisData();
    if (network) {{
        nodes.clear(); edges.clear();
        nodes.add(d.nodes); edges.add(d.edges);
    }} else {{
        initNetwork(d);
    }}
    updateStatus();
}}

function initNetwork(d) {{
    var container = document.getElementById("neo-graph");
    nodes = new vis.DataSet(d.nodes);
    edges = new vis.DataSet(d.edges);
    var options = {{
        physics: {{
            enabled: true,
            stabilization: {{ iterations: 150, fit: true }},
            barnesHut: {{
                gravitationalConstant: -4000,
                centralGravity: 0.2,
                springLength: 130,
                springConstant: 0.04,
                damping: 0.1,
                avoidOverlap: 0.1,
            }},
        }},
        interaction: {{
            hover: true,
            tooltipDelay: 300,
            zoomView: true,
            dragView: true,
            multiselect: true,
        }},
        layout: {{ improvedLayout: true }},
    }};
    network = new vis.Network(container, {{ nodes: nodes, edges: edges }}, options);
    network.on("click", onNodeClick);
    network.on("doubleClick", onDoubleClick);
}}

function onNodeClick(params) {{
    if (params.nodes.length > 0) {{
        var nodeId = params.nodes[0];
        var raw = rawNodes.find(n => n.id === nodeId);
        if (raw) showDetail(raw);
    }} else if (params.edges.length > 0) {{
        var edgeId = params.edges[0];
        var raw = rawEdges.find(e => e.id === edgeId);
        if (raw) showEdgeDetail(raw);
    }} else {{
        closeDetail();
    }}
}}

function onDoubleClick(params) {{
    if (params.nodes.length > 0) {{
        network.focus(params.nodes[0], {{ scale: 1.5, animation: true }});
    }}
}}

function showDetail(node) {{
    var panel = document.getElementById("neo-detail");
    var inner = document.getElementById("neo-detail-inner");
    var color = node.color;
    var typeLabel = nodeLabels[node.group] || node.group;

    var html = '<div class="detail-header">';
    html += '<span class="node-badge" style="background:' + color + '">' + typeLabel + '</span>';
    html += '<span style="font-size:14px;color:#fff">' + (node.label || '') + '</span>';
    html += '<span class="close-btn" onclick="closeDetail()">&#x2715;</span>';
    html += '</div>';
    html += '<div class="detail-props">';
    if (node.properties) {{
        Object.entries(node.properties).forEach(function([k, v]) {{
            html += '<div class="prop-key">' + k + '</div>';
            html += '<div class="prop-val">' + escHtml(v) + '</div>';
        }});
    }}
    html += '</div>';

    inner.innerHTML = html;
    panel.classList.add("open");
    document.getElementById("neo-status").classList.add("has-detail");
}}

function showEdgeDetail(edge) {{
    var panel = document.getElementById("neo-detail");
    var inner = document.getElementById("neo-detail-inner");

    var html = '<div class="detail-header">';
    html += '<span class="node-badge" style="background:#6e7a8a">RELATIONSHIP</span>';
    html += '<span style="font-size:14px;color:#fff">:' + edge.type + '</span>';
    html += '<span class="close-btn" onclick="closeDetail()">&#x2715;</span>';
    html += '</div>';
    html += '<div class="detail-props">';
    if (edge.properties) {{
        Object.entries(edge.properties).forEach(function([k, v]) {{
            html += '<div class="prop-key">' + k + '</div>';
            html += '<div class="prop-val">' + escHtml(v) + '</div>';
        }});
    }}
    html += '</div>';

    inner.innerHTML = html;
    panel.classList.add("open");
    document.getElementById("neo-status").classList.add("has-detail");
}}

function closeDetail() {{
    document.getElementById("neo-detail").classList.remove("open");
    document.getElementById("neo-status").classList.remove("has-detail");
}}

function escHtml(s) {{
    return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}}

function updateStatus() {{
    var visNodes = nodes ? nodes.length : 0;
    var visEdges = edges ? edges.length : 0;
    document.getElementById("status-text").textContent =
        "Displaying " + visNodes + " nodes, " + visEdges + " relationships.";
}}

function zoomIn() {{ network.moveTo({{ scale: network.getScale() * 1.3, animation: true }}); }}
function zoomOut() {{ network.moveTo({{ scale: network.getScale() / 1.3, animation: true }}); }}
function fitGraph() {{ network.fit({{ animation: true }}); }}

// Query engine
var typeAliases = {{
    "Requirement": "requirements", "requirement": "requirements",
    "DesignInput": "design_inputs", "designinput": "design_inputs",
    "Test": "tests", "test": "tests",
    "Risk": "risks", "risk": "risks",
    "RiskControl": "risk_controls", "riskcontrol": "risk_controls",
    "Regulation": "regulations", "regulation": "regulations",
    "Function": "functions", "function": "functions",
    "Person": "persons", "person": "persons",
    "Document": "documents", "document": "documents",
    "PlanTask": "plan_tasks", "plantask": "plan_tasks",
    "SoftwareItem": "software_items", "softwareitem": "software_items",
    "DocIndexEntry": "doc_index_entries", "docindexentry": "doc_index_entries",
    "Product": "products", "product": "products",
    "ReviewItem": "review_items", "reviewitem": "review_items",
    "SemanticFragment": "semantic_fragments", "semanticfragment": "semantic_fragments",
    "Component": "components", "component": "components",
    "TestMeasurement": "test_measurements", "testmeasurement": "test_measurements",
}};

function showHelp() {{ document.getElementById("query-help").style.display = "block"; }}
function hideHelp() {{ document.getElementById("query-help").style.display = "none"; }}
function setQuery(el) {{
    document.getElementById("query-input").value = el.textContent;
    hideHelp();
    runQuery();
}}

function runQuery() {{
    var q = document.getElementById("query-input").value.trim();
    if (!q) return;
    hideHelp();

    var result = parseAndExecute(q);
    if (result.error) {{
        alert("查询错误: " + result.error);
        return;
    }}

    // Apply result to graph
    var nodeSet = new Set(result.nodeIds);
    var vn = rawNodes.filter(n => nodeSet.has(n.id)).map(n => ({{
        id: n.id, label: n.label, group: n.group,
        color: {{ background: n.color, border: n.color,
            highlight: {{ background: lighten(n.color), border: "#fff" }},
            hover: {{ background: lighten(n.color), border: "#ccc" }} }},
        font: {{ color: "#fff", size: 11, face: "Open Sans, Microsoft YaHei" }},
        shape: "dot", size: getNodeSize(n.group), borderWidth: 2,
        shadow: {{ enabled: true, size: 6, color: "rgba(0,0,0,0.3)" }},
    }}));
    var ve = rawEdges.filter(e => result.edgeIds.has(e.id)).map(e => {{
        var edgeColor = e.cross_doc ? "#e8a838" : "#5a6a7a";
        return {{
            id: e.id, from: e.from, to: e.to, label: e.type,
            color: {{ color: edgeColor, highlight: "#fff", hover: "#aab4be" }},
            font: {{ size: 9, color: "#8c939c", strokeWidth: 0, face: "monospace" }},
            arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }},
            width: e.cross_doc ? 1.8 : 1,
            smooth: {{ enabled: true, type: "curvedCW", roundness: 0.12 }},
            dashes: e.cross_doc ? false : [5, 5],
        }};
    }});

    if (network) {{
        nodes.clear(); edges.clear();
        nodes.add(vn); edges.add(ve);
    }} else {{
        initNetwork({{ nodes: vn, edges: ve }});
    }}
    updateStatus();
}}

function parseAndExecute(q) {{
    var nodeIds = [];
    var edgeIds = new Set();

    // Parse LIMIT
    var limit = Infinity;
    var limitMatch = q.match(/LIMIT\\s+(\\d+)/i);
    if (limitMatch) limit = parseInt(limitMatch[1]);

    // Parse WHERE clause for property filtering
    var whereClause = null;
    var whereMatch = q.match(/WHERE\\s+(.+?)\\s+(RETURN|$)/i);
    if (whereMatch) whereClause = whereMatch[1].trim();

    // Parse relationship type filter: -[r:TYPE]->
    var relTypeFilter = null;
    var relMatch = q.match(/\\[\\w*:(\\w+)\\]/);
    if (relMatch) relTypeFilter = relMatch[1];

    // Parse edge property filter: WHERE r.prop='val'
    var edgePropFilter = null;
    if (whereClause) {{
        var epf = whereClause.match(/r\\.(\\w+)\\s*=\\s*'([^']+)'/);
        if (epf) edgePropFilter = {{ key: epf[1], val: epf[2] }};
    }}

    // Parse node label: (n:Label)
    var labelMatch = q.match(/\\(\\w+:(\\w+)\\)/);
    var targetLabel = labelMatch ? labelMatch[1] : null;
    var targetGroup = targetLabel ? (typeAliases[targetLabel] || typeAliases[targetLabel.toLowerCase()]) : null;

    // Parse second node label for pattern: (n:A)-[r]->(m:B)
    var secondLabelMatch = q.match(/->\\s*\\(\\w+:(\\w+)\\)/);
    var secondGroup = secondLabelMatch ? (typeAliases[secondLabelMatch[1]] || typeAliases[secondLabelMatch[1].toLowerCase()]) : null;

    // Detect if query has relationship pattern
    var hasRel = /\\)-\\[/.test(q);

    // Parse text search: WHERE n.label CONTAINS 'text' or WHERE n.prop CONTAINS 'text'
    var textSearch = null;
    if (whereClause && !edgePropFilter) {{
        var tsm = whereClause.match(/(\\w+)\\.(\\w+)\\s+CONTAINS\\s+'([^']+)'/i);
        if (tsm) textSearch = {{ prop: tsm[2], text: tsm[3].toLowerCase() }};
    }}

    if (hasRel) {{
        // Relationship query: find edges and connected nodes
        rawEdges.forEach(function(e) {{
            // Filter by relationship type
            if (relTypeFilter && e.type !== relTypeFilter) return;
            // Filter by edge property
            if (edgePropFilter && e.properties) {{
                if ((e.properties[edgePropFilter.key] || '') !== edgePropFilter.val) return;
            }}
            var fromNode = rawNodes.find(n => n.id === e.from);
            var toNode = rawNodes.find(n => n.id === e.to);
            if (!fromNode || !toNode) return;
            // Filter by source label
            if (targetGroup && fromNode.group !== targetGroup) return;
            // Filter by target label
            if (secondGroup && toNode.group !== secondGroup) return;
            edgeIds.add(e.id);
            nodeIds.push(fromNode.id);
            nodeIds.push(toNode.id);
        }});
    }} else {{
        // Node-only query
        rawNodes.forEach(function(n) {{
            if (targetGroup && n.group !== targetGroup) return;
            if (textSearch) {{
                var searchIn = "";
                if (textSearch.prop === "label") {{
                    searchIn = (n.label || "").toLowerCase();
                }} else if (n.properties && n.properties[textSearch.prop]) {{
                    searchIn = n.properties[textSearch.prop].toLowerCase();
                }} else {{
                    // Search all properties
                    searchIn = Object.values(n.properties || {{}}).join(" ").toLowerCase();
                }}
                if (!searchIn.includes(textSearch.text)) return;
            }}
            nodeIds.push(n.id);
        }});
    }}

    // Deduplicate and apply limit
    nodeIds = [...new Set(nodeIds)].slice(0, limit);

    return {{ nodeIds: nodeIds, edgeIds: edgeIds }};
}}

// Init
rebuildGraph();
</script>
</body>
</html>'''


if __name__ == "__main__":
    main()
