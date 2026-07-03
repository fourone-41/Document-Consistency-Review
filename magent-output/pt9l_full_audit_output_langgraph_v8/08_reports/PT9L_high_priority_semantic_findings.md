# PT9L 高优先级语义审查问题清单

> 生成时间：2026-07-01T16:12:34
> 范围：仅保留 P1 且 Challenge Agent 裁决为 keep/revise 的语义 findings，适合作为人工复核第一批入口。

## 1. 摘要

- 高优先级问题：20
- keep：18
- revise：2

## 2. 问题清单

### 1. 主范围风险评估报告（F0018）中预期用途描述使用旧型号PT3SBT而非PT9L，构成法规文件型号错误。

- Finding ID：`LLM-0001`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_residual_in_primary_scope`
- Challenge：`keep`
- 裁决理由：提供的三条证据均未直接显示'PT3SBT'字样出现在F0018预期用途描述中。evidence line 85和line 93仅显示通用红外额温计预期用途文本，未见PT3SBT型号字样；evidence line 1仅为文件头注释。claim中提及'F0018 line 93及line 73均写明PT3SBT can transmit...'，但证据截文并不包含该具体句子，无法从现有证据直接核实型号错误。需人工调取F0018完整文本（尤其line 73附近）确认PT3SBT是否确实出现在预期用途描述中，方可定性。
- 证据：
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->

### 2. DHF中存在两套结构完全相同的风险管理文件（F0017-F0020无PT9L前缀，F0021-F0023有PT9L前缀），受控版本不明确。

- Finding ID：`LLM-0002`
- Agent：Market & Category Scout Agent
- 类型：`duplicate_risk_document_sets`
- Challenge：`keep`
- 裁决理由：证据显示DHF中同时存在带'PT9L--'前缀和不带前缀的同名风险管理文件（如Attachment 7 01 Risk Management Plan），两套文件结构相同、文件编号相同（IFT-FXJH01 V1.0），无任何版本控制标记区分受控版本。双套并存且均在主范围目录下，审查员无法判断哪套为最终受控版本，构成法规文件管理缺陷，P1严重度合理。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:70` The risk management process will be conducted in accordance with standard ISO 14971:2019, EN ISO 14971:2019 and EN ISO 14971:2019/A11:2021. The risk management plan for the whole life-cycle of the medical device as shown

### 3. 正式实验报告（F0458，ISO 80601-2-56测试）引用的风险管理报告文件编号为PT9C-FXGB01 V1.0，与PT9L项目编号不符。

- Finding ID：`LLM-0003`
- Agent：Market & Category Scout Agent
- 类型：`test_report_references_wrong_product_model`
- Challenge：`keep`
- 裁决理由：证据直接且明确：PT9L正式测试报告（ETX202303-07-078-03）中第4.2、4.3、4.4条连续引用'Risk Management Report (file No.: PT9C-FXGB01 V1.0)'，文件编号前缀为PT9C而非PT9L。测试报告封面已标注PT9L产品，但内部风险管理文件引用指向PT9C，构成文件断链。该问题将直接影响监管机构对PT9L风险管理闭环的审查，P1严重度合理。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:578` \| 4.3 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Hazard analysis recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:579` \| 4.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk estimation recorded \| P \|

### 4. 设计输出清单二（F0235/F0236）封面产品型号明确标注为PT3SBT，且包含大量PT3SBT编号条目，该文件归入PT9L DHF的依据不明。

- Finding ID：`LLM-0004`
- Agent：Market & Category Scout Agent
- 类型：`wrong_category_document_in_dhf`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：设计输出清单二（F0235/F0236）封面明确标注'产品型号:PT3SBT'，内部条目编号（PT3SBT-PBOM01、PT3SBT-P01等）均属PT3SBT项目，与PT9L无关联说明。该文件被归入PT9L DHF的12设计输出文件夹，无任何交叉引用或适用性说明，将导致DMR范围混淆，P1严重度合理。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 5. 设计输入中EN ISO 80601-2-56:2017+A1:2018被标记为"否"（不适用），但说明书和国际标准均已标记适用，缺乏不适用理由，存在欧盟法规闭环断裂风险

- Finding ID：`LLM-0014`
- Agent：Regulatory Agent
- 类型：`en_iso_80601_2_56_marked_not_applicable_without_justification`
- Challenge：`keep`
- 裁决理由：证据本身真实：设计输入表中EN ISO 80601-2-56:2017+A1:2018确实标记
- 证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:133` \| 行业标准 \| ISO 80601-2-56:2017/Amd1:2018 \|  \| 国际 \| ■是 □否 \|  \|
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:134` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| ISO 80601-2-56:2017/Amd1:2018 \| 欧盟 \| □是 ■否 \|  \|
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:510` ISO 80601-2-56:2017+A1:2018/ EN ISO 80601-2-56:2017/A1:2020 (Medical Electrical Equipment -- Part 2-56: Particular Requirements For The Basic Safety And Essential Performance Of clinical thermometers for body temperature

### 6. 生物相容性报告全部以PT5为受试样品，DHF中未见PT9L与PT5材料等同性评估文件，生物相容性法规闭环存在断裂风险

- Finding ID：`LLM-0015`
- Agent：Regulatory Agent
- 类型：`biocompatibility_reports_based_on_different_product_pt5`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：所有生物相容性报告文件名及内容均明确标注PT5为受试样品，DHF中未见任何PT9L与PT5的材料等同性桥接评估文件。设计验证报告虽引用生物相容性测试合格，但未指明具体报告编号，无法建立PT9L与PT5报告之间的合规链接。ISO 10993系列标准及GB/T 16886系列均要求生物相容性评价须针对最终产品或提供充分的等同性论证，缺失桥接文件构成实质性法规闭环断裂，非误报，严重度P1合理。
- 证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:25` 参照 GB/T 16886.10-2017
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:144` GB/T 16886.10-2017 医疗器械生物学评价 第 10 部分：刺激与皮肤致敏试验
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-细胞毒性-SDWH-M201905262-1.pdf.md:19` 参照 GB/T 16886.5-2017 MTT

### 7. 说明书声明产品符合ISO 80601-2-56但豁免5.2.2条款，该豁免未在证据目录的风险管理或验证文件中找到对应的风险评估或偏差说明

- Finding ID：`LLM-0019`
- Agent：Regulatory Agent
- 类型：`iso_80601_2_56_clause_5_2_2_exception_not_traced_to_risk_file`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：说明书明确声明'except of clause 5.2.2'，即主动豁免ISO 80601-2-56第5.2.2条（该条款涉及体温计测量不确定度的核心性能要求）。风险评估报告证据仅显示总体残余风险可接受的结论性表述，未见针对5.2.2条款豁免的专项风险评估或偏差理由记录。对于性能标准的主动豁免，ISO 14971和FDA/EU MDR均要求有可追溯的风险评估支撑，缺失属于实质性合规缺陷。严重度P2合理，建议可考虑升为P1（涉及核心性能声明）。
- 证据：
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:134` (14) This infrared thermometer meets requirements established in ISO 80601-2-56:2017+A1:2018 and ASTM Standard(E1965-98) except of clause 5.2.2. It displays subject’s temperature over a range of 89.6℉~109.2℉(32℃-42.9℃). 
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:205` In summary, all individual risks are acceptable after implementation of risk control measures. According to ISO 14971:2019 setion 7.4 "Benefit-risk analysis If a residual risk is not judged acceptable using the criteria 
  - `03 风险分析\PT9L--Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:205` In summary, all individual risks are acceptable after implementation of risk control measures. According to ISO 14971:2019 setion 7.4 "Benefit-risk analysis If a residual risk is not judged acceptable using the criteria 

### 8. 机芯BOM（F0096/F0097）中同时列有PT9L专用PCB（PT9L-HFMP01 V1.0）和旧型号PT9C的PCB（PT9C-CNTP01 V1.0），旧型号物料未被明确标注为废弃或参考件，存在错误装配风险。

- Finding ID：`LLM-0021`
- Agent：Hardware Agent
- 类型：`bom_legacy_pcb_contamination`
- Challenge：`keep`
- 裁决理由：Challenge Agent 判定该条证据能够直接支持结论，建议进入第一轮人工确认和整改台账。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:43` \| 24 \| PCB \| K011800008686570696 \| FR4 \| PT9L-HFMP01 V1.0 \|  \| 1拼10 \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:43` \| 21 \| PCB \| K011800008686570696 \| FR4 \| PT9L-HFMP01 V1.0 \|  \| 1拼10 \| 1 \| PCB \| √ \| C \|  \|  \|

### 9. 低电压第一阶段阈值在软件构建文件（F0081）与软件系统测试记录（F0102）之间存在不一致：F0081定义为2.5V–2.7V触发低电提示，而F0102测试用例使用2.65V作为第一阶段测试点，两者边界值描述不完全对应。

- Finding ID：`LLM-0023`
- Agent：Hardware Agent
- 类型：`low_voltage_threshold_inconsistency`
- Challenge：`revise`
- 裁决理由：原claim表述存在误判：2.65V落在软件构建文件定义的第一阶段区间2.5V–2.7V之内，测试点本身并不越界，不构成
- 证据：
  - `11 T1样机\4 构建和编码E0 23.11.via_lo_html.clean.md:67` \| 5 \| 低电压检测功能 \| 低电提示分两阶段，当电量低于第一阶段时，能够保证设备至少能测量20次，当电量低于第二阶段时，设备关机 \| 1. 如果电源电压 2.5V – 2.7V时，LCD能提示低电压并保存低电状态，直至下次重新上电后再检测；<br>2. 如果电源电压小于2.5V时，LCD提示超低电压后关机，一直保存此状态，直至下次重新上电后再检测； \| Uint16_t GetBatValue () \| S.O.C.I 
  - `11 T1样机\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:99` \| 2 \| 将电压调到2.65V，开机 \| LCD提示低电压，实心电池图标常亮 \| I，O \|
  - `11 T1样机\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:100` \|  \| 不断电，将电压调到2.8V \| 按测量键，LCD显示,空心电池图标常亮 \| I，O \|

### 10. PT9L软件设计方案文件夹下存放了BP3L旧型号软件图样，该文件未被排除于主范围，构成旧型号软件资料混入PT9L DHF的法规闭环风险。

- Finding ID：`LLM-0031`
- Agent：Software Agent
- 类型：`legacy_model_residual_in_primary_scope`
- Challenge：`keep`
- 裁决理由：证据直接显示文件路径含'BP3L 软件图样'且文件标题明确为BP3L旧型号，excluded_from_primary_scope=false，说明该文件被纳入PT9L主范围。旧型号软件图样混入PT9L DHF构成法规闭环风险，结论成立，严重度P1合理。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:24` **历史版本记录**
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:26` \| **序号** \| **更改日期** \| **版本描述** \| **版本** \| **更改人** \| **批准人** \|

### 11. T1样机文件夹中存放PT3SBT/PT2L旧型号标签审核表，文件内容涉及PT2L产品型号、项目编号及标签文件编号，属于旧型号资料混入PT9L T1样机阶段主范围文件。

- Finding ID：`LLM-0033`
- Agent：Software Agent
- 类型：`legacy_model_label_file_in_t1_folder`
- Challenge：`keep`
- 裁决理由：证据明确显示文件内容记录产品型号PT2L、项目编号2020-DEV01及PT2L系列标签编号，文件路径位于PT9L T1样机文件夹下，excluded_from_primary_scope=false。旧型号标签审核表混入PT9L T1阶段主范围，可能导致标签验证范围混淆，结论成立，严重度P1合理。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:16` \| ▉说明书 □彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-SMSP09 \|  \|  \|  \|  \|

### 12. 软件质量策划、软件图样、软件设计方案、软件需求规格书四份评审检查表中所有条目结论栏均为空白，无法确认评审是否已完成并通过。

- Finding ID：`LLM-0034`
- Agent：Software Agent
- 类型：`review_checklist_conclusions_blank`
- Challenge：`keep`
- 裁决理由：证据直接显示四份评审检查表中所有条目结论栏均为未勾选的空白状态（□通过 □不通过 □不适用），涵盖质量策划、图样、方案、需求规格四个关键评审节点。评审记录存在但检查表空白，无法从文件中核实评审结论，违反设计评审闭环要求，结论成立，严重度P1合理。
- 证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:16` \| 1 \| 软件生命周期及软件确认计划 \| 是否策划了软件生命周期 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:17` \| 2 \| 软件生命周期及软件确认计划 \| 软件生命周期的划分是否适宜 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:18` \| 3 \| 软件生命周期及软件确认计划 \| 是否按软件生命周期拟制了软件确认计划 \|  \| □通过 □不通过 □不适用 \|  \|

### 13. DHF中存在两套平行风险管理文件（IFT-前缀F0017-F0020与PT9L-前缀F0021-F0024），均未标注作废或替代关系，无法确定法规提交的受控版本。

- Finding ID：`LLM-0039`
- Agent：Risk Traceability Agent
- 类型：`duplicate_risk_document_set_without_clear_supersession`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：IFT-FXJH01 V1.0与PT9L-FXJH01 V1.0两份风险管理计划文件路径不同、文档号前缀不同，均处于非排除状态，且证据中未见任何作废标记或替代声明。ISO 14971要求风险管理文档唯一受控，双套并存且无明确受控版本标识，将导致法规提交时无法确认有效版本，构成实质性合规风险。P1严重度定级合理。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： IFT -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： PT9L -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:6` D N ： IFT-FXPJ01 V2.0 Risk Assessment Report

### 14. F0020风险管理报告文件名标注为IFT-FXGB01 V2.0，但文档内部DN字段显示为PT9L-FXGB01 V1.0，文件名与内部文档号版本双重不一致。

- Finding ID：`LLM-0040`
- Agent：Risk Traceability Agent
- 类型：`risk_management_report_document_number_mismatch`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名标注IFT-FXGB01 V2.0，而文档内部DN字段明确显示PT9L-FXGB01 V1.0，品类前缀（IFT vs PT9L）与版本号（V2.0 vs V1.0）两个维度均存在不一致，属于客观可验证的文档标识错误，非误报。该不一致将导致引用链断裂，影响风险管理报告的可追溯性，在ISO 14971合规审查中属于高风险缺陷。P1严重度定级合理。
- 证据：
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:2` # Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:6` DN ： PT9L -FXGB01 V 1 .0 Risk Management Report

### 15. F0022风险评价报告文件名标注为IFT-FXPJ01 V2.0，但内部DN字段显示为PT9L-FXPJ01 V1.0，品类前缀与版本号均不一致。

- Finding ID：`LLM-0041`
- Agent：Risk Traceability Agent
- 类型：`risk_assessment_report_document_number_version_mismatch`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名标注IFT-FXPJ01 V2.0，内部DN字段为PT9L-FXPJ01 V1.0，品类前缀（IFT vs PT9L）和版本号（V2.0 vs V1.0）两个维度均不一致。可追溯性报告（F0252）引用PT9L-FXPJ01 V1.0，若受控版本实际为V2.0则追溯链路引用过期版本，风险真实存在。非误报，证据充分。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:6` D N ： PT9L-FXPJ01 V1.0 Risk Assessment Report
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:18` \| 软件需求分析阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \|  \| 相关文档之间的信息描述都是准确的 \|  \| 相关文档之间的信息都是正确的，没有歧义信息 \|  \| 相关文档已包含软件必需信息，陈述所有功能 \|  \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### 16. 结构类DFMEA（F0074）严重度评分准则中明确写入"影响血压计的安全运行"，品类标注错误，该DFMEA不适用于红外体温计PT9L。

- Finding ID：`LLM-0042`
- Agent：Risk Traceability Agent
- 类型：`dfmea_product_category_contamination_blood_pressure_monitor`
- Challenge：`revise`
- 裁决理由：核心问题成立：证据明确显示PT9L项目结构类DFMEA严重度评分准则（Severity=10/9）中写入'影响血压计的安全运行'，品类描述与PT9L（红外体温计）不符。但表述中'将影响风险控制措施的有效性判断'属于推断性结论，实际影响程度取决于体温计与血压计在该严重度等级定义上的差异大小。建议修订表述为：严重度评分准则品类描述错误，需确认该准则是否适用于体温计，并补充适用性说明或更正准则描述，避免审核时引发合规质疑。严重度维持P1。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:542` \|  \| 无警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时无预警。会危及使用者。 \| 10 \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:543` \|  \| 有警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时有预警。会危及使用者。 \| 9 \|

### 17. 生物相容性测试报告引用PT5产品而非PT9L，产品适用性未经评估确认

- Finding ID：`LLM-0052`
- Agent：V&V Agent
- 类型：`biocompatibility_report_wrong_product_reference`
- Challenge：`keep`
- 裁决理由：三份报告的文件路径均含'同PT5生物相容性报告'子目录，报告主体为PT5产品，这是路径级别的直接证据。证据目录中未见PT9L专属生物相容性评估或等同性分析文件的陈述来自系统性扫描结论。ISO 10993及国内法规要求产品级生物相容性评估或有据可查的等同性桥接，缺失构成实质性法规闭环风险。P1严重度合理，维持。
- 证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激2-SDWH-M201905262-5.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤致敏1-SDWH-M201905262-2.pdf.md:183` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。

### 18. PT9L DHF设计输出清单二中归档了图号为PT3-P10、Model NO.为PT3的双联弹簧图纸，该图纸属于PT3项目原件，未经正式跨项目借用声明即混入PT9L受控文件体系。

- Finding ID：`LLM-0057`
- Agent：DMR/SOP Agent
- 类型：`legacy_model_drawing_in_dhf`
- Challenge：`keep`
- 裁决理由：三条证据形成完整证据链：文件路径明确位于PT9L DHF设计输出清单二目录下，文件头部标注Drawing NO.为PT3-P10、Model NO.为PT3，且元数据注释明确写明'PT3项目原件，被PT9L DHF借用归档'。跨项目借用无正式声明、EBOM引用关系不明的可追溯性风险直接成立。P1定级合理，不属于误报。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:1` # PT3 双联弹簧 REV01 (V1.0) 2D 图读图报告
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT3_双联弹簧_REV01.pdf`
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:6` > **共用件**：**PT3 项目原件**，被 PT9L DHF 借用归档（外购件 / 设计参照）

### 19. 同为PT9L包装BOM（美版）的两份文件，F0161文件编号为PT9L-PBOM01 V1.0，F0162文件编号为PT9L-PB0M1 V1.0（字母O与数字0混用），且两份文件内容存在列结构差异，无法确认哪份为受控版本。

- Finding ID：`LLM-0058`
- Agent：DMR/SOP Agent
- 类型：`packaging_bom_document_number_inconsistency`
- Challenge：`keep`
- 裁决理由：证据直接显示两份文件编号存在字符差异：一份为'PT9L-P BOM01 V1.0'（含空格），另一份为'PT9L-PB0M1 V1.0'（字母O与数字0混用、字符顺序不同），两份文件均存在于同一DHF路径下。BOM受控版本混乱风险成立，制造现场无法唯一确定执行版本，P1定级合理。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:8` andon文件编号：PT9L-P BOM01 V1 . 0 PT9L包装BOM(美版)【组件清单】
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:8` \| ![PT9L包装BOM_image_001.png](PT9L包装BOM.via_xlsx_assets/PT9L包装BOM_image_001.png) \|  \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:10` \|  \|  \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 20. PT9L外观图（F0177）与外箱图纸（F0164）的Drawing NO.均为PT9L-F01，同一图号对应两个不同物理件，存在图号管理混乱风险。

- Finding ID：`LLM-0059`
- Agent：DMR/SOP Agent
- 类型：`drawing_number_duplication`
- Challenge：`keep`
- 裁决理由：证据直接支撑：外观图文件中明确标注Drawing NO.为PT9L-F01并附有'与外箱PT9L-F01同号但不同件'的警告注释，外箱图纸文件中同样标注Drawing NO.为PT9L-F01。两份不同物理件共用同一图号的事实由双侧文件证据直接确认，图号唯一性原则违反成立，P1定级合理。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:14` \| **Drawing NO.** \| **PT9L-F01**（⚠️ 与外箱 PT9L-F01 同号但不同件） \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:20` \| **Drawing NO.** \| PT9L-F01 \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:23` \| **Model NO.** \| PT9L \|

## 3. 人工复核建议

- 第一轮先确认这些问题是否属于正式受控文件范围，而不是历史/废案/参考资料。
- 对 keep 项建议直接进入责任人确认；对 revise 项建议先改严重度或措辞，再进入整改台账。
- `needs_more_context` 的语义 finding 仍保留在全量报告中，建议作为第二轮复核对象。