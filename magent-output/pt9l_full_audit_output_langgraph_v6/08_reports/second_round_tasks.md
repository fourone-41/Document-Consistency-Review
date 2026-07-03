# 第二轮补充检索任务

> 生成时间：2026-06-30T15:36:40
> 原始 needs_more_context 数量：21
> Context Recovery 后状态：21 条语义项均为 human_review，需人工复核；另有 31 条机械/数值项进入 human_review。

## 1. 任务清单

### LLM-0001：主范围风险控制验证报告（F0019）正文中出现旧型号PT3SBT，而非PT9L，导致预期用途描述与本项目不符。

- Agent：Market & Category Scout Agent
- 严重度：`P1`
- 类型：`legacy_model_in_primary_scope`
- 补查建议：补充检索 IFT-FXYS01 全文，确认 PT3SBT 是否出现，以及出现在哪个上下文；同时检索 IFT-FXGB01、PT9L-FXYS01、PT9L-FXGB01。
- 当前证据：
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers

### LLM-0006：主范围DFMEA文件（F0074）多处内容明确描述血压计功能（电池给血压计供电、包装血压计等），与PT9L红外体温计品类不符。

- Agent：Market & Category Scout Agent
- 严重度：`P1`
- 类型：`legacy_category_in_primary_scope`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17` \|  \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \|  \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \|  \|  \| □ \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:18` \|  \| 彩包装 \| 包装血压计 \| 腕枕无法装入彩包装或腕枕装入彩包装后晃动量太大 \| 生产人员无法包装 \| 4 \| C \| 彩包装的尺寸设计不合理 \| 2 \|  \| 实际装配 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:19` \|  \| 彩包装 \| 包装血压计 \| 彩包装支撑强度不够 \| 彩包装褶皱或破损 \| 4 \| C \| 彩包装的材质强度不够 \| 3 \|  \| 跌落试验、运输试验 \| 2 \| 24 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### LLM-0007：主范围软件设计方案文件夹中存在BP3L软件图样（F0052），与PT9L项目型号不符。

- Agent：Market & Category Scout Agent
- 严重度：`P2`
- 类型：`legacy_model_in_primary_scope`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50` ![图片 13](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d468a82f.png)
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54` ![图片 23](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_cd06a829.png)

### LLM-0008：主范围设计输出清单二（F0235、F0236）中大量条目引用PT3SBT文件编号，与PT9L项目不符。

- Agent：Market & Category Scout Agent
- 严重度：`P1`
- 类型：`legacy_model_in_primary_scope`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### LLM-0009：主范围标签审核表（F0082）文件名为PT3SBT，内容引用PT2L型号及文件编号，与PT9L项目不符。

- Agent：Market & Category Scout Agent
- 严重度：`P2`
- 类型：`legacy_model_in_primary_scope`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计

### LLM-0010：主范围设计输入汇总表（F0031）与历史草稿（F0319）在EN ISO 80601-2-56和MDR 2017/745适用性勾选上存在矛盾，正式版本选项需复核。

- Agent：Market & Category Scout Agent
- 严重度：`P2`
- 类型：`regulatory_standard_applicability_discrepancy`
- 补查建议：检索两套风险文件的修订历史、封面、文件编号、签署页和文件控制记录，确认哪套是正式受控版本。
- 当前证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:134` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| ISO 80601-2-56:2017/Amd1:2018 \| 欧盟 \| □是 ■否 \|  \|
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:143` \| 欧盟指令 \| MDR 2017/745 \|  \| 欧盟 \| □是 ■否 \|  \|
  - `历史记录\PT9LDHF-草稿\04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:127` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \|  \| 欧盟 \| ■是 □否 \|  \|

### LLM-0012：结构类FMEA中将产品描述为'血压计'，与PT9L红外体温计品类不符，构成法规/验证闭环风险。

- Agent：Regulatory Agent
- 严重度：`P1`
- 类型：`dfmea_wrong_product_category_reference`
- 补查建议：检索 PT9C-CNTP01 在所有文件中的出现位置，判断是共用件、子模块、旧型号混入，还是 PT9L 正式使用受控料号。
- 当前证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:22` \|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌印刷内容容易被擦拭掉 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌未覆膜 \| 2 \|  \| 依IEC60601-1:2005 电气安全通用要求中7.1.3 标记耐久性要求 对铭牌进行试验 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \

### LLM-0019：说明书声明符合ISO 80601-2-56但'except of clause 5.2.2'，该豁免条款未在设计输入或风险文件中找到正式说明。

- Agent：Regulatory Agent
- 严重度：`P2`
- 类型：`iso_80601_2_56_exception_clause_5_2_2_not_justified`
- 补查建议：检索软件质量策划评审、软件方案评审、软件需求评审相关文件，确认是否存在另一版本已填写，或 Markdown 转换遗漏勾选信息。
- 当前证据：
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:134` (14) This infrared thermometer meets requirements established in ISO 80601-2-56:2017+A1:2018 and ASTM Standard(E1965-98) except of clause 5.2.2. It displays subject’s temperature o
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:133` \| 行业标准 \| ISO 80601-2-56:2017/Amd1:2018 \|  \| 国际 \| ■是 □否 \|  \|

### LLM-0020：设计输入和设计验证报告均未勾选CE认证，但说明书和风险文件多处引用EN标准，市场范围与标准引用存在不一致。

- Agent：Regulatory Agent
- 严重度：`P2`
- 类型：`ce_market_not_selected_but_eu_standards_referenced`
- 补查建议：检索构建和编码、软件需求、软件设计、子程序测试记录、软件系统测试记录、软件确认报告，确认追溯表是否在其他文件中。
- 当前证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:22` \| 2 \| 销售地区及认证 Intended markets and certification \| 要求符合如下认证体系要求： □ CE 对应地区： 欧洲 ■ FDA 对应地区：美国 □ CFDA 对应地区：中国 □ 其他 \|  \|
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:34` \| 2 \| 销售地区及认证 Intended markets and certification \| 要求符合如下认证体系要求： □ CE 对应地区： 欧洲 ■ FDA 对应地区：美国 □ CFDA 对应地区：中国 □ 其他 \| □手板□T1■设计确认 \| -- \| -- \| -- \| -- \|
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:506` IEC 60601-1:2005+A1:2012+A2:2020/ EN 60601-1:2006/A2:2021 (Medical electrical equipment - Part 1: General requirements for basic safety and essential performance).

### LLM-0022：电池使用寿命测试报告中电池容量标注为1000mAh，与包装BOM中1200mAh不一致，测试代表性存疑。

- Agent：Hardware Agent
- 严重度：`P1`
- 类型：`battery_parameter_inconsistency`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.pdf.md:29` 测试使用电池：两节七号干电池（3V/1000mAh）；
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.via_lo_html.clean.md:18` 测试使用电池：两节七号干电池（3V/1000mAh）；
  - `11 T1样机\PT9L包装BOM.via_xlsx.clean.md:23` \| 10 \| 电池 \| K020400000757680820 \|  \| 7号碱性 1.5V/1200mAh \| LR03 \|  \| 2 \|  \| √ \| C \|  \|

### LLM-0025：T1样机评审检查表中含"电池不能和袖带相邻存放"检查项，袖带为血压计专用部件，与IFT品类不符。

- Agent：Hardware Agent
- 严重度：`P2`
- 类型：`sample_review_checklist_cross_contamination`
- 补查建议：检索风险管理报告全文，关键词包括 EMC、immunity、electromagnetic、60601-1-2、pass/fail、essential performance。
- 当前证据：
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:38` \| 24 \| 装 配 检 查 \| 电池不能和袖带相邻存放 \|  \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\T1样机评审检查表E0 23.11.via_xlsx.clean.md:38` \| 24 \| 装 配 检 查 \| 电池不能和袖带相邻存放 \|  \| □通过 □不通过 □不适用 \|

### LLM-0030：软件质量策划评审检查表、软件需求规格书评审检查表、软件设计方案评审检查表的评审结论栏全部为空白复选框，评审是否通过无法确认

- Agent：Software Agent
- 严重度：`P2`
- 类型：`review_checklist_result_blank`
- 补查建议：检索设计评审计划、设计评审检查表、设计验证计划、设计验证报告封皮和会议记录，确认验证状态是否在其他记录中体现。
- 当前证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:16` \| 1 \| 软件生命周期及软件确认计划 \| 是否策划了软件生命周期 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:17` \| 2 \| 软件生命周期及软件确认计划 \| 软件生命周期的划分是否适宜 \|  \| □通过 □不通过 □不适用 \|  \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:18` \| 3 \| 软件生命周期及软件确认计划 \| 是否按软件生命周期拟制了软件确认计划 \|  \| □通过 □不通过 □不适用 \|  \|

### LLM-0040：DHF中存在两套平行风险文件：IFT前缀（F0017-F0020）与PT9L前缀（F0021-F0024），均为同名文件，未明确哪套为正式受控版本。

- Agent：Risk Traceability Agent
- 严重度：`P1`
- 类型：`duplicate_parallel_risk_file_set`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： IFT -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable

### LLM-0046：用户现场测试计划（F0260）文件名含PT9C，但内容包含风险评估条款，未见PT9L对应版本的用户测试计划证据。

- Agent：Risk Traceability Agent
- 严重度：`P2`
- 类型：`user_test_plan_wrong_model_residual`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:87` 4\. 测试人员在评审用户现场测试记录表中的用户使用过程记录时，检查用户操作是否正确。若操作过程中发现异常情况或新的风险，应进行记录；
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:151` **风险评估：**
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:153` 是否发现新的风险 ｜ □未发现 □有新风险，解决方案：

### LLM-0047：EMC型式试验报告（F0456）明确要求免疫通过/失败准则应纳入风险管理文件，但现有证据目录中未见风险管理文件包含EMC免疫准则的对应条款。

- Agent：Risk Traceability Agent
- 严重度：`P2`
- 类型：`emc_immunity_criteria_risk_file_linkage_unverified`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `实验报告\最终报告\2024-08-15 TX202303-07-078-01 PT9L EMC  型式试验报告英文.pdf.md:622` \| Note 1: Specific, detailed immunity pass/fail criteria, shall be based on applicable part two standards or risk management, for immunity with regard to em disturbances. These pa
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable

### LLM-0050：T1阶段设计验证报告封皮中三个子报告勾选框均为"□"（未勾选），无法确认T1验证已正式完成并通过。

- Agent：V&V Agent
- 严重度：`P2`
- 类型：`verification_report_cover_not_signed_off`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:22` □设计验证报告－通用要求部分 文件编号： PT9L-T1TY01 V1.0;
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:24` □设计验证报告－功能规格部分 文件编号： PT9L-T1GN01 V1.0;
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:26` □设计验证报告－性能规格部分 文件编号： PT9L-T1XN01 V1.0;

### LLM-0053：生物相容性报告（皮肤刺激、皮肤致敏、细胞毒性）均以PT5为受试样品，未见PT9L专属生物相容性评价证据。

- Agent：V&V Agent
- 严重度：`P1`
- 类型：`biocompatibility_report_wrong_model`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激2-SDWH-M201905262-5.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤致敏1-SDWH-M201905262-2.pdf.md:183` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。

### LLM-0055：设计验证计划封皮（F0118）中子计划勾选框状态无法从证据中确认，存在验证计划正式批准状态不明的风险。

- Agent：V&V Agent
- 严重度：`P2`
- 类型：`verification_plan_cover_subplan_not_checked`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\设计验证计划E0\设计验证计划(封面)E0 23.11.md:13` <div style="overflow-x:auto; border:1px solid #e5e7eb; border-radius:6px; padding:0; background:#fff; margin:6px 0;"><table style="border-collapse:collapse; width:max-content; font
  - `11 T1样机\设计验证计划E0\设计验证计划(封面)E0 23.11.md:15` \|     \| 文件编号： \| PT9L-YZJH01 \| V1.0 \| 设计验证计划 \| 表号: QR-7.3-06/E0 \|     \|
  - `11 T1样机\设计验证计划E0\xingneng.via_xlsx.clean.md:14` 1.本设计验证计划需批准后方能使用执行，

### LLM-0059：产品检验标准中允许对不合格温度计复测两次且两次合格即判合格，该规则是否已在验证计划判定准则中明确引用存疑。

- Agent：V&V Agent
- 严重度：`P3`
- 类型：`acceptance_criteria_retest_rule_consistency`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `11 T1样机\PT9L红外体温计产品检验标准 V1.0.doc.md:250` 4. 对测试结果不符合规定的温度计，可复测两次，两次复测合格，亦可作合格处理。</td>
  - `11 T1样机\PT9L红外体温计产品检验标准 V1.0.doc.md:267` 4. 对测试结果不符合规定的温度计，可复测两次，两次复测合格，亦可作合格处理。</td>
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:23` \| 1 \| 温度显示范围 \| 32.0℃～42.9℃ \| □手板■T1□设计确认 \| 参见《PT9L红外体温计产品检验标准V1.0 》第6项 \| 全部测试结果均需符合《PT9L红外体温计产品检验标准V1.0》中第6项的要求 \| 参见《PT9L红外体温计检测报告 V1.0》中第6项测试结果 \| 合格 \|

### LLM-0062：外观图（F0177）与外箱图纸（F0164）的Drawing NO.均为PT9L-F01，但两者为不同物件，图号冲突将导致图纸管理混乱和制造转移错误风险。

- Agent：DMR/SOP Agent
- 严重度：`P1`
- 类型：`drawing_number_collision`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:14` \| **Drawing NO.** \| **PT9L-F01**（⚠️ 与外箱 PT9L-F01 同号但不同件） \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:20` \| **Drawing NO.** \| PT9L-F01 \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:23` \| **Model NO.** \| PT9L \|

### LLM-0063：散热器金属套图纸（75CEE0-Model.pdf）为外购供应商图号（GXT-001/天津小泉），尚未完成内部标准图号映射，制造转移资料中图号体系不统一。

- Agent：DMR/SOP Agent
- 严重度：`P2`
- 类型：`supplier_drawing_internal_number_not_mapped`
- 补查建议：补充检索该 finding 的上下游文件、同名文件、历史版本和正式受控版本。
- 当前证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:8` > **关键背景**：本图非 T-Z1/PT9L 自制结构件，是 **外购供应商图纸**（天津小泉精密金属制品有限公司 2018-09-17），用于 PT9L 红外探头组件中的"散热器金属套"，与 `FDIR-V14_散热器压块_REV01_0714.pdf` 配合使用（见技术要求第 4 条）。
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:101` ## 4. 装配 / 约束推断（B 级）
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:107` - **总长 11.79⁻⁰·⁰⁵⁻⁰**：**只能小不能大**——避免影响装配链。
