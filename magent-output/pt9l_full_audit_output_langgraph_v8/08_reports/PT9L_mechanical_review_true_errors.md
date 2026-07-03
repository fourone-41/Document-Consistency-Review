# PT9L 机械候选二轮复审确认问题

> 生成时间：2026-07-01T16:12:34
> 范围：仅包含 mechanical_review_node 判定为 confirm 的机械候选。

## 1. 摘要

- 确认问题数：167

## 2. 问题清单

### 1. Stage 01客户需求书文件标题含"血压计"，但内容为红外额温计规格，产品品类标签与实际内容不符，构成产品身份污染。

- Finding ID：`MR-0001`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径及标题均为"客户需求书E0-血压计 23.6"，但PF-0001至PF-0003的内容明确描述温度显示范围32.0℃～42.9℃、红外测温方式测量人体额头温度等额温计特征参数，与血压计品类完全不符。PF-0003第81行明确写明"本品主要采用红外测温方式测量人体额头温度"。文件标题"血压计"系品类标签错误，该文件作为PT9L DHF Stage 01正式立项文件，标题与内容的品类不一致会导致产品身份证据链混乱，需正式更正文件标题或补充说明。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:2` # 客户需求书E0-血压计 23.6

### 2. 正式风险评估报告（IFT-FXPJ01 V2.0）产品介绍段落将PT3SBT作为独立蓝牙型号嵌入，构成PT9L DHF主审范围内的产品身份污染缺陷

- Finding ID：`MR-0002`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件路径为03风险分析\\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530，primary_scope=true，属于PT9L正式DHF主审范围内的受控风险评估报告。第93行产品介绍段落明确写明"PT3SBT can transmit the temperature to a smart device with Bluetooth"，将PT3SBT作为具有蓝牙功能的独立型号标识嵌入本应专属于PT9L的产品描述中。结合same_term_file_samples显示PT3SBT在Stage 11（T1样机标签审核表）和Stage 12（设计输出清单）中大量出现（共46条primary记录），说明PT3SBT是DHF体系内另一独立型号，而非PT9L的别名或子型号。在正式风险评估报告的产品介绍章节中混入另一型号标识，且无任何多型号共用声明，构成可确认的产品身份污染错误，影响风险评估文件的产品适用范围完整性。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers

### 3. 正式风险评估报告（IFT-FXPJ01 V2.0）产品介绍段落将PT3SBT作为独立蓝牙型号嵌入，构成PT9L DHF主审范围内的产品身份污染缺陷

- Finding ID：`MR-0003`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件路径为03风险分析\\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530，primary_scope=true，属于PT9L正式DHF主审范围内的受控风险评估报告。第93行产品介绍段落明确写明"PT3SBT can transmit the temperature to a smart device with Bluetooth"，将PT3SBT作为具有蓝牙功能的独立型号标识嵌入本应专属于PT9L的产品描述中。结合same_term_file_samples显示PT3SBT在Stage 11（T1样机标签审核表）和Stage 12（设计输出清单）中大量出现（共46条primary记录），说明PT3SBT是DHF体系内另一独立型号，而非PT9L的别名或子型号。在正式风险评估报告的产品介绍章节中混入另一型号标识，且无任何多型号共用声明，构成可确认的产品身份污染错误，影响风险评估文件的产品适用范围完整性。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers

### 4. 正式风险控制验证报告（IFT-FXYS01 V2.0）产品介绍段落将PT3SBT作为独立蓝牙型号嵌入，与MC-CLUSTER-0006构成同一文件体系内的系统性产品身份污染缺陷

- Finding ID：`MR-0004`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件路径为03风险分析\\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01 V2.0，primary_scope=true，属于PT9L正式DHF主审范围内的受控风险控制验证报告。第85行产品介绍段落与MC-CLUSTER-0006完全相同，同样写明"PT3SBT can transmit the temperature to a smart device with Bluetooth"。两份正式风险文件（风险评估报告+风险控制验证报告）均在产品介绍章节嵌入PT3SBT型号标识，说明这是系统性问题而非偶发笔误。风险控制验证报告的产品范围定义直接影响蓝牙相关风险控制措施的适用性判断，在无多型号共用声明的情况下，该错误构成可确认的文件受控缺陷和产品身份污染。
- 证据：
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers

### 5. 正式风险控制验证报告（IFT-FXYS01 V2.0）产品介绍段落将PT3SBT作为独立蓝牙型号嵌入，与MC-CLUSTER-0006构成同一文件体系内的系统性产品身份污染缺陷

- Finding ID：`MR-0005`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件路径为03风险分析\\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01 V2.0，primary_scope=true，属于PT9L正式DHF主审范围内的受控风险控制验证报告。第85行产品介绍段落与MC-CLUSTER-0006完全相同，同样写明"PT3SBT can transmit the temperature to a smart device with Bluetooth"。两份正式风险文件（风险评估报告+风险控制验证报告）均在产品介绍章节嵌入PT3SBT型号标识，说明这是系统性问题而非偶发笔误。风险控制验证报告的产品范围定义直接影响蓝牙相关风险控制措施的适用性判断，在无多型号共用声明的情况下，该错误构成可确认的文件受控缺陷和产品身份污染。
- 证据：
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers

### 6. Stage 05结构设计方案评审检查表文件标题含"血压计"，与PT9L额温计产品身份不符，构成产品身份污染。

- Finding ID：`MR-0006`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件标题为"结构设计方案评审检查表-血压计E0 23.11"，位于Stage 05正式设计阶段，属于PT9L DHF主审范围内的正式文件。文件标题中"血压计"与PT9L（红外额温计）产品品类不符。虽然仅有一个候选（MF-0030），但该文件作为正式设计评审检查表，标题品类错误会影响产品身份证据链的完整性，需正式更正。
- 证据：
  - `05 结构设计方案E0 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2` # 结构设计方案评审检查表-血压计E0 23.11

### 7. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0007`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 8. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0008`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 9. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0009`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:20` \| **Drawing NO.** \| （待填 - 见右下标题栏） \|

### 10. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0010`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:21` \| **Part name** \| （待填 - 见右下标题栏中文零件名） \|

### 11. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0011`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:22` \| **Pro material** \| （待填） \|

### 12. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0012`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:23` \| **Surf dispose** \| （待填） \|

### 13. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0013`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:24` \| **Scale** \| （待填） \|

### 14. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0014`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:25` \| **Tolerance** \| （待填 - 见标题栏 Tolerance 表） \|

### 15. 硬件设计方案E0读图报告中标题栏关键字段（图号、零件名、材料、表面处理、比例、公差）均为"待填"占位符，正式DHF文件信息不完整。

- Finding ID：`MR-0015`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 06正式主审范围，文件头注释明确标注"自动生成模板+待填"，且Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance共6个标题栏字段均以"（待填）"形式存在，未提取或录入实际图纸信息。这些字段是硬件设计图纸可追溯性的核心标识，缺失将导致DHF证据链断裂，构成实质性受控质量问题。Model NO.已填PT9L，确认属于本产品正式文件范围。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:33` > 待填 - 通常位于左下角或右下角，逐条完整录入（不可跳过）。

### 16. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0016`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11

### 17. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0017`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50` ![图片 13](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d468a82f.png)

### 18. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0018`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54` ![图片 23](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_cd06a829.png)

### 19. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0019`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:58` ![图片 24](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_7adb510b.png)

### 20. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0020`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:62` ![图片 25](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_e758576.png)

### 21. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0021`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:66` ![图片 27](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_91561bdc.png)

### 22. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0022`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:70` ![图片 18](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_9bff6abd.png)

### 23. Stage 07软件图样文件名及资产路径全部使用"BP3L"，但文件内部编号标注为PT9L，文件名与受控编号存在型号不一致，构成产品身份混淆。

- Finding ID：`MR-0023`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，文件名及所有图片资产路径均使用"BP3L"型号标识。但MF-0041第6行明确显示文件编号为"PT9L-RJTY01 V1.0"，说明该文件受控编号属于PT9L体系。文件名与受控编号的型号不一致（BP3L vs PT9L）在正式DHF软件设计阶段属于产品身份混淆问题：若BP3L为旧型号或平台型号，需有明确的共用件/转换说明；若为命名错误，需正式更正文件名。当前证据不足以判断BP3L与PT9L的关系，但文件名型号与受控编号型号不一致本身即为需纠正的问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:74` ![图片 19](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_4f8d1455.png)

### 24. 软件需求规格书页脚显示"第0页/共5页 模板版本：I"，表明文件仍为模板状态，未完成正式化转换。

- Finding ID：`MR-0024`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件路径位于Stage 07正式主审范围。"第0页"表明页码未更新，"模板版本：I"表明文件版本标识仍停留在模板初始版本，未升级为正式受控版本号。软件需求规格书是IEC 62304合规的核心文件，若以模板状态归档将导致软件需求基线无法确立，属于实质性受控质量问题。
- 证据：
  - `07 软件设计方案E0 23.11\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:177` 第 0 页 / 共 5 页 模板版本： I

### 25. DFMEA文件中FMEA编号含"XXXX"占位符未填写，且产品型号标注为KD-5915L而非PT9L，存在文件标识缺失与型号不符双重问题。

- Finding ID：`MR-0025`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围（T1样机DFMEA）。MF-0050中FMEA编号"KD-XXXX-PDFM01 V1.0"、MF-0059中"KD-XXXX-ODFM01 V1.0"均含XXXX占位符，表明文件编号未完成填写。同时两处产品型号均为KD-5915L，与本项目PT9L不符，不能以"合理引用旧型号"解释，因为FMEA是针对具体产品的风险分析文件，型号错误意味着分析对象可能不对应PT9L实际设计，严重影响DHF/DMR证据链完整性。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:12` \|  \| 分类： \| 包装类 \|  \|  \| 编制人： \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA编号：KD-XXXX-PDFM01 V1.0 \|  \|  \|  \|  \|  \|  \|  \|

### 26. Stage 11 DFMEA文件中产品型号标注为KD-5915L，与PT9L不符，且内容中大量出现"血压计"功能描述，该DFMEA文件疑为其他产品文件混入PT9L DHF，构成严重产品身份污染。

- Finding ID：`MR-0026`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，第13行明确标注"产品型号：KD-5915L"，与PT9L完全不符。文件内容中"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"等描述均指向血压计产品，而非红外额温计PT9L。该DFMEA文件位于Stage 11 T1样机阶段，属于PT9L DHF正式主审范围，但其产品型号和内容均属于另一产品（KD-5915L血压计），属于严重的产品身份污染——错误产品的DFMEA被纳入PT9L DHF，将导致风险分析证据链完全失效，需立即核查并替换为PT9L对应的正确DFMEA文件。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17` \|  \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \|  \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \|  \|  \| □ \|

### 27. Stage 11 DFMEA文件中产品型号标注为KD-5915L，与PT9L不符，且内容中大量出现"血压计"功能描述，该DFMEA文件疑为其他产品文件混入PT9L DHF，构成严重产品身份污染。

- Finding ID：`MR-0027`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，第13行明确标注"产品型号：KD-5915L"，与PT9L完全不符。文件内容中"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"等描述均指向血压计产品，而非红外额温计PT9L。该DFMEA文件位于Stage 11 T1样机阶段，属于PT9L DHF正式主审范围，但其产品型号和内容均属于另一产品（KD-5915L血压计），属于严重的产品身份污染——错误产品的DFMEA被纳入PT9L DHF，将导致风险分析证据链完全失效，需立即核查并替换为PT9L对应的正确DFMEA文件。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:18` \|  \| 彩包装 \| 包装血压计 \| 腕枕无法装入彩包装或腕枕装入彩包装后晃动量太大 \| 生产人员无法包装 \| 4 \| C \| 彩包装的尺寸设计不合理 \| 2 \|  \| 实际装配 \| 2 \| 16 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 28. Stage 11 DFMEA文件中产品型号标注为KD-5915L，与PT9L不符，且内容中大量出现"血压计"功能描述，该DFMEA文件疑为其他产品文件混入PT9L DHF，构成严重产品身份污染。

- Finding ID：`MR-0028`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，第13行明确标注"产品型号：KD-5915L"，与PT9L完全不符。文件内容中"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"等描述均指向血压计产品，而非红外额温计PT9L。该DFMEA文件位于Stage 11 T1样机阶段，属于PT9L DHF正式主审范围，但其产品型号和内容均属于另一产品（KD-5915L血压计），属于严重的产品身份污染——错误产品的DFMEA被纳入PT9L DHF，将导致风险分析证据链完全失效，需立即核查并替换为PT9L对应的正确DFMEA文件。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:19` \|  \| 彩包装 \| 包装血压计 \| 彩包装支撑强度不够 \| 彩包装褶皱或破损 \| 4 \| C \| 彩包装的材质强度不够 \| 3 \|  \| 跌落试验、运输试验 \| 2 \| 24 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 29. Stage 11 DFMEA文件中产品型号标注为KD-5915L，与PT9L不符，且内容中大量出现"血压计"功能描述，该DFMEA文件疑为其他产品文件混入PT9L DHF，构成严重产品身份污染。

- Finding ID：`MR-0029`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，第13行明确标注"产品型号：KD-5915L"，与PT9L完全不符。文件内容中"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"等描述均指向血压计产品，而非红外额温计PT9L。该DFMEA文件位于Stage 11 T1样机阶段，属于PT9L DHF正式主审范围，但其产品型号和内容均属于另一产品（KD-5915L血压计），属于严重的产品身份污染——错误产品的DFMEA被纳入PT9L DHF，将导致风险分析证据链完全失效，需立即核查并替换为PT9L对应的正确DFMEA文件。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:21` \|  \| 铭牌 \| 给用户关于机器的信息 \| 铭牌在运输过程中脱落 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌背胶强度不够 \| 3 \|  \| 跌落试验、运输试验 \| 2 \| 24 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 30. Stage 11 DFMEA文件中产品型号标注为KD-5915L，与PT9L不符，且内容中大量出现"血压计"功能描述，该DFMEA文件疑为其他产品文件混入PT9L DHF，构成严重产品身份污染。

- Finding ID：`MR-0030`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：MF-0051至MF-0057均来自"结构类FMEA E0(1)(1).via_xlsx.clean.md"，第13行明确标注"产品型号：KD-5915L"，与PT9L完全不符。文件内容中"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"等描述均指向血压计产品，而非红外额温计PT9L。该DFMEA文件位于Stage 11 T1样机阶段，属于PT9L DHF正式主审范围，但其产品型号和内容均属于另一产品（KD-5915L血压计），属于严重的产品身份污染——错误产品的DFMEA被纳入PT9L DHF，将导致风险分析证据链完全失效，需立即核查并替换为PT9L对应的正确DFMEA文件。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:23` \|  \| 铭牌 \| 给用户关于机器的信息 \| 标识不清楚 内容不全面 \| 用户无法识别血压计的相关法规信息 用户误用 \| 9 \| A \| 印刷油墨质量不好 未完全符合法规要求 \| 4 \|  \| 目测检查 法规符合性检查 \| 5 \| 180 \| 铭牌内容及可识别度检验 \| 9 \| 4 \| 1 \| 36 \| 检查检验记录 \

### 31. DFMEA文件中FMEA编号含"XXXX"占位符未填写，且产品型号标注为KD-5915L而非PT9L，存在文件标识缺失与型号不符双重问题。

- Finding ID：`MR-0031`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围（T1样机DFMEA）。MF-0050中FMEA编号"KD-XXXX-PDFM01 V1.0"、MF-0059中"KD-XXXX-ODFM01 V1.0"均含XXXX占位符，表明文件编号未完成填写。同时两处产品型号均为KD-5915L，与本项目PT9L不符，不能以"合理引用旧型号"解释，因为FMEA是针对具体产品的风险分析文件，型号错误意味着分析对象可能不对应PT9L实际设计，严重影响DHF/DMR证据链完整性。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:188` \|  \| 分类： \| 辅料类 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA编号：KD-XXXX-ODFM01 V1.0 \|  \|  \|  \|  \|  \|  \|

### 32. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0032`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）

### 33. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0033`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）

### 34. 标签审核表文件名含旧型号PT3SBT，文件内同时混用PT2L与PT9L模板，且所有Sheet中签署日期字段均为空白"年月日"，属于型号混用与签署缺失问题。

- Finding ID：`MR-0034`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围。文件名"PT3SBT标签审核表（海外更新）"使用旧型号PT3SBT，内部Sheet"标签报告模板-美"包含PT2L(美亚)标签检查报告，与本项目PT9L不符。虽然Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"均已更新为PT9L，但所有Sheet的拟制、审核、检查签署日期字段均为"年月日"空白占位，表明正式签署未完成。标签审核是法规合规的关键证据，签署缺失使文件不具备受控有效性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:6` ## Sheet: 标签报告模板 -美

### 35. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0035`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告

### 36. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0036`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计

### 37. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0037`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:16` \| ▉说明书 □彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-SMSP09 \|  \|  \|  \|  \|

### 38. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0038`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:17` \| □说明书 ▉彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-CBZP07 \|  \|  \|  \|  \|

### 39. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0039`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:18` \| □说明书 □彩包装 ▉铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-F96 \|  \|  \|  \|  \|

### 40. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0040`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:19` \| □说明书 □彩包装 □铭牌 ▉外箱 □其他： \|  \|  \|  \| PT2L-F97 \|  \|  \|  \|  \|

### 41. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0041`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:22` \| IEC 60601-1 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ01 V1.0 \|

### 42. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0042`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:23` \| IEC 60601-1-2 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ02 V1.0 \|

### 43. 标签审核表文件名含旧型号PT3SBT，文件内同时混用PT2L与PT9L模板，且所有Sheet中签署日期字段均为空白"年月日"，属于型号混用与签署缺失问题。

- Finding ID：`MR-0043`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围。文件名"PT3SBT标签审核表（海外更新）"使用旧型号PT3SBT，内部Sheet"标签报告模板-美"包含PT2L(美亚)标签检查报告，与本项目PT9L不符。虽然Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"均已更新为PT9L，但所有Sheet的拟制、审核、检查签署日期字段均为"年月日"空白占位，表明正式签署未完成。标签审核是法规合规的关键证据，签署缺失使文件不具备受控有效性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:39` ## Sheet: 标签报告模板 -美  (2)

### 44. 标签审核表文件名含旧型号PT3SBT，文件内同时混用PT2L与PT9L模板，且所有Sheet中签署日期字段均为空白"年月日"，属于型号混用与签署缺失问题。

- Finding ID：`MR-0044`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围。文件名"PT3SBT标签审核表（海外更新）"使用旧型号PT3SBT，内部Sheet"标签报告模板-美"包含PT2L(美亚)标签检查报告，与本项目PT9L不符。虽然Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"均已更新为PT9L，但所有Sheet的拟制、审核、检查签署日期字段均为"年月日"空白占位，表明正式签署未完成。标签审核是法规合规的关键证据，签署缺失使文件不具备受控有效性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:68` ## Sheet: 标签报告模板 -简版

### 45. 标签审核表文件名含旧型号PT3SBT，文件内同时混用PT2L与PT9L模板，且所有Sheet中签署日期字段均为空白"年月日"，属于型号混用与签署缺失问题。

- Finding ID：`MR-0045`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：文件位于Stage 11正式主审范围。文件名"PT3SBT标签审核表（海外更新）"使用旧型号PT3SBT，内部Sheet"标签报告模板-美"包含PT2L(美亚)标签检查报告，与本项目PT9L不符。虽然Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"均已更新为PT9L，但所有Sheet的拟制、审核、检查签署日期字段均为"年月日"空白占位，表明正式签署未完成。标签审核是法规合规的关键证据，签署缺失使文件不具备受控有效性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:101` ## Sheet: 标签报告模板 -欧美

### 46. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0046`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:156` \|  \| – the date of manufacture or use by date, if applicable. – 如果适用，生产日期或使用截止日期。 The serial number, lot or batch identifier, and the date of manufacture may be provided in a hum

### 47. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0047`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:156` \|  \| – the date of manufacture or use by date, if applicable. – 如果适用，生产日期或使用截止日期。 The serial number, lot or batch identifier, and the date of manufacture may be provided in a hum

### 48. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0048`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:161` \|  \| When consulting the ACCOMPANYING DOCUMENTS is a mandatory action, safety sign IEC 60878 Safety 01 (see Table D.2, safety sign 10) shall be used instead of symbol ISO 7000-16

### 49. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0049`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:161` \|  \| When consulting the ACCOMPANYING DOCUMENTS is a mandatory action, safety sign IEC 60878 Safety 01 (see Table D.2, safety sign 10) shall be used instead of symbol ISO 7000-16

### 50. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0050`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:186` \|  \| ME EQUIPMENT or its parts shall be marked with a symbol, using the letters IP followed by the designations described in IEC 60529, according to the classification in 6.3 (se

### 51. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0051`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:186` \|  \| ME EQUIPMENT or its parts shall be marked with a symbol, using the letters IP followed by the designations described in IEC 60529, according to the classification in 6.3 (se

### 52. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0052`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:189` \|  \| TYPE B APPLIED PARTS with symbol IEC 60417-5840,/B型应用部分以IEC60417-5840符号标记（DB:2002-10全部） \| NA \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_010.png](PT3SBT标签审核表（海外更新）.vi

### 53. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0053`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:189` \|  \| TYPE B APPLIED PARTS with symbol IEC 60417-5840,/B型应用部分以IEC60417-5840符号标记（DB:2002-10全部） \| NA \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_010.png](PT3SBT标签审核表（海外更新）.vi

### 54. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0054`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:196` \| 7.2.11 \| 符号Symbols \| —— \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_011.png](PT3SBT标签审核表（海外更新）.via_xlsx_assets/PT3SBT标签审核表（海外更新）_image_011.png) \| —— \|

### 55. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0055`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:196` \| 7.2.11 \| 符号Symbols \| —— \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_011.png](PT3SBT标签审核表（海外更新）.via_xlsx_assets/PT3SBT标签审核表（海外更新）_image_011.png) \| —— \|

### 56. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0056`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:280` \|  \| For mains-operated ME EQUIPMENT with an additional power source not automatically maintained in a fully usable condition, the instructions for use shall include a warning st

### 57. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0057`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:280` \|  \| For mains-operated ME EQUIPMENT with an additional power source not automatically maintained in a fully usable condition, the instructions for use shall include a warning st

### 58. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0058`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:282` \|  \| If an INTERNAL ELECTRICAL POWER SOURCE is replaceable, the instructions for use shall state its specification./如果内部电源是可更换的，使用说明书应陈述其规格。 \| A \| 检查说明书是否有此描述 \| OK \|  \| Prod

### 59. PT3SBT标签审核表文件内部实质内容为PT2L红外体温计，文件标题与内容型号严重不符，构成标签合规证据缺陷

- Finding ID：`MR-0059`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件名及标题为"PT3SBT标签审核表（海外更新）"，但文件内部所有实质内容均指向PT2L：产品型号填写为PT2L，项目编号为2020-DEV01，产品名称为红外体温计，文件编号为PT2L-SMSP09/PT2L-CBZP07/PT2L-F96/PT2L-F97，检查记录引用PT2L(美亚)-ZXBQ01/02。该文件位于Stage 11正式目录（primary_scope=true），共24个候选命中。文件标题声称审核PT3SBT的标签，但内容实为PT2L的标签审核数据，这意味着PT3SBT实际上缺乏有效的标签审核证据，或该文件系错误复用PT2L模板未更新内容，构成实质性标签合规证据缺陷，影响PT9L DHF证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:282` \|  \| If an INTERNAL ELECTRICAL POWER SOURCE is replaceable, the instructions for use shall state its specification./如果内部电源是可更换的，使用说明书应陈述其规格。 \| A \| 检查说明书是否有此描述 \| OK \|  \| Prod

### 60. PT9L正式BOM（EBOM01和T1EB01）中传感器板PCB图号标注为PT9C-CNTP01 V1.0，属于跨型号图号引用，现有证据范围内未见共用件受控说明，构成BOM产品身份不一致缺陷。

- Finding ID：`MR-0060`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0095和MF-0096均来自primary_scope=true的PT9L正式BOM文件（Stage 11），传感器板第2行PCB的图号字段明确标注为"PT9C-CNTP01 V1.0"，带有PT9C型号前缀，与文件所属产品PT9L不一致。在全部76条同术语证据中（primary 19条、auxiliary 57条），未发现任何共用件台账、跨型号零部件受控声明或PT9C-CNTP01适用性转换记录。按最终裁决政策，当前证据足以证明正式BOM中存在跨型号图号引用且缺乏受控说明，构成可确认的产品身份不一致问题，应予confirm。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 61. PT9L正式BOM（EBOM01和T1EB01）中传感器板PCB图号标注为PT9C-CNTP01 V1.0，属于跨型号图号引用，现有证据范围内未见共用件受控说明，构成BOM产品身份不一致缺陷。

- Finding ID：`MR-0061`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0095和MF-0096均来自primary_scope=true的PT9L正式BOM文件（Stage 11），传感器板第2行PCB的图号字段明确标注为"PT9C-CNTP01 V1.0"，带有PT9C型号前缀，与文件所属产品PT9L不一致。在全部76条同术语证据中（primary 19条、auxiliary 57条），未发现任何共用件台账、跨型号零部件受控声明或PT9C-CNTP01适用性转换记录。按最终裁决政策，当前证据足以证明正式BOM中存在跨型号图号引用且缺乏受控说明，构成可确认的产品身份不一致问题，应予confirm。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 62. PT9L正式设计验证报告中存在名为"血压计法规标准清单20160719"的Sheet，日期为2016年，疑为旧型号/旧模板遗留内容混入正式DHF文件。

- Finding ID：`MR-0062`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0097所在文件为PT9L Stage 11正式设计验证报告（primary_scope=true），其中Sheet名"血压计法规标准清单20160719"含有明确的2016年日期，与PT9L项目时间线不符，且未标注型号为PT9L。该Sheet可能是从旧型号文件复制而来的模板页，未经清理即纳入正式验证报告，构成正式DHF文件中存在旧型号/历史遗留内容的产品身份污染风险，属于可复核的实质性问题。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:127` ## Sheet: 血压计法规标准清单20160719

### 63. PT9L Stage 12正式设计输出BOM（PT9L-EBOM01 V1.0）中传感器板PCB图号标注为PT9C-CNTP01 V1.0，属于跨型号图号引用，现有证据范围内未见共用件受控说明，构成正式设计输出BOM产品身份不一致缺陷。

- Finding ID：`MR-0063`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0142来自primary_scope=true的Stage 12正式设计输出文件（PT9L-设计输出清单一\\机芯类组件清单PT9L-EBOM01 V1.0），属于最高受控级别的设计输出范围。BOM第50行传感器板PCB图号字段明确为"PT9C-CNTP01 V1.0"，与产品型号PT9L不符。该问题与MC-CLUSTER-0020为同一PCB在不同阶段文件中的重复体现，Stage 12正式设计输出中仍存在此跨型号引用，说明问题未在设计输出阶段得到纠正。全部证据范围内未见共用件受控声明或适用性验证记录。按最终裁决政策，正式设计输出BOM中存在跨型号图号引用且缺乏受控说明，证据足以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 64. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0064`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:26` \| 3 \| 接口板PCB图 \| Top Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 65. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0065`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:27` \| 3 \| 接口板PCB图 \| Top Overlay 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 66. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0066`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:28` \| 3 \| 接口板PCB图 \| Bottom Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 67. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0067`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:29` \| 3 \| 接口板PCB图 \| Bottom Overlay 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 68. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0068`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:30` \| 3 \| 接口板PCB图 \| Drill Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 69. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0069`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:31` \| 3 \| 接口板PCB图 \| 拼板示意图(顶层) \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 70. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0070`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:32` \| 3 \| 接口板PCB图 \| 拼板示意图(底层) \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 71. PT9L正式设计输出清单一（Stage 12）中第3项接口板PCB图的全部8个图层条目均引用PT9C-CNTP01 V1.0作为图号，与同清单中主板PCB图使用PT9L-HFMP01前缀形成明显不一致，且文件中无任何共用件声明、设计转换记录或跨型号引用说明，构成正式DHF设计输出清单中的产品身份污染。

- Finding ID：`MR-0071`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据充分：文件为Stage 12 primary_scope=true的正式设计输出清单一，同文件第2项主板PCB图使用PT9L-HFMP01 V1.0图号，而第3项接口板PCB图（共8个图层：Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）全部使用PT9C-CNTP01 V1.0图号。PT9C与PT9L为不同型号前缀，在正式设计输出清单中将PT9C编号的图纸列为PT9L设计输出项目，且无任何共用件受控声明、平台共用说明或设计转换记录，违反设计输出文件的产品身份一致性要求。这不是合理引用或历史来源说明，而是正式受控清单中的实质性图号归属错误，足以构成可确认的DHF文件受控缺陷。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:33` \| 3 \| 接口板PCB图 \| T-Z1-P14 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 72. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0072`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:26` \| 6 \| 防拆签 \| T040800073941030093 \| PET \|  \| PT3-F21 \|  \|  \| PT3 \|  \| 2 \|  \| √ \| C \|  \|  \|

### 73. PT9L包装BOM及总装BOM（Stage 12正式文件）中多个零部件图号归属PT3型号，与MC-CLUSTER-0032形成交叉印证，确认PT9L正式DMR存在PT3零部件身份混入问题。

- Finding ID：`MR-0073`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：本cluster与MC-CLUSTER-0032来源于同一批正式设计输出文件（Stage 12 primary_scope=true），候选证据为PT9L包装BOM（MF-0152）和总装类组件清单PT9L-ABOM01 V1.0（MF-0197/0198/0199）。MF-0152显示防拆签PT3-F21来源型号明确标注为PT3；MF-0197/0198/0199显示双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01均归属PT3。这些零部件在PT9L正式BOM中以PT3图号直接受控，未见共用件声明或PT9L适用性转换记录，构成PT9L DMR产品身份污染的实质证据，与MC-CLUSTER-0032互相印证，应予确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:19` \| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|

### 74. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0074`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 75. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0075`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 76. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0076`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:2` # T040800073941030093-PT3-F21 2D 图读图报告

### 77. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0077`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:4` > 源文件：`T040800073941030093-PT3-F21.pdf`（PDF 尺寸 741×488 pt，文字层字符 < 400，矢量图纸）。

### 78. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0078`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:12` ![T040800073941030093-PT3-F21 概览](_assets/T040800073941030093-PT3-F21/overview.png)

### 79. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0079`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:20` \| **Drawing NO.** \| （待填 - 见右下标题栏） \|

### 80. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0080`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:21` \| **Part name** \| （待填 - 见右下标题栏中文零件名） \|

### 81. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0081`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:22` \| **Pro material** \| （待填） \|

### 82. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0082`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:23` \| **Surf dispose** \| （待填） \|

### 83. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0083`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:24` \| **Scale** \| （待填） \|

### 84. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0084`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:25` \| **Tolerance** \| （待填 - 见标题栏 Tolerance 表） \|

### 85. Stage 12正式设计输出清单二中PT3包装图纸读图报告存在大量关键字段（图号、零件名、材料、表面处理、比例、公差、版次、型号等）均为待填状态，属于正式受控文件内容缺失

- Finding ID：`MR-0085`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。文件T040800073941030093-PT3-F21.pdf.md的标题栏A级字段（Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.）全部标注为'（待填）'，且文件头注释明确标注'2026-05-14 自动生成模板 + 待填'，说明该读图报告从未被人工完成填写。这些字段是图纸受控信息的核心要素，其缺失意味着该设计输出文件实质上处于未完成状态，无法作为有效的设计输出证据，构成实质性受控质量问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:26` \| **Edition** \| （待填） \|

### 86. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0086`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:89` \| ![r0c0](_assets/T040800073941030093-PT3-F21/r0c0.png) \| ![r0c1](_assets/T040800073941030093-PT3-F21/r0c1.png) \|

### 87. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0087`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:90` \| ![r1c0](_assets/T040800073941030093-PT3-F21/r1c0.png) \| ![r1c1](_assets/T040800073941030093-PT3-F21/r1c1.png) \|

### 88. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0088`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:96` - 源 PDF：`T040800073941030093-PT3-F21.pdf`

### 89. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0089`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:97` - 视觉块图：`_assets/T040800073941030093-PT3-F21/`（4 张 PNG，300 DPI）

### 90. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0090`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:6` > **关联**：[疑点表 §4.1](../../../../wiki/drawings/pt9l-2d-audit-doubts.md#41-75cee0-散热器金属套图号-5b44cgxt-001) **75CEE0 黄铜套 2m 跌落要求** 的配合件；[疑点表 §6.3 新增](#疑点新增) 总装图 BOM 编号 13 PT3-M01 = 本图

### 91. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0091`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:28` **iHealth 内部图号映射**：根据 [总装图 BOM](PT9L-总装图-v1.0-20240627.pdf.md) 编号 13，本件在 PT9L BOM 中以 **PT3-M01** 入账（"压块"）。

### 92. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0092`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:98` - **PT9L BOM 中位置**：[总装图序号 13 (PT3-M01)](PT9L-总装图-v1.0-20240627.pdf.md)

### 93. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0093`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:99` - **配合 75CEE0 在 BOM 中位置**：序号 14 (PT3-M03)

### 94. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0094`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:108` \| 2 \| **FDIR-V14 = PT3-M01？**（Famidoc 图号 = iHealth 内部 BOM 号） \| 是 \|

### 95. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0095`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:112` \| 6 \| iHealth 内部是否有"压块"独立图（带 PT3-M01 图号）补归档 \| 推测无 \|

### 96. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0096`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:120` - **设计日期**：2017-06-28（早于 PT9L 项目，PT9L 沿用 PT3 系列散热器组件）

### 97. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0097`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:122` - **供应商**：**Famidoc**（深圳法米德 / 厦门法米德医疗器械有限公司，PT3 散热器组件供应商）

### 98. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0098`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:1` # PT3 双联弹簧 REV01 (V1.0) 2D 图读图报告

### 99. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0099`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT3_双联弹簧_REV01.pdf`

### 100. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0100`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:6` > **共用件**：**PT3 项目原件**，被 PT9L DHF 借用归档（外购件 / 设计参照）

### 101. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0101`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:14` \| **Drawing NO.** \| **PT3-P10** \|

### 102. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0102`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:17` \| **Model NO.** \| **PT3**（注：归档于 PT9L DHF，实为 PT3 项目原件） \|

### 103. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0103`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:80` - 与正极 PT5-M02 / 负极 PT5-M03 **功能等价**，但合二为一（PT3 项目使用，PT9L 借用归档）

### 104. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0104`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:81` - **PT9L 实际装配**：以分离的 PT5-M02 + PT5-M03 为准（详见 wiki 主页 §2.4），PT3-P10 双联弹簧**不一定**进入 PT9L 量产 BOM

### 105. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0105`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:89` \| 1 \| PT9L 量产 BOM 是否使用 PT3-P10 双联弹簧？还是分离的 PT5-M02 + M03？ \| 分离件（PT5 系列） \|

### 106. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0106`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:42` \| 20 \| **PT3-P10** \| **双连弹簧** \| 1 \|

### 107. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0107`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:48` \| 14 \| **PT3-M03** \| **金属套**（=75CEE0 黄铜套？） \| 1 \|

### 108. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0108`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:49` \| 13 \| **PT3-M01** \| **压块**（=散热器压块 FDIR-V14？） \| 1 \|

### 109. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0109`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:74` 6. **散热组**：压块 (13, PT3-M01) + 金属套 (14, PT3-M03)

### 110. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0110`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:77` 9. **电池组**：电池盖 (18, T-Z1-P04) + 7# 碱性电池 × 2 (19) + 双联弹簧 (20, PT3-P10) + 负极弹簧 (21, PT5-M03) + 正极弹簧 (22, PT5-M02) + 螺钉 M2X5 × 3 (23)

### 111. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0111`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:93` \| **图号格式** \| T-Z1-PXX（结构件） / PT3-MXX（散热器 / 双联弹簧借用 PT3） / PT5-MXX（弹簧借用 PT5） / PT9L-LXX（液晶专属） ✓ \|

### 112. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0112`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:108` ### 6.2 金属套（14）= PT3-M03 vs 75CEE0（外购）

### 113. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0113`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:110` - 总装图 BOM 中 **金属套 = PT3-M03**（PT3 项目原件号）

### 114. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0114`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\正极弹簧PT5-M02.pdf.md:96` \| 4 \| 与 PT3 双联弹簧 REV01 的功能区别（PT3 为双联，PT5/PT9L 为分离的正/负 2 件） \| — \|

### 115. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0115`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\负极弹簧PT5-M03.pdf.md:116` - **关联**：[正极弹簧 PT5-M02](正极弹簧PT5-M02.pdf.md)、[PT3 双联弹簧 REV01](PT3_双联弹簧_REV01.pdf.md)、[wiki/drawings/pt9l-drawings.md §2.4](../../../../wiki/drawings/pt9l-drawings.md)

### 116. PT9L包装BOM及总装BOM（Stage 12正式文件）中多个零部件图号归属PT3型号，与MC-CLUSTER-0032形成交叉印证，确认PT9L正式DMR存在PT3零部件身份混入问题。

- Finding ID：`MR-0116`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：本cluster与MC-CLUSTER-0032来源于同一批正式设计输出文件（Stage 12 primary_scope=true），候选证据为PT9L包装BOM（MF-0152）和总装类组件清单PT9L-ABOM01 V1.0（MF-0197/0198/0199）。MF-0152显示防拆签PT3-F21来源型号明确标注为PT3；MF-0197/0198/0199显示双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01均归属PT3。这些零部件在PT9L正式BOM中以PT3图号直接受控，未见共用件声明或PT9L适用性转换记录，构成PT9L DMR产品身份污染的实质证据，与MC-CLUSTER-0032互相印证，应予确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28` \| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|

### 117. PT9L包装BOM及总装BOM（Stage 12正式文件）中多个零部件图号归属PT3型号，与MC-CLUSTER-0032形成交叉印证，确认PT9L正式DMR存在PT3零部件身份混入问题。

- Finding ID：`MR-0117`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：本cluster与MC-CLUSTER-0032来源于同一批正式设计输出文件（Stage 12 primary_scope=true），候选证据为PT9L包装BOM（MF-0152）和总装类组件清单PT9L-ABOM01 V1.0（MF-0197/0198/0199）。MF-0152显示防拆签PT3-F21来源型号明确标注为PT3；MF-0197/0198/0199显示双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01均归属PT3。这些零部件在PT9L正式BOM中以PT3图号直接受控，未见共用件声明或PT9L适用性转换记录，构成PT9L DMR产品身份污染的实质证据，与MC-CLUSTER-0032互相印证，应予确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35` \| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|

### 118. PT9L包装BOM及总装BOM（Stage 12正式文件）中多个零部件图号归属PT3型号，与MC-CLUSTER-0032形成交叉印证，确认PT9L正式DMR存在PT3零部件身份混入问题。

- Finding ID：`MR-0118`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：本cluster与MC-CLUSTER-0032来源于同一批正式设计输出文件（Stage 12 primary_scope=true），候选证据为PT9L包装BOM（MF-0152）和总装类组件清单PT9L-ABOM01 V1.0（MF-0197/0198/0199）。MF-0152显示防拆签PT3-F21来源型号明确标注为PT3；MF-0197/0198/0199显示双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01均归属PT3。这些零部件在PT9L正式BOM中以PT3图号直接受控，未见共用件声明或PT9L适用性转换记录，构成PT9L DMR产品身份污染的实质证据，与MC-CLUSTER-0032互相印证，应予确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36` \| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|

### 119. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0119`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:35` \| 15 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 120. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0120`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:38` \| 18 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 121. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0121`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:39` \| 19 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 122. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0122`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:63` \| 32 \| PT3总装类组件清单 \| PT9L-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 123. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0123`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:139` \| 14 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 124. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0124`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:147` \| 22 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 125. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0125`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:148` \| 23 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 126. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0126`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:173` \| 38 \| 防拆签 \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 127. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0127`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:185` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 128. Stage 12正式设计输出清单二中PT3SBT型号页的提交、审核、批准日期签署栏全部空白，属于正式受控文件签署缺失

- Finding ID：`MR-0128`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。两个候选（MF-0211来自子目录版本，MF-0226来自根目录版本）均显示'产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日 批准: 年 月 日'，三处签署日期栏均为空白（仅保留'年 月 日'占位符）。该Sheet标注为'PT3参考'，但文件本身位于正式设计输出清单二中，且PT3SBT作为参考型号出现在PT9L设计输出清单内，其签署状态直接影响文件的受控有效性。提交/审核/批准签署缺失是文件受控的基本要求，构成实质性合规问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:237` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日

### 129. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0129`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:261` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 130. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0130`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:262` \| 15 \| 胶垫 \| PT3SBT-P02 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 131. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0131`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:270` \| 19 \| 装配说明 \| PT3SBT（国内）-ZPSM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 132. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0132`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:291` \| 33 \| PT3总装类组件清单 \| PT3SBT-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 133. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0133`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:293` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 134. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0134`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:35` \| 15 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 135. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0135`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:38` \| 18 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 136. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0136`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:39` \| 19 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 137. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0137`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:56` \| 28 \| 防拆签 \|  \|  \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 138. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0138`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:141` \| 14 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 139. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0139`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:149` \| 22 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 140. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0140`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:150` \| 23 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 141. PT9L正式设计输出清单二（BOM及设计输出清单）中多处将零部件来源型号标注为PT3，包括防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等，构成PT9L正式DMR中的产品身份混用，需提供共用件受控依据。

- Finding ID：`MR-0141`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件均位于Stage 12 primary_scope=true的正式设计输出范围，包括PT9L包装BOM（PT9L包装BOM.via_xlsx）和总装类组件清单（PT9L-ABOM01 V1.0）以及设计输出清单二（设计输出清单二E0）。证据显示：①PT9L包装BOM第6行防拆签（T040800073941030093）图号PT3-F21、来源型号PT3；②总装BOM第15行双联弹簧（T030100000482550143）图号PT3-P10、来源PT3；③总装BOM第22行金属套（T030100000507180765）图号PT3-M02、来源PT3；④总装BOM第23行压块（T030100000497180765）图号PT3-M01、来源PT3。上述零部件在PT9L正式DMR的BOM中以PT3型号图号直接列入，未见PT9L专属图号或共用件转换说明。这属于正式设计输出文件中的产品身份混用，影响PT9L DMR的完整性和可追溯性，构成实质性合规问题。同一BOM中还出现PT1-F07（外箱条码标签来源PT1），进一步表明该BOM存在系统性跨型号零部件身份混用问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:175` \| 38 \| 防拆签 \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 142. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0142`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 143. Stage 12正式设计输出清单二中PT3SBT型号页的提交、审核、批准日期签署栏全部空白，属于正式受控文件签署缺失

- Finding ID：`MR-0143`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12设计输出清单二，primary_scope=true，属于正式主审范围。两个候选（MF-0211来自子目录版本，MF-0226来自根目录版本）均显示'产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日 批准: 年 月 日'，三处签署日期栏均为空白（仅保留'年 月 日'占位符）。该Sheet标注为'PT3参考'，但文件本身位于正式设计输出清单二中，且PT3SBT作为参考型号出现在PT9L设计输出清单内，其签署状态直接影响文件的受控有效性。提交/审核/批准签署缺失是文件受控的基本要求，构成实质性合规问题。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日

### 144. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0144`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 145. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0145`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:264` \| 15 \| 胶垫 \| PT3SBT-P02 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 146. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0146`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:272` \| 19 \| 装配说明 \| PT3SBT（国内）-ZPSM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 147. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0147`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:293` \| 33 \| PT3总装类组件清单 \| PT3SBT-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 148. PT9L设计输出清单二（Stage 12正式文件）中包含PT3SBT产品的完整BOM文件编号（PT3SBT-PBOM01、PT3SBT-ABOM01）及专属零部件（PT3SBT-P01收纳盒、PT3SBT-P02胶垫、PT3SBT装配说明），属于异型号产品文件实质性混入PT9L正式DHF，构成严重产品身份污染。

- Finding ID：`MR-0148`
- 二审 Agent：Product Identity Agent
- 严重度：`P0`
- 二审理由：文件为Stage 12 primary_scope=true的设计输出清单二E0（两个路径版本均命中），属于PT9L正式DHF核心文件。证据显示：①MF-0210/MF-0225：清单第34项'PT3包装类组件清单'文件编号为PT3SBT-PBOM01 V1.0，该编号前缀为PT3SBT而非PT9L；②MF-0215：清单第33项'PT3总装类组件清单'文件编号为PT3SBT-ABOM01 V1.0；③MF-0212/MF-0227：零部件第14项'收纳盒'编号PT3SBT-P01 V1.0；④MF-0213：零部件第15项'胶垫'编号PT3SBT-P02 V1.0；⑤MF-0214：装配说明编号PT3SBT（国内）-ZPSM01 V1.0。上述条目均以PT3SBT为产品前缀，出现在PT9L设计输出清单二的正式受控列表中，说明PT3SBT产品的设计输出文件被纳入PT9L DHF管理范围，或PT9L设计输出清单二实际上是PT3SBT的文件而非PT9L专属文件。无论哪种情形，均构成P0级产品身份污染：若该清单确为PT9L文件，则PT3SBT文件混入PT9L DHF；若该清单实为PT3SBT文件，则Stage 12中存在错误归档。需立即核查该设计输出清单二的产品归属及文件受控状态。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:295` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 149. Stage 18正式设计确认文件中存在PT9C型号身份污染，文件标题直接命名为PT9C，且用户测试计划标题亦为PT9C，但文件编号显示PT9L-RYCJ01，存在型号不一致问题。

- Finding ID：`MR-0149`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0232所在文件路径为'18 设计确认\\PT9C设计确认E0 23.11.via_xlsx.clean.md'，文件标题为'PT9C设计确认E0 23.11'，属于Stage 18正式设计确认范围（primary_scope=true），文件名及标题均以PT9C命名而非PT9L，构成产品身份污染。MF-0276所在文件'用户现场测试计划 PT9C V1.0'标题为PT9C，但文件编号'PT9L-RYCJ01 V1.0'指向PT9L，型号标识前后矛盾，说明该文件系由PT9C版本改版而来但标题未同步更新，属于正式DHF文件中的产品身份不一致问题，需要确认文件是否已正式受控并完成型号更正。
- 证据：
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:2` # PT9C设计确认E0  23.11

### 150. Stage 18正式设计确认目录中存在文件标题同时含PT9L与PT2L的checklist（PT9L Checklist of EN 60601-1-6... PT2L（美亚）-UETR01 V1.0），源路径显示该文件来自'PT9L DHF-历史文件'子目录，PT2L在DHF中有独立的历史型号风险管理文件系列，表明该文件为PT2L历史型号文件被混入PT9L正式Stage 18设计确认目录，构成产品身份混用及历史文件混入正式DHF的文件受控缺陷。

- Finding ID：`MR-0150`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据足以确认：①文件标题明确包含'PT2L（美亚）'，PT2L在DHF中有独立的风险管理文件系列（03风险分析/2L风险改-历史文件/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0等），说明PT2L是独立的历史型号而非PT9L的子型号别名；②MF-0236来源路径明确为'02_RnD_DHF/PT9L DHF-历史文件/设计确认/...'，表明该文件原属历史文件目录；③该文件现位于Stage 18正式设计确认目录（primary_scope=true），属于历史型号文件混入正式DHF设计确认阶段；④文件编号DN为PT9L-UETR01 V1.0，但文件内容针对PT2L美亚型号，存在文件编号与实际适用型号不一致的双重问题。综合以上，当前证据足以证明这是正式DHF中的产品身份混用及文件受控缺陷。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:3` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0

### 151. Stage 18正式设计确认目录中存在文件标题同时含PT9L与PT2L的checklist（PT9L Checklist of EN 60601-1-6... PT2L（美亚）-UETR01 V1.0），源路径显示该文件来自'PT9L DHF-历史文件'子目录，PT2L在DHF中有独立的历史型号风险管理文件系列，表明该文件为PT2L历史型号文件被混入PT9L正式Stage 18设计确认目录，构成产品身份混用及历史文件混入正式DHF的文件受控缺陷。

- Finding ID：`MR-0151`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据足以确认：①文件标题明确包含'PT2L（美亚）'，PT2L在DHF中有独立的风险管理文件系列（03风险分析/2L风险改-历史文件/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0等），说明PT2L是独立的历史型号而非PT9L的子型号别名；②MF-0236来源路径明确为'02_RnD_DHF/PT9L DHF-历史文件/设计确认/...'，表明该文件原属历史文件目录；③该文件现位于Stage 18正式设计确认目录（primary_scope=true），属于历史型号文件混入正式DHF设计确认阶段；④文件编号DN为PT9L-UETR01 V1.0，但文件内容针对PT2L美亚型号，存在文件编号与实际适用型号不一致的双重问题。综合以上，当前证据足以证明这是正式DHF中的产品身份混用及文件受控缺陷。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:14` ![第 1 页原始整页图](_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_1.png)

### 152. Stage 18正式设计确认目录中存在文件标题同时含PT9L与PT2L的checklist（PT9L Checklist of EN 60601-1-6... PT2L（美亚）-UETR01 V1.0），源路径显示该文件来自'PT9L DHF-历史文件'子目录，PT2L在DHF中有独立的历史型号风险管理文件系列，表明该文件为PT2L历史型号文件被混入PT9L正式Stage 18设计确认目录，构成产品身份混用及历史文件混入正式DHF的文件受控缺陷。

- Finding ID：`MR-0152`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据足以确认：①文件标题明确包含'PT2L（美亚）'，PT2L在DHF中有独立的风险管理文件系列（03风险分析/2L风险改-历史文件/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0等），说明PT2L是独立的历史型号而非PT9L的子型号别名；②MF-0236来源路径明确为'02_RnD_DHF/PT9L DHF-历史文件/设计确认/...'，表明该文件原属历史文件目录；③该文件现位于Stage 18正式设计确认目录（primary_scope=true），属于历史型号文件混入正式DHF设计确认阶段；④文件编号DN为PT9L-UETR01 V1.0，但文件内容针对PT2L美亚型号，存在文件编号与实际适用型号不一致的双重问题。综合以上，当前证据足以证明这是正式DHF中的产品身份混用及文件受控缺陷。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:88` ![第 3 页原始整页图](_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_3.png)

### 153. Stage 18正式设计确认目录中存在文件标题同时含PT9L与PT2L的checklist（PT9L Checklist of EN 60601-1-6... PT2L（美亚）-UETR01 V1.0），源路径显示该文件来自'PT9L DHF-历史文件'子目录，PT2L在DHF中有独立的历史型号风险管理文件系列，表明该文件为PT2L历史型号文件被混入PT9L正式Stage 18设计确认目录，构成产品身份混用及历史文件混入正式DHF的文件受控缺陷。

- Finding ID：`MR-0153`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据足以确认：①文件标题明确包含'PT2L（美亚）'，PT2L在DHF中有独立的风险管理文件系列（03风险分析/2L风险改-历史文件/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0等），说明PT2L是独立的历史型号而非PT9L的子型号别名；②MF-0236来源路径明确为'02_RnD_DHF/PT9L DHF-历史文件/设计确认/...'，表明该文件原属历史文件目录；③该文件现位于Stage 18正式设计确认目录（primary_scope=true），属于历史型号文件混入正式DHF设计确认阶段；④文件编号DN为PT9L-UETR01 V1.0，但文件内容针对PT2L美亚型号，存在文件编号与实际适用型号不一致的双重问题。综合以上，当前证据足以证明这是正式DHF中的产品身份混用及文件受控缺陷。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:113` - 源 PDF：`02_RnD_DHF/PT9L DHF-历史文件/设计确认/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf`

### 154. Stage 18正式设计确认目录中存在文件标题同时含PT9L与PT2L的checklist（PT9L Checklist of EN 60601-1-6... PT2L（美亚）-UETR01 V1.0），源路径显示该文件来自'PT9L DHF-历史文件'子目录，PT2L在DHF中有独立的历史型号风险管理文件系列，表明该文件为PT2L历史型号文件被混入PT9L正式Stage 18设计确认目录，构成产品身份混用及历史文件混入正式DHF的文件受控缺陷。

- Finding ID：`MR-0154`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：证据足以确认：①文件标题明确包含'PT2L（美亚）'，PT2L在DHF中有独立的风险管理文件系列（03风险分析/2L风险改-历史文件/V1.0-1 Risk Management Plan PT2L美亚-FXJH01 V1.0等），说明PT2L是独立的历史型号而非PT9L的子型号别名；②MF-0236来源路径明确为'02_RnD_DHF/PT9L DHF-历史文件/设计确认/...'，表明该文件原属历史文件目录；③该文件现位于Stage 18正式设计确认目录（primary_scope=true），属于历史型号文件混入正式DHF设计确认阶段；④文件编号DN为PT9L-UETR01 V1.0，但文件内容针对PT2L美亚型号，存在文件编号与实际适用型号不一致的双重问题。综合以上，当前证据足以证明这是正式DHF中的产品身份混用及文件受控缺陷。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:114` - 证据原图（签字/盖章/照片页）：`_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_*.png`

### 155. Stage 18正式设计确认目录中的checklist（via_lo_html转换版本）标题同时含PT9L与PT2L，与MC-CLUSTER-0040为同一文件的不同转换版本，同样构成PT2L历史型号文件混入PT9L正式DHF设计确认阶段的产品身份混用及文件受控缺陷。

- Finding ID：`MR-0155`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0238与MC-CLUSTER-0040所涉文件为同一原始文件的不同格式转换版本（via_lo_html vs PDF），文件标题、文件编号DN（PT9L-UETR01 V1.0）及PT2L（美亚）标注完全一致，位于同一Stage 18正式设计确认目录（primary_scope=true）。基于MC-CLUSTER-0040的裁决逻辑，PT2L为独立历史型号，该文件属于历史型号文件混入正式DHF，构成相同性质的产品身份混用及文件受控缺陷。两个cluster为同一问题的两个证据实例，均应confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.via_lo_html.clean.md:2` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0

### 156. Stage 18正式设计确认文件中存在PT9C型号身份污染，文件标题直接命名为PT9C，且用户测试计划标题亦为PT9C，但文件编号显示PT9L-RYCJ01，存在型号不一致问题。

- Finding ID：`MR-0156`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0232所在文件路径为'18 设计确认\\PT9C设计确认E0 23.11.via_xlsx.clean.md'，文件标题为'PT9C设计确认E0 23.11'，属于Stage 18正式设计确认范围（primary_scope=true），文件名及标题均以PT9C命名而非PT9L，构成产品身份污染。MF-0276所在文件'用户现场测试计划 PT9C V1.0'标题为PT9C，但文件编号'PT9L-RYCJ01 V1.0'指向PT9L，型号标识前后矛盾，说明该文件系由PT9C版本改版而来但标题未同步更新，属于正式DHF文件中的产品身份不一致问题，需要确认文件是否已正式受控并完成型号更正。
- 证据：
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:2` # 用户现场测试计划 PT9C V1.0

### 157. 正式DHF清单（PT9L-DHF清单-常规）第92行设计输出条目中出现"PT9C"字样，疑为异型号身份污染

- Finding ID：`MR-0157`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：该文件路径为PT9L-DHF清单-常规.via_xlsx.clean.md，primary_scope=true，属于正式受控DHF清单。第92行"设计输出清单一（PT9L-SJSC01 V1.0）"对应列中填写了"PT9C"，该列在上下文中并非文档编号或来源引用字段，而是与设计输出条目并列的属性字段，疑似将PT9C作为该设计输出的关联型号或来源型号填入。PT9L与PT9C为不同型号，在正式DHF清单中出现异型号标注，构成产品身份污染风险，需进一步核查该列含义及PT9C与PT9L的关系是否有受控说明。
- 证据：
  - `PT9L-DHF清单-常规.via_xlsx.clean.md:92` \| 设计输出 \| 82 \| 设计输出清单一 \| PT9L-SJSC01 V1.0 \|  \| 2024.4.20 \| PT9C \| 是 \|  \| 时间未定 \|

### 158. PT9结构DHF主审范围内存在以"血压计"命名的结构设计方案评审检查表，构成品类身份污染

- Finding ID：`MR-0158`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径为PT9结构DHF\\5E0版结构方案阶段 23.11\\结构设计方案评审检查表-血压计E0 23.11，primary_scope=true，属于正式DHF主审范围。文件标题直接以"血压计"命名，PT9L为红外体温计，与血压计属于不同品类医疗器械。在PT9L正式结构DHF目录下存在血压计评审检查表，说明该文件可能被错误纳入PT9L DHF，或文件命名存在严重错误，构成品类身份污染，影响DHF完整性与合规性，需核查该文件是否应属于PT9L DHF范围及其内容是否与PT9L相关。
- 证据：
  - `PT9结构DHF\5E0版结构方案阶段 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2` # 结构设计方案评审检查表-血压计E0 23.11

### 159. PT9L 正式外部测试报告（ETX202303-07-078-03）中，ISO 14971 各条款（4.2、4.3、4.4、5、6.4）符合性验证表统一引用风险管理报告文件编号 PT9C-FXGB01 V1.0，文件编号前缀 PT9C 与受审产品型号 PT9L 不符，构成跨型号风险管理文件引用缺陷，风险管理合规证据链存在产品身份标识不一致。

- Finding ID：`MR-0159`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据显示：①该正式外部测试报告文件名明确标注受审产品为 PT9L（ETX202303-07-078-03 PT9L -2-56 报告-正式），属于 primary scope；②在 ISO 14971 符合性验证表的全部5处引用（条款4.2、4.3、4.4、5、6.4）中，文件编号均为 PT9C-FXGB01 V1.0，前缀 PT9C 与 PT9L 存在明确型号差异；③报告内部及周边上下文中无任何共用件声明、平台文件标注或适用性说明；④same_term 统计显示 PT9C 在 primary scope 中出现19次，但均无法从现有证据中确认存在正式的跨型号适用性授权文件。在正式外部测试报告的 ISO 14971 合规证据链中，风险管理报告是核心支撑文件，其文件编号与受审产品型号不一致，直接导致该报告的合规证据链完整性存疑。这属于可确认的产品身份标识不一致缺陷（cross_model_risk_document_reference），而非仅凭怀疑的推断。依据最终裁决政策，当前证据足以证明正式主审范围内存在文件受控缺陷及法规/一致性缺陷，裁决为 confirm，定级 P1。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|

### 160. PT9L 正式外部测试报告（ETX202303-07-078-03）中，ISO 14971 各条款（4.2、4.3、4.4、5、6.4）符合性验证表统一引用风险管理报告文件编号 PT9C-FXGB01 V1.0，文件编号前缀 PT9C 与受审产品型号 PT9L 不符，构成跨型号风险管理文件引用缺陷，风险管理合规证据链存在产品身份标识不一致。

- Finding ID：`MR-0160`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据显示：①该正式外部测试报告文件名明确标注受审产品为 PT9L（ETX202303-07-078-03 PT9L -2-56 报告-正式），属于 primary scope；②在 ISO 14971 符合性验证表的全部5处引用（条款4.2、4.3、4.4、5、6.4）中，文件编号均为 PT9C-FXGB01 V1.0，前缀 PT9C 与 PT9L 存在明确型号差异；③报告内部及周边上下文中无任何共用件声明、平台文件标注或适用性说明；④same_term 统计显示 PT9C 在 primary scope 中出现19次，但均无法从现有证据中确认存在正式的跨型号适用性授权文件。在正式外部测试报告的 ISO 14971 合规证据链中，风险管理报告是核心支撑文件，其文件编号与受审产品型号不一致，直接导致该报告的合规证据链完整性存疑。这属于可确认的产品身份标识不一致缺陷（cross_model_risk_document_reference），而非仅凭怀疑的推断。依据最终裁决政策，当前证据足以证明正式主审范围内存在文件受控缺陷及法规/一致性缺陷，裁决为 confirm，定级 P1。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:578` \| 4.3 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Hazard analysis recorded \| P \|

### 161. PT9L 正式外部测试报告（ETX202303-07-078-03）中，ISO 14971 各条款（4.2、4.3、4.4、5、6.4）符合性验证表统一引用风险管理报告文件编号 PT9C-FXGB01 V1.0，文件编号前缀 PT9C 与受审产品型号 PT9L 不符，构成跨型号风险管理文件引用缺陷，风险管理合规证据链存在产品身份标识不一致。

- Finding ID：`MR-0161`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据显示：①该正式外部测试报告文件名明确标注受审产品为 PT9L（ETX202303-07-078-03 PT9L -2-56 报告-正式），属于 primary scope；②在 ISO 14971 符合性验证表的全部5处引用（条款4.2、4.3、4.4、5、6.4）中，文件编号均为 PT9C-FXGB01 V1.0，前缀 PT9C 与 PT9L 存在明确型号差异；③报告内部及周边上下文中无任何共用件声明、平台文件标注或适用性说明；④same_term 统计显示 PT9C 在 primary scope 中出现19次，但均无法从现有证据中确认存在正式的跨型号适用性授权文件。在正式外部测试报告的 ISO 14971 合规证据链中，风险管理报告是核心支撑文件，其文件编号与受审产品型号不一致，直接导致该报告的合规证据链完整性存疑。这属于可确认的产品身份标识不一致缺陷（cross_model_risk_document_reference），而非仅凭怀疑的推断。依据最终裁决政策，当前证据足以证明正式主审范围内存在文件受控缺陷及法规/一致性缺陷，裁决为 confirm，定级 P1。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:579` \| 4.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk estimation recorded \| P \|

### 162. PT9L 正式外部测试报告（ETX202303-07-078-03）中，ISO 14971 各条款（4.2、4.3、4.4、5、6.4）符合性验证表统一引用风险管理报告文件编号 PT9C-FXGB01 V1.0，文件编号前缀 PT9C 与受审产品型号 PT9L 不符，构成跨型号风险管理文件引用缺陷，风险管理合规证据链存在产品身份标识不一致。

- Finding ID：`MR-0162`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据显示：①该正式外部测试报告文件名明确标注受审产品为 PT9L（ETX202303-07-078-03 PT9L -2-56 报告-正式），属于 primary scope；②在 ISO 14971 符合性验证表的全部5处引用（条款4.2、4.3、4.4、5、6.4）中，文件编号均为 PT9C-FXGB01 V1.0，前缀 PT9C 与 PT9L 存在明确型号差异；③报告内部及周边上下文中无任何共用件声明、平台文件标注或适用性说明；④same_term 统计显示 PT9C 在 primary scope 中出现19次，但均无法从现有证据中确认存在正式的跨型号适用性授权文件。在正式外部测试报告的 ISO 14971 合规证据链中，风险管理报告是核心支撑文件，其文件编号与受审产品型号不一致，直接导致该报告的合规证据链完整性存疑。这属于可确认的产品身份标识不一致缺陷（cross_model_risk_document_reference），而非仅凭怀疑的推断。依据最终裁决政策，当前证据足以证明正式主审范围内存在文件受控缺陷及法规/一致性缺陷，裁决为 confirm，定级 P1。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:580` \| 5 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk evaluation recorded \| P \|

### 163. PT9L 正式外部测试报告（ETX202303-07-078-03）中，ISO 14971 各条款（4.2、4.3、4.4、5、6.4）符合性验证表统一引用风险管理报告文件编号 PT9C-FXGB01 V1.0，文件编号前缀 PT9C 与受审产品型号 PT9L 不符，构成跨型号风险管理文件引用缺陷，风险管理合规证据链存在产品身份标识不一致。

- Finding ID：`MR-0163`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据显示：①该正式外部测试报告文件名明确标注受审产品为 PT9L（ETX202303-07-078-03 PT9L -2-56 报告-正式），属于 primary scope；②在 ISO 14971 符合性验证表的全部5处引用（条款4.2、4.3、4.4、5、6.4）中，文件编号均为 PT9C-FXGB01 V1.0，前缀 PT9C 与 PT9L 存在明确型号差异；③报告内部及周边上下文中无任何共用件声明、平台文件标注或适用性说明；④same_term 统计显示 PT9C 在 primary scope 中出现19次，但均无法从现有证据中确认存在正式的跨型号适用性授权文件。在正式外部测试报告的 ISO 14971 合规证据链中，风险管理报告是核心支撑文件，其文件编号与受审产品型号不一致，直接导致该报告的合规证据链完整性存疑。这属于可确认的产品身份标识不一致缺陷（cross_model_risk_document_reference），而非仅凭怀疑的推断。依据最终裁决政策，当前证据足以证明正式主审范围内存在文件受控缺陷及法规/一致性缺陷，裁决为 confirm，定级 P1。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:581` \| 6.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Residual risk evaluated. \| P \|

### 164. Stage 01客户需求书文件标题含"血压计"，但内容为红外额温计规格，产品品类标签与实际内容不符，构成产品身份污染。

- Finding ID：`MR-0164`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径及标题均为"客户需求书E0-血压计 23.6"，但PF-0001至PF-0003的内容明确描述温度显示范围32.0℃～42.9℃、红外测温方式测量人体额头温度等额温计特征参数，与血压计品类完全不符。PF-0003第81行明确写明"本品主要采用红外测温方式测量人体额头温度"。文件标题"血压计"系品类标签错误，该文件作为PT9L DHF Stage 01正式立项文件，标题与内容的品类不一致会导致产品身份证据链混乱，需正式更正文件标题或补充说明。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:104` \| 3 \| 测量误差 \| ≥35℃且≤42℃：±0.2℃，其它：±0.3℃ \|  \|

### 165. Stage 01客户需求书文件标题含"血压计"，但内容为红外额温计规格，产品品类标签与实际内容不符，构成产品身份污染。

- Finding ID：`MR-0165`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径及标题均为"客户需求书E0-血压计 23.6"，但PF-0001至PF-0003的内容明确描述温度显示范围32.0℃～42.9℃、红外测温方式测量人体额头温度等额温计特征参数，与血压计品类完全不符。PF-0003第81行明确写明"本品主要采用红外测温方式测量人体额头温度"。文件标题"血压计"系品类标签错误，该文件作为PT9L DHF Stage 01正式立项文件，标题与内容的品类不一致会导致产品身份证据链混乱，需正式更正文件标题或补充说明。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:132` \| 11 \| 错误分类显示 \| □No \| ■错误种类：2种 （1、超出工作环境温度 2、超过量程 ） \|  \|  \|  \|

### 166. Stage 01客户需求书文件标题含"血压计"，但内容为红外额温计规格，产品品类标签与实际内容不符，构成产品身份污染。

- Finding ID：`MR-0166`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径及标题均为"客户需求书E0-血压计 23.6"，但PF-0001至PF-0003的内容明确描述温度显示范围32.0℃～42.9℃、红外测温方式测量人体额头温度等额温计特征参数，与血压计品类完全不符。PF-0003第81行明确写明"本品主要采用红外测温方式测量人体额头温度"。文件标题"血压计"系品类标签错误，该文件作为PT9L DHF Stage 01正式立项文件，标题与内容的品类不一致会导致产品身份证据链混乱，需正式更正文件标题或补充说明。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:85` \| 8 \| 产品寿命 \| 见附件3：《客户需求书－性能规格部分》V1.0 \|  \|  \|

### 167. Stage 01客户需求书文件标题含"血压计"，但内容为红外额温计规格，产品品类标签与实际内容不符，构成产品身份污染。

- Finding ID：`MR-0167`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：文件路径及标题均为"客户需求书E0-血压计 23.6"，但PF-0001至PF-0003的内容明确描述温度显示范围32.0℃～42.9℃、红外测温方式测量人体额头温度等额温计特征参数，与血压计品类完全不符。PF-0003第81行明确写明"本品主要采用红外测温方式测量人体额头温度"。文件标题"血压计"系品类标签错误，该文件作为PT9L DHF Stage 01正式立项文件，标题与内容的品类不一致会导致产品身份证据链混乱，需正式更正文件标题或补充说明。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:6` ## Sheet: 历史版本记录
