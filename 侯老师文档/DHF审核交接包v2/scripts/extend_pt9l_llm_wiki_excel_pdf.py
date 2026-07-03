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
WIKI_ROOT = PT9L_MD / "llm_wiki"
WIKI_DIR = WIKI_ROOT / "wiki"
SOURCES_ROOT = WIKI_ROOT / "sources"
MANIFESTS_DIR = WIKI_ROOT / "manifests"
PT9L_MANIFESTS = PT9L_MD / "_manifests"

WORD_CATALOG = MANIFESTS_DIR / "source_catalog.csv"
EXCEL_MANIFEST = PT9L_MANIFESTS / "excel_conversion_manifest.csv"
PDF_MANIFEST = PT9L_MANIFESTS / "pdf_conversion_manifest.csv"


def now() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat(sep=" ")


def safe_part(text: str, max_len: int = 100) -> str:
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", text)
    text = re.sub(r"\s+", "_", text).strip("._ ")
    return (text or "unnamed")[:max_len]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = []
        for row in rows:
            for key in row.keys():
                if key not in fields:
                    fields.append(key)
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
    lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * len(rows[0])) + " |"]
    for row in rows[1:]:
        escaped = [str(cell).replace("\n", " ").replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(escaped) + " |")
    return lines


def wiki_link(path: Path, base: Path = WIKI_ROOT) -> str:
    return path.relative_to(base).as_posix()


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
    if parts[0].startswith("04_User_Manual"):
        return "User Manual"
    if "DMR" in rel.upper():
        return "DMR"
    return parts[0]


def source_copy_path(row: dict[str, str], modality: str) -> Path:
    rel = row["source_relative_path"].replace("\\", "/")
    parent_parts = rel.split("/")[:-1]
    parent = Path(*parent_parts) if parent_parts else Path()
    stem = safe_part(Path(row["markdown_path"]).stem)
    return SOURCES_ROOT / modality / parent / f"{stem}.source.md"


def normalize_excel_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, 1):
        src = Path(row["markdown_path"])
        dst = source_copy_path(row, "excel")
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        record = {
            "wiki_id": f"PT9L-EXCEL-{idx:04d}",
            "modality": "excel",
            "stage": stage_from_rel(row["source_relative_path"]),
            "source_relative_path": row["source_relative_path"],
            "source_type": Path(row["source_relative_path"]).suffix.lower().lstrip("."),
            "output_markdown": row["markdown_path"],
            "assets_dir": row["assets_dir"],
            "wiki_source_path": str(dst),
            "wiki_source_rel": wiki_link(dst),
            "conversion_status": row.get("status", ""),
            "loss_risk_level": row.get("loss_risk", ""),
            "risk_reasons": row.get("risk_reasons", ""),
            "page_count": "",
            "sheet_count": row.get("sheet_count", ""),
            "semantic_finding_count": row.get("semantic_finding_count", ""),
            "visual_evidence_count": row.get("page_visual_count", ""),
            "image_count": row.get("image_count", ""),
            "manual_review_required": "yes" if row.get("loss_risk") in {"high", "medium", "blocked"} else "no",
        }
        records.append(record)
    return records


def normalize_pdf_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for idx, row in enumerate(rows, 1):
        src = Path(row["markdown_path"])
        dst = source_copy_path(row, "pdf")
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        record = {
            "wiki_id": f"PT9L-PDF-{idx:04d}",
            "modality": "pdf",
            "stage": stage_from_rel(row["source_relative_path"]),
            "source_relative_path": row["source_relative_path"],
            "source_type": "pdf",
            "pdf_type": row.get("pdf_type", ""),
            "output_markdown": row["markdown_path"],
            "assets_dir": row["assets_dir"],
            "wiki_source_path": str(dst),
            "wiki_source_rel": wiki_link(dst),
            "conversion_status": row.get("status", ""),
            "loss_risk_level": row.get("loss_risk", ""),
            "risk_reasons": row.get("risk_reasons", ""),
            "page_count": row.get("page_count", ""),
            "sheet_count": "",
            "semantic_finding_count": row.get("semantic_finding_count", ""),
            "visual_evidence_count": row.get("visual_evidence_count", ""),
            "image_count": row.get("embedded_image_count", ""),
            "manual_review_required": "yes" if row.get("loss_risk") in {"high", "medium", "blocked"} else "no",
        }
        records.append(record)
    return records


def read_word_rows() -> list[dict[str, Any]]:
    rows = read_csv(WORD_CATALOG)
    for row in rows:
        row["modality"] = "word"
        row.setdefault("page_count", "")
        row.setdefault("sheet_count", "")
        row.setdefault("semantic_finding_count", "")
        row.setdefault("visual_evidence_count", row.get("visual_format_count", ""))
    return rows


def write_catalog_page(path: Path, title: str, rows: list[dict[str, Any]], modality: str) -> None:
    table = [["ID", "Stage", "File", "Type", "Risk", "Key Counts", "Source"]]
    for row in rows:
        counts = []
        if row.get("sheet_count"):
            counts.append(f"sheets={row['sheet_count']}")
        if row.get("page_count"):
            counts.append(f"pages={row['page_count']}")
        if row.get("semantic_finding_count"):
            counts.append(f"semantic={row['semantic_finding_count']}")
        if row.get("visual_evidence_count"):
            counts.append(f"visual={row['visual_evidence_count']}")
        table.append(
            [
                row["wiki_id"],
                row["stage"],
                Path(row["source_relative_path"]).name,
                row.get("pdf_type") or row.get("source_type", modality),
                row.get("loss_risk_level", ""),
                "; ".join(counts),
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [f"# {title}", "", f"- source_files: {len(rows)}", ""]
    lines.extend(md_table(table))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_modality_coverage(all_rows: list[dict[str, Any]]) -> None:
    by_modality = Counter(row["modality"] for row in all_rows)
    by_risk = Counter((row["modality"], row.get("loss_risk_level", "")) for row in all_rows)
    table = [["Modality", "Sources", "High", "Medium", "Low", "Blocked"]]
    for modality in ["word", "excel", "pdf"]:
        table.append(
            [
                modality,
                str(by_modality.get(modality, 0)),
                str(by_risk.get((modality, "high"), 0)),
                str(by_risk.get((modality, "medium"), 0)),
                str(by_risk.get((modality, "low"), 0)),
                str(by_risk.get((modality, "blocked"), 0)),
            ]
        )
    lines = [
        "# Modality Coverage",
        "",
        f"- generated_at: {now()}",
        f"- total_sources: {len(all_rows)}",
        "",
    ]
    lines.extend(md_table(table))
    lines.extend(
        [
            "",
            "## Evidence Rule",
            "",
            "For Excel and PDF sources, use the copied source Markdown for navigation, then inspect the original `.assets` directory for page images, OCR, layout manifests, sheet/page manifests, and conversion loss details.",
            "",
        ]
    )
    (WIKI_DIR / "modality_coverage.md").write_text("\n".join(lines), encoding="utf-8")


def write_excel_pdf_high_risk(rows: list[dict[str, Any]]) -> None:
    risky = [row for row in rows if row.get("loss_risk_level") in {"high", "medium", "blocked"}]
    table = [["ID", "Modality", "Risk", "Source", "Reasons", "Assets", "Markdown"]]
    for row in risky:
        table.append(
            [
                row["wiki_id"],
                row["modality"],
                row.get("loss_risk_level", ""),
                row["source_relative_path"],
                row.get("risk_reasons", ""),
                row.get("assets_dir", ""),
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [
        "# Excel/PDF High Risk Conversion Gaps",
        "",
        "These files are converted and searchable, but the source evidence requires visual/layout/OCR review before formal claims.",
        "",
    ]
    lines.extend(md_table(table))
    (WIKI_DIR / "excel_pdf_high_risk_conversion_gaps.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_stage_modality_pages(all_rows: list[dict[str, Any]]) -> None:
    by_stage: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in all_rows:
        by_stage[row["stage"]].append(row)
    stage_dir = WIKI_DIR / "stages_all"
    stage_dir.mkdir(parents=True, exist_ok=True)
    for stage, items in sorted(by_stage.items()):
        counts = Counter(row["modality"] for row in items)
        table = [["ID", "Modality", "File", "Type", "Risk", "Source"]]
        for row in items:
            table.append(
                [
                    row["wiki_id"],
                    row["modality"],
                    Path(row["source_relative_path"]).name,
                    row.get("pdf_type") or row.get("source_type", ""),
                    row.get("loss_risk_level", ""),
                    f"[source](../../{row['wiki_source_rel']})",
                ]
            )
        lines = [
            f"# {stage} - All Modalities",
            "",
            f"- total_sources: {len(items)}",
            f"- word: {counts.get('word', 0)}",
            f"- excel: {counts.get('excel', 0)}",
            f"- pdf: {counts.get('pdf', 0)}",
            "",
        ]
        lines.extend(md_table(table))
        (stage_dir / f"{safe_part(stage)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(all_rows: list[dict[str, Any]]) -> None:
    modality_counts = Counter(row["modality"] for row in all_rows)
    risk_counts = Counter(row.get("loss_risk_level", "") for row in all_rows)
    stage_counts = Counter(row["stage"] for row in all_rows)
    lines = [
        "# PT9L Wiki Index",
        "",
        "This is the main entry point for AI and human review across Word, Excel, and PDF evidence.",
        "",
        "## Coverage",
        "",
        f"- total converted sources: {len(all_rows)}",
        f"- Word sources: {modality_counts.get('word', 0)}",
        f"- Excel sources: {modality_counts.get('excel', 0)}",
        f"- PDF sources: {modality_counts.get('pdf', 0)}",
        f"- high risk conversion gaps: {risk_counts.get('high', 0)}",
        f"- medium risk conversion gaps: {risk_counts.get('medium', 0)}",
        f"- low risk files: {risk_counts.get('low', 0)}",
        f"- blocked files: {risk_counts.get('blocked', 0)}",
        "",
        "## Core Pages",
        "",
        "- [All Source Catalog](all_source_catalog.md)",
        "- [Word Source Catalog](source_catalog.md)",
        "- [Excel Source Catalog](excel_source_catalog.md)",
        "- [PDF Source Catalog](pdf_source_catalog.md)",
        "- [Modality Coverage](modality_coverage.md)",
        "- [Word High Risk Conversion Gaps](high_risk_conversion_gaps.md)",
        "- [Excel/PDF High Risk Conversion Gaps](excel_pdf_high_risk_conversion_gaps.md)",
        "- [Conversion Data Format](../DATA_FORMAT.md)",
        "- [Agent Rules](../AGENTS.md)",
        "",
        "## Stage Pages - All Modalities",
        "",
    ]
    for stage, count in sorted(stage_counts.items()):
        lines.append(f"- [{stage}](stages_all/{safe_part(stage)}.md) - {count} source files")
    lines.extend(
        [
            "",
            "## Query Rule",
            "",
            "Read this page first, then open the relevant modality catalog or stage page. For evidence-critical answers, inspect linked source markdown and the original assets directory from the manifest.",
            "",
        ]
    )
    (WIKI_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_readme(all_rows: list[dict[str, Any]]) -> None:
    modality_counts = Counter(row["modality"] for row in all_rows)
    lines = [
        "# PT9L LLM Wiki",
        "",
        "This wiki compiles converted PT9L DHF/DMR evidence into a structured markdown knowledge base for LLM use.",
        "",
        "## Current Coverage",
        "",
        f"- generated_at: {now()}",
        f"- total_sources: {len(all_rows)}",
        f"- word: {modality_counts.get('word', 0)}",
        f"- excel: {modality_counts.get('excel', 0)}",
        f"- pdf: {modality_counts.get('pdf', 0)}",
        "",
        "Start here: [`wiki/index.md`](wiki/index.md).",
        "",
    ]
    (WIKI_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_agents() -> None:
    path = WIKI_ROOT / "AGENTS.md"
    text = path.read_text(encoding="utf-8") if path.exists() else "# PT9L LLM Wiki Agent Rules\n"
    marker = "## Excel/PDF Extension Rules"
    if marker not in text:
        text = text.rstrip() + "\n\n" + "\n".join(
            [
                marker,
                "",
                "- Excel sources live under `sources/excel/`; PDF sources live under `sources/pdf/`.",
                "- Use `wiki/excel_source_catalog.md` and `wiki/pdf_source_catalog.md` for modality-specific navigation.",
                "- Excel Markdown is not sufficient by itself; inspect `page_manifest.csv`, sheet CSV/MD files, text objects, semantic findings, and sheet page PNG/PDF evidence in the original `.assets` directory.",
                "- PDF Markdown is not sufficient by itself; inspect `pages_png/`, `pages_text/`, `pages_ocr/`, `pages_layout/`, `pages_ordered_md/`, and conversion loss manifests in the original `.assets` directory.",
                "- `wiki/all_source_catalog.md` and `wiki/stages_all/` are the preferred entry points when the question may span Word, Excel, and PDF evidence.",
                "",
            ]
        )
    path.write_text(text, encoding="utf-8")


def write_llms(all_rows: list[dict[str, Any]]) -> None:
    lines = [
        "# PT9L LLM Wiki",
        "",
        "PT9L DHF/DMR Word, Excel, and PDF evidence compiled into a local LLM Wiki.",
        "",
        "## Main Entry Points",
        "",
        "- llm_wiki/wiki/index.md",
        "- llm_wiki/wiki/all_source_catalog.md",
        "- llm_wiki/wiki/excel_source_catalog.md",
        "- llm_wiki/wiki/pdf_source_catalog.md",
        "- llm_wiki/wiki/modality_coverage.md",
        "- llm_wiki/AGENTS.md",
        "- DATA_FORMAT.md",
        "",
        "## Source Markdown",
        "",
    ]
    for row in all_rows:
        lines.append(f"- {row['wiki_source_rel']} - {row['source_relative_path']} [{row.get('loss_risk_level', '')}]")
    (WIKI_ROOT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    full_lines = list(lines)
    full_lines.extend(["", "## Full Wiki Pages", ""])
    for path in sorted(WIKI_DIR.rglob("*.md")):
        full_lines.extend(["", f"--- {path.relative_to(WIKI_ROOT).as_posix()} ---", "", path.read_text(encoding="utf-8", errors="ignore")])
    (WIKI_ROOT / "llms-full.txt").write_text("\n".join(full_lines) + "\n", encoding="utf-8")


def main() -> int:
    if not WIKI_ROOT.exists():
        raise SystemExit(f"missing existing word wiki: {WIKI_ROOT}")
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)

    word_rows = read_word_rows()
    excel_rows = normalize_excel_rows(read_csv(EXCEL_MANIFEST))
    pdf_rows = normalize_pdf_rows(read_csv(PDF_MANIFEST))
    excel_pdf_rows = excel_rows + pdf_rows
    all_rows = word_rows + excel_pdf_rows

    common_fields = [
        "wiki_id",
        "modality",
        "stage",
        "source_relative_path",
        "source_type",
        "pdf_type",
        "output_markdown",
        "assets_dir",
        "wiki_source_path",
        "wiki_source_rel",
        "conversion_status",
        "loss_risk_level",
        "risk_reasons",
        "page_count",
        "sheet_count",
        "semantic_finding_count",
        "visual_evidence_count",
        "image_count",
        "manual_review_required",
    ]
    write_csv(MANIFESTS_DIR / "excel_source_catalog.csv", excel_rows, common_fields)
    write_csv(MANIFESTS_DIR / "pdf_source_catalog.csv", pdf_rows, common_fields)
    write_csv(MANIFESTS_DIR / "all_source_catalog.csv", all_rows, common_fields)
    write_json(MANIFESTS_DIR / "all_source_catalog.json", all_rows)

    write_catalog_page(WIKI_DIR / "excel_source_catalog.md", "Excel Source Catalog", excel_rows, "excel")
    write_catalog_page(WIKI_DIR / "pdf_source_catalog.md", "PDF Source Catalog", pdf_rows, "pdf")
    write_catalog_page(WIKI_DIR / "all_source_catalog.md", "All Source Catalog", all_rows, "all")
    write_excel_pdf_high_risk(excel_pdf_rows)
    write_modality_coverage(all_rows)
    write_stage_modality_pages(all_rows)
    write_index(all_rows)
    write_readme(all_rows)
    write_agents()
    write_llms(all_rows)

    print(f"llm_wiki={WIKI_ROOT}")
    print(f"word={len(word_rows)}")
    print(f"excel={len(excel_rows)}")
    print(f"pdf={len(pdf_rows)}")
    print(f"all={len(all_rows)}")
    print(f"index={WIKI_DIR / 'index.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
