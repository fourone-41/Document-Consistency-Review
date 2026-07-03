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
ALL_CATALOG = MANIFESTS_DIR / "all_source_catalog.csv"
REMAINING_MANIFEST = PT9L_MANIFESTS / "remaining_source_manifest.csv"


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


def source_copy_path(row: dict[str, str]) -> Path:
    rel = row["source_relative_path"].replace("\\", "/")
    parent_parts = rel.split("/")[:-1]
    parent = Path(*parent_parts) if parent_parts else Path()
    modality = row.get("modality", "remaining")
    stem = safe_part(Path(row["markdown_path"]).stem)
    return SOURCES_ROOT / modality / parent / f"{stem}.source.md"


def wiki_id_prefix(modality: str) -> str:
    return {
        "artwork": "PT9L-ARTWORK",
        "cad": "PT9L-CAD",
        "image": "PT9L-IMAGE",
        "archive": "PT9L-ARCHIVE",
        "ignored": "PT9L-IGNORED",
    }.get(modality, "PT9L-REMAINING")


def normalize_remaining(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    counters: Counter[str] = Counter()
    records: list[dict[str, Any]] = []
    for row in rows:
        modality = row.get("modality", "remaining")
        counters[modality] += 1
        src = Path(row["markdown_path"])
        dst = source_copy_path(row)
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        loss = row.get("loss_risk", "")
        record = {
            "wiki_id": f"{wiki_id_prefix(modality)}-{counters[modality]:04d}",
            "modality": modality,
            "stage": stage_from_rel(row["source_relative_path"]),
            "source_relative_path": row["source_relative_path"],
            "source_type": row.get("source_type", ""),
            "pdf_type": "",
            "output_markdown": row["markdown_path"],
            "assets_dir": row["assets_dir"],
            "wiki_source_path": str(dst),
            "wiki_source_rel": wiki_link(dst),
            "conversion_status": row.get("status", ""),
            "loss_risk_level": loss,
            "risk_reasons": row.get("risk_reasons", ""),
            "page_count": row.get("page_count", ""),
            "sheet_count": "",
            "semantic_finding_count": row.get("semantic_finding_count", ""),
            "visual_evidence_count": row.get("visual_evidence_count", ""),
            "image_count": row.get("image_count", ""),
            "manual_review_required": "yes" if loss in {"high", "medium", "blocked"} else "no",
            "archive_member_count": row.get("archive_member_count", ""),
            "related_pdf_count": row.get("related_pdf_count", ""),
        }
        records.append(record)
    return records


def write_catalog_page(path: Path, title: str, rows: list[dict[str, Any]]) -> None:
    table = [["ID", "Modality", "Stage", "File", "Type", "Status", "Risk", "Key Counts", "Source"]]
    for row in rows:
        counts = []
        if row.get("page_count"):
            counts.append(f"pages={row['page_count']}")
        if row.get("archive_member_count"):
            counts.append(f"members={row['archive_member_count']}")
        if row.get("semantic_finding_count"):
            counts.append(f"semantic={row['semantic_finding_count']}")
        if row.get("visual_evidence_count"):
            counts.append(f"visual={row['visual_evidence_count']}")
        if row.get("related_pdf_count"):
            counts.append(f"related_pdf={row['related_pdf_count']}")
        table.append(
            [
                row["wiki_id"],
                row["modality"],
                row["stage"],
                Path(row["source_relative_path"]).name,
                row.get("source_type", ""),
                row.get("conversion_status", ""),
                row.get("loss_risk_level", ""),
                "; ".join(counts),
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [f"# {title}", "", f"- source_files: {len(rows)}", ""]
    lines.extend(md_table(table))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_ignored_page(rows: list[dict[str, Any]]) -> None:
    ignored = [row for row in rows if row["modality"] == "ignored"]
    table = [["ID", "Source", "Type", "Reason", "Source"]]
    for row in ignored:
        table.append(
            [
                row["wiki_id"],
                row["source_relative_path"],
                row.get("source_type", ""),
                row.get("risk_reasons", ""),
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [
        "# Ignored Files",
        "",
        "These files were registered but not converted because they are version-control or temporary files, not formal DHF/DMR evidence.",
        "",
    ]
    lines.extend(md_table(table))
    (WIKI_DIR / "ignored_files.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_remaining_high_risk(rows: list[dict[str, Any]]) -> None:
    risky = [row for row in rows if row.get("loss_risk_level") in {"high", "medium", "blocked"}]
    table = [["ID", "Modality", "Risk", "Status", "Source", "Reasons", "Assets", "Markdown"]]
    for row in risky:
        table.append(
            [
                row["wiki_id"],
                row["modality"],
                row.get("loss_risk_level", ""),
                row.get("conversion_status", ""),
                row["source_relative_path"],
                row.get("risk_reasons", ""),
                row.get("assets_dir", ""),
                f"[source](../{row['wiki_source_rel']})",
            ]
        )
    lines = [
        "# Remaining Format Conversion Gaps",
        "",
        "These remaining-format sources are searchable or registered, but require visual/tool review before formal claims.",
        "",
    ]
    lines.extend(md_table(table))
    (WIKI_DIR / "remaining_high_risk_conversion_gaps.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_stage_pages(all_rows: list[dict[str, Any]]) -> None:
    by_stage: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in all_rows:
        by_stage[row["stage"]].append(row)
    stage_dir = WIKI_DIR / "stages_all"
    stage_dir.mkdir(parents=True, exist_ok=True)
    for stage, items in sorted(by_stage.items()):
        counts = Counter(row["modality"] for row in items)
        table = [["ID", "Modality", "File", "Type", "Status", "Risk", "Source"]]
        for row in items:
            table.append(
                [
                    row["wiki_id"],
                    row["modality"],
                    Path(row["source_relative_path"]).name,
                    row.get("pdf_type") or row.get("source_type", ""),
                    row.get("conversion_status", ""),
                    row.get("loss_risk_level", ""),
                    f"[source](../../{row['wiki_source_rel']})",
                ]
            )
        lines = [
            f"# {stage} - All Modalities",
            "",
            f"- total_sources: {len(items)}",
        ]
        for modality, count in sorted(counts.items()):
            lines.append(f"- {modality}: {count}")
        lines.append("")
        lines.extend(md_table(table))
        (stage_dir / f"{safe_part(stage)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_modality_coverage(all_rows: list[dict[str, Any]]) -> None:
    by_modality = Counter(row["modality"] for row in all_rows)
    by_risk = Counter((row["modality"], row.get("loss_risk_level", "")) for row in all_rows)
    table = [["Modality", "Sources", "High", "Medium", "Low", "Blocked", "Ignored"]]
    for modality in sorted(by_modality):
        table.append(
            [
                modality,
                str(by_modality.get(modality, 0)),
                str(by_risk.get((modality, "high"), 0)),
                str(by_risk.get((modality, "medium"), 0)),
                str(by_risk.get((modality, "low"), 0)),
                str(by_risk.get((modality, "blocked"), 0)),
                str(by_risk.get((modality, "ignored"), 0)),
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
            "Use copied source Markdown for navigation. For evidence-critical answers, inspect the original `.assets` directory listed in the catalogs.",
            "",
        ]
    )
    (WIKI_DIR / "modality_coverage.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(all_rows: list[dict[str, Any]]) -> None:
    modality_counts = Counter(row["modality"] for row in all_rows)
    risk_counts = Counter(row.get("loss_risk_level", "") for row in all_rows)
    stage_counts = Counter(row["stage"] for row in all_rows)
    lines = [
        "# PT9L Wiki Index",
        "",
        "This is the main entry point for AI and human review across Word, Excel, PDF, artwork, CAD, image, archive, and ignored evidence records.",
        "",
        "## Coverage",
        "",
        f"- total converted/registered sources: {len(all_rows)}",
    ]
    for modality, count in sorted(modality_counts.items()):
        lines.append(f"- {modality} sources: {count}")
    lines.extend(
        [
            f"- high risk conversion gaps: {risk_counts.get('high', 0)}",
            f"- medium risk conversion gaps: {risk_counts.get('medium', 0)}",
            f"- low risk files: {risk_counts.get('low', 0)}",
            f"- blocked files: {risk_counts.get('blocked', 0)}",
            f"- ignored files: {risk_counts.get('ignored', 0)}",
            "",
            "## Core Pages",
            "",
            "- [All Source Catalog](all_source_catalog.md)",
            "- [Word Source Catalog](source_catalog.md)",
            "- [Excel Source Catalog](excel_source_catalog.md)",
            "- [PDF Source Catalog](pdf_source_catalog.md)",
            "- [Remaining Source Catalog](remaining_source_catalog.md)",
            "- [Artwork/CAD/Image/Archive Catalog](artwork_cad_image_catalog.md)",
            "- [Ignored Files](ignored_files.md)",
            "- [Modality Coverage](modality_coverage.md)",
            "- [Word High Risk Conversion Gaps](high_risk_conversion_gaps.md)",
            "- [Excel/PDF High Risk Conversion Gaps](excel_pdf_high_risk_conversion_gaps.md)",
            "- [Remaining Format Conversion Gaps](remaining_high_risk_conversion_gaps.md)",
            "- [Conversion Data Format](../DATA_FORMAT.md)",
            "- [Agent Rules](../AGENTS.md)",
            "",
            "## Stage Pages - All Modalities",
            "",
        ]
    )
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
        "This wiki compiles converted and registered PT9L DHF/DMR evidence into a structured markdown knowledge base for LLM use.",
        "",
        "## Current Coverage",
        "",
        f"- generated_at: {now()}",
        f"- total_sources: {len(all_rows)}",
    ]
    for modality, count in sorted(modality_counts.items()):
        lines.append(f"- {modality}: {count}")
    lines.extend(["", "Start here: [`wiki/index.md`](wiki/index.md).", ""])
    (WIKI_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_agents() -> None:
    path = WIKI_ROOT / "AGENTS.md"
    text = path.read_text(encoding="utf-8") if path.exists() else "# PT9L LLM Wiki Agent Rules\n"
    marker = "## Remaining Format Rules"
    if marker not in text:
        text = text.rstrip() + "\n\n" + "\n".join(
            [
                marker,
                "",
                "- Remaining format sources live under `sources/artwork/`, `sources/cad/`, `sources/image/`, `sources/archive/`, and `sources/ignored/`.",
                "- Use `wiki/remaining_source_catalog.md` for all remaining formats.",
                "- Use `wiki/artwork_cad_image_catalog.md` for design-source evidence such as AI, DWG, images, and archives.",
                "- AI artwork may be PDF-compatible and rendered to PNG/OCR, but still requires visual review against original artwork/PDF evidence.",
                "- DWG files require AutoCAD/DWG tooling for native conversion. If unavailable, use related converted PDF evidence and keep DWG as partial/high risk.",
                "- ZIP files are archives. Inspect `archive_manifest.csv` and use existing converted records for internal PDFs/Excel when available.",
                "- `.scc` and `.tmp` are registered as ignored unless the user explicitly says they are formal evidence.",
                "",
            ]
        )
    path.write_text(text, encoding="utf-8")


def write_llms(all_rows: list[dict[str, Any]]) -> None:
    lines = [
        "# PT9L LLM Wiki",
        "",
        "PT9L DHF/DMR Word, Excel, PDF, artwork, CAD, image, archive, and ignored evidence records compiled into a local LLM Wiki.",
        "",
        "## Main Entry Points",
        "",
        "- llm_wiki/wiki/index.md",
        "- llm_wiki/wiki/all_source_catalog.md",
        "- llm_wiki/wiki/remaining_source_catalog.md",
        "- llm_wiki/wiki/artwork_cad_image_catalog.md",
        "- llm_wiki/wiki/ignored_files.md",
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
        raise SystemExit(f"missing wiki root: {WIKI_ROOT}")
    existing = read_csv(ALL_CATALOG)
    existing = [row for row in existing if row.get("modality") not in {"artwork", "cad", "image", "archive", "ignored"}]
    remaining_rows = normalize_remaining(read_csv(REMAINING_MANIFEST))
    all_rows = existing + remaining_rows
    fields = [
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
        "archive_member_count",
        "related_pdf_count",
    ]
    write_csv(MANIFESTS_DIR / "remaining_source_catalog.csv", remaining_rows, fields)
    write_csv(MANIFESTS_DIR / "all_source_catalog.csv", all_rows, fields)
    write_json(MANIFESTS_DIR / "all_source_catalog.json", all_rows)
    write_catalog_page(WIKI_DIR / "remaining_source_catalog.md", "Remaining Source Catalog", remaining_rows)
    write_catalog_page(WIKI_DIR / "artwork_cad_image_catalog.md", "Artwork/CAD/Image/Archive Catalog", [row for row in remaining_rows if row["modality"] != "ignored"])
    write_ignored_page(remaining_rows)
    write_remaining_high_risk(remaining_rows)
    write_stage_pages(all_rows)
    write_modality_coverage(all_rows)
    write_index(all_rows)
    write_readme(all_rows)
    write_agents()
    write_llms(all_rows)
    print(f"llm_wiki={WIKI_ROOT}")
    print(f"remaining={len(remaining_rows)}")
    print(f"all={len(all_rows)}")
    print(f"index={WIKI_DIR / 'index.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
