# PT9L 机械候选复审驳回/非错误清单

> 生成时间：2026-07-01T16:12:34
> 范围：mechanical_review_node 经一轮或二轮 LLM 复审后判定为 dismiss 的机械候选。dismiss 表示当前证据下不构成可确认错误，不等于人工最终裁决。

## 1. 摘要

- 驳回/非错误候选数：348

## 2. 按 Agent 统计

| Agent | 数量 |
|---|---:|
| Product Identity Agent | 158 |
| Document Control Agent | 85 |
| Regulatory Agent | 74 |
| Hardware Agent | 31 |

## 3. 样例清单

### 1. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0002`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:2`
- 命中文本：# V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号均为PT2L型号（PT2L美亚-FXJH01 V1.0），且文件内容（line 6）显示DN字段虽提及PT9L-FXJH01 V1.0，但整体文件为PT2L历史风险管理计划。该文件属于前代型号的历史归档文件，primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 2. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0003`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html.clean.md:117`
- 命中文本：![形状2](V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0.via_lo_html_assets/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0_html_f9d9f2af.gif) Acceptable Control as much as possible Not acceptable
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号均为PT2L型号（PT2L美亚-FXJH01 V1.0），且文件内容（line 6）显示DN字段虽提及PT9L-FXJH01 V1.0，但整体文件为PT2L历史风险管理计划。该文件属于前代型号的历史归档文件，primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 3. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0004`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:6`
- 命中文本：D N : PT2L( 美亚 ) - SGFP 01 V1.0 Risk Assessment Report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 4. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0005`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 5. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0006`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:81`
- 命中文本：When the PT2L infrared thermometer project was launched, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 6. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0007`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:83`
- 命中文本：Currently, the PT2L infrared thermometer is in the feasibility review stage of design changes. The purpose of this risk management review is to determine whether the design changes of the PT2L infrared thermometer will g
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 7. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0008`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:107`
- 命中文本：Please find the document *Risk Management P* *lan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 8. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0009`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-2 Risk Assessment Report .via_lo_html.clean.md:124`
- 命中文本：\| **A.2.1** \| What is the intended use and how is the medical device to be used?<br>□ what is the medical device’s role relative to:<br>□ what are the indications for use (e.g. patient population, user profile, use env
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题、文档编号（PT2L(美亚)-SGFP01 V1.0）及产品型号字段（Product model: PT2L）均指向PT2L型号。文件内容描述的是PT2L设计变更阶段的风险评估活动，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 9. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0010`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:6`
- 命中文本：D N: PT2L( 美亚 ) - SGYS 01 V 1 .0 Verification of risk control measure and residual risk evaluation report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 10. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0011`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 11. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0012`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:95`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 12. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0013`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:198`
- 命中文本：型式试验报告：PT2L(美亚)-XNTB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 13. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0014`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:202`
- 命中文本：说明书：PT2L(美亚)-SMSY02 V2.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 14. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0015`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:204`
- 命中文本：易用性报告：PT2L(美亚)-UETR01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 15. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0016`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:206`
- 命中文本：临床评估报告：PT2L(美亚)-RLPB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 16. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0017`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-3 Verification of risk control measure and residual risk evaluation report .via_lo_html.clean.md:208`
- 命中文本：软件确认报告：PT2L(美亚)-RJQB01 V1.0
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L(美亚)-SGYS01 V1.0）均指向PT2L型号，产品型号字段亦为PT2L。文件中引用的各类支持文件（型式试验报告、说明书、易用性报告、临床评估报告、软件确认报告等）均以PT2L(美亚)为前缀，属于PT2L历史设计变更的配套文件。primary_scope=false，不在PT9L正式主审范围内，不构成合规证据缺陷。

### 17. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0018`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:6`
- 命中文本：DN ： PT2L-FXGB01 V 4 .0 Risk Management Report
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 18. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0019`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:14`
- 命中文本：Product model： PT2L
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 19. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0020`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:60`
- 命中文本：PT2L replaced the MCU with a smaller memory in hardware to ensure that the new MCU has sufficient performance and functions while meeting cost requirements. Re-evaluated the structural design in structure to find parts t
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 20. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0021`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:64`
- 命中文本：At the same time as the PT2L infrared thermometer project was established, we planned risk management activities for the product and formulated a risk management plan.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 21. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0022`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:66`
- 命中文本：The risk management plan determined the risk acceptance criteria for the PT2L infrared thermometer and arranged the review of the product's risk management activities.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 22. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0023`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:70`
- 命中文本：In the early development and prototype stages of the PT2L infrared thermometer, the risk management team conducted a risk management review and formed relevant risk management documents.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 23. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0024`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:72`
- 命中文本：While the PT2L infrared thermometer was undergoing design changes, the company formed a risk management team to ensure that the risk management activities for the design changes of the project were effectively implemente
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 24. 发现疑似旧型号/异类品类/模板残留：PT2L

- 原始候选 ID：`MF-0025`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_document_out_of_scope`
- 文件：`03 风险分析\2L风险改 - 历史文件\V1.0-4 Risk Management Report .via_lo_html.clean.md:96`
- 命中文本：Please find the document *Risk Management Plan* (PT2L-FXJH01 V1.0) for the risk acceptance criteria.
- 驳回理由：文件路径明确包含"2L风险改 - 历史文件"目录，文件标题及文档编号（PT2L-FXGB01 V4.0）均指向PT2L型号，产品型号字段为PT2L。文件内容详细描述了PT2L设计变更（MCU替换、结构优化、软件适配）的风险管理全过程，与PT9L无直接关联。primary_scope=false，属于历史归档文件，不构成PT9L合规证据缺陷。

### 25. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0040`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_structural_label_not_content_gap`
- 文件：`07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70`
- 命中文本：## Sheet: 模板修改记录
- 驳回理由：MF-0040所在文件为软件质量策划评审检查表，"## Sheet: 模板修改记录"是Excel转换后对Sheet名称的忠实还原，属于文件格式的组成部分。该Sheet本身用于记录模板历史变更，其存在本身不构成"待填"或"未受控"问题。若修改记录行为空，属于无变更历史的正常状态，不影响正式文件受控质量。

### 26. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0054`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:20`
- 命中文本：\|  \| 彩包装 \| 包装血压计 \| 标识不清楚 内容不全面 \| 用户误用 \| 9 \| A \| 说明书印刷油墨质量不好 未完全符合法规要求 \| 4 \|  \| 目测检查 法规符合性检查 \| 5 \| 180 \| 标识内容及可识别度检验 \| 9 \| 4 \| 1 \| 36 \| 检查检验记录 \|  \|  \| □ \|
- 驳回理由：该cluster所有候选均来自Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被分析产品的功能描述词出现，涵盖彩包装标识、铭牌、说明书等组件的失效模式分析，内容完整且包含法规符合性检查措施（目测检查、法规符合性检查）。这是PT9L DHF中正常的设计失效模式分析，"血压计"为产品类别描述而非旧型号引用，不构成合规证据缺陷。

### 27. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0056`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:22`
- 命中文本：\|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌印刷内容容易被擦拭掉 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌未覆膜 \| 2 \|  \| 依IEC60601-1:2005 电气安全通用要求中7.1.3 标记耐久性要求 对铭牌进行试验 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：该cluster所有候选均来自Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被分析产品的功能描述词出现，涵盖彩包装标识、铭牌、说明书等组件的失效模式分析，内容完整且包含法规符合性检查措施（目测检查、法规符合性检查）。这是PT9L DHF中正常的设计失效模式分析，"血压计"为产品类别描述而非旧型号引用，不构成合规证据缺陷。

### 28. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0058`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:24`
- 命中文本：\|  \| 说明书 \| 给用户关于机器使用的信息 \| 说明书印刷不够清楚 \| 用户无法识别血压计使用的相关信息 \| 4 \| C \| 说明书印刷油墨质量不好 \| 2 \|  \| 实际使用 \| 1 \| 8 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：该cluster所有候选均来自Stage 11正式DFMEA文件（结构类FMEA E0），文件中"血压计"作为被分析产品的功能描述词出现，涵盖彩包装标识、铭牌、说明书等组件的失效模式分析，内容完整且包含法规符合性检查措施（目测检查、法规符合性检查）。这是PT9L DHF中正常的设计失效模式分析，"血压计"为产品类别描述而非旧型号引用，不构成合规证据缺陷。

### 29. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0060`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_to_predecessor_model`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:2`
- 命中文本：# 09a-10 PT3 transport report
- 驳回理由：MF-0060文件名虽含"PT3 transport report"，但MF-0061第12行明确标注"Model name: PT9L"，文件受控编号为"PT9L-YSBG01 V1.0"，说明该运输报告的受控主体为PT9L。MF-0141为运输试验评估报告，明确说明"根据PT3运输试验报告评估"，通过对比PT3与PT9L的包装参数（彩包装、外箱材质、尺寸、重量等）进行相似性评估，结论为"评估合格"。这是医疗器械DHF中常见的参比机型评估方法，PT3作为已有机型被合理引用作为评估依据，不构成产品身份污染。文件名中"PT3"为历史来源标注，不影响PT9L正式DHF证据链。

### 30. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0061`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_to_predecessor_model`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:14`
- 命中文本：**1 ![直线 2](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_75410098.gif) . Test purposes**
- 驳回理由：MF-0060文件名虽含"PT3 transport report"，但MF-0061第12行明确标注"Model name: PT9L"，文件受控编号为"PT9L-YSBG01 V1.0"，说明该运输报告的受控主体为PT9L。MF-0141为运输试验评估报告，明确说明"根据PT3运输试验报告评估"，通过对比PT3与PT9L的包装参数（彩包装、外箱材质、尺寸、重量等）进行相似性评估，结论为"评估合格"。这是医疗器械DHF中常见的参比机型评估方法，PT3作为已有机型被合理引用作为评估依据，不构成产品身份污染。文件名中"PT3"为历史来源标注，不影响PT9L正式DHF证据链。

### 31. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0062`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_to_predecessor_model`
- 文件：`11 T1样机\09a-10 PT3 transport report.via_lo_html.clean.md:46`
- 命中文本：\| Corner \| 970 mm \| 1 box \| ![图片 1](09a-10 PT3 transport report.via_lo_html_assets/09a-10 PT3 transport report_html_9a00f4a6.png) \|
- 驳回理由：MF-0060文件名虽含"PT3 transport report"，但MF-0061第12行明确标注"Model name: PT9L"，文件受控编号为"PT9L-YSBG01 V1.0"，说明该运输报告的受控主体为PT9L。MF-0141为运输试验评估报告，明确说明"根据PT3运输试验报告评估"，通过对比PT3与PT9L的包装参数（彩包装、外箱材质、尺寸、重量等）进行相似性评估，结论为"评估合格"。这是医疗器械DHF中常见的参比机型评估方法，PT3作为已有机型被合理引用作为评估依据，不构成产品身份污染。文件名中"PT3"为历史来源标注，不影响PT9L正式DHF证据链。

### 32. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0091`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_shared_component_reference`
- 文件：`11 T1样机\PT9L包装BOM.via_xlsx.clean.md:19`
- 命中文本：\| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|
- 驳回理由：MF-0091至MF-0094均来自PT9L正式BOM文件（PT9L包装BOM及总装类组件清单PT9L-ABOM01 V1.0），文件标题明确为PT9L受控文件。BOM中PT3-F21（防拆签）、PT3-P10（双联弹簧）、PT3-M02（金属套）、PT3-M01（压块）等零件的"来源型号"列标注为PT3，这是BOM中标准的共用件/沿用件来源追溯标注方式，表明这些零件最初为PT3机型设计但在PT9L中共用。同一BOM中还存在PT5、T-Z1、PT1等其他来源型号的共用件，进一步证实这是系统性的共用件管理做法。此类标注不影响PT9L产品身份，属于合理的物料来源引用。

### 33. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0092`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_shared_component_reference`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28`
- 命中文本：\| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|
- 驳回理由：MF-0091至MF-0094均来自PT9L正式BOM文件（PT9L包装BOM及总装类组件清单PT9L-ABOM01 V1.0），文件标题明确为PT9L受控文件。BOM中PT3-F21（防拆签）、PT3-P10（双联弹簧）、PT3-M02（金属套）、PT3-M01（压块）等零件的"来源型号"列标注为PT3，这是BOM中标准的共用件/沿用件来源追溯标注方式，表明这些零件最初为PT3机型设计但在PT9L中共用。同一BOM中还存在PT5、T-Z1、PT1等其他来源型号的共用件，进一步证实这是系统性的共用件管理做法。此类标注不影响PT9L产品身份，属于合理的物料来源引用。

### 34. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0093`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_shared_component_reference`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35`
- 命中文本：\| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：MF-0091至MF-0094均来自PT9L正式BOM文件（PT9L包装BOM及总装类组件清单PT9L-ABOM01 V1.0），文件标题明确为PT9L受控文件。BOM中PT3-F21（防拆签）、PT3-P10（双联弹簧）、PT3-M02（金属套）、PT3-M01（压块）等零件的"来源型号"列标注为PT3，这是BOM中标准的共用件/沿用件来源追溯标注方式，表明这些零件最初为PT3机型设计但在PT9L中共用。同一BOM中还存在PT5、T-Z1、PT1等其他来源型号的共用件，进一步证实这是系统性的共用件管理做法。此类标注不影响PT9L产品身份，属于合理的物料来源引用。

### 35. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0094`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_shared_component_reference`
- 文件：`11 T1样机\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36`
- 命中文本：\| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|
- 驳回理由：MF-0091至MF-0094均来自PT9L正式BOM文件（PT9L包装BOM及总装类组件清单PT9L-ABOM01 V1.0），文件标题明确为PT9L受控文件。BOM中PT3-F21（防拆签）、PT3-P10（双联弹簧）、PT3-M02（金属套）、PT3-M01（压块）等零件的"来源型号"列标注为PT3，这是BOM中标准的共用件/沿用件来源追溯标注方式，表明这些零件最初为PT3机型设计但在PT9L中共用。同一BOM中还存在PT5、T-Z1、PT1等其他来源型号的共用件，进一步证实这是系统性的共用件管理做法。此类标注不影响PT9L产品身份，属于合理的物料来源引用。

### 36. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0098`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:460`
- 命中文本：功能描述 ｜ 血压计数据打包函数
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 37. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0099`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:477`
- 命中文本：\| sen_num= SENTENCE_SYSTOLIC，num=120 \| 血压计播报高压120mmHg \| 血压计播报高压120mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 38. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0100`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:478`
- 命中文本：\| sen_num= SENTENCE_DIASTOLIC，num=80 \| 血压计播报低压80mmHg \| 血压计播报高压80mmHg \| OK \|
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 39. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0101`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:313`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，0.5S内上位机回复ACK，用串口检测血压计发送数据 \| 串口发送加压过慢数据：<br>A0 07 00 7E A1 38 04 00 00 5B不重发 \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 40. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0102`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:314`
- 命中文本：\| 发送加压过慢错误提示数据时等待ACK，上位机不回复ACK，用串口检测血压计发送数据并查看run_mode的值 \| 用串口侦测到的数据为<br>A0 07 00 7E A1 38 04 00 00 5B以0.5s重发三次<br>run_mode=MODE_erC \|  \|  \|
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 41. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0103`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:322`
- 命中文本：void Bpm_Cmd_Decete(void) ｜ Blood pressure cuff protocol parsing，血压计协议解析
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 42. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0104`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:406`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 43. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0105`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:408`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 44. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0106`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:412`
- 命中文本：4\. 按APP中“开始测量”，血压计进入测量态。
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 45. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0107`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:444`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 46. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0108`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件测试计划E0 23.11.via_lo_html.clean.md:448`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0023的primary_scope为false，所有候选均来自软件测试计划文件。文件中"血压计袖带"、"血压计进入测量态"、"血压计协议解析"、"血压计停止测量"等均为对PT9L产品功能的正常描述，PT9L本身即属血压计品类，此类用词属合理的产品类别引用，不涉及异型号身份混淆，不构成产品身份污染。

### 47. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0109`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:54`
- 命中文本：1\. 将血压计袖带捆绑于胳膊。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 48. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0110`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:56`
- 命中文本：2\. 开启手机APP，将手机与血压计通过蓝牙建立连接，认证通过后，绿色指示灯点亮。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 49. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0111`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:60`
- 命中文本：4\. **按 APP 中“开始测量”，血压计进入测量态。**
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 50. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0112`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:108`
- 命中文本：4\. 在加压过程中点击APP中暂停图标，血压计停止测量；加压过程中关闭APP，血压计停止测量；加压过程中关闭IOS设备蓝牙，血压计停止测量，绿灯熄灭。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 51. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0113`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:116`
- 命中文本：a . 血压测量完毕后，血压计停泵放气，此时屏幕显示此次的测量结果。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 52. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0114`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:128`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击APP界面的暂停图标退出测量界面。退出后血压计不加压，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 53. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0115`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:130`
- 命中文本：2\. 点击“开始测量”正常开始测量，在血压计测量过程中点击APP界面的暂停图标退出测量界面。血压计立即关泵开阀，再次点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 54. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0116`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:138`
- 命中文本：1\. 点击“开始测量”同时挤压袖带，在血压计浮零过程中点击HOME键离开APP界面。退出后血压计不加压，再次打开APP，点击“开始测量”后正常进行测量。
- 驳回理由：MC-CLUSTER-0022的primary_scope为false，所有候选均来自软件测试记录文件。PT9L本身即为血压计类产品，文件中"血压计袖带"、"血压计停止测量"、"血压计数据打包函数"等表述均为对被测产品功能的正常描述，属于合理的产品类别引用，不涉及异型号或旧型号身份混淆。MF-0100中"血压计播报低压80mmHg"实测值误写为"血压计播报高压80mmHg"属测试记录笔误，但不属于产品身份问题，应由测试记录质量审查处理。整体不构成DHF产品身份污染。

### 55. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0117`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_structural_label_not_content_gap`
- 文件：`11 T1样机\软件文件底稿\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70`
- 命中文本：## Sheet: 模板修改记录
- 驳回理由：MF-0117所在文件为Stage 11软件文件底稿中的软件质量策划评审检查表，primary_scope标注为false，且"## Sheet: 模板修改记录"与MC-CLUSTER-0010完全同构，均为Excel Sheet名称的格式还原。该Sheet用于记录模板变更历史，其存在不构成待填或未受控问题，不影响PT9L正式DHF/DMR证据链。

### 56. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0118`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2`
- 命中文本：# BP3L 软件图样E0 23.11
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 57. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0119`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:48`
- 命中文本：![图片 4](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d805c950.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 58. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0120`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50`
- 命中文本：![图片 6](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_a0cd39dd.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 59. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0121`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:52`
- 命中文本：![Picture 3](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_20a262b4.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 60. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0122`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54`
- 命中文本：![图片 8](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_e11cac5c.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 61. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0123`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:56`
- 命中文本：![Picture 7](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_f49c074.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 62. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0124`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:58`
- 命中文本：![图片 10](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_ae5eec4.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 63. 发现疑似旧型号/异类品类/模板残留：BP3L

- 原始候选 ID：`MF-0125`
- Agent：Product Identity Agent
- 复审轮次：`second_round_enriched_final`
- 类型：`auxiliary_scope_wrong_model_file_no_formal_impact`
- 文件：`11 T1样机\软件文件底稿\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:60`
- 命中文本：![图片 11](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_2540465a.gif)
- 驳回理由：8条候选（MF-0118至MF-0125）的primary_scope均为false，文件路径为"11 T1样机\\软件文件底稿\\软件图样E0 23.11"，"软件文件底稿"子目录表明其为工作底稿而非正式受控输出。同术语文件样本显示，同名文件"BP3L 软件图样E0 23.11"在Stage 07（软件设计方案E0 23.11\\软件图样E0 23.11）以primary_scope=true存在，说明该文件在正式Stage 07已受控归档，Stage 11底稿目录的副本属于历史来源/工作过程留存。文件内部编号字段含"PT9L-RJTY01 V1.0"，进一步说明该文件是PT9L软件图样的底稿版本（文件名沿用了BP3L原始文件名但内容已对应PT9L编号），属于文件命名历史遗留而非异型号文件混入正式DHF。按最终裁决政策，所有候选均在auxiliary范围，无primary_scope证据，当前证据不构成可确认的正式DHF错误，应予dismiss。

### 64. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0126`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:79`
- 命中文本：1\. “血压测量态”由“加压前处理”、“加压测量过程”、“发送测量数据”三个子模块组成。“加压前处理”主要进行加压前的浮零处理，为后续找到基准零点压力；“加压测量过程”为血压计充气过程，主要包含加压速度判断、压力平台判断、检波、抗干扰和计算过程；“发送测量数据”包括血压计在测量过程中向上位机发送压力、脉搏波等实时数据，以及在测量结束后向上位机发送血压、心跳等测量结果。
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 65. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0127`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:87`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 66. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0128`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:88`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 67. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0129`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:93`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 68. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0130`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:110`
- 命中文本：通讯方案采用《iHealth血压计通信协议V2.4》中如下命令字，具体指令格式参见《iHealth血压计通信协议V2.4》（GF-10-010 V2.4）。
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 69. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0131`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:127`
- 命中文本：\| 命令型 \| 0x32 \| 浮零完毕 \| 无 \| 无 \| 下位机回复ACK，单台血压计测量或多台血压计组成测量系统，但无需同时加压机型适用 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 70. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0132`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:128`
- 命中文本：\| 实时数据型 \| 0x30 \| 浮零中 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK ，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据浮零指令中的数据信息确定是否发送启动加压指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 71. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0133`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_category_term_functional_reference`
- 文件：`11 T1样机\软件文件底稿\软件方案E0 23.11\3-1 软件方案设计E0  23.11.via_lo_html.clean.md:130`
- 命中文本：\| 实时数据型 \| 0x3C/<br>0x3D \| 蓝牙接口测量过程数据 \| 无 \| 无 \| 上位机根据接收到指令的状态ID，确定是否回复ACK，对于多台血压计组成的测量系统，若需多台血压计同时加压，应根据测量数据指令中的数据信息确定是否发送测量完毕指令 \|
- 驳回理由：MC-CLUSTER-0026的primary_scope为false，所有候选均来自软件方案设计文件。文件中"血压计上电后"、"血压计自动关机"、"血压计充气过程"、"血压计通信协议"等均为对PT9L产品功能和通信方案的正常描述，PT9L本身即为血压计类产品，此类用词属合理的产品类别引用。MF-0130中引用的《iHealth血压计通信协议V2.4》为通用协议文件引用，属正常技术参考，不构成产品身份污染。

### 72. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0134`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_name_generic_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:107`
- 命中文本：\| 1 \| 初始化功能 \| 血压计上电后，初始化相关模块，等待移动设备与血压计建立蓝牙连接 \|
- 驳回理由：文件路径为'11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11'，属于PT9L开发阶段软件需求文件。所有命中文本（初始化功能、关机功能、错误显示功能、响应时间等）均以'血压计'作为被审产品PT9L的通用品类名称进行功能描述，语义上指代的正是PT9L本身，并非引用其他型号产品。'血压计'是医疗器械通用名称，在产品自身文件中使用不构成产品身份污染，应予驳回。

### 73. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0135`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_name_generic_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:108`
- 命中文本：\| 2 \| 关机功能 \| 蓝牙无连接时，血压计自动关机，关机时，泵和阀都不能工作； \|
- 驳回理由：文件路径为'11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11'，属于PT9L开发阶段软件需求文件。所有命中文本（初始化功能、关机功能、错误显示功能、响应时间等）均以'血压计'作为被审产品PT9L的通用品类名称进行功能描述，语义上指代的正是PT9L本身，并非引用其他型号产品。'血压计'是医疗器械通用名称，在产品自身文件中使用不构成产品身份污染，应予驳回。

### 74. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0136`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_name_generic_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:113`
- 命中文本：\| 7 \| 错误显示功能 \| 机器主要检测的错误包括：检测不到零点、高低压未检出、压力大于297mmHg时间超过1.5s、袖带内的压力在15mmHg以上的时间超过160s、满度错误、数据传输失败、EEPROM访问失败、EEPROM三备份错误、电量低等。当血压计与移动设备建立连接时，应能将相关错误信息传输至移动设备。 \|
- 驳回理由：文件路径为'11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11'，属于PT9L开发阶段软件需求文件。所有命中文本（初始化功能、关机功能、错误显示功能、响应时间等）均以'血压计'作为被审产品PT9L的通用品类名称进行功能描述，语义上指代的正是PT9L本身，并非引用其他型号产品。'血压计'是医疗器械通用名称，在产品自身文件中使用不构成产品身份污染，应予驳回。

### 75. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0137`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_compliant_reference`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:127`
- 命中文本：\| 3 \| 《PT9L设计输入-性能规格部分（三）IEC/EN 80601-2-30 》<br>(PT9L-SRXN01 V1.0) \| 201.7.2.<br>101 \| 自动血压计的显示 \|
- 驳回理由：该候选位于Stage 11软件需求规格文件（primary_scope=false），文件内容为PT9L设计输入性能规格的标准条款追溯表，"自动血压计的显示"（IEC/EN 80601-2-30第201.7.2.101条）是对适用标准条款的正常引用，用于说明软件需求的法规来源依据。PT9L为腕式血压计产品，引用该标准条款属于合理的技术文件结构，不存在型号混用或证据缺陷问题。

### 76. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0138`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_name_generic_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:151`
- 命中文本：上电后系统进入关机态（低功耗状态），不开机并且不充电时灯不亮。在关机态，与手机蓝牙进行连接并建立通信后，绿灯常亮，启动iHealth APP点击开始测量键开始测量，测量过程中血压计将得到的压力及心跳信息传输至手机；测量完毕后，手机显示高压、低压、心率、血压分类、心律不齐（如果有）；测量过程中若出现异常，手机会显示相应提示信息。当电池电量不足时，手机会显示电量不足提示并且血压计上的红色LED灯闪烁。
- 驳回理由：文件路径为'11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11'，属于PT9L开发阶段软件需求文件。所有命中文本（初始化功能、关机功能、错误显示功能、响应时间等）均以'血压计'作为被审产品PT9L的通用品类名称进行功能描述，语义上指代的正是PT9L本身，并非引用其他型号产品。'血压计'是医疗器械通用名称，在产品自身文件中使用不构成产品身份污染，应予驳回。

### 77. 发现疑似旧型号/异类品类/模板残留：血压计

- 原始候选 ID：`MF-0139`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`product_name_generic_usage`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:172`
- 命中文本：□ 自动关机时间：血压计与手机蓝牙断开连接后，血压计自动关机
- 驳回理由：文件路径为'11 T1样机\\软件文件底稿\\软件需求E0 23.11\\2-1 软件需求规格E0 23.11'，属于PT9L开发阶段软件需求文件。所有命中文本（初始化功能、关机功能、错误显示功能、响应时间等）均以'血压计'作为被审产品PT9L的通用品类名称进行功能描述，语义上指代的正是PT9L本身，并非引用其他型号产品。'血压计'是医疗器械通用名称，在产品自身文件中使用不构成产品身份污染，应予驳回。

### 78. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0140`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_marker_in_non_primary_scope`
- 文件：`11 T1样机\软件文件底稿\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:226`
- 命中文本：第 0 页 / 共 5 页 模板版本： I
- 驳回理由：该候选位于 Stage 11 T1样机软件文件底稿目录，primary_scope=false，属于草稿/底稿范围。'第 0 页 / 共 5 页 模板版本：I'是文档页脚的模板版本标识行，属于正常的文档格式元数据，不代表内容未填写或受控缺失。不影响PT9L正式DHF/DMR证据链，予以dismiss。

### 79. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0141`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`acceptable_reference_to_predecessor_model`
- 文件：`11 T1样机\运输\运输试验评估报告2020-3-27.via_lo_html.clean.md:37`
- 命中文本：\| **评 估 结 论** \| 根据“ PT3 运输试验报告”评估：<br>对比结果说明： 两机型相比较，彩包装、外箱材质、开合方式、连接方式均相同、两机型相比较彩包装、外箱尺寸、重量、材质均相似，故评估该包装对本产品在运输过程中整机的安全和性能无影响，评估合格。<br>☑ **合格** □ **不合格** *说明：*<br>□ **包装形式不同项差别较大，不能评估运输过程对整机安全和性能 的 影响，需进行运输试验** \|  \|
- 驳回理由：MF-0060文件名虽含"PT3 transport report"，但MF-0061第12行明确标注"Model name: PT9L"，文件受控编号为"PT9L-YSBG01 V1.0"，说明该运输报告的受控主体为PT9L。MF-0141为运输试验评估报告，明确说明"根据PT3运输试验报告评估"，通过对比PT3与PT9L的包装参数（彩包装、外箱材质、尺寸、重量等）进行相似性评估，结论为"评估合格"。这是医疗器械DHF中常见的参比机型评估方法，PT3作为已有机型被合理引用作为评估依据，不构成产品身份污染。文件名中"PT3"为历史来源标注，不影响PT9L正式DHF证据链。

### 80. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0170`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_as_descriptive_annotation`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:10`
- 命中文本：## 0. 标题栏（A 级，外购件 Famidoc 模板）
- 驳回理由：MF-0170中'外购件 Famidoc 模板'是对图纸标题栏来源的描述性注释（即该图纸使用Famidoc供应商标准图框），MF-0171中'Famidoc 供应商标准 A4 横向模板'是对图框规格的客观描述。两处均为读图报告对原始PDF图纸格式特征的如实记录，内容字段已填写完整（零件名、审批日期、公差等级等均有实际内容），不存在未填写或受控缺失问题。予以dismiss。

### 81. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0171`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_as_descriptive_annotation`
- 文件：`12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:26`
- 命中文本：\| **图框** \| Famidoc 供应商标准 A4 横向模板 \|
- 驳回理由：MF-0170中'外购件 Famidoc 模板'是对图纸标题栏来源的描述性注释（即该图纸使用Famidoc供应商标准图框），MF-0171中'Famidoc 供应商标准 A4 横向模板'是对图框规格的客观描述。两处均为读图报告对原始PDF图纸格式特征的如实记录，内容字段已填写完整（零件名、审批日期、公差等级等均有实际内容），不存在未填写或受控缺失问题。予以dismiss。

### 82. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0200`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_in_non_primary_scope_early_drawing`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\上盖20210727.pdf.md:38`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：两个候选均位于'早期图纸'子目录（上盖20210727、探头20210727），primary_scope=false，属于历史早期图纸范围。'技术要求（4条标准ABS模板）'是读图报告的章节标题，描述该图纸技术要求部分采用标准ABS注塑件模板条款，属于对图纸内容的客观描述，不代表文件未完成或受控缺失。不影响PT9L正式DHF/DMR证据链，予以dismiss。

### 83. 发现疑似旧型号/异类品类/模板残留：模板

- 原始候选 ID：`MF-0201`
- Agent：Document Control Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`template_label_in_non_primary_scope_early_drawing`
- 文件：`12 设计输出（含01、02）\设计输出清单二\早期图纸\探头20210727.pdf.md:25`
- 命中文本：## 1. 技术要求（4 条标准 ABS 模板）
- 驳回理由：两个候选均位于'早期图纸'子目录（上盖20210727、探头20210727），primary_scope=false，属于历史早期图纸范围。'技术要求（4条标准ABS模板）'是读图报告的章节标题，描述该图纸技术要求部分采用标准ABS注塑件模板条款，属于对图纸内容的客观描述，不代表文件未完成或受控缺失。不影响PT9L正式DHF/DMR证据链，予以dismiss。

### 84. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0239`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:31`
- 命中文本：\| 型号 \| PT9L \| PT3 \|
- 驳回理由：MF-0239、MF-0241、MF-0242、MF-0243、MF-0252均来自'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，文件明确位于'废案与备份'目录。PT3在该文件中作为同品种医疗器械（对比产品）被引用，属于临床评价中合理的同品种对比引用，且文件本身已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 85. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0240`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_historical_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:36`
- 命中文本：\| 符合注册要求的使用说明书 \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT9L） \| 附件1<br>iHealth体温计使用说明书<br>红外体温计（PT3） \|
- 驳回理由：该候选位于Stage 18废案与备份目录（primary_scope=false），文件为临床评价报告草稿。PT3在文件中作为PT9L的同品种对照医疗器械出现，用于临床等同性比较，这是临床评价报告的标准结构要求。文件明确标注PT9L为被评价产品，PT3为对照品种，引用逻辑清晰合理。文件位于废案目录，不影响正式DHF证据链。

### 86. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0241`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:46`
- 命中文本：PT9L红外体温计和PT3红外体温计均为有源器械。其等效性比较参见表3-1。
- 驳回理由：MF-0239、MF-0241、MF-0242、MF-0243、MF-0252均来自'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，文件明确位于'废案与备份'目录。PT3在该文件中作为同品种医疗器械（对比产品）被引用，属于临床评价中合理的同品种对比引用，且文件本身已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 87. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0242`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:83`
- 命中文本：\| PT3 \| ![图片 5](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_25bd38c1.png) \| PT9L \| ![图片 38](7.临床评价报告.via_lo_html_assets/7.临床评价报告_html_c235e89e.png) \|
- 驳回理由：MF-0239、MF-0241、MF-0242、MF-0243、MF-0252均来自'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，文件明确位于'废案与备份'目录。PT3在该文件中作为同品种医疗器械（对比产品）被引用，属于临床评价中合理的同品种对比引用，且文件本身已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 88. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0243`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:93`
- 命中文本：数据来源为柯顿（天津）电子医疗器械有限公司PT3红外体温计于2013年取得由中国人民解放军第 100医院及苏州市立医院本部医院所进行的临床试验报告所得，试验主要进行的是临床验证。
- 驳回理由：MF-0239、MF-0241、MF-0242、MF-0243、MF-0252均来自'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，文件明确位于'废案与备份'目录。PT3在该文件中作为同品种医疗器械（对比产品）被引用，属于临床评价中合理的同品种对比引用，且文件本身已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 89. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0244`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:97`
- 命中文本：产品的临床试验由护理人员负责实施，采取自身对照试验方法，采用TH30F非接触红外额式体温与经过校准的水银玻璃体温计同步测定的方法，验证非接触红外额式体温计的准确度。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 90. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0245`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:107`
- 命中文本：具体参加附件：TH30F临床研究方案及临床试验报告见附3。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 91. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0246`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:111`
- 命中文本：同品种医疗器械TH30F未收到投诉，未发现不良事件。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 92. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0247`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_historical_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:115`
- 命中文本：同品种医疗器械TH30F未采取过与临床风险相关的纠正措施。
- 驳回理由：该cluster两个候选均位于Stage 18废案与备份目录（primary_scope=false）的临床评价报告中。TH30F作为同品种医疗器械与PT3并列，用于支持PT9L的临床评价同品种路径，文件明确说明"PT3和TH30F为同品种医疗器械"并得出PT9L的评价结论。这是临床评价报告中标准的同品种引用方式，文件位于废案目录，不影响正式DHF/DMR证据链完整性。

### 93. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0248`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 94. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0249`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:186`
- 命中文本：（六）PT3和TH30F产品性能比对测试报告
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 95. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0250`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 96. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0251`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:188`
- 命中文本：针对PT3和TH30F两个型号产品，我司对其性能进行了比对测试，详见附件2。
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 97. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0252`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:190`
- 命中文本：（七）PT3红外体温计准确度验证报告
- 驳回理由：MF-0239、MF-0241、MF-0242、MF-0243、MF-0252均来自'18 设计确认\\废案与备份\\7.临床评价报告.via_lo_html.clean.md'，primary_scope=false，文件明确位于'废案与备份'目录。PT3在该文件中作为同品种医疗器械（对比产品）被引用，属于临床评价中合理的同品种对比引用，且文件本身已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 98. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0253`
- Agent：Regulatory Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`false_positive_historical_reference`
- 文件：`18 设计确认\废案与备份\7.临床评价报告.via_lo_html.clean.md:196`
- 命中文本：PT3和TH30F为同品种医疗器械，综合上述数据集的分析结果，PT9L在正常使用条件下，产品可达到预期性能；与预期受益相比较，产品的风险可接受。
- 驳回理由：该cluster两个候选均位于Stage 18废案与备份目录（primary_scope=false）的临床评价报告中。TH30F作为同品种医疗器械与PT3并列，用于支持PT9L的临床评价同品种路径，文件明确说明"PT3和TH30F为同品种医疗器械"并得出PT9L的评价结论。这是临床评价报告中标准的同品种引用方式，文件位于废案目录，不影响正式DHF/DMR证据链完整性。

### 99. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0254`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:12`
- 命中文本：型号规格：PT9CL
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 100. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0255`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:34`
- 命中文本：我公司天津九安医疗电子股份有限公司研制开发的PT9C型红外体温计是一款通过接收人体额头部位散发的红外能量，来测量人体温度的红外体温计。
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 101. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0256`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 102. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0257`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:82`
- 命中文本：PT9C与本公司注册生产的红外体温计 PT3（注册证号：津械注准20192070046）为实质性等同的同类产品，基本原理、结构组成、制造材料、性能要求、安全性评价、符合的国家/行业标准、预期用途等方面完全等同，且该同类产品上市销售无不良事故记录。依据国家食品药品监督管理局发布的《临床评价指导原则》规定，将本公司生产的红外体温计与上述公司生产的红外计进行了对比，具体对比情况说明见申报产品与同品种医疗器械对比表。
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 103. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0258`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 104. 发现疑似旧型号/异类品类/模板残留：PT9C

- 原始候选 ID：`MF-0259`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md:135`
- 命中文本：通过《申报产品与目录中已获准境内注册医疗器械对比表》中对比表明，拟注册的PT9C红外体温计产品在结构性能、材料组成、性能要求、灭菌消毒方式、适用范围、使用说明上与柯顿（天津）电子医疗器械有限公司注册生产的红外体温计PT3（注册证号：津械注准20192070046）基本相同，表明拟注册产品与已获准境内注册的产品基本等同。
- 驳回理由：MF-0254至MF-0259均来自'18 设计确认\\废案与备份\\PT9L医用电子体温计临床评价报告-中国版本不适用.via_lo_html.clean.md'，primary_scope=false，文件名明确标注'中国版本不适用'且位于废案目录。文件内容为PT9C的临床评价报告，PT9C在此作为申报产品被描述，与PT3进行同品种对比。该文件系PT9C阶段的历史废案文件被归档于PT9L DHF废案目录，不代表PT9L正式DHF/DMR的产品身份，不影响PT9L正式证据链。

### 105. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0260`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 106. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0261`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:2`
- 命中文本：# 附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 107. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0262`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 108. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0263`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:18`
- 命中文本：\| 测 试 记 录 单 ![附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg](附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx_assets/附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H_image_001.jpg) \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 109. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0264`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:22`
- 命中文本：\| 依据标准 \|  \| 柯顿（天津）电子医疗器械有限公司《红外体温计技术要求》 \|  \|  \|  \| 产品型号 \|  \|  \| PT3与TH30F \|  \| 试验时间 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 110. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0265`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:22`
- 命中文本：\| 依据标准 \|  \| 柯顿（天津）电子医疗器械有限公司《红外体温计技术要求》 \|  \|  \|  \| 产品型号 \|  \|  \| PT3与TH30F \|  \| 试验时间 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 111. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0266`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:34`
- 命中文本：\| 测试项目 \| #1号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 112. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0267`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:55`
- 命中文本：\| 测试项目 \| #2号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 113. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0268`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:76`
- 命中文本：\| 测试项目 \| #3号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 114. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0269`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:97`
- 命中文本：\| 测试项目 \| #4号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 115. 发现疑似旧型号/异类品类/模板残留：PT3

- 原始候选 ID：`MF-0270`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:118`
- 命中文本：\| 测试项目 \| #5号（PT3） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 116. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0271`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:139`
- 命中文本：\| 测试项目 \| #6号（TH30F） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 117. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0272`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:160`
- 命中文本：\| 测试项目 \| #7号（TH30F） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 118. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0273`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:181`
- 命中文本：\| 测试项目 \| #8号（TH30F） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 119. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0274`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:202`
- 命中文本：\| 测试项目 \| #9号（TH30F） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

### 120. 发现疑似旧型号/异类品类/模板残留：TH30F

- 原始候选 ID：`MF-0275`
- Agent：Product Identity Agent
- 复审轮次：`first_round_cluster_review`
- 类型：`historical_draft_reference`
- 文件：`18 设计确认\废案与备份\附件2：PT3与TH30F的黑体准确性比对测试报告V1.0H.via_xlsx.clean.md:223`
- 命中文本：\| 测试项目 \| #10号（TH30F） \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|
- 驳回理由：所有23个候选均来自'18 设计确认\\废案与备份\\'目录下的文件（临床评价报告及PT3与TH30F黑体准确性比对测试报告），primary_scope=false。TH30F在废案临床评价报告中作为临床验证所用的测试器械型号被引用，属于历史临床数据来源的合理说明，文件已被标记为废案。不影响PT9L正式DHF/DMR证据链。

> 仅展示前 120 条，完整数据见 `13_mechanical_agent_review/mechanical_dismissed_candidates.jsonl`。