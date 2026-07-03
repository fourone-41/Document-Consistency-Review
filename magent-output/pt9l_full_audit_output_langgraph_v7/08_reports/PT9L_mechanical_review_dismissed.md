# PT9L 机械候选复审驳回/非错误清单

> 生成时间：2026-07-01T14:27:18
> 范围：mechanical_review_node 经一轮或二轮 LLM 复审后判定为 dismiss 的机械候选。dismiss 表示当前证据下不构成可确认错误，不等于人工最终裁决。

## 1. 摘要

- 驳回/非错误候选数：365

## 2. 按 Agent 统计

| Agent | 数量 |
|---|---:|
| Product Identity Agent | 169 |
| Document Control Agent | 87 |
| Regulatory Agent | 78 |
| Hardware Agent | 31 |

## 3. 样例清单

### 1. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0001`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_label_not_model_contamination`
- 文件：`01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:2`
- 命中文本：# 客户需求书E0-血压计 23.6
- 驳回理由：文件《客户需求书E0-血压计 23.6》位于Stage 01立项批准书目录下，属于PT9L正式DHF的客户需求阶段文件。文件标题及内容中的"血压计"系对本产品所属品类（无创血压/体温测量类医疗器械）的通用描述，并非引用其他型号产品。结合PF-0001至PF-0004的内容（温度测量规格、功能需求、环保要求等），全部内容均指向本次开发产品，无任何其他型号编号出现。"血压计"在此为合理的产品类别标签，不影响PT9L正式DHF/DMR的产品身份证据链，予以dismiss。

### 2. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0002`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:2`
- 命中文本：# V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L美亚-FXJH01 V1.0，属于前代型号PT2L的历史风险管理计划。primary_scope=false已标注非主审范围。该文件不构成PT9L DHF/DMR的合规证据缺陷，属于历史/前代型号文件范围，予以dismiss。

### 3. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0003`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:117`
- 命中文本：![形状2](V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html_assets/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0_html_f9d9f2af.gif) Acceptable Control as much as possible Not acceptable
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L美亚-FXJH01 V1.0，属于前代型号PT2L的历史风险管理计划。primary_scope=false已标注非主审范围。该文件不构成PT9L DHF/DMR的合规证据缺陷，属于历史/前代型号文件范围，予以dismiss。

### 4. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0004`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:6`
- 命中文本：D N : PT2L( 美亚 ) - SGFP 01 V1.0 Risk Assessment Report
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 5. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0005`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 6. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0006`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:81`
- 命中文本：When the PT2L infrared thermometer project was launched, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 7. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0007`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:83`
- 命中文本：Currently, the PT2L infrared thermometer is in the feasibility review stage of design changes. The purpose of this risk management review is to determine whether the design changes of the PT2L infrared thermometer will g
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 8. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0008`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:107`
- 命中文本：Please find the document *Risk Management P* *lan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 9. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0009`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:124`
- 命中文本：\| **A.2.1** \| What is the intended use and how is the medical device to be used?<br>□ what is the medical device’s role relative to:<br>□ what are the indications for use (e.g. patient population, user profile, use env
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGFP01 V1.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02亦为PT2L项目。primary_scope=false已标注非主审范围。所有候选均为PT2L历史风险评估文件的正常内容，不构成PT9L合规缺陷，予以dismiss。

### 10. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0010`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:6`
- 命中文本：D N: PT2L( 美亚 ) - SGYS 01 V 1 .0 Verification of risk control measure and residual risk evaluation report
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 11. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0011`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 12. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0012`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:95`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 13. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0013`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:198`
- 命中文本：型式试验报告：PT2L(美亚)-XNTB01 V1.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 14. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0014`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:202`
- 命中文本：说明书：PT2L(美亚)-SMSY02 V2.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 15. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0015`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:204`
- 命中文本：易用性报告：PT2L(美亚)-UETR01 V1.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 16. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0016`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:206`
- 命中文本：临床评估报告：PT2L(美亚)-RLPB01 V1.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 17. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0017`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:208`
- 命中文本：软件确认报告：PT2L(美亚)-RJQB01 V1.0
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L(美亚)-SGYS01 V1.0，产品型号字段明确记录为PT2L。文件中引用的型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等均为PT2L(美亚)系列文件编号，属于PT2L历史项目内部交叉引用，合理且自洽。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 18. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0018`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:6`
- 命中文本：DN ： PT2L-FXGB01 V 4 .0 Risk Management Report
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 19. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0019`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 20. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0020`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:60`
- 命中文本：PT2L replaced the MCU with a smaller memory in hardware to ensure that the new MCU has sufficient performance and functions while meeting cost requirements. Re-evaluated the structural design in structure to find parts t
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 21. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0021`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:64`
- 命中文本：At the same time as the PT2L infrared thermometer project was established, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 22. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0022`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:66`
- 命中文本：The risk management plan determined the risk acceptance criteria for the PT2L infrared thermometer and arranged the review of the product's risk management activities.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 23. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0023`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:70`
- 命中文本：In the early development and prototype stages of the PT2L infrared thermometer, the risk management team conducted a risk management review and formed relevant risk management documents.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 24. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0024`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:72`
- 命中文本：While the PT2L infrared thermometer was undergoing design changes, the company formed a risk management team to ensure that the risk management activities for the design changes of the project were effectively implemente
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 25. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0025`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_file_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:96`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确为"03 风险分析\\2L风险改 - 历史文件"，文件标题及文档编号均为PT2L-FXGB01 V4.0，产品型号字段明确记录为PT2L，项目编号2020-002-WX02为PT2L项目。文件内容完整描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理活动，属于PT2L历史项目的完整风险管理报告。primary_scope=false已标注非主审范围，不构成PT9L合规缺陷，予以dismiss。

### 26. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0026`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_variant_reference`
- 文件：`03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件为正式风险评估报告IFT-FXPJ01 V2.0（primary_scope=true），PT3SBT出现在产品介绍段落（1.1节），用于说明该型号具备蓝牙传输功能的差异化特性（"PT3SBT can transmit the temperature to a smart device with Bluetooth"），属于产品族系内型号变体的功能描述性引用。该引用方式在多型号共用风险文件中属于合理做法，不存在型号混淆、证据链断裂或受控文件错误标注问题。两个候选（MF-0026、MF-0027）指向同一行同一文本，内容完全一致，无额外风险信号，予以dismiss。

### 27. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0027`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_variant_reference`
- 文件：`03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件为正式风险评估报告IFT-FXPJ01 V2.0（primary_scope=true），PT3SBT出现在产品介绍段落（1.1节），用于说明该型号具备蓝牙传输功能的差异化特性（"PT3SBT can transmit the temperature to a smart device with Bluetooth"），属于产品族系内型号变体的功能描述性引用。该引用方式在多型号共用风险文件中属于合理做法，不存在型号混淆、证据链断裂或受控文件错误标注问题。两个候选（MF-0026、MF-0027）指向同一行同一文本，内容完全一致，无额外风险信号，予以dismiss。

### 28. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0028`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_variant_reference`
- 文件：`03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件为正式风险控制验证报告IFT-FXYS01 V2.0（primary_scope=true），PT3SBT同样出现在产品介绍段落（1.1节），描述蓝牙功能变体，与MC-CLUSTER-0006情形一致，属于产品族系内型号变体的功能描述性引用。两个候选（MF-0028、MF-0029）指向同一行同一文本，内容完全一致。该引用不影响风险控制验证的完整性与受控状态，不构成PT9L合规证据缺陷，予以dismiss。

### 29. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0029`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_variant_reference`
- 文件：`03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85`
- 命中文本：The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea
- 驳回理由：文件为正式风险控制验证报告IFT-FXYS01 V2.0（primary_scope=true），PT3SBT同样出现在产品介绍段落（1.1节），描述蓝牙功能变体，与MC-CLUSTER-0006情形一致，属于产品族系内型号变体的功能描述性引用。两个候选（MF-0028、MF-0029）指向同一行同一文本，内容完全一致。该引用不影响风险控制验证的完整性与受控状态，不构成PT9L合规证据缺陷，予以dismiss。

### 30. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0030`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_label_not_model_contamination`
- 文件：`05 结构设计方案E0 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2`
- 命中文本：# 结构设计方案评审检查表-血压计E0 23.11
- 驳回理由：文件《结构设计方案评审检查表-血压计E0 23.11》位于Stage 05结构设计方案目录下，属于PT9L正式DHF受控范围。文件标题中"血压计"系产品品类描述，与MC-CLUSTER-0001情形相同，为合理的品类标签用法。现有证据（仅MF-0030，内容为Sheet2标题行）未显示任何其他型号编号，不构成产品身份污染，予以dismiss。

### 31. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0040`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_template_sheet_name`
- 文件：`07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70`
- 命中文本：## Sheet: 模板修改记录
- 驳回理由：MF-0040所在文件为"软件质量策划评审检查表E0 23.11.via_xlsx.clean.md"，"## Sheet: 模板修改记录"是Excel工作簿中一个Sheet的名称，其下方表格结构（修改日期、修改人、修改内容）为标准变更历史记录区域。该Sheet名称本身是文件设计的一部分，用于记录模板版本演变，并非占位符或待填字段。即使该Sheet当前无填写记录，也属于变更历史为空的正常情况，不影响文件的受控状态和证据链完整性。误报，予以dismiss。

### 32. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0054`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_product_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:20`
- 命中文本：\|  \| 彩包装 \| 包装血压计 \| 标识不清楚 内容不全面 \| 用户误用 \| 9 \| A \| 说明书印刷油墨质量不好 未完全符合法规要求 \| 4 \|  \| 目测检查 法规符合性检查 \| 5 \| 180 \| 标识内容及可识别度检验 \| 9 \| 4 \| 1 \| 36 \| 检查检验记录 \|  \|  \| □ \|
- 驳回理由：证据来源为Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被包装/被标识的产品本体出现（如"包装血压计"、"给用户关于机器的信息"等），系对PT9L产品功能的正常描述，并非误引其他型号。相关FMEA条目（彩包装、铭牌、说明书标识风险）均指向PT9L本机，RPN评估及控制措施完整，不构成合规证据缺陷。

### 33. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0056`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_product_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:22`
- 命中文本：\|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌印刷内容容易被擦拭掉 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌未覆膜 \| 2 \|  \| 依IEC60601-1:2005 电气安全通用要求中7.1.3 标记耐久性要求 对铭牌进行试验 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：证据来源为Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被包装/被标识的产品本体出现（如"包装血压计"、"给用户关于机器的信息"等），系对PT9L产品功能的正常描述，并非误引其他型号。相关FMEA条目（彩包装、铭牌、说明书标识风险）均指向PT9L本机，RPN评估及控制措施完整，不构成合规证据缺陷。

### 34. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0058`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_product_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:24`
- 命中文本：\|  \| 说明书 \| 给用户关于机器使用的信息 \| 说明书印刷不够清楚 \| 用户无法识别血压计使用的相关信息 \| 4 \| C \| 说明书印刷油墨质量不好 \| 2 \|  \| 实际使用 \| 1 \| 8 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：证据来源为Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被包装/被标识的产品本体出现（如"包装血压计"、"给用户关于机器的信息"等），系对PT9L产品功能的正常描述，并非误引其他型号。相关FMEA条目（彩包装、铭牌、说明书标识风险）均指向PT9L本机，RPN评估及控制措施完整，不构成合规证据缺陷。

### 35. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0060`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`cross_model_transport_evaluation_reference`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:2`
- 命中文本：# 09a-10 PT3 transport report
- 驳回理由：MF-0060至MF-0062所在文件《09a-10 PT3 transport report》虽文件名含PT3，但文件正文第12行明确标注"Model name: PT9L"，文件编号为PT9L-YSBG01 V1.0，表明该运输报告本身即为PT9L的正式运输试验报告，文件名中"PT3"可能为试验序号或内部编号（"09a-10 PT3"中PT3疑为"Package Test 3"或试验编号），不代表产品型号PT3。MF-0141《运输试验评估报告》中明确引用"PT3运输试验报告"作为评估基准，并对两机型包装进行了逐项对比，结论为评估合格，属于正式的同类机型评估引用，符合医疗器械DHF中利用相似产品数据进行等效评估的常规做法。整体不构成产品身份污染，予以dismiss。但建议确认MF-0141评估报告中被评估产品型号是否明确标注为PT9L，以及签字批准栏是否完整。

### 36. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0061`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`cross_model_transport_evaluation_reference`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:14`
- 命中文本：**1 ![直线 2](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_75410098.gif) . Test purposes**
- 驳回理由：MF-0060至MF-0062所在文件《09a-10 PT3 transport report》虽文件名含PT3，但文件正文第12行明确标注"Model name: PT9L"，文件编号为PT9L-YSBG01 V1.0，表明该运输报告本身即为PT9L的正式运输试验报告，文件名中"PT3"可能为试验序号或内部编号（"09a-10 PT3"中PT3疑为"Package Test 3"或试验编号），不代表产品型号PT3。MF-0141《运输试验评估报告》中明确引用"PT3运输试验报告"作为评估基准，并对两机型包装进行了逐项对比，结论为评估合格，属于正式的同类机型评估引用，符合医疗器械DHF中利用相似产品数据进行等效评估的常规做法。整体不构成产品身份污染，予以dismiss。但建议确认MF-0141评估报告中被评估产品型号是否明确标注为PT9L，以及签字批准栏是否完整。

### 37. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0062`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`cross_model_transport_evaluation_reference`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:46`
- 命中文本：\| Corner \| 970 mm \| 1 box \| ![图片 1](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_9a00f4a6.png) \|
- 驳回理由：MF-0060至MF-0062所在文件《09a-10 PT3 transport report》虽文件名含PT3，但文件正文第12行明确标注"Model name: PT9L"，文件编号为PT9L-YSBG01 V1.0，表明该运输报告本身即为PT9L的正式运输试验报告，文件名中"PT3"可能为试验序号或内部编号（"09a-10 PT3"中PT3疑为"Package Test 3"或试验编号），不代表产品型号PT3。MF-0141《运输试验评估报告》中明确引用"PT3运输试验报告"作为评估基准，并对两机型包装进行了逐项对比，结论为评估合格，属于正式的同类机型评估引用，符合医疗器械DHF中利用相似产品数据进行等效评估的常规做法。整体不构成产品身份污染，予以dismiss。但建议确认MF-0141评估报告中被评估产品型号是否明确标注为PT9L，以及签字批准栏是否完整。

### 38. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0091`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`shared_component_cross_model_reference_in_bom`
- 文件：`11 T1样机\PT9L包装BOM.via_xlsx.clean.md:19`
- 命中文本：\| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|
- 驳回理由：PT9L包装BOM（MF-0091）和总装类组件清单PT9L-ABOM01（MF-0092至MF-0094）均为PT9L正式DHF/DMR的受控BOM文件，文件标题和编号均明确归属PT9L。BOM中PT3来源的零件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01）以"来源型号"列标注PT3，这是医疗器械制造企业BOM中标注共用件原始开发型号的常规做法，表明这些零件最初为PT3型号开发但在PT9L中共用。同一BOM中同时存在PT9L、PT5、PT1、T-Z1等多个来源型号标注，进一步印证这是系统性的共用件管理方式。零件本身已通过料号（K/T开头编号）进行唯一标识和受控管理，不影响PT9L产品身份的完整性，予以dismiss。

### 39. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0092`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`shared_component_cross_model_reference_in_bom`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28`
- 命中文本：\| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|
- 驳回理由：PT9L包装BOM（MF-0091）和总装类组件清单PT9L-ABOM01（MF-0092至MF-0094）均为PT9L正式DHF/DMR的受控BOM文件，文件标题和编号均明确归属PT9L。BOM中PT3来源的零件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01）以"来源型号"列标注PT3，这是医疗器械制造企业BOM中标注共用件原始开发型号的常规做法，表明这些零件最初为PT3型号开发但在PT9L中共用。同一BOM中同时存在PT9L、PT5、PT1、T-Z1等多个来源型号标注，进一步印证这是系统性的共用件管理方式。零件本身已通过料号（K/T开头编号）进行唯一标识和受控管理，不影响PT9L产品身份的完整性，予以dismiss。

### 40. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0093`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`shared_component_cross_model_reference_in_bom`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35`
- 命中文本：\| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：PT9L包装BOM（MF-0091）和总装类组件清单PT9L-ABOM01（MF-0092至MF-0094）均为PT9L正式DHF/DMR的受控BOM文件，文件标题和编号均明确归属PT9L。BOM中PT3来源的零件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01）以"来源型号"列标注PT3，这是医疗器械制造企业BOM中标注共用件原始开发型号的常规做法，表明这些零件最初为PT3型号开发但在PT9L中共用。同一BOM中同时存在PT9L、PT5、PT1、T-Z1等多个来源型号标注，进一步印证这是系统性的共用件管理方式。零件本身已通过料号（K/T开头编号）进行唯一标识和受控管理，不影响PT9L产品身份的完整性，予以dismiss。

### 41. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0094`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`shared_component_cross_model_reference_in_bom`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36`
- 命中文本：\| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：PT9L包装BOM（MF-0091）和总装类组件清单PT9L-ABOM01（MF-0092至MF-0094）均为PT9L正式DHF/DMR的受控BOM文件，文件标题和编号均明确归属PT9L。BOM中PT3来源的零件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01）以"来源型号"列标注PT3，这是医疗器械制造企业BOM中标注共用件原始开发型号的常规做法，表明这些零件最初为PT3型号开发但在PT9L中共用。同一BOM中同时存在PT9L、PT5、PT1、T-Z1等多个来源型号标注，进一步印证这是系统性的共用件管理方式。零件本身已通过料号（K/T开头编号）进行唯一标识和受控管理，不影响PT9L产品身份的完整性，予以dismiss。

### 42. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0098`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:460`
- 命中文本：功能描述 ｜ 血压计数据打包函数
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 43. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0099`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:477`
- 命中文本：\| sen_num= SENTENCE_SYSTOLIC，num=120 \| 血压计播报高压120mmHg \| 血压计播报高压120mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 44. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0100`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:478`
- 命中文本：\| sen_num= SENTENCE_DIASTOLIC，num=80 \| 血压计播报低压80mmHg \| 血压计播报高压80mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 45. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0101`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:313`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，0.5S内上位机回复ACK，用串口检测血压计发送数据 \| 串口发送加压过慢数据：<br>A0 07 00 7E A1 38 04 00 00 5B不重发 \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 46. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0102`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:314`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，上位机不回复ACK，用串口检测血压计发送数据并查看run_mode的值 \| 用串口侦测到的数据为<br>A0 07 00 7E A1 38 04 00 00 5B以0.5s重发三次<br>run_mode=MODE_erC \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 47. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0103`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:322`
- 命中文本：void Bpm_Cmd_Decete(void) ｜ Blood pressure cuff protocol parsing，血压计协议解析
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 48. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0104`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:406`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 49. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0105`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:408`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 50. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0106`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:412`
- 命中文本：4\. 按APP中“开始测量”，血压计进入测量态。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 51. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0107`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:444`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 52. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0108`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:448`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0023的primary_scope=false，文件为软件测试计划。所有命中均为描述PT9L血压计产品测试步骤和功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计进入测量态"、"血压计协议解析"等），"血压计"为产品品类通称，用于描述被测对象PT9L的功能特性，属于正常技术文档用语。无证据表明这些描述指向其他型号产品，不构成产品身份污染。

### 53. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0109`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:54`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 54. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0110`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:56`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 55. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0111`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:60`
- 命中文本：4\. **按 APP 中“开始测量”，血压计进入测量态。**
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 56. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0112`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:108`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 57. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0113`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:116`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 58. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0114`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:128`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击APP界面的暂停图标退出测量界面。退出后血压计不加压，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 59. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0115`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:130`
- 命中文本：2\. 点击“开始测量”正常开始测量，在血压计测量过程中点击APP界面的暂停图标退出测量界面。血压计立即关泵开阀，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 60. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0116`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:138`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击HOME键离开APP界面。退出后血压计不加压，再次打开APP，点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope=false，文件为软件系统测试记录。所有命中均为描述PT9L血压计产品操作步骤、功能行为的自然语言表述（如"将血压计袖带捆绑于胳膊"、"血压计停止测量"、"血压计数据打包函数"等），这些均是对PT9L产品功能的正常描述，"血压计"在此为产品品类通称而非异型号标识符。无证据表明这些描述指向其他型号产品，不影响PT9L的产品身份证据链。

### 61. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0117`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_template_sheet_name`
- 文件：`11 T1样机\软件文件底稿\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70`
- 命中文本：## Sheet: 模板修改记录
- 驳回理由：MF-0117所在文件路径为"11 T1样机\\软件文件底稿\\质量策划E0 23.11\\软件质量策划评审检查表E0 23.11.via_xlsx.clean.md"，cluster的primary_scope为false，表明该文件属于底稿/工作文件范围而非正式受控主文件。"## Sheet: 模板修改记录"为Excel Sheet名称，与MC-CLUSTER-0010完全相同的结构，属于文件内置变更记录区域标签。综合primary_scope=false及Sheet名称性质，予以dismiss。

### 62. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0118`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2`
- 命中文本：# BP3L 软件图样E0 23.11
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 63. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0119`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:48`
- 命中文本：![图片 4](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d805c950.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 64. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0120`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50`
- 命中文本：![图片 6](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_a0cd39dd.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 65. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0121`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:52`
- 命中文本：![Picture 3](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_20a262b4.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 66. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0122`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54`
- 命中文本：![图片 8](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_e11cac5c.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 67. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0123`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:56`
- 命中文本：![Picture 7](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_f49c074.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 68. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0124`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:58`
- 命中文本：![图片 10](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_ae5eec4.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 69. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0125`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_document_not_in_formal_dhf`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:60`
- 命中文本：![图片 11](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_2540465a.gif)
- 驳回理由：MC-CLUSTER-0025的8个候选（MF-0118至MF-0125）全部来自"11 T1样机\\软件文件底稿\\软件图样E0 23.11"目录，primary_scope=false，candidate_scope_counts显示primary=0、auxiliary=8，属于辅助/草稿范围而非正式DHF受控目录。软件文件底稿属于工作过程文件，不等同于正式受控的DHF文件。同一BP3L软件图样文件在正式DHF目录（Stage 07）中的产品身份标识问题已由MC-CLUSTER-0011 confirm覆盖。本cluster在辅助范围内的相同问题不构成独立的正式DHF错误，当前证据不能证明这是正式受控文件层面的实质错误，依据最终裁决政策应选择dismiss。

### 70. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0126`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:79`
- 命中文本：1\. “血压测量态”由“加压前处理”、“加压测量过程”、“发送测量数据”三个子模块组成。“加压前处理”主要进行加压前的浮零处理，为后续找到基准零点压力；“加压测量过程”为血压计充气过程，主要包含加压速度判断、压力平台判断、检波、抗干扰和计算过程；“发送测量数据”包括血压计在测量过程中向上位机发送压力、脉搏波等实时数据，以及在测量结束后向上位机发送血压、心跳等测量结果。
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 71. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0127`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:87`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 72. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0128`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:88`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 73. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0129`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:93`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 74. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0130`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:110`
- 命中文本：通讯方案采用《iHealth血压计通信协议V2.4》中如下命令字，具体指令格式参见《iHealth血压计通信协议V2.4》（GF-10-010 V2.4）。
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 75. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0131`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:127`
- 命中文本：\| 命令型 \| 0x32 \| 浮零完毕 \| 无 \| 无 \| 下位机回复ACK，单台血压计测量或多台血压计组成测量系统，但无需同时加压机型适用 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 76. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0132`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:128`
- 命中文本：\| 实时数据型 \| 0x30 \| 浮零中 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK ，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据浮零指令中的数据信息确定是否发送启动加压指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 77. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0133`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`functional_term_false_positive`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:130`
- 命中文本：\| 实时数据型 \| 0x3C/<br>0x3D \| 蓝牙接口测量过程数据 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据测量数据指令中的数据信息确定是否发送测量完毕指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope=false，文件为软件方案设计。所有命中均为描述PT9L血压计产品软件功能规格、设计规格和通信方案的自然语言表述（如"血压计上电后初始化"、"血压计自动关机"、"血压计通信协议"等），"血压计"为产品品类通称，用于描述PT9L产品的软件功能特性，属于正常技术文档用语。引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属于合理技术引用。无证据表明这些描述指向其他具体型号产品，不构成产品身份污染。

### 78. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0134`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_generic_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:107`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：所有命中证据均位于Stage 11 T1样机软件需求规格书（E0版本底稿）中，文件描述的是PT9L血压计产品自身的初始化、关机、加压、测量、错误显示等功能，'血压计'为该产品的品类通用名称而非异型号标识符。文件路径明确属于PT9L开发阶段文件，primary_scope=false仅表示该stage非主审范围，但内容本身不存在异型号混入。判定为误报，予以驳回。

### 79. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0135`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_generic_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:108`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：所有命中证据均位于Stage 11 T1样机软件需求规格书（E0版本底稿）中，文件描述的是PT9L血压计产品自身的初始化、关机、加压、测量、错误显示等功能，'血压计'为该产品的品类通用名称而非异型号标识符。文件路径明确属于PT9L开发阶段文件，primary_scope=false仅表示该stage非主审范围，但内容本身不存在异型号混入。判定为误报，予以驳回。

### 80. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0136`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_generic_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:113`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：所有命中证据均位于Stage 11 T1样机软件需求规格书（E0版本底稿）中，文件描述的是PT9L血压计产品自身的初始化、关机、加压、测量、错误显示等功能，'血压计'为该产品的品类通用名称而非异型号标识符。文件路径明确属于PT9L开发阶段文件，primary_scope=false仅表示该stage非主审范围，但内容本身不存在异型号混入。判定为误报，予以驳回。

### 81. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0137`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`reasonable_product_reference`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:127`
- 命中文本：\| 3 \| 《PT9L设计输入-性能规格部分（三）IEC/EN 80601-2-30 》<br>(PT9L-SRXN01 V1.0) \| 201.7.2.<br>101 \| 自动血压计的显示 \|
- 驳回理由：证据来源为Stage 11软件需求规格文件，文件编号引用PT9L-SRXN01 V1.0，内容为PT9L自动血压计的显示、测量范围等功能需求条款，"血压计"系对PT9L产品类型的正常描述，属于IEC/EN 80601-2-30标准条款的合理引用。primary_scope虽为false，但内容本身不存在型号混用或合规缺陷，予以dismiss。

### 82. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0138`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_generic_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:151`
- 命中文本：上电后系统进入关机态（低功耗状态），不开机并且不充电时灯不亮。在关机态，与手机蓝牙进行连接并建立通信后，绿灯常亮，启动iHealth APP点击开始测量键开始测量，测量过程中血压计将得到的压力及心跳信息传输至手机；测量完毕后，手机显示高压、低压、心率、血压分类、心律不齐（如果有）；测量过程中若出现异常，手机会显示相应提示信息。当电池电量不足时，手机会显示电量不足提示并且血压计上的红色LED灯闪烁。
- 驳回理由：所有命中证据均位于Stage 11 T1样机软件需求规格书（E0版本底稿）中，文件描述的是PT9L血压计产品自身的初始化、关机、加压、测量、错误显示等功能，'血压计'为该产品的品类通用名称而非异型号标识符。文件路径明确属于PT9L开发阶段文件，primary_scope=false仅表示该stage非主审范围，但内容本身不存在异型号混入。判定为误报，予以驳回。

### 83. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0139`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`benign_product_generic_name_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:172`
- 命中文本：□ 自动关机时间：血压计与手机蓝牙断开连接后，血压计自动关机
- 驳回理由：所有命中证据均位于Stage 11 T1样机软件需求规格书（E0版本底稿）中，文件描述的是PT9L血压计产品自身的初始化、关机、加压、测量、错误显示等功能，'血压计'为该产品的品类通用名称而非异型号标识符。文件路径明确属于PT9L开发阶段文件，primary_scope=false仅表示该stage非主审范围，但内容本身不存在异型号混入。判定为误报，予以驳回。

### 84. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0140`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`draft_template_marker`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:226`
- 命中文本：第 0 页 / 共 5 页 模板版本： I
- 驳回理由：文件路径为"11 T1样机\\软件文件底稿\\软件需求E0 23.11"，明确标注为底稿（草稿阶段），primary_scope=false。"第 0 页 / 共 5 页 模板版本：I"是文档模板的页脚标记，属于草稿编制过程中的正常模板痕迹，不影响PT9L正式DHF证据链，予以dismiss。

### 85. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0141`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`cross_model_transport_evaluation_reference`
- 文件：`11 T1样机\运输\运输试验评估报告2020-3-27.via_lo_html.clean.md:37`
- 命中文本：\| **评 估 结 论** \| 根据“ PT3 运输试验报告”评估：<br>对比结果说明： 两机型相比较，彩包装、外箱材质、开合方式、连接方式均相同、两机型相比较彩包装、外箱尺寸、重量、材质均相似，故评估该包装对本产品在运输过程中整机的安全和性能无影响，评估合格。<br>☑ **合格** □ **不合格** *说明：*<br>□ **包装形式不同项差别较大，不能评估运输过程对整机安全和性能 的 影响，需进行运输试验** \|  \|
- 驳回理由：MF-0060至MF-0062所在文件《09a-10 PT3 transport report》虽文件名含PT3，但文件正文第12行明确标注"Model name: PT9L"，文件编号为PT9L-YSBG01 V1.0，表明该运输报告本身即为PT9L的正式运输试验报告，文件名中"PT3"可能为试验序号或内部编号（"09a-10 PT3"中PT3疑为"Package Test 3"或试验编号），不代表产品型号PT3。MF-0141《运输试验评估报告》中明确引用"PT3运输试验报告"作为评估基准，并对两机型包装进行了逐项对比，结论为评估合格，属于正式的同类机型评估引用，符合医疗器械DHF中利用相似产品数据进行等效评估的常规做法。整体不构成产品身份污染，予以dismiss。但建议确认MF-0141评估报告中被评估产品型号是否明确标注为PT9L，以及签字批准栏是否完整。

### 86. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0152`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_component_reference_unverified`
- 文件：`12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:19`
- 命中文本：\| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|
- 驳回理由：MF-0152、MF-0197、MF-0198、MF-0199均位于Stage 12 primary_scope=true的PT9L包装BOM及总装类组件清单中，零件图号归属标注为PT3（PT3-F21防拆签、PT3-P10双联弹簧、PT3-M02金属套、PT3-M01压块）。但观察同一BOM文件，其中同样存在PT5-M03、PT5-M02、T-Z1-P10、T-Z1-P12等多个其他型号前缀的共用件引用，说明该BOM的编制惯例是直接保留零件原始型号归属编号，属于多型号平台共用件的常规引用方式。同时same_term_file_samples中显示Stage 12设计输出清单二目录下存在PT3零件对应图纸文件（如PT3_双联弹簧_REV01.pdf、T040800073941030093-PT3-F21.pdf），说明这些零件的设计输出图纸已纳入PT9L DHF设计输出清单二，具备受控依据。当前证据不能证明存在缺少共用件受控说明的正式文件受控缺陷，属于共用件/历史来源合理引用，不构成产品身份污染。

### 87. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0170`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`supplier_template_reference_description`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:10`
- 命中文本：## 0. 标题栏（A 级，外购件 Famidoc 模板）
- 驳回理由：MF-0170中"标题栏（A 级，外购件 Famidoc 模板）"是对图纸标题栏类型的分类描述；MF-0171中"Famidoc 供应商标准 A4 横向模板"是对图框规格的技术说明，均属于读图报告对图纸属性的合理描述性标注。该图纸（散热器压块）已有完整的零件名称、审批日期（2017-07-14）、公差等级等实质内容，"模板"一词在此语境下指供应商图框标准，非空白占位符，不影响设计输出的完整性，予以dismiss。

### 88. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0171`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`supplier_template_reference_description`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:26`
- 命中文本：\| **图框** \| Famidoc 供应商标准 A4 横向模板 \|
- 驳回理由：MF-0170中"标题栏（A 级，外购件 Famidoc 模板）"是对图纸标题栏类型的分类描述；MF-0171中"Famidoc 供应商标准 A4 横向模板"是对图框规格的技术说明，均属于读图报告对图纸属性的合理描述性标注。该图纸（散热器压块）已有完整的零件名称、审批日期（2017-07-14）、公差等级等实质内容，"模板"一词在此语境下指供应商图框标准，非空白占位符，不影响设计输出的完整性，予以dismiss。

### 89. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0197`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_component_reference_unverified`
- 文件：`12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28`
- 命中文本：\| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|
- 驳回理由：MF-0152、MF-0197、MF-0198、MF-0199均位于Stage 12 primary_scope=true的PT9L包装BOM及总装类组件清单中，零件图号归属标注为PT3（PT3-F21防拆签、PT3-P10双联弹簧、PT3-M02金属套、PT3-M01压块）。但观察同一BOM文件，其中同样存在PT5-M03、PT5-M02、T-Z1-P10、T-Z1-P12等多个其他型号前缀的共用件引用，说明该BOM的编制惯例是直接保留零件原始型号归属编号，属于多型号平台共用件的常规引用方式。同时same_term_file_samples中显示Stage 12设计输出清单二目录下存在PT3零件对应图纸文件（如PT3_双联弹簧_REV01.pdf、T040800073941030093-PT3-F21.pdf），说明这些零件的设计输出图纸已纳入PT9L DHF设计输出清单二，具备受控依据。当前证据不能证明存在缺少共用件受控说明的正式文件受控缺陷，属于共用件/历史来源合理引用，不构成产品身份污染。

### 90. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0198`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_component_reference_unverified`
- 文件：`12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35`
- 命中文本：\| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：MF-0152、MF-0197、MF-0198、MF-0199均位于Stage 12 primary_scope=true的PT9L包装BOM及总装类组件清单中，零件图号归属标注为PT3（PT3-F21防拆签、PT3-P10双联弹簧、PT3-M02金属套、PT3-M01压块）。但观察同一BOM文件，其中同样存在PT5-M03、PT5-M02、T-Z1-P10、T-Z1-P12等多个其他型号前缀的共用件引用，说明该BOM的编制惯例是直接保留零件原始型号归属编号，属于多型号平台共用件的常规引用方式。同时same_term_file_samples中显示Stage 12设计输出清单二目录下存在PT3零件对应图纸文件（如PT3_双联弹簧_REV01.pdf、T040800073941030093-PT3-F21.pdf），说明这些零件的设计输出图纸已纳入PT9L DHF设计输出清单二，具备受控依据。当前证据不能证明存在缺少共用件受控说明的正式文件受控缺陷，属于共用件/历史来源合理引用，不构成产品身份污染。

### 91. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0199`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`cross_model_component_reference_unverified`
- 文件：`12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36`
- 命中文本：\| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：MF-0152、MF-0197、MF-0198、MF-0199均位于Stage 12 primary_scope=true的PT9L包装BOM及总装类组件清单中，零件图号归属标注为PT3（PT3-F21防拆签、PT3-P10双联弹簧、PT3-M02金属套、PT3-M01压块）。但观察同一BOM文件，其中同样存在PT5-M03、PT5-M02、T-Z1-P10、T-Z1-P12等多个其他型号前缀的共用件引用，说明该BOM的编制惯例是直接保留零件原始型号归属编号，属于多型号平台共用件的常规引用方式。同时same_term_file_samples中显示Stage 12设计输出清单二目录下存在PT3零件对应图纸文件（如PT3_双联弹簧_REV01.pdf、T040800073941030093-PT3-F21.pdf），说明这些零件的设计输出图纸已纳入PT9L DHF设计输出清单二，具备受控依据。当前证据不能证明存在缺少共用件受控说明的正式文件受控缺陷，属于共用件/历史来源合理引用，不构成产品身份污染。

### 92. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0200`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_drawing_template_annotation`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\上盖20210727.pdf.md:38`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：文件路径为"12 设计输出（含01、02）\\设计输出清单二\\早期图纸"，primary_scope=false，属于历史早期图纸归档范围。"技术要求（4条标准ABS模板）"是对图纸技术要求章节内容类型的描述性标注，表明该技术要求采用标准ABS材料模板条款，并非空白占位符。早期图纸不在PT9L正式DHF主审范围内，予以dismiss。

### 93. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0201`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_drawing_template_annotation`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\探头20210727.pdf.md:25`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：文件路径为"12 设计输出（含01、02）\\设计输出清单二\\早期图纸"，primary_scope=false，属于历史早期图纸归档范围。"技术要求（4条标准ABS模板）"是对图纸技术要求章节内容类型的描述性标注，表明该技术要求采用标准ABS材料模板条款，并非空白占位符。早期图纸不在PT9L正式DHF主审范围内，予以dismiss。

### 94. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0211`
- Agent：Document Control Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`reference_sheet_historical_content`
- 文件：`12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:237`
- 命中文本：产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
- 驳回理由：Sheet名明确标注为"PT3参考"，文件编制者已通过命名方式将该Sheet定性为参考/历史对比用途，而非PT9L正式设计输出受控Sheet。同文件其他上下文显示PT3SBT相关物料编号（PT3SBT-P01、PT3SBT-P02、PT3SBT-ABOM01、PT3SBT-PBOM01等）在正式Sheet中亦有合理引用，说明PT3SBT作为关联历史型号在DHF中存在合理的参考背景。签署日期空白及产品型号为PT3SBT均与"参考Sheet"的定位一致，属于历史/参考来源说明情形。当前证据不能证明该Sheet被纳入PT9L正式受控设计输出内容，不构成可确认的文件受控质量错误，依据裁决政策应选择dismiss。

### 95. 发现疑似旧型号/异类品类/模板残留：PT3SBT

- 原始候选 ID：`MF-0226`
- Agent：Document Control Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`reference_sheet_historical_content`
- 文件：`12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239`
- 命中文本：产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
- 驳回理由：Sheet名明确标注为"PT3参考"，文件编制者已通过命名方式将该Sheet定性为参考/历史对比用途，而非PT9L正式设计输出受控Sheet。同文件其他上下文显示PT3SBT相关物料编号（PT3SBT-P01、PT3SBT-P02、PT3SBT-ABOM01、PT3SBT-PBOM01等）在正式Sheet中亦有合理引用，说明PT3SBT作为关联历史型号在DHF中存在合理的参考背景。签署日期空白及产品型号为PT3SBT均与"参考Sheet"的定位一致，属于历史/参考来源说明情形。当前证据不能证明该Sheet被纳入PT9L正式受控设计输出内容，不构成可确认的文件受控质量错误，依据裁决政策应选择dismiss。

### 96. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0239`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:31`
- 命中文本：\| 型号 \| PT9L \| PT3 \|
- 驳回理由：所有候选证据（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，明确位于废案与备份目录。文件内容为临床评价报告，PT3作为同品种医疗器械（同一公司已注册产品）被用于等效性对比，属于临床评价方法论中的合理引用，不代表PT9L正式DHF将PT3混入产品身份。废案目录文件不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 97. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0240`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_废案_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:36`
- 命中文本：\| 符合注册要求的使用说明书 \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT9L） \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT3） \|
- 驳回理由：文件路径明确为"18 设计确认\\废案与备份"，属于废案/备份文件范围。文件内容将PT3作为PT9L的同品种医疗器械进行临床对比评价，系临床评价报告的标准写法，PT3作为已上市同品种产品被引用具有合理性。该文件不在正式受控DHF/DMR主文件范围内，不影响PT9L正式证据链。

### 98. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0241`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:46`
- 命中文本：PT9L红外体温计和PT3红外体温计均为有源器械。其等效性比较参见表3-1。
- 驳回理由：所有候选证据（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，明确位于废案与备份目录。文件内容为临床评价报告，PT3作为同品种医疗器械（同一公司已注册产品）被用于等效性对比，属于临床评价方法论中的合理引用，不代表PT9L正式DHF将PT3混入产品身份。废案目录文件不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 99. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0242`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:83`
- 命中文本：\| PT3 \| ![图片 5](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_25bd38c1.png) \| PT9L \| ![图片 38](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_c235e89e.png) \|
- 驳回理由：所有候选证据（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，明确位于废案与备份目录。文件内容为临床评价报告，PT3作为同品种医疗器械（同一公司已注册产品）被用于等效性对比，属于临床评价方法论中的合理引用，不代表PT9L正式DHF将PT3混入产品身份。废案目录文件不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 100. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0243`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:93`
- 命中文本：数据来源为柯顿（天津）电子医疗器械有限公司PT3红外体温计于2013年取得由中国人民解放军第 100医院及苏州市立医院本部医院所进行的临床试验报告所得，试验主要进行的是临床验证。
- 驳回理由：所有候选证据（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，明确位于废案与备份目录。文件内容为临床评价报告，PT3作为同品种医疗器械（同一公司已注册产品）被用于等效性对比，属于临床评价方法论中的合理引用，不代表PT9L正式DHF将PT3混入产品身份。废案目录文件不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 101. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0244`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:97`
- 命中文本：产品的临床试验由护理人员负责实施，采取自身对照试验方法，采用TH30F非接触红外额式体温与经过校准的水银玻璃体温计同步测定的方法，验证非接触红外额式体温计的准确度。
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 102. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0245`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:107`
- 命中文本：具体参加附件：TH30F临床研究方案及临床试验报告见附3。
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 103. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0246`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:111`
- 命中文本：同品种医疗器械TH30F未收到投诉，未发现不良事件。
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 104. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0247`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_废案_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:115`
- 命中文本：同品种医疗器械TH30F未采取过与临床风险相关的纠正措施。
- 驳回理由：文件路径明确为"18 设计确认\\废案与备份"，属于废案/备份文件范围。TH30F在临床评价报告中作为PT9L的同品种医疗器械被引用，用于说明不良事件、纠正措施及临床数据，系临床评价的合规写法。该文件不在正式受控DHF/DMR主文件范围内，不构成合规缺陷。

### 105. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0248`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 106. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0249`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 107. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0250`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 108. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0251`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 109. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0252`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:190`
- 命中文本：（七）PT3红外体温计准确度验证报告
- 驳回理由：所有候选证据（MF-0239、MF-0241、MF-0242、MF-0243、MF-0252）均来自路径'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，明确位于废案与备份目录。文件内容为临床评价报告，PT3作为同品种医疗器械（同一公司已注册产品）被用于等效性对比，属于临床评价方法论中的合理引用，不代表PT9L正式DHF将PT3混入产品身份。废案目录文件不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 110. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0253`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_废案_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:196`
- 命中文本：PT3和TH30F为同品种医疗器械，综合上述数据集的分析结果，PT9L在正常使用条件下，产品可达到预期性能；与预期受益相比较，产品的风险可接受。
- 驳回理由：文件路径明确为"18 设计确认\\废案与备份"，属于废案/备份文件范围。TH30F在临床评价报告中作为PT9L的同品种医疗器械被引用，用于说明不良事件、纠正措施及临床数据，系临床评价的合规写法。该文件不在正式受控DHF/DMR主文件范围内，不构成合规缺陷。

### 111. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0254`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:12`
- 命中文本：型号规格：PT9CL
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 112. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0255`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:34`
- 命中文本：我公司天津九安医疗电子股份有限公司研制开发的PT9C型红外体温计是一款通过接收人体额头部位散发的红外能量，来测量人体温度的红外体温计。
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 113. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0256`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 114. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0257`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 115. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0258`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 116. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0259`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：所有候选证据（MF-0254至MF-0259）均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名已标注'中国版本不适用'。文件内容为PT9C型红外体温计的临床评价报告，PT9C作为申报产品出现，PT3作为同品种对比产品。该文件属于历史/废案文件，已被明确标注为不适用版本，归入废案与备份目录，不属于PT9L正式DHF/DMR受控文件范围，不影响PT9L证据链。

### 117. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0260`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 118. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0261`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 119. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0262`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

### 120. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0263`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_reference_in_废案_directory`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有候选证据均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在文件中作为临床验证的对照品（非接触红外额式体温计）或与PT3进行性能比对的参照型号，属于临床评价数据来源的合理说明，不代表TH30F被纳入PT9L产品身份。废案目录文件不属于PT9L正式DHF/DMR受控范围，不影响PT9L证据链完整性。

> 仅展示前 120 条，完整数据见 `13_mechanical_agent_review/mechanical_dismissed_candidates.jsonl`。