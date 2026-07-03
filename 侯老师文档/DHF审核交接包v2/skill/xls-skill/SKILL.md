---
name: xls-skill
description: Excel `.xls` and `.xlsx` to AI-readable Markdown workflow for DHF/DMR evidence. Use when converting, auditing, sampling, or reviewing spreadsheets with tables, formulas, merged cells, hidden rows/sheets, filters, embedded images, charts, OLE objects, signatures, inspection photos, color-coded status/risk/pass-fail cells, or conditional formatting.
---

# XLS Skill: Excel XLS/XLSX -> AI-Readable Markdown

## Agent Entry

For a dedicated Excel conversion agent, use:

- `AGENT.md`: agent role, workflow, learned lessons, and required outputs.
- `AGENT_PROMPT.md`: copyable startup prompt for a new agent.
- `PROMPT.md`: short task prompt for Excel conversion/audit.

## Goal

Convert every `.xls` / `.xlsx` file into AI-readable evidence without losing spreadsheet meaning.

Readable tables are not enough. The output must preserve or report:

- source file path and resolved path
- workbook metadata and sheet list
- every visible sheet table as Markdown/CSV
- formulas and calculated values
- merged-cell structure
- hidden sheets, hidden rows, hidden columns, filters, and freeze panes
- cell comments/notes and hyperlinks
- embedded images, drawings, charts, signatures, screenshots, and inspection photos
- headers/footers, print-title areas, and floating text boxes/shapes such as form numbers
- cell fill color, font color, conditional formatting, and color-coded status/risk/pass-fail meaning
- OLE/embedded objects
- conversion loss risks

## Required Output Per Excel File

For every `.xls` / `.xlsx`, produce:

- `<name>.md`: workbook-level Markdown index with source metadata.
- `sheets_csv/`: one CSV per sheet, preserving table values.
- `sheets_md/`: one Markdown table per sheet when feasible.
- `sheet_pages_pdf/`: sheet-level PDF exports when Excel layout carries meaning.
- `sheet_pages_png/`: rendered sheet/page snapshots for visual review.
- `<name>.pages.md`: page visual review Markdown linking exported PDF/PNG pages.
- `page_manifest.csv`: sheet/page number, PDF path, PNG path, render method, and visual-review reason.
- `images/`: every embedded image extracted as a standalone file.
- `<name>.images.md`: image review page with OCR/nearby-cell context.
- `formula_manifest.csv`: formulas, formula cells, and cached/display values when available.
- `visual_format_manifest.csv`: cell color, fill, font color, conditional-format/color-coded meaning.
- `structure_manifest.csv`: merged cells, hidden sheets/rows/columns, filters, freeze panes, dimensions.
- `text_objects_manifest.csv`: page headers/footers, print titles, shape text, and floating text boxes.
- `semantic_findings_manifest.csv` when applicable: defect grades, tool/fixture lists, operation steps, icon/symbol meanings, and other high-value QA facts extracted from tables/images.
- `conversion_loss.json` or CSV row: source inspection result and risk reasons.
- Manual review flag: `yes` unless conversion loss risk is proven low.

## Mandatory Workflow

0. Check conversion toolkit readiness.
   - Read `D:\AI_0415\03DHF\skill\conversion-toolkit-skill\SKILL.md`.
   - Run `python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py" --install`.
   - Do not start Excel conversion until Python packages, Excel COM, PyMuPDF, and Tesseract with `chi_sim`, `eng`, `osd` are ready or missing-tool risk is explicitly reported.

0.5. Run the batch conversion gate before full Excel conversion.
   - Convert only 3 representative `.xls/.xlsx` files first. If fewer than 3 Excel files exist, convert all Excel files.
   - Inspect the sample Markdown, CSV/MD sheet outputs, page PNG/PDF renders, manifests, shape/header text, OCR/image outputs, and `conversion_loss` records.
   - The gate fails if any sample has blocked opening, empty/garbled Markdown, mojibake paths, missing sheets, missing page visuals, missing assets, wrong source metadata, or unhandled exceptions.
   - Record sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
   - Run the full Excel batch only after the sample gate passes. If it fails, fix the converter/tooling and rerun the sample gate first.

1. Resolve source path.
   - Do not trust terminal mojibake.
   - Use `Path.exists()` / `Test-Path`.
   - Keep both `recorded_source_path` and `resolved_source_path`.
   - Avoid hardcoded Chinese path literals in scripts; use manifest paths or Unicode escapes.

2. Normalize workbook input.
   - `.xlsx`: inspect directly with `openpyxl` and, when needed, Excel COM.
   - `.xls`: convert to `.xlsx` using Microsoft Excel COM on Windows; use LibreOffice only as fallback and mark method.
   - Keep the converted `.xlsx` as an intermediate evidence artifact or record its temp path/method.
   - Run GUI automation with timeout/per-file isolation so one bad workbook cannot block the batch.

3. Extract sheet data.
   - Export every visible worksheet to CSV.
   - Generate Markdown tables only when size is manageable; keep CSV as the source-of-truth table output.
   - Preserve sheet order and sheet names.
   - Record used ranges and dimensions.
   - Do not drop blank-looking rows/columns if they are inside the used range and carry layout meaning.

3.1. Create page-visual evidence for layout-heavy sheets.
   - Excel evidence must use two parallel channels:
     - Structured channel: workbook Markdown, sheet CSV/MD, and manifests from original Excel cells/objects.
     - Page visual channel: export relevant sheets to PDF/PNG and create a page visual Markdown review file.
   - Use the page visual channel when the sheet contains images plus arrows/text boxes, shape labels, screenshots, labels, signatures, stamps, print-layout forms, DMR work instructions, inspection specs, FMEA tables, label review forms, or any question about "where/what does it look like".
   - Do not replace original Excel extraction with PDF. Use both: PDF/PNG preserves visual layout and relative positions; original Excel preserves cells, formulas, hidden content, object metadata, and machine-readable structure.
   - Preserve sheet name, page number, PDF path, PNG path, and render method in a page manifest.

4. Extract formulas and calculated values.
   - Read formula view (`data_only=False`) and value view (`data_only=True`) when possible.
   - Record formula cell, formula text, cached/display value, number format, and sheet name.
   - If cached values are missing or stale, mark `formula_value_review_required=yes`.

5. Inspect source structure.
   - Record merged cell ranges and their top-left value.
   - Record hidden sheets, hidden rows, hidden columns.
   - Record filters, freeze panes, print area, data validation, comments/notes, hyperlinks.
   - Record page setup headers/footers, print titles, charts, drawings, shapes, text boxes, and embedded/OLE objects when detectable.
   - Use Excel COM when openpyxl cannot read floating text. Form numbers such as `???QR-7.3-01/E0` may live in a header or text box and will not appear in normal sheet CSV.

6. Extract embedded images.
   - For `.xlsx`, read workbook package / `openpyxl` images.
   - For `.xls`, convert to `.xlsx` first; if image extraction fails, use Excel COM export/screenshot fallback.
   - `openpyxl` may drop unsupported image formats such as WMF/EMF. If warnings mention unsupported image format, mark image extraction as incomplete and use Excel COM export/screenshot fallback or manual review.
   - Save every image under `images/`.
   - Record sheet name, anchor cell, nearby cell text, image size, OCR text, and inferred evidence type.
   - Do not rely only on image order. Pair images to nearby sheet context and anchor cells.
   - If images and annotations/arrows/text boxes are separate objects, standalone image extraction is incomplete. Export the whole sheet/page to PDF/PNG and answer from the combined page view.

7. Extract visual-format semantics.
   - Inspect cell fill color, font color, borders, conditional formatting, and icon sets/data bars/color scales when available.
   - If color, highlight, or icon formatting encodes status, risk, pass/fail, accept/reject, priority, or inspection result, output a semantic matrix/table.
   - Do not treat a CSV value table as complete evidence when the workbook uses color or conditional formatting to encode meaning.
   - If the meaning of colors cannot be inferred from legends/nearby labels, mark `visual_format_review_required=yes`.

8. Extract high-value semantic findings.
   - Defect-grade tables: detect `CR` / `MA` / `MI` header columns and count rows marked with `?` under each grade. Preserve item name, inherited parent item, description, method/tool, grade, and row/sheet evidence.
   - Equipment and fixtures: extract every tool, fixture, jig, and test device from `??????`, `????`, nearby images, and operation text. Include model-like IDs such as `P03PXXXXXX`, `M0MIXXXXXX`, `S0N9XXXXXX`, `B080XXXXXX`.
   - Operation procedures: preserve ordered steps exactly, especially button sequences, long-press durations, screen states, wait times, and pass criteria.
   - Screen icons/symbols: if a workbook contains small LCD screenshots or symbols, crop/upscale if needed and describe the visible symbol in text. Example: low-battery is an empty horizontal battery icon with a right-side nub.
   - Version/document metadata: extract document number, version, effective date, controlled form number, sheet-specific procedure number, and do not rely on the filename alone.

9. Assign conversion loss risk.
   - `high`: formulas, OLE objects, embedded images, hidden sheets/rows/columns, or color-coded meaning may be missing.
   - `high`: workbook contains conditional formatting or visual status/risk/pass-fail semantics not represented in Markdown/CSV.
   - `medium`: merged cells, large tables, image anchoring, formula cached values, visual mapping, defect-grade tick columns, operation steps, or symbol images need confirmation.
   - `low`: tables, formulas, images, structure, and visual semantics are represented or not present.

10. Assign readiness.
   - `ai_ready`: table content readable and no high/medium conversion loss risk.
   - `partial`: readable but any conversion loss risk remains.
   - `blocked`: source cannot be opened or conversion failed.

## Prompt Template

```text
You are converting Excel .xls/.xlsx DHF/DMR evidence into AI-readable Markdown.

Do not only check whether CSV/Markdown has cell values. Check whether the workbook lost source information.

For each Excel file:
1. Resolve the real source path with Path.exists/Test-Path.
2. Convert .xls -> .xlsx with Excel COM when needed.
3. Export every visible sheet to CSV and manageable Markdown.
4. Preserve workbook metadata in the Markdown header.
5. Export relevant sheet pages to PDF/PNG and create page visual Markdown when layout carries meaning.
6. Extract all embedded images with sheet name, anchor cell, nearby text, OCR, and review page.
7. Inspect formulas, cached values, merged cells, hidden sheets/rows/columns, filters, comments, hyperlinks, charts, OLE objects, and visual formatting.
8. If colors/conditional formatting/icons define a matrix or category, output a semantic mapping.
9. Extract semantic findings such as defect-grade counts, tool/fixture lists, operation steps, screen symbol meanings, and document metadata.
10. Output high/medium/low conversion loss risk.
11. Mark high and medium risk files as partial, not ai_ready.
```

## Learned Lessons From PT9L

- Excel images can be real DHF/DMR evidence: inspection diagrams, process photos, labels, packaging, drawings, test equipment, and signatures.
- Extracted image order is not enough. Always record sheet name, anchor cell, nearby text, OCR text, and inferred evidence value.
- WMF/EMF images in Excel may be dropped by `openpyxl`; this is not a successful image conversion. Use Excel COM export/screenshot fallback or mark the file high risk.
- Material brand/model/specification may exist only in an embedded image label, even when the sheet cell says only a generic name. In PT9L `????`, the table says `???`, but the image label shows `Conformal Coating` and model-like text `PU1030-40S`. Always inspect images before answering material/spec questions.
- Form numbers and document numbers can be stored outside normal cells. In PT9L `?????E0.xls`, the performance sheet shows `???QR-7.3-01/E0` in the upper-right header/textbox area; normal CSV/Markdown extraction missed it. Extract Excel headers/footers and shape text with Excel COM.
- Image OCR must include small top-label text when the photo is a material label; use crop/upscale OCR if the first pass misses model strings such as `PU1030-40S`.
- Process-area answers need combined evidence from operation text, requirement text, and images. For example, a coating operation can say `sensor board surface`, while the requirement says it must fully cover the four sensor solder joints.
- Defect-grade tables can encode the answer by check marks under `CR` / `MA` / `MI`, not by repeating the grade text on each row. Count the tick marks by grade and carry parent item labels downward when rows omit the item name.
- Fixture/tool questions require cross-sheet deduplication. In PT9L DMR, battery fixtures, screw fixtures, spring welding fixtures, brightness fixtures, blackbody fixtures, and machine-core test fixtures appear across different workbooks/sheets.
- Screen-symbol questions require image review, not only text. In PT9L low-battery inspection, the low-battery symbol is an empty horizontal battery icon with a small nub on the right.
- Operation-step answers need button names and timing. In PT9L clear-memory inspection, the evidence is power-off state + long press measurement key + setting key for 8 seconds + `M` and `DEL` flash + `M` disappears after about 2 seconds.
- Color-difference requirements may appear in multiple sections: numeric delta E <= 0.8, visual not obvious, same gloss as sample, PANTONE difference limits, and assembly color difference between parts.
- Excel sheet page export is required for layout questions. In PT9L `????1`, the embedded photo and shape labels (`????????`, `????`, `??`, `???`) are separate Excel objects; only the exported sheet page preserved their relative positions.
- Treat page visual MD and Excel structured MD as parallel evidence. Use page visual MD for "where is it / what does it look like"; use structured MD/manifests for formulas, counts, metadata, hidden sheets, and exact cell content.
- A workbook can look readable as CSV while losing formulas, merged headers, hidden sheets, conditional formatting, and color-coded decisions.
- Color/highlight can be the data. Use the same principle learned from Word risk matrices: if black/white/red/green cells mean `acceptable`, `not acceptable`, `pass`, `fail`, or risk level, extract the per-cell meaning.
- For `.xls`, the first risk is the initial conversion to `.xlsx`; record the method and mark review if conversion changes sheet/image/formula behavior.
- Chinese path display in terminal can be mojibake and must not be trusted.
