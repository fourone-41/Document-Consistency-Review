from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(r"D:\AI_0415\03DHF")
REPORT_PATH = ROOT / "tool_check_report.json"
TSINGHUA_INDEX = "https://pypi.tuna.tsinghua.edu.cn/simple"
TSINGHUA_HOST = "pypi.tuna.tsinghua.edu.cn"
TESSERACT_EXE = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
LOCAL_TESSDATA = ROOT / "packages" / "tessdata"
LIBREOFFICE_EXE = Path(r"C:\Program Files\LibreOffice\program\soffice.exe")

PYTHON_PACKAGES = {
    "markitdown": "markitdown",
    "openpyxl": "openpyxl",
    "win32com": "pywin32",
    "fitz": "PyMuPDF",
    "PIL": "Pillow",
    "pytesseract": "pytesseract",
}


def run(cmd: list[str], timeout: int = 120) -> tuple[int, str]:
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except Exception as exc:
        return 999, str(exc)


def ensure_pip() -> dict[str, Any]:
    code, output = run([sys.executable, "-m", "pip", "--version"], timeout=30)
    if code == 0:
        return {"ok": True, "action": "pip_available", "output": output.strip()}
    code, output = run([sys.executable, "-m", "ensurepip", "--upgrade"], timeout=120)
    return {"ok": code == 0, "action": "ensurepip", "output": output.strip()}


def install_missing(missing_distributions: list[str]) -> dict[str, Any]:
    if not missing_distributions:
        return {"ok": True, "action": "none", "packages": [], "output": ""}
    pip_status = ensure_pip()
    if not pip_status["ok"]:
        return {"ok": False, "action": "ensurepip_failed", "packages": missing_distributions, "output": pip_status["output"]}
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-i",
        TSINGHUA_INDEX,
        "--trusted-host",
        TSINGHUA_HOST,
        *missing_distributions,
    ]
    code, output = run(cmd, timeout=600)
    return {"ok": code == 0, "action": "pip_install", "packages": missing_distributions, "output": output.strip()}


def check_python_packages() -> dict[str, Any]:
    rows = []
    missing: list[str] = []
    for module_name, distribution in PYTHON_PACKAGES.items():
        ok = importlib.util.find_spec(module_name) is not None
        rows.append({"module": module_name, "distribution": distribution, "ok": ok})
        if not ok:
            missing.append(distribution)
    # De-duplicate pywin32 or other repeated distributions.
    missing = sorted(set(missing))
    return {"ok": not missing, "items": rows, "missing_distributions": missing}


def check_office_com() -> dict[str, Any]:
    result: dict[str, Any] = {"word_com": False, "excel_com": False, "errors": []}
    try:
        import pythoncom  # type: ignore
        import win32com.client  # type: ignore

        pythoncom.CoInitialize()
        for app_name, key in [("Word.Application", "word_com"), ("Excel.Application", "excel_com")]:
            app = None
            try:
                app = win32com.client.DispatchEx(app_name)
                result[key] = True
            except Exception as exc:
                result["errors"].append(f"{app_name}: {exc}")
            finally:
                try:
                    if app is not None:
                        app.Quit()
                except Exception:
                    pass
        pythoncom.CoUninitialize()
    except Exception as exc:
        result["errors"].append(str(exc))
    result["ok"] = bool(result["word_com"] and result["excel_com"])
    return result


def check_tesseract() -> dict[str, Any]:
    result: dict[str, Any] = {
        "exe_path": str(TESSERACT_EXE),
        "exe_exists": TESSERACT_EXE.exists(),
        "tessdata_path": str(LOCAL_TESSDATA),
        "tessdata_exists": LOCAL_TESSDATA.exists(),
        "languages": [],
        "ok": False,
        "error": "",
    }
    if not TESSERACT_EXE.exists():
        result["error"] = "tesseract.exe not found"
        return result
    try:
        import pytesseract  # type: ignore

        pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_EXE)
        if LOCAL_TESSDATA.exists():
            os.environ["TESSDATA_PREFIX"] = str(LOCAL_TESSDATA)
        result["version"] = str(pytesseract.get_tesseract_version())
        languages = pytesseract.get_languages(config="")
        result["languages"] = languages
        required = {"chi_sim", "eng", "osd"}
        result["ok"] = required.issubset(set(languages))
        if not result["ok"]:
            result["error"] = f"missing languages: {sorted(required - set(languages))}"
    except Exception as exc:
        result["error"] = str(exc)
    return result


def check_external_tools() -> dict[str, Any]:
    return {
        "tesseract": check_tesseract(),
        "libreoffice": {
            "path": str(LIBREOFFICE_EXE),
            "exists": LIBREOFFICE_EXE.exists(),
            "optional": True,
        },
        "soffice_on_path": shutil.which("soffice") or "",
    }


def compute_readiness(report: dict[str, Any]) -> dict[str, Any]:
    blockers = []
    warnings = []
    if not report["python_packages"]["ok"]:
        blockers.append("missing_python_packages")
    office = report["office_com"]
    if not office.get("word_com"):
        blockers.append("word_com_missing")
    if not office.get("excel_com"):
        blockers.append("excel_com_missing")
    tess = report["external_tools"]["tesseract"]
    if not tess.get("ok"):
        blockers.append("tesseract_or_languages_missing")
    if not report["external_tools"]["libreoffice"]["exists"]:
        warnings.append("libreoffice_optional_missing")
    return {
        "ready_for_word": not any(b in blockers for b in ["missing_python_packages", "word_com_missing", "tesseract_or_languages_missing"]),
        "ready_for_excel": not any(b in blockers for b in ["missing_python_packages", "excel_com_missing", "tesseract_or_languages_missing"]),
        "ready_for_pdf": not any(b in blockers for b in ["missing_python_packages", "tesseract_or_languages_missing"]),
        "blockers": blockers,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true", help="Install missing Python packages with Tsinghua PyPI mirror.")
    args = parser.parse_args()

    report: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "python": sys.executable,
        "python_version": sys.version,
        "install_attempt": None,
    }

    pkg_status = check_python_packages()
    if args.install and not pkg_status["ok"]:
        report["install_attempt"] = install_missing(pkg_status["missing_distributions"])
        pkg_status = check_python_packages()
    report["python_packages"] = pkg_status
    report["office_com"] = check_office_com()
    report["external_tools"] = check_external_tools()
    report["readiness"] = compute_readiness(report)

    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"report={REPORT_PATH}")
    print(f"ready_for_word={report['readiness']['ready_for_word']}")
    print(f"ready_for_excel={report['readiness']['ready_for_excel']}")
    print(f"ready_for_pdf={report['readiness']['ready_for_pdf']}")
    if report["readiness"]["blockers"]:
        print("blockers=" + ";".join(report["readiness"]["blockers"]))
    if report["readiness"]["warnings"]:
        print("warnings=" + ";".join(report["readiness"]["warnings"]))
    return 0 if not report["readiness"]["blockers"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
