# DOC Conversion Prompt

You are converting legacy Word `.doc` DHF/DMR evidence into AI-readable Markdown.

Do not only check whether Markdown has text. Check whether the conversion lost source information.

For each `.doc` file:

1. Resolve the real source path. If the recorded path fails, try known path remaps before calling it missing.
2. Convert `.doc` to `.docx` using LibreOffice or Word COM with timeout.
3. Convert `.docx` to Markdown using MarkItDown.
4. Preserve source metadata in the Markdown header.
5. Export pages to PDF/PNG and create page visual Markdown when layout carries meaning.
6. Inspect the original Word source for:
   - tables
   - checkbox states
   - Word form fields
   - content controls
   - checkmark symbols
   - inline/floating images
   - embedded OLE or Excel objects
   - table shading, text highlight, font color, and colored shapes that encode meaning
7. If labels/arrows/text boxes are separate Word objects from images, answer from the exported page snapshot.
8. If colors/highlights define a matrix or category, output a semantic row/column mapping. Do not treat an empty Markdown table plus a legend image as complete evidence.
9. Compare source signals to Markdown/images/page snapshots.
10. Output a conversion loss risk level: high / medium / low.
11. Mark high and medium risk files as partial, not ai_ready.

Final output must include:

- Markdown file path
- page visual Markdown/PDF/PNG paths when applicable
- source file path
- conversion method
- loss risk reason
- manual review required yes/no
