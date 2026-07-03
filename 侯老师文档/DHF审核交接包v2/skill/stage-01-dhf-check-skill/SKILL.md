---
name: stage-01-dhf-check-skill
description: Checks Stage 01 DHF project approval/customer requirement evidence for product identity, sales region, product category, personnel list, customer requirements versus regulations, US forehead thermometer regulatory baseline, missing legal evidence, and latest-version status. Use when auditing 01 stage files, PT9L_CHECK, project approval, customer requirement, personnel/responsibility list, requirement-by-requirement regulatory checks, US sales, forehead thermometer, 21 CFR 880.2910, 510(k), FDA SDV/FLL, ASTM E1965, or ISO 80601-2-56.
---

# Stage 01 DHF Check Skill

## Purpose

Use this skill for the first content-audit stage of DHF/DMR projects.

Stage 01 establishes the baseline identity of the product and the regulatory baseline for the sales region. Later DHF/DMR checks must compare against this baseline.

For PT9L, the known baseline is:

- Model: `PT9L`
- Product type: infrared no-touch forehead thermometer
- Sales region: USA
- Stage 01 check folder: `PT9L_CHECK/02_RnD_DHF/01 ...`

Avoid hardcoding Chinese path names inside scripts or machine-readable files. Prefer manifests, discovered paths, stable English labels, and source filenames.

## Required Inputs

Read these before making a conclusion:

- Converted Stage 01 Markdown and assets under `PT9L_MD/02_RnD_DHF/01 ...`
- Existing Stage 01 check files under `PT9L_CHECK/02_RnD_DHF/01 ...`
- Regulation manifest: `PT9L_MD/_manifests/regulation_pdf_manifest.csv`
- Stage 13 converted regulation evidence under `PT9L_MD/02_RnD_DHF/13 ...`
- Current official FDA/eCFR/Federal Register evidence when checking latest-version status

For any Excel-derived evidence, inspect the Excel assets, not only the Markdown:

- sheet CSV/Markdown
- sheet page PNG/PDF
- text object manifest
- visual format manifest
- semantic findings
- conversion loss report

## Stage 01 Check Scope

Stage 01 has two jobs:

1. Extract the baseline content that later DHF/DMR files must not contradict.
2. Check whether the customer requirements are at least as broad/strict as the applicable regulatory baseline.

## Required Extraction Content

Extract these fields first:

- Product model
- Product name
- Product category: forehead thermometer, ear thermometer, nebulizer, or other
- Sales region
- Registration path or registration responsibility
- Personnel list and responsibilities:
  - project leader
  - compiler/drafter
  - reviewer/approver
  - business owner
  - structure, hardware, software, certification, quality, resource, introduction, and customer representative roles when present
- Customer and intended market assumptions
- Customer requirement items from all Stage 01 customer requirement sections:
  - general requirements
  - performance specifications
  - function specifications
  - component/subassembly specifications
  - packaging, transport, environmental, usability, warning, labeling, and special requirements

## Required Check Content

For each extracted customer requirement item, check:

- Whether it is a direct legal/regulatory requirement, consensus-standard requirement, customer/business requirement, or non-regulatory item.
- Whether the requirement is broader/stricter than the regulation, not narrower/weaker.
- For range requirements, the customer range must cover the regulatory minimum range.
- For error/accuracy/risk requirements, the customer limit must be equal to or stricter than the regulatory limit.
- For warning/display/labeling/usability requirements, the customer requirement must at least cover the regulatory requirement.
- For items with no direct numeric regulatory limit, mark as `needs_followup_validation` instead of guessing.
- For non-regulatory items, mark as `non_regulatory_item`, but still preserve them for traceability.
- For every `nonconforming` or `potential_nonconforming` item, do not stop at the conclusion. Provide:
  - the exact regulation/standard requirement;
  - what the customer requirement, IFU/manual, label, or design input currently claims;
  - why the current claim is narrower/weaker or unsupported;
  - a practical remediation path, such as revising the requirement, revising the IFU/manual claim, adding a mode distinction, adding verification evidence, or documenting an applicability/no-applicability rationale in the regulation list.
- Split uncertain early-stage items into two levels:
  - `evidence_required_now`: the trigger is already known from the requirement, BOM, design decision, sales state, label, or existing evidence. Require evidence or a documented no-applicability rationale.
  - `prompt_for_later`: the trigger is not known yet, such as battery chemistry, final packaging material, sales states, PFAS content, or environmental marketing claims. Record a prompt question, but do not mark it as missing evidence at Stage 01.

When the file uses EU evidence for a US sales project, do not accept it automatically. Apply this evidence-chain test:

- Identify the exact US requirement triggered by product, packaging, battery, sales state, claim, or material.
- Identify what evidence that US requirement needs: test report, supplier declaration, exposure assessment, warning decision, label, transport document, state registration, or no-applicability rationale.
- Check whether the EU report covers the same material/component/revision and the same substance or hazard.
- If it covers the same technical fact, reuse it as supporting evidence.
- If the US rule needs a different decision, warning, state screen, or report, mark a US-specific gap.
- Example: EU RoHS can support restricted-substance material evidence, but it does not replace California Prop 65 exposure/warning decision, TSCA/PFAS reporting applicability, US state packaging rules, button/coin battery rules, lithium transport rules, state battery recycling/e-waste screens, or FTC Green Guides claim substantiation.
- Battery example: do not require `UL 4200A` or `UN 38.3` at Stage 01 if the battery type is not known. Prompt for battery type. If the product evidence already says AAA/LR03 alkaline, preserve that evidence and mark button/coin and lithium-specific rules as not triggered for the current design.
- Temperature-display example: if the customer requirement/manual says `32.0C-42.9C` but the applicable ASTM E1965 skin infrared thermometer displayed/subject range requires coverage such as `22C-40C`, mark it as potential nonconforming and give the fix path. The fix may be to expand the display/subject range and verify it, or to state clearly in the IFU/manual that `32.0C-42.9C` is only `body mode` / clinical measuring range while separately documenting the ASTM display/subject range. If the project does not claim that ASTM display range applies, the regulation list must document the alternative applicable regulation/standard path and the no-applicability rationale.

For US forehead thermometer projects, customer requirements must be checked against at least:

- `21 CFR 880.2910` device classification and exemption conditions
- `21 CFR 807` or 510(k) path when claimed or not exempt
- `21 CFR 801` labeling baseline
- `ASTM E1965` infrared thermometer scope, displayed temperature range, accuracy, resolution, warning signs, construction, and labeling
- `ISO 80601-2-56` clinical thermometer basic safety and essential performance
- `IEC 60601-1-11` home healthcare environment where home use is claimed
- `IEC 60601-1-2` EMC where applicable
- `IEC 62366-1` and FDA human factors guidance for use/error-prone interfaces
- `ISO 14971` risk-management-dependent requirements
- `ISO 20417` information supplied by manufacturer

For US forehead thermometer projects, prepare and maintain a regulatory baseline package:

- `21 CFR 880.2910 Clinical electronic thermometer`
- `21 CFR 880.9 Limitations of exemptions`
- `21 CFR 807 Subpart E Premarket Notification 510(k)` when the device is not exempt or when the file claims 510(k)
- `21 CFR 801 Labeling`
- FDA product classification / TPLC for `SDV Clinical Electronic Thermometer`
- FDA product classification for `FLL Continuous Measurement Thermometer` as an exclusion check
- FDA recognized consensus standard pages for `ISO 80601-2-56` and `ASTM E1965`
- Local standards from Stage 13, including `ASTM E1965-98 (2023)` and `ISO 80601-2-56:2017 + AMD1:2018`

## Current PT9L Regulatory Interpretation

As of the latest check in this project:

- `21 CFR 880.2910` was amended by `90 FR 25891`, effective `2025-06-18`.
- Certain Class II clinical electronic thermometers are 510(k)-exempt if they meet the exemption limitations.
- Exemption conditions include:
  - not telethermographic
  - not continuous temperature measurement
  - performance/specifications validated with currently FDA-recognized standards such as `ISO 80601-2-56`, `ASTM E1965`, `ASTM E1112`, or `ASTM E1104`
- Intermittent forehead thermometers should be checked against FDA product code `SDV`.
- Continuous measurement thermometers should be checked against product code `FLL` and are not the same exemption path.
- `ISO 80601-2-56:2017 + AMD1:2018` remains the FDA-recognized edition found during the project check; ED3/DIS is under development and must not be treated as the replacement until officially published and recognized.
- `ASTM E1965-98 (2023)` is locally available in the Stage 13 regulation package.

Always re-check official sources for latest-version status before a final audit report. Do not rely only on memory.

## Mandatory Workflow

1. Load the general working method skill first:
   - `D:/AI_0415/03DHF/skill/SKILL.md`

2. Locate Stage 01 source evidence.
   - Use manifests and file discovery.
   - Do not trust terminal mojibake.
   - Do not mark missing until wrapper folders, invisible spaces, and manifests are checked.

3. Extract product identity and personnel baseline.
   - Record exact source document names and evidence locations.
   - If a field appears in Excel, verify via sheet visual/page evidence.
   - If a field conflicts across documents, record both values and mark a discrepancy.
   - Extract personnel from review participants, signature tables, approval fields, version history, headers/footers, and text boxes.
   - Keep names traceable to the source document and role. If the same person appears under multiple roles, record each role.

4. Build or update Stage 01 check outputs under `PT9L_CHECK`.
   Required outputs:
   - `stage_01_core_fields.md`
   - `us_forehead_thermometer_regulatory_baseline.md`
   - `us_regulatory_evidence_index.csv`
   - `customer_requirements_vs_regulations_report.html`
   - optional reproducible report script, for example `generate_customer_requirements_vs_regulations_report.py`
   - `stage_01_check_report.md` when doing a full check
   - `stage_01_findings.csv` when discrepancies are found

5. Extract and check customer requirements.
   - Use Excel assets for customer requirement workbooks: sheet CSV/Markdown, visual page evidence, text objects, structure manifest, semantic findings, and conversion loss.
   - Do not rely only on clipped Markdown previews for wide Excel sheets.
   - Compare every customer requirement row against the regulatory baseline.
   - Produce an HTML report with one row per requirement item: ID, section, item, customer requirement, result, regulation/standard, reason, and evidence source.
   - Highlight `nonconforming` or `potential_nonconforming` rows clearly.
   - For every highlighted issue, include a `recommended_action` / remediation method so the report tells the team how to close the issue, not only that it failed.
   - The PT9L precedent report is `customer_requirements_vs_regulations_report.html`.

6. Prepare the US regulatory baseline package.
   - First use local Stage 13 evidence where available.
   - For missing CFR/FDA pages, download/capture official current evidence when possible.
   - If direct eCFR fetch is blocked, use Federal Register, FDA pages, official APIs, or clearly mark the evidence as pending official capture.

7. Check latest-version status.
   - Separate "standard exists locally" from "standard is current/latest".
   - Separate legal requirements from consensus standards.
   - Mark status as `available`, `missing`, `listed_only`, `needs_current_check`, or `official_capture_pending`.

8. Interpret 510(k) carefully.
   - Do not assume every US forehead thermometer requires 510(k).
   - Do not assume every US forehead thermometer is exempt.
   - Decide based on the device functions and the latest `21 CFR 880.2910` exemption conditions.
   - If the project files mention 510(k), record whether this is old-path, conservative-path, customer-requested, or current-path evidence.

9. Write findings as actionable checks.
   Each finding should include:
   - field or requirement
   - expected baseline
   - observed value
   - source evidence
   - severity
   - next action

## Output Quality Rules

- Keep machine-readable files ASCII-safe when possible.
- Do not store question-mark mojibake strings in baseline files.
- Use manifest references such as `regulation_pdf_manifest.csv source_file=...` instead of fragile Chinese paths.
- Preserve source traceability for every conclusion.
- Mark unknowns explicitly; do not fill regulatory gaps by guessing.
- End user-facing replies with the Chinese meow character required by the general working method.

## Quick Checklist

- [ ] Product model confirmed
- [ ] Product category confirmed
- [ ] Sales region confirmed
- [ ] Personnel list and responsibility roles confirmed
- [ ] Customer requirement items extracted from all Stage 01 sections
- [ ] Customer requirements checked item-by-item against regulations/standards
- [ ] HTML customer-requirements-vs-regulations report generated
- [ ] US regulatory baseline file exists
- [ ] Evidence index CSV exists
- [ ] Local Stage 13 standards mapped
- [ ] Missing CFR/FDA pages listed
- [ ] Latest-version status checked or marked pending
- [ ] 510(k) path interpreted conditionally
- [ ] No question-mark mojibake remains in check outputs
