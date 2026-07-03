---
name: conversion-toolkit-skill
description: Checks and prepares the local toolchain for DHF/DMR Word, Excel, and PDF conversion. Use before converting doc/docx/xls/xlsx/pdf files, before running conversion agents, or when the user mentions missing tools, installing tools, OCR, MarkItDown, Office COM, Tesseract, PyMuPDF, openpyxl, or PDF/Excel/Word conversion readiness.
---

# Conversion Toolkit Skill

## Purpose

Before any Word, Excel, or PDF conversion, verify that the local conversion toolchain is ready. Do not start conversion until required tools are present or the missing-tool risk is explicitly reported.

## Mandatory First Step

Run the toolkit check script before conversion:

```powershell
python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py" --install
```

If `--install` fails because of network or permission issues, rerun without `--install` and report the missing tools:

```powershell
python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py"
```

## Required Toolchain

### Python Packages

These can be auto-installed by the script with the Tsinghua PyPI mirror:

- `markitdown`: Word text conversion where used.
- `openpyxl`: Excel `.xlsx` structure, values, formulas, styles, images.
- `pywin32`: Word/Excel COM automation on Windows.
- `PyMuPDF`: PDF page rendering and page image generation.
- `Pillow`: image preprocessing/cropping/upscaling.
- `pytesseract`: Python wrapper for Tesseract OCR.

### External Applications

These must be detected and cannot always be safely auto-installed:

- Microsoft Word COM: required for robust `.doc` and Word visual/header/field inspection.
- Microsoft Excel COM: required for `.xls -> .xlsx`, shape text, headers/footers, sheet PDF export.
- Tesseract OCR: required for scanned PDFs/images and Excel/Word image OCR.
- Tesseract languages: `chi_sim`, `eng`, `osd`.
- LibreOffice: optional fallback for legacy Office conversion.

## Known Good Local Paths

Use these when present:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
D:\AI_0415\03DHF\packages\tessdata
```

The local tessdata directory should contain:

```text
chi_sim.traineddata
eng.traineddata
osd.traineddata
```

When calling `pytesseract`, set:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"D:\AI_0415\03DHF\packages\tessdata"
```

## Readiness Rules

- If Python packages are missing, run the toolkit script with `--install` before conversion.
- If Tesseract is missing, do not claim OCR readiness. Copy or install Tesseract first.
- If `chi_sim` is missing, do not claim Chinese OCR readiness.
- If Word COM is missing, `.doc` conversion and Word visual/header/form-field inspection are incomplete.
- If Excel COM is missing, `.xls` conversion and Excel page visual evidence are incomplete.
- If PyMuPDF is missing, PDF page rendering and Excel sheet PNG rendering are incomplete.
- If only LibreOffice is missing but Word/Excel COM is available, continue and record LibreOffice as optional missing.

## Batch Conversion Gate (Mandatory)

Before any full batch conversion, run a per-type sample gate.

- For each source type or modality in the batch, convert only 3 representative files first. If fewer than 3 files exist for that type, convert all files of that type.
- For mixed batches, sample independently per type, for example 3 `.doc`, 3 `.docx`, 3 `.xls/.xlsx`, 3 `.pdf`, 3 `.ai`, 3 images, and 3 archives.
- After sample conversion, inspect logs, Markdown, manifests, copied sources, visual pages, OCR text, and `conversion_loss` output.
- The sample gate fails if there are blocked files, empty/garbled Markdown, mojibake path errors, missing page renders, missing OCR where OCR is required, missing assets, wrong source paths, or obvious metadata mismatches.
- Record the sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
- Only run the full batch after the sample gate passes. If the sample fails, fix tooling or converter logic first, then rerun the sample gate.
- Do not silently skip this gate just because the toolchain check passed.

## Output

The script writes:

```text
D:\AI_0415\03DHF\tool_check_report.json
```

Use this report as evidence that the environment was checked before conversion.

## Tsinghua Mirror Install Command

If manual install is needed:

```powershell
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn markitdown openpyxl pywin32 PyMuPDF Pillow pytesseract
```
