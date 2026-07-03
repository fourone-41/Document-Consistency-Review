---
name: stage-03-dhf-check-skill
description: Checks Stage 03 DHF risk management evidence for risk management plan, risk assessment report, ISO 14971/ISO TR 24971 coverage, QP-7.3 carry-forward, Stage 01/02 traceability, risk control path to design input, T1 verification, DFMEA, residual risk, and final risk management report. Use when auditing 03 risk folders, risk plans, risk assessment reports, R1-Rn risk controls, or risk traceability to later DHF stages.
---

# Stage 03 DHF Risk Check Skill

## Purpose

Use this skill for the Stage 03 DHF risk-management content audit.

The audit order is important:

1. Confirm the tool/readability layer is available.
2. Define what to extract.
3. Define check items.
4. Run the checks.
5. Use the report and closure matrix to prove that every check item was covered.
6. Human reviewers then judge whether the conclusions are acceptable.

Stage 03 checks whether risk management plan and risk assessment evidence:

- carry forward Stage 01 product, user, market, customer, and regulatory baselines;
- execute the Stage 02 development-plan risk-evaluation task;
- create risk-control outputs that later stages must close.

## Required Inputs

Read before concluding:

- Stage 01 core fields and Stage 01 requirement/regulatory findings.
- Stage 02 development-plan baseline and Stage 01-to-02 link check table.
- Converted Stage 03 risk management plan and risk assessment report.
- Risk file assets: visual format manifests, image manifests, metadata, conversion loss reports, and any page/visual evidence.
- QP-7.3 procedure evidence, especially the clauses stating that risk analysis is performed after plan approval and is a design-input source.
- Later stage evidence when checking closure: Stage 04 design input, Stage 08 T1/DFMEA/verification, Stage 11 residual risk and risk management report.

## Required Extraction Content

Extract:

- product model, project number, product name, document numbers, versions, drafter, approver, and dates;
- risk management standards and references;
- lifecycle phases covered by the risk management plan;
- risk management group members and roles;
- severity/probability criteria, risk matrix, residual risk acceptance criteria, and risk control verification criteria;
- risk topics from the risk assessment report, including intended use, user, environment, skin contact, measurement accuracy, measurement range, software, data, battery, cleaning, labeling, IFU, misuse, EMC, and essential performance;
- risk IDs and planned risk control measures where available.
- Chapter 3 source logic:
  - `3.1 Bibliography` and whether it explicitly lists applicable regulation/standard sources;
  - `3.2 ISO/TR 24971:2020 Annex A` questions and their device-characteristic coverage;
  - `3.3 IEC 60601-1` clause questions and their basic-safety/essential-performance coverage;
  - `3.4 IEC 60601-1-2` EMC risk-management questions and tables;
  - how these question groups flow into R1-Rn rows.
- P/S judgment details:
  - high-frequency rows such as P6 or P5;
  - high-severity rows such as S4 or S5;
  - clustered rows such as repeated P4/S3 design, labeling, or software controls;
  - whether the file gives a rationale for P and S values.

## Required Checks

For each Stage 03 folder, check:

- identity consistency with Stage 01 and Stage 02;
- whether risk plan and risk assessment report are present as Stage 02 planned outputs;
- whether risk management group members trace to Stage 02 personnel or have justified added roles;
- whether signatures, dates, version history, approvals, and release evidence are complete;
- whether standards used by risk files align with the project regulatory baseline;
- whether Chapter 3 identifies the source standard, annex, or clause behind the risk-identification questions;
- whether Chapter 3 or an appendix maps China/US/EU regulatory sources to risk topics and R IDs when those markets are in scope;
- whether market scope is clear: project-required market versus general company template coverage;
- whether the risk file maps `ISO/TR 24971 Annex A`, `IEC 60601-1`, and `IEC 60601-1-2` questions into R IDs;
- whether P/S values are justified rather than only filled in;
- whether risk matrices and color-coded tables require visual/manual review;
- whether Stage 01 issues have a risk path, such as temperature range, labeling, battery, environmental, software/data, intended use, or market requirements;
- whether Stage 03 outputs have a planned closure path into Stage 04, Stage 08, and Stage 11.

## Finding Rules

- Treat blank signature/date fields as `evidence_gap` unless visual evidence proves they are present.
- Treat visual risk matrices as `manual_visual_review_required` when conversion loss reports mention visual-format semantics.
- Treat added quality/process/medical personnel as acceptable only when role rationale or traceability exists.
- Treat Bluetooth/App/data risks as variant-dependent unless the specific model configuration confirms applicability.
- Do not accept a risk control as closed in Stage 03; closure needs later evidence.
- Treat missing China/US/EU regulation-to-risk mapping as a finding when the company practice or project scope requires multi-market risk coverage.
- Treat bare P/S numbers without rationale as `needs_explanation`, especially for P6/P5, S4/S5, P4/S3 clusters, and EMC/electrical risks.
- Treat Chapter 3 source standards as insufficiently audited unless the report identifies both the source and the downstream R IDs.
- Every finding must include expected requirement, observed evidence, source evidence, status, and recommended action.

## Required Outputs

Under the mirrored Stage 03 check folder, create or update:

- `stage_03_check_items.md`
- `stage_03_check_items_closure_matrix.csv`
- `stage_03_risk_baseline.md`
- `stage_03_risk_check_report.html`
- `stage_03_findings.csv`
- `stage_03_traceability_matrix.csv`
- optional but recommended: `stage_03_regulatory_risk_logic_matrix.csv`

## Closure Rule

The HTML report is not complete just because it has findings. It is complete only when every `CHK-03-*` item in `stage_03_check_items.md` has a corresponding conclusion in:

- the HTML report;
- `stage_03_findings.csv`;
- `stage_03_traceability_matrix.csv`;
- `stage_03_regulatory_risk_logic_matrix.csv`, when regulatory-source mapping is involved;
- `stage_03_check_items_closure_matrix.csv`.

If a check item has no corresponding report/finding/matrix entry, mark the audit as incomplete.

## Reuse For Other Models

Keep the same structure for other product types. Product-specific risk topics will change, but the relationship logic remains:

`Stage 01 requirements + Stage 02 plan -> Stage 03 risk plan/assessment -> Stage 04 design input -> Stage 08 verification/DFMEA -> Stage 11 residual risk/risk management report`.
