# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
RECOVERY_REPORT = ROOT / "markitdown_word_recovery_report.csv"
OUT_CSV = ROOT / "conversion_loss_risk_report.csv"
OUT_MD = ROOT / "conversion_loss_risk_summary.md"
PYTHON = Path(sys.executable)
CHECK_CHARS = {
    "\u2611",
    "\u2612",
    "\u2713",
    "\u2714",
    "\u221a",
    "\u25a0",
    "\u25a1",
    "\u00fe",
    "\u00fc",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def count_check_chars(text: str) -> int:
    return sum(1 for ch in text if ch in CHECK_CHARS)


def worker(input_json: Path, output_json: Path) -> None:
    payload = json.loads(input_json.read_text(encoding="utf-8"))
    source = Path(payload["source"])
    result: dict[str, Any] = {
        "inspection_status": "failed",
        "error_message": "",
        "source_text_length": 0,
        "source_table_count": 0,
        "source_form_field_count": 0,
        "source_checkbox_form_field_count": 0,
        "source_checkbox_checked_count": 0,
        "source_content_control_count": 0,
        "source_checkbox_content_control_count": 0,
        "source_inline_shape_count": 0,
        "source_embedded_ole_count": 0,
        "source_floating_shape_count": 0,
        "source_checkmark_char_count": 0,
    }
    word = None
    doc = None
    try:
        import pythoncom
        import win32com.client

        pythoncom.CoInitialize()
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(str(source.resolve()), ReadOnly=True, AddToRecentFiles=False, ConfirmConversions=False)
        text = str(doc.Range().Text or "")
        result["source_text_length"] = len(text)
        result["source_table_count"] = int(doc.Tables.Count)
        result["source_form_field_count"] = int(doc.FormFields.Count)
        checkbox_forms = 0
        checkbox_checked = 0
        for i in range(1, int(doc.FormFields.Count) + 1):
            ff = doc.FormFields.Item(i)
            try:
                cb = ff.CheckBox
                checkbox_forms += 1
                if bool(cb.Value):
                    checkbox_checked += 1
            except Exception:
                pass
        result["source_checkbox_form_field_count"] = checkbox_forms
        result["source_checkbox_checked_count"] = checkbox_checked
        try:
            result["source_content_control_count"] = int(doc.ContentControls.Count)
            cc_checkbox = 0
            for i in range(1, int(doc.ContentControls.Count) + 1):
                cc = doc.ContentControls.Item(i)
                # Word checkbox content controls usually expose Checked.
                try:
                    _ = cc.Checked
                    cc_checkbox += 1
                except Exception:
                    pass
            result["source_checkbox_content_control_count"] = cc_checkbox
        except Exception:
            pass
        result["source_inline_shape_count"] = int(doc.InlineShapes.Count)
        embedded = 0
        for i in range(1, int(doc.InlineShapes.Count) + 1):
            shape = doc.InlineShapes.Item(i)
            try:
                if int(shape.Type) in {1, 2, 5}:
                    embedded += 1
            except Exception:
                try:
                    _ = shape.OLEFormat
                    embedded += 1
                except Exception:
                    pass
        result["source_embedded_ole_count"] = embedded
        try:
            result["source_floating_shape_count"] = int(doc.Shapes.Count)
        except Exception:
            pass
        result["source_checkmark_char_count"] = count_check_chars(text)
        result["inspection_status"] = "success"
        doc.Close(False)
        doc = None
        word.Quit()
        word = None
    except Exception as exc:
        result["error_message"] = str(exc)
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
    finally:
        try:
            pythoncom.CoUninitialize()  # type: ignore[name-defined]
        except Exception:
            pass
    output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def inspect_source(source: Path, timeout: int = 60) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        input_json = temp / "input.json"
        output_json = temp / "output.json"
        input_json.write_text(json.dumps({"source": str(source)}, ensure_ascii=False), encoding="utf-8")
        try:
            subprocess.run(
                [str(PYTHON), str(Path(__file__).resolve()), "--worker", str(input_json), str(output_json)],
                timeout=timeout,
                check=False,
                capture_output=True,
                text=True,
            )
        except subprocess.TimeoutExpired:
            return {"inspection_status": "timeout", "error_message": f"inspection exceeded {timeout}s"}
        if output_json.exists():
            return json.loads(output_json.read_text(encoding="utf-8"))
        return {"inspection_status": "failed", "error_message": "worker produced no output"}


def assess(row: dict[str, str], inspected: dict[str, Any]) -> dict[str, str]:
    md_path = Path(row.get("output_md_path", ""))
    md_text = read_text(md_path)
    md_check_count = count_check_chars(md_text)
    reasons: list[str] = []
    status = inspected.get("inspection_status", "")
    if status != "success":
        reasons.append(f"source_inspection_{status}")
    if int(inspected.get("source_checkbox_form_field_count") or 0) > 0:
        reasons.append("word_checkbox_form_fields_present")
    if int(inspected.get("source_checkbox_content_control_count") or 0) > 0:
        reasons.append("word_checkbox_content_controls_present")
    if int(inspected.get("source_embedded_ole_count") or 0) > 0:
        reasons.append("embedded_ole_or_spreadsheet_present")
    if int(inspected.get("source_inline_shape_count") or 0) > 0:
        reasons.append("inline_shapes_present")
    if int(inspected.get("source_table_count") or 0) > 0 and "|" not in md_text:
        reasons.append("source_tables_not_obvious_in_markdown")
    source_check_count = int(inspected.get("source_checkmark_char_count") or 0)
    if source_check_count > md_check_count:
        reasons.append("checkmark_symbols_may_be_lost")
    if int(inspected.get("source_form_field_count") or 0) > 0 and "?" not in md_text and "checkbox" not in md_text.lower():
        reasons.append("form_field_state_not_explicit_in_markdown")

    if any(r in reasons for r in ["embedded_ole_or_spreadsheet_present", "word_checkbox_form_fields_present", "word_checkbox_content_controls_present", "checkmark_symbols_may_be_lost", "form_field_state_not_explicit_in_markdown"]):
        level = "high"
    elif reasons:
        level = "medium"
    else:
        level = "low"

    return {
        "file_id": row.get("file_id", ""),
        "original_file_path": row.get("original_file_path", ""),
        "resolved_source_path": row.get("resolved_source_path", ""),
        "output_md_path": row.get("output_md_path", ""),
        "inspection_status": str(status),
        "source_table_count": str(inspected.get("source_table_count", "")),
        "source_form_field_count": str(inspected.get("source_form_field_count", "")),
        "source_checkbox_form_field_count": str(inspected.get("source_checkbox_form_field_count", "")),
        "source_checkbox_checked_count": str(inspected.get("source_checkbox_checked_count", "")),
        "source_content_control_count": str(inspected.get("source_content_control_count", "")),
        "source_checkbox_content_control_count": str(inspected.get("source_checkbox_content_control_count", "")),
        "source_inline_shape_count": str(inspected.get("source_inline_shape_count", "")),
        "source_embedded_ole_count": str(inspected.get("source_embedded_ole_count", "")),
        "source_floating_shape_count": str(inspected.get("source_floating_shape_count", "")),
        "source_checkmark_char_count": str(inspected.get("source_checkmark_char_count", "")),
        "markdown_checkmark_char_count": str(md_check_count),
        "loss_risk_level": level,
        "risk_reasons": "; ".join(reasons),
        "error_message": str(inspected.get("error_message", "")),
    }


def write_summary(rows: list[dict[str, str]]) -> None:
    from collections import Counter

    counts = Counter(row["loss_risk_level"] for row in rows)
    reason_counts: Counter[str] = Counter()
    for row in rows:
        for reason in row["risk_reasons"].split("; "):
            if reason:
                reason_counts[reason] += 1
    lines = [
        "# Conversion Loss Risk Summary",
        "",
        "This report checks whether readable Markdown may still have lost source information such as checkboxes, embedded spreadsheets, OLE objects, or table states.",
        "",
        "## Risk Levels",
        "",
    ]
    for level in ["high", "medium", "low"]:
        lines.append(f"- {level}: {counts.get(level, 0)}")
    lines.extend(["", "## Main Risk Reasons", ""])
    for reason, count in reason_counts.most_common(20):
        lines.append(f"- {reason}: {count}")
    lines.extend(["", f"Full detail: `{OUT_CSV.name}`"])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) >= 2 and sys.argv[1] == "--worker":
        worker(Path(sys.argv[2]), Path(sys.argv[3]))
        return

    recovery_rows = [
        row
        for row in read_csv(RECOVERY_REPORT)
        if row.get("conversion_status") == "success" and row.get("resolved_source_path")
    ]
    fields = [
        "file_id",
        "original_file_path",
        "resolved_source_path",
        "output_md_path",
        "inspection_status",
        "source_table_count",
        "source_form_field_count",
        "source_checkbox_form_field_count",
        "source_checkbox_checked_count",
        "source_content_control_count",
        "source_checkbox_content_control_count",
        "source_inline_shape_count",
        "source_embedded_ole_count",
        "source_floating_shape_count",
        "source_checkmark_char_count",
        "markdown_checkmark_char_count",
        "loss_risk_level",
        "risk_reasons",
        "error_message",
    ]
    out_rows: list[dict[str, str]] = []
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for idx, row in enumerate(recovery_rows, start=1):
            source = Path(row["resolved_source_path"])
            print(f"auditing {idx}/{len(recovery_rows)} {source.name}", flush=True)
            inspected = inspect_source(source)
            out = assess(row, inspected)
            out_rows.append(out)
            writer.writerow(out)
            f.flush()
    write_summary(out_rows)
    print(f"rows={len(out_rows)}")
    print(f"csv={OUT_CSV}")
    print(f"summary={OUT_MD}")


if __name__ == "__main__":
    main()
