# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from markitdown import MarkItDown


ROOT = Path(__file__).resolve().parent
CONVERSION_REPORT = ROOT / "conversion_report.csv"
OUT_DIR = ROOT / "converted_md" / "markitdown_recovered"
REPORT = ROOT / "markitdown_word_recovery_report.csv"
SOFFICE = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")
LEGACY_WRAPPER_DIR = "PT9L-DHF -梳理版"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def safe_part(text: str, max_len: int = 120) -> str:
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", text)
    text = re.sub(r"\s+", "_", text).strip("._ ")
    return (text or "unnamed")[:max_len]


def relative_output_path(source: Path) -> Path:
    try:
        rel = source.resolve().relative_to(ROOT)
        parent = OUT_DIR / rel.parent
    except Exception:
        parent = OUT_DIR
    parent.mkdir(parents=True, exist_ok=True)
    return parent / f"{safe_part(source.stem)}.markitdown.md"


def resolve_source_path(recorded_path: Path) -> tuple[Path, str]:
    if recorded_path.exists():
        return recorded_path, "recorded_path"
    parts = list(recorded_path.parts)
    if LEGACY_WRAPPER_DIR in parts:
        parts.remove(LEGACY_WRAPPER_DIR)
        remapped = Path(*parts)
        if remapped.exists():
            return remapped, f"removed_wrapper_dir:{LEGACY_WRAPPER_DIR}"
    return recorded_path, "not_found"


def convert_doc_with_word(source: Path, temp_dir: Path) -> tuple[Path | None, str, str]:
    try:
        import pythoncom
        import win32com.client
    except Exception as exc:
        return None, "word_com_unavailable", str(exc)

    out_path = temp_dir / f"{safe_part(source.stem)}.docx"
    word = None
    doc = None
    try:
        pythoncom.CoInitialize()
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(str(source.resolve()), ReadOnly=True)
        doc.SaveAs2(str(out_path.resolve()), FileFormat=16)
        doc.Close(False)
        doc = None
        word.Quit()
        word = None
        if out_path.exists():
            return out_path, "word_com_doc_to_docx", ""
        return None, "word_com_doc_to_docx", "docx output missing"
    except Exception as exc:
        try:
            if doc is not None:
                doc.Close(False)
        except Exception:
            pass
        try:
            if word is not None:
                word.Quit()
        except Exception:
            pass
        return None, "word_com_doc_to_docx", str(exc)
    finally:
        try:
            pythoncom.CoUninitialize()
        except Exception:
            pass


def convert_doc_with_libreoffice(source: Path, temp_dir: Path) -> tuple[Path | None, str, str]:
    if not SOFFICE.exists():
        return None, "libreoffice_unavailable", f"missing {SOFFICE}"
    try:
        subprocess.run(
            [
                str(SOFFICE),
                "--headless",
                "--convert-to",
                "docx",
                "--outdir",
                str(temp_dir),
                str(source),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except Exception as exc:
        return None, "libreoffice_doc_to_docx", str(exc)
    out_path = temp_dir / f"{source.stem}.docx"
    if out_path.exists():
        return out_path, "libreoffice_doc_to_docx", ""
    matches = list(temp_dir.glob("*.docx"))
    if matches:
        return matches[0], "libreoffice_doc_to_docx", ""
    return None, "libreoffice_doc_to_docx", "docx output missing"


def doc_to_docx(source: Path, temp_dir: Path) -> tuple[Path | None, str, str]:
    path, method, error = convert_doc_with_libreoffice(source, temp_dir)
    if path:
        return path, method, error
    word_path, word_method, word_error = convert_doc_with_word(source, temp_dir)
    if word_path:
        return word_path, word_method, word_error
    return None, f"{method}; {word_method}", f"{error}; {word_error}"


def markdown_header(source: Path, source_type: str, method: str) -> str:
    return "\n".join(
        [
            "---",
            f"source_file: {source}",
            f"source_file_name: {source.name}",
            f"source_type: {source_type}",
            f"conversion_method: {method}",
            f"converted_at: {dt.datetime.now().replace(microsecond=0).isoformat(sep=' ')}",
            "manual_review_required: yes",
            "---",
            "",
        ]
    )


def convert_with_markitdown(md: MarkItDown, input_path: Path, source: Path, method: str) -> tuple[str, str]:
    try:
        result = md.convert(str(input_path))
        text = getattr(result, "text_content", "") or ""
        if not text.strip():
            return "", "markitdown returned empty text"
        return markdown_header(source, source.suffix.lower().lstrip("."), method) + text.strip() + "\n", ""
    except Exception as exc:
        return "", str(exc)


def process_row(row: dict[str, str], md: MarkItDown, temp_root: Path) -> dict[str, Any]:
    recorded_source = Path(row.get("original_file_path", ""))
    source, source_resolution = resolve_source_path(recorded_source)
    ext = row.get("file_extension", "").lower()
    out_md = relative_output_path(recorded_source)
    result: dict[str, Any] = {
        "file_id": row.get("file_id", ""),
        "original_file_path": str(recorded_source),
        "resolved_source_path": str(source),
        "source_resolution": source_resolution,
        "original_file_name": row.get("original_file_name", source.name),
        "file_extension": ext,
        "source_exists": "yes" if source.exists() else "no",
        "intermediate_docx_path": "",
        "output_md_path": str(out_md),
        "conversion_status": "failed",
        "conversion_method": "",
        "text_length": "0",
        "manual_review_required": "yes",
        "error_message": "",
    }
    if ext not in {"doc", "docx"}:
        result["conversion_status"] = "skipped"
        result["error_message"] = "not a Word file"
        return result
    if not source.exists():
        result["conversion_status"] = "missing_source"
        result["error_message"] = "source file not present in current workspace"
        return result

    with tempfile.TemporaryDirectory(dir=temp_root) as td:
        temp_dir = Path(td)
        input_path = source
        method_parts: list[str] = []
        if ext == "doc":
            docx_path, method, error = doc_to_docx(source, temp_dir)
            method_parts.append(method)
            if not docx_path:
                result["conversion_method"] = "; ".join(method_parts)
                result["error_message"] = error
                return result
            input_path = docx_path
            result["intermediate_docx_path"] = str(docx_path)
        elif ext == "docx":
            method_parts.append("native_docx")

        text, error = convert_with_markitdown(md, input_path, source, "; ".join(method_parts + ["markitdown"]))
        result["conversion_method"] = "; ".join(method_parts + ["markitdown"])
        if error:
            result["error_message"] = error
            return result
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text(text, encoding="utf-8")
        result["conversion_status"] = "success"
        result["text_length"] = str(len(text))
        result["manual_review_required"] = "yes"
        result["error_message"] = ""
        return result


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = read_csv(CONVERSION_REPORT)
    word_rows = [r for r in rows if r.get("file_extension", "").lower() == "doc"]
    md = MarkItDown()
    report_rows: list[dict[str, Any]] = []
    fields = [
        "file_id",
        "original_file_path",
        "resolved_source_path",
        "source_resolution",
        "original_file_name",
        "file_extension",
        "source_exists",
        "intermediate_docx_path",
        "output_md_path",
        "conversion_status",
        "conversion_method",
        "text_length",
        "manual_review_required",
        "error_message",
    ]
    with REPORT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
    with tempfile.TemporaryDirectory() as td:
        temp_root = Path(td)
        for row in word_rows:
            name = row.get("original_file_name") or Path(row.get("original_file_path", "")).name
            print(f"recovering {name}", flush=True)
            result = process_row(row, md, temp_root)
            report_rows.append(result)
            with REPORT.open("a", encoding="utf-8-sig", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
                writer.writerow(result)

    success = sum(1 for r in report_rows if r["conversion_status"] == "success")
    missing = sum(1 for r in report_rows if r["conversion_status"] == "missing_source")
    failed = sum(1 for r in report_rows if r["conversion_status"] == "failed")
    print(f"word_files={len(report_rows)} success={success} missing_source={missing} failed={failed}")
    print(f"report={REPORT}")


if __name__ == "__main__":
    main()
