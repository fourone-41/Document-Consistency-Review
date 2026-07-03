---
name: remaining-format-skill
description: Converts and registers remaining DHF/DMR source formats after Word, Excel, and PDF are done. Use for `.ai`, `.dwg`, `.zip`, `.jpg`, `.png`, `.scc`, `.tmp`, artwork, CAD, images, archives, ignored files, or when extending PT9L_MD and llm_wiki with remaining formats.
---

# Remaining Format Skill

## Purpose

Use this skill after Word, Excel, and PDF conversion to cover remaining source files:

- `.ai`: Illustrator/artwork/label/packaging source
- `.dwg`: CAD source drawing
- `.zip`: archive containing drawings, spreadsheets, PDFs, or source files
- `.jpg` / `.png`: standalone image evidence
- `.scc` / `.tmp`: version-control or temporary residue, normally ignored

The goal is not to force every file into text. The goal is complete audit coverage: every source file must be `success`, `partial`, `blocked`, or `ignored`, with evidence and reason recorded.

## Required Output Per File

For every remaining source file, produce:

- `<name>.md`
- `<name>.assets\source\`
- `conversion_loss.json`
- row in `remaining_source_manifest.csv`
- copied source Markdown in `llm_wiki\sources\<modality>\` when wiki is extended

Additional outputs by type:

- `.ai`: `pages_png\`, `pages_text\`, `pages_ocr\`, `pages_layout\`, `page_manifest.csv`, `visual_evidence_manifest.csv`, `semantic_findings_manifest.csv`, `related_sources_manifest.csv`
- `.dwg`: `related_sources_manifest.csv`; native conversion only when DWG tooling is available
- `.zip`: `unzipped\`, `archive_manifest.csv`
- image: `images\`, `image_manifest.csv`, `ocr_text.txt`, `semantic_findings_manifest.csv`
- ignored: registration Markdown and `conversion_loss.json`

## Mandatory Workflow

0. Read `D:\AI_0415\03DHF\skill\conversion-toolkit-skill\SKILL.md` if rendering/OCR is needed.

1. Inventory remaining formats.
   - Scan original source roots, not generated folders.
   - Exclude `PT9L_MD`, `converted_md`, temp conversion outputs, and wiki copies.
   - Record extension counts and examples.

1.5. Run the per-format batch conversion gate before full conversion.
   - For each remaining format/modality, convert or register only 3 representative files first. If fewer than 3 exist for that format, process all files of that format.
   - Sample independently per type: `.ai`, `.dwg`, `.zip`, `.jpg/.png`, and ignored `.scc/.tmp` registration.
   - Inspect sample Markdown, copied source, rendered pages/images, OCR text, archive manifests, related-source links, conversion status, and `conversion_loss` records.
   - The gate fails if any sample has empty/garbled output, mojibake paths, missing copied sources, missing renders/OCR where required, broken archive extraction, wrong related-source links, wrong source metadata, or unhandled exceptions.
   - Record sample file list, sample result, issues, fixes, and proceed/stop decision in the batch summary.
   - Run the full remaining-format batch only after every sampled format passes. If a type fails, fix that converter/tooling and rerun that type's sample gate first.

2. Check tools.
   - `.ai`: test PyMuPDF first because many AI files are PDF-compatible.
   - `.ai`: if PyMuPDF fails, check Illustrator COM, Inkscape, or Ghostscript.
   - `.dwg`: check AutoCAD, DWG TrueView, ODA File Converter, or other DWG-to-PDF tools.
   - Images: require Pillow and Tesseract OCR.

3. Convert `.ai`.
   - Treat as artwork/packaging/label evidence.
   - Render to PNG when PDF-compatible or supported by local tools.
   - Extract native text and OCR text.
   - Extract key semantic findings: drawing number, revision, material, size, tolerance, color/PANTONE, product claims, manufacturer, regulatory symbols.
   - Link same/similar converted PDF evidence when available.
   - Mark `high/partial` because artwork must be visually reviewed.

4. Convert `.dwg`.
   - If native DWG tooling exists, convert to PDF/PNG and then use drawing/PDF rules.
   - If no native tool exists, do not guess content.
   - Copy source, mark `partial/high` when related PDF evidence exists.
   - Mark `blocked` only when neither native conversion nor related evidence exists.

5. Convert `.zip`.
   - Copy source zip to `.assets\source\`.
   - Extract into `.assets\unzipped\`.
   - Generate `archive_manifest.csv`.
   - Link internal PDFs/Excel files to existing converted manifests when matching by filename.
   - Mark archive `partial/high` if it contains unconverted DWG or unknown formal evidence.

6. Convert images.
   - Copy source image.
   - Generate review image.
   - OCR with `chi_sim+eng`.
   - Record image size and OCR status.
   - Mark `medium/partial` unless it is purely decorative and proven low risk.

7. Register ignored files.
   - `.scc` and `.tmp` are normally not formal evidence.
   - Copy/register them, but mark `ignored`.
   - Put them in ignored manifest and wiki ignored page.

8. Write global manifests.
   - `remaining_source_manifest.csv`
   - `remaining_conversion_summary.md`
   - `artwork_source_manifest.csv`
   - `cad_source_manifest.csv`
   - `image_source_manifest.csv`
   - `archive_source_manifest.csv`
   - `ignored_source_manifest.csv`
   - semantic/visual manifests when applicable

9. Extend wiki.
   - Read and follow `D:\AI_0415\03DHF\skill\llm-wiki-skill\SKILL.md`.
   - Add sources under:
     - `sources\artwork\`
     - `sources\cad\`
     - `sources\image\`
     - `sources\archive\`
     - `sources\ignored\`
   - Add/update remaining catalogs, ignored page, modality coverage, all catalog, stage pages, and llms files.

## PT9L Reference Scripts

```text
D:\AI_0415\03DHF\PT9L\convert_remaining_to_pt9l_md.py
D:\AI_0415\03DHF\PT9L\extend_pt9l_llm_wiki_remaining.py
```

PT9L expected result:

```text
artwork=9
cad=2
image=2
archive=2
ignored=2
blocked=0
total wiki sources=254
```

## Quality Checklist

- All remaining files have a status.
- `.ai` files render to PNG or are linked to alternative PDF evidence.
- `.dwg` files are not guessed; tool absence is explicit.
- `.zip` internal files are indexed.
- Images have OCR/review evidence.
- `.scc/.tmp` are ignored, not silently dropped.
- `blocked=0` or every blocked file has a clear reason.
- Wiki catalogs and source counts match manifests.
