# US Forehead Thermometer Regulatory Baseline

Source stage: Stage 01 project approval / customer requirement stage

Product identity baseline:

- Product model: `PT9L`
- Product category: infrared no-touch forehead thermometer / forehead thermometer
- Sales region: USA

This page defines the US regulatory baseline that later DHF/DMR files should align with.

## Conclusion

The local regulation PDF package from PT9L stage 13 already contains many applicable consensus standards, but it does not fully contain the US CFR legal basis pages.

For PT9L, the Stage 01 check package should therefore use two layers:

1. US legal/regulatory requirements that must be present or referenced.
2. FDA-recognized or product-applicable standards already available in the stage 13 regulation package.

## Core US Legal / FDA Regulatory Requirements

| Requirement | Current status | Local evidence status | Latest-version check |
| --- | --- | --- | --- |
| `21 CFR 880.2910 Clinical electronic thermometer` | Required baseline for US clinical electronic thermometer classification | Missing from local regulation PDF package; needs official local capture/download | Current as amended at `90 FR 25891`, effective `2025-06-18` |
| `21 CFR 880.9 Limitations of exemptions` | Required when relying on 510(k) exemption | Missing from local regulation PDF package; needs official local capture/download | Should be checked from current eCFR before final audit |
| `21 CFR 807 Subpart E Premarket Notification 510(k)` | Applies if device is not exempt; also useful as conditional requirement | Missing from local regulation PDF package; needs official local capture/download | Current FDA process uses electronic 510(k) / eSTAR unless exempt |
| `21 CFR 801 Labeling` | Required labeling baseline | Listed in design input as `21CFR 801 Labeling`, but official CFR text not locally present | Should be checked from current eCFR before final audit |
| FDA product code `SDV Clinical Electronic Thermometer` | Relevant after 2025 exemption rule for intermittent clinical electronic thermometers | Not locally captured | FDA TPLC page checked via web search; page last updated `2026-04-13` |
| FDA product code `FLL Continuous Measurement Thermometer` | Non-exempt continuous measurement thermometer; conditional exclusion check | Not locally captured | Current rule distinguishes `FLL` from exempt `SDV` |

## 510(k) Exemption Logic For PT9L

Under the current `21 CFR 880.2910`, certain Class II clinical electronic thermometers are exempt from premarket notification if all conditions are met:

- The device is not a clinical thermometer with telethermographic functions.
- The device is not a clinical thermometer with continuous temperature measurement functions.
- Appropriate analysis and testing validates specifications and performance using currently FDA-recognized standards such as `ISO 80601-2-56`, `ASTM E1965`, `ASTM E1112`, or `ASTM E1104`.

Stage 01 PT9L evidence describes intermittent forehead temperature measurement, so the initial direction is `SDV / 510(k)-exempt if conditions are met`, not automatic 510(k). However, because the project customer requirements mention `510k`, final audit should record whether the project followed the pre-2025 path, a conservative path, or the current exemption path.

## Local Standards Already Available In Folder 13

| Standard / Guidance | Local converted evidence | Applicability | Latest-version check |
| --- | --- | --- | --- |
| `ASTM E1965-98 (2023)` | See `PT9L_MD/_manifests/regulation_pdf_manifest.csv`, source_file `ASTM E1965-98 (2023).pdf` | Infrared thermometer performance and labeling support | Current reapproved 2023 edition found locally |
| `ISO 80601-2-56:2017 + AMD1:2018` | See regulation manifest, source_file `ISO 80601-2-56-2017+AMD1-2018.pdf` | Clinical thermometer basic safety and essential performance | FDA-recognized edition remains 2017 + AMD1:2018; ED3 is in development, not published as replacement |
| `EN ISO 80601-2-56:2017+A1:2020` | See regulation manifest, source_file `EN ISO 80601-2-56-2017+A1-2020.pdf` | EU/harmonized version, secondary for US baseline | Available locally, but US check should prioritize FDA-recognized ISO edition |
| `IEC 60601-1:2005+AMD1:2012+AMD2:2020` | See regulation manifest, source_file `IEC 60601-1-2020.pdf` | Electrical safety | Available locally; text layer sparse, use page images/OCR if needed |
| `IEC 60601-1-2:2014+AMD1:2020` | See regulation manifest, source_file `IEC 60601-1-2-2014+AMD1-2020.pdf` | EMC | Available locally |
| `IEC 60601-1-11:2015+AMD1:2020` | See regulation manifest, source_file `IEC 60601-1-11-2015+AMD1-2020.pdf` | Home healthcare environment | Available locally |
| `IEC 62366-1:2015+AMD1:2020` | See regulation manifest, source_file `IEC 62366-1 AMD 1-2020.pdf` | Usability engineering | Available locally; scanned/text sparse, use targeted OCR if needed |
| `ISO 14971:2019` | See regulation manifest, source_file `ISO14971-2019.pdf` | Risk management | Available locally |
| `ISO/TR 24971:2020` | See regulation manifest, source_file `ISO-TR-24971-2020.pdf` | Risk management guidance | Available locally |
| `ISO 20417:2021` | See regulation manifest, source_file `ISO 20417-2021.pdf` | Information supplied by manufacturer | Available locally |
| `FDA Human Factors Guidance (2016)` | See regulation manifest, source_file `FDA Guidance Applying Human Factors and Usability Engineering to Medical Devices (2016).pdf` | Human factors / usability support | Available locally |
| `FDA Reprocessing Guidance (2015, updated 2017)` | See regulation manifest, source_file `FDA Guidance Reprocessing Medical Devices in Health Care Settings Validation Methods and Labeling (2015, updated 2017).pdf` | Cleaning/reprocessing labeling where applicable | Available locally |

## Missing Items To Download Or Capture

Before finalizing the regulatory audit, create local evidence copies for:

- Current eCFR `21 CFR 880.2910`
- Current eCFR `21 CFR 880.9`
- Current eCFR `21 CFR 807 Subpart E`
- Current eCFR `21 CFR 801`
- FDA TPLC/Product Classification page for `SDV`
- FDA TPLC/Product Classification page for `FLL`
- FDA recognized consensus standard detail page for `ISO 80601-2-56`
- FDA recognized consensus standard detail page for `ASTM E1965`

These are not present in the current stage 13 converted PDF package.

## Stage 01 Check Use

For the `01` stage, verify that:

- The product is identified as an infrared no-touch forehead thermometer, not an ear thermometer or nebulizer.
- The sales region is USA.
- The regulatory baseline includes `21 CFR 880.2910`.
- The 510(k) pathway is interpreted conditionally under the latest 2025 exemption rule.
- The applicable performance validation standards include `ISO 80601-2-56` and/or `ASTM E1965`.
