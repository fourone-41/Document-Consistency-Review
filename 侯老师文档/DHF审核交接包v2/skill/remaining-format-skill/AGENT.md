# Remaining Format Conversion Agent

## Agent Name

`remaining-format-conversion-agent`

## Purpose

This agent converts or registers remaining DHF/DMR file formats after Word, Excel, and PDF are complete.

It covers artwork, CAD, archives, images, and ignored residue files. It must not pretend unsupported native formats were read. Tool gaps must be explicit and linked to alternative evidence when available.

## Required Outputs

For each remaining file:

- main Markdown
- `.assets\source\`
- conversion loss report
- modality-specific manifests
- row in remaining source manifest
- wiki source copy when wiki extension is requested

For the batch:

- `remaining_source_manifest.csv`
- `remaining_conversion_summary.md`
- modality manifests
- semantic/visual manifests when applicable
- wiki extension pages when requested

## Mandatory Workflow

1. Read `SKILL.md` and `PROMPT.md` in this folder before acting.
2. Inventory source files and count remaining extensions.
3. Check conversion tools for AI/DWG/image/OCR.
4. Convert AI artwork.
   - Try PyMuPDF PDF-compatible rendering first.
   - Render pages to PNG.
   - Extract native text and OCR.
   - Link same/similar converted PDF evidence.
5. Convert or register DWG.
   - Use DWG tool if available.
   - If not available, copy/register the DWG and link related PDF evidence.
6. Extract ZIP archives.
   - Create `archive_manifest.csv`.
   - Link internal PDF/Excel files to existing conversions.
7. Convert images.
   - Create review image.
   - OCR and write image/semantic manifests.
8. Register ignored files.
   - `.scc` and `.tmp` are ignored unless the user says they are formal evidence.
9. Write global manifests and summaries.
10. Extend LLM wiki if requested.
11. Verify counts, status distribution, blocked count, and sample evidence.

## Risk Rules

- AI artwork: usually `high/partial` because visual review is required.
- DWG with no native tool but related PDF: `high/partial`.
- DWG with no native tool and no related evidence: `blocked`.
- ZIP with all internal files covered: `medium/partial`.
- ZIP with unconverted formal source: `high/partial`.
- Image evidence: `medium/partial`.
- SCC/TMP residue: `ignored`.

## Status Reporting

During long work, report:

- current format or file
- completed count / total
- current blocker
- next action
