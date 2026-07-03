# PT9L 高优先级语义审查问题清单

> 生成时间：2026-06-30T15:36:40
> 范围：仅保留 P1 且 Challenge Agent 裁决为 keep/revise 的语义 findings，适合作为人工复核第一批入口。

## 1. 摘要

- 高优先级问题：19
- keep：18
- revise：1

## 2. 问题清单

### 1. 主范围风险评估报告（F0018）正文两处均出现旧型号PT3SBT，预期用途描述与PT9L项目不符。

- Finding ID：`LLM-0002`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- Challenge：`keep`
- 裁决理由：三条证据均直接命中：line 239封面明确写'产品型号:PT3SBT'，line 187和line 293的BOM编号前缀均为PT3SBT（PT3SBT-PBOM01、PT3SBT-ABOM01）。证据与claim高度一致，设计输出清单二封面及内容型号均为PT3SBT而非PT9L，属于DMR核心文件型号错误，结论成立，严重度P1合理。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea

### 2. 03风险分析文件夹中存在两套结构相同的风险管理文件（F0017-F0020无PT9L前缀 vs F0021-F0023有PT9L前缀），受控版本不明确。

- Finding ID：`LLM-0003`
- Agent：Market & Category Scout Agent
- 类型：`duplicate_risk_file_set_without_clear_control`
- Challenge：`keep`
- 裁决理由：三条证据均直接支持结论：line 2文件标题明确为'结构设计方案评审检查表-血压计E0 23.11'；line 17和line 18的FMEA内容明确描述血压计功能（给血压计供电、包装血压计、腕枕等血压计专属部件）。血压计与红外体温计属不同品类，法规标准体系差异显著，此类文件混入PT9L DHF属于实质性文件管理错误，结论成立，严重度P1合理。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:16` **Reviewed by** *(Certification Engineer)* Date:
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->

### 3. 正式实验报告（F0458，PT9L -2-56测试报告）中引用的风险管理报告文件号为PT9C-FXGB01，与PT9L项目文件号体系不一致。

- Finding ID：`LLM-0004`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_test_report`
- Challenge：`keep`
- 裁决理由：三条证据（line 577、578、579）均直接命中，测试报告在4.2、4.3、4.4条款中连续引用'Risk Management Report (file No.: PT9C-FXGB01 V1.0)'，而PT9L对应风险管理报告文件号应为IFT-FXGB01。PT9C为另一型号，文件号体系不一致在认证审查中属于可被质疑的一致性缺陷，结论成立，严重度P1合理。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:578` \| 4.3 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Hazard analysis recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:579` \| 4.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk estimation recorded \| P \|

### 4. PT9L T1样机文件夹中存在PT3SBT标签审核表，且检查记录引用PT2L标签文件，旧型号残留污染主范围文件，法规证据归属不清。

- Finding ID：`LLM-0011`
- Agent：Regulatory Agent
- 类型：`old_product_contamination_in_primary_scope`
- Challenge：`keep`
- 裁决理由：证据直接：文件路径明确位于PT9L T1样机目录下，文件名含'PT3SBT'型号标识，内容涉及血压计电池仓标识条款，与PT9L红外体温计产品无对应关系。跨型号文件混入DHF目录构成文件边界污染，法规审查时存在被误认为PT9L有效证据的风险，结论成立，严重度P1合理。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:20` \| 标准名称 \| 适用性 \|  \| 标签类型 \|  \|  \|  \|  \| 检查记录 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:22` \| IEC 60601-1 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ01 V1.0 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:23` \| IEC 60601-1-2 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ02 V1.0 \|

### 5. 风险评估报告和FMEA均引用IEC 60601-1作为适用标准，但红外体温计通常为非电气设备，IEC 60601-1适用性需正式说明。

- Finding ID：`LLM-0016`
- Agent：Regulatory Agent
- 类型：`iec_60601_1_applicability_questionable_for_ift`
- Challenge：`keep`
- 裁决理由：证据明确：文件标题、路径、图片资产均标注BP3L，且该文件物理位于PT9L的07软件设计方案目录下。BP3L为血压计，与PT9L红外体温计属不同品类，软件图样不存在共用合理性。文件残留导致DHF边界不清的结论直接成立，无误报迹象。严重度P1合理，跨品类文件污染对法规审查影响显著。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:62` 3.3 Questions from IEC 60601-1:2005+AMD1:2012+AMD2:2020 Edition 3.2 8
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:64` 3.4: Additional questions arising from IEC 60601-1-2:2014+A1:2020 edition 4.1: 13
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:177` ### .3 Questions from IEC 60601-1:2005+AMD1:2012+AMD2:2020 Edition 3.2

### 6. 设计验证报告文件名含'EN1060-1项'，EN 1060-1为血压计标准，疑为旧品类模板残留，影响验证报告与IFT法规要求的对应关系。

- Finding ID：`LLM-0017`
- Agent：Regulatory Agent
- 类型：`design_verification_report_title_references_blood_pressure_standard`
- Challenge：`keep`
- 裁决理由：证据明确：文件名含PT3SBT，内容型号为PT2L，物理路径位于PT9L的11 T1样机目录下。PT3SBT与PT2L均为旧型号，与PT9L无关联，不存在合理的共用或引用场景。DMR文件污染结论直接成立。严重度P1合理，T1样机阶段出现无关型号标签审核表可能误导制造和审查决策。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:23` \| 1 \| 温度显示范围 \| 32.0℃～42.9℃ \| □手板■T1□设计确认 \| 参见《PT9L红外体温计产品检验标准V1.0 》第6项 \| 全部测试结果均需符合《PT9L红外体温计产品检验标准V1.0》中第6项的要求 \| 参见《PT9L红外体温计检测报告 V1.0》中第6项测试结果 \| 合格 \|
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:24` \| 2 \| 显示分辨力 \| 0.1℃ \| □手板■T1□设计确认 ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（一）EN1060-1项_image_001.png) ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:25` \| 3 \| 测量误差 \| ≥35℃且≤42℃：±0.2℃，其它：±0.3℃ \| □手板■T1□设计确认 ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（一）EN1060-1项_image_001.png) ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_

### 7. 机芯BOM中存在旧型号PT9C的PCB料号，与PT9L项目不符，可能导致验证闭环断裂。

- Finding ID：`LLM-0021`
- Agent：Hardware Agent
- 类型：`bom_pcb_cross_contamination`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：三条evidence分别显示IFT-FXJH01 V1.0与PT9L-FXJH01 V1.0两套文件同时存在于03风险分析目录，且F0018（IFT-FXPJ01 V2.0）与对应PT9L版本（V1.0）版本号不一致。两套文件无废止标记，审查员无法判断受控有效版本，构成法规闭环风险。证据充分，非误报，维持P1。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 8. 整机寿命测试报告存在三个版本文件（F0084、F0085、F0095），文件编号相同但来源不同，版本控制状态不明确。

- Finding ID：`LLM-0026`
- Agent：Hardware Agent
- 类型：`duplicate_life_test_report_version_control`
- Challenge：`keep`
- 裁决理由：证据直接显示T阶段设计验证报告封皮三个子报告均为□未勾选（line 22、24等），而子报告内容（VV-088~VV-097）已存在，封皮与内容脱节事实清晰。按21 CFR 820.30(f)要求，验证记录须完整关联，空选封皮构成形式上的验证闭环缺失，不属于误报。P1严重度合理，因其直接影响审查员对验证完成状态的判断。
- 证据：
  - `11 T1样机\PT9L产品寿命测试报告.via_lo_html.clean.md:6` 文 件编号： PT9L-PLER01 V1.0 整机寿命评估报告
  - `11 T1样机\整机寿命测试报告2020-3-25.via_lo_html.clean.md:6` 文 件编号： PT9L-PLER01 V1.0 整机寿命测试报告
  - `11 T1样机\整机寿命测试报告2020-3-25.via_lo_html.clean.md:12` \| **测试目的： PT9L 寿命测试** \| **测试时间：** \|

### 9. 结构类FMEA中电池功能描述为"给血压计供电"，与PT9L红外体温计品类不符。

- Finding ID：`LLM-0027`
- Agent：Hardware Agent
- 类型：`structural_fmea_product_type_error`
- Challenge：`keep`
- 裁决理由：证据显示设计确认阶段封皮结论栏'☐设计验证合格'为未勾选状态（VV-111），而通用要求和法规标准部分已☑（VV-109、VV-110），形成内部矛盾。文件名含'加结论'字样，说明该栏位本应被填写，空白属于遗漏而非设计。21 CFR 820.30(g)明确要求设计确认须有书面结论，此finding核心成立，非误报。P1严重度合理。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17` \|  \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \|  \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \|  \|  \| □ \|

### 10. 多份样机评审检查表中所有检查项结果栏均为空白（无通过/不通过/不适用勾选），评审完成状态无法确认。

- Finding ID：`LLM-0028`
- Agent：Hardware Agent
- 类型：`sample_review_checklist_result_blank`
- Challenge：`keep`
- 裁决理由：证据明确显示T1样机文件夹下所有生物相容性报告路径均含'同PT5生物相容性报告'，报告编号为PT5专属系列（SDWH-M201905262），无任何PT9L标识。DHF中未见桥接评估或材料等同性声明文件。ISO 10993要求对被评价器械本身进行评价或提供充分的等同性论证，跨型号直接引用且无说明文件构成实质性法规符合性风险。P1严重度合理，不属于误报。
- 证据：
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:16` \| 2 \| 装 配 检 查 \| 电池盖配合 \|  \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:29` \| 15 \| 装 配 检 查 \| 电池弹簧固定 \|  \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:34` \| 20 \| 装 配 检 查 \| PCB固定 \|  \| □通过 □不通过 □不适用 \|

### 11. PT9L机芯类组件清单中PCB图号引用PT9C旧型号文件编号，存在设计输出与当前型号不一致的法规风险

- Finding ID：`LLM-0031`
- Agent：Software Agent
- 类型：`legacy_model_pcb_reference_in_bom`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件路径确认该图纸归档于PT9L DHF设计输出清单二，而图纸标题、来源注释均明确标注为PT3项目原件，仅以'共用件/设计参照'注释归档，缺乏正式跨型号受控引用程序。无论PT9L是否实际使用该弹簧，均存在法规可追溯性缺陷（21 CFR 820.30(d)/ISO 13485 7.3.4要求设计输出可追溯至设计输入）。非误报，核心问题成立，严重度P1合理。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 12. PT3SBT/PT2L旧型号标签审核表存放于PT9L T1样机文件夹，文件内容与PT9L无关，构成旧型号资料残留

- Finding ID：`LLM-0032`
- Agent：Software Agent
- 类型：`legacy_model_label_document_in_t1_folder`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：两份独立文件（外观图与外箱图纸）的Drawing NO.均为PT9L-F01，且解析报告中已明确标注冲突警告。图号唯一性是受控图纸管理的基本要求，重复图号将导致制造、采购、质检无法通过图号唯一定位文件，属于配置管理实质性缺陷。非误报，严重度P1合理。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:16` \| ▉说明书 □彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-SMSP09 \|  \|  \|  \|  \|

### 13. 风险管理报告（F0020）文件名标注IFT-FXGB01 V2.0，但正文文件号字段显示PT9L-FXGB01 V1.0，文件号与版本号双重矛盾。

- Finding ID：`LLM-0039`
- Agent：Risk Traceability Agent
- 类型：`document_number_internal_contradiction`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：同一文件的文件名标注IFT-FXGB01 V2.0，正文DN字段显示PT9L-FXGB01 V1.0，品类前缀（IFT vs PT9L）和版本号（V2.0 vs V1.0）均存在矛盾，属于文件受控管理的实质性缺陷，影响风险管理文件的可追溯性和法规提交依据的确定性。P1严重度合理。
- 证据：
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:2` # Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:6` DN ： PT9L -FXGB01 V 1 .0 Risk Management Report

### 14. F0022（PT9L版风险评价报告）文件名标注V2.0，但正文DN字段显示PT9L-FXPJ01 V1.0，版本号不一致。

- Finding ID：`LLM-0041`
- Agent：Risk Traceability Agent
- 类型：`risk_assessment_report_version_mismatch`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名标注V2.0（line 2），正文DN字段明确写入V1.0（line 6），两者不一致事实清晰；可追溯性分析报告（line 18）引用PT9L-FXPJ01 V1.0，若受控版本实为V2.0则引用链断裂，追溯闭环受损。非误报，核心问题成立。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:6` D N ： PT9L-FXPJ01 V1.0 Risk Assessment Report
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:18` \| 软件需求分析阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \|  \| 相关文档之间的信息描述都是准确的 \|  \| 相关文档之间的信息都是正确的，没有歧义信息 \|  \| 相关文档已包含软件必需信息，陈述所有功能 \|  \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### 15. F0023（PT9L版风险控制验证报告）文件名标注V2.0，但正文DN字段显示PT9L-FXYS01 V1.0，版本号不一致。

- Finding ID：`LLM-0042`
- Agent：Risk Traceability Agent
- 类型：`risk_control_verification_report_version_mismatch`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名含V2.0，正文DN字段明确写入PT9L-FXYS01 V1.0（line 6），版本号不一致；可追溯性分析报告（line 32）引用V1.0，若受控版本为V2.0则剩余风险评估闭环证据链存疑。与LLM-0041属同类问题，均有直接文本支撑，非误报。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:6` D N: PT9L-FXYS01 V1.0 Verification of risk control measure and residual risk evaluation r eport
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:32` \| 用户测试阶段 \| 风险管理 \| 风险控制措施验证以及剩余风险评估报告PT9L-FXYS01 V1.0<br>风险管理报告<br>PT9L-FXGB01 V1.0 \|  \| 相关文档之间的信息描述都是准确的 \|  \| 相关文档之间的信息都是正确的，没有歧义信息 \|  \| 相关文档已包含软件必需信息，陈述所有功能 \|  \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### 16. 结构类DFMEA（F0074）严重度评分表中明确写入"影响血压计的安全运行"，品类描述与PT9L红外体温计不符，构成旧品类残留。

- Finding ID：`LLM-0043`
- Agent：Risk Traceability Agent
- 类型：`dfmea_wrong_product_category_residual`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：结构类DFMEA严重度评分表line 542和line 543均明确写入'影响血压计的安全运行'，而该文件归属PT9L红外体温计项目，品类描述错误属实。严重度准则描述错误将直接影响RPN评分适用性，进而影响所有依赖该DFMEA的风险控制结论有效性，P1定级合理。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:542` \|  \| 无警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时无预警。会危及使用者。 \| 10 \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:543` \|  \| 有警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时有预警。会危及使用者。 \| 9 \|

### 17. 设计确认阶段验证报告封皮中"设计验证合格"结论项为"☐"（未勾选），设计确认闭环结论缺失。

- Finding ID：`LLM-0051`
- Agent：V&V Agent
- 类型：`design_confirmation_cover_pass_not_checked`
- Challenge：`keep`
- 裁决理由：证据直接且明确：line 28显示"☐设计验证合格"未勾选，而line 22和line 24显示两个子报告均已勾选（☑），形成鲜明对比。封皮汇总结论项空白导致设计确认阶段无法形成法规要求的正式通过声明，属于设计确认闭环缺失的实质性问题。证据充分支持P1定级，无误报迹象。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:28` ☐设计验证合格：所有设计验证项目已按照相应的设计验证计划进行，都已验证通过合格。
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:22` ☑设计验证报告－通用要求部分 文件编号： PT9L-Q1TY01 V1.0
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:24` ☑设计验证报告－法规标准部分 文件编号： PT9L-Q1BZ01 V1.0

### 18. PT9L DHF设计输出清单二中归档了型号为PT3的双联弹簧图纸（Drawing NO. PT3-P10，Model NO. PT3），该图纸属于PT3项目原件，非PT9L设计输出，存在法规/验证闭环风险。

- Finding ID：`LLM-0060`
- Agent：DMR/SOP Agent
- 类型：`legacy_model_drawing_in_dhf`
- Challenge：`revise`
- 裁决理由：核心问题成立：PT3图纸（Drawing NO. PT3-P10，Model NO. PT3）归档于PT9L DHF设计输出清单二，且现有EBOM证据中未见PT3-P10条目，验证闭环存在断裂风险，P1严重度合理。但'借用归档（外购件/设计参照）'注释存在歧义——若该件仅作设计参照而非实际用于PT9L产品，则EBOM中不出现属正常情况，闭环断裂结论需修正。建议将claim表述调整为：'PT3图纸归档于PT9L DHF但EBOM中无对应条目，需明确该零件是否实际用于PT9L；若实际使用则存在验证闭环断裂，若仅为设计参照则需在DHF中补充说明以避免审查歧义'，严重度维持P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:1` # PT3 双联弹簧 REV01 (V1.0) 2D 图读图报告
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT3_双联弹簧_REV01.pdf`
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:6` > **共用件**：**PT3 项目原件**，被 PT9L DHF 借用归档（外购件 / 设计参照）

### 19. 两份包装BOM文件（F0161和F0162）均声称是PT9L包装BOM（美版），但文件编号不一致：F0161为PT9L-PBOM01 V1.0，F0162为PT9L-PB0M1 V1.0（字母O与数字0混用），构成受控文件唯一性风险。

- Finding ID：`LLM-0061`
- Agent：DMR/SOP Agent
- 类型：`packaging_bom_document_number_inconsistency`
- Challenge：`keep`
- 裁决理由：证据直接支持结论。两份独立文件中均可见文件编号差异：F0161为'PT9L-P BOM01 V1.0'，F0162为'PT9L-PB0M1 V1.0'（B后为数字0而非字母O）。两处证据来自不同文件路径，非同一文档重复引用。字母O与数字0混用在受控文件编号中构成真实的唯一性风险，符合P1严重度定义。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:8` andon文件编号：PT9L-P BOM01 V1 . 0 PT9L包装BOM(美版)【组件清单】
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:8` \| ![PT9L包装BOM_image_001.png](PT9L包装BOM.via_xlsx_assets/PT9L包装BOM_image_001.png) \|  \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:10` \|  \|  \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

## 3. 人工复核建议

- 第一轮先确认这些问题是否属于正式受控文件范围，而不是历史/废案/参考资料。
- 对 keep 项建议直接进入责任人确认；对 revise 项建议先改严重度或措辞，再进入整改台账。
- `needs_more_context` 的语义 finding 仍保留在全量报告中，建议作为第二轮复核对象。