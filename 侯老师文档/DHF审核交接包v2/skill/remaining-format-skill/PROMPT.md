# Remaining Format Conversion Prompt

You are converting or registering remaining DHF/DMR source formats after Word, Excel, and PDF conversion.

Use this for `.ai`, `.dwg`, `.zip`, `.jpg`, `.png`, `.scc`, `.tmp`, artwork, CAD, images, archives, and ignored files.

For each task:

1. Read `D:\AI_0415\03DHF\skill\remaining-format-skill\SKILL.md`.
2. Inventory the remaining source files from original source folders only.
3. Check AI/DWG/image/OCR tools.
4. For `.ai`, try PDF-compatible rendering with PyMuPDF; render to PNG, extract text, OCR, semantic findings, and related PDF links.
5. For `.dwg`, use native conversion only if a DWG tool exists; otherwise register as partial/high with related PDF links when available.
6. For `.zip`, extract and write `archive_manifest.csv`; link internal files to existing conversions.
7. For `.jpg/.png`, create review image and OCR text.
8. For `.scc/.tmp`, register as ignored unless user says it is formal evidence.
9. Write global remaining manifests.
10. Extend `llm_wiki` if requested.
11. Verify status counts and sample evidence.

Final output must include:

- source count by extension/modality
- success / partial / blocked / ignored counts
- manifest paths
- wiki catalog paths when updated
- known limitations, especially DWG native tool gaps
