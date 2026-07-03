# Prompt Template - DMR Manufacturing SOP Check

Audit the DMR / manufacturing SOP package for product `{product_identity}`.

Inputs:

- DMR converted folder: `{dmr_folder}`
- DMR master record detail: `{dmr_master_record}`
- Stage 09 design-output check package: `{stage_09_package}`
- Stage 10 trial-production check package: `{stage_10_package}`
- Stage 11 design-validation/content audit package: `{stage_11_package}`
- Output folder: `{output_folder}`

Rules:

- Read the DMR master record detail first.
- Use the master record as the DMR order and file-list baseline.
- Extract file name, file number, version, effective date, category/part, and remarks.
- Check each DMR group from body content: WI, QI, process control plan, PFMEA, component list, incoming/system procedures, packaging/label controls, and DHR record readiness.
- Map DMR content to DHF outputs and to shop-floor actual operation.
- Do not close from title, filename, document number, or master-list entry alone.
- Do not claim DMR readiness until Stage 10 DMR suitability and key approvals are closed.

Required outputs:

- `dmr_mfg_sop_baseline.md`
- `dmr_check_items.md`
- `dmr_findings.csv`
- `dmr_dhf_traceability_matrix.csv`
- `dmr_check_items_closure_matrix.csv`
- `dmr_mfg_sop_check_report.html`
