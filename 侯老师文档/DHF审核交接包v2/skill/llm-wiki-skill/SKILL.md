---
name: llm-wiki-skill
description: Builds and maintains an LLM wiki from converted DHF/DMR Markdown evidence. Use when the user asks to create, update, extend, or audit a wiki/llm wiki from Word, Excel, PDF, or other converted evidence under PT9L_MD, including source catalogs, manifests, stage pages, risk pages, and llms.txt.
---

# LLM Wiki Skill

## Purpose

Use this skill to turn converted DHF/DMR evidence into a local LLM wiki.

The wiki is not a replacement for conversion evidence. It is a navigation and retrieval layer over converted Markdown and `.assets` folders. Evidence-critical answers must still inspect source Markdown, manifests, page images, OCR/layout outputs, sheet exports, visual evidence, and `conversion_loss.json`.

## Expected Input

The converted evidence root should mirror the original project structure, for example:

```text
D:\AI_0415\03DHF\PT9L_MD
```

Each converted file should have:

- `<source-relative-path>\<name>.md`
- `<source-relative-path>\<name>.assets\`
- global manifests under `_manifests\`

For PT9L, the main conversion manifests are:

```text
_manifests\word_conversion_manifest.csv
_manifests\excel_conversion_manifest.csv
_manifests\pdf_conversion_manifest.csv
```

## Wiki Layout

Use this structure:

```text
llm_wiki\
  README.md
  AGENTS.md
  llms.txt
  llms-full.txt
  sources\
    word\
    excel\
    pdf\
    artwork\
    cad\
    image\
    archive\
    ignored\
  wiki\
    index.md
    source_catalog.md
    excel_source_catalog.md
    pdf_source_catalog.md
    remaining_source_catalog.md
    artwork_cad_image_catalog.md
    ignored_files.md
    all_source_catalog.md
    modality_coverage.md
    high_risk_conversion_gaps.md
    excel_pdf_high_risk_conversion_gaps.md
    remaining_high_risk_conversion_gaps.md
    stages\
    stages_all\
    topics\
  manifests\
    source_catalog.csv
    excel_source_catalog.csv
    pdf_source_catalog.csv
    remaining_source_catalog.csv
    all_source_catalog.csv
    all_source_catalog.json
```

## Core Rules

1. Preserve the converted source Markdown as immutable wiki sources.
   - Copy Word sources to `llm_wiki\sources\word\`.
   - Copy Excel sources to `llm_wiki\sources\excel\`.
   - Copy PDF sources to `llm_wiki\sources\pdf\`.
   - Keep relative source paths whenever possible.
   - Do not edit copied source Markdown by hand.

2. Keep `.assets` outside the wiki source copy.
   - The wiki catalog should point to the original `assets_dir`.
   - Do not duplicate large `pages_png`, `sheet_pages_png`, OCR files, extracted images, or CSV evidence unless the user explicitly asks.
   - Wiki source Markdown is for navigation; the original `.assets` folders remain the evidence store.

3. Build catalog pages by modality.
   - Word: `wiki/source_catalog.md`
   - Excel: `wiki/excel_source_catalog.md`
   - PDF: `wiki/pdf_source_catalog.md`
   - All modalities: `wiki/all_source_catalog.md`

4. Build stage pages.
   - `wiki/stages\`: existing Word-only stage pages may remain.
   - `wiki/stages_all\`: combined Word/Excel/PDF stage pages.
   - Stage is inferred from `source_relative_path`.

5. Keep risk visible.
   - Include `loss_risk_level`, `risk_reasons`, `manual_review_required`, and `assets_dir` in catalogs.
   - High/medium risk means the file is searchable but not fully AI-ready without evidence review.
   - `blocked` must be called out separately.

6. Update LLM entry files.
   - `wiki/index.md` is the main entry point.
   - `README.md` summarizes coverage.
   - `AGENTS.md` tells future agents how to use the wiki.
   - `llms.txt` lists entry points and all copied source Markdown.
   - `llms-full.txt` includes entry points plus full wiki page contents.

## Evidence Rules By Modality

### Word

Use copied source Markdown for text navigation, then inspect `assets_dir` when risk is high/medium.

Important Word evidence includes:

- images
- signatures/stamps
- headers/footers
- checkboxes/form fields
- tracked or floating objects
- visual formatting and highlight color
- OLE/embedded objects

### Excel

Excel Markdown alone is not enough. Inspect the original `.assets` folder for:

- `sheets_csv\`
- `sheets_md\`
- `sheet_pages_pdf\`
- `sheet_pages_png\`
- `page_manifest.csv`
- `formula_manifest.csv`
- `structure_manifest.csv`
- `visual_format_manifest.csv`
- `text_objects_manifest.csv`
- `semantic_findings_manifest.csv`
- `conversion_loss.json`

Use the visual channel for layout-dependent work instructions, headers, form numbers, text boxes, images, signatures, screenshots, color meaning, print views, and sheet/page relationships.

### PDF

PDF Markdown alone is not enough. Inspect the original `.assets` folder for:

- `pages_png\`
- `pages_text\`
- `pages_ocr\`
- `pages_layout\`
- `pages_ordered_md\`
- `page_manifest.csv`
- `visual_evidence_manifest.csv`
- `semantic_findings_manifest.csv`
- `conversion_loss.json`

Use page PNG and layout/OCR evidence for drawings, reports, scanned documents, Gantt charts, packaging artwork, labels, multi-column manuals, regulatory tables, and critical symbols such as less-than-or-equal, greater-than-or-equal, plus-minus, Celsius, and square-centimeter units.

## Mandatory Workflow

1. Confirm source manifests exist.
   - For Word-only wiki, require `word_conversion_manifest.csv`.
   - For Excel extension, require `excel_conversion_manifest.csv`.
   - For PDF extension, require `pdf_conversion_manifest.csv`.

2. Read existing wiki before changing it.
   - Read `llm_wiki\wiki\index.md`.
   - Read `llm_wiki\manifests\source_catalog.csv` if present.
   - Determine whether you are rebuilding the whole wiki or extending it.

3. Do not accidentally delete a completed wiki.
   - If using a script that deletes `llm_wiki`, warn before running it.
   - For adding Excel/PDF after Word is already done, use an incremental extension script.

4. Normalize rows into a common catalog schema:

```text
wiki_id
modality
stage
source_relative_path
source_type
pdf_type
output_markdown
assets_dir
wiki_source_path
wiki_source_rel
conversion_status
loss_risk_level
risk_reasons
page_count
sheet_count
semantic_finding_count
visual_evidence_count
image_count
manual_review_required
```

5. Copy source Markdown into modality folders.
   - Use safe filenames for Windows-reserved characters.
   - Preserve source-relative parent directories.
   - Keep copied filenames ending in `.source.md`.

6. Write or update:
   - modality source catalogs
   - all-source catalog
   - modality coverage page
   - high-risk pages
   - stage pages
   - README
   - AGENTS
   - llms.txt
   - llms-full.txt

7. Verify counts.
   - Count source rows by modality.
   - Count copied Markdown files under each `sources\<modality>\`.
   - Confirm `blocked` count.
   - Open at least one catalog page and one copied source page per new modality.

## PT9L Reference Scripts

For PT9L, these scripts captured the working pattern:

```text
D:\AI_0415\03DHF\PT9L\build_pt9l_llm_wiki.py
D:\AI_0415\03DHF\PT9L\extend_pt9l_llm_wiki_excel_pdf.py
```

`build_pt9l_llm_wiki.py` is Word-focused and deletes/rebuilds `llm_wiki`.

`extend_pt9l_llm_wiki_excel_pdf.py` is incremental and preserves the existing Word wiki while adding Excel and PDF:

```text
python "D:\AI_0415\03DHF\PT9L\extend_pt9l_llm_wiki_excel_pdf.py"
```

Expected PT9L result after Word + Excel + PDF:

```text
word=84
excel=62
pdf=91
all=237
blocked=0
```

## Output Quality Checklist

Before reporting done, verify:

- `wiki\index.md` includes Word, Excel, PDF counts.
- `wiki\all_source_catalog.md` exists.
- `wiki\excel_source_catalog.md` exists when Excel is included.
- `wiki\pdf_source_catalog.md` exists when PDF is included.
- `wiki\modality_coverage.md` exists.
- `wiki\stages_all\` exists and has stage pages.
- `manifests\all_source_catalog.csv` and `.json` exist.
- `sources\excel\` count matches Excel manifest count.
- `sources\pdf\` count matches PDF manifest count.
- `AGENTS.md` includes modality-specific evidence rules.
- `llms.txt` and `llms-full.txt` were regenerated.

## Common Failure Modes

- Do not rely on terminal output for Chinese paths; use Python `Path` and manifest values.
- Do not treat high risk as failure. In this workflow high risk often means visual evidence exists and must be reviewed.
- Do not drop `.assets` paths from catalogs; they are required for audit-grade answers.
- Do not merge Excel/PDF into the Word-only `source_catalog.csv` unless the schema is explicitly expanded.
- Do not overwrite user-maintained topic pages unless rebuilding is explicitly requested.
- Do not duplicate large evidence assets into the wiki unless storage size is acceptable and requested.
