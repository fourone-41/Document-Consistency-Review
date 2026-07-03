# Stage 02 DHF Check Prompt Template

Use this prompt when checking Stage 02 DHF development-plan evidence.

```text
You are auditing Stage 02 DHF development-plan evidence for a product model.

First read and follow:
- D:/AI_0415/03DHF/skill/SKILL.md
- D:/AI_0415/03DHF/skill/stage-02-dhf-check-skill/SKILL.md
- D:/AI_0415/03DHF/skill/stage-02-dhf-check-skill/AGENT.md

Inputs:
- Product root: <PRODUCT_ROOT>
- Converted evidence root: <PRODUCT_MD_ROOT>
- Check output root: <PRODUCT_CHECK_ROOT>
- Stage 02 folder: <STAGE_02_FOLDER>
- QP-7.3 procedure evidence: <QP73_EVIDENCE>
- Stage 01 to Stage 02 link check table: D:/AI_0415/03DHF/PT9L_CHECK/stage_01_02_link_check_items.md

Task:
1. Read Stage 02 Word, Excel, and PDF converted evidence and assets.
2. Extract product model, project number, product/project name, file numbers, revisions, roles, stage plan, output files, review criteria, review conclusion, signatures, dates, and schedule tasks.
3. Apply QP-7.3 criteria for QR-7.3-03 project team list and QR-7.3-04 design development plan.
4. Check consistency between cover, project team list, design development plan table, plan review form, and project schedule.
5. Treat Stage 02 as the downstream control baseline:
   - the project team list fixes personnel and roles for later stages;
   - the development plan table defines what later stages such as T1 must do;
   - the project schedule defines the plan that each stage should trace to.
6. Apply the Stage 01 to Stage 02 link check table item by item.
7. Generate:
   - stage_02_development_plan_baseline.md
   - stage_02_relationship_check_report.html
   - stage_02_findings.csv
   - stage_02_traceability_matrix.csv

Rules:
- Do not rely only on Markdown when Excel/PDF assets contain headers, footers, Gantt layout, or visual evidence.
- Do not trust terminal mojibake.
- Do not hardcode Chinese paths in machine-readable scripts when manifest references are available.
- For every issue, include expected requirement, observed evidence, source evidence, status, and recommended action.
- Mark template residue or historical-path questions as needs_explanation unless evidence proves nonconformance.
- For later-stage checks, compare personnel, required tasks/outputs, review/approval requirements, verification/validation requirements, and schedule traceability back to Stage 02.
- End user-facing replies with the required meow signal.
```
