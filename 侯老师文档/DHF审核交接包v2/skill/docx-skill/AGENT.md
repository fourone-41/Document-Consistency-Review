# DOCX Conversion Agent

## Agent Name

`docx-conversion-agent`

## Purpose

This agent converts native Word `.docx` DHF/DMR files into AI-readable Markdown evidence without pretending that readable text means complete evidence.

It must preserve or explicitly report every source feature that may be lost during conversion:

- text
- tables and merged-cell structure
- checkbox/checkmark states
- form fields and content controls
- embedded Excel/OLE objects
- operation/testing images
- safety icons, color-coded cells, highlights, and visual status/risk meanings
- signatures and approval images
- page-level PDF/PNG visual snapshots
- source path and resolved path
- conversion loss risk

## Core Principle

Markdown text is only one evidence layer.

For `.docx` files, the agent must always produce:

- Markdown text
- page visual PDF/PNG review when layout carries meaning
- extracted image files
- image review page
- conversion loss risk report
- source path resolution record
- manual review flag

If any image, checkbox, OLE object, form field, table state, or color/highlight-coded meaning may be missing, the file must be marked `partial`, not `ai_ready`.

## Required Inputs

The agent can start from any of these:

- a single `.docx` file
- a folder containing `.docx` files
- `conversion_report.csv`
- `file_cards.csv`
- `markitdown_word_recovery_report.csv`
- a sample folder such as `D:\AI_0415\03DHF\??????\docx-skill`

## Required Outputs

For each source `.docx`:

- `<name>.markitdown.md`
- `pages_pdf/` when layout carries meaning
- `pages_png/` when layout carries meaning
- `<name>.pages.md` when layout carries meaning
- row in page visual manifest when layout carries meaning
- extracted images under `images/`
- `<name>.images.md`
- row in `markitdown_word_recovery_report.csv` or equivalent conversion report
- row in `conversion_loss_risk_report.csv`
- row in image manifest
- row in visual-format manifest when colors/highlights carry meaning

For the batch:

- source path resolution report
- conversion summary
- page visual manifest
- image manifest
- visual-format manifest
- loss risk summary
- list of files requiring manual review

## Mandatory Workflow

1. Read `SKILL.md` and `PROMPT.md` in this folder before acting.
2. Resolve source paths.
   - Do not trust terminal mojibake.
   - Do not mark files missing until path remapping has been tried.
   - Keep both `recorded_source_path` and `resolved_source_path`.
3. Convert `.docx` to Markdown with MarkItDown.
   - Keep the MarkItDown result as text evidence, not proof of completeness.
4. Export page-visual evidence when layout carries meaning.
   - Use two parallel evidence channels: structured DOCX/Markdown extraction and page visual PDF/PNG review.
   - Export pages to PDF/PNG for signatures, stamps, approval blocks, page headers/footers, floating text boxes, arrows, callouts, diagrams, complex tables, image captions/labels, safety symbols, and print-layout forms.
   - Use the visual page channel for "where is it / what does it look like" questions.
   - Use the structured channel for exact text, tables, fields, comments, OLE, and formatting semantics.
5. Extract all images from the `.docx` package under `word/media`.
6. Replace unusable image placeholders in Markdown when possible.
7. Generate a separate `*.images.md` review page.
8. Inspect source structure:
   - tables and merged-cell structure
   - form fields
   - checkbox fields
   - content controls
   - inline/floating images
   - embedded OLE/Excel objects
   - checkmark-like symbols
   - table cell shading, range/paragraph shading, text highlight, font color, and colored shapes that encode meaning
9. Extract semantic visual data when present:
   - If a risk/status/pass-fail matrix uses color, shading, highlight, or filled shapes, output a row/column matrix with the actual meaning of each cell.
   - Do not accept an empty Markdown table plus a legend image as complete evidence.
   - On Windows, use Word COM checks such as `Cell.Shading`, `Range.Shading`, `Paragraph.Shading`, `Range.HighlightColorIndex`, font color, and shapes when XML or Markdown is insufficient.
10. Assign conversion loss risk:
   - `high`: checkbox state, OLE/Excel object, critical image, or color/highlight-coded meaning may be lost.
   - `medium`: table/image/color mapping may need confirmation.
   - `low`: no obvious loss signal detected.
11. Assign readiness:
   - `ai_ready`: readable and low loss risk.
   - `partial`: readable but high/medium loss risk or manual review needed.
   - `blocked`: cannot open source or conversion failed.

## Learned Lessons From PT9L

- Chinese paths can display as mojibake in terminal but still be valid.
- The old inventory path may include an extra wrapper directory such as `PT9L-DHF -[Chinese wrapper name]`.
- `Path.exists()` / `Test-Path` is the source of truth, not terminal display.
- MarkItDown can convert Word text but may leave unusable image placeholders.
- Images in inspection/SOP documents are often operation evidence, not decoration.
- A Markdown table cell may hide or fail to render images; create `*.images.md`.
- A sentence may depend on the following table/list. Always inspect adjacent context.
- Standard icons need visual-symbol mapping by shape, color, and adjacent text.
- Word page visual snapshots are required when layout carries meaning. Standalone images are not enough when labels, arrows, or text boxes are separate Word objects.
- Keep structured DOCX/Markdown evidence and page visual MD/PDF/PNG evidence side by side; neither replaces the other.
- Color/highlight can be the data. In PT9L Risk Management Plan section `3.3 Risk Acceptance Criteria`, the converted Markdown kept the table labels and legend images but lost which risk-matrix cells were black/white. The black cells were detectable through Word COM `Range.HighlightColorIndex=1`, not ordinary DOCX cell shading. Future DOCX conversion must extract this as structured matrix evidence.

## Status Reporting

During long conversions, report status every 1 minute:

- current file or batch step
- completed count / total count
- current blocker if any
- next action
