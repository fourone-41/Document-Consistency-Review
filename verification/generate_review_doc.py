"""
生成左右对照审查文档：左边原文件全文，右边放raw_extraction的JSON全文（原样）
"""
import json
import os
from pathlib import Path

OUTPUT_DIR = Path(r"D:\项目文档一致性审查\verification\output")
RAW_DIR = OUTPUT_DIR / "raw_extraction"
REVIEW_OUTPUT = OUTPUT_DIR / "extraction_review.html"

FILES = [
    {
        "source": Path(r"D:\项目文档一致性审查\pt9l_markdown_output\01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md"),
        "extraction": RAW_DIR / "客户需求书E0-血压计 23.6.via_xlsx.clean.json",
        "label": "客户需求书",
    },
    {
        "source": Path(r"D:\项目文档一致性审查\pt9l_markdown_output\04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md"),
        "extraction": RAW_DIR / "设计输入汇总表E0  20211118.via_xlsx.clean.json",
        "label": "设计输入汇总表",
    },
    {
        "source": Path(r"D:\项目文档一致性审查\pt9l_markdown_output\11 T1样机\PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md"),
        "extraction": RAW_DIR / "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.json",
        "label": "检测报告",
    },
]


def escape_html(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def generate_html():
    sections = []

    for idx, f in enumerate(FILES):
        source_text = ""
        if f["source"].exists():
            with open(f["source"], "r", encoding="utf-8") as fp:
                source_text = fp.read()

        extraction_text = ""
        if f["extraction"].exists():
            with open(f["extraction"], "r", encoding="utf-8") as fp:
                raw = json.load(fp)
                extraction_text = json.dumps(raw, ensure_ascii=False, indent=2)

        sections.append(f"""
        <div class="file-block" id="file-{idx}">
            <div class="file-title">{escape_html(f['label'])} &mdash; {escape_html(f['source'].name)}</div>
            <div class="split-view">
                <div class="pane left-pane">
                    <div class="pane-header">原文件 ({escape_html(f['source'].name)})</div>
                    <pre class="content">{escape_html(source_text)}</pre>
                </div>
                <div class="divider"></div>
                <div class="pane right-pane">
                    <div class="pane-header">抽取结果 ({escape_html(f['extraction'].name)})</div>
                    <pre class="content">{escape_html(extraction_text)}</pre>
                </div>
            </div>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>抽取对照审查 - 左原文 | 右JSON</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: "Consolas", "Microsoft YaHei", monospace;
            font-size: 13px;
            background: #1e1e2e;
            color: #cdd6f4;
        }}
        .nav {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: #181825;
            padding: 10px 20px;
            border-bottom: 1px solid #313244;
            display: flex;
            gap: 20px;
            align-items: center;
        }}
        .nav-title {{
            font-size: 15px;
            font-weight: bold;
            color: #89b4fa;
        }}
        .nav a {{
            color: #a6e3a1;
            text-decoration: none;
            padding: 4px 12px;
            border-radius: 4px;
            background: #313244;
        }}
        .nav a:hover {{ background: #45475a; }}
        .file-block {{
            margin: 16px;
        }}
        .file-title {{
            background: #313244;
            color: #cba6f7;
            padding: 10px 20px;
            font-size: 15px;
            font-weight: bold;
            border-radius: 8px 8px 0 0;
            border-bottom: 2px solid #cba6f7;
        }}
        .split-view {{
            display: flex;
            height: 80vh;
            border: 1px solid #313244;
            border-radius: 0 0 8px 8px;
            overflow: hidden;
        }}
        .pane {{
            flex: 1;
            overflow: auto;
            padding: 0;
        }}
        .left-pane {{ background: #1e1e2e; }}
        .right-pane {{ background: #181825; }}
        .pane-header {{
            position: sticky;
            top: 0;
            z-index: 10;
            padding: 8px 16px;
            font-weight: bold;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .left-pane .pane-header {{
            background: #1e1e2e;
            color: #89b4fa;
            border-bottom: 1px solid #313244;
        }}
        .right-pane .pane-header {{
            background: #181825;
            color: #a6e3a1;
            border-bottom: 1px solid #313244;
        }}
        .divider {{
            width: 3px;
            background: #45475a;
            cursor: col-resize;
        }}
        .content {{
            padding: 12px 16px;
            white-space: pre-wrap;
            word-wrap: break-word;
            line-height: 1.7;
            font-size: 13px;
        }}
        .left-pane .content {{ color: #cdd6f4; }}
        .right-pane .content {{ color: #bac2de; }}
        .pane::-webkit-scrollbar {{ width: 8px; }}
        .pane::-webkit-scrollbar-track {{ background: transparent; }}
        .pane::-webkit-scrollbar-thumb {{ background: #45475a; border-radius: 4px; }}
        .pane::-webkit-scrollbar-thumb:hover {{ background: #585b70; }}

        @media print {{
            .nav {{ display: none; }}
            .split-view {{ height: auto; flex-direction: column; }}
            .pane {{ overflow: visible; }}
            .divider {{ height: 2px; width: 100%; }}
        }}
    </style>
</head>
<body>
    <div class="nav">
        <span class="nav-title">抽取对照审查</span>
        <a href="#file-0">客户需求书</a>
        <a href="#file-1">设计输入汇总表</a>
        <a href="#file-2">检测报告</a>
        <span style="color:#6c7086; margin-left:auto;">左=源文件原文 | 右=raw_extraction JSON原文 | 两边独立滚动 | 中间可拖拽</span>
    </div>
    {''.join(sections)}
    <script>
        document.querySelectorAll('.divider').forEach(divider => {{
            let isResizing = false;
            divider.addEventListener('mousedown', e => {{
                isResizing = true;
                document.body.style.cursor = 'col-resize';
                document.body.style.userSelect = 'none';
            }});
            document.addEventListener('mousemove', e => {{
                if (!isResizing) return;
                const container = divider.parentElement;
                const rect = container.getBoundingClientRect();
                const offset = e.clientX - rect.left;
                const pct = (offset / rect.width) * 100;
                if (pct > 20 && pct < 80) {{
                    container.querySelector('.left-pane').style.flex = `0 0 ${{pct}}%`;
                    container.querySelector('.right-pane').style.flex = `0 0 ${{100 - pct}}%`;
                }}
            }});
            document.addEventListener('mouseup', () => {{
                isResizing = false;
                document.body.style.cursor = '';
                document.body.style.userSelect = '';
            }});
        }});
    </script>
</body>
</html>"""

    with open(REVIEW_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Generated: {REVIEW_OUTPUT}")
    print(f"     Size: {os.path.getsize(REVIEW_OUTPUT) / 1024:.1f} KB")


if __name__ == "__main__":
    generate_html()
