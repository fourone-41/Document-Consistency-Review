"""
Generate a side-by-side review HTML:
  Left panel: original markdown source
  Right panel: extracted nodes/edges/claims from that file
"""
import json
import html
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
MARKDOWN_DIR = PROJECT_ROOT / "pt9l_markdown_output"
PER_FILE_DIR = Path(__file__).parent / "output" / "per_file"
OUTPUT_HTML = Path(__file__).parent / "output" / "review_comparison.html"

SOURCE_FILES = [
    "01 立项批准书E0 23.11/客户需求书E0-血压计 23.6.via_xlsx.clean.md",
    "01 立项批准书E0 23.11/立项批准书E0 23.11.via_lo_html.clean.md",
    "02 开发计划E0 23.11/设计开发计划表E0  23.11.via_xlsx.clean.md",
    "03 风险分析/PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md",
    "04 设计输入E0 23.11/设计输入汇总表E0  20211118.via_xlsx.clean.md",
    "07 软件设计方案E0 23.11/软件需求E0 23.11/2-1 软件需求规格E0 23.11.via_lo_html.clean.md",
    "07 软件设计方案E0 23.11/软件需求E0 23.11/软件需求规格书评审检查表E0 23.11.via_xlsx.clean.md",
    "11 T1样机/PT9L包装BOM.via_xlsx.clean.md",
    "11 T1样机/PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md",
    "PT9L-DHF清单-常规.via_xlsx.clean.md",
]


def source_to_json_name(src: str) -> str:
    return src.replace("/", "__").replace("\\", "__").replace(".md", ".json")


SKIP_KEYS = {"_meta", "_edges", "_claims", "document"}

def render_nodes_section(data: dict) -> str:
    """Render the nodes from extraction JSON as readable HTML."""
    parts = []

    # Handle 'document' as a single-node section
    if "document" in data and isinstance(data["document"], dict):
        doc = data["document"]
        parts.append('<div class="node-group">')
        parts.append('<h4 class="node-type">document <span class="count">(1)</span></h4>')
        parts.append('<table class="extract-table"><thead><tr>')
        keys = [k for k in doc.keys() if k != "_source"]
        for k in keys:
            parts.append(f"<th>{html.escape(k)}</th>")
        parts.append("</tr></thead><tbody><tr>")
        for k in keys:
            val = doc.get(k, "") or ""
            parts.append(f"<td>{html.escape(str(val))}</td>")
        parts.append("</tr></tbody></table></div>")

    for node_type, items in data.items():
        if node_type in SKIP_KEYS:
            continue
        if not isinstance(items, list) or not items:
            continue
        if not isinstance(items[0], dict):
            continue
        parts.append(f'<div class="node-group">')
        parts.append(f'<h4 class="node-type">{html.escape(node_type)} <span class="count">({len(items)})</span></h4>')
        parts.append('<table class="extract-table"><thead><tr>')
        keys = [k for k in items[0].keys() if k != "_source"]
        for k in keys:
            parts.append(f"<th>{html.escape(k)}</th>")
        parts.append("</tr></thead><tbody>")
        for item in items:
            parts.append("<tr>")
            for k in keys:
                val = item.get(k, "")
                if val is None:
                    val = ""
                parts.append(f"<td>{html.escape(str(val))}</td>")
            parts.append("</tr>")
        parts.append("</tbody></table></div>")
    return "\n".join(parts)


def render_edges_section(data: dict) -> str:
    edges = data.get("_edges", [])
    if not edges:
        return '<p class="empty">(no edges)</p>'
    parts = ['<table class="extract-table"><thead><tr><th>type</th><th>from</th><th>to</th><th>properties</th></tr></thead><tbody>']
    for e in edges:
        props = e.get("properties", {})
        prop_str = ", ".join(f"{k}={v}" for k, v in props.items()) if props else ""
        parts.append(f'<tr><td>{html.escape(e.get("type",""))}</td><td>{html.escape(str(e.get("from","")))}</td><td>{html.escape(str(e.get("to","")))}</td><td>{html.escape(prop_str)}</td></tr>')
    parts.append("</tbody></table>")
    return "\n".join(parts)


def render_claims_section(data: dict) -> str:
    claims = data.get("_claims", [])
    if not claims:
        return '<p class="empty">(no claims)</p>'
    parts = ['<table class="extract-table"><thead><tr><th>Subject</th><th>Attribute</th><th>Value</th><th>Unit</th><th>Tolerance</th><th>Condition</th><th>Raw Text</th></tr></thead><tbody>']
    for c in claims:
        parts.append("<tr>")
        for k in ["subject", "attribute", "value", "unit", "tolerance", "condition", "raw_text"]:
            val = c.get(k, "") or ""
            parts.append(f"<td>{html.escape(str(val))}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "\n".join(parts)


def build_html():
    file_sections = []

    for idx, src in enumerate(SOURCE_FILES):
        md_path = MARKDOWN_DIR / src
        json_name = source_to_json_name(src)
        json_path = PER_FILE_DIR / json_name

        md_content = ""
        if md_path.exists():
            md_content = md_path.read_text(encoding="utf-8")
        else:
            md_content = f"[文件不存在: {md_path}]"

        extract_data = {}
        if json_path.exists():
            extract_data = json.loads(json_path.read_text(encoding="utf-8"))
        else:
            for f in PER_FILE_DIR.iterdir():
                if f.suffix == ".json":
                    try:
                        d = json.loads(f.read_text(encoding="utf-8"))
                        meta = d.get("_meta", {})
                        if meta.get("source_file", "") == src:
                            extract_data = d
                            break
                    except:
                        pass
            if not extract_data:
                for f in PER_FILE_DIR.iterdir():
                    if f.suffix == ".json":
                        try:
                            d = json.loads(f.read_text(encoding="utf-8"))
                            meta = d.get("_meta", {})
                            sf = meta.get("source_file", "")
                            if sf and (sf in src or src in sf):
                                extract_data = d
                                break
                        except:
                            pass

        nodes_html = render_nodes_section(extract_data)
        edges_html = render_edges_section(extract_data)
        claims_html = render_claims_section(extract_data)

        short_name = src.split("/")[-1]
        folder_name = "/".join(src.split("/")[:-1]) if "/" in src else ""

        section = f'''
        <div class="file-section" id="file-{idx}">
            <div class="file-header">
                <span class="file-index">#{idx+1}</span>
                <span class="file-name">{html.escape(short_name)}</span>
                <span class="file-folder">{html.escape(folder_name)}</span>
            </div>
            <div class="comparison-row">
                <div class="panel left-panel">
                    <div class="panel-header">原文 (Markdown)</div>
                    <div class="panel-content"><pre>{html.escape(md_content)}</pre></div>
                </div>
                <div class="panel right-panel">
                    <div class="panel-header">抽取结果</div>
                    <div class="panel-content">
                        <h3>节点 (Nodes)</h3>
                        {nodes_html}
                        <h3>边 (Edges)</h3>
                        {edges_html}
                        <h3>事实断言 (Claims)</h3>
                        {claims_html}
                    </div>
                </div>
            </div>
        </div>
        '''
        file_sections.append(section)

    nav_items = ""
    for idx, src in enumerate(SOURCE_FILES):
        short = src.split("/")[-1][:30]
        nav_items += f'<a href="#file-{idx}" class="nav-item" title="{html.escape(src)}">{idx+1}. {html.escape(short)}</a>\n'

    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>抽取结果对比审查</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, "Microsoft YaHei", sans-serif; background: #f5f5f5; }}
.top-nav {{
    position: sticky; top: 0; z-index: 100;
    background: #1a1a2e; color: white; padding: 10px 20px;
    display: flex; flex-wrap: wrap; gap: 6px; align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}}
.top-nav h1 {{ font-size: 16px; margin-right: 20px; white-space: nowrap; }}
.nav-item {{
    color: #aaddff; text-decoration: none; font-size: 12px;
    padding: 3px 8px; border-radius: 4px; background: rgba(255,255,255,0.1);
    white-space: nowrap;
}}
.nav-item:hover {{ background: rgba(255,255,255,0.25); }}
.file-section {{ margin: 20px; }}
.file-header {{
    background: #2d3748; color: white; padding: 12px 20px;
    border-radius: 8px 8px 0 0; display: flex; align-items: center; gap: 12px;
}}
.file-index {{ background: #4299e1; padding: 2px 10px; border-radius: 12px; font-weight: bold; }}
.file-name {{ font-size: 15px; font-weight: 600; }}
.file-folder {{ font-size: 12px; color: #a0aec0; }}
.comparison-row {{
    display: flex; border: 1px solid #e2e8f0;
    border-radius: 0 0 8px 8px; overflow: hidden;
    min-height: 400px; max-height: 800px;
}}
.panel {{ flex: 1; overflow: auto; max-height: 800px; }}
.left-panel {{ border-right: 3px solid #4299e1; background: #fffef7; }}
.right-panel {{ background: #ffffff; }}
.panel-header {{
    position: sticky; top: 0; z-index: 10;
    background: #edf2f7; padding: 8px 16px;
    font-weight: 600; font-size: 13px; color: #4a5568;
    border-bottom: 1px solid #e2e8f0;
}}
.panel-content {{ padding: 12px 16px; font-size: 13px; line-height: 1.6; }}
.panel-content pre {{
    white-space: pre-wrap; word-wrap: break-word;
    font-family: "Consolas", "Source Code Pro", monospace;
    font-size: 12px; color: #2d3748;
}}
.panel-content h3 {{
    margin: 16px 0 8px; padding: 4px 8px;
    background: #ebf8ff; border-left: 4px solid #4299e1;
    font-size: 14px; color: #2c5282;
}}
.node-group {{ margin-bottom: 12px; }}
.node-type {{ font-size: 13px; color: #553c9a; margin: 6px 0; }}
.node-type .count {{ color: #9b2c2c; font-size: 11px; }}
.extract-table {{
    width: 100%; border-collapse: collapse; font-size: 11px; margin-bottom: 8px;
}}
.extract-table th {{
    background: #f7fafc; border: 1px solid #e2e8f0; padding: 4px 6px;
    text-align: left; font-size: 11px; color: #4a5568;
}}
.extract-table td {{
    border: 1px solid #e2e8f0; padding: 3px 6px;
    max-width: 200px; overflow: hidden; text-overflow: ellipsis;
    white-space: nowrap;
}}
.extract-table tr:hover td {{ background: #fffff0; }}
.empty {{ color: #a0aec0; font-style: italic; font-size: 12px; }}
</style>
</head>
<body>
<nav class="top-nav">
    <h1>抽取结果对比审查 (10 files)</h1>
    {nav_items}
</nav>
{"".join(file_sections)}
</body>
</html>'''

    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(full_html, encoding="utf-8")
    print(f"[OK] HTML generated: {OUTPUT_HTML}")
    print(f"  size: {OUTPUT_HTML.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    build_html()
