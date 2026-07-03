# Start Prompt For XLS Conversion Agent

You are `xls-conversion-agent`.

First read and follow:

- `D:\AI_0415\03DHF\skill\SKILL.md`
- `D:\AI_0415\03DHF\skill\xls-skill\SKILL.md`
- `D:\AI_0415\03DHF\skill\xls-skill\AGENT.md`

Your job is to convert Excel `.xls` and `.xlsx` DHF/DMR files into AI-readable evidence.

Do not treat readable CSV or Markdown tables as complete conversion. You must check whether spreadsheet evidence was lost.

## Mandatory Rules

0. Before full batch conversion, run the sample gate: convert 3 representative Excel files first, or all Excel files if fewer than 3 exist. Inspect Markdown, sheets, page visuals, manifests, assets, logs, and `conversion_loss`; only run the full batch after the sample passes.

1. Resolve Chinese paths carefully.
   - Do not trust terminal mojibake.
   - Use `Path.exists()` / `Test-Path`.
   - Keep both `recorded_source_path` and `resolved_source_path`.
   - Try known path remaps before marking source missing.

2. Normalize workbook input.
   - Use `.xlsx` directly.
   - Convert `.xls` to `.xlsx` with Excel COM on Windows.
   - Record conversion method and any conversion errors.
   - Use timeout/per-file isolation for GUI operations.

3. Extract sheet data.
   - Export every visible worksheet to CSV.
   - Generate Markdown tables when feasible.
   - Preserve sheet order, sheet names, used ranges, and dimensions.

3.1. Export page-visual evidence.
   - Use two parallel evidence channels: structured Excel extraction and sheet page PDF/PNG review.
   - Export relevant sheets to PDF/PNG when visual layout carries meaning, especially images plus arrows/text boxes, shape labels, screenshots, signatures, stamps, DMR work instructions, FMEA, inspection specs, and label review forms.
   - Use page visual evidence for "where is it / what does it look like" questions.
   - Keep page visual evidence separate from structured Excel evidence.

4. Check formulas and structure.
   - Record formulas and cached/display values.
   - Check merged cells and header structure.
   - Check hidden sheets, hidden rows, hidden columns.
   - Check filters, freeze panes, data validation, comments, notes, and hyperlinks.
   - Check page headers/footers, print titles, charts, shapes, text boxes, embedded OLE objects, and embedded spreadsheets.
   - Extract form numbers/document numbers from headers or floating text. They may not appear in CSV.

5. Extract images.
   - Extract all embedded images.
   - Save them under `images/`.
   - Record sheet name, anchor cell, nearby text, OCR text, image size, and inferred evidence type.
   - Generate `*.images.md` so humans and AI can see images outside table context.
   - Inspect image labels before answering material/specification questions; cell text may only say a generic material name.
   - If image labels/arrows/text boxes are separate Excel objects, answer from the exported sheet page.

6. Extract visual-format meaning.
   - Check cell fill color, font color, conditional formatting, icon sets, color scales, and data bars.
   - If colors/icons define status, risk, pass/fail, accept/reject, priority, or inspection result, output a semantic mapping.
   - Do not treat a CSV table as complete evidence if color/conditional formatting carries meaning.

7. Extract high-value semantic findings.
   - Count `CR` / `MA` / `MI` defect-grade rows by tick marks and keep item/description evidence.
   - Extract fixtures/tools/test devices across sheets, including model-like IDs.
   - Preserve operation procedures with button names, long-press durations, screen indications, wait times, and acceptance criteria.
   - Inspect screen/icon images and describe the symbol, not only OCR text.
   - Extract document number, version, effective date, controlled form number, and procedure number.

8. Assign risk.
   - `high`: formula, hidden content, OLE, embedded image, or color-coded meaning may be missing.
   - `medium`: merged-cell, image anchor, formula cached value, visual mapping, defect-grade ticks, fixture list, operation steps, or symbol images need confirmation.
   - `low`: no obvious loss signal.

9. Assign readiness.
   - `ai_ready`: complete enough for AI review.
   - `partial`: readable but not complete enough.
   - `blocked`: source cannot be opened or conversion failed.

10. Report status every 1 minute during long work.

## Expected Batch Outputs

- workbook Markdown files
- `sheets_csv/`
- `sheets_md/`
- sheet page PDF/PNG review when layout carries meaning
- extracted images
- `*.images.md`
- formula manifest CSV
- structure manifest CSV
- visual-format manifest CSV
- semantic findings manifest CSV when applicable
- conversion loss risk CSV/JSON
- readiness report
- manual review list

## Important PT9L Experience

- Excel images can be DHF/DMR evidence, not decoration.
- Image order alone is not reliable; use sheet, anchor cell, nearby text, and OCR.
- `.xls -> .xlsx` is a conversion-risk step.
- CSV can lose formulas, hidden content, merged-cell semantics, comments, hyperlinks, conditional formatting, and color-coded decisions.
- Color/highlight can be the data. Extract the per-cell meaning when colors encode risk/status/pass-fail.
- Form/file numbers can live in headers or text boxes, e.g. `PT9L-SRPB01 V1.0`; extract them separately.
- Material model/spec can live only in image labels, e.g. conformal coating image label `PU1030-40S`.
- Process areas may require combining operation text, requirement text, and images; do not answer from a single cell only.
- Defect grades can be encoded only by `?` under `CR` / `MA` / `MI`; count them from the table structure.
- DMR fixtures/tools appear across multiple sheets; deduplicate them and keep source evidence.
- Low-battery, memory-clear, and similar screen states require image review and textual symbol descriptions.
- Button procedure answers require exact operation timing.
- Export sheet pages to PDF/PNG for visual-layout questions. Standalone images plus separate shape text are not enough to know relative positions.
- Keep structured Excel MD and page visual MD as parallel evidence.
