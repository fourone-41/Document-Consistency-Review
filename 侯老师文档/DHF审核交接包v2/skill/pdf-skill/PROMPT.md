# PDF Conversion Prompt

You are converting PDF DHF/DMR evidence into AI-readable Markdown.

Do not only check whether native PDF text can be extracted. Check whether page-level visual evidence was lost.

For each PDF file:

1. Resolve the real source path.
2. Inspect page count, metadata, encryption, attachments, forms, annotations, page size, and rotation.
3. Classify PDF type: converted-office, image-only report, drawing/CAD/artwork, manual/packaging/instruction, or mixed.
4. Extract native text per page with coordinates when possible.
5. Reconstruct layout and human reading order; generate `pages_ordered_md/`.
6. Render every page to PNG.
7. OCR scanned/sparse/garbled pages; crop/upscale small labels, title blocks, stamps, and signatures when needed.
8. Place OCR text into the correct visual region when layout matters.
9. Extract signatures, stamps, handwriting, checkmarks, tables, diagrams, drawings, labels, photos, symbols, title blocks, captions, callouts, warnings, panels, and annotations.
10. For Gantt/project-plan PDFs, answer phase dates only after visual row/timeline alignment.
11. For schematics, crop/upscale small component blocks before answering MCU, NTC, sensor, connector, net, or value questions.
12. Preserve and visually verify critical symbols: `≤`, `≥`, `±`, `℃`, `°C`, `°F`, `Ω`, `μ`, `mL`, `cm²`, polarity signs, and decimal points.
13. Extract document metadata and semantic findings: document number, revision/version, effective date, controlled form number, approvals, standards, product/model, test results, dimensions, pass/fail, warnings, labels, and instruction steps.
14. Compare native text, OCR text, ordered Markdown, and rendered page images.
15. Output a conversion loss risk level: high / medium / low.
16. Mark high and medium risk files as partial, not ai_ready.

Final output must include:

- PDF Markdown path
- source file path
- page count
- rendered page image path pattern
- native text path
- OCR text path when applicable
- layout manifest/path
- ordered page Markdown path
- page manifest path
- visual evidence manifest path
- semantic findings manifest path when applicable
- loss risk reason
- manual review required yes/no
