# PT9L 机械候选复审驳回/非错误清单

> 生成时间：2026-06-30T15:36:40
> 范围：mechanical_review_node 经一轮或二轮 LLM 复审后判定为 dismiss 的机械候选。dismiss 表示当前证据下不构成可确认错误，不等于人工最终裁决。

## 1. 摘要

- 驳回/非错误候选数：328

## 2. 按 Agent 统计

| Agent | 数量 |
|---|---:|
| Product Identity Agent | 166 |
| Document Control Agent | 84 |
| Regulatory Agent | 78 |

## 3. 样例清单

### 1. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0002`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:2`
- 命中文本：# V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0"，属于前代型号PT2L的历史风险管理计划。primary_scope=false，且文件内容与PT9L无直接关联（第6行虽出现"DN：PT9L-FXJH01 V1.0"字样，但结合上下文判断为文件内部引用或转换痕迹，不改变该文件本质为PT2L历史文件的定性）。该cluster不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 2. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0003`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:117`
- 命中文本：![形状2](V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html_assets/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0_html_f9d9f2af.gif) Acceptable Control as much as possible Not acceptable
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0"，属于前代型号PT2L的历史风险管理计划。primary_scope=false，且文件内容与PT9L无直接关联（第6行虽出现"DN：PT9L-FXJH01 V1.0"字样，但结合上下文判断为文件内部引用或转换痕迹，不改变该文件本质为PT2L历史文件的定性）。该cluster不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 3. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0004`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:6`
- 命中文本：D N : PT2L( 美亚 ) - SGFP 01 V1.0 Risk Assessment Report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 4. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0005`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 5. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0006`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:81`
- 命中文本：When the PT2L infrared thermometer project was launched, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 6. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0007`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:83`
- 命中文本：Currently, the PT2L infrared thermometer is in the feasibility review stage of design changes. The purpose of this risk management review is to determine whether the design changes of the PT2L infrared thermometer will g
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 7. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0008`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:107`
- 命中文本：Please find the document *Risk Management P* *lan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 8. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0009`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:124`
- 命中文本：\| **A.2.1** \| What is the intended use and how is the medical device to be used?<br>□ what is the medical device’s role relative to:<br>□ what are the indications for use (e.g. patient population, user profile, use env
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-2 Risk Assessment Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险评估文件。primary_scope=false，所有候选证据均来自同一历史文件，内容描述的是PT2L设计变更阶段的风险管理活动，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 9. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0010`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:6`
- 命中文本：D N: PT2L( 美亚 ) - SGYS 01 V 1 .0 Verification of risk control measure and residual risk evaluation report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 10. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0011`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 11. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0012`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:95`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 12. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0013`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:198`
- 命中文本：型式试验报告：PT2L(美亚)-XNTB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 13. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0014`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:202`
- 命中文本：说明书：PT2L(美亚)-SMSY02 V2.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 14. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0015`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:204`
- 命中文本：易用性报告：PT2L(美亚)-UETR01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 15. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0016`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:206`
- 命中文本：临床评估报告：PT2L(美亚)-RLPB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 16. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0017`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:208`
- 命中文本：软件确认报告：PT2L(美亚)-RJQB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-3 Verification of risk control measure and residual risk evaluation report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险控制验证文件。primary_scope=false，文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)编号体系，属于历史文件内部的合理交叉引用，不构成PT9L正式DHF/DMR的合规证据缺陷，予以dismiss。

### 17. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0018`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:6`
- 命中文本：DN ： PT2L-FXGB01 V 4 .0 Risk Management Report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 18. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0019`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 19. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0020`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:60`
- 命中文本：PT2L replaced the MCU with a smaller memory in hardware to ensure that the new MCU has sufficient performance and functions while meeting cost requirements. Re-evaluated the structural design in structure to find parts t
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 20. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0021`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:64`
- 命中文本：At the same time as the PT2L infrared thermometer project was established, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 21. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0022`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:66`
- 命中文本：The risk management plan determined the risk acceptance criteria for the PT2L infrared thermometer and arranged the review of the product's risk management activities.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 22. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0023`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:70`
- 命中文本：In the early development and prototype stages of the PT2L infrared thermometer, the risk management team conducted a risk management review and formed relevant risk management documents.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 23. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0024`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:72`
- 命中文本：While the PT2L infrared thermometer was undergoing design changes, the company formed a risk management team to ensure that the risk management activities for the design changes of the project were effectively implemente
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 24. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0025`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:96`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件名为"V1.0-4 Risk Management Report"，产品型号明确标注为PT2L，项目编号2020-002-WX02，属于PT2L前代型号的历史风险管理报告（V4.0版本为PT2L自身迭代版本）。primary_scope=false，文件内容完整描述PT2L设计变更的风险管理全过程，与PT9L正式DHF/DMR无关联，不构成合规证据缺陷，予以dismiss。

### 25. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0026`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_model_reference`
- 文件：`03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件路径为"03 风险分析\\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable"，primary_scope=true，属于正式受控风险评估文件。PT3SBT出现在产品介绍章节（1.1节），作为具备蓝牙功能的产品型号标识，描述其可将体温数据传输至智能设备，属于产品功能描述中对具体型号的合理引用。该引用不构成型号混用、证据链断裂或合规缺陷，两个候选证据（MF-0026、MF-0027）来自同一行同一文本，内容一致，属于正常的产品型号功能说明，予以dismiss。

### 26. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0027`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_model_reference`
- 文件：`03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件路径为"03 风险分析\\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable"，primary_scope=true，属于正式受控风险评估文件。PT3SBT出现在产品介绍章节（1.1节），作为具备蓝牙功能的产品型号标识，描述其可将体温数据传输至智能设备，属于产品功能描述中对具体型号的合理引用。该引用不构成型号混用、证据链断裂或合规缺陷，两个候选证据（MF-0026、MF-0027）来自同一行同一文本，内容一致，属于正常的产品型号功能说明，予以dismiss。

### 27. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0028`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_model_reference`
- 文件：`03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件路径为"03 风险分析\\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01 V2.0 2024053-All appli"，primary_scope=true，属于正式受控风险控制验证文件。PT3SBT出现在产品介绍章节（1.1节），与MC-CLUSTER-0006中的表述完全一致，属于产品功能描述中对蓝牙型号的合理标识引用。两个候选证据（MF-0028、MF-0029）来自同一行同一文本，内容一致，不构成型号混用或证据链缺陷，予以dismiss。

### 28. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0029`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_model_reference`
- 文件：`03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件路径为"03 风险分析\\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01 V2.0 2024053-All appli"，primary_scope=true，属于正式受控风险控制验证文件。PT3SBT出现在产品介绍章节（1.1节），与MC-CLUSTER-0006中的表述完全一致，属于产品功能描述中对蓝牙型号的合理标识引用。两个候选证据（MF-0028、MF-0029）来自同一行同一文本，内容一致，不构成型号混用或证据链缺陷，予以dismiss。

### 29. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0051`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_product_category_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17`
- 命中文本：\|  \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \|  \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \|  \|  \| □ \|
- 驳回理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，位于Stage 11 T1样机DFMEA目录，属于PT9L正式受控文件。文件表头（第13行）明确标注产品型号"KD-5915L"（PT9L对应型号），内容描述的是电池供电、彩包装、铭牌、说明书等与额温计整机一致的结构项目。文件中"血压计"出现在功能描述列（如"给血压计供电"、"包装血压计"、"用户无法识别血压计的相关法规信息"），是对产品整机的功能性描述用语，并非引用其他产品型号，属于FMEA文件中常见的产品功能描述表达方式。不影响PT9L DHF证据链的产品身份一致性。

### 30. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0052`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_product_category_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:18`
- 命中文本：\|  \| 彩包装 \| 包装血压计 \| 腕枕无法装入彩包装或腕枕装入彩包装后晃动量太大 \| 生产人员无法包装 \| 4 \| C \| 彩包装的尺寸设计不合理 \| 2 \|  \| 实际装配 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，位于Stage 11 T1样机DFMEA目录，属于PT9L正式受控文件。文件表头（第13行）明确标注产品型号"KD-5915L"（PT9L对应型号），内容描述的是电池供电、彩包装、铭牌、说明书等与额温计整机一致的结构项目。文件中"血压计"出现在功能描述列（如"给血压计供电"、"包装血压计"、"用户无法识别血压计的相关法规信息"），是对产品整机的功能性描述用语，并非引用其他产品型号，属于FMEA文件中常见的产品功能描述表达方式。不影响PT9L DHF证据链的产品身份一致性。

### 31. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0053`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_product_category_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:19`
- 命中文本：\|  \| 彩包装 \| 包装血压计 \| 彩包装支撑强度不够 \| 彩包装褶皱或破损 \| 4 \| C \| 彩包装的材质强度不够 \| 3 \|  \| 跌落试验、运输试验 \| 2 \| 24 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，位于Stage 11 T1样机DFMEA目录，属于PT9L正式受控文件。文件表头（第13行）明确标注产品型号"KD-5915L"（PT9L对应型号），内容描述的是电池供电、彩包装、铭牌、说明书等与额温计整机一致的结构项目。文件中"血压计"出现在功能描述列（如"给血压计供电"、"包装血压计"、"用户无法识别血压计的相关法规信息"），是对产品整机的功能性描述用语，并非引用其他产品型号，属于FMEA文件中常见的产品功能描述表达方式。不影响PT9L DHF证据链的产品身份一致性。

### 32. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0054`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:20`
- 命中文本：\|  \| 彩包装 \| 包装血压计 \| 标识不清楚 内容不全面 \| 用户误用 \| 9 \| A \| 说明书印刷油墨质量不好 未完全符合法规要求 \| 4 \|  \| 目测检查 法规符合性检查 \| 5 \| 180 \| 标识内容及可识别度检验 \| 9 \| 4 \| 1 \| 36 \| 检查检验记录 \|  \|  \| □ \|
- 驳回理由：文件位于Stage 11正式T1样机DFMEA（E0 23.11），'血压计'作为产品功能描述词出现在彩包装、铭牌、说明书等部件的失效模式分析中，属于对被审查产品PT9L（腕式血压计）本身的正常功能描述，并非误引其他型号。FMEA条目中包含法规符合性检查、IEC60601-1标记耐久性要求等控制措施，内容完整合规。不构成合规证据缺陷。

### 33. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0055`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_product_category_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:21`
- 命中文本：\|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌在运输过程中脱落 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌背胶强度不够 \| 3 \|  \| 跌落试验、运输试验 \| 2 \| 24 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，位于Stage 11 T1样机DFMEA目录，属于PT9L正式受控文件。文件表头（第13行）明确标注产品型号"KD-5915L"（PT9L对应型号），内容描述的是电池供电、彩包装、铭牌、说明书等与额温计整机一致的结构项目。文件中"血压计"出现在功能描述列（如"给血压计供电"、"包装血压计"、"用户无法识别血压计的相关法规信息"），是对产品整机的功能性描述用语，并非引用其他产品型号，属于FMEA文件中常见的产品功能描述表达方式。不影响PT9L DHF证据链的产品身份一致性。

### 34. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0056`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:22`
- 命中文本：\|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌印刷内容容易被擦拭掉 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌未覆膜 \| 2 \|  \| 依IEC60601-1:2005 电气安全通用要求中7.1.3 标记耐久性要求 对铭牌进行试验 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：文件位于Stage 11正式T1样机DFMEA（E0 23.11），'血压计'作为产品功能描述词出现在彩包装、铭牌、说明书等部件的失效模式分析中，属于对被审查产品PT9L（腕式血压计）本身的正常功能描述，并非误引其他型号。FMEA条目中包含法规符合性检查、IEC60601-1标记耐久性要求等控制措施，内容完整合规。不构成合规证据缺陷。

### 35. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0057`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_product_category_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:23`
- 命中文本：\|  \| 铭牌 \| 给用户关于机器的信息 \| 标识不清楚 内容不全面 \| 用户无法识别血压计的相关法规信息 用户误用 \| 9 \| A \| 印刷油墨质量不好 未完全符合法规要求 \| 4 \|  \| 目测检查 法规符合性检查 \| 5 \| 180 \| 铭牌内容及可识别度检验 \| 9 \| 4 \| 1 \| 36 \| 检查检验记录 \|  \|  \| □ \|
- 驳回理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，位于Stage 11 T1样机DFMEA目录，属于PT9L正式受控文件。文件表头（第13行）明确标注产品型号"KD-5915L"（PT9L对应型号），内容描述的是电池供电、彩包装、铭牌、说明书等与额温计整机一致的结构项目。文件中"血压计"出现在功能描述列（如"给血压计供电"、"包装血压计"、"用户无法识别血压计的相关法规信息"），是对产品整机的功能性描述用语，并非引用其他产品型号，属于FMEA文件中常见的产品功能描述表达方式。不影响PT9L DHF证据链的产品身份一致性。

### 36. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0058`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:24`
- 命中文本：\|  \| 说明书 \| 给用户关于机器使用的信息 \| 说明书印刷不够清楚 \| 用户无法识别血压计使用的相关信息 \| 4 \| C \| 说明书印刷油墨质量不好 \| 2 \|  \| 实际使用 \| 1 \| 8 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：文件位于Stage 11正式T1样机DFMEA（E0 23.11），'血压计'作为产品功能描述词出现在彩包装、铭牌、说明书等部件的失效模式分析中，属于对被审查产品PT9L（腕式血压计）本身的正常功能描述，并非误引其他型号。FMEA条目中包含法规符合性检查、IEC60601-1标记耐久性要求等控制措施，内容完整合规。不构成合规证据缺陷。

### 37. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0060`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_model_citation`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:2`
- 命中文本：# 09a-10 PT3 transport report
- 驳回理由：MF-0060至MF-0062来自"09a-10 PT3 transport report"，该文件SN标注"PT9L-YSBG01 V1.0"，正文第12行明确"Model name: PT9L"，说明该运输报告虽以PT3命名（可能为模板来源或历史文件名），但内容已明确归属PT9L。MF-0141来自"运输试验评估报告"，评估结论明确引用"PT3运输试验报告"作为参比依据，对两机型包装进行相似性比较，结论为评估合格。这是医疗器械DHF中常见的参比评估方法，PT3作为参比机型被正式引用，有明确的评估逻辑和结论，不构成产品身份污染。文件编号PT9L-YSBG01已将该报告纳入PT9L受控体系。

### 38. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0061`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_model_citation`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:14`
- 命中文本：**1 ![直线 2](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_75410098.gif) . Test purposes**
- 驳回理由：MF-0060至MF-0062来自"09a-10 PT3 transport report"，该文件SN标注"PT9L-YSBG01 V1.0"，正文第12行明确"Model name: PT9L"，说明该运输报告虽以PT3命名（可能为模板来源或历史文件名），但内容已明确归属PT9L。MF-0141来自"运输试验评估报告"，评估结论明确引用"PT3运输试验报告"作为参比依据，对两机型包装进行相似性比较，结论为评估合格。这是医疗器械DHF中常见的参比评估方法，PT3作为参比机型被正式引用，有明确的评估逻辑和结论，不构成产品身份污染。文件编号PT9L-YSBG01已将该报告纳入PT9L受控体系。

### 39. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0062`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_model_citation`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:46`
- 命中文本：\| Corner \| 970 mm \| 1 box \| ![图片 1](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_9a00f4a6.png) \|
- 驳回理由：MF-0060至MF-0062来自"09a-10 PT3 transport report"，该文件SN标注"PT9L-YSBG01 V1.0"，正文第12行明确"Model name: PT9L"，说明该运输报告虽以PT3命名（可能为模板来源或历史文件名），但内容已明确归属PT9L。MF-0141来自"运输试验评估报告"，评估结论明确引用"PT3运输试验报告"作为参比依据，对两机型包装进行相似性比较，结论为评估合格。这是医疗器械DHF中常见的参比评估方法，PT3作为参比机型被正式引用，有明确的评估逻辑和结论，不构成产品身份污染。文件编号PT9L-YSBG01已将该报告纳入PT9L受控体系。

### 40. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0091`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_shared_component_unverified`
- 文件：`11 T1样机\PT9L包装BOM.via_xlsx.clean.md:19`
- 命中文本：\| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|
- 驳回理由：BOM中PT3来源零件均有对应的正式设计输出图纸文件存在于Stage 12 primary scope（如T040800073941030093-PT3-F21.pdf、PT3_双联弹簧_REV01.pdf、FDIR-V14_散热器压块_REV01_0714.pdf），说明这些零件的图纸已纳入PT9L设计输出清单受控管理。同时BOM中还存在PT5、T-Z1等多型号来源零件，表明该BOM体系采用保留原始图号来源型号的惯例做法，并非产品身份混淆。BOM中的"来源型号"列记录的是零件原始图号归属，属于正常的跨型号共用件标注方式，有对应设计输出文件支撑，当前证据不能证明存在缺少共用件评估记录的正式受控缺陷。

### 41. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0092`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_shared_component_unverified`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28`
- 命中文本：\| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|
- 驳回理由：BOM中PT3来源零件均有对应的正式设计输出图纸文件存在于Stage 12 primary scope（如T040800073941030093-PT3-F21.pdf、PT3_双联弹簧_REV01.pdf、FDIR-V14_散热器压块_REV01_0714.pdf），说明这些零件的图纸已纳入PT9L设计输出清单受控管理。同时BOM中还存在PT5、T-Z1等多型号来源零件，表明该BOM体系采用保留原始图号来源型号的惯例做法，并非产品身份混淆。BOM中的"来源型号"列记录的是零件原始图号归属，属于正常的跨型号共用件标注方式，有对应设计输出文件支撑，当前证据不能证明存在缺少共用件评估记录的正式受控缺陷。

### 42. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0093`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_shared_component_unverified`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35`
- 命中文本：\| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：BOM中PT3来源零件均有对应的正式设计输出图纸文件存在于Stage 12 primary scope（如T040800073941030093-PT3-F21.pdf、PT3_双联弹簧_REV01.pdf、FDIR-V14_散热器压块_REV01_0714.pdf），说明这些零件的图纸已纳入PT9L设计输出清单受控管理。同时BOM中还存在PT5、T-Z1等多型号来源零件，表明该BOM体系采用保留原始图号来源型号的惯例做法，并非产品身份混淆。BOM中的"来源型号"列记录的是零件原始图号归属，属于正常的跨型号共用件标注方式，有对应设计输出文件支撑，当前证据不能证明存在缺少共用件评估记录的正式受控缺陷。

### 43. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0094`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_shared_component_unverified`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36`
- 命中文本：\| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：BOM中PT3来源零件均有对应的正式设计输出图纸文件存在于Stage 12 primary scope（如T040800073941030093-PT3-F21.pdf、PT3_双联弹簧_REV01.pdf、FDIR-V14_散热器压块_REV01_0714.pdf），说明这些零件的图纸已纳入PT9L设计输出清单受控管理。同时BOM中还存在PT5、T-Z1等多型号来源零件，表明该BOM体系采用保留原始图号来源型号的惯例做法，并非产品身份混淆。BOM中的"来源型号"列记录的是零件原始图号归属，属于正常的跨型号共用件标注方式，有对应设计输出文件支撑，当前证据不能证明存在缺少共用件评估记录的正式受控缺陷。

### 44. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0098`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:460`
- 命中文本：功能描述 ｜ 血压计数据打包函数
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 45. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0099`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:477`
- 命中文本：\| sen_num= SENTENCE_SYSTOLIC，num=120 \| 血压计播报高压120mmHg \| 血压计播报高压120mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 46. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0100`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:478`
- 命中文本：\| sen_num= SENTENCE_DIASTOLIC，num=80 \| 血压计播报低压80mmHg \| 血压计播报高压80mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 47. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0101`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:313`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，0.5S内上位机回复ACK，用串口检测血压计发送数据 \| 串口发送加压过慢数据：<br>A0 07 00 7E A1 38 04 00 00 5B不重发 \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 48. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0102`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:314`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，上位机不回复ACK，用串口检测血压计发送数据并查看run_mode的值 \| 用串口侦测到的数据为<br>A0 07 00 7E A1 38 04 00 00 5B以0.5s重发三次<br>run_mode=MODE_erC \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 49. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0103`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:322`
- 命中文本：void Bpm_Cmd_Decete(void) ｜ Blood pressure cuff protocol parsing，血压计协议解析
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 50. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0104`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:406`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 51. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0105`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:408`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 52. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0106`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:412`
- 命中文本：4\. 按APP中“开始测量”，血压计进入测量态。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 53. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0107`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:444`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 54. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0108`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_plan`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:448`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，所有候选证据（MF-0101至MF-0108）均来自软件测试计划，语境与MC-CLUSTER-0022高度一致，均为描述PT9L血压测量功能的操作步骤和子程序测试项目（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等）。"血压计"系产品功能类别的通用描述，非异型号产品引用，不影响PT9L正式DHF/DMR，予以dismiss。

### 55. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0109`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:54`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 56. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0110`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:56`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 57. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0111`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:60`
- 命中文本：4\. **按 APP 中“开始测量”，血压计进入测量态。**
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 58. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0112`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:108`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 59. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0113`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:116`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 60. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0114`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:128`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击APP界面的暂停图标退出测量界面。退出后血压计不加压，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 61. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0115`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:130`
- 命中文本：2\. 点击“开始测量”正常开始测量，在血压计测量过程中点击APP界面的暂停图标退出测量界面。血压计立即关泵开阀，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 62. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0116`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_test_record`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:138`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击HOME键离开APP界面。退出后血压计不加压，再次打开APP，点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，所有候选证据（MF-0098至MF-0116）均来自软件系统测试记录，语境为描述PT9L设备的血压测量操作步骤（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计停泵放气"等），以及软件函数功能描述（"血压计数据打包函数"、"血压计协议解析"）。"血压计"在此处是对PT9L产品类别的通用称谓，并非指代另一具体型号产品，属于合理的功能描述性引用，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 63. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0117`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`draft_template_sheet_outside_primary_scope`
- 文件：`11 T1样机\软件文件底稿\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70`
- 命中文本：## Sheet: 模板修改记录
- 驳回理由：该cluster的primary_scope明确标注为false，文件路径为"11 T1样机\\软件文件底稿\\..."，属于底稿目录而非正式受控文件目录。内容（"模板修改记录"Sheet空白）与MC-CLUSTER-0010（Stage 07正式文件中的同名Sheet）高度重复，正式文件问题已在MC-CLUSTER-0010中confirm处理。底稿文件中的模板结构残留属于工作过程文件的正常状态，不影响PT9L正式DHF/DMR的证据链完整性，予以dismiss。

### 64. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0118`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2`
- 命中文本：# BP3L 软件图样E0 23.11
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 65. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0119`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:48`
- 命中文本：![图片 4](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d805c950.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 66. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0120`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50`
- 命中文本：![图片 6](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_a0cd39dd.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 67. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0121`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:52`
- 命中文本：![Picture 3](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_20a262b4.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 68. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0122`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54`
- 命中文本：![图片 8](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_e11cac5c.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 69. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0123`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:56`
- 命中文本：![Picture 7](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_f49c074.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 70. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0124`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:58`
- 命中文本：![图片 10](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_ae5eec4.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 71. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0125`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_document_in_dhf_folder`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:60`
- 命中文本：![图片 11](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_2540465a.gif)
- 驳回理由：全部8个候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11\\"，属于底稿/工作文件目录。同一文件的正式受控版本存在于"07 软件设计方案E0 23.11\\软件图样E0 23.11\\"（Stage 07 primary scope，count=8）。Stage 11中的副本为底稿留存，不属于正式DHF受控文件。文件内部编号已标注为PT9L-RJTY01 V1.0，文件名BP3L为历史来源命名，正式编号已更正为PT9L。该情形属于辅助/历史范围的底稿文件，当前证据不构成正式DHF产品身份污染错误。

### 72. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0126`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:79`
- 命中文本：1\. “血压测量态”由“加压前处理”、“加压测量过程”、“发送测量数据”三个子模块组成。“加压前处理”主要进行加压前的浮零处理，为后续找到基准零点压力；“加压测量过程”为血压计充气过程，主要包含加压速度判断、压力平台判断、检波、抗干扰和计算过程；“发送测量数据”包括血压计在测量过程中向上位机发送压力、脉搏波等实时数据，以及在测量结束后向上位机发送血压、心跳等测量结果。
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 73. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0127`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:87`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 74. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0128`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:88`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 75. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0129`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:93`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 76. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0130`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:110`
- 命中文本：通讯方案采用《iHealth血压计通信协议V2.4》中如下命令字，具体指令格式参见《iHealth血压计通信协议V2.4》（GF-10-010 V2.4）。
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 77. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0131`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:127`
- 命中文本：\| 命令型 \| 0x32 \| 浮零完毕 \| 无 \| 无 \| 下位机回复ACK，单台血压计测量或多台血压计组成测量系统，但无需同时加压机型适用 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 78. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0132`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:128`
- 命中文本：\| 实时数据型 \| 0x30 \| 浮零中 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK ，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据浮零指令中的数据信息确定是否发送启动加压指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 79. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0133`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`generic_product_category_term_in_software_design`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:130`
- 命中文本：\| 实时数据型 \| 0x3C/<br>0x3D \| 蓝牙接口测量过程数据 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据测量数据指令中的数据信息确定是否发送测量完毕指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，所有候选证据（MF-0126至MF-0133）均来自软件方案设计文件，语境为描述PT9L血压测量功能模块（如"血压测量态"子模块说明、软件设计规格表中的功能描述、通信协议中的"血压计"指代）。"血压计"在此处是对PT9L产品类别及其功能的通用称谓，引用的通信协议（iHealth血压计通信协议V2.4）属于共用协议规范的合理引用，不指代另一具体型号产品，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 80. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0134`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:107`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：所有命中证据均位于"11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11"文件中，该文件为PT9L T1样机阶段的软件需求规格书底稿。文中"血压计"指代的正是PT9L产品本身（上电、关机、加压、测量、蓝牙连接等功能均为PT9L的核心功能描述），属于产品通用名称的正常使用，并非引用其他型号产品。primary_scope=false且为Stage 11底稿，不影响正式DHF/DMR证据链，可驳回。

### 81. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0135`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:108`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：所有命中证据均位于"11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11"文件中，该文件为PT9L T1样机阶段的软件需求规格书底稿。文中"血压计"指代的正是PT9L产品本身（上电、关机、加压、测量、蓝牙连接等功能均为PT9L的核心功能描述），属于产品通用名称的正常使用，并非引用其他型号产品。primary_scope=false且为Stage 11底稿，不影响正式DHF/DMR证据链，可驳回。

### 82. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0136`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:113`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：所有命中证据均位于"11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11"文件中，该文件为PT9L T1样机阶段的软件需求规格书底稿。文中"血压计"指代的正是PT9L产品本身（上电、关机、加压、测量、蓝牙连接等功能均为PT9L的核心功能描述），属于产品通用名称的正常使用，并非引用其他型号产品。primary_scope=false且为Stage 11底稿，不影响正式DHF/DMR证据链，可驳回。

### 83. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0137`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:127`
- 命中文本：\| 3 \| 《PT9L设计输入-性能规格部分（三）IEC/EN 80601-2-30 》<br>(PT9L-SRXN01 V1.0) \| 201.7.2.<br>101 \| 自动血压计的显示 \|
- 驳回理由：文件为PT9L软件需求规格（Stage 11，primary_scope=false），引用来源为'PT9L设计输入-性能规格部分（三）IEC/EN 80601-2-30'（文件编号PT9L-SRXN01 V1.0），条款201.7.2.101'自动血压计的显示'是IEC/EN 80601-2-30标准中针对自动血压计的专用条款，PT9L本身即为自动血压计产品，此处为正常的标准条款引用，属于合理的设计输入溯源。不构成合规证据缺陷。

### 84. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0138`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:151`
- 命中文本：上电后系统进入关机态（低功耗状态），不开机并且不充电时灯不亮。在关机态，与手机蓝牙进行连接并建立通信后，绿灯常亮，启动iHealth APP点击开始测量键开始测量，测量过程中血压计将得到的压力及心跳信息传输至手机；测量完毕后，手机显示高压、低压、心率、血压分类、心律不齐（如果有）；测量过程中若出现异常，手机会显示相应提示信息。当电池电量不足时，手机会显示电量不足提示并且血压计上的红色LED灯闪烁。
- 驳回理由：所有命中证据均位于"11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11"文件中，该文件为PT9L T1样机阶段的软件需求规格书底稿。文中"血压计"指代的正是PT9L产品本身（上电、关机、加压、测量、蓝牙连接等功能均为PT9L的核心功能描述），属于产品通用名称的正常使用，并非引用其他型号产品。primary_scope=false且为Stage 11底稿，不影响正式DHF/DMR证据链，可驳回。

### 85. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0139`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:172`
- 命中文本：□ 自动关机时间：血压计与手机蓝牙断开连接后，血压计自动关机
- 驳回理由：所有命中证据均位于"11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11"文件中，该文件为PT9L T1样机阶段的软件需求规格书底稿。文中"血压计"指代的正是PT9L产品本身（上电、关机、加压、测量、蓝牙连接等功能均为PT9L的核心功能描述），属于产品通用名称的正常使用，并非引用其他型号产品。primary_scope=false且为Stage 11底稿，不影响正式DHF/DMR证据链，可驳回。

### 86. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0140`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_metadata_in_draft_scope`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:226`
- 命中文本：第 0 页 / 共 5 页 模板版本： I
- 驳回理由：该候选位于Stage 11 T1样机软件文件底稿目录，primary_scope=false，文件路径含"底稿"字样，属草稿/工作文件范围。"第 0 页 / 共 5 页 模板版本：I"为文档排版模板的页脚元数据，不影响PT9L正式DHF/DMR软件需求规格的受控状态。按规则：草稿/历史范围且不影响正式证据链，应dismiss。

### 87. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0141`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_model_citation`
- 文件：`11 T1样机\运输\运输试验评估报告2020-3-27.via_lo_html.clean.md:37`
- 命中文本：\| **评 估 结 论** \| 根据“ PT3 运输试验报告”评估：<br>对比结果说明： 两机型相比较，彩包装、外箱材质、开合方式、连接方式均相同、两机型相比较彩包装、外箱尺寸、重量、材质均相似，故评估该包装对本产品在运输过程中整机的安全和性能无影响，评估合格。<br>☑ **合格** □ **不合格** *说明：*<br>□ **包装形式不同项差别较大，不能评估运输过程对整机安全和性能 的 影响，需进行运输试验** \|  \|
- 驳回理由：MF-0060至MF-0062来自"09a-10 PT3 transport report"，该文件SN标注"PT9L-YSBG01 V1.0"，正文第12行明确"Model name: PT9L"，说明该运输报告虽以PT3命名（可能为模板来源或历史文件名），但内容已明确归属PT9L。MF-0141来自"运输试验评估报告"，评估结论明确引用"PT3运输试验报告"作为参比依据，对两机型包装进行相似性比较，结论为评估合格。这是医疗器械DHF中常见的参比评估方法，PT3作为参比机型被正式引用，有明确的评估逻辑和结论，不构成产品身份污染。文件编号PT9L-YSBG01已将该报告纳入PT9L受控体系。

### 88. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0142`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_component_reference_unverified`
- 文件：`12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50`
- 命中文本：\| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|
- 驳回理由：MF-0142所在BOM（机芯类组件清单PT9L-EBOM01 V1.0）中PT9C-CNTP01 V1.0 PCB有唯一物料编号K0118000084609A1106，与MC-CLUSTER-0019中PT3来源零件的处理方式一致，均属于BOM保留原始图号来源型号的惯例做法。该BOM同时存在多型号来源零件引用，说明跨型号共用件引用在该DHF体系中属于常规做法。当前证据中未发现该PCB被错误使用或导致产品身份混淆的直接证据，仅凭BOM中型号标注无法证明缺少共用件说明属于正式受控缺陷。按最终裁决政策，当前证据不构成可确认错误，应选择dismiss。

### 89. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0170`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_reference_as_technical_description`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:10`
- 命中文本：## 0. 标题栏（A 级，外购件 Famidoc 模板）
- 驳回理由：该cluster位于Stage 12主审范围（primary_scope=true），但两处"模板"出现均为技术描述性内容：MF-0170中"外购件Famidoc模板"为章节标题对图纸来源的说明，MF-0171中"Famidoc供应商标准A4横向模板"为图框字段的实际填写内容，描述的是供应商使用的图框规格。这是对外购件图纸格式的合理引用说明，图纸本身标题栏字段（零件名、图号、审批等）均已填写完整（见nearby_context中PART NAME=散热器压块、iHealth审批=2017-07-14等），不存在空白或未填问题。按规则：合理引用，不影响证据链，应dismiss。

### 90. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0171`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_reference_as_technical_description`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:26`
- 命中文本：\| **图框** \| Famidoc 供应商标准 A4 横向模板 \|
- 驳回理由：该cluster位于Stage 12主审范围（primary_scope=true），但两处"模板"出现均为技术描述性内容：MF-0170中"外购件Famidoc模板"为章节标题对图纸来源的说明，MF-0171中"Famidoc供应商标准A4横向模板"为图框字段的实际填写内容，描述的是供应商使用的图框规格。这是对外购件图纸格式的合理引用说明，图纸本身标题栏字段（零件名、图号、审批等）均已填写完整（见nearby_context中PART NAME=散热器压块、iHealth审批=2017-07-14等），不存在空白或未填问题。按规则：合理引用，不影响证据链，应dismiss。

### 91. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0200`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_in_early_drawing_out_of_scope`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\上盖20210727.pdf.md:38`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：该cluster的primary_scope=false，文件路径含"早期图纸"子目录（上盖20210727.pdf.md、探头20210727.pdf.md），日期为2021年，属历史早期设计阶段文件。"4条标准ABS模板"为章节标题对技术要求来源的描述性标注，非空白或未填字段。早期图纸不在PT9L正式DHF/DMR主审范围内，按规则：历史/草稿/废案范围，应dismiss。

### 92. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0201`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_in_early_drawing_out_of_scope`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\探头20210727.pdf.md:25`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：该cluster的primary_scope=false，文件路径含"早期图纸"子目录（上盖20210727.pdf.md、探头20210727.pdf.md），日期为2021年，属历史早期设计阶段文件。"4条标准ABS模板"为章节标题对技术要求来源的描述性标注，非空白或未填字段。早期图纸不在PT9L正式DHF/DMR主审范围内，按规则：历史/草稿/废案范围，应dismiss。

### 93. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0239`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:31`
- 命中文本：\| 型号 \| PT9L \| PT3 \|
- 驳回理由：所有候选（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告'，primary_scope=false，明确位于废案与备份目录。文件内容显示PT3作为PT9L的同品种对比医疗器械（已注册产品，注册证号：津械注准20192070046）被引用，属于临床评价报告中标准的同品种比较引用，符合《临床评价指导原则》要求。该文件已被标注为废案，不在正式DHF主审范围内，PT3的出现属于合理的历史参考引用，不影响PT9L正式DHF/DMR证据链。

### 94. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0240`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_scope_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:36`
- 命中文本：\| 符合注册要求的使用说明书 \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT9L） \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT3） \|
- 驳回理由：文件路径明确为'18 设计确认\废案与备份\7.临床评价报告'，属于废案与备份目录（primary_scope=false，stage=Stage 18废案）。PT3作为同品种医疗器械出现在临床评价报告的对比表格中，是临床评价路径中同品种对比的标准做法。该文件为废案，不代表正式DHF/DMR中的受控证据。即使存在问题也不影响PT9L正式DHF/DMR证据链。

### 95. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0241`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:46`
- 命中文本：PT9L红外体温计和PT3红外体温计均为有源器械。其等效性比较参见表3-1。
- 驳回理由：所有候选（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告'，primary_scope=false，明确位于废案与备份目录。文件内容显示PT3作为PT9L的同品种对比医疗器械（已注册产品，注册证号：津械注准20192070046）被引用，属于临床评价报告中标准的同品种比较引用，符合《临床评价指导原则》要求。该文件已被标注为废案，不在正式DHF主审范围内，PT3的出现属于合理的历史参考引用，不影响PT9L正式DHF/DMR证据链。

### 96. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0242`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:83`
- 命中文本：\| PT3 \| ![图片 5](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_25bd38c1.png) \| PT9L \| ![图片 38](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_c235e89e.png) \|
- 驳回理由：所有候选（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告'，primary_scope=false，明确位于废案与备份目录。文件内容显示PT3作为PT9L的同品种对比医疗器械（已注册产品，注册证号：津械注准20192070046）被引用，属于临床评价报告中标准的同品种比较引用，符合《临床评价指导原则》要求。该文件已被标注为废案，不在正式DHF主审范围内，PT3的出现属于合理的历史参考引用，不影响PT9L正式DHF/DMR证据链。

### 97. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0243`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:93`
- 命中文本：数据来源为柯顿（天津）电子医疗器械有限公司PT3红外体温计于2013年取得由中国人民解放军第 100医院及苏州市立医院本部医院所进行的临床试验报告所得，试验主要进行的是临床验证。
- 驳回理由：所有候选（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告'，primary_scope=false，明确位于废案与备份目录。文件内容显示PT3作为PT9L的同品种对比医疗器械（已注册产品，注册证号：津械注准20192070046）被引用，属于临床评价报告中标准的同品种比较引用，符合《临床评价指导原则》要求。该文件已被标注为废案，不在正式DHF主审范围内，PT3的出现属于合理的历史参考引用，不影响PT9L正式DHF/DMR证据链。

### 98. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0244`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:97`
- 命中文本：产品的临床试验由护理人员负责实施，采取自身对照试验方法，采用TH30F非接触红外额式体温与经过校准的水银玻璃体温计同步测定的方法，验证非接触红外额式体温计的准确度。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 99. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0245`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:107`
- 命中文本：具体参加附件：TH30F临床研究方案及临床试验报告见附3。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 100. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0246`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:111`
- 命中文本：同品种医疗器械TH30F未收到投诉，未发现不良事件。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 101. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0247`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_scope_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:115`
- 命中文本：同品种医疗器械TH30F未采取过与临床风险相关的纠正措施。
- 驳回理由：文件路径为'18 设计确认\废案与备份\7.临床评价报告'，属于废案与备份目录（primary_scope=false）。TH30F作为同品种医疗器械在临床评价报告中被引用，用于说明不良事件、纠正措施及中国人群数据，符合临床评价同品种对比的规范要求。文件为废案，不影响正式DHF/DMR证据链完整性。

### 102. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0248`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 103. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0249`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 104. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0250`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 105. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0251`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 106. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0252`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:190`
- 命中文本：（七）PT3红外体温计准确度验证报告
- 驳回理由：所有候选（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告'，primary_scope=false，明确位于废案与备份目录。文件内容显示PT3作为PT9L的同品种对比医疗器械（已注册产品，注册证号：津械注准20192070046）被引用，属于临床评价报告中标准的同品种比较引用，符合《临床评价指导原则》要求。该文件已被标注为废案，不在正式DHF主审范围内，PT3的出现属于合理的历史参考引用，不影响PT9L正式DHF/DMR证据链。

### 107. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0253`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_scope_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:196`
- 命中文本：PT3和TH30F为同品种医疗器械，综合上述数据集的分析结果，PT9L在正常使用条件下，产品可达到预期性能；与预期受益相比较，产品的风险可接受。
- 驳回理由：文件路径为'18 设计确认\废案与备份\7.临床评价报告'，属于废案与备份目录（primary_scope=false）。TH30F作为同品种医疗器械在临床评价报告中被引用，用于说明不良事件、纠正措施及中国人群数据，符合临床评价同品种对比的规范要求。文件为废案，不影响正式DHF/DMR证据链完整性。

### 108. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0254`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:12`
- 命中文本：型号规格：PT9CL
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 109. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0255`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:34`
- 命中文本：我公司天津九安医疗电子股份有限公司研制开发的PT9C型红外体温计是一款通过接收人体额头部位散发的红外能量，来测量人体温度的红外体温计。
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 110. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0256`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 111. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0257`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 112. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0258`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 113. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0259`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：所有候选（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用'，primary_scope=false，文件名已明确标注'中国版本不适用'，属于废案文件。文件内容显示该临床评价报告原为PT9C申报文件，描述PT9C与PT3的等同性比较，属于PT9C注册申报的历史文件，被归入PT9L DHF废案备份目录留存。该文件不在正式DHF主审范围，PT9C的出现是历史文件本身的产品标识，属于合理的历史来源归档，不影响PT9L正式DHF/DMR证据链完整性。

### 114. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0260`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 115. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0261`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 116. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0262`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 117. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0263`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 118. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0264`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:22`
- 命中文本：\| 依据标准 \|  \| 柯顿（天津）电子医疗器械有限公司《红外体温计技术要求》 \|  \|  \|  \| 产品型号 \|  \|  \| PT3与TH30F \|  \| 试验时间 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 119. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0265`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:22`
- 命中文本：\| 依据标准 \|  \| 柯顿（天津）电子医疗器械有限公司《红外体温计技术要求》 \|  \|  \|  \| 产品型号 \|  \|  \| PT3与TH30F \|  \| 试验时间 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

### 120. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0266`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:34`
- 命中文本：\| 测试项目 \| #1号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及附件2比对测试报告），primary_scope=false。TH30F在文件中作为PT3临床试验的对照品（非接触红外额式体温计与水银玻璃体温计对照）以及PT3性能比对测试的参照型号被引用，属于临床评价方法学中的合理引用。文件明确标注为废案，不在正式DHF主审范围内，不影响PT9L正式DHF/DMR。

> 仅展示前 120 条，完整数据见 `13_mechanical_agent_review/mechanical_dismissed_candidates.jsonl`。