# PDF Conversion Skill

Use this skill to convert `.pdf` DHF/DMR evidence into AI-readable Markdown and review assets.

## Purpose

PDF files can be born-digital documents, scanned documents, drawings, labels, certificates, reports, or mixed files with a partial text layer. A readable text extraction is not enough. The conversion must preserve page-level source evidence and explicitly report visual or OCR loss.

## PDF Source Types

Classify every PDF before conversion. A batch may contain mixed types:

1. Converted-office PDF.
   - Likely generated from Word, Excel, PPT, or another office file.
   - Native text may exist, but reading order can be wrong because headers, footers, columns, tables, floating text boxes, and page artifacts may be interleaved.
   - Preserve page images and reconstruct logical reading order from layout, not only from raw text extraction order.

2. Image-only report PDF.
   - Pages are scans/photos of reports, certificates, test records, signatures, or stamped documents.
   - Treat rendered page images as the primary evidence and OCR as derived text.
   - Use OCR on full pages plus crop/upscale OCR for title blocks, stamps, signatures, tables, labels, and small result fields.

3. Drawing/CAD/artwork PDF.
   - Pages contain engineering drawings, packaging artwork, labels, diagrams, dimensions, revision tables, BOM/title blocks, and approval blocks.
   - Extract title block fields, drawing number, revision, scale, material, dimensions, tolerances, notes, approvals, and date.
   - Preserve page image at high DPI and mark manual review unless title block, dimensions, and key notes are represented.
   - For schematics, crop/upscale small circuit regions before answering component questions. MCU/IC model, NTC divider values, connector names, pin labels, and net names are often unreadable in whole-page thumbnails.

4. Manual/packaging/instruction PDF.
   - Pages may use multi-column layout, sidebars, icons, warnings, image captions, callouts, and packaging panels.
   - Extract content in human reading order: title -> section heading -> paragraph/list/table/image caption/callout, not raw PDF object order.
   - Preserve icons and symbol meanings with nearby text. Do not lose packaging panel order or instruction step order.

## Required Output Per PDF File

For every `.pdf`, produce:

- `<name>.md`: document-level Markdown index with source metadata.
- `pages_text/`: one text file per page from native PDF text extraction.
- `pages_ocr/`: one OCR text file per rendered page when OCR is needed.
- `pages_png/`: rendered page images, preferably 200-300 DPI for review.
- `pages_layout/`: per-page layout JSON/CSV with text blocks, bounding boxes, columns/regions, reading-order index, and source method.
- `pages_ordered_md/`: one Markdown file per page reconstructed in human reading order.
- `images/`: extracted embedded images when available.
- `page_manifest.csv`: page number, PDF type, size, rotation, text-layer status, OCR status, image path, layout/order status, and page risk.
- `visual_evidence_manifest.csv`: signatures, stamps, handwritten marks, diagrams, tables, labels, photos, checkmarks, symbols, and other visual evidence.
- `semantic_findings_manifest.csv` when applicable: document number, version, effective date, controlled form number, standards, product/model, approvals, test results, defect grades, drawings, dimensions, and other QA facts.
- `conversion_loss.json` or CSV row: source inspection result and risk reasons.
- Manual review flag: `yes` unless conversion loss risk is proven low.

## Mandatory Workflow

0. Check conversion toolkit readiness.
   - Read `D:\AI_0415\03DHF\skill\conversion-toolkit-skill\SKILL.md`.
   - Run `python "D:\AI_0415\03DHF\skill\conversion-toolkit-skill\scripts\check_conversion_tools.py" --install`.
   - Do not start PDF conversion until Python packages, PyMuPDF, Pillow, pytesseract, and Tesseract with `chi_sim`, `eng`, `osd` are ready or missing-tool risk is explicitly reported.

0.5. Run the batch conversion gate before full PDF conversion.
   - Convert only 3 representative `.pdf` files first. If fewer than 3 PDF files exist, convert all PDF files.
   - If the PDF set contains mixed types, include representative samples when possible: office PDF, scanned/image-only PDF, report/certificate PDF, drawing/artwork PDF, and manual/packaging PDF.
   - Inspect the sample Markdown, page PNG renders, native text, OCR text, layout/reading-order outputs, image extraction, manifests, and `conversion_loss` records.
   - The gate fails if any sample has blocked/encrypted handling errors, empty/garbled Markdown, mojibake paths, missing page renders, OCR hangs/timeouts without reporting, wrong reading order, wrong source metadata, or unhandled exceptions.
   - Record sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
   - Run the full PDF batch only after the sample gate passes. If it fails, fix the converter/tooling and rerun the sample gate first.

1. Resolve source path.
   - Do not trust terminal mojibake.
   - Use `Path.exists()` / `Test-Path`.
   - Keep both `recorded_source_path` and `resolved_source_path`.

2. Inspect PDF structure.
   - Record page count, page sizes, rotations, encryption/password status, metadata, attachments, forms, annotations, bookmarks, and embedded files when detectable.
   - Use PyMuPDF (`fitz`) for page text, page rendering, images, annotations, and metadata.

3. Extract native text.
   - Extract page text with coordinates when possible.
   - Keep one text file per page to preserve page evidence.
   - Do not assume native text is complete; some PDFs contain hidden, reordered, or partial text layers.

3.1. Reconstruct page layout and reading order.
   - Extract text blocks with bounding boxes, font size when available, and block type hints.
   - Determine human reading order per page before writing Markdown.
   - For normal documents: sort by page regions, columns, y-position, then x-position, while keeping headings, paragraphs, lists, tables, captions, footnotes, and page headers/footers separate.
   - For multi-column manuals or packaging PDFs: detect columns/panels and read each panel/column top-to-bottom before moving to the next logical region.
   - For tables: preserve table grid order and do not flatten row/column relationships into arbitrary text.
   - For drawings: treat title block, revision block, notes block, dimensions, and callout labels as named regions rather than ordinary paragraphs.
   - Mark `reading_order_review_required=yes` if native extraction order conflicts with visual page order, columns are detected, text overlaps, tables are fragmented, or OCR text cannot be confidently placed.
   - Produce `pages_ordered_md/` from layout-aware reading order, not from raw extraction order alone.

4. Render pages for visual review.
   - Render every page to PNG at review resolution.
   - Use 300 DPI for small print, drawings, labels, certificates, signatures, and forms.
   - Preserve page number in the image filename.

5. OCR pages when needed.
   - OCR all pages with no text layer.
   - OCR pages where text extraction is sparse, garbled, or likely incomplete.
   - Use crop/upscale OCR for small labels, stamps, drawing title blocks, signatures, and dimension text.
   - Keep OCR text separate from native text so conflicts are visible.
   - For image-only report PDFs, OCR full pages plus critical cropped regions.
   - For manual/packaging PDFs, OCR/image text must be placed back into the correct visual region or panel before Markdown is considered complete.

6. Extract visual evidence.
   - Identify signatures, stamps, handwritten notes, checkmarks, tables, diagrams, photos, icons, labels, title blocks, and drawings.
   - For drawings or certificates, inspect title block fields such as drawing number, revision, material, scale, approval, and date.
   - For test reports, preserve result tables, acceptance criteria, units, and pass/fail conclusions.
   - For regulatory or standards evidence, preserve standard numbers, edition/year, and applicability text.
   - For manuals and packaging PDFs, preserve warnings, icons, captions, callout arrows, step numbers, panel order, and section hierarchy.
   - For Gantt/project-plan PDFs, do not answer phase dates from text extraction alone. Use the rendered page to align task rows with timeline bars and start/end labels.
   - For packaging/artwork PDFs, extract both artwork text and drawing notes: material, surface treatment, dimensions, color/PANTONE, drawing number, edition, manufacturer, product claims, and label specifications.
   - For schematics, extract circuit blocks as visual evidence. Record component designators, model/value, connected nets, and functional interpretation when asked.

7. Extract high-value semantic findings.
   - Document metadata: document number, revision/version, effective date, controlled form number, title, author/approver, and page count.
   - Table semantics: pass/fail, CR/MA/MI, acceptable/not acceptable, checked/unchecked, and color/status meaning.
   - Visual QA facts: signatures/stamps present, images/photos present, drawing dimensions, labels, symbols, and test setup screenshots.
   - If a finding comes from a rendered image or OCR, include page number and image path as evidence.
   - Preserve critical symbols exactly: `≤`, `≥`, `±`, `℃`, `°C`, `°F`, `Ω`, `μ`, `mL`, `cm²`, superscripts/subscripts, polarity signs, and decimal points. OCR may confuse `≤` with `<`, `±` with `+`, `cm²` with `cm2`, or `0.5` with `0.S`; verify against page image before answering specifications.

8. Assign conversion loss risk.
   - `high`: scanned pages, signatures/stamps, drawings, images, forms, annotations, embedded files, or OCR-dependent evidence may be missing.
   - `high`: native text extraction is garbled, page order is suspicious, or tables/dimensions/title blocks are not represented in Markdown.
   - `high`: manual/packaging reading order, columns/panels, captions, callouts, warnings, or instruction steps are not represented in visual order.
   - `medium`: OCR confidence, table reconstruction, image interpretation, or visual evidence needs confirmation.
   - `low`: native text, OCR, page images, visual evidence, and semantic findings are represented or not present.

9. Assign readiness.
   - `ai_ready`: content and visual evidence are complete enough for AI review.
   - `partial`: readable but any conversion loss risk remains.
   - `blocked`: PDF cannot be opened, is password-protected, or rendering/OCR failed.

## Prompt Template

```text
You are converting PDF DHF/DMR evidence into AI-readable Markdown.

Do not only check whether text extraction worked. Check whether page-level and visual evidence was lost.

For each PDF:
1. Resolve the real source path.
2. Inspect page count, metadata, attachments, forms, annotations, page size, and rotation.
3. Classify PDF type: converted-office, image-only report, drawing/CAD/artwork, or manual/packaging/instruction.
4. Extract native text per page with coordinates.
5. Reconstruct layout and human reading order; output pages_ordered_md.
6. Render every page to PNG for visual review.
7. OCR scanned/sparse/garbled pages, using crop/upscale OCR when needed.
8. Extract signatures, stamps, drawings, tables, labels, photos, symbols, title blocks, captions, callouts, warnings, and annotations.
9. Extract document metadata and high-value semantic findings.
10. Compare native text, OCR text, ordered Markdown, and page images.
11. Output high/medium/low conversion loss risk.
12. Mark high and medium risk files as partial, not ai_ready.
```

## Learned Lessons From PT9L

- A PDF may look text-readable while losing the actual page evidence. Keep page images for every page.
- Scanned drawings and certificates require OCR plus visual review; native text extraction may be empty.
- Small title blocks, labels, signatures, and stamps often need crop/upscale OCR.
- For DHF/DMR review, document number, revision, effective date, controlled form number, signature/stamp presence, and approval status are first-class evidence.
- Tables and drawings are high risk if only flattened text is extracted; preserve page image references and mark manual review.
- PDF text object order is not the same as human reading order. Manuals, packaging PDFs, labels, and converted-office PDFs must be reconstructed by page layout, columns, panels, captions, and table structure.
- For image-only reports, the rendered page is the source of truth and OCR is a searchable derivative.
- For drawings/artwork, title blocks, revision blocks, dimensions, tolerances, notes, and approval areas are first-class evidence.
- PT9L project-plan PDFs showed that Gantt dates require visual alignment. Text extraction listed dates separately from task names; `T1阶段` had to be confirmed from the page image as `2024/2/7` to `2024/4/23`.
- PT9L scanned biocompatibility reports showed OCR is useful but must be tied to page images. Section `9.1.2` included actual sample area `222.684 cm²` and extraction ratio `3 cm² : 1 mL`; units and superscripts require image confirmation.
- PT9L packaging artwork showed OCR can misread regulatory/specification symbols. `Measurement Distance: ≤1.18 in (3 cm)` was misread as `<1.18in(3cm)`; always verify comparison symbols visually.
- PT9L schematic PDFs require crop/upscale review. Whole-page extraction found the MCU area, but the answer required a crop to read `U2 BH67F2762`; the NTC circuit also required a crop to identify `NTC 10k`, `R15 10k`, `C18 0.1uF`, `VCM`, and `AI_NTC`.
- Manual screenshots and icons must be answered from the manual table, not generalized. `Err` in the PT9L manual corresponds to ambient temperature outside `50°F-104°F (10°C-40°C)` or unstable, with the action to use the thermometer within the designed ambient temperature range.
- EMC tables in manuals should be mapped to standards. `Table 3 - Proximity fields from RF wireless communications equipment` maps to IEC 60601-1-2 EMC wireless RF proximity immunity context, while IEC 61000-4-39 is proximity magnetic fields and should not be conflated.
