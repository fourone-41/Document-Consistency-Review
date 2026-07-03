# Stage 03 DHF Risk Check Prompt Template

Use this prompt when starting a Stage 03 DHF risk check for a new model.

```text
Run the Stage 03 DHF risk check.

Inputs:
- product_original_root: <path to product original DHF/DMR root>
- product_md_root: <path to converted AI-readable root>
- product_check_root: <path to mirrored check output root>
- stage_01_check_folder: <path to Stage 01 check outputs>
- stage_02_check_folder: <path to Stage 02 check outputs>
- qms_procedure_md: <path to QP-7.3 converted procedure>
- stage_03_md_folder: <path to converted Stage 03 risk folder>

Rules:
- Read the Stage 03 DHF risk check skill before acting.
- Do not edit the plan file if one is attached.
- Do not recreate existing todos; update their statuses as work progresses.
- Read the risk management plan, risk assessment report, and assets.
- Extract the Stage 03 risk baseline: identity, document numbers, people, standards, lifecycle phases, risk criteria, risk group, risk topics, risk IDs, and planned controls.
- Audit the logic of Chapter 3 in the risk assessment report:
  - which standard/regulation source is used;
  - which annex, table, or clause is used;
  - how ISO/TR 24971 Annex A questions, IEC 60601-1 questions, and IEC 60601-1-2 EMC questions flow into R1-Rn risk rows;
  - whether China/US/EU regulatory risks are explicitly mapped when multi-market coverage is expected.
- Audit the frequency/probability and severity judgment:
  - P is probability/frequency, not generic difficulty;
  - S is harm severity;
  - high P, high S, and clustered P4/S3 rows must have rationale;
  - if rationale is missing, create a finding and remediation path.
- Check Stage 01 to Stage 03 carry-forward.
- Check Stage 02 to Stage 03 carry-forward.
- Check the downstream closure path from Stage 03 to Stage 04 design input, Stage 08 verification/DFMEA, and Stage 11 residual risk/risk management report.
- Treat visual risk matrices and color-coded acceptance tables as requiring visual/manual review if conversion loss reports indicate visual-format semantics.
- Treat blank signature/date fields as evidence gaps unless original/page visual evidence proves otherwise.
- Provide actionable remediation for every nonconforming, evidence-gap, manual-review, or needs-explanation item.

Outputs:
- stage_03_risk_baseline.md
- stage_03_risk_check_report.html in Chinese
- stage_03_findings.csv
- stage_03_traceability_matrix.csv
- stage_03_regulatory_risk_logic_matrix.csv when regulatory-source mapping is needed

Do not stop until all requested outputs are generated and checked.
```
