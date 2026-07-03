---
name: docx-skill
description: Word `.docx` to AI-readable Markdown workflow for DHF/DMR evidence. Use when converting, auditing, sampling, or reviewing `.docx` files with tables, images, checkbox states, form fields, embedded Excel/OLE objects, signatures, or approval forms.
---

# DOCX Skill: Word DOCX -> AI-Readable Markdown

## Agent Entry

For a dedicated DOCX conversion agent, use:

- `AGENT.md`: agent role, workflow, learned lessons, and required outputs.
- `AGENT_PROMPT.md`: copyable startup prompt for a new agent.
- `PROMPT.md`: short task prompt for DOCX conversion/audit.

## Goal

Convert every Word `.docx` file into AI-readable evidence without losing source meaning.

Readable Markdown is not enough. The output must preserve or report:

- source file path and resolved path
- Markdown text
- Word tables
- checkbox/checkmark state
- Word form fields and content controls
- embedded Excel/OLE objects
- operation/testing images
- safety icons and standard symbols, including color and meaning
- table cell shading, text highlight, background color, and color-coded risk/status meaning
- signatures and approval images
- page-level PDF/PNG visual snapshots for layout-dependent evidence
- page headers/footers, especially file number, form number, version, title, and page count
- conversion loss risk

## Required Output Per DOCX File

- `<name>.markitdown.md`
- `pages_pdf/`: document PDF export or page-level PDF evidence.
- `pages_png/`: rendered page snapshots for visual review.
- `<name>.pages.md`: page visual review Markdown linking PDF/PNG pages.
- `page_manifest.csv`: page number, PDF/PNG path, render method, and visual-review reason.
- extracted images under `images/`
- `<name>.images.md`
- image manifest row
- `word_header_footer_text.txt` and/or `header_footer_manifest.csv`: all section headers/footers, including primary, first-page, and even-page variants.
- semantic visual-format manifest row when colors/highlights carry meaning
- conversion loss risk row
- manual review flag

## Mandatory Workflow

0. Check conversion toolkit readiness.
   - Read `D:\AI_0415\03DHF\skill\conversion-toolkit-skill\SKILL.md`.
   - Run `python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py" --install`.
   - Do not start DOCX conversion until Python packages, Word COM, Tesseract with `chi_sim`, `eng`, `osd`, and required conversion tools are ready or missing-tool risk is explicitly reported.

0.5. Run the batch conversion gate before full DOCX conversion.
   - Convert only 3 representative `.docx` files first. If fewer than 3 DOCX files exist, convert all DOCX files.
   - Inspect the sample Markdown, page PNG/PDF renders, extracted images, form/checkbox/OLE checks, manifests, and `conversion_loss` records.
   - The gate fails if any sample has blocked opening, empty/garbled Markdown, mojibake paths, missing page visuals, missing embedded images, wrong source metadata, or unhandled exceptions.
   - Record sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
   - Run the full DOCX batch only after the sample gate passes. If it fails, fix the converter/tooling and rerun the sample gate first.

1. Resolve source path.
   - Do not trust terminal mojibake.
   - Use `Path.exists()` / `Test-Path`.
   - Keep both `recorded_source_path` and `resolved_source_path`.

2. Convert `.docx` to Markdown.
   - Use Microsoft MarkItDown for primary text conversion.
   - Keep MarkItDown output as text evidence, not proof of completeness.

2.1. Extract Word headers and footers.
   - Use Word COM on Windows to inspect every section's `Headers` and `Footers`, including primary, first-page, and even-page variants.
   - File numbers, form numbers, versions, titles, and page counts often live only in headers/footers and may be absent from MarkItDown Markdown.
   - Write `word_header_footer_text.txt` and/or `header_footer_manifest.csv` under the assets folder.
   - During DHF list checks, count a file number as found if it appears in header/footer text, even when body Markdown does not contain it.
   - Do not report `doc_no_not_found` for Word files until headers/footers and page visual evidence have been checked.

2.2. Create page-visual evidence when layout can carry meaning.
   - Word evidence must use two parallel channels:
     - Structured channel: Markdown text, tables, extracted images, form fields, content controls, OLE, visual-format manifests.
     - Page visual channel: export the document/pages to PDF/PNG and create a page visual Markdown review file.
   - Use the page visual channel for signatures, stamps, approval blocks, page headers/footers, floating text boxes, arrows, callouts, diagrams, complex tables, image captions/labels, safety symbols, print-layout forms, and any question about "where/what does it look like".
   - Do not replace DOCX inspection with PDF. Use both: PDF/PNG preserves human-visible layout and relative positions; DOCX inspection preserves structure, fields, object metadata, hidden/revision data where available, and machine-readable text.
   - Preserve page number, PDF path, PNG path, render method, and visual-review reason in a page manifest.

3. Extract embedded images.
   - Read the `.docx` zip package.
   - Extract all files under `word/media`.
   - Save images under `images/`.
   - Replace unusable Markdown image placeholders if possible.
   - Generate a separate `*.images.md` page that displays all images outside complex tables.
   - Do not rely only on extracted image order for semantic placement. Image order can be different from the visual document order.
   - Safety icons and standard symbols must be identified independently by shape/color/nearby text.
   - Standard icon sections require explicit icon-to-meaning mapping, not only image extraction.
   - If images, labels, arrows, and text boxes are separate Word objects, standalone image extraction is incomplete. Export the whole page to PDF/PNG and answer from the combined page view.

4. Inspect source structure.
   - Count Word tables.
   - Count form fields.
   - Count checkbox fields and checked states.
   - Count content controls.
   - Count inline/floating images.
   - Count embedded OLE or Excel objects.
   - Count checkmark-like characters.
   - Check whether nearby tables/lists after headings or explanatory sentences are preserved.
   - Do not answer a sentence in isolation when the source has a following table or list that completes the meaning.
   - Detect safety/standard icons and record their color, shape, nearby label, and meaning.
   - For each standard icon, pair the extracted icon image with its adjacent explanation text. If the Markdown has a `data:image...` placeholder or image order mismatch, mark `icon_mapping_review_required=yes`.
   - Inspect visual formatting that carries meaning: table cell shading, text highlight, paragraph/range shading, font color, and shape-filled cells.
   - For Word files on Windows, use Word COM when XML or Markdown is insufficient. Check `Cell.Shading`, `Range.Shading`, `Paragraph.Shading`, `Range.HighlightColorIndex`, and nearby shapes/images.
   - If a risk/status matrix uses black/white or colored blocks to mean categories such as `Not acceptable` / `Acceptable`, extract a semantic matrix that maps every row/column cell to its meaning.
   - Do not treat an empty Markdown table plus a legend image as complete evidence. The legend is not enough unless each colored cell position is also captured.

5. Assign conversion loss risk.
   - `high`: checkbox state, OLE/Excel object, or critical image may be missing.
   - `high`: color/highlight-coded acceptance, status, pass/fail, risk, priority, or classification is present in the source but missing from Markdown.
   - `medium`: image/table/color mapping needs confirmation.
   - `low`: no obvious loss signal detected.

6. Assign readiness.
   - `ai_ready`: text readable and low loss risk.
   - `partial`: readable but medium/high loss risk or manual review needed.
   - `blocked`: source cannot be opened or conversion failed.

## Prompt Template

```text
You are converting Word .docx DHF/DMR evidence into AI-readable Markdown.

Do not only check whether Markdown has text. Check whether the conversion lost source information.

For each .docx file:
1. Resolve the real source path with Path.exists/Test-Path.
2. Convert .docx to Markdown using MarkItDown.
3. Preserve source metadata in the Markdown header.
4. Export pages to PDF/PNG and create page visual Markdown when layout carries meaning.
5. Extract all images from word/media into images/.
6. Generate a separate *.images.md review page.
7. Inspect the source DOCX for tables, checkbox states, form fields, content controls, images, OLE/Excel objects, and checkmark symbols.
8. Inspect source visual formatting that carries meaning, including table shading, text highlight, font color, and colored shapes. If colors/highlights define a matrix or category, output a semantic matrix.
9. Output high/medium/low conversion loss risk.
10. Mark high and medium risk files as partial, not ai_ready.
```

## Learned Lessons From DOC Work

- Chinese path display in terminal can be mojibake and must not be trusted.
- Images may explain operation or testing method; they are evidence, not decoration.
- Images inside Markdown tables may not render; always create `*.images.md`.
- Safety icons are evidence. A yellow triangle with an exclamation mark means warning and must not be reduced to plain text without the icon meaning/color.
- Image order replacement can be wrong. For example, the image before `Warning` may map incorrectly unless the icon itself is identified.
- Standard icons must be mapped by visual symbol plus adjacent text. Example: a black factory silhouette means `Manufacturer`; it may appear as a separate extracted image even when the Markdown line still has a `data:image...` placeholder.
- MarkItDown text output is useful but not sufficient.
- Word page export is required when layout matters. Use page visual MD/PDF/PNG for signatures, stamps, page headers/footers, arrows, callouts, floating text boxes, diagrams, and complex approval forms.
- Treat page visual MD and Word structured MD as parallel evidence. Use page visual MD for "where is it / what does it look like"; use structured DOCX/Markdown/manifests for exact text, tables, fields, comments, OLE, and formatting semantics.
- Keep source file, Markdown, images, and risk reports together.
- A sentence can depend on the table immediately below it. For example, `Use only accessories provided by the original manufacturer...` under `Box contents` must be read together with the accessory table: thermometer, AAA batteries, and user manual.
- When answering questions from a converted manual, include the adjacent table/list content if it defines the actual requirement.
- Color/highlight can be the data. In PT9L Risk Management Plan section `3.3 Risk Acceptance Criteria`, the Markdown kept the table labels and legend images but lost which risk-matrix cells were black/white. Word COM showed the black cells were represented by `HighlightColorIndex=1`, not ordinary `w:shd` cell shading. Extract this as structured evidence, e.g. `6 Frequent` and `5 Probable` are all `Not acceptable`; `1 Few` is all `Acceptable`.
- For color-coded tables, check more than one source signal: DOCX XML `w:shd`, Word COM cell/range/paragraph shading, `Range.HighlightColorIndex`, font color, and floating/inline shapes. If any method finds meaningful color not represented in Markdown, mark the file `partial`.
