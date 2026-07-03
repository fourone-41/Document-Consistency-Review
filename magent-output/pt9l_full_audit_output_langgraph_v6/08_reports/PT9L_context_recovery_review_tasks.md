# PT9L Context Recovery ?????????

> ?????`14_context_recovery/context_recovery_results.jsonl`
> ?????????????????????52 ????? `human_review`?

| ?? | ?? | ???? |
|---|---:|---|
| mechanical_review | 31 | human_review |
| challenge_agent | 21 | human_review |
| ?? | 52 | human_review |

## ????

### CTX-M-0001 / MC-CLUSTER-0073

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (16.0±2.0℃, 21±3℃, 23.0±2.0℃, 25±5℃, +15 °C, +35 °C, +40 °C, +5 °C) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0002 / MC-CLUSTER-0074

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (+15 °C, +35 °C, +40 °C, +5 °C, -104℉, -107.6℉, -109.2℉, -109.22℉) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0003 / MC-CLUSTER-0075

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (16.0±2.0℃, 23.0±2.0℃, -0.1℃, -0.2℃, -104℉, -107.6℉, -109.2℉, -40℃) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0004 / MC-CLUSTER-0076

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P3`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (-3V, 0.1 V, 01 V, 02 V, 04 V, 1.5V, 100 V, 12 V) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0005 / MC-CLUSTER-0077

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (-003-04, -078-02, -2-56, -20~55, 0 -4, 10~40, 1060-1, 10993-10) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0006 / MC-CLUSTER-0078

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (-003-04, -078-02, -20~55, 0-300, 0 -4, 10~40, 1060-3, 1112-86) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0007 / MC-CLUSTER-0079

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (1060-1, 10993-10, 10993-5, 1112-86, 1965-98, 2.6-3, 2002-10, 2020-3) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0008 / MC-CLUSTER-0080

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (23.0±2.0℃, -109.2℉, -42.9℃, 0.1°C, 0.2℃, 0.3℃, 0.4°F, 10℃) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0009 / MC-CLUSTER-0081

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P3`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (50±20%, 55±10%, -70%, -85%, -95%, 0%, 10%, 100 %) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0010 / MC-CLUSTER-0082

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (-1060h, 0.5s, 060 h, 1 min, 1.4 s, 1.5 s, 1060h, 14.8 h) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0011 / MC-CLUSTER-0083

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (1000-4, 1060-1, 1060-3, 10993-10, 10993-5, 1112-86, 14155-1, 14155-2) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0012 / MC-CLUSTER-0084

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (01 V, 1.5V, 15V, 2.7V, 2000 V, 2400 V, 300 V, 42.4 V) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0013 / MC-CLUSTER-0085

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (1 s, 10s, 15 s, 2s, 3秒, 30分钟, 48 h, 5 年) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0014 / MC-CLUSTER-0086

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (0%, 10%, 100 %, 110 %, 20%, 50%, 70%, 75%) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0015 / MC-CLUSTER-0087

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (060 h, 1.5 s, 1060 h, 2 h, 24 h, 4 h, 48 h, 5 s) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0016 / MC-CLUSTER-0088

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (±0.02℃, ± 0.03 °C, ±0.1°C, ±0.2℃, ± 0.3 ℃, ±0.5 °C, ±1 °C, ±2 °C) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0017 / MC-CLUSTER-0089

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P3`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (-95%, 100%, 15%, 20%, 50%, 70%, 75%, 85%) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0018 / MC-CLUSTER-0090

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (-95%, 10 %, 15 %, 3%, 55%, 70 %, 90 %, 93%) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0019 / MC-CLUSTER-0091

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P3`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (01 V, 1.5V, 12 V, 12.4 V, 15.1 V, 2.7V, 24.8 V, 3V) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0020 / MC-CLUSTER-0092

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (±0.03, ±0.05, ±0.1V, ±0.2, ±0.4, ±1mm, ±20, ±50) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0021 / MC-CLUSTER-0093

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (0.5s, 1分钟, 120 min, 15分钟, 2s, 30分钟, 5 s, 6小时) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 8, "parameter_context": 30, "page_context": 0}

### CTX-M-0022 / MC-CLUSTER-0094

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (±0, ±0.02, ±0.03, ±0.1V, ±0.2, ±0.4, ±0.5) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 7, "parameter_context": 30, "page_context": 0}

### CTX-M-0023 / MC-CLUSTER-0095

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (±0.05, ±0.2, ±0.4, ±0.5, ± 1, ±2) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 6, "parameter_context": 30, "page_context": 0}

### CTX-M-0024 / MC-CLUSTER-0096

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (±0.02℃, ± 0.1 °C, ±0.2℃, ± 0.3 ℃, ±2.0℃) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 5, "parameter_context": 30, "page_context": 0}

### CTX-M-0025 / MC-CLUSTER-0097

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (±0, ±0.2, ±0.4, ±0.5, ±1) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 5, "parameter_context": 30, "page_context": 0}

### CTX-M-0026 / MC-CLUSTER-0098

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_accuracy has multiple numeric values (0.03 v, 0.1V, 01 V, 2.7V, 3.3V) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 5, "parameter_context": 30, "page_context": 0}

### CTX-M-0027 / MC-CLUSTER-0099

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P3`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (±0.1°C, ±0.2℃, ±0.3℃, ±2.0℃) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 4, "parameter_context": 30, "page_context": 0}

### CTX-M-0028 / MC-CLUSTER-0100

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (± 0.1 °C, ± 0.2 ℃, ± 0.3 ℃) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 3, "parameter_context": 30, "page_context": 0}

### CTX-M-0029 / MC-CLUSTER-0101

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: operating_environment has multiple numeric values (±10%, ±20%, ±3%) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 3, "parameter_context": 30, "page_context": 0}

### CTX-M-0030 / MC-CLUSTER-0102

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: battery has multiple numeric values (±10 %, ±20%) across controlled documents.
- ??????补充 SSOT 参数上下文后仍存在跨阶段/跨文件数值差异，但当前证据无法区分规格要求、测试条件或环境设定，需人工确认参数语义。
- ??????{"same_item_evidence": 2, "parameter_context": 30, "page_context": 0}

### CTX-M-0031 / MC-CLUSTER-0103

- ???`mechanical`
- Agent?Hardware Agent
- ?????`parameter_semantics`
- ????`P2`
- ?????`human_review`
- ?????Parameter alignment candidate: measurement_range has multiple numeric values (±10 %, ±3%) across controlled documents.
- ??????补充参数上下文后仍无法判断差异是否属于真实不一致，需人工查看原始表格和测试条件。
- ??????{"same_item_evidence": 2, "parameter_context": 30, "page_context": 0}

### CTX-S-0032 / LLM-0001

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`risk_control_verification_context`
- ????`P1`
- ?????`human_review`
- ?????主范围风险控制验证报告（F0019）正文中出现旧型号PT3SBT，而非PT9L，导致预期用途描述与本项目不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 1, "parameter_context": 0, "page_context": 0}

### CTX-S-0033 / LLM-0006

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`product_identity_context`
- ????`P1`
- ?????`human_review`
- ?????主范围DFMEA文件（F0074）多处内容明确描述血压计功能（电池给血压计供电、包装血压计等），与PT9L红外体温计品类不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0034 / LLM-0007

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`product_identity_context`
- ????`P2`
- ?????`human_review`
- ?????主范围软件设计方案文件夹中存在BP3L软件图样（F0052），与PT9L项目型号不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0035 / LLM-0008

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`product_identity_context`
- ????`P1`
- ?????`human_review`
- ?????主范围设计输出清单二（F0235、F0236）中大量条目引用PT3SBT文件编号，与PT9L项目不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0036 / LLM-0009

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`product_identity_context`
- ????`P2`
- ?????`human_review`
- ?????主范围标签审核表（F0082）文件名为PT3SBT，内容引用PT2L型号及文件编号，与PT9L项目不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0037 / LLM-0010

- ???`semantic`
- Agent?Market & Category Scout Agent
- ?????`neighboring_evidence_context`
- ????`P2`
- ?????`human_review`
- ?????主范围设计输入汇总表（F0031）与历史草稿（F0319）在EN ISO 80601-2-56和MDR 2017/745适用性勾选上存在矛盾，正式版本选项需复核。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 4, "parameter_context": 0, "page_context": 12}

### CTX-S-0038 / LLM-0012

- ???`semantic`
- Agent?Regulatory Agent
- ?????`risk_control_verification_context`
- ????`P1`
- ?????`human_review`
- ?????结构类FMEA中将产品描述为'血压计'，与PT9L红外体温计品类不符，构成法规/验证闭环风险。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 1, "parameter_context": 0, "page_context": 12}

### CTX-S-0039 / LLM-0019

- ???`semantic`
- Agent?Regulatory Agent
- ?????`risk_control_verification_context`
- ????`P2`
- ?????`human_review`
- ?????说明书声明符合ISO 80601-2-56但'except of clause 5.2.2'，该豁免条款未在设计输入或风险文件中找到正式说明。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 2, "parameter_context": 0, "page_context": 12}

### CTX-S-0040 / LLM-0020

- ???`semantic`
- Agent?Regulatory Agent
- ?????`risk_control_verification_context`
- ????`P2`
- ?????`human_review`
- ?????设计输入和设计验证报告均未勾选CE认证，但说明书和风险文件多处引用EN标准，市场范围与标准引用存在不一致。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0041 / LLM-0022

- ???`semantic`
- Agent?Hardware Agent
- ?????`neighboring_evidence_context`
- ????`P1`
- ?????`human_review`
- ?????电池使用寿命测试报告中电池容量标注为1000mAh，与包装BOM中1200mAh不一致，测试代表性存疑。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 3, "parameter_context": 0, "page_context": 0}

### CTX-S-0042 / LLM-0025

- ???`semantic`
- Agent?Hardware Agent
- ?????`neighboring_evidence_context`
- ????`P2`
- ?????`human_review`
- ?????T1样机评审检查表中含"电池不能和袖带相邻存放"检查项，袖带为血压计专用部件，与IFT品类不符。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 2, "parameter_context": 0, "page_context": 0}

### CTX-S-0043 / LLM-0030

- ???`semantic`
- Agent?Software Agent
- ?????`document_control_context`
- ????`P2`
- ?????`human_review`
- ?????软件质量策划评审检查表、软件需求规格书评审检查表、软件设计方案评审检查表的评审结论栏全部为空白复选框，评审是否通过无法确认
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 12}

### CTX-S-0044 / LLM-0040

- ???`semantic`
- Agent?Risk Traceability Agent
- ?????`risk_control_verification_context`
- ????`P1`
- ?????`human_review`
- ?????DHF中存在两套平行风险文件：IFT前缀（F0017-F0020）与PT9L前缀（F0021-F0024），均为同名文件，未明确哪套为正式受控版本。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0045 / LLM-0046

- ???`semantic`
- Agent?Risk Traceability Agent
- ?????`risk_control_verification_context`
- ????`P2`
- ?????`human_review`
- ?????用户现场测试计划（F0260）文件名含PT9C，但内容包含风险评估条款，未见PT9L对应版本的用户测试计划证据。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 3, "parameter_context": 0, "page_context": 12}

### CTX-S-0046 / LLM-0047

- ???`semantic`
- Agent?Risk Traceability Agent
- ?????`risk_control_verification_context`
- ????`P2`
- ?????`human_review`
- ?????EMC型式试验报告（F0456）明确要求免疫通过/失败准则应纳入风险管理文件，但现有证据目录中未见风险管理文件包含EMC免疫准则的对应条款。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 3, "parameter_context": 0, "page_context": 0}

### CTX-S-0047 / LLM-0050

- ???`semantic`
- Agent?V&V Agent
- ?????`neighboring_evidence_context`
- ????`P2`
- ?????`human_review`
- ?????T1阶段设计验证报告封皮中三个子报告勾选框均为"□"（未勾选），无法确认T1验证已正式完成并通过。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0048 / LLM-0053

- ???`semantic`
- Agent?V&V Agent
- ?????`product_identity_context`
- ????`P1`
- ?????`human_review`
- ?????生物相容性报告（皮肤刺激、皮肤致敏、细胞毒性）均以PT5为受试样品，未见PT9L专属生物相容性评价证据。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 12}

### CTX-S-0049 / LLM-0055

- ???`semantic`
- Agent?V&V Agent
- ?????`risk_control_verification_context`
- ????`P2`
- ?????`human_review`
- ?????设计验证计划封皮（F0118）中子计划勾选框状态无法从证据中确认，存在验证计划正式批准状态不明的风险。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0050 / LLM-0059

- ???`semantic`
- Agent?V&V Agent
- ?????`neighboring_evidence_context`
- ????`P3`
- ?????`human_review`
- ?????产品检验标准中允许对不合格温度计复测两次且两次合格即判合格，该规则是否已在验证计划判定准则中明确引用存疑。
- ??????自动补证据未找到足够上下文，需人工补充原始文件或受控版本信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 0}

### CTX-S-0051 / LLM-0062

- ???`semantic`
- Agent?DMR/SOP Agent
- ?????`risk_control_verification_context`
- ????`P1`
- ?????`human_review`
- ?????外观图（F0177）与外箱图纸（F0164）的Drawing NO.均为PT9L-F01，但两者为不同物件，图号冲突将导致图纸管理混乱和制造转移错误风险。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 4, "parameter_context": 0, "page_context": 12}

### CTX-S-0052 / LLM-0063

- ???`semantic`
- Agent?DMR/SOP Agent
- ?????`product_identity_context`
- ????`P2`
- ?????`human_review`
- ?????散热器金属套图纸（75CEE0-Model.pdf）为外购供应商图号（GXT-001/天津小泉），尚未完成内部标准图号映射，制造转移资料中图号体系不统一。
- ??????已补充 PageIndex 上下文，但仍需要人工确认受控版本、上下游文件关系或原始表格信息。
- ??????{"same_item_evidence": 5, "parameter_context": 0, "page_context": 12}
