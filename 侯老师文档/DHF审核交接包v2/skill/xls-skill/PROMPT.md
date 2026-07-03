# XLS Conversion Prompt

You are converting Excel `.xls` / `.xlsx` DHF/DMR evidence into AI-readable Markdown.

Do not only check whether CSV or Markdown has values. Check whether spreadsheet source information was lost.

For each Excel file:

1. Resolve the real source path. If the recorded path fails, try known path remaps before calling it missing.
2. Convert `.xls` to `.xlsx` using Excel COM when needed.
3. Export every visible sheet to CSV and manageable Markdown.
4. Preserve workbook metadata in the Markdown header.
5. Export relevant sheet pages to PDF/PNG and create page visual Markdown when layout carries meaning.
6. Inspect formulas and cached/display values.
7. Inspect merged cells, hidden sheets/rows/columns, filters, freeze panes, comments, hyperlinks, headers/footers, text boxes, charts, shapes, OLE objects, and data validation.
8. Extract form/file numbers from headers or floating text boxes; do not assume CSV contains them.
9. Extract all images with sheet name, anchor cell, nearby text, OCR, size, and evidence type.
10. If images and arrow/text labels are separate objects, answer from the exported sheet page.
11. Inspect image labels before answering material/specification questions.
12. If colors, conditional formatting, or icons define a matrix/category/status, output a semantic mapping.
13. Extract high-value semantic findings: `CR`/`MA`/`MI` tick-counts, fixtures/tools, operation steps, symbol/icon descriptions, document number, version, effective date, and controlled form number.
14. Compare source signals to CSV/Markdown/images/page snapshots.
15. Output a conversion loss risk level: high / medium / low.
16. Mark high and medium risk files as partial, not ai_ready.

Final output must include:

- workbook Markdown path
- source file path
- conversion method
- sheet CSV paths
- sheet page visual Markdown/PDF/PNG paths when applicable
- image review path
- formula manifest path
- structure manifest path
- text objects/header manifest path
- visual-format manifest path
- semantic findings manifest path when applicable
- loss risk reason
- manual review required yes/no
