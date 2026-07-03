# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_CSV = ROOT / "ai_readiness_report.csv"
OUT_MD = ROOT / "ai_readiness_summary.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm_path(value: str) -> str:
    try:
        return str(Path(value).resolve()).lower()
    except Exception:
        return value.lower()


def yes(value: str) -> bool:
    return str(value).strip().lower() in {"yes", "true", "1", "y"}


def status_from_inputs(
    conv: dict[str, str],
    quality: dict[str, str] | None,
    doc_extra: dict[str, str] | None,
    word_recovery: dict[str, str] | None,
    loss_risk: dict[str, str] | None,
    image_counts: dict[str, int],
    image_manual_counts: dict[str, int],
) -> tuple[str, str, str]:
    ext = conv.get("file_extension", "").lower()
    conversion_status = conv.get("conversion_status", "").lower()
    md_path = conv.get("output_md_path", "") or conv.get("markdown_path", "")
    issues: list[str] = []
    evidence: list[str] = []

    if md_path:
        evidence.append("markdown")
    if doc_extra:
        evidence.append("legacy_doc_table_recovery")
    word_recovered = bool(word_recovery and word_recovery.get("conversion_status", "").lower() == "success")
    if word_recovered:
        evidence.append("markitdown_word_recovery")
    if loss_risk:
        evidence.append("conversion_loss_risk_checked")
    if image_counts.get(norm_path(conv.get("original_file_path", "")), 0):
        evidence.append("excel_image_evidence")

    doc_recovered = bool(doc_extra and doc_extra.get("conversion_status", "").lower() == "success")
    if ("failed" in conversion_status or "error" in conversion_status) and not doc_recovered and not word_recovered:
        issues.append("conversion_failed")
    if not md_path and ext not in {"zip", "rar", "7z", "dwg", "dxf", "stp", "step", "igs", "iges"}:
        issues.append("no_markdown_output")
    if quality:
        for key in [
            "manual_review_required",
            "suspected_empty_file",
            "suspected_garbled_text",
            "suspected_incomplete_table",
            "suspected_ocr_error",
            "suspected_missing_key_info",
        ]:
            if yes(quality.get(key, "")):
                issues.append(key)
        if quality.get("quality_level", "").lower() == "failed":
            issues.append("quality_failed")
    if ext in {"xls", "xlsx"}:
        count = image_counts.get(norm_path(conv.get("original_file_path", "")), 0)
        manual = image_manual_counts.get(norm_path(conv.get("original_file_path", "")), 0)
        if count:
            issues.append(f"excel_images_extracted:{count}")
            if manual:
                issues.append(f"excel_images_need_review:{manual}")
        else:
            evidence.append("excel_no_embedded_images_detected")
    if ext == "doc" and doc_extra:
        try:
            embedded_objects = int(doc_extra.get("embedded_object_count", "0") or "0")
        except ValueError:
            embedded_objects = 0
        if embedded_objects:
            issues.append("legacy_doc_embedded_object")
        if yes(doc_extra.get("manual_review_required", "")):
            issues.append("legacy_doc_manual_review")
    if word_recovered:
        issues.append("markitdown_word_manual_review")
    if loss_risk:
        level = loss_risk.get("loss_risk_level", "")
        if level == "high":
            issues.append("conversion_loss_high_risk")
        elif level == "medium":
            issues.append("conversion_loss_medium_risk")
    if ext in {"zip", "rar", "7z"}:
        issues.append("archive_needs_unpacking_or_manifest")
    if ext in {"dwg", "dxf", "stp", "step", "igs", "iges"}:
        issues.append("engineering_native_file_needs_special_parser")

    if "conversion_failed" in issues:
        return "blocked", "; ".join(evidence), "; ".join(issues)
    serious = {"no_markdown_output", "source_missing"}
    if serious.intersection(issues):
        return "metadata_only", "; ".join(evidence), "; ".join(issues)
    if any(
        issue.startswith(("excel_images_need_review", "legacy_doc", "archive_", "engineering_", "suspected_ocr", "conversion_loss_"))
        or issue in {"manual_review_required", "suspected_garbled_text", "suspected_incomplete_table", "suspected_missing_key_info", "quality_failed"}
        for issue in issues
    ):
        return "partial", "; ".join(evidence), "; ".join(issues)
    if md_path or evidence:
        return "ai_ready", "; ".join(evidence), "; ".join(issues)
    return "metadata_only", "; ".join(evidence), "no_extracted_evidence"


def main() -> None:
    conversions = read_csv(ROOT / "conversion_report.csv")
    quality_rows = read_csv(ROOT / "conversion_quality_report.csv")
    doc_rows = read_csv(ROOT / "doc_table_extraction_report.csv")
    word_recovery_rows = read_csv(ROOT / "markitdown_word_recovery_report.csv")
    loss_risk_rows = read_csv(ROOT / "conversion_loss_risk_report.csv")
    image_rows = read_csv(ROOT / "excel_image_evidence" / "image_evidence_index.csv")

    quality_by_path = {
        norm_path(row.get("original_file_path", "") or row.get("source_file", "")): row
        for row in quality_rows
    }
    doc_by_path = {
        norm_path(row.get("original_file_path", "") or row.get("source_file", "") or row.get("doc_file", "")): row
        for row in doc_rows
    }
    word_recovery_by_path = {
        norm_path(row.get("original_file_path", "")): row
        for row in word_recovery_rows
        if row.get("conversion_status", "").lower() == "success"
    }
    loss_risk_by_path = {
        norm_path(row.get("original_file_path", "")): row
        for row in loss_risk_rows
        if row.get("loss_risk_level") in {"high", "medium", "low"}
    }
    image_counts: dict[str, int] = defaultdict(int)
    image_manual_counts: dict[str, int] = defaultdict(int)
    for row in image_rows:
        source = norm_path(row.get("excel_file", ""))
        if row.get("image_path"):
            image_counts[source] += 1
            if yes(row.get("manual_review_required", "")):
                image_manual_counts[source] += 1

    fields = [
        "original_file_path",
        "file_name",
        "file_extension",
        "conversion_status",
        "markdown_path",
        "ai_readiness_level",
        "evidence_available",
        "readiness_gaps",
    ]
    report_rows: list[dict[str, str]] = []
    for conv in conversions:
        key = norm_path(conv.get("original_file_path", ""))
        status, evidence, gaps = status_from_inputs(
            conv,
            quality_by_path.get(key),
            doc_by_path.get(key),
            word_recovery_by_path.get(key),
            loss_risk_by_path.get(key),
            image_counts,
            image_manual_counts,
        )
        report_rows.append({
            "original_file_path": conv.get("original_file_path", ""),
            "file_name": conv.get("original_file_name", "") or conv.get("file_name", "") or Path(conv.get("original_file_path", "")).name,
            "file_extension": conv.get("file_extension", ""),
            "conversion_status": conv.get("conversion_status", ""),
            "markdown_path": conv.get("output_md_path", "") or conv.get("markdown_path", ""),
            "ai_readiness_level": status,
            "evidence_available": evidence,
            "readiness_gaps": gaps,
        })

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(report_rows)

    counts = Counter(row["ai_readiness_level"] for row in report_rows)
    ext_counts = Counter(row["file_extension"].lower() for row in report_rows)
    gap_counts = Counter()
    for row in report_rows:
        for gap in row["readiness_gaps"].split("; "):
            if gap:
                gap_counts[gap.split(":")[0]] += 1

    lines = [
        "# AI Readiness Summary",
        "",
        f"Generated at: {dt.datetime.now().replace(microsecond=0).isoformat(sep=' ')}",
        "",
        "## Overall Readiness",
        "",
    ]
    for level in ["ai_ready", "partial", "metadata_only", "blocked"]:
        lines.append(f"- {level}: {counts.get(level, 0)}")
    lines.extend([
        "",
        "## Main Remaining Gaps",
        "",
    ])
    for gap, count in gap_counts.most_common(20):
        lines.append(f"- {gap}: {count}")
    lines.extend([
        "",
        "## File Type Coverage",
        "",
    ])
    for ext, count in ext_counts.most_common():
        lines.append(f"- {ext or '[none]'}: {count}")
    lines.extend([
        "",
        "## Interpretation",
        "",
        "- `ai_ready` files can enter first-pass DHF/DMR review.",
        "- `partial` files contain useful evidence, but listed blind spots must be reviewed or accepted.",
        "- `metadata_only` files are registered but not substantively readable yet.",
        "- `blocked` files need source recovery, conversion repair, or a special parser.",
        "",
        f"Full detail: `{OUT_CSV.name}`",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"rows={len(report_rows)}")
    for level in ["ai_ready", "partial", "metadata_only", "blocked"]:
        print(f"{level}={counts.get(level, 0)}")
    print(f"summary={OUT_MD}")
    print(f"csv={OUT_CSV}")


if __name__ == "__main__":
    main()
