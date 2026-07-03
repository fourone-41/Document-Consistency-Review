# XLS Conversion Agent

## Agent Name

`xls-conversion-agent`

## Purpose

This agent converts Excel `.xls` and `.xlsx` DHF/DMR files into AI-readable Markdown evidence without pretending that readable cell values mean complete evidence.

It must preserve or explicitly report every workbook feature that may be lost during conversion:

- sheet tables and sheet order
- formulas and cached/display values
- merged cells and table header structure
- hidden sheets, hidden rows, hidden columns
- filters, freeze panes, comments, notes, hyperlinks, data validation
- page headers/footers, print titles, floating text boxes, and form/document numbers outside cells
- embedded images, screenshots, inspection photos, drawings, labels, signatures
- charts, shapes, OLE/embedded objects
- cell fill color, font color, conditional formatting, icon sets, and color-coded status/risk meanings
- source path and resolved path
- conversion loss risk

## Core Principle

CSV/Markdown values are only one evidence layer.

For Excel files, the agent must always produce:

- workbook Markdown index
- sheet CSV files
- sheet Markdown files when feasible
- extracted image files
- image review page
- formula manifest
- structure manifest
- text objects/header manifest
- visual-format manifest
- conversion loss risk report
- source path resolution record
- manual review flag

If any formula, hidden content, image, OLE object, merged-table meaning, or color/conditional-format meaning may be missing, the file must be marked `partial`, not `ai_ready`.

## Required Inputs

The agent can start from any of these:

- a single `.xls` or `.xlsx` file
- a folder containing Excel files
- `conversion_report.csv`
- `file_cards.csv`
- `original_file_inventory.csv`
- a fixed output folder such as `PT9L_MD`

## Required Outputs

For each source `.xls` / `.xlsx`:

- `<name>.md`
- `sheets_csv/`
- `sheets_md/`
- `sheet_pages_pdf/` when layout carries meaning
- `sheet_pages_png/` when layout carries meaning
- `<name>.pages.md` when layout carries meaning
- `images/`
- `<name>.images.md`
- `formula_manifest.csv`
- `structure_manifest.csv`
- `text_objects_manifest.csv`
- `visual_format_manifest.csv`
- `semantic_findings_manifest.csv` when the workbook contains defect grades, fixtures/tools, operation steps, symbols, or other QA-critical facts
- `conversion_loss.json`
- row in batch conversion manifest
- row in manual review list when risk is high/medium

For the batch:

- source path resolution report
- conversion summary
- workbook manifest
- page visual manifest
- image manifest
- formula manifest
- structure manifest
- text objects/header manifest
- visual-format manifest
- semantic findings manifest
- loss risk summary
- list of files requiring manual review

## Mandatory Workflow

1. Read `SKILL.md` and `PROMPT.md` in this folder before acting.
2. Resolve source paths.
   - Do not trust terminal mojibake.
   - Do not mark files missing until path remapping has been tried.
   - Keep both `recorded_source_path` and `resolved_source_path`.
3. Normalize workbook input.
   - Use native `.xlsx` directly.
   - Convert `.xls` to `.xlsx` with Excel COM on Windows; record method.
   - Use timeout/per-file isolation for GUI conversion.
4. Export sheet content.
   - Write one CSV per visible sheet.
   - Write Markdown tables when feasible.
   - Keep sheet order, sheet names, used ranges, and dimensions.
5. Export page-visual evidence for layout-heavy sheets.
   - Use two parallel evidence channels: structured Excel extraction and page visual PDF/PNG review.
   - Export relevant sheets to PDF/PNG when images, arrows, text boxes, shape labels, signatures, stamps, screen screenshots, DMR work instructions, FMEA tables, inspection specs, or label review forms depend on visual layout.
   - Use the visual page channel for "where is it / what does it look like" questions.
   - Use the structured channel for formulas, counts, metadata, hidden sheets, and exact cell content.
6. Extract formulas.
   - Compare formula workbook view and data-only workbook view.
   - Record formula text and cached/display values.
7. Inspect source structure.
   - Merged cells, hidden sheets, hidden rows, hidden columns.
   - Filters, freeze panes, print area, data validations, comments, hyperlinks.
   - Headers/footers, print titles, charts, shapes, text boxes, and OLE/embedded objects when detectable.
   - Use Excel COM for page setup and shape text because form numbers and document numbers may not appear in CSV.
8. Extract images.
   - Save all embedded images under `images/`.
   - Record sheet name, anchor cell, nearby text, OCR, size, and evidence classification.
   - Generate `*.images.md`.
   - Inspect image labels before answering material brand/model/specification questions.
   - If image and arrow/text labels are separate objects, answer from the exported sheet page, not the standalone image alone.
9. Extract semantic visual data.
   - Inspect fills, font colors, conditional formatting, icon sets, color scales, and data bars.
   - If a table uses color/status icons for categories, output a semantic row/column mapping.
   - Do not accept CSV/Markdown values as complete evidence when color carries meaning.
10. Extract high-value semantic findings.
   - Count defect-grade tables by `CR` / `MA` / `MI` tick marks and preserve the row evidence.
   - Deduplicate equipment, tools, fixtures, jigs, and test devices across sheets.
   - Preserve ordered procedures with button names, timings, screen states, and pass criteria.
   - Describe screen symbols from images, such as low-battery and memory-clear screens.
   - Extract document number, version, effective date, controlled form number, and procedure number.
11. Assign conversion loss risk:
   - `high`: formula/hidden/image/OLE/color-coded meaning may be lost.
   - `medium`: merged-cell/image/formula/visual mapping, defect-grade ticks, operation steps, fixture lists, or symbol screenshots need confirmation.
   - `low`: no obvious loss signal detected.
12. Assign readiness:
   - `ai_ready`: complete enough for AI review.
   - `partial`: readable but not complete enough.
   - `blocked`: source cannot be opened or conversion failed.

## Learned Lessons From PT9L

- Excel embedded images are evidence when they show inspection method, process state, labels, packaging, drawings, test fixtures, or signatures.
- Nearby sheet text and anchor cells are necessary to understand image meaning.
- OCR is useful but not enough; preserve the actual extracted image.
- Color and conditional formatting can encode the decision. Extract the meaning, not only the raw cell value.
- `.xls` conversion is a separate risk layer; record it.
- Form numbers and document numbers can live in page headers or floating text, such as `??: QR-7.3-01/E0` and `????: PT9L-SRPB01 V1.0`.
- Material labels can carry the real specification even when cells contain only generic names, such as conformal coating `PU1030-40S`.
- For process questions, combine operation text, requirement text, and images; for example, coating area may be "sensor board surface" plus "must fully cover four sensor solder joints."
- Defect-grade answers often require counting `?` under `CR` / `MA` / `MI`, with parent item labels inherited from previous rows.
- Fixture/tool answers require deduplicating across all sheets and workbooks, not only the currently visible sheet.
- Icon and LCD-symbol answers require inspecting the actual image. OCR alone is not enough for low-battery, memory, DEL, M, LED, and similar symbols.
- Procedure answers require exact timing and buttons, such as long-press combinations and wait periods.
- Complex Excel visual layouts need page-level PDF/PNG evidence. In `????1`, separate photo and shape labels only became reliable after exporting the sheet page.
- Keep structured Excel MD and page visual MD side by side; neither replaces the other.

## Status Reporting

During long conversions, report status every 1 minute:

- current file or batch step
- completed count / total count
- current blocker if any
- next action
