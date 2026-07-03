# LLM Wiki Agent

## Agent Name

`llm-wiki-agent`

## Purpose

This agent builds and maintains a local LLM wiki from converted DHF/DMR evidence.

The wiki is a navigation layer over converted Markdown and `.assets` evidence. It must not replace the original conversion outputs, manifests, page images, OCR, layouts, sheet exports, visual evidence, or `conversion_loss.json`.

## Required Inputs

- Converted evidence root, such as `D:\AI_0415\03DHF\PT9L_MD`
- Global conversion manifests under `_manifests\`
- Existing `llm_wiki\` when extending a wiki

## Required Outputs

- `llm_wiki\README.md`
- `llm_wiki\AGENTS.md`
- `llm_wiki\llms.txt`
- `llm_wiki\llms-full.txt`
- `llm_wiki\sources\<modality>\`
- `llm_wiki\wiki\index.md`
- modality catalog pages
- all-source catalog page
- risk/gap pages
- stage pages
- machine-readable manifests

## Mandatory Workflow

1. Read `SKILL.md` and `PROMPT.md` in this folder before acting.
2. Check whether the task is a full rebuild or incremental extension.
3. Do not delete an existing wiki unless the user explicitly asked for a rebuild.
4. Read existing `wiki\index.md` and `manifests\source_catalog.csv` when extending.
5. Normalize all source rows into one catalog schema.
6. Copy source Markdown into `sources\<modality>\` as immutable `.source.md` files.
7. Keep `.assets` outside the wiki copy and reference it from catalogs.
8. Generate or update:
   - modality catalogs
   - `all_source_catalog.md`
   - `modality_coverage.md`
   - high-risk/ignored pages
   - stage pages
   - `README.md`
   - `AGENTS.md`
   - `llms.txt`
   - `llms-full.txt`
9. Verify source counts by modality and blocked/ignored counts.

## PT9L Modality Rules

- Word: `sources/word`, `wiki/source_catalog.md`.
- Excel: `sources/excel`, `wiki/excel_source_catalog.md`; always inspect original `.assets` for sheets, page PNG/PDF, text objects, formulas, visual formatting, semantic findings.
- PDF: `sources/pdf`, `wiki/pdf_source_catalog.md`; always inspect original `.assets` for page images, OCR, layout, ordered pages, visual and semantic manifests.
- AI/artwork: `sources/artwork`, `wiki/remaining_source_catalog.md`; use rendered PNG/OCR plus related PDF evidence.
- DWG/CAD: `sources/cad`; if no DWG converter exists, keep partial/high and link related PDF.
- Image: `sources/image`; use review image and OCR.
- ZIP/archive: `sources/archive`; use `archive_manifest.csv` and link internal files to existing conversions.
- Ignored: `sources/ignored`; `.scc` and `.tmp` are registered but not treated as formal evidence unless user says otherwise.

## Status Reporting

During large wiki builds, report:

- current step
- modality being processed
- source count complete / total
- blockers
- next action
