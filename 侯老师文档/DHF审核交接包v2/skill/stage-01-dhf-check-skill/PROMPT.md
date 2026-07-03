# Stage 01 DHF Check Prompt Template

Use this prompt when checking Stage 01 DHF evidence.

```text
You are auditing Stage 01 DHF evidence for a product model.

First read and follow:
- D:/AI_0415/03DHF/skill/SKILL.md
- D:/AI_0415/03DHF/skill/stage-01-dhf-check-skill/SKILL.md
- D:/AI_0415/03DHF/skill/stage-01-dhf-check-skill/AGENT.md

Inputs:
- Product root: <PRODUCT_ROOT>
- Converted evidence root: <PRODUCT_MD_ROOT>
- Check output root: <PRODUCT_CHECK_ROOT>
- Stage 01 folder: <STAGE_01_FOLDER>
- Regulation folder/stage: <REGULATION_STAGE_FOLDER>

Task:
1. Read existing Stage 01 converted evidence and assets.
2. Extract and verify:
   - product model
   - product name
   - product category
   - sales region
   - registration path/responsibility
   - personnel list and responsibilities
3. Extract personnel from review participants, signature tables, version history, approval fields, headers/footers, and text boxes. Preserve role, person, department when available, and source evidence.
4. Save or update `stage_01_core_fields.md`.
5. Extract every customer requirement item from all Stage 01 customer requirement sections:
   - general requirements
   - performance specifications
   - function specifications
   - component/subassembly specifications
   - packaging and transport
   - environmental requirements
   - warning/display/labeling/usability requirements
   - special requirements
6. If the sales region is USA and the product is a forehead thermometer, prepare the US regulatory baseline:
   - 21 CFR 880.2910
   - 21 CFR 880.9
   - 21 CFR 807 Subpart E
   - 21 CFR 801
   - FDA SDV product classification
   - FDA FLL product classification as an exclusion check
   - FDA-recognized ISO 80601-2-56 and ASTM E1965 status
   - local Stage 13 standards already converted
7. Check each customer requirement item against the baseline:
   - range requirements must cover the regulatory minimum range
   - accuracy/error/risk requirements must be equal to or stricter than regulatory limits
   - warning/display/labeling/usability requirements must at least cover regulatory requirements
   - non-regulatory items should be marked and preserved
   - items requiring test evidence should be marked as follow-up validation, not guessed
   - nonconforming or potential-nonconforming items must include a remediation path, not only a fail conclusion
   - for temperature display range issues, explain whether the current wording is a full display/subject range claim or only body-mode clinical measuring range; recommend either expanding/verifying the applicable range, revising IFU/manual wording, or documenting the alternative regulatory path/no-applicability rationale
8. Save or update:
   - `us_forehead_thermometer_regulatory_baseline.md`
   - `us_regulatory_evidence_index.csv`
   - `customer_requirements_vs_regulations_report.html`
   - a reproducible report-generation script when HTML is generated
9. Check latest-version status using official sources where possible.
10. If official sources cannot be captured because of access blocking, mark `official_capture_pending` and cite the best available official alternate evidence, such as Federal Register or FDA database pages.
11. Produce `stage_01_check_report.md` and `stage_01_findings.csv` if a full audit is requested.

Rules:
- Do not rely only on Markdown when Excel assets or page visuals contain the field.
- Do not rely on clipped Markdown previews for wide customer requirement Excel sheets; inspect CSV and assets.
- Do not hardcode Chinese paths in scripts or machine-readable outputs.
- Do not store garbled question-mark mojibake text.
- Use manifests and source_file values to reference Stage 13 standards.
- Distinguish legal requirements from consensus standards.
- Distinguish local availability from latest-version status.
- Interpret 510(k) conditionally; do not assume every US forehead thermometer requires 510(k) or is exempt.
- Mark unknowns and pending captures honestly.
- When a requirement fails or may fail, include: exact regulation/standard basis, observed claim, why it fails, and recommended action.
- End user-facing replies with the required meow signal.
```

## Expected Output Files

```text
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../stage_01_core_fields.md
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../us_forehead_thermometer_regulatory_baseline.md
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../us_regulatory_evidence_index.csv
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../customer_requirements_vs_regulations_report.html
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../stage_01_check_report.md
<PRODUCT_CHECK_ROOT>/02_RnD_DHF/01 .../stage_01_findings.csv
```

## Customer Requirement HTML Report

The HTML report must include:

- total counts by result category
- evidence and regulatory baseline used
- one row per requirement item
- columns: ID, section, item, customer requirement, result, regulation/standard, reason, evidence source, recommended action when applicable
- clear highlighting for conforming, follow-up validation, potential nonconforming, and non-regulatory items
- key issues summary

## Finding Format

Use this schema for `stage_01_findings.csv`:

```csv
finding_id,severity,check_area,expected,observed,source_evidence,status,next_action
```

Severity:

- `critical`: wrong product type, wrong sales region, or wrong regulatory path that affects market access
- `major`: missing required legal evidence or unsupported 510(k)/exemption claim
- `minor`: wording inconsistency that does not change the regulatory path
- `info`: evidence is present but should be captured more cleanly
