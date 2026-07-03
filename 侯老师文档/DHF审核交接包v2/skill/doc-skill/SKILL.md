---
name: doc-skill
description: Legacy Word `.doc` to AI-readable Markdown workflow for DHF/DMR evidence. Use when converting, auditing, sampling, or reviewing old Word `.doc` files, especially files with tables, checkbox states, embedded Excel/OLE objects, signatures, or approval forms.
---

# DOC Skill: Word DOC -> AI-Readable Markdown

## Agent Entry

For a dedicated DOC conversion agent, use:

- `AGENT.md`: agent role, workflow, learned lessons, and required outputs.
- `AGENT_PROMPT.md`: copyable startup prompt for a new agent.
- `PROMPT.md`: short task prompt for DOC conversion/audit.

## Goal

Convert every legacy Word `.doc` file into evidence that AI can read as completely as possible, while explicitly flagging anything that Markdown may lose.

`Readable Markdown` is not enough. The output must preserve or report:

- source file path and file name
- conversion method
- paragraph text
- table content and table structure
- checkbox/checkmark state
- Word form fields and content controls
- embedded Excel/OLE objects
- pictures/signature/approval blocks
- safety icons and standard symbols, including color and meaning
- table cell shading, text highlight, background color, and color-coded risk/status meaning
- page-level PDF/PNG visual snapshots for layout-dependent evidence
- page headers/footers, especially file number, form number, version, title, and page count
- conversion loss risks

## Required Output Per DOC File

For every `.doc`, produce:

- `<name>.markitdown.md`: Markdown text converted through Word/LibreOffice -> DOCX -> MarkItDown.
- `pages_pdf/`: document PDF export or page-level PDF evidence.
- `pages_png/`: rendered page snapshots for visual review.
- `<name>.pages.md`: page visual review Markdown linking PDF/PNG pages.
- `page_manifest.csv`: page number, PDF/PNG path, render method, and visual-review reason.
- `images/`: every embedded Word image extracted as a standalone file.
- `<name>.image_manifest.csv` or CSV row: image file path, source DOC, image order, and whether Markdown references it.
- `<name>.visual_format_manifest.csv` or CSV row when colors/highlights carry meaning.
- `word_header_footer_text.txt` and/or `header_footer_manifest.csv`: all section headers/footers, including primary, first-page, and even-page variants.
- `<name>.loss.json` or CSV row: source inspection result for checkboxes, form fields, OLE objects, tables, images, and shapes.
- Manual review flag: `yes` unless conversion loss risk is proven low.
- Source metadata at top of Markdown:
  - `source_file`
  - `resolved_source_path`
  - `source_file_name`
  - `source_type`
  - `conversion_method`
  - `converted_at`
  - `manual_review_required`

## Conversion Workflow

0. Check conversion toolkit readiness.
   - Read `D:\AI_0415\03DHF\skill\conversion-toolkit-skill\SKILL.md`.
   - Run `python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py" --install`.
   - Do not start DOC conversion until Python packages, Word COM, Tesseract with `chi_sim`, `eng`, `osd`, and required conversion tools are ready or missing-tool risk is explicitly reported.

0.5. Run the batch conversion gate before full DOC conversion.
   - Convert only 3 representative `.doc` files first. If fewer than 3 DOC files exist, convert all DOC files.
   - Inspect the sample Markdown, page PNG/PDF renders, image extraction, form/checkbox/OLE checks, manifests, and `conversion_loss` records.
   - The gate fails if any sample has blocked opening, empty/garbled Markdown, mojibake paths, missing page visuals, missing embedded images, wrong source metadata, or unhandled exceptions.
   - Record sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
   - Run the full DOC batch only after the sample gate passes. If it fails, fix the converter/tooling and rerun the sample gate first.

1. Resolve source path.
   - If the old inventory path contains an extra wrapper folder such as `PT9L-DHF -[Chinese wrapper name]`, try removing that wrapper and verify with `Path.exists()` / `Test-Path`.
   - Do not mark a file missing until alternate path resolution has been tried.
   - Do not trust terminal mojibake. Chinese names shown as `???` or garbled text in shell output are display artifacts unless `Path.exists()` also fails.
   - Keep both `recorded_source_path` and `resolved_source_path` in reports.
   - In scripts, avoid hardcoding Chinese path literals. Use CSV input, `Path.parts`, or Unicode escapes for known Chinese constants.

2. Convert `.doc` to `.docx`.
   - Prefer LibreOffice CLI when stable.
   - Use Microsoft Word COM as fallback on Windows.
   - Run with timeout or per-file subprocess so one bad file cannot block the batch.

3. Convert `.docx` to Markdown.
   - Use Microsoft MarkItDown for primary Markdown conversion.
   - Keep MarkItDown output as text evidence, not as proof of completeness.
   - If Markdown contains `data:image/...base64...` placeholders or missing image data, this is not acceptable as final evidence.

3.1. Extract Word headers and footers.
   - Use Word COM on Windows to inspect every section's `Headers` and `Footers`, including primary, first-page, and even-page variants.
   - File numbers, form numbers, versions, titles, and page counts often live only in headers/footers and may be absent from MarkItDown Markdown.
   - Write `word_header_footer_text.txt` and/or `header_footer_manifest.csv` under the assets folder.
   - During DHF list checks, count a file number as found if it appears in header/footer text, even when body Markdown does not contain it.
   - Do not report `doc_no_not_found` for Word files until headers/footers and page visual evidence have been checked.

3.2. Create page-visual evidence when layout can carry meaning.
   - Legacy Word evidence must use two parallel channels:
     - Structured channel: Markdown text, tables, extracted images, form fields, content controls, OLE, visual-format manifests.
     - Page visual channel: export the original or converted Word document/pages to PDF/PNG and create a page visual Markdown review file.
   - Use the page visual channel for signatures, stamps, approval blocks, page headers/footers, floating text boxes, arrows, callouts, diagrams, complex tables, image captions/labels, safety symbols, print-layout forms, and any question about "where/what does it look like".
   - Do not replace DOC/DOCX inspection with PDF. Use both: PDF/PNG preserves human-visible layout and relative positions; DOC/DOCX inspection preserves text, fields, object metadata, OLE, tables, and formatting semantics where available.
   - Preserve page number, PDF path, PNG path, render method, and visual-review reason in a page manifest.

4. Extract embedded images.
   - Extract images from the converted `.docx` package under `word/media`.
   - Save every image as a standalone file under an `images/` folder.
   - Replace Markdown image placeholders with relative links to those extracted files.
   - If image order cannot be mapped perfectly, preserve all images and mark `image_mapping_review_required=yes`.
   - Do not rely only on extracted image order for semantic placement. Image order can be different from visual document order.
   - Safety icons and standard symbols must be identified independently by shape/color/nearby text.
   - Standard icon sections require explicit icon-to-meaning mapping, not only image extraction.
   - If images, labels, arrows, and text boxes are separate Word objects, standalone image extraction is incomplete. Export the whole page to PDF/PNG and answer from the combined page view.

5. Inspect source document directly.
   - Count Word tables.
   - Count form fields.
   - Count checkbox form fields and checked states.
   - Count content controls.
   - Count inline shapes and floating shapes.
   - Count embedded OLE objects / embedded spreadsheets.
   - Count checkmark-like characters.
   - Check whether nearby tables/lists after headings or explanatory sentences are preserved.
   - Do not answer a sentence in isolation when the source has a following table or list that completes the meaning.
   - Detect safety/standard icons and record their color, shape, nearby label, and meaning.
   - For each standard icon, pair the extracted icon image with its adjacent explanation text. If the Markdown has a `data:image...` placeholder or image order mismatch, mark `icon_mapping_review_required=yes`.
   - Inspect visual formatting that carries meaning: table cell shading, text highlight, paragraph/range shading, font color, and shape-filled cells.
   - Use Word COM when XML or Markdown is insufficient. Check `Cell.Shading`, `Range.Shading`, `Paragraph.Shading`, `Range.HighlightColorIndex`, font color, and nearby shapes/images.
   - If a risk/status matrix uses black/white or colored blocks to mean categories such as `Not acceptable` / `Acceptable`, extract a semantic matrix that maps every row/column cell to its meaning.
   - Do not treat an empty Markdown table plus a legend image as complete evidence. The legend is not enough unless each colored cell position is also captured.

6. Compare source signals against Markdown.
   - If source has checkbox/form fields but Markdown does not explicitly show state, mark `conversion_loss_high_risk`.
   - If source has embedded OLE/Excel objects, mark `conversion_loss_high_risk`.
   - If source has color/highlight-coded acceptance, status, pass/fail, risk, priority, or classification but Markdown does not explicitly preserve the per-cell meaning, mark `conversion_loss_high_risk`.
   - If source has tables but Markdown tables are not obvious, mark `conversion_loss_medium_risk`.
   - If source has inline/floating shapes or color blocks, mark at least `conversion_loss_medium_risk` unless separately extracted and semantically mapped.

7. Only then assign readiness.
   - `ai_ready`: text readable and no high/medium conversion loss risk.
   - `partial`: text readable but any conversion loss risk remains.
   - `blocked`: source cannot be opened or conversion failed.

## Prompt Template

Use this prompt when asking an AI agent to convert or audit DOC files:

```text
You are converting legacy Word .doc DHF/DMR evidence into AI-readable Markdown.

Do not only check whether Markdown has text. Check whether the conversion lost source information.

For each .doc file:
1. Resolve the real source path. If the recorded path fails, try known path remaps before calling it missing.
2. Convert .doc -> .docx using LibreOffice or Word COM with timeout.
3. Convert .docx -> Markdown using MarkItDown.
4. Preserve source metadata in the Markdown header.
5. Export pages to PDF/PNG and create page visual Markdown when layout carries meaning.
6. Inspect the original Word source for:
   - tables
   - checkbox states
   - Word form fields
   - content controls
   - checkmark symbols
   - inline/floating images
   - embedded OLE or Excel objects
   - visual formatting that carries meaning: table shading, text highlight, font color, and colored shapes
7. If labels/arrows/text boxes are separate Word objects from images, answer from the exported page snapshot.
8. If colors/highlights define a matrix or category, output a semantic matrix.
9. Compare source signals to Markdown/images/page snapshots.
10. Output a conversion loss risk level: high / medium / low.
11. Mark high and medium risk files as partial, not ai_ready.

Final output must include:
- Markdown file path
- page visual Markdown/PDF/PNG paths when applicable
- source file path
- conversion method
- loss risk reason
- manual review required yes/no
```

## Current PT9L Scripts

Use these existing project scripts as the starting point:

- `recover_word_with_markitdown.py`
- `markitdown_word_recovery_report.csv`
- `audit_word_conversion_loss.py`
- `conversion_loss_risk_report.csv`
- `build_ai_readiness_report.py`
- `build_knowledge_layer.py`

## Review Rule

If a user says "the MD looks readable but something from the DOC may be missing", treat that as valid. Re-check source objects and do not dismiss the concern.

If a user asks about a sentence from a manual or procedure, inspect the surrounding context before answering. A sentence can depend on the table immediately below it. For example, `Use only accessories provided by the original manufacturer...` under `Box contents` must be read together with the accessory table: thermometer, AAA batteries, and user manual.

If a user asks about an icon, inspect the icon image itself. Safety icons can carry meaning through shape and color. For example, a yellow triangle with an exclamation mark means warning; this must be preserved as icon evidence, not reduced to plain text only.

Standard icons must be mapped by visual symbol plus adjacent text. For example, a black factory silhouette means `Manufacturer`; it may appear as a separate extracted image even when the Markdown line still has a `data:image...` placeholder.

If a table uses color, shading, highlight, or filled shapes to encode meaning, treat that formatting as source data. For example, in PT9L Risk Management Plan section `3.3 Risk Acceptance Criteria`, the Markdown preserved the labels and the `Not acceptable` / `Acceptable` legend images but lost which matrix cells were black/white. Word COM showed the black cells through `Range.HighlightColorIndex=1`, not ordinary DOCX `w:shd` cell shading. For `.doc` and converted `.docx`, check `Cell.Shading`, `Range.Shading`, `Paragraph.Shading`, `Range.HighlightColorIndex`, font color, and nearby shapes/images; output a structured matrix and mark the file `partial` if Markdown does not preserve the per-cell meaning.

If Word layout carries meaning, export page-level PDF/PNG evidence. Use page visual MD for signatures, stamps, page headers/footers, arrows, callouts, floating text boxes, diagrams, and complex approval forms. Keep page visual MD and structured Word MD as parallel evidence; neither replaces the other.
