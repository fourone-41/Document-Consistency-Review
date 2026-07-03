# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PT9L_MD = Path("D:/AI_0415/03DHF/PT9L_MD")
MANIFEST = PT9L_MD / "_manifests" / "word_conversion_manifest.csv"
WIKI_ROOT = PT9L_MD / "llm_wiki"
SOURCES_DIR = WIKI_ROOT / "sources" / "word"
WIKI_DIR = WIKI_ROOT / "wiki"
MANIFESTS_DIR = WIKI_ROOT / "manifests"


def now() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat(sep=" ")


def safe_part(text: str, max_len: int = 100) -> str:
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", text)
    text = re.sub(r"\s+", "_", text).strip("._ ")
    return (text or "unnamed")[:max_len]


def read_manifest() -> list[dict[str, str]]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def stage_from_rel(rel: str) -> str:
    parts = rel.replace("\\", "/").split("/")
    if not parts:
        return "unknown"
    if parts[0].startswith("02_RnD_DHF"):
        if len(parts) >= 2:
            return f"DHF - {parts[1]}"
        return "DHF"
    if parts[0].startswith("03_Mfg_SOP"):
        return "Manufacturing SOP"
    if "DMR" in rel.upper():
        return "DMR"
    return parts[0]


def source_copy_path(row: dict[str, str]) -> Path:
    rel = row["source_relative_path"].replace("\\", "/")
    parent = Path(*Path(rel).parts[:-1]) if "/" in rel else Path()
    stem = safe_part(Path(row["output_markdown"]).stem)
    return SOURCES_DIR / parent / f"{stem}.source.md"


def wiki_link(path: Path, base: Path = WIKI_ROOT) -> str:
    return path.relative_to(base).as_posix()


def copy_sources(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, 1):
        src = Path(row["output_markdown"])
        dst = source_copy_path(row)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        record = dict(row)
        record["wiki_source_path"] = str(dst)
        record["wiki_source_rel"] = wiki_link(dst)
        record["wiki_id"] = f"PT9L-WORD-{idx:04d}"
        record["stage"] = stage_from_rel(row["source_relative_path"])
        records.append(record)
    return records


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def md_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * len(header)) + " |"]
    for row in rows[1:]:
        escaped = [str(cell).replace("\n", " ").replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(escaped) + " |")
    return lines


def write_agents() -> None:
    (WIKI_ROOT / "AGENTS.md").write_text(
        "\n".join(
            [
                "# PT9L LLM Wiki Agent Rules",
                "",
                "This is a Karpathy-style LLM Wiki for PT9L DHF/DMR evidence.",
                "",
                "## Layers",
                "",
                "- `sources/`: immutable source markdown copied from `PT9L_MD` conversion outputs. Do not edit these files by hand.",
                "- `wiki/`: AI-maintained summaries, indexes, topic pages, risk pages, and synthesis pages.",
                "- `manifests/`: machine-readable catalogs used to rebuild indexes and verify coverage.",
                "",
                "## Required Workflow",
                "",
                "1. For answering questions, read `wiki/index.md` first, then the relevant page, then the linked source markdown.",
                "2. For evidence-critical claims, cite source paths from `sources/` or original paths from `manifests/source_catalog.csv`.",
                "3. Do not treat Markdown text as complete evidence when the manifest says `loss_risk_level` is `high` or `medium`.",
                "4. For high-risk files, inspect the `.assets` folder listed in `source_catalog.csv`, especially images, `visual_format_manifest.csv`, and `conversion_loss.json`.",
                "5. If a source has visual-format evidence, preserve color/highlight meaning in the wiki page. Empty tables plus legends are not enough.",
                "6. When adding new converted files, rerun `build_pt9l_llm_wiki.py` or update `sources/`, `manifests/`, `wiki/index.md`, and `llms.txt` consistently.",
                "",
                "## Page Types",
                "",
                "- `wiki/index.md`: main navigation and current coverage.",
                "- `wiki/source_catalog.md`: all converted Word source pages.",
                "- `wiki/high_risk_conversion_gaps.md`: files that need manual review before formal audit.",
                "- `wiki/stages/*.md`: DHF/DMR/manufacturing group pages.",
                "- `wiki/topics/*.md`: future AI-maintained topic synthesis pages.",
                "",
                "## Important PT9L Rules",
                "",
                "- `PT9L_MD` mirrors the original `PT9L` Word file structure.",
                "- `.doc` and `.docx` share the same content-completeness checks; `.doc` has an extra initial conversion risk.",
                "- Evidence includes text, tables, images, icons, checkboxes, OLE/Excel objects, signatures, and visual formatting.",
                "- Risk matrices may encode meaning through Word highlight such as `Range.HighlightColorIndex=1`.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_readme(rows: list[dict[str, Any]]) -> None:
    counts = Counter(row["source_type"] for row in rows)
    risks = Counter(row["loss_risk_level"] for row in rows)
    lines = [
        "# PT9L LLM Wiki",
        "",
        "This wiki compiles converted PT9L Word evidence into a structured markdown knowledge base for LLM use.",
        "",
        "It follows the LLM Wiki pattern:",
        "",
        "- `sources/`: converted source Markdown copied from `PT9L_MD`.",
        "- `wiki/`: AI-maintained navigation and synthesis pages.",
        "- `manifests/`: CSV/JSON catalogs for traceability.",
        "- `AGENTS.md`: rules for future AI agents maintaining the wiki.",
        "",
        "## Current Coverage",
        "",
        f"- generated_at: {now()}",
        f"- source_files: {len(rows)}",
        f"- doc: {counts.get('doc', 0)}",
        f"- docx: {counts.get('docx', 0)}",
        f"- high_risk_conversion_gaps: {risks.get('high', 0)}",
        f"- medium_risk_conversion_gaps: {risks.get('medium', 0)}",
        f"- low_risk_files: {risks.get('low', 0)}",
        "",
        "Start here: [`wiki/index.md`](wiki/index.md).",
        "",
    ]
    (WIKI_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(rows: list[dict[str, Any]]) -> None:
    stage_counts = Counter(row["stage"] for row in rows)
    risks = Counter(row["loss_risk_level"] for row in rows)
    lines = [
        "# PT9L Wiki Index",
        "",
        "This is the main entry point for AI and human review.",
        "",
        "## Coverage",
        "",
        f"- converted Word sources: {len(rows)}",
        f"- high risk conversion gaps: {risks.get('high', 0)}",
        f"- medium risk conversion gaps: {risks.get('medium', 0)}",
        f"- low risk files: {risks.get('low', 0)}",
        "",
        "## Core Pages",
        "",
        "- [Source Catalog](source_catalog.md)",
        "- [High Risk Conversion Gaps](high_risk_conversion_gaps.md)",
        "- [Conversion Data Format](../DATA_FORMAT.md)",
        "- [Agent Rules](../AGENTS.md)",
        "",
        "## Stage Pages",
        "",
    ]
    for stage, count in sorted(stage_counts.items()):
        filename = f"stages/{safe_part(stage)}.md"
        lines.append(f"- [{stage}]({filename}) - {count} source files")
    lines.extend(["", "## Query Rule", "", "Read this page first, then open the relevant stage/source page. For evidence-critical answers, inspect linked source markdown and assets."])
    (WIKI_DIR / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_source_catalog(rows: list[dict[str, Any]]) -> None:
    table = [["ID", "Stage", "Source", "Risk", "Images", "Visual", "Markdown"]]
    for row in rows:
        table.append(
            [
                row["wiki_id"],
                row["stage"],
                Path(row["source_relative_path"]).name,
                row["loss_risk_level"],
                row["image_count"],
                row["visual_format_count"],
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = ["# Source Catalog", "", "All converted Word markdown sources included in this LLM Wiki.", ""]
    lines.extend(md_table(table))
    (WIKI_DIR / "source_catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_high_risk(rows: list[dict[str, Any]]) -> None:
    risky = [row for row in rows if row["loss_risk_level"] in {"high", "medium"}]
    table = [["ID", "Risk", "Reasons", "Source", "Assets", "Markdown"]]
    for row in risky:
        table.append(
            [
                row["wiki_id"],
                row["loss_risk_level"],
                row["risk_reasons"],
                row["source_relative_path"],
                row["assets_dir"],
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [
        "# High Risk Conversion Gaps",
        "",
        "Files listed here are readable but not fully AI-ready until the flagged conversion risks are reviewed.",
        "",
    ]
    lines.extend(md_table(table))
    (WIKI_DIR / "high_risk_conversion_gaps.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_stage_pages(rows: list[dict[str, Any]]) -> None:
    by_stage: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_stage[row["stage"]].append(row)
    stage_dir = WIKI_DIR / "stages"
    stage_dir.mkdir(parents=True, exist_ok=True)
    for stage, items in sorted(by_stage.items()):
        risks = Counter(row["loss_risk_level"] for row in items)
        table = [["ID", "File", "Type", "Risk", "Reasons", "Source"]]
        for row in items:
            table.append(
                [
                    row["wiki_id"],
                    Path(row["source_relative_path"]).name,
                    row["source_type"],
                    row["loss_risk_level"],
                    row["risk_reasons"],
                    f"[source](../../{row['wiki_source_rel']})",
                ]
            )
        lines = [
            f"# {stage}",
            "",
            f"- source_files: {len(items)}",
            f"- high: {risks.get('high', 0)}",
            f"- medium: {risks.get('medium', 0)}",
            f"- low: {risks.get('low', 0)}",
            "",
        ]
        lines.extend(md_table(table))
        (stage_dir / f"{safe_part(stage)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_llms_txt(rows: list[dict[str, Any]]) -> None:
    lines = [
        "# PT9L LLM Wiki",
        "",
        "PT9L DHF/DMR Word evidence compiled into a local LLM Wiki.",
        "",
        "## Main Entry Points",
        "",
        "- llm_wiki/wiki/index.md",
        "- llm_wiki/wiki/source_catalog.md",
        "- llm_wiki/wiki/high_risk_conversion_gaps.md",
        "- llm_wiki/AGENTS.md",
        "- DATA_FORMAT.md",
        "",
        "## Source Markdown",
        "",
    ]
    for row in rows:
        lines.append(f"- {row['wiki_source_rel']} - {row['source_relative_path']} [{row['loss_risk_level']}]")
    (WIKI_ROOT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    full_lines = list(lines)
    full_lines.extend(["", "## Full Wiki Pages", ""])
    for path in sorted(WIKI_DIR.rglob("*.md")):
        full_lines.extend(["", f"--- {path.relative_to(WIKI_ROOT).as_posix()} ---", "", path.read_text(encoding="utf-8", errors="ignore")])
    (WIKI_ROOT / "llms-full.txt").write_text("\n".join(full_lines) + "\n", encoding="utf-8")


def write_manifest_files(rows: list[dict[str, Any]]) -> None:
    fields = [
        "wiki_id",
        "stage",
        "source_file",
        "source_relative_path",
        "source_type",
        "output_markdown",
        "assets_dir",
        "wiki_source_path",
        "wiki_source_rel",
        "conversion_status",
        "loss_risk_level",
        "risk_reasons",
        "image_count",
        "visual_format_count",
        "manual_review_required",
    ]
    write_csv(MANIFESTS_DIR / "source_catalog.csv", rows, fields)
    write_json(MANIFESTS_DIR / "source_catalog.json", rows)


def main() -> int:
    if not MANIFEST.exists():
        raise SystemExit(f"missing manifest: {MANIFEST}")
    if WIKI_ROOT.exists():
        shutil.rmtree(WIKI_ROOT)
    WIKI_ROOT.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "topics").mkdir(parents=True, exist_ok=True)

    rows = read_manifest()
    records = copy_sources(rows)
    write_manifest_files(records)
    write_agents()
    write_readme(records)
    write_index(records)
    write_source_catalog(records)
    write_high_risk(records)
    write_stage_pages(records)
    write_llms_txt(records)
    print(f"llm_wiki={WIKI_ROOT}")
    print(f"sources={len(records)}")
    print(f"index={WIKI_DIR / 'index.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
