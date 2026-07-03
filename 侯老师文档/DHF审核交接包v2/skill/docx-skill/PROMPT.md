# DOCX Conversion Prompt

You are converting native Word `.docx` DHF/DMR evidence into AI-readable Markdown.

Do not only check whether Markdown has text. Check whether the conversion lost source information.

For each `.docx` file:

1. Resolve the real source path. If the recorded path fails, try known path remaps before calling it missing.
2. Convert `.docx` to Markdown using MarkItDown.
3. Preserve source metadata in the Markdown header.
4. Export pages to PDF/PNG and create page visual Markdown when layout carries meaning.
5. Extract all images from the `.docx` package under `word/media`.
6. Generate `*.images.md` for image review outside complex Markdown tables.
7. Inspect the original DOCX source for:
   - tables and merged-cell structure
   - checkbox states
   - Word form fields
   - content controls
   - checkmark symbols
   - inline/floating images
   - embedded OLE or Excel objects
   - table shading, text highlight, font color, and colored shapes that encode meaning
8. If labels/arrows/text boxes are separate Word objects from images, answer from the exported page snapshot.
9. If colors/highlights define a matrix or category, output a semantic row/column mapping. Do not treat an empty Markdown table plus a legend image as complete evidence.
10. Compare source signals to Markdown/images/page snapshots.
11. Output a conversion loss risk level: high / medium / low.
12. Mark high and medium risk files as partial, not ai_ready.

Final output must include:

- Markdown file path
- page visual Markdown/PDF/PNG paths when applicable
- source file path
- conversion method
- extracted image path
- image mapping risk
- visual-format mapping risk
- loss risk reason
- manual review required yes/no
