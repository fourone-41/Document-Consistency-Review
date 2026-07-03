# PT9L 高优先级语义审查问题清单

> 生成时间：2026-07-01T14:27:18
> 范围：仅保留 P1 且 Challenge Agent 裁决为 keep/revise 的语义 findings，适合作为人工复核第一批入口。

## 1. 摘要

- 高优先级问题：20
- keep：16
- revise：4

## 2. 问题清单

### 1. 主范围风险评估报告（F0018）正文两处均出现旧型号PT3SBT，而非PT9L，与同文件夹PT9L版本（F0022）并存，受控版本不明确。

- Finding ID：`LLM-0002`
- Agent：Market & Category Scout Agent
- 类型：`old_model_residual_in_primary_scope`
- Challenge：`revise`
- 裁决理由：claim声称F0018 line 93出现PT3SBT，但实际evidence text同样为通用预期用途描述，未直接显示PT3SBT字样，直接证据不足。然而，文件名'Attachment 7 02 Risk Assessment Report IFT-FXPJ01'（无PT9L前缀）与'PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01'（有PT9L前缀）两份文件同时存在于主范围且excluded_from_primary_scope均为false，双版本并存、受控版本不明确的核心问题具有合理依据。建议修改claim，聚焦于'同一文件存在有/无PT9L前缀两个版本并存于DHF主范围，受控版本不明确'，而非依赖未经证实的正文PT3SBT字样。严重度维持P1。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->

### 2. 软件设计方案文件夹中存在BP3L软件图样（F0052），BP3L为血压计型号，与PT9L红外体温计品类不符，出现在主范围内。

- Finding ID：`LLM-0004`
- Agent：Market & Category Scout Agent
- 类型：`old_category_residual_in_primary_scope`
- Challenge：`keep`
- 裁决理由：证据直接且充分：文件标题行明确为'# BP3L 软件图样E0 23.11'，图片引用路径亦含'BP3L'前缀，文件位于'07 软件设计方案E0 23.11'目录且excluded_from_primary_scope=false。BP3L为血压计型号，与PT9L红外体温计品类不符，属于跨品类文件混入DHF主范围，可能导致软件验证追溯链混乱，问题成立，严重度P1合理。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50` ![图片 13](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d468a82f.png)
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54` ![图片 23](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_cd06a829.png)

### 3. 设计输出清单二（F0235/F0236）中大量出现PT3SBT物料编号及产品型号标注，与PT9L项目不符，且两份文件并存于主范围。

- Finding ID：`LLM-0005`
- Agent：Market & Category Scout Agent
- 类型：`old_category_residual_in_primary_scope`
- Challenge：`keep`
- 裁决理由：证据直接且充分：line 239明确显示'产品型号:PT3SBT'，line 187和line 263显示PT3SBT-PBOM01、PT3SBT-P01等BOM编号，文件位于'12 设计输出（含01、02）\设计输出清单二'且excluded_from_primary_scope=false。PT3SBT型号与PT9L项目不符，且两份同名文件并存，BOM追溯链断裂风险成立，严重度P1合理。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 4. 设计输入汇总表正式版（F0031）与历史草稿版（F0319）在EN ISO 80601-2-56和MDR 2017/745适用性勾选上存在实质性差异，正式版将欧盟标准和MDR标记为"否"。

- Finding ID：`LLM-0010`
- Agent：Market & Category Scout Agent
- 类型：`regulatory_standard_inconsistency`
- Challenge：`revise`
- 裁决理由：证据直接支持正式版（F0031）与草稿版（F0319）在EN ISO 80601-2-56和MDR 2017/745适用性上存在实质性差异。核心问题成立且风险较高。但需调整表述：(1) 正式版将欧盟标准标记为'否'可能是产品市场策略调整（如该型号不申请CE认证），属于合理的设计输入变更，而非必然的'重大遗漏'；(2) 真正的风险在于该变更是否经过正式的设计输入变更评审和批准，以及是否有变更理由记录。若无变更审批记录，则属于设计控制程序缺陷。建议将严重度升级为P1，因为若产品实际销往欧盟市场而设计输入基线排除了MDR和欧盟标准，将构成重大合规风险，表述应聚焦于'设计输入变更缺乏可追溯的变更理由和审批记录'。
- 证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:134` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| ISO 80601-2-56:2017/Amd1:2018 \| 欧盟 \| □是 ■否 \|  \|
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:143` \| 欧盟指令 \| MDR 2017/745 \|  \| 欧盟 \| □是 ■否 \|  \|
  - `历史记录\PT9LDHF-草稿\04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:127` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \|  \| 欧盟 \| ■是 □否 \|  \|

### 5. PT9L DHF中存在以PT3SBT为标题、PT2L为检查记录引用的标签审核表（F0082），旧型号文件出现在主范围文件夹中，法规证据归属不清。

- Finding ID：`LLM-0012`
- Agent：Regulatory Agent
- 类型：`old_model_label_audit_in_pt9l_dhf`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件路径位于'11 T1样机'文件夹下，文件标题明确为'PT3SBT标签审核表'，检查记录列引用'PT2L(美亚)-ZXBQ01~06'，与PT9L无任何直接关联。若该文件被用作PT9L标签合规证据，则证据主体错误，法规归属不清问题实质存在。P1严重度合理，旧型号文件混入主范围文件夹属于DHF文件管理缺陷，可能在监管审查中引发质疑。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:20` \| 标准名称 \| 适用性 \|  \| 标签类型 \|  \|  \|  \|  \| 检查记录 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:22` \| IEC 60601-1 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ01 V1.0 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:23` \| IEC 60601-1-2 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ02 V1.0 \|

### 6. 生物相容性测试报告（F0104~F0108）受试样品均为PT5，而非PT9L，缺乏材料等同性桥接文件，无法直接支撑PT9L生物相容性法规闭环。

- Finding ID：`LLM-0014`
- Agent：Regulatory Agent
- 类型：`biocompatibility_report_wrong_subject_device`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：所有生物相容性报告文件路径均含'PT5'，报告编号为PT5专属系列，文件夹名称亦为'同PT5生物相容性报告'。设计验证报告声明通过但引用的是PT5报告，缺乏PT9L与PT5材料等同性桥接文件（如材料清单对比、等同性声明）。根据GB/T 16886系列及ISO 10993要求，跨型号引用生物相容性报告须有明确的等同性论证，缺失该文件构成实质性法规闭环风险。P1严重度合理。
- 证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:25` 参照 GB/T 16886.10-2017
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:144` GB/T 16886.10-2017 医疗器械生物学评价 第 10 部分：刺激与皮肤致敏试验
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-细胞毒性-SDWH-M201905262-1.pdf.md:19` 参照 GB/T 16886.5-2017 MTT

### 7. 机芯BOM中存在旧型号PT9C的PCB料号，与PT9L项目不符，构成BOM与硬件设计的法规闭环风险。

- Finding ID：`LLM-0021`
- Agent：Hardware Agent
- 类型：`bom_legacy_pcb_contamination`
- Challenge：`keep`
- 裁决理由：两份BOM文件（PT9L-EBOM01和PT9L-T1EB01）均同时包含PT9L专用PCB料号和PT9C专用PCB料号，证据直接支持BOM中存在旧型号残留的结论。若生产阶段误用PT9C-CNTP01，将导致硬件设计与验证报告不一致，构成法规闭环风险。证据充分，严重度P1合理。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:43` \| 21 \| PCB \| K011800008686570696 \| FR4 \| PT9L-HFMP01 V1.0 \|  \| 1拼10 \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 8. 电池使用寿命测试报告中测试用电池规格（3V/1000mAh）与包装BOM中电池规格（1.5V/1200mAh）不一致，测试有效性存疑。

- Finding ID：`LLM-0022`
- Agent：Hardware Agent
- 类型：`battery_spec_inconsistency`
- Challenge：`revise`
- 裁决理由：核心问题成立：测试报告明确记录电池容量为1000mAh，BOM指定电池容量为1200mAh，两者不一致。但表述需修正：两节1.5V串联总电压确为3V，因此电压描述"3V"本身不构成矛盾，真正的不一致点仅在容量（1000mAh vs 1200mAh）及可能的具体型号差异。建议修订claim，明确指出容量差异是核心风险，并说明测试结论（≥1000次）是否仍覆盖出货电池需补充验证。严重度P1维持，因测试有效性直接影响产品性能声称的法规支撑。
- 证据：
  - `11 T1样机\PT9L包装BOM.via_xlsx.clean.md:23` \| 10 \| 电池 \| K020400000757680820 \|  \| 7号碱性 1.5V/1200mAh \| LR03 \|  \| 2 \|  \| √ \| C \|  \|
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.pdf.md:29` 测试使用电池：两节七号干电池（3V/1000mAh）；
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.via_lo_html.clean.md:18` 测试使用电池：两节七号干电池（3V/1000mAh）；

### 9. 设计验证计划（通用要求部分）中电池条目出现"次血压测量"字样，属于血压计品类文字污染，影响IFT验证文件完整性。

- Finding ID：`LLM-0023`
- Agent：Hardware Agent
- 类型：`blood_pressure_text_contamination_in_dvp`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：设计验证计划通用要求部分电池条目原文含"次血压测量"字样，PT9L为红外体温计，该文字属于明确的品类污染。该文件属于法规提交核心文件，文字污染可能引发监管机构对产品品类的混淆，风险真实存在。严重度P1合理。
- 证据：
  - `11 T1样机\设计验证计划E0\设计验证计划-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:47` \| 20 \| 电池 battery \| □可充电电池：在充满电后，电池电量至少能进行 次血压测量，并且电池性能参数不变。 □电池：需要符合WERC认证 ■无要求 \| □手板■T1□设计确认 \| 电池寿命测试报告 \| 符合设计输入要求 \|  \|

### 10. PT9L软件设计方案文件夹下存放了BP3L型号的软件图样，属于旧型号文件残留于主范围文件，构成法规/验证闭环风险

- Finding ID：`LLM-0030`
- Agent：Software Agent
- 类型：`legacy_model_contamination_in_primary_scope`
- Challenge：`keep`
- 裁决理由：证据最强：文件路径位于PT9L的'07 软件设计方案E0 23.11\软件图样E0 23.11'目录下，但文件标题第2行明确为'# BP3L 软件图样E0 23.11'，属于BP3L型号文件。软件图样评审计划和评审记录若以该目录为评审对象，则PT9L软件图样评审闭环实质上针对的是BP3L文件，验证闭环无效。这是法规符合性的直接风险，P1定级合理，非误报。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:24` **历史版本记录**
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:26` \| **序号** \| **更改日期** \| **版本描述** \| **版本** \| **更改人** \| **批准人** \|

### 11. PT9L机芯类组件清单中PCB图号引用旧型号PT9C文件编号，BOM与当前型号设计文件不一致

- Finding ID：`LLM-0031`
- Agent：Software Agent
- 类型：`legacy_model_pcb_reference_in_bom`
- Challenge：`keep`
- 裁决理由：两份独立BOM文件（EBOM01和T1EB01）的PCB行均记录图号'PT9C-CNTP01 V1.0'，PT9C为旧型号，证据一致且可直接核实。两份文件同时出现排除偶发录入错误的可能性，PCB图号错误直接影响硬件配置基线可信度，P1严重度合理。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:63` \| 章节 \|  \| 版本 \| 拟制(专业工程师): 审核(专业主管): 审核(项目负责人): 批准(产品线主管): \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 12. PT9L结构类FMEA文件中产品型号字段出现KD-5915L，同一文件内型号标识前后不一致，FMEA有效性存疑

- Finding ID：`LLM-0033`
- Agent：Software Agent
- 类型：`legacy_model_in_dfmea_product_number`
- Challenge：`keep`
- 裁决理由：同一FMEA文件内第13行、第189行产品型号为'KD-5915L'，第370行又出现'PT9L'，三处证据均来自同一文件，前后矛盾无法用格式差异解释。强烈提示该文件由其他型号FMEA改写且未完整替换，FMEA分析对象同一性存疑，直接影响风险分析有效性，P1严重度合理。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:13` \|  \| 产品型号： \| KD-5915L \|  \|  \| 审核： \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA版本： \| V1.0 \|  \|  \|  \|  \|  \|  \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:189` \|  \| 产品型号： \| KD-5915L \|  \|  \| 编制： \|  \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA版本： \| V1.0 \|  \|  \|  \|  \|  \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:370` \|  \| 产品型号： \| PT9L \|  \|  \| 审核： \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA版本： \| V1.0 \|  \|  \|  \|  \|  \|  \|

### 13. 软件质量策划、软件图样、软件设计方案、软件需求规格书四份评审检查表结论栏全部为空白，无法证明评审已实际执行

- Finding ID：`LLM-0034`
- Agent：Software Agent
- 类型：`review_checklist_all_blank_no_conclusion`
- Challenge：`keep`
- 裁决理由：证据显示多份评审检查表（质量策划、图样、方案、需求规格）结论栏均为未勾选的空白复选框，覆盖四个评审阶段，非偶发。评审记录文件存在不能弥补检查表无结论的缺陷，YY/T 0664要求评审活动有完整闭环记录，P1严重度合理。
- 证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:16` \| 1 \| 软件生命周期及软件确认计划 \| 是否策划了软件生命周期 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:17` \| 2 \| 软件生命周期及软件确认计划 \| 软件生命周期的划分是否适宜 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:18` \| 3 \| 软件生命周期及软件确认计划 \| 是否按软件生命周期拟制了软件确认计划 \|  \| □通过 □不通过 □不适用 \|  \|

### 14. 风险管理报告（F0020）文件名标注版本为V2.0，但正文文件号字段显示为PT9L-FXJH01 V1.0（风险管理计划编号），文件号与文件类型不符，且版本号不一致。

- Finding ID：`LLM-0040`
- Agent：Risk Traceability Agent
- 类型：`document_id_version_mismatch_in_risk_management_report`
- Challenge：`keep`
- 裁决理由：证据直接且明确：文件名标注IFT-FXGB01 V2.0，正文DN字段显示PT9L-FXGB01 V1.0，品类前缀（IFT vs PT9L）和版本号（V2.0 vs V1.0）双重不一致均有原文支撑，非推断。此类文件标识不一致在监管审查中属于直接可观察的文件控制缺陷，可能导致审查机构无法确认文件有效性及风险闭环认定，影响重大。原定P1合理，建议维持。
- 证据：
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:2` # Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:6` DN ： PT9L -FXGB01 V 1 .0 Risk Management Report

### 15. 风险分析文件夹中同时存在IFT前缀（F0017-F0020）和PT9L前缀（F0021-F0024）两套完整的风险管理文件（计划、评价、控制验证、报告），DHF中有效受控版本不明确。

- Finding ID：`LLM-0041`
- Agent：Risk Traceability Agent
- 类型：`dual_document_set_ift_vs_pt9l_risk_files`
- Challenge：`keep`
- 裁决理由：证据明确显示同一DHF风险分析文件夹中存在IFT前缀（F0017-F0020）和PT9L前缀（F0021-F0024）两套平行的完整风险管理文件，文件名路径均可验证。两套文件均含Risk Management Plan，文件号前缀不同但内容高度重叠，审查机构无法判断受控版本，构成法规闭环风险。证据直接支持结论，非误报。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： IFT -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable

### 16. PT9L版风险评价报告（F0022）文件名标注为V2.0，但正文DN字段显示为PT9L-FXPJ01 V1.0，版本号不一致，无法确认该报告是否为最终受控版本。

- Finding ID：`LLM-0042`
- Agent：Risk Traceability Agent
- 类型：`risk_assessment_report_version_mismatch_pt9l_set`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名路径含V2.0（PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0），但正文DN字段明确标注PT9L-FXPJ01 V1.0，两者版本号不一致。可追溯性分析报告引用V1.0，若受控版本实为V2.0则引用失效。版本号内外不一致是客观事实，非误报，严重度P1合理。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:6` D N ： PT9L-FXPJ01 V1.0 Risk Assessment Report
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:18` \| 软件需求分析阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \|  \| 相关文档之间的信息描述都是准确的 \|  \| 相关文档之间的信息都是正确的，没有歧义信息 \|  \| 相关文档已包含软件必需信息，陈述所有功能 \|  \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### 17. PT9L版风险控制措施验证报告（F0023）文件名标注为V2.0，但正文DN字段显示为PT9L-FXYS01 V1.0，版本号不一致，剩余风险评估结论所依据的版本不明确。

- Finding ID：`LLM-0043`
- Agent：Risk Traceability Agent
- 类型：`risk_control_verification_report_version_mismatch_pt9l_set`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：文件名路径含V2.0（PT9L--Attachment 7 03 Verification...IFT-FXYS01 V2.0），但正文DN字段明确标注PT9L-FXYS01 V1.0，版本号内外不一致。可追溯性分析报告引用V1.0，与LLM-0042属于同一模式的系统性版本标注问题，非误报。严重度P1合理，因剩余风险验证闭环直接受影响。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:6` D N: PT9L-FXYS01 V1.0 Verification of risk control measure and residual risk evaluation r eport
  - `03 风险分析\PT9L--Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:52` 1.2 Introduction on implementation of the risk management plan 3
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:32` \| 用户测试阶段 \| 风险管理 \| 风险控制措施验证以及剩余风险评估报告PT9L-FXYS01 V1.0<br>风险管理报告<br>PT9L-FXGB01 V1.0 \|  \| 相关文档之间的信息描述都是准确的 \|  \| 相关文档之间的信息都是正确的，没有歧义信息 \|  \| 相关文档已包含软件必需信息，陈述所有功能 \|  \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### 18. 结构类DFMEA（F0074）严重度评分准则中明确写入"影响血压计的安全运行"，品类描述与PT9L红外体温计不符，DFMEA风险评估基准存在品类错误。

- Finding ID：`LLM-0044`
- Agent：Risk Traceability Agent
- 类型：`dfmea_wrong_product_category_blood_pressure_monitor`
- Challenge：`keep`
- 裁决理由：证据直接支持结论：结构类DFMEA严重度评分准则中第10分和第9分条目均明确写入
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:542` \|  \| 无警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时无预警。会危及使用者。 \| 10 \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:543` \|  \| 有警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时有预警。会危及使用者。 \| 9 \|

### 19. T1阶段验证报告封皮所列子报告文件编号（PT9L-T1TY01/T1GN01/T1XN01）与实际验证报告中使用的编号（PT9L-YZXN01/YZGN01）不一致，且封皮子项均为"□"未勾选。

- Finding ID：`LLM-0051`
- Agent：V&V Agent
- 类型：`t1_verification_report_cover_document_number_mismatch`
- Challenge：`revise`
- 裁决理由：证据显示封皮文件编号（PT9L-T1YB01）与正文引用的验证计划编号（PT9L-YZXN01/YZGN01）体系确实不一致，且复选框全部未勾选，核心问题成立。但原claim中列举的子报告编号（T1TY01/T1GN01/T1XN01）在所提供证据行中未直接出现，证据仅支持'封皮编号与实际报告编号不一致'及'复选框未勾选'两点，表述需收窄至证据可直接支持的范围。严重度P1维持，但建议将claim修订为：T1阶段验证报告封皮文件编号（PT9L-T1YB01）与实际验证报告内部引用的计划编号体系（PT9L-YZXN01/YZGN01）不一致，且封皮所有子项复选框均未勾选，无法确认T1阶段验证报告已正式归档完成。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:2` # 设计验证报告封皮-T阶段 E0  23.11
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:6` 文件编号 : PT9L -T1YB01 V1.0 设计验证报告
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:8` 设计验证报告

### 20. DHF中生物相容性测试报告（皮肤刺激、皮肤致敏、细胞毒性）均以PT5为受试样品，证据目录中未见PT9L专属生物相容性报告或材料等同性评估文件。

- Finding ID：`LLM-0053`
- Agent：V&V Agent
- 类型：`biocompatibility_report_wrong_product_reference`
- Challenge：`keep`
- 裁决理由：证据明确显示DHF中所有生物相容性报告（皮肤刺激、皮肤致敏、细胞毒性）文件路径均含'同PT5生物相容性报告'，报告编号为PT5系列，受试品为PT5而非PT9L。证据目录中未见PT9L专属生物相容性报告或材料等同性评估文件。ISO 10993要求对受试产品本身或经充分等同性论证后方可引用其他产品报告，当前缺少等同性评估文件，法规闭环风险成立。P1严重度合理。
- 证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激2-SDWH-M201905262-5.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤致敏1-SDWH-M201905262-2.pdf.md:183` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。

## 3. 人工复核建议

- 第一轮先确认这些问题是否属于正式受控文件范围，而不是历史/废案/参考资料。
- 对 keep 项建议直接进入责任人确认；对 revise 项建议先改严重度或措辞，再进入整改台账。
- `needs_more_context` 的语义 finding 仍保留在全量报告中，建议作为第二轮复核对象。