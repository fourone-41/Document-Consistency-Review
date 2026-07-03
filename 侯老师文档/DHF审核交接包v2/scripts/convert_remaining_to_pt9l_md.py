# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import shutil
import zipfile
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
from PIL import Image
import pytesseract


ROOT = Path(__file__).resolve().parent
MD_ROOT = ROOT.parent / "PT9L_MD"
MANIFEST_DIR = MD_ROOT / "_manifests"
TESSERACT_EXE = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
TESSDATA_DIR = ROOT.parent / "packages" / "tessdata"
SOURCE_ROOTS = [
    ROOT / "02_RnD_DHF",
    ROOT / "03_Mfg_SOP",
    ROOT / "04_User_Manual",
]
TARGET_EXTS = {".ai", ".dwg", ".zip", ".jpg", ".jpeg", ".png", ".scc", ".tmp"}
IGNORED_EXTS = {".scc", ".tmp"}


def now() -> str:
    return dt.datetime.now().replace(microsecond=0).isoformat(sep=" ")


def setup_ocr() -> tuple[bool, str]:
    try:
        if TESSERACT_EXE.exists():
            pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_EXE)
        if TESSDATA_DIR.exists():
            os.environ["TESSDATA_PREFIX"] = str(TESSDATA_DIR)
        version = str(pytesseract.get_tesseract_version())
        languages = set(pytesseract.get_languages(config=""))
        missing = sorted({"chi_sim", "eng", "osd"} - languages)
        if missing:
            return False, f"{version}; missing_languages={missing}"
        return True, f"{version}; languages={sorted(languages)}"
    except Exception as exc:
        return False, str(exc)


def rel_to_root(path: Path) -> Path:
    return path.resolve().relative_to(ROOT.resolve())


def safe_name(text: str, max_len: int = 80) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "_", text).strip(" ._")
    cleaned = re.sub(r"\s+", "_", cleaned)
    return (cleaned or "file")[:max_len]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = []
        for row in rows:
            for key in row.keys():
                if key not in fieldnames:
                    fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_key(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+\(\d+\)$", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", text)
    return text


def existing_pdf_markdown() -> dict[str, dict[str, str]]:
    rows = read_csv(MANIFEST_DIR / "pdf_conversion_manifest.csv")
    by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        key = normalize_key(Path(row.get("source_relative_path", "")).stem)
        if key:
            by_key[key] = row
    return by_key


def existing_excel_markdown() -> dict[str, dict[str, str]]:
    rows = read_csv(MANIFEST_DIR / "excel_conversion_manifest.csv")
    by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        key = normalize_key(Path(row.get("source_relative_path", "")).stem)
        if key:
            by_key[key] = row
    return by_key


def find_related_converted(source: Path, modality: str) -> list[dict[str, str]]:
    manifest = existing_pdf_markdown() if modality == "pdf" else existing_excel_markdown()
    source_key = normalize_key(source.stem)
    results = []
    for key, row in manifest.items():
        if key and source_key and (key == source_key or key in source_key or source_key in key):
            results.append(row)
    return results[:10]


def semantic_findings(page_no: int, text: str, source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    patterns = {
        "document_number": r"(?:No\.|NO\.|\u7f16\u53f7|\u6587\u4ef6\u7f16\u53f7|\u8868\u53f7|\u56fe\u53f7|Drawing No\.?)[:\uff1a\s]*([A-Za-z0-9_.\-/]+)",
        "revision": r"(?:Rev\.?|REV\.?|\u7248\u672c|\u7248\u6b21)[:\uff1a\s]*([A-Za-z0-9_.\-/]+)",
        "date": r"(?:Date|\u65e5\u671f)[:\uff1a\s]*([0-9]{4}[./-][0-9]{1,2}[./-][0-9]{1,2})",
        "standard": r"((?:IEC|ISO|EN|ANSI|ASTM|AAMI|GB|YY)\s*[0-9][A-Za-z0-9\-:./ ]*)",
        "material": r"(?:Material|\u6750\u8d28)[:\uff1a\s]*([A-Za-z0-9_.\-/\u4e00-\u9fff ]+)",
        "pantone_or_color": r"(PANTONE\s*[A-Za-z0-9\- ]+|CMYK\s*[0-9,./% ]+|\u989c\u8272[:\uff1a\s]*[A-Za-z0-9\u4e00-\u9fff\- ]+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text[:10000], flags=re.I)
        if match:
            rows.append(
                {
                    "page": page_no,
                    "finding_type": key,
                    "value": match.group(1) if match.groups() else match.group(0),
                    "evidence": match.group(0),
                    "source": source,
                }
            )
    return rows


def ocr_image(path: Path, ocr_available: bool) -> tuple[str, str]:
    if not ocr_available:
        return "", "needed_but_tesseract_unavailable"
    try:
        text = pytesseract.image_to_string(Image.open(path), lang="chi_sim+eng", timeout=90)
        return text, "done"
    except RuntimeError as exc:
        return f"OCR_TIMEOUT_OR_RUNTIME_ERROR: {exc}", "failed"
    except Exception as exc:
        return f"OCR_FAILED: {exc}", "failed"


def init_output(source: Path) -> tuple[Path, Path, Path]:
    rel = rel_to_root(source)
    md_path = MD_ROOT / rel.with_suffix(".md")
    assets_dir = md_path.with_suffix(".assets")
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    assets_dir.mkdir(parents=True, exist_ok=True)
    source_dir = assets_dir / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, source_dir / source.name)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    return md_path, assets_dir, rel


def convert_ai(source: Path, ocr_available: bool) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    md_path, assets_dir, rel = init_output(source)
    pages_png = assets_dir / "pages_png"
    pages_text = assets_dir / "pages_text"
    pages_ocr = assets_dir / "pages_ocr"
    pages_layout = assets_dir / "pages_layout"
    for directory in [pages_png, pages_text, pages_ocr, pages_layout]:
        directory.mkdir(parents=True, exist_ok=True)
    related_pdf = find_related_converted(source, "pdf")
    page_rows: list[dict[str, Any]] = []
    semantic_rows: list[dict[str, Any]] = []
    visual_rows: list[dict[str, Any]] = []
    metadata: dict[str, Any] = {}
    status = "success"
    risk = "high"
    readiness = "partial"
    reasons = ["artwork_source_requires_visual_review"]
    page_count = 0
    try:
        doc = fitz.open(source)
        page_count = doc.page_count
        metadata = doc.metadata or {}
        for page_index in range(page_count):
            page_no = page_index + 1
            page = doc.load_page(page_index)
            native_text = page.get_text("text") or ""
            (pages_text / f"page_{page_no:03d}.txt").write_text(native_text, encoding="utf-8")
            blocks = page.get_text("blocks") or []
            layout_rows = []
            for order_idx, block in enumerate(blocks, start=1):
                if len(block) < 7:
                    continue
                x0, y0, x1, y1, text, block_no, btype = block[:7]
                if str(text).strip():
                    layout_rows.append(
                        {
                            "page": page_no,
                            "reading_order": order_idx,
                            "block_no": block_no,
                            "block_type": "text" if int(btype) == 0 else "image",
                            "x0": round(float(x0), 2),
                            "y0": round(float(y0), 2),
                            "x1": round(float(x1), 2),
                            "y1": round(float(y1), 2),
                            "text": str(text).strip()[:1000],
                        }
                    )
            write_csv(pages_layout / f"page_{page_no:03d}_layout.csv", layout_rows)
            pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
            png_path = pages_png / f"page_{page_no:03d}.png"
            pix.save(png_path)
            ocr_text, ocr_status = ocr_image(png_path, ocr_available)
            (pages_ocr / f"page_{page_no:03d}.txt").write_text(ocr_text, encoding="utf-8")
            semantic_rows.extend(semantic_findings(page_no, native_text, "native_text"))
            semantic_rows.extend(semantic_findings(page_no, ocr_text, "ocr_text"))
            visual_rows.append(
                {
                    "page": page_no,
                    "evidence_type": "artwork_page",
                    "value": "AI artwork rendered to PNG",
                    "evidence": str(png_path.relative_to(assets_dir)),
                }
            )
            page_rows.append(
                {
                    "page": page_no,
                    "source_type": "ai",
                    "width": round(float(page.rect.width), 2),
                    "height": round(float(page.rect.height), 2),
                    "native_text_chars": len(native_text.strip()),
                    "ocr_status": ocr_status,
                    "image_path": str(png_path.relative_to(assets_dir)),
                    "page_risk": "artwork_visual_review_required",
                }
            )
        doc.close()
    except Exception as exc:
        status = "partial" if related_pdf else "blocked"
        readiness = "partial" if related_pdf else "blocked"
        risk = "high" if related_pdf else "blocked"
        reasons.append(f"ai_render_failed: {exc}")
        if related_pdf:
            reasons.append("related_converted_pdf_available")

    if related_pdf:
        reasons.append("related_converted_pdf_available")
    write_csv(assets_dir / "page_manifest.csv", page_rows)
    write_csv(assets_dir / "visual_evidence_manifest.csv", visual_rows)
    write_csv(assets_dir / "semantic_findings_manifest.csv", semantic_rows)
    related_rows = [
        {
            "related_source_relative_path": row.get("source_relative_path", ""),
            "related_markdown_path": row.get("markdown_path", ""),
            "related_assets_dir": row.get("assets_dir", ""),
            "relationship": "same_or_similar_artwork_pdf",
        }
        for row in related_pdf
    ]
    write_csv(assets_dir / "related_sources_manifest.csv", related_rows)
    loss = {
        "source": str(source),
        "method": "pymupdf_pdf_compatible_ai_render_ocr",
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": list(dict.fromkeys(reasons)),
        "manual_review_required": True,
        "page_count": page_count,
        "related_pdf_count": len(related_pdf),
        "semantic_finding_count": len(semantic_rows),
        "visual_evidence_count": len(visual_rows),
    }
    (assets_dir / "conversion_loss.json").write_text(json.dumps(loss, ensure_ascii=False, indent=2), encoding="utf-8")
    md_lines = [
        "---",
        "remaining_skill_schema: pt9l-md-artwork-v1",
        f"source_file: {source.name}",
        f"source_relative_path: {rel.as_posix()}",
        "source_type: ai",
        f"assets_dir: {assets_dir.name}",
        f"conversion_loss_risk: {risk}",
        f"readiness: {readiness}",
        "manual_review_required: yes",
        f"converted_at: {now()}",
        "---",
        "",
        f"# {source.stem}",
        "",
        "## Summary",
        "",
        f"- source: `{rel.as_posix()}`",
        f"- pages: {page_count}",
        f"- status: {status}",
        f"- related_pdf_count: {len(related_pdf)}",
        f"- risk_reasons: {'; '.join(loss['risk_reasons'])}",
        "",
        "## Evidence Files",
        "",
        f"- [page_manifest.csv]({assets_dir.name}/page_manifest.csv)",
        f"- [pages_png]({assets_dir.name}/pages_png/)",
        f"- [pages_text]({assets_dir.name}/pages_text/)",
        f"- [pages_ocr]({assets_dir.name}/pages_ocr/)",
        f"- [visual_evidence_manifest.csv]({assets_dir.name}/visual_evidence_manifest.csv)",
        f"- [semantic_findings_manifest.csv]({assets_dir.name}/semantic_findings_manifest.csv)",
        f"- [related_sources_manifest.csv]({assets_dir.name}/related_sources_manifest.csv)",
        f"- [conversion_loss.json]({assets_dir.name}/conversion_loss.json)",
        "",
        "## Metadata",
        "",
        "```json",
        json.dumps(metadata, ensure_ascii=False, indent=2),
        "```",
        "",
    ]
    for row in page_rows:
        md_lines.append(f"- Page {row['page']}: [png]({assets_dir.name}/{str(row['image_path']).replace(chr(92), '/')}); ocr={row['ocr_status']}")
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    record = base_record(source, rel, md_path, assets_dir, "artwork", status, risk, readiness, reasons)
    record.update({"page_count": page_count, "semantic_finding_count": len(semantic_rows), "visual_evidence_count": len(visual_rows), "related_pdf_count": len(related_pdf)})
    return record, semantic_rows, visual_rows


def convert_image(source: Path, ocr_available: bool) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    md_path, assets_dir, rel = init_output(source)
    images_dir = assets_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    copied = images_dir / source.name
    shutil.copy2(source, copied)
    review_png = images_dir / f"{safe_name(source.stem)}.review.png"
    try:
        with Image.open(source) as img:
            width, height = img.size
            img.convert("RGB").save(review_png)
    except Exception:
        width = height = 0
        shutil.copy2(source, review_png)
    ocr_text, ocr_status = ocr_image(review_png, ocr_available)
    (assets_dir / "ocr_text.txt").write_text(ocr_text, encoding="utf-8")
    semantic_rows = semantic_findings(1, ocr_text, "ocr_text")
    image_rows = [
        {
            "image_path": str(review_png.relative_to(assets_dir)),
            "source_image": str(copied.relative_to(assets_dir)),
            "width": width,
            "height": height,
            "ocr_status": ocr_status,
            "manual_review_required": "yes",
        }
    ]
    write_csv(assets_dir / "image_manifest.csv", image_rows)
    write_csv(assets_dir / "semantic_findings_manifest.csv", semantic_rows)
    risk = "medium"
    readiness = "partial"
    reasons = ["image_ocr_and_visual_review_required"]
    loss = {
        "source": str(source),
        "method": "image_copy_ocr",
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": reasons,
        "manual_review_required": True,
        "semantic_finding_count": len(semantic_rows),
    }
    (assets_dir / "conversion_loss.json").write_text(json.dumps(loss, ensure_ascii=False, indent=2), encoding="utf-8")
    md_lines = [
        "---",
        "remaining_skill_schema: pt9l-md-image-v1",
        f"source_file: {source.name}",
        f"source_relative_path: {rel.as_posix()}",
        f"source_type: {source.suffix.lower().lstrip('.')}",
        f"assets_dir: {assets_dir.name}",
        f"conversion_loss_risk: {risk}",
        f"readiness: {readiness}",
        "manual_review_required: yes",
        f"converted_at: {now()}",
        "---",
        "",
        f"# {source.stem}",
        "",
        f"![review image]({assets_dir.name}/{str(review_png.relative_to(assets_dir)).replace(chr(92), '/')})",
        "",
        "## Summary",
        "",
        f"- source: `{rel.as_posix()}`",
        f"- size: {width} x {height}",
        f"- ocr_status: {ocr_status}",
        "",
        "## OCR Text",
        "",
        "```text",
        ocr_text[:4000],
        "```",
        "",
    ]
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    record = base_record(source, rel, md_path, assets_dir, "image", "success", risk, readiness, reasons)
    record.update({"semantic_finding_count": len(semantic_rows), "visual_evidence_count": 1, "image_count": 1})
    return record, semantic_rows


def convert_dwg(source: Path) -> dict[str, Any]:
    md_path, assets_dir, rel = init_output(source)
    related_pdf = find_related_converted(source, "pdf")
    status = "blocked"
    risk = "blocked"
    readiness = "blocked"
    reasons = ["dwg_conversion_tool_unavailable", "autocad_or_oda_converter_required"]
    if related_pdf:
        status = "partial"
        risk = "high"
        readiness = "partial"
        reasons.append("related_converted_pdf_available")
    related_rows = [
        {
            "related_source_relative_path": row.get("source_relative_path", ""),
            "related_markdown_path": row.get("markdown_path", ""),
            "related_assets_dir": row.get("assets_dir", ""),
            "relationship": "same_or_related_cad_pdf",
        }
        for row in related_pdf
    ]
    write_csv(assets_dir / "related_sources_manifest.csv", related_rows)
    loss = {
        "source": str(source),
        "method": "dwg_tool_check",
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": reasons,
        "manual_review_required": True,
        "related_pdf_count": len(related_pdf),
    }
    (assets_dir / "conversion_loss.json").write_text(json.dumps(loss, ensure_ascii=False, indent=2), encoding="utf-8")
    md_lines = [
        "---",
        "remaining_skill_schema: pt9l-md-cad-v1",
        f"source_file: {source.name}",
        f"source_relative_path: {rel.as_posix()}",
        "source_type: dwg",
        f"assets_dir: {assets_dir.name}",
        f"conversion_loss_risk: {risk}",
        f"readiness: {readiness}",
        "manual_review_required: yes",
        f"converted_at: {now()}",
        "---",
        "",
        f"# {source.stem}",
        "",
        "DWG source was copied, but no local AutoCAD/DWG conversion tool was available.",
        "",
        f"- related_pdf_count: {len(related_pdf)}",
        f"- risk_reasons: {'; '.join(reasons)}",
        "",
        f"- [related_sources_manifest.csv]({assets_dir.name}/related_sources_manifest.csv)",
        f"- [conversion_loss.json]({assets_dir.name}/conversion_loss.json)",
        "",
    ]
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    record = base_record(source, rel, md_path, assets_dir, "cad", status, risk, readiness, reasons)
    record.update({"related_pdf_count": len(related_pdf)})
    return record


def convert_archive(source: Path) -> dict[str, Any]:
    md_path, assets_dir, rel = init_output(source)
    unzipped = assets_dir / "unzipped"
    unzipped.mkdir(parents=True, exist_ok=True)
    archive_rows: list[dict[str, Any]] = []
    status = "success"
    risk = "medium"
    readiness = "partial"
    reasons = ["archive_extracted_and_indexed"]
    pdf_manifest = existing_pdf_markdown()
    excel_manifest = existing_excel_markdown()
    try:
        with zipfile.ZipFile(source) as zf:
            zf.extractall(unzipped)
            for info in zf.infolist():
                if info.is_dir():
                    continue
                internal_ext = Path(info.filename).suffix.lower()
                key = normalize_key(Path(info.filename).stem)
                covered_by = ""
                covered_markdown = ""
                internal_status = "indexed"
                if internal_ext == ".pdf" and key in pdf_manifest:
                    covered_by = "pdf_conversion_manifest"
                    covered_markdown = pdf_manifest[key].get("markdown_path", "")
                    internal_status = "covered_by_existing_pdf_conversion"
                elif internal_ext in {".xls", ".xlsx"} and key in excel_manifest:
                    covered_by = "excel_conversion_manifest"
                    covered_markdown = excel_manifest[key].get("markdown_path", "")
                    internal_status = "covered_by_existing_excel_conversion"
                elif internal_ext == ".dwg":
                    internal_status = "blocked_dwg_tool_unavailable"
                    status = "partial"
                    risk = "high"
                    reasons.append("archive_contains_dwg")
                archive_rows.append(
                    {
                        "archive_member": info.filename,
                        "extension": internal_ext,
                        "file_size": info.file_size,
                        "status": internal_status,
                        "covered_by": covered_by,
                        "covered_markdown": covered_markdown,
                    }
                )
    except Exception as exc:
        status = "blocked"
        risk = "blocked"
        readiness = "blocked"
        reasons.append(f"archive_extract_failed: {exc}")
    write_csv(assets_dir / "archive_manifest.csv", archive_rows)
    loss = {
        "source": str(source),
        "method": "zip_extract_index",
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": list(dict.fromkeys(reasons)),
        "manual_review_required": risk != "low",
        "archive_member_count": len(archive_rows),
    }
    (assets_dir / "conversion_loss.json").write_text(json.dumps(loss, ensure_ascii=False, indent=2), encoding="utf-8")
    md_lines = [
        "---",
        "remaining_skill_schema: pt9l-md-archive-v1",
        f"source_file: {source.name}",
        f"source_relative_path: {rel.as_posix()}",
        "source_type: zip",
        f"assets_dir: {assets_dir.name}",
        f"conversion_loss_risk: {risk}",
        f"readiness: {readiness}",
        "manual_review_required: yes",
        f"converted_at: {now()}",
        "---",
        "",
        f"# {source.stem}",
        "",
        "Archive was extracted and indexed. Internal files are linked to existing conversions when a matching source conversion exists.",
        "",
        f"- archive_member_count: {len(archive_rows)}",
        f"- status: {status}",
        f"- risk_reasons: {'; '.join(loss['risk_reasons'])}",
        "",
        f"- [archive_manifest.csv]({assets_dir.name}/archive_manifest.csv)",
        f"- [conversion_loss.json]({assets_dir.name}/conversion_loss.json)",
        "",
    ]
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    record = base_record(source, rel, md_path, assets_dir, "archive", status, risk, readiness, reasons)
    record.update({"archive_member_count": len(archive_rows)})
    return record


def convert_ignored(source: Path) -> dict[str, Any]:
    md_path, assets_dir, rel = init_output(source)
    risk = "ignored"
    readiness = "ignored"
    status = "ignored"
    reasons = ["version_control_or_temporary_file_not_formal_evidence"]
    loss = {
        "source": str(source),
        "method": "ignored_file_registration",
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": reasons,
        "manual_review_required": False,
    }
    (assets_dir / "conversion_loss.json").write_text(json.dumps(loss, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(
        "\n".join(
            [
                "---",
                "remaining_skill_schema: pt9l-md-ignored-v1",
                f"source_file: {source.name}",
                f"source_relative_path: {rel.as_posix()}",
                f"source_type: {source.suffix.lower().lstrip('.')}",
                f"assets_dir: {assets_dir.name}",
                "conversion_loss_risk: ignored",
                "readiness: ignored",
                "manual_review_required: no",
                f"converted_at: {now()}",
                "---",
                "",
                f"# {source.stem}",
                "",
                "This file was registered but not converted because it is a version-control or temporary file, not formal DHF/DMR evidence.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return base_record(source, rel, md_path, assets_dir, "ignored", status, risk, readiness, reasons)


def base_record(source: Path, rel: Path, md_path: Path, assets_dir: Path, modality: str, status: str, risk: str, readiness: str, reasons: list[str]) -> dict[str, Any]:
    return {
        "source_relative_path": rel.as_posix(),
        "markdown_path": str(md_path),
        "assets_dir": str(assets_dir),
        "status": status,
        "modality": modality,
        "source_type": source.suffix.lower().lstrip("."),
        "source_size": source.stat().st_size,
        "loss_risk": risk,
        "readiness": readiness,
        "risk_reasons": "; ".join(list(dict.fromkeys(reasons))),
        "page_count": "",
        "archive_member_count": "",
        "semantic_finding_count": "",
        "visual_evidence_count": "",
        "image_count": "",
        "related_pdf_count": "",
    }


def gather_sources() -> list[Path]:
    rows: list[Path] = []
    for base in SOURCE_ROOTS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in TARGET_EXTS:
                rows.append(path)
    return sorted(rows, key=lambda p: (p.suffix.lower(), str(p).lower()))


def write_global_manifests(rows: list[dict[str, Any]], semantic_rows: list[dict[str, Any]], visual_rows: list[dict[str, Any]]) -> None:
    fields = [
        "source_relative_path",
        "markdown_path",
        "assets_dir",
        "status",
        "modality",
        "source_type",
        "source_size",
        "loss_risk",
        "readiness",
        "risk_reasons",
        "page_count",
        "archive_member_count",
        "semantic_finding_count",
        "visual_evidence_count",
        "image_count",
        "related_pdf_count",
    ]
    write_csv(MANIFEST_DIR / "remaining_source_manifest.csv", rows, fields)
    write_csv(MANIFEST_DIR / "remaining_semantic_findings_manifest.csv", semantic_rows)
    write_csv(MANIFEST_DIR / "remaining_visual_evidence_manifest.csv", visual_rows)
    write_csv(MANIFEST_DIR / "artwork_source_manifest.csv", [r for r in rows if r["modality"] == "artwork"], fields)
    write_csv(MANIFEST_DIR / "cad_source_manifest.csv", [r for r in rows if r["modality"] == "cad"], fields)
    write_csv(MANIFEST_DIR / "image_source_manifest.csv", [r for r in rows if r["modality"] == "image"], fields)
    write_csv(MANIFEST_DIR / "archive_source_manifest.csv", [r for r in rows if r["modality"] == "archive"], fields)
    write_csv(MANIFEST_DIR / "ignored_source_manifest.csv", [r for r in rows if r["modality"] == "ignored"], fields)
    summary = [
        "# Remaining Source Conversion Summary",
        "",
        f"- generated_at: {now()}",
        f"- source_count: {len(rows)}",
        f"- success: {sum(1 for r in rows if r['status'] == 'success')}",
        f"- partial: {sum(1 for r in rows if r['status'] == 'partial')}",
        f"- blocked: {sum(1 for r in rows if r['status'] == 'blocked')}",
        f"- ignored: {sum(1 for r in rows if r['status'] == 'ignored')}",
        "",
    ]
    for row in rows:
        summary.append(f"- `{row['source_relative_path']}` -> `{row['markdown_path']}` [{row['status']}/{row['loss_risk']}]")
    (MANIFEST_DIR / "remaining_conversion_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


def main() -> int:
    ocr_available, ocr_status = setup_ocr()
    sources = gather_sources()
    print(f"remaining_sources={len(sources)}")
    print(f"ocr_available={ocr_available}; {ocr_status}")
    records: list[dict[str, Any]] = []
    semantic_all: list[dict[str, Any]] = []
    visual_all: list[dict[str, Any]] = []
    for idx, source in enumerate(sources, start=1):
        ext = source.suffix.lower()
        print(f"[{idx}/{len(sources)}] {rel_to_root(source).as_posix()}")
        if ext in IGNORED_EXTS:
            record = convert_ignored(source)
        elif ext == ".ai":
            record, semantic_rows, visual_rows = convert_ai(source, ocr_available)
            for row in semantic_rows:
                row["source_relative_path"] = record["source_relative_path"]
                row["assets_dir"] = record["assets_dir"]
            for row in visual_rows:
                row["source_relative_path"] = record["source_relative_path"]
                row["assets_dir"] = record["assets_dir"]
            semantic_all.extend(semantic_rows)
            visual_all.extend(visual_rows)
        elif ext == ".dwg":
            record = convert_dwg(source)
        elif ext == ".zip":
            record = convert_archive(source)
        elif ext in {".jpg", ".jpeg", ".png"}:
            record, semantic_rows = convert_image(source, ocr_available)
            for row in semantic_rows:
                row["source_relative_path"] = record["source_relative_path"]
                row["assets_dir"] = record["assets_dir"]
            semantic_all.extend(semantic_rows)
        else:
            record = convert_ignored(source)
        records.append(record)
    write_global_manifests(records, semantic_all, visual_all)
    print(f"converted={sum(1 for r in records if r['status'] == 'success')}/{len(records)}")
    print(f"partial={sum(1 for r in records if r['status'] == 'partial')}")
    print(f"blocked={sum(1 for r in records if r['status'] == 'blocked')}")
    print(f"ignored={sum(1 for r in records if r['status'] == 'ignored')}")
    print(f"summary={MANIFEST_DIR / 'remaining_conversion_summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
