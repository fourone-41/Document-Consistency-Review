# PDF Conversion Agent

## Agent Name

`pdf-conversion-agent`

## Purpose

This agent converts PDF DHF/DMR evidence into AI-readable Markdown while preserving page-level visual evidence.

It must not treat extracted text as complete conversion. PDFs may contain scanned pages, drawings, stamps, signatures, photos, annotations, forms, title blocks, and small labels that are only visible after rendering.

Every PDF must be classified before conversion:

- `converted_office_pdf`: exported from Word/Excel/PPT/other office sources; native text may exist but object order can differ from visual reading order.
- `image_only_report_pdf`: scanned/photo report, certificate, test record, signature/stamp evidence; page image is primary evidence and OCR is derived text.
- `drawing_cad_artwork_pdf`: drawings, packaging artwork, labels, dimensions, title blocks, revision tables, approval blocks.
- `manual_packaging_instruction_pdf`: manuals, IFU, packaging panels, labels, warnings, icons, captions, callouts, multi-column pages.

## Required Outputs

For each source `.pdf`:

- `<name>.md`
- `pages_text/`
- `pages_ocr/`
- `pages_png/`
- `pages_layout/`
- `pages_ordered_md/`
- `images/`
- `page_manifest.csv`
- `visual_evidence_manifest.csv`
- `semantic_findings_manifest.csv` when applicable
- `conversion_loss.json`
- row in batch conversion manifest
- row in manual review list when risk is high/medium

For the batch:

- source path resolution report
- conversion summary
- PDF manifest
- page manifest
- visual evidence manifest
- semantic findings manifest
- loss risk summary
- list of files requiring manual review

## Mandatory Workflow

1. Read `SKILL.md` and `PROMPT.md` in this folder before acting.
2. Resolve source paths.
   - Do not trust terminal mojibake.
   - Keep both `recorded_source_path` and `resolved_source_path`.
3. Inspect PDF structure.
   - Page count, metadata, attachments, forms, annotations, bookmarks, page sizes, and rotations.
4. Classify PDF type.
   - Identify whether the PDF is converted-office, image-only report, drawing/CAD/artwork, manual/packaging/instruction, or mixed.
   - Record type per file and per page when mixed.
5. Extract native page text.
   - Store one text file per page.
   - Flag sparse, empty, or garbled text.
   - Extract text coordinates when possible.
6. Reconstruct layout and reading order.
   - Store block bounding boxes, detected regions/columns, table regions, title blocks, captions, and reading-order index in `pages_layout/`.
   - Produce `pages_ordered_md/` from human reading order, not raw PDF object order.
   - For manual/packaging PDFs, preserve column/panel order, warnings, icons, captions, callouts, and instruction steps.
   - For drawings/artwork, extract title block, revision block, notes block, dimensions, and approval area as named regions.
   - Mark `reading_order_review_required=yes` when columns, panels, fragmented tables, overlapping text, or native/OCR order conflicts are detected.
7. Render every page.
   - Store one PNG per page.
   - Use higher DPI for small text, drawings, signatures, stamps, and labels.
8. OCR when needed.
   - OCR scanned/sparse/garbled pages.
   - Use crop/upscale OCR for small title blocks and labels.
   - For image-only reports, OCR full pages plus critical cropped regions.
   - Place OCR text back into the correct visual region before considering Markdown complete.
9. Extract visual evidence.
   - Signatures, stamps, handwritten marks, checkmarks, tables, diagrams, photos, symbols, labels, drawings, title blocks, and annotations.
   - For manuals/packaging, also preserve warnings, icons, captions, callout arrows, panel order, and section hierarchy.
   - For project plans/Gantt charts, preserve task row, timeline bar, start/end labels, and phase summary bars from the rendered page.
   - For schematics, crop/upscale MCU, sensor, NTC, connector, and power blocks when component labels or net names are too small in the full page.
10. Extract semantic findings.
   - Document number, version/revision, effective date, controlled form number, title, approval, standards, product/model, test results, pass/fail, dimensions, drawing fields, warnings, labels, and instruction steps.
   - Preserve critical symbols exactly: `≤`, `≥`, `±`, `℃`, `°C`, `°F`, `Ω`, `μ`, `mL`, `cm²`, polarity signs, and decimal points. Verify them against page images because OCR may confuse them.
11. Assign conversion loss risk.
   - `high`: scanned pages, signatures/stamps, drawings, forms, annotations, embedded files, OCR-dependent evidence, or table/title-block loss may be present.
   - `high`: reading order, columns/panels, captions/callouts, manual steps, or drawing title blocks are not represented in Markdown.
   - `medium`: OCR, table reconstruction, page visual evidence, or semantic findings need confirmation.
   - `low`: no obvious loss signal detected.
12. Assign readiness.
   - `ai_ready`: complete enough for AI review.
   - `partial`: readable but not complete enough.
   - `blocked`: source cannot be opened or conversion failed.

## Important PT9L Experience

- Page images are required evidence, not optional screenshots.
- Scanned PDFs must be treated as image evidence first and text evidence second.
- Drawing title blocks and form headers are often where document number, revision, date, and approval live.
- Signatures and stamps may determine DHF/DMR approval status and must be explicitly recorded.
- OCR text must be tied back to page number and rendered image path.
- PDF text extraction order is not reliable enough for manuals, packaging, labels, or converted-office PDFs. Always reconstruct human reading order from layout.
- Image-only reports must treat the rendered page as primary evidence and OCR as searchable derivative text.
- Drawing/artwork PDFs must preserve title blocks, revision blocks, dimensions, tolerances, notes, materials, scale, approvals, and dates.
- Gantt/project-plan PDFs require visual row/timeline alignment. Do not answer phase start/end dates from raw text order alone.
- Scanned reports need OCR plus image confirmation for units and superscripts, such as `cm²`, `mL`, and extraction ratios.
- Packaging/artwork OCR can misread specification symbols such as `≤` as `<`; always verify comparison symbols and units visually before answering.
- Schematic PDFs often require crop/upscale. PT9L MCU was confirmed from a crop as `U2 BH67F2762`; NTC design required a crop to identify `NTC 10k`, `R15 10k`, `C18 0.1uF`, `VCM`, and `AI_NTC`.
- Manual error icons must be answered from the exact troubleshooting table. PT9L `Err` means ambient temperature outside `50°F-104°F (10°C-40°C)` or unstable, not a generic target-temperature error.
- EMC manual tables should be mapped carefully: RF wireless proximity fields belong to the IEC 60601-1-2 EMC wireless RF proximity immunity context; do not confuse this with IEC 61000-4-39 proximity magnetic fields.

## Status Reporting

During long conversions, report status every 1 minute:

- current file or batch step
- completed count / total count
- current blocker if any
- next action
