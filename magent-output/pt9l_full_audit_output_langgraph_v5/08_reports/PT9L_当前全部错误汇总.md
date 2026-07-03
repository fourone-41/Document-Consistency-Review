# PT9L 当前全部错误汇总

> 生成时间：2026-06-25T16:59:03
> 数据来源：`pt9l_full_audit_output_langgraph_v5`。机械候选已经过一轮多 Agent LLM 复审和二轮补证据最终裁决。

## 1. 总览

- 全量 Markdown 文件：470
- 当前确认错误总数：71 项（按机械 cluster 去重 + 语义 finding 计数）
- 机械确认错误：21 类，对应候选行 156 条
- 机械判定非错误：328 条候选；机械未决：0 条
- 语义确认/修订错误：50 条（keep 31，revise 19）
- 语义仍需人工补证疑点：16 条；已丢弃语义误报：1 条

说明：`confirm/keep/revise` 进入本汇总主清单；`needs_more_context` 不算已确认错误，但单独列在第 7 节，便于继续人工复核。

## 2. 严重度统计（确认错误）

| 严重度 | 数量 |
|---|---:|
| P1 | 33 |
| P2 | 26 |
| P3 | 12 |

## 3. 来源统计（确认错误）

| 来源 | 数量 |
|---|---:|
| 语义审查确认/修订错误 | 50 |
| 机械复审确认错误 | 21 |

## 4. Agent 统计（确认错误）

| Agent | 数量 |
|---|---:|
| Product Identity Agent | 12 |
| Regulatory Agent | 9 |
| Software Agent | 9 |
| Market & Category Scout Agent | 8 |
| Risk Traceability Agent | 8 |
| Document Control Agent | 7 |
| Hardware Agent | 7 |
| V&V Agent | 6 |
| DMR/SOP Agent | 5 |

## 5. 机械复审确认错误（按 Cluster 去重）

### M001. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Cluster：`MC-CLUSTER-0071`
- 严重度：`P1`
- Agent：Regulatory Agent
- 类型：`wrong_model_reference_in_risk_management_evidence`
- 阶段/术语：External Test / `PT9C`
- 涉及候选行数：5
- 裁决理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 代表证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|

### M002. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Cluster：`MC-CLUSTER-0009`
- 严重度：`P1`
- Agent：Document Control Agent
- 类型：`unfilled_template_fields_in_controlled_document`
- 阶段/术语：Stage 06 / `模板`
- 涉及候选行数：9
- 裁决理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 代表证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### M003. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Cluster：`MC-CLUSTER-0011`
- 严重度：`P1`
- Agent：Product Identity Agent
- 类型：`legacy_model_id_residual_in_formal_document`
- 阶段/术语：Stage 07 / `BP3L`
- 涉及候选行数：8
- 裁决理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 代表证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11

### M004. Stage 11 DFMEA文件中FMEA编号含"XXXX"占位符（KD-XXXX-PDFM01 V1.0、KD-XXXX-ODFM01 V1.0），且产品型号字段填写为KD-5915L而非PT9L，存在文件编号未受控及型号不符的双重质量问题。

- Cluster：`MC-CLUSTER-0013`
- 严重度：`P1`
- Agent：Document Control Agent
- 类型：`unfilled_document_number_placeholder_and_wrong_model_number`
- 阶段/术语：Stage 11 / `XXX`
- 涉及候选行数：2
- 裁决理由：该文件位于Stage 11主审范围（primary_scope=true），为结构类FMEA正式文件。FMEA编号中的"XXXX"是明确的占位符，表明文件编号未被正式分配，违反受控文件编号唯一性要求。同时，产品型号字段填写为KD-5915L，而本DHF/DMR审查对象为PT9L，型号不符可能意味着该FMEA文件是从其他产品模板复制而来且未完成适配，或存在错误引用。FMEA编号未受控直接影响设计风险分析的可追溯性，型号不符影响证据链的归属确认，两者叠加构成P1级问题。
- 代表证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:12` \| \| 分类： \| 包装类 \| \| \| 编制人： \| \| \| \| \| \| \| \| \| FMEA编号：KD-XXXX-PDFM01 V1.0 \| \| \| \| \| \| \| \|

### M005. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Cluster：`MC-CLUSTER-0017`
- 严重度：`P1`
- Agent：Regulatory Agent
- 类型：`wrong_model_reference_in_label_review`
- 阶段/术语：Stage 11 / `PT3SBT`
- 涉及候选行数：24
- 裁决理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 代表证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）

### M006. PT3SBT标签审核表（Stage 11正式文件）中包含PT2L（美亚）和PT9L的标签检查报告模板，所有Sheet的拟制、审核、检查签署日期均为空白（"年月日"占位符），且文件名含PT3SBT与内容型号不一致，属于标签审核文件未完成签署及型号标识混乱的受控质量问题。

- Cluster：`MC-CLUSTER-0018`
- 严重度：`P1`
- Agent：Document Control Agent
- 类型：`unsigned_label_review_template_with_wrong_model_reference`
- 阶段/术语：Stage 11 / `PT3SBT`
- 涉及候选行数：4
- 裁决理由：该文件位于Stage 11主审范围（primary_scope=true），文件名为PT3SBT标签审核表，但内容中Sheet"标签报告模板-美"对应PT2L（美亚），Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"对应PT9L，文件名与部分内容型号不一致，存在型号混用风险。更关键的是，所有Sheet中的拟制、审核、检查签署日期均为"年月日"空白占位符，表明标签审核活动从未被正式签署确认。标签审核表是医疗器械上市前的重要合规文件，签署缺失意味着审核活动无法被证明已实际执行，构成P1级受控合规问题。
- 代表证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:6` ## Sheet: 标签报告模板 -美

### M007. PT9L正式BOM（EBOM和T1样机BOM）中PCB图号引用了PT9C型号编号（PT9C-CNTP01 V1.0），构成异型号零件编号污染受控BOM。

- Cluster：`MC-CLUSTER-0020`
- 严重度：`P1`
- Agent：Product Identity Agent
- 类型：`cross_model_part_number_in_bom`
- 阶段/术语：Stage 11 / `PT9C`
- 涉及候选行数：2
- 裁决理由：MF-0095和MF-0096均为primary_scope=true的正式受控BOM文件（PT9L-EBOM01 V1.0和PT9L-T1EB01 V1.0），两份文件第50行均出现PCB图号"PT9C-CNTP01 V1.0"，该图号前缀明确为PT9C而非PT9L。在正式受控BOM中，零件图号应与目标产品型号一致或有明确的共用件说明。当前证据中无任何共用件声明或跨型号引用说明，属于异型号编号直接写入PT9L正式BOM，影响产品身份证据链完整性，应予confirm。
- 代表证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \| \| \| 1 \| PCB \| √ \| C \| \| \|

### M008. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Cluster：`MC-CLUSTER-0034`
- 严重度：`P1`
- Agent：Document Control Agent
- 类型：`unfilled_required_fields_in_design_output`
- 阶段/术语：Stage 12 / `PT3`
- 涉及候选行数：9
- 裁决理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 代表证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### M009. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Cluster：`MC-CLUSTER-0037`
- 严重度：`P1`
- Agent：Product Identity Agent
- 类型：`foreign_product_identity_in_design_output`
- 阶段/术语：Stage 12 / `PT3SBT`
- 涉及候选行数：12
- 裁决理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 代表证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:185` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \| \| \| \| \| \| \| \| \| \| \| \| \|

### M010. Stage 12主审范围设计输出清单二中PT3SBT参考Sheet的提交、审核、批准日期及签署全部空白，构成正式文件受控签署缺失问题

- Cluster：`MC-CLUSTER-0038`
- 严重度：`P1`
- Agent：Document Control Agent
- 类型：`missing_approval_signatures_in_design_output_list`
- 阶段/术语：Stage 12 / `PT3SBT`
- 涉及候选行数：2
- 裁决理由：该cluster位于Stage 12主审范围（primary_scope=true），两个候选（MF-0211、MF-0226）分别来自设计输出清单二的两个版本文件，均指向Sheet"PT3参考"中产品型号PT3SBT的签署行："提交: 年 月 日 审核: 年 月 日 批准: 年 月 日"——三项签署栏均为空白占位符，未填写实际日期和签署人。设计输出清单二作为DHF核心受控文件，其提交/审核/批准签署是文件受控的必要条件。即使该Sheet标注为"PT3参考"，其出现在正式设计输出清单二文件中且签署栏空白，仍构成文件受控完整性缺陷，需要确认是否为有效参考页或应完成签署。
- 代表证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:237` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日

### M011. 正式设计确认文件（Stage 18主范围）以PT9C命名，且用户测试计划标题亦为PT9C，构成PT9L DHF产品身份污染。

- Cluster：`MC-CLUSTER-0039`
- 严重度：`P1`
- Agent：Product Identity Agent
- 类型：`product_identity_contamination_in_formal_dv_document`
- 阶段/术语：Stage 18 / `PT9C`
- 涉及候选行数：2
- 裁决理由：MF-0232所在文件路径为'18 设计确认\\PT9C设计确认E0 23.11.via_xlsx.clean.md'，文件标题直接为'PT9C设计确认E0 23.11'，primary_scope=true，属于Stage 18正式主审范围内的设计确认文件，文件名及标题均以PT9C标识，而非PT9L。MF-0276所在文件'用户现场测试计划 PT9C V1.0'标题亦为PT9C，但文件编号行显示'PT9L-RYCJ01 V1.0'，说明文件内容编号已更新为PT9L，但标题仍残留PT9C，存在型号不一致问题。两份文件均在正式设计确认目录下，非废案/备份，属于实质性产品身份不一致，需确认文件是否为PT9C遗留文件误归入PT9L DHF，或标题未同步更新，影响PT9L DHF证据链完整性。
- 代表证据：
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:2` # PT9C设计确认E0 23.11

### M012. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Cluster：`MC-CLUSTER-0001`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`product_identity_label_contamination`
- 阶段/术语：Stage 01 / `血压计`
- 涉及候选行数：5
- 裁决理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 代表证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:2` # 客户需求书E0-血压计 23.6

### M013. 结构设计方案评审检查表文件标题使用"血压计"，但该文件属于PT9L额温计Stage 05正式结构设计阶段文件，存在产品身份标签污染。

- Cluster：`MC-CLUSTER-0008`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`product_identity_label_contamination`
- 阶段/术语：Stage 05 / `血压计`
- 涉及候选行数：1
- 裁决理由：文件"结构设计方案评审检查表-血压计E0 23.11"位于Stage 05结构设计方案目录，属于PT9L DHF正式受控文件。文件标题中"血压计"与PT9L（红外额温计）产品类别不符，构成文件命名层面的产品身份污染。虽然仅有1个候选（MF-0030），但其位于正式主审范围，文件标题直接标注错误品类，影响文件可追溯性和产品身份一致性。
- 代表证据：
  - `05 结构设计方案E0 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2` # 结构设计方案评审检查表-血压计E0 23.11

### M014. 软件质量策划评审检查表（Stage 07正式文件）中存在名为"模板修改记录"的Sheet，内容为空白行，属于Excel模板结构未实例化、修改记录未填写的受控文件质量问题。

- Cluster：`MC-CLUSTER-0010`
- 严重度：`P2`
- Agent：Document Control Agent
- 类型：`empty_template_sheet_in_controlled_document`
- 阶段/术语：Stage 07 / `模板`
- 涉及候选行数：1
- 裁决理由：该文件位于Stage 07主审范围（primary_scope=true），为软件质量策划评审检查表的正式受控版本。"模板修改记录"Sheet包含修改日期、修改人、修改内容三列表头，但所有数据行均为空白，说明该Sheet为模板原始结构，从未被实际填写。受控文件的修改记录是版本管理的重要组成部分，空白修改记录表明文件版本变更历史未被记录，影响文件受控完整性。定为P2级，因其影响版本追溯但不直接影响设计输出内容。
- 代表证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70` ## Sheet: 模板修改记录

### M015. 软件需求规格文件（Stage 07正式文件）中出现"第0页/共5页 模板版本：I"字样，为模板页码占位符及模板版本标识未替换，属于正式文件中模板残留问题。

- Cluster：`MC-CLUSTER-0012`
- 严重度：`P2`
- Agent：Document Control Agent
- 类型：`template_placeholder_not_replaced_in_formal_document`
- 阶段/术语：Stage 07 / `模板`
- 涉及候选行数：1
- 裁决理由：该文件位于Stage 07主审范围（primary_scope=true），为软件需求规格说明书的正式受控版本。"第0页/共5页"是明显的模板占位符（正式文件页码不应为0），"模板版本：I"是模板管理标识，均应在文件正式化时替换为实际内容。这些残留标识表明文件可能未经完整的模板实例化处理即进入受控状态，影响文件的正式性和可信度。定为P2级，因其属于格式/标识问题，不直接影响需求内容本身，但影响文件受控状态的判断。
- 代表证据：
  - `07 软件设计方案E0 23.11\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:177` 第 0 页 / 共 5 页 模板版本： I

### M016. PT9L设计验证报告（正式文件）中存在名为"血压计法规标准清单20160719"的Sheet，该Sheet名未更新为PT9L专属标识，暗示文件模板来源于旧版通用血压计模板且未完成产品身份转换。

- Cluster：`MC-CLUSTER-0021`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`legacy_template_sheet_name_in_formal_validation_report`
- 阶段/术语：Stage 11 / `血压计`
- 涉及候选行数：1
- 裁决理由：MF-0097所在文件为primary_scope=true的正式设计验证报告（Stage 11），Sheet名"血压计法规标准清单20160719"中的日期"20160719"与PT9L项目时间线不符，且未包含PT9L型号标识，表明该Sheet系从旧型号或通用模板直接沿用，未完成产品身份更新。设计验证报告作为核心DHF文件，其内部Sheet名称应明确对应PT9L，否则影响法规符合性证据的可追溯性，予以confirm。
- 代表证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:127` ## Sheet: 血压计法规标准清单20160719

### M017. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Cluster：`MC-CLUSTER-0031`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`cross_model_component_reference_without_controlled_declaration`
- 阶段/术语：Stage 12 / `PT9C`
- 涉及候选行数：8
- 裁决理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 代表证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:26` \| 3 \| 接口板PCB图 \| Top Layer 层 \| \| \| PT9C-CNTP01 V1.0 \| V1.0 \| \| \| \| \| \| \| \| \| \| \|

### M018. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Cluster：`MC-CLUSTER-0032`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`cross_model_shared_component_undocumented`
- 阶段/术语：Stage 12 / `PT3`
- 涉及候选行数：50
- 裁决理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 代表证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:26` \| 6 \| 防拆签 \| T040800073941030093 \| PET \| \| PT3-F21 \| \| \| PT3 \| \| 2 \| \| √ \| C \| \| \|

### M019. PT9L包装BOM及总装BOM中多处引用PT3型号零部件（PT3-F21、PT3-P10、PT3-M02、PT3-M01），型号归属明确标注为PT3，与MC-CLUSTER-0032同源，构成跨型号共用件引用问题。

- Cluster：`MC-CLUSTER-0033`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`cross_model_shared_component_undocumented`
- 阶段/术语：Stage 12 / `PT3`
- 涉及候选行数：4
- 裁决理由：MF-0152（PT9L包装BOM）、MF-0197、MF-0198、MF-0199（总装类组件清单PT9L-ABOM01 V1.0）均为Stage 12 primary_scope=true的正式受控BOM文件。防拆签PT3-F21（型号归属PT3）、双联弹簧PT3-P10（型号归属PT3）、金属套PT3-M02（型号归属PT3）、压块PT3-M01（型号归属PT3）在PT9L正式BOM中明确标注来源型号为PT3。这与MC-CLUSTER-0032的问题性质相同，均为PT9L正式BOM中引用PT3型号零部件且未见共用件受控说明。属于正式文件中的实质性产品身份问题，应confirm。
- 代表证据：
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:19` \| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \| \| 2 \| \| √ \| C \| \|

### M020. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Cluster：`MC-CLUSTER-0040`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`product_identity_mixed_model_in_formal_checklist_filename`
- 阶段/术语：Stage 18 / `PT2L`
- 涉及候选行数：5
- 裁决理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 代表证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:3` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0

### M021. Stage 18正式设计确认目录下PT2L（美亚）Checklist的clean.md版本与MC-CLUSTER-0040同源，同样存在PT2L型号标识混入正式文件标题且缺乏受控说明的问题。

- Cluster：`MC-CLUSTER-0041`
- 严重度：`P2`
- Agent：Product Identity Agent
- 类型：`product_identity_mixed_model_in_formal_checklist_filename`
- 阶段/术语：Stage 18 / `PT2L`
- 涉及候选行数：1
- 裁决理由：MF-0238为MC-CLUSTER-0040所涉同一文件的via_lo_html.clean.md转换版本，primary_scope=true，位于Stage 18正式目录。文件标题同样含PT2L（美亚），文件编号DN字段为PT9L-UETR01 V1.0。与MC-CLUSTER-0040属于同一文件的不同格式版本，问题性质完全相同：正式DHF目录中存在历史/异型号文件且PT2L身份缺乏受控说明。依据与MC-CLUSTER-0040相同的裁决逻辑，予以confirm。
- 代表证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.via_lo_html.clean.md:2` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0


## 6. 语义审查确认/修订错误

### S001. PT9L DHF设计输出清单二中归档了型号为PT3的双联弹簧图纸（Drawing NO. PT3-P10，Model NO. PT3），该图纸属于PT3项目原件，非PT9L设计输出，存在法规/验证闭环风险。

- Finding ID：`LLM-0060`
- 严重度：`P1`
- Challenge：`revise`
- Agent：DMR/SOP Agent
- 类型：`legacy_model_drawing_in_dhf`
- 审查理由：DMR-133/134明确标注Drawing NO.为PT3-P10、Model NO.为PT3，DMR-132注明为'PT3项目原件，被PT9L DHF借用归档'。若该件实际用于PT9L，则PT9L EBOM中应有对应物料编码及图号，但当前证据中EBOM（DMR-037至DMR-042）未见PT3-P10条目，形成验证闭环断裂。
- Challenge 理由：核心问题成立：PT3图纸（Drawing NO. PT3-P10，Model NO. PT3）归档于PT9L DHF设计输出清单二，且现有EBOM证据中未见PT3-P10条目，验证闭环存在断裂风险，P1严重度合理。但'借用归档（外购件/设计参照）'注释存在歧义——若该件仅作设计参照而非实际用于PT9L产品，则EBOM中不出现属正常情况，闭环断裂结论需修正。建议将claim表述调整为：'PT3图纸归档于PT9L DHF但EBOM中无对应条目，需明确该零件是否实际用于PT9L；若实际使用则存在验证闭环断裂，若仅为设计参照则需在DHF中补充说明以避免审查歧义'，严重度维持P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:1` # PT3 双联弹簧 REV01 (V1.0) 2D 图读图报告
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT3_双联弹簧_REV01.pdf`
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:6` > **共用件**：**PT3 项目原件**，被 PT9L DHF 借用归档（外购件 / 设计参照）

### S002. 两份包装BOM文件（F0161和F0162）均声称是PT9L包装BOM（美版），但文件编号不一致：F0161为PT9L-PBOM01 V1.0，F0162为PT9L-PB0M1 V1.0（字母O与数字0混用），构成受控文件唯一性风险。

- Finding ID：`LLM-0061`
- 严重度：`P1`
- Challenge：`keep`
- Agent：DMR/SOP Agent
- 类型：`packaging_bom_document_number_inconsistency`
- 审查理由：DMR-055显示F0161文件编号为'PT9L-P BOM01 V1.0'，DMR-062/063显示F0162文件编号为'PT9L-PB0M1 V1.0'（B后为数字0非字母O）。两份文件物料条目高度重叠（DMR-057/058对比DMR-065/066），但编号不同，无法确定哪份为受控版本，可能导致生产现场使用错误版本。
- Challenge 理由：证据直接支持结论。两份独立文件中均可见文件编号差异：F0161为'PT9L-P BOM01 V1.0'，F0162为'PT9L-PB0M1 V1.0'（B后为数字0而非字母O）。两处证据来自不同文件路径，非同一文档重复引用。字母O与数字0混用在受控文件编号中构成真实的唯一性风险，符合P1严重度定义。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:8` andon文件编号：PT9L-P BOM01 V1 . 0 PT9L包装BOM(美版)【组件清单】
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:8` \| ![PT9L包装BOM_image_001.png](PT9L包装BOM.via_xlsx_assets/PT9L包装BOM_image_001.png) \| \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \| \| \| \| \| \| \| \| \| \|
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:10` \| \| \| 文件编号：PT9L-PB0M1 V1.0 PT9L包装B0M（美版）【组件清单】 \| \| \| \| \| \| \| \| \| \|

### S003. 机芯BOM中存在旧型号PT9C的PCB料号，与PT9L项目不符，可能导致验证闭环断裂。

- Finding ID：`LLM-0021`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`bom_pcb_cross_contamination`
- 审查理由：F0096和F0097的机芯BOM中均列有料号K0118000084609A1106、图号PT9C-CNTP01 V1.0的PCB，与PT9L主PCB（PT9L-HFMP01 V1.0）并列存在。若该PT9C PCB实际用于生产，则PT9L的硬件验证结论不能覆盖该物料，构成法规验证闭环断裂风险。
- Challenge 理由：证据直接支持结论：三条evidence分别显示IFT-FXJH01 V1.0与PT9L-FXJH01 V1.0两套文件同时存在于03风险分析目录，且F0018（IFT-FXPJ01 V2.0）与对应PT9L版本（V1.0）版本号不一致。两套文件无废止标记，审查员无法判断受控有效版本，构成法规闭环风险。证据充分，非误报，维持P1。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \| \| \| 1 \| PCB \| √ \| C \| \| \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \| \| \| 1 \| PCB \| √ \| C \| \| \|

### S004. 电池使用寿命测试报告中电池容量标注为1000mAh，与包装BOM中1200mAh不一致，测试代表性存疑。

- Finding ID：`LLM-0022`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`battery_parameter_inconsistency`
- 审查理由：HW-071/HW-076（电池寿命测试报告）描述测试电池为"两节七号干电池（3V/1000mAh）"，而HW-065（包装BOM）列明随机电池为"7号碱性 1.5V/1200mAh"。容量差异200mAh可能导致测试结论（≥1000次）不能代表实际出货电池的寿命表现，影响验证闭环有效性。
- Challenge 理由：证据直接支持结论：line 542和543明确写明
- 证据：
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.pdf.md:29` 测试使用电池：两节七号干电池（3V/1000mAh）；
  - `11 T1样机\PT9L电池使用寿命测试报告 V1.0.via_lo_html.clean.md:18` 测试使用电池：两节七号干电池（3V/1000mAh）；
  - `11 T1样机\PT9L包装BOM.via_xlsx.clean.md:23` \| 10 \| 电池 \| K020400000757680820 \| \| 7号碱性 1.5V/1200mAh \| LR03 \| \| 2 \| \| √ \| C \| \|

### S005. 整机寿命测试报告存在三个版本文件（F0084、F0085、F0095），文件编号相同但来源不同，版本控制状态不明确。

- Finding ID：`LLM-0026`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`duplicate_life_test_report_version_control`
- 审查理由：HW-047~HW-051（F0084，PDF版）、HW-053~HW-058（F0085，HTML版）、HW-092~HW-097（F0095，文件名含2020-3-25）三份文件均使用编号PT9L-PLER01 V1.0，但F0095文件名含日期2020-3-25，早于PT9L项目正常时间线，存在使用旧版报告替代当前验证结论的风险。
- Challenge 理由：证据直接显示T阶段设计验证报告封皮三个子报告均为□未勾选（line 22、24等），而子报告内容（VV-088~VV-097）已存在，封皮与内容脱节事实清晰。按21 CFR 820.30(f)要求，验证记录须完整关联，空选封皮构成形式上的验证闭环缺失，不属于误报。P1严重度合理，因其直接影响审查员对验证完成状态的判断。
- 证据：
  - `11 T1样机\PT9L产品寿命测试报告.via_lo_html.clean.md:6` 文 件编号： PT9L-PLER01 V1.0 整机寿命评估报告
  - `11 T1样机\整机寿命测试报告2020-3-25.via_lo_html.clean.md:6` 文 件编号： PT9L-PLER01 V1.0 整机寿命测试报告
  - `11 T1样机\整机寿命测试报告2020-3-25.via_lo_html.clean.md:12` \| **测试目的： PT9L 寿命测试** \| **测试时间：** \|

### S006. 结构类FMEA中电池功能描述为"给血压计供电"，与PT9L红外体温计品类不符。

- Finding ID：`LLM-0027`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`structural_fmea_product_type_error`
- 审查理由：HW-014（F0074结构类FMEA第17行）明确写有"给血压计供电"，PT9L为红外体温计。该错误出现在FMEA的功能描述列，属于主范围文件中的品类污染，可能影响FMEA分析的完整性和法规审查结论。
- Challenge 理由：证据显示设计确认阶段封皮结论栏'☐设计验证合格'为未勾选状态（VV-111），而通用要求和法规标准部分已☑（VV-109、VV-110），形成内部矛盾。文件名含'加结论'字样，说明该栏位本应被填写，空白属于遗漏而非设计。21 CFR 820.30(g)明确要求设计确认须有书面结论，此finding核心成立，非误报。P1严重度合理。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17` \| \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \| \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \| \| \| □ \|

### S007. 多份样机评审检查表中所有检查项结果栏均为空白（无通过/不通过/不适用勾选），评审完成状态无法确认。

- Finding ID：`LLM-0028`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`sample_review_checklist_result_blank`
- 审查理由：HW-020至HW-036（F0076、F0078、F0080三份评审检查表）的所有检查项结果列均显示为"□通过 □不通过 □不适用"，无任何勾选记录。若这些表格为正式评审记录，空白结果意味着评审未完成或记录未归档，影响DHF完整性。
- Challenge 理由：证据明确显示T1样机文件夹下所有生物相容性报告路径均含'同PT5生物相容性报告'，报告编号为PT5专属系列（SDWH-M201905262），无任何PT9L标识。DHF中未见桥接评估或材料等同性声明文件。ISO 10993要求对被评价器械本身进行评价或提供充分的等同性论证，跨型号直接引用且无说明文件构成实质性法规符合性风险。P1严重度合理，不属于误报。
- 证据：
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:16` \| 2 \| 装 配 检 查 \| 电池盖配合 \| \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:29` \| 15 \| 装 配 检 查 \| 电池弹簧固定 \| \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:34` \| 20 \| 装 配 检 查 \| PCB固定 \| \| □通过 □不通过 □不适用 \|

### S008. 主范围风险评估报告（F0018）正文两处均出现旧型号PT3SBT，预期用途描述与PT9L项目不符。

- Finding ID：`LLM-0002`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- 审查理由：F0018 line 93与SCOUT-073（同一文件line 93）均写明PT3SBT，该文件属于PT9L DHF主范围。风险评估报告是ISO 14971合规的核心文件，型号错误将直接影响法规审查结论，属于高优先级闭环风险。
- Challenge 理由：三条证据均直接命中：line 239封面明确写'产品型号:PT3SBT'，line 187和line 293的BOM编号前缀均为PT3SBT（PT3SBT-PBOM01、PT3SBT-ABOM01）。证据与claim高度一致，设计输出清单二封面及内容型号均为PT3SBT而非PT9L，属于DMR核心文件型号错误，结论成立，严重度P1合理。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:93` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea...

### S009. 03风险分析文件夹中存在两套结构相同的风险管理文件（F0017-F0020无PT9L前缀 vs F0021-F0023有PT9L前缀），受控版本不明确。

- Finding ID：`LLM-0003`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`duplicate_risk_file_set_without_clear_control`
- 审查理由：F0017与F0021内容结构高度相似（目录页码完全一致），F0018与F0022同理，但文件命名不同。DHF中同时存在两套文件，若无明确的版本控制说明，审查机构无法判断哪套为正式受控版本，存在引用错误文件的法规风险。
- Challenge 理由：三条证据均直接支持结论：line 2文件标题明确为'结构设计方案评审检查表-血压计E0 23.11'；line 17和line 18的FMEA内容明确描述血压计功能（给血压计供电、包装血压计、腕枕等血压计专属部件）。血压计与红外体温计属不同品类，法规标准体系差异显著，此类文件混入PT9L DHF属于实质性文件管理错误，结论成立，严重度P1合理。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:16` **Reviewed by** *(Certification Engineer)* Date:
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:1` <!-- hybrid clean-md; source = via_lo_html.md; 规整表=GFM，多段大格=标题/段落，无 HTML 标签/无合并记号 -->

### S010. 正式实验报告（F0458，PT9L -2-56测试报告）中引用的风险管理报告文件号为PT9C-FXGB01，与PT9L项目文件号体系不一致。

- Finding ID：`LLM-0004`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_test_report`
- 审查理由：F0458 lines 577-581中测试报告多次引用PT9C-FXGB01作为风险管理报告依据，而PT9L项目的风险管理报告文件号应为IFT-FXGB01（F0020）或PT9L前缀文件。测试报告引用错误型号的风险文件，将导致ISO 80601-2-56符合性证据链断裂。
- Challenge 理由：三条证据（line 577、578、579）均直接命中，测试报告在4.2、4.3、4.4条款中连续引用'Risk Management Report (file No.: PT9C-FXGB01 V1.0)'，而PT9L对应风险管理报告文件号应为IFT-FXGB01。PT9C为另一型号，文件号体系不一致在认证审查中属于可被质疑的一致性缺陷，结论成立，严重度P1合理。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:578` \| 4.3 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Hazard analysis recorded \| P \|
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:579` \| 4.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk estimation recorded \| P \|

### S011. 主范围DFMEA文件（F0074）多处内容明确描述血压计功能（电池给血压计供电、包装血压计等），与PT9L红外体温计品类不符。

- Finding ID：`LLM-0006`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`legacy_category_in_primary_scope`
- 审查理由：F0074 lines 17-22中DFMEA条目功能描述均为血压计相关内容（"给血压计供电""包装血压计""用户无法识别血压计的相关法规信息"），该文件位于PT9L DHF主范围T1样机DFMEA文件夹。DFMEA品类错误将导致失效模式分析无法覆盖体温计实际风险，影响设计验证完整性。
- Challenge 理由：证据直接且充分：结构类FMEA（F0074 line 22）明确写
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:17` \| \| 电池 \| 给血压计供电 \| 电池无法装入电池仓 \| 用户无法测量 \| 8 \| B \| 电池的尺寸超出设计要求 \| 3 \| \| 实际装配 \| 5 \| 120 \| 尺寸检验 \| 8 \| 3 \| 2 \| 48 \| 检查尺寸检测报告 \| \| \| □ \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:18` \| \| 彩包装 \| 包装血压计 \| 腕枕无法装入彩包装或腕枕装入彩包装后晃动量太大 \| 生产人员无法包装 \| 4 \| C \| 彩包装的尺寸设计不合理 \| 2 \| \| 实际装配 \| 2 \| 16 \| \| \| \| \| \| \| \| \| \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:19` \| \| 彩包装 \| 包装血压计 \| 彩包装支撑强度不够 \| 彩包装褶皱或破损 \| 4 \| C \| 彩包装的材质强度不够 \| 3 \| \| 跌落试验、运输试验 \| 2 \| 24 \| \| \| \| \| \| \| \| \| \|

### S012. 主范围设计输出清单二（F0235、F0236）中大量条目引用PT3SBT文件编号，与PT9L项目不符。

- Finding ID：`LLM-0008`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- 审查理由：F0235/F0236中多个设计输出条目（包装BOM、总装BOM、装配说明、收纳盒、胶垫等）均使用PT3SBT前缀编号，且封面标注"产品型号:PT3SBT"。设计输出清单是DHF核心受控文件，型号错误将导致设计输出与PT9L产品无法对应，影响设计转换完整性。
- Challenge 理由：证据直接支持结论：设计输入汇总表（line 134）明确勾选
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \| \| \| \| \| \| \| \| \| \| \| \| \|
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \| \| \| \| \| \| \| \| \| \| \| \| \|

### S013. PT9L T1样机文件夹中存在PT3SBT标签审核表，且检查记录引用PT2L标签文件，旧型号残留污染主范围文件，法规证据归属不清。

- Finding ID：`LLM-0011`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Regulatory Agent
- 类型：`old_product_contamination_in_primary_scope`
- 审查理由：REG-060~REG-065所在文件路径为'11 T1样机\PT3SBT标签审核表（海外更新）'，检查记录列明确写'PT2L(美亚)-ZXBQ01~06'，与PT9L无直接关联。若审查机构将此文件视为PT9L的标签合规证据，将导致法规闭环错误。
- Challenge 理由：证据直接：文件路径明确位于PT9L T1样机目录下，文件名含'PT3SBT'型号标识，内容涉及血压计电池仓标识条款，与PT9L红外体温计产品无对应关系。跨型号文件混入DHF目录构成文件边界污染，法规审查时存在被误认为PT9L有效证据的风险，结论成立，严重度P1合理。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:20` \| 标准名称 \| 适用性 \| \| 标签类型 \| \| \| \| \| 检查记录 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:22` \| IEC 60601-1 \| A \| \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ01 V1.0 \|
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:23` \| IEC 60601-1-2 \| A \| \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ02 V1.0 \|

### S014. 风险评估报告和FMEA均引用IEC 60601-1作为适用标准，但红外体温计通常为非电气设备，IEC 60601-1适用性需正式说明。

- Finding ID：`LLM-0016`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Regulatory Agent
- 类型：`iec_60601_1_applicability_questionable_for_ift`
- 审查理由：REG-002~REG-007及REG-010~REG-015显示风险评估报告包含大量IEC 60601-1条款问答；REG-029/REG-032 FMEA也引用IEC 60601-1。若PT9L为电池供电非网电设备，需在标准适用性文件中明确说明IEC 60601-1的适用范围和豁免条款，否则构成过度声明风险。
- Challenge 理由：证据明确：文件标题、路径、图片资产均标注BP3L，且该文件物理位于PT9L的07软件设计方案目录下。BP3L为血压计，与PT9L红外体温计属不同品类，软件图样不存在共用合理性。文件残留导致DHF边界不清的结论直接成立，无误报迹象。严重度P1合理，跨品类文件污染对法规审查影响显著。
- 证据：
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:62` 3.3 Questions from IEC 60601-1:2005+AMD1:2012+AMD2:2020 Edition 3.2 8
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:64` 3.4: Additional questions arising from IEC 60601-1-2:2014+A1:2020 edition 4.1: 13
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:177` ### .3 Questions from IEC 60601-1:2005+AMD1:2012+AMD2:2020 Edition 3.2

### S015. 设计验证报告文件名含'EN1060-1项'，EN 1060-1为血压计标准，疑为旧品类模板残留，影响验证报告与IFT法规要求的对应关系。

- Finding ID：`LLM-0017`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Regulatory Agent
- 类型：`design_verification_report_title_references_blood_pressure_standard`
- 审查理由：REG-120~REG-125所在文件路径为'性能规格部分（一）EN1060-1项'，EN 1060-1是血压计非侵入性血压计标准。IFT应适用ISO 80601-2-56，文件标题错误可能导致审查人员对验证覆盖范围产生疑问，需确认内容是否已按IFT标准重新编制。
- Challenge 理由：证据明确：文件名含PT3SBT，内容型号为PT2L，物理路径位于PT9L的11 T1样机目录下。PT3SBT与PT2L均为旧型号，与PT9L无关联，不存在合理的共用或引用场景。DMR文件污染结论直接成立。严重度P1合理，T1样机阶段出现无关型号标签审核表可能误导制造和审查决策。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:23` \| 1 \| 温度显示范围 \| 32.0℃～42.9℃ \| □手板■T1□设计确认 \| 参见《PT9L红外体温计产品检验标准V1.0 》第6项 \| 全部测试结果均需符合《PT9L红外体温计产品检验标准V1.0》中第6项的要求 \| 参见《PT9L红外体温计检测报告 V1.0》中第6项测试结果 \| 合格 \|
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:24` \| 2 \| 显示分辨力 \| 0.1℃ \| □手板■T1□设计确认 ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（一）EN1060-1项_image_001.png) ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（一）EN...
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:25` \| 3 \| 测量误差 \| ≥35℃且≤42℃：±0.2℃，其它：±0.3℃ \| □手板■T1□设计确认 ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx_assets/性能规格部分（一）EN1060-1项_image_001.png) ![性能规格部分（一）EN1060-1项_image_001.png](性能规格部分（一）EN1060-1项.via_xlsx...

### S016. 风险管理报告（F0020）文件名标注IFT-FXGB01 V2.0，但正文文件号字段显示PT9L-FXGB01 V1.0，文件号与版本号双重矛盾。

- Finding ID：`LLM-0039`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Risk Traceability Agent
- 类型：`document_number_internal_contradiction`
- 审查理由：文件名（IFT-FXGB01 V2.0）与正文DN字段（PT9L-FXGB01 V1.0）在品类前缀和版本号上均不一致，导致下游引用文件无法确定受控版本，影响风险管理闭环可追溯性。
- Challenge 理由：证据直接支持结论：同一文件的文件名标注IFT-FXGB01 V2.0，正文DN字段显示PT9L-FXGB01 V1.0，品类前缀（IFT vs PT9L）和版本号（V2.0 vs V1.0）均存在矛盾，属于文件受控管理的实质性缺陷，影响风险管理文件的可追溯性和法规提交依据的确定性。P1严重度合理。
- 证据：
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:2` # Attachment 7 04 Risk Management Report IFT-FXGB01 V2.0 20240530-All applicable
  - `03 风险分析\Attachment 7 04 Risk Management Report IFT-FXGB01  V2.0 20240530-All applicable.via_lo_html.clean.md:6` DN ： PT9L -FXGB01 V 1 .0 Risk Management Report

### S017. F0022（PT9L版风险评价报告）文件名标注V2.0，但正文DN字段显示PT9L-FXPJ01 V1.0，版本号不一致。

- Finding ID：`LLM-0041`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Risk Traceability Agent
- 类型：`risk_assessment_report_version_mismatch`
- 审查理由：文件名与正文版本号不符，F0252可追溯性分析报告引用PT9L-FXPJ01 V1.0，若实际受控版本为V2.0则引用失效；若为V1.0则文件名标注错误，两种情况均影响追溯闭环。
- Challenge 理由：证据直接支持结论：文件名标注V2.0（line 2），正文DN字段明确写入V1.0（line 6），两者不一致事实清晰；可追溯性分析报告（line 18）引用PT9L-FXPJ01 V1.0，若受控版本实为V2.0则引用链断裂，追溯闭环受损。非误报，核心问题成立。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:6` D N ： PT9L-FXPJ01 V1.0 Risk Assessment Report
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:18` \| 软件需求分析阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \| \| 相关文档之间的信息描述都是准确的 \| \| 相关文档之间的信息都是正确的，没有歧义信息 \| \| 相关文档已包含软件必需信息，陈述所有功能 \| \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### S018. F0023（PT9L版风险控制验证报告）文件名标注V2.0，但正文DN字段显示PT9L-FXYS01 V1.0，版本号不一致。

- Finding ID：`LLM-0042`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Risk Traceability Agent
- 类型：`risk_control_verification_report_version_mismatch`
- 审查理由：与风险评价报告类似，文件名与正文版本号不符。F0124可追溯性分析报告引用PT9L-FXYS01 V1.0，若实际为V2.0则引用链断裂，剩余风险评估的闭环证据链存疑。
- Challenge 理由：证据直接支持结论：文件名含V2.0，正文DN字段明确写入PT9L-FXYS01 V1.0（line 6），版本号不一致；可追溯性分析报告（line 32）引用V1.0，若受控版本为V2.0则剩余风险评估闭环证据链存疑。与LLM-0041属同类问题，均有直接文本支撑，非误报。
- 证据：
  - `03 风险分析\PT9L--Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:6` D N: PT9L-FXYS01 V1.0 Verification of risk control measure and residual risk evaluation r eport
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:32` \| 用户测试阶段 \| 风险管理 \| 风险控制措施验证以及剩余风险评估报告PT9L-FXYS01 V1.0<br>风险管理报告<br>PT9L-FXGB01 V1.0 \| \| 相关文档之间的信息描述都是准确的 \| \| 相关文档之间的信息都是正确的，没有歧义信息 \| \| 相关文档已包含软件必需信息，陈述所有功能 \| \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|

### S019. 结构类DFMEA（F0074）严重度评分表中明确写入"影响血压计的安全运行"，品类描述与PT9L红外体温计不符，构成旧品类残留。

- Finding ID：`LLM-0043`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Risk Traceability Agent
- 类型：`dfmea_wrong_product_category_residual`
- 审查理由：DFMEA严重度准则中的产品描述直接影响风险评分的适用性判断。血压计与红外体温计的危害场景、严重度定义不同，若评分准则基于错误品类，则所有依赖该DFMEA的风险控制验证结论均存在有效性风险。
- Challenge 理由：证据直接支持结论：结构类DFMEA严重度评分表line 542和line 543均明确写入'影响血压计的安全运行'，而该文件归属PT9L红外体温计项目，品类描述错误属实。严重度准则描述错误将直接影响RPN评分适用性，进而影响所有依赖该DFMEA的风险控制结论有效性，P1定级合理。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:542` \| \| 无警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时无预警。会危及使用者。 \| 10 \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:543` \| \| 有警告的严重危害 \| 潜在失效模式影响血压计的安全运行和/或包含不符合法规情形，失效发生时有预警。会危及使用者。 \| 9 \|

### S020. PT9L机芯类组件清单中PCB图号引用PT9C旧型号文件编号，存在设计输出与当前型号不一致的法规风险

- Finding ID：`LLM-0031`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Software Agent
- 类型：`legacy_model_pcb_reference_in_bom`
- 审查理由：SW-119（F0096）和SW-125（F0097）均在PT9L机芯BOM的PCB行中记录图号"PT9C-CNTP01 V1.0"，PT9C为旧型号。两份BOM文件（EBOM01和T1EB01）均出现此引用，说明非偶发笔误。若PT9L实际使用的PCB图纸仍归档于PT9C文件体系，则PT9L的设计输出追溯链断裂，不符合设计控制要求。
- Challenge 理由：证据直接支持结论：文件路径确认该图纸归档于PT9L DHF设计输出清单二，而图纸标题、来源注释均明确标注为PT3项目原件，仅以'共用件/设计参照'注释归档，缺乏正式跨型号受控引用程序。无论PT9L是否实际使用该弹簧，均存在法规可追溯性缺陷（21 CFR 820.30(d)/ISO 13485 7.3.4要求设计输出可追溯至设计输入）。非误报，核心问题成立，严重度P1合理。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \| \| \| 1 \| PCB \| √ \| C \| \| \|
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \| \| \| 1 \| PCB \| √ \| C \| \| \|

### S021. PT3SBT/PT2L旧型号标签审核表存放于PT9L T1样机文件夹，文件内容与PT9L无关，构成旧型号资料残留

- Finding ID：`LLM-0032`
- 严重度：`P1`
- Challenge：`keep`
- Agent：Software Agent
- 类型：`legacy_model_label_document_in_t1_folder`
- 审查理由：SW-087至SW-092均来自F0082，文件名为"PT3SBT标签审核表（海外更新）"，内容明确记录产品型号PT2L、项目编号2020-DEV01及PT2L专属文件编号（PT2L-SMSP09等）。该文件路径位于"11 T1样机"文件夹且excluded_from_primary_scope=false，与PT9L T1样机阶段文件混存，可能导致标签验证范围混淆。
- Challenge 理由：证据直接支持结论：两份独立文件（外观图与外箱图纸）的Drawing NO.均为PT9L-F01，且解析报告中已明确标注冲突警告。图号唯一性是受控图纸管理的基本要求，重复图号将导致制造、采购、质检无法通过图号唯一定位文件，属于配置管理实质性缺陷。非误报，严重度P1合理。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:16` \| ▉说明书 □彩包装 □铭牌 □外箱 □其他： \| \| \| \| PT2L-SMSP09 \| \| \| \| \|

### S022. 设计确认阶段验证报告封皮中"设计验证合格"结论项为"☐"（未勾选），设计确认闭环结论缺失。

- Finding ID：`LLM-0051`
- 严重度：`P1`
- Challenge：`keep`
- Agent：V&V Agent
- 类型：`design_confirmation_cover_pass_not_checked`
- 审查理由：VV-111显示"☐设计验证合格：所有设计验证项目已按照相应的设计验证计划进行，都已验证通过合格"未被勾选，而VV-109/VV-110显示两个子报告已勾选。结论项空白直接导致设计确认无法形成法规要求的正式通过声明。
- Challenge 理由：证据直接且明确：line 28显示"☐设计验证合格"未勾选，而line 22和line 24显示两个子报告均已勾选（☑），形成鲜明对比。封皮汇总结论项空白导致设计确认阶段无法形成法规要求的正式通过声明，属于设计确认闭环缺失的实质性问题。证据充分支持P1定级，无误报迹象。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:28` ☐设计验证合格：所有设计验证项目已按照相应的设计验证计划进行，都已验证通过合格。
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:22` ☑设计验证报告－通用要求部分 文件编号： PT9L-Q1TY01 V1.0
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:24` ☑设计验证报告－法规标准部分 文件编号： PT9L-Q1BZ01 V1.0

### S023. 散热器压块图纸（FDIR-V14）在PT9L总装图BOM中以PT3-M01入账，图号前缀为PT3而非PT9L，与PT9L项目图号命名规范不符，存在物料可追溯性风险。

- Finding ID：`LLM-0064`
- 严重度：`P2`
- Challenge：`revise`
- Agent：DMR/SOP Agent
- 类型：`assembly_drawing_pt3_m01_bom_traceability_gap`
- 审查理由：DMR-126明确指出'本件在PT9L BOM中以PT3-M01入账'，DMR-125显示该图纸路径在PT9L DHF历史文件中。PT3-M01前缀暗示该件源自PT3项目，若PT9L与PT3的压块规格存在差异而未经变更控制，则验证数据可能不适用于PT9L。
- Challenge 理由：证据支持核心事实：散热器压块在PT9L BOM中以PT3-M01入账，图号前缀与PT9L项目不符。但finding将此定性为'验证数据可能不适用于PT9L'的风险，属于推断性结论，超出现有证据范围——证据仅证明图号命名不一致，未证明PT3与PT9L压块规格存在实质差异。建议将claim修订为：'散热器压块图纸在PT9L BOM中以跨项目图号PT3-M01入账，图号体系不一致，需确认该件是否经过PT9L适用性评估及变更控制'，严重度维持P2。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/FDIR-V14_散热器压块_REV01_0714.pdf`
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:6` > **关联**：[疑点表 §4.1](../../../../wiki/drawings/pt9l-2d-audit-doubts.md#41-75cee0-散热器金属套图号-5b44cgxt-001) **75CEE0 黄铜套 2m 跌落要求** 的配合件；[疑点表 §6.3 新增](#疑点新增) 总装图 BOM 编号 13 PT3-M01 = 本图
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:28` **iHealth 内部图号映射**：根据 [总装图 BOM](PT9L-总装图-v1.0-20240627.pdf.md) 编号 13，本件在 PT9L BOM 中以 **PT3-M01** 入账（"压块"）。

### S024. F0162包装BOM（受控文件PT9L-PB0M1 V1.0）中仅列出彩包装和纸托2项，而F0161包装BOM列出4项（含说明书PT9L-SMSPO1和保护膜PT9L-P10），两份BOM物料条目数量不一致，存在漏料风险。

- Finding ID：`LLM-0065`
- 严重度：`P2`
- Challenge：`keep`
- Agent：DMR/SOP Agent
- 类型：`packaging_bom_missing_items`
- 审查理由：DMR-065/066显示F0162仅有彩包装和纸托2条记录；DMR-057至DMR-060显示F0161有4条记录，多出说明书（DMR-059）和保护膜（DMR-060）。说明书属于A级重要度，若制造现场依据F0162配料将导致说明书漏装，影响产品合规性。
- Challenge 理由：证据直接支持结论。所提供的evidence清晰显示F0162（文件名37ed31b4835c1e57463e2ca2628ef51）中包含彩包装（行21）、纸托（行22）、说明书（行23）共3条记录，而rationale称F0162仅有2项——但无论实际条目数为2还是3，说明书（PT9L-SMSPO1，A级重要度）是否在两份BOM中均有记录仍需核实。核心问题（两份声称相同用途的包装BOM物料条目不一致）有证据支撑，说明书漏装风险对产品合规性影响真实，P2严重度合理。注：evidence中行23已显示说明书条目，建议人工复核F0162完整内容以确认实际缺失项。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:21` \| 1 \| 彩包装 \| K040200021397620814 \| 350g白卡纸 覆哑膜 \| \| PT9L-CBZP01 \| \| \| PT9L \| \| 1 \| \| √ \| A \| \| \|
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:22` \| 2 \| 纸托 \| K040500002717620814 \| 350g白卡纸 覆哑膜 \| \| PT9L-F04 \| \| \| PT9L \| \| 1 \| \| √ \| C \| \| \|
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:23` \| 3 \| 说明书 \| K040700022027620814 \| 70g双胶纸 \| \| PT9L-SMSPO1 \| \| \| PT9L \| \| 1 \| \| √ \| A \| \| \|

### S025. 设计验证计划通用要求部分含"次血压测量"字样，与PT9L红外体温计品类不符，构成品类污染风险。

- Finding ID：`LLM-0024`
- 严重度：`P2`
- Challenge：`keep`
- Agent：Hardware Agent
- 类型：`blood_pressure_terminology_contamination`
- 审查理由：HW-139（设计验证计划-通用要求和法规部分）第20项电池条目中写有"在充满电后，电池电量至少能进行 次血压测量"，PT9L为红外体温计，不涉及血压测量。该文字残留表明该文件从血压计模板复制而来且未完整清理，可能导致审查机构对产品品类产生疑问。
- Challenge 理由：证据直接支持结论：F0252（可追溯性分析报告）line 18和line 28均明确引用PT9L-FXPJ01 V1.0，而F0018 line 23的变更记录证实V2.0于2024.5.30已更新风险控制措施描述内容。两套文件同时存在于DHF（参见LLM-0021），可追溯性报告未同步至最新版本，追溯链存在实质性断裂风险。证据充分，维持P2。
- 证据：
  - `11 T1样机\设计验证计划E0\设计验证计划-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:47` \| 20 \| 电池 battery \| □可充电电池：在充满电后，电池电量至少能进行 次血压测量，并且电池性能参数不变。 □电池：需要符合WERC认证 ■无要求 \| □手板■T1□设计确认 \| 电池寿命测试报告 \| 符合设计输入要求 \| \|

### S026. 主范围软件设计方案文件夹中存在BP3L软件图样（F0052），与PT9L项目型号不符。

- Finding ID：`LLM-0007`
- 严重度：`P2`
- Challenge：`revise`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- 审查理由：F0052文件标题及资产路径均为"BP3L 软件图样"，位于PT9L DHF主范围07软件设计方案文件夹。BP3L为血压计型号，其软件图样出现在体温计DHF中，可能导致软件设计输出清单引用错误文件，影响软件验证闭环。
- Challenge 理由：核心问题成立：PT9L DHF中存在文件名为
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50` ![图片 13](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d468a82f.png)
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54` ![图片 23](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_cd06a829.png)

### S027. 主范围标签审核表（F0082）文件名为PT3SBT，内容引用PT2L型号及文件编号，与PT9L项目不符。

- Finding ID：`LLM-0009`
- 严重度：`P2`
- Challenge：`keep`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- 审查理由：F0082文件名为"PT3SBT标签审核表"，内容中产品型号为PT2L，项目编号为2020-DEV01，文件编号均为PT2L前缀。该文件位于PT9L DHF主范围T1样机文件夹，标签审核表型号错误将导致PT9L标签合规性无法通过该文件得到验证。
- Challenge 理由：证据支持结论：所有生物相容性报告文件名均含
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计

### S028. 设计输入中EN ISO 80601-2-56:2017+A1:2018被标记为'否（不适用）'，但说明书声明符合该标准，存在法规适用性矛盾。

- Finding ID：`LLM-0014`
- 严重度：`P2`
- Challenge：`keep`
- Agent：Regulatory Agent
- 类型：`en_iso_80601_2_56_marked_not_applicable_for_eu`
- 审查理由：REG-024显示设计输入汇总表中EN ISO 80601-2-56欧盟版本勾选'■否'，而REG-071说明书明确列出'EN ISO 80601-2-56:2017/A1:2020'为适用标准。若产品面向欧盟市场，该矛盾将导致技术文件与标签声明不一致，影响CE合规性。
- Challenge 理由：证据直接：三份评审检查表中电池盖配合、电池弹簧固定、PCB固定等关键装配项结论栏均为全空（□通过□不通过□不适用均未勾选），无法证明评审已执行和闭环。涉及多份文件（F0076/F0078/F0080）且为系统性空白，非偶发。硬件装配验证记录不完整是DHF实质性缺陷，P2严重度合理。
- 证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:134` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| ISO 80601-2-56:2017/Amd1:2018 \| 欧盟 \| □是 ■否 \| \|
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:510` ISO 80601-2-56:2017+A1:2018/ EN ISO 80601-2-56:2017/A1:2020 (Medical Electrical Equipment -- Part 2-56: Particular Requirements For The Basic Safety And Essential Performance Of clinical thermometers for body temperature...

### S029. DHF中存在两套内容高度相似的风险管理文件（F0017/F0018/F0019与F0021/F0022/F0023），版本号和日期相同，文件归属和主控版本不明确。

- Finding ID：`LLM-0018`
- 严重度：`P2`
- Challenge：`revise`
- Agent：Regulatory Agent
- 类型：`duplicate_risk_management_files_without_differentiation`
- 审查理由：REG-001与REG-009、REG-002与REG-010、REG-008与REG-016的source_text完全一致，仅文件路径前缀不同（有无'PT9L--'前缀）。两套文件并存且无差异，无法判断哪套为PT9L正式受控版本，存在法规文件管理混乱风险。
- Challenge 理由：核心问题成立：PT9L BOM中PCB图号引用PT9C-CNTP01 V1.0，跨型号引用需要解释。但原finding将其直接定性为'错误型号物料规格'过于武断——PT9C与PT9L可能共用同一PCB设计（平台化开发中图号沿用旧型号前缀是常见做法），也可能确为错误引用。现有证据无法区分这两种情形。建议将结论修改为'PT9L BOM中PCB图号引用PT9C-CNTP01，需确认该PCB是否为PT9C/PT9L共用设计，若非共用则构成BOM物料规格错误'，并将严重度从P1降至P2，因为在共用PCB场景下风险较低。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:70` The risk management process will be conducted in accordance with standard ISO 14971:2019, EN ISO 14971:2019 and EN ISO 14971:2019/A11:2021. The risk management plan for the whole life-cycle of the medical device as shown...
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:70` The risk management process will be conducted in accordance with standard ISO 14971:2019, EN ISO 14971:2019 and EN ISO 14971:2019/A11:2021. The risk management plan for the whole life-cycle of the medical device as shown...
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:62` 3.3 Questions from IEC 60601-1:2005+AMD1:2012+AMD2:2020 Edition 3.2 8

### S030. F0242（设计确认文件）文件名含PT9C，但其中引用的风险管理报告为PT9L-FXGB01 V1.0，文件归属与引用内容存在型号混用。

- Finding ID：`LLM-0045`
- 严重度：`P2`
- Challenge：`keep`
- Agent：Risk Traceability Agent
- 类型：`design_validation_risk_reference_uses_old_model_pt9c`
- 审查理由：PT9C为旧型号，若该设计确认文件实为PT9C项目文件被复用于PT9L，则其风险管理闭环声明（"所有降低风险措施已实施"）的适用性存疑；若为PT9L文件则文件名应更正。
- Challenge 理由：证据直接支持结论：文件名含'PT9C'（rel_path明确），但内部line 87引用风险管理报告PT9L-FXGB01 V1.0，型号混用事实清晰。该文件若为PT9C项目文件被复用，则其风险管理闭环声明（line 46 '所有降低风险措施已经实施'）对PT9L的适用性存疑；若为PT9L文件则文件名标注错误。两种情况均构成文档管理缺陷，P2定级合理，不属于误报。
- 证据：
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:23` \| 4.风险 \| 风险管理 \| 安全性，有效性 \| 依据“风险管理计划“，检查风险管理文档， \| 确认所有降低风险措施已经实施，剩余风险均可接受，风险管理报告通过评审 \| 试产后 \| 项目负责人 \| 项目负责人负责确认所有降低风险措施已经实施，剩余风险均可接受，风险管理报告通过评审 \|
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:46` \| 4.风险 \| 风险管理 \| 所有降低风险措施是否已经实施，剩余风险均可接受，风险管理报告通过评审 \| \| \| ■是 □否 \| \|
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:87` \| 4.风险 \| 风险管理 \| 风险管理报告 \| PT9L-FXGB01 V1.0 \| ■是 □否 \|

### S031. 设计验证计划（F0121）中YY/T 0316-2016、EN ISO 14971:2019等风险相关标准均被标注为"否"（不适用），与项目实际执行风险管理活动相矛盾。

- Finding ID：`LLM-0048`
- 严重度：`P2`
- Challenge：`revise`
- Agent：Risk Traceability Agent
- 类型：`design_verification_plan_risk_standard_not_applicable_marked`
- 审查理由：F0121第101-104行显示风险相关标准均勾选"否"，但DHF中存在完整的风险管理文件体系（F0017-F0024），且设计验证报告（F0114）引用了风险管理报告。验证计划与实际执行之间的矛盾需要解释。
- Challenge 理由：核心矛盾点成立：E0阶段设计验证计划将风险相关标准标注为'否'，而DHF中存在完整风险管理体系。但原始表述将此定性为直接矛盾过于强硬——E0为早期样机阶段，验证计划中标注'否'可能反映该阶段范围界定（风险管理活动单独管理，不纳入该验证计划覆盖范围），属于文档范围划分问题而非执行缺失。应修订为：E0设计验证计划未将风险标准纳入覆盖范围，需补充说明或适用性评审记录，以消除与实际风险管理活动之间的文档一致性疑问。严重度维持P2。
- 证据：
  - `11 T1样机\设计验证计划E0\设计验证计划-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:101` \| \| 风险 \| YY/T 0316-2016 \| □是 ■否 \| -- \| -- \| -- \| \|
  - `11 T1样机\设计验证计划E0\设计验证计划-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:102` \| \| 风险 \| YY/T 1437-2023 \| □是 ■否 \| -- \| -- \| -- \| \|
  - `11 T1样机\设计验证计划E0\设计验证计划-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:103` \| \| 风险 \| YY/T 1473-2023 \| □是 ■否 \| -- \| -- \| -- \| \|

### S032. 子程序测试记录中记录的软件版本号PT-HT2762-V0029-1.0.0与软件需求规格书、设计方案的版本对应关系在证据目录中缺失

- Finding ID：`LLM-0034`
- 严重度：`P2`
- Challenge：`revise`
- Agent：Software Agent
- 类型：`software_version_traceability_gap`
- 审查理由：SW-139记录了具体软件版本号PT-HT2762-V0029-1.0.0，但证据目录中未见将该版本号与PT9L-RJXQ01（需求规格）、PT9L-RJFA01（设计方案）关联的版本矩阵或配置管理记录。构建和编码文件（SW-084/SW-085）提及追溯表，但追溯表内容未在证据中呈现，无法确认版本一致性闭环。
- Challenge 理由：核心问题部分成立：供应商原图（GXT-001/天津小泉）未转换为本厂标准图号即归档于DHF，这一事实有证据支持（evidence line 8、line 120）。但'散热器压块在总装BOM中以PT3-M01入账'的证据仅来自rationale引用的DMR-125/126，在提供的evidence中未直接体现，属于超出直接证据范围的推断。建议修订：将finding范围收窄至'供应商原图未经本厂标准化转换即归档'，删除或标注为待核实的PT3-M01编号问题，严重度维持P2。
- 证据：
  - `11 T1样机\测试计划及测试记录E0 23.11\子程序测试记录E0 23.11.via_lo_html.clean.md:42` 软件版本：PT-HT2762-V0029-1.0.0
  - `11 T1样机\4 构建和编码E0 23.11.via_lo_html.clean.md:59` 2\. **源代码的可追溯性分析（ T raceability analysis ）**
  - `11 T1样机\4 构建和编码E0 23.11.via_lo_html.clean.md:61` \| 序号. \| 软件需求功能 \| 软件需求描述 \| 软件设计方法 \| 有关子程序 \| 测试方法 \|

### S033. 证据目录中未见独立的软件确认报告，软件质量策划声称包含确认计划但确认执行结果文件无法从现有证据确认存在

- Finding ID：`LLM-0036`
- 严重度：`P2`
- Challenge：`revise`
- Agent：Software Agent
- 类型：`software_validation_report_absence`
- 审查理由：SW-003明确声明软件质量策划包含软件确认计划，SW-004/SW-005规划了确认阶段输出文件要求。但证据目录中仅有子程序测试记录（SW-130至SW-140）和T1样机检测报告（SW-106至SW-111），未见以"软件确认报告"或"软件验证与确认报告"命名的独立文件。YY/T 0664要求软件确认有独立记录，缺失构成法规闭环风险。
- Challenge 理由：核心问题成立：质量策划明确声明包含软件确认计划，但证据目录中无法找到独立的软件确认执行报告，YY/T 0664要求确认活动有独立记录，法规闭环风险真实存在。但原表述将'无法从现有证据确认存在'与'缺失'等同，过于绝对——现有证据仅为目录级扫描，不能排除文件存在于未索引路径。建议将严重度维持P2，但将结论修订为'现有证据目录中未见独立软件确认报告，需补充提供或说明其所在位置'，避免直接断言文件缺失。
- 证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\1 质量策划E0 23.11.via_lo_html.clean.md:50` 本计划作为软件部分的设计和开发策划的结束，识别了必要的任务、阶段，规定了人员职责、必要的资源支持、相关评审要求、各阶段接收准则、软件配置管理要求以及异常报告和解决程序等内容。本软件质量策划在软件生命周期策划部分中包含了软件确认计划相关内容。
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\1 质量策划E0 23.11.via_lo_html.clean.md:72` 5\. **软件生命周期策划及软件确认计划**
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\1 质量策划E0 23.11.via_lo_html.clean.md:74` \| 阶段 \| 主要工作内容 \| 人员职责 \| 输出文件 \| 输出文件要求 \| 相关评审 \| 软件确认接收准则 \|

### S034. T1样机评审检查表中软件功能检查条目（程序版本一致性、通信协议版本、APP/云端版本）全部为空白，T1阶段软件评审结论无法确认

- Finding ID：`LLM-0037`
- 严重度：`P2`
- Challenge：`keep`
- Agent：Software Agent
- 类型：`t1_review_checklist_software_items_blank`
- 审查理由：SW-075/SW-076/SW-077（F0076）和SW-078/SW-079/SW-080（F0078）两份T1样机评审检查表中，软件和功能检查相关条目（第62、90、91项）均为空白复选框，无通过/不通过记录。T1样机阶段是软件功能首次系统验证的关键节点，评审结论空白意味着该阶段软件评审闭环证据缺失。
- Challenge 理由：证据直接且明确：两份T1样机评审检查表（F0076、F0078）中第62、90、91项软件功能检查条目均为空白复选框，无任何勾选记录。T1阶段是软件功能首次系统验证关键节点，评审闭环证据缺失属于实质性质量问题，非误报。严重度P2合理。
- 证据：
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:76` \| 62 \| 软 件 和 功 能 检 查 \| 程序版本文件名与程序自检号一致性检查 \| \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:104` \| 90 \| 软 件 和 功 能 检 查 \| 通信协议版本 \| \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:105` \| 91 \| \| APP/云端版本记录 \| \| □通过 □不通过 □不适用 \|

### S035. DHF主范围文件中混入PT3SBT型号的标签审核表，与PT9L项目无关，构成型号混淆风险。

- Finding ID：`LLM-0052`
- 严重度：`P2`
- Challenge：`revise`
- Agent：V&V Agent
- 类型：`wrong_model_label_audit_in_dhf`
- 审查理由：VV-038所在文件路径为"11 T1样机\\PT3SBT标签审核表（海外更新）"，excluded_from_primary_scope=false，即该文件被纳入主范围。PT3SBT为旧型号，其标签审核结论不能代表PT9L，若监管机构审查时将其误认为PT9L证据，将产生严重法规风险。
- Challenge 理由：核心问题成立：文件路径明确标注"PT3SBT标签审核表（海外更新）"，且excluded_from_primary_scope=false，说明该文件确实被纳入PT9L项目DHF主范围。型号混淆风险客观存在。但原始表述将其定为P1（严重）略有过重——该文件本身不会直接导致产品安全失效，主要风险在于监管审查时的证据混淆和法规符合性声明的准确性。建议将严重度调整为P2，并在表述中明确指出需要确认该文件是否有对应的等同性说明或引用说明，以区分"错误纳入"与"有意引用旧型号数据"两种情形。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:1033` \| (b) \| No exemption depending on insufficiency of label space, as prescribed in regulations promulgated under section 502(b) of the act, shall apply if such insufficiency is caused by:如502(b)法案中规定，不能因为以下原因省略包装上的标识： \| A ...

### S036. 通用要求验证报告中外形/重量和包装要求两项验证结果全部标注为"--"，未实际执行验证。

- Finding ID：`LLM-0054`
- 严重度：`P2`
- Challenge：`keep`
- Agent：V&V Agent
- 类型：`packaging_weight_verification_not_executed`
- 审查理由：VV-098/VV-099显示条目3（外形和重量）和条目4（包装要求）的验证方法、判定准则、结果列均为"--"，而设计输入（VV-016/VV-017）明确要求这两项参见组件规格部分。验证计划（VV-134）中包装要求已列入T1阶段，报告中却无对应结果，存在验证缺口。
- Challenge 理由：证据直接支持结论：line 35和line 36明确显示条目3（外形和重量）和条目4（包装要求）的验证方法、判定准则、结果列均为"--"，即未实际执行验证。设计输入（line 23）已明确列出外形和重量要求，验证计划亦将包装要求列入T1阶段，但验证报告中无对应结果，验证闭环缺口成立。P2定级合理，属于验证执行完整性问题而非直接安全风险。无误报迹象，保留。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:35` \| 3 \| 外形和重量要求 Size and weight \| 详见《设计输入-组件规格部分》中的相关要求 \| -- \| -- \| -- \| -- \| -- \|
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:36` \| 4 \| 包装要求 Packaging \| 详见《设计输入-组件规格部分》中的相关要求 \| -- \| -- \| -- \| -- \| -- \|
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:23` \| 3 \| 外形和重量要求 Size and weight \| 详见《设计输入-组件规格部分》中的相关要求 \| \|

### S037. 设计输入汇总表文件名含日期"20211118"，而设计输入封皮版本为"E0 23.11"，日期不一致，存在版本对应关系不明的风险。

- Finding ID：`LLM-0056`
- 严重度：`P2`
- Challenge：`keep`
- Agent：V&V Agent
- 类型：`design_input_summary_date_mismatch`
- 审查理由：VV-013显示汇总表文件名为"设计输入汇总表E0 20211118"，VV-001/VV-002显示封皮版本为"E0 23.11"（2023年11月）。两者相差约两年，若汇总表未随封皮同步更新，则封皮所声明的设计输入范围与实际汇总内容可能不一致。
- Challenge 理由：证据直接支持结论：汇总表文件名含'20211118'，而所在文件夹及封皮版本均为'E0 23.11'（2023年11月），两者相差约两年。若汇总表内容未随封皮同步更新，则封皮声明的设计输入范围与实际汇总内容可能不一致，属于版本控制风险。证据充分，非误报，维持P2。
- 证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:2` # 设计输入汇总表E0 20211118
  - `04 设计输入E0 23.11\QR-7.3-05设计输入(封面)E0  23.11.via_lo_html.clean.md:2` # QR-7.3-05设计输入(封面)E0 23.11
  - `04 设计输入E0 23.11\QR-7.3-05设计输入(封面)E0  23.11.via_lo_html.clean.md:6` 文件编号 : PT9L-SJSR01 V1.0 设计输入 表号 : QR-7.3-05/E0

### S038. 手板样机设计评审记录中设计验证报告评估栏四个选项均为"□"，未勾选任何验证状态，评审结论不完整。

- Finding ID：`LLM-0057`
- 严重度：`P2`
- Challenge：`keep`
- Agent：V&V Agent
- 类型：`design_review_record_verification_status_unchecked`
- 审查理由：VV-031~VV-036显示评审记录中"有设计验证报告"及后续四个互斥选项（合格/未按计划/未完成/有不合格项）均为"□"，且VV-031显示"□有：设计验证报告文件编号："后为空。评审计划（VV-030）要求验证条目需通过，但评审记录未记录验证状态，评审闭环存在缺口。
- Challenge 理由：证据直接支持结论：评审记录中'□有：设计验证报告文件编号：'后为空，且后续四个互斥验证状态选项均为'□'未勾选，评审闭环存在明确缺口。该问题在医疗器械设计控制中属于实质性记录不完整，非误报，维持P2。
- 证据：
  - `11 T1样机\10 评审E1 23.11\手板样机设计评审记录E0 23.11.via_lo_html.clean.md:38` □ 有：设计验证报告文件编号：
  - `11 T1样机\10 评审E1 23.11\手板样机设计评审记录E0 23.11.via_lo_html.clean.md:40` 对设计验证报告的评估： *（如有设计验证填写本栏）*
  - `11 T1样机\10 评审E1 23.11\手板样机设计评审记录E0 23.11.via_lo_html.clean.md:42` □ 本次设计验证已按验证计划进行并完成，且验证项合格；

### S039. 外观图（PT9L-F01 V1.0）仅标注上盖白色，未标注Cool Gray 8U装饰色规格，与彩包装图（DMR-082）描述的橙/白双色外观存在潜在不一致，外观验收标准不完整。

- Finding ID：`LLM-0066`
- 严重度：`P3`
- Challenge：`revise`
- Agent：DMR/SOP Agent
- 类型：`appearance_drawing_color_spec_incomplete`
- 审查理由：DMR-140指出外观图'只标了上盖白色，未提Cool Gray 8U上盖装饰'，且注明'高概率取消，待工程师确认'。若外观图颜色规格未最终确认，则产品缺陷定义（DMR-013）中的外观缺陷等级评价缺乏完整基准，影响出货检验。
- Challenge 理由：核心问题成立：外观图PT9L-F01 V1.0仅标注上盖白色，未标注Cool Gray 8U装饰色规格，与彩包装图DMR-082描述的橙/白双色外观存在潜在不一致，且DMR-140已注明'高概率取消，待工程师确认'，说明该颜色规格处于未决状态。这直接影响出货检验中外观缺陷等级评价的基准完整性，问题属实。但当前P2定级偏高：DMR-140已有内部标注提示待确认，说明设计团队已知晓该问题并在跟进，且'高概率取消'意味着该装饰色可能已被设计决策移除，实际风险可能低于P2。建议降为P3，并修改表述为'外观图颜色规格存在未关闭的设计决策，需确认Cool Gray 8U装饰色是否已正式取消并同步更新外观验收标准'，避免将'待确认'状态直接等同于'不一致缺陷'。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:1` # PT9L 外观图 V1.0 (2024-06-27) 2D 图读图报告
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT9L-外观图-v1.0-20240627.pdf`
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:14` \| **Drawing NO.** \| **PT9L-F01**（⚠️ 与外箱 PT9L-F01 同号但不同件） \|

### S040. 低电压第一阶段触发阈值在构建编码文件与软件测试记录之间存在描述差异（2.5~2.7V vs 2.65V），需确认实际固件实现值。

- Finding ID：`LLM-0023`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Hardware Agent
- 类型：`low_voltage_threshold_discrepancy`
- 审查理由：HW-039（构建和编码）描述第一阶段低电为"2.5V–2.7V"区间，HW-113（软件系统测试记录）测试用例使用2.65V触发低电提示，HW-114（测试记录行100）又出现2.8V时"空心电池图标"的描述。三处数值不完全一致，若固件实际阈值与验证用例不符，则低电检测功能验证结论的有效性存疑。
- Challenge 理由：核心问题（PT9C文件混入PT9L DHF）成立：文件路径明确位于PT9L DHF的
- 证据：
  - `11 T1样机\4 构建和编码E0 23.11.via_lo_html.clean.md:67` \| 5 \| 低电压检测功能 \| 低电提示分两阶段，当电量低于第一阶段时，能够保证设备至少能测量20次，当电量低于第二阶段时，设备关机 \| 1. 如果电源电压 2.5V – 2.7V时，LCD能提示低电压并保存低电状态，直至下次重新上电后再检测；<br>2. 如果电源电压小于2.5V时，LCD提示超低电压后关机，一直保存此状态，直至下次重新上电后再检测； \| Uint16_t GetBatValue () \| S.O.C.I \|
  - `11 T1样机\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:99` \| 2 \| 将电压调到2.65V，开机 \| LCD提示低电压，实心电池图标常亮 \| I，O \|
  - `11 T1样机\测试计划及测试记录E0 23.11\软件系统测试记录 E0 23.11.via_lo_html.clean.md:100` \| \| 不断电，将电压调到2.8V \| 按测量键，LCD显示,空心电池图标常亮 \| I，O \|

### S041. 主范围结构设计方案评审检查表（F0035）文件名及标题均标注"血压计"，与PT9L红外体温计品类不符。

- Finding ID：`LLM-0005`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Market & Category Scout Agent
- 类型：`legacy_category_in_primary_scope`
- 审查理由：F0035文件标题为"结构设计方案评审检查表-血压计E0 23.11"，该文件位于PT9L DHF主范围的05结构设计方案文件夹中。品类错误的评审检查表若被用于PT9L结构设计评审，将导致评审准则与产品实际品类不匹配，影响设计验证闭环。
- Challenge 理由：三条证据直接支持核心问题：文件标题为'PT3SBT标签审核表（海外更新）'，内容产品型号为PT2L，引用PT2L系列文件编号，与PT9L项目无直接关联，确属旧型号文件残留混入DHF。核心问题成立，但该文件为标签审核表，属于参考性/历史性文件，对PT9L标签符合性追溯的实际干扰程度相对有限（不涉及风险控制闭环或测试报告），P2严重度略偏高，建议降为P3，并在表述中明确该文件为历史遗留参考文件而非PT9L现行受控文件，以准确反映风险等级。
- 证据：
  - `05 结构设计方案E0 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2` # 结构设计方案评审检查表-血压计E0 23.11

### S042. 设计验证报告封皮的'验证合格'与'验证不合格'复选框均未勾选，正式验证结论缺失，法规闭环不完整。

- Finding ID：`LLM-0013`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Regulatory Agent
- 类型：`design_verification_report_conclusion_not_signed`
- 审查理由：REG-138和REG-139显示封皮两个结论选项均为'☐'空白状态，无法确认验证是否已正式通过。ISO 13485及FDA 21 CFR 820均要求设计验证有正式书面结论，空白封皮不满足该要求。
- Challenge 理由：核心问题成立：测试报告电池容量1000mAh与BOM出货电池1200mAh不一致，测试代表性存疑。但原rationale已自行分析'测试电池容量低于出货电池则结果偏保守尚可接受'，说明该差异在最坏情况下对安全性影响有限，属于文件记录规范性问题而非直接安全风险。严重度从P2下调至P3更为合适，同时建议表述聚焦于'测试电池与出货电池规格不一致，需补充说明或重新测试'。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:28` ☐设计验证合格：所有设计验证项目已按照相应的设计验证计划进行，都已验证通过合格。
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-设计确认阶段E0  23.11-加结论.via_lo_html.clean.md:30` ☐设计验证不合格：

### S043. 所有生物相容性测试报告均以PT5为受试样品，证据目录中未见PT9L材料等同性桥接文件，生物相容性法规证据闭环存在缺口。

- Finding ID：`LLM-0015`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Regulatory Agent
- 类型：`biocompatibility_reports_based_on_pt5_not_pt9l`
- 审查理由：REG-090~REG-119共涉及F0104~F0108五份报告，报告编号均含'PT5'，测试样品为PT5产品。说明书REG-067声明PT9L材料通过ISO 10993-5/10993-10，但无PT9L专属报告或材料等同性评估文件支撑，不满足ISO 10993-1:2018的桥接要求。
- Challenge 理由：核心观察属实但严重度偏高。关键细节：'血压测量'字样仅出现在F0121设计验证计划的未勾选选项中，该条目最终勾选为'■无要求'；对比证据显示设计输入汇总表（04目录）和设计验证报告中对应条目均已改为'次测量'（无'血压'字样），说明模板清理在主要文件中已完成，仅验证计划一处存在残留。该问题属于文件质量轻微缺陷，不影响产品符合性判断，P3严重度合理，但P3已是最低级，建议表述调整为'轻微文件质量缺陷，建议在下一版本修订时清理'，不宜夸大法规审查风险。
- 证据：
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:162` (8) The materials (ABS, TPU, PMMA, PC) of expect contact with patient have passed the ISO 10993-5 and ISO 10993-10 standards test, no toxicity, allergy and irritation reaction. They are in compliance with the Medical Dev...
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:25` 参照 GB/T 16886.10-2017
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:144` GB/T 16886.10-2017 医疗器械生物学评价 第 10 部分：刺激与皮肤致敏试验

### S044. 风险管理计划（F0017/F0021）版本均为V1.0（2024.02.02），而风险评价报告和风险控制验证报告均已更新至V2.0（2024.05.30），计划文件未同步更新。

- Finding ID：`LLM-0044`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Risk Traceability Agent
- 类型：`risk_management_plan_version_frozen_at_v1`
- 审查理由：ISO 14971要求风险管理计划应覆盖整个产品生命周期活动。若评价报告和验证报告在V2.0中有实质性变更（如危害序列调整），而计划文件未更新，则计划与执行之间存在不一致，影响法规符合性声明。
- Challenge 理由：核心观察成立：风险管理计划停留在V1.0（2024.02.02），而评价报告和验证报告已升至V2.0（2024.05.30）。但证据仅证明版本号差异，未能证明计划内容与V2.0报告存在实质性不一致（V2.0变更记录显示仅为问题清单更新和措辞改写，非危害序列重大调整）。ISO 14971要求计划覆盖生命周期活动，但不强制计划版本号与执行报告同步更新。P1定级偏高，应降为P3，表述应聚焦于'计划版本未随执行文件更新，需确认计划内容是否仍覆盖V2.0报告所描述的活动范围'，而非直接断言法规符合性受损。
- 证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： IFT -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:23` \| 2 \| 2024.5.30 \| 1. Question list has been updated according to Annex A of ISO/TR 24971:2020<br>2. Content of risk control measures has been reworded to better describe the development control process \| V2.0 \| Wang Di \|...

### S045. 可追溯性分析报告（F0252）在验证与确认阶段引用风险评价报告PT9L-FXPJ01 V1.0，但文件目录中已存在V2.0版本，引用版本未更新。

- Finding ID：`LLM-0049`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Risk Traceability Agent
- 类型：`traceability_report_references_v1_while_v2_exists`
- 审查理由：可追溯性报告作为设计确认的汇总文件，若引用的风险文件版本已被更新版本替代，则追溯链路指向过时文件，可能导致审查员误判风险管理活动的完整性。
- Challenge 理由：核心问题成立：可追溯性分析报告引用V1.0，而目录中已存在V2.0，属于文档版本管理缺陷，证据直接支持。但原定P3严重度合理，无需上调。表述可精确化：该问题属于文档维护缺陷，不直接影响风险控制有效性，但会导致审查员追溯链路指向过时版本，需在可追溯性报告中更新引用至V2.0并说明版本变更影响评估。
- 证据：
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:18` \| 软件需求分析阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \| \| 相关文档之间的信息描述都是准确的 \| \| 相关文档之间的信息都是正确的，没有歧义信息 \| \| 相关文档已包含软件必需信息，陈述所有功能 \| \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|
  - `18 设计确认\可追溯性分析报告.via_lo_html.clean.md:28` \| 验证与确认<br>阶段 \| 风险管理 \| 风险管理计划<br>PT9L-FXJH01<br>风险评价报告<br>PT9L-FXPJ01 V1.0 \| \| 相关文档之间的信息描述都是准确的 \| \| 相关文档之间的信息都是正确的，没有歧义信息 \| \| 相关文档已包含软件必需信息，陈述所有功能 \| \| 相关文档之间没有自相矛盾及互相矛盾，与产品说明无矛盾 \|
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable

### S046. PT9L软件设计方案文件夹下存放BP3L旧型号软件图样，该文件未被排除出主范围，构成法规验证闭环污染风险

- Finding ID：`LLM-0029`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Software Agent
- 类型：`legacy_model_document_in_primary_scope`
- 审查理由：SW-014/SW-015/SW-016/SW-017/SW-018/SW-019均来自F0052，文件标题明确为"BP3L 软件图样"，路径位于"07 软件设计方案E0 23.11\\软件图样E0 23.11"主文件夹内，excluded_from_primary_scope=false。BP3L为血压计旧型号，其软件图样出现在IFT红外体温计PT9L的软件设计方案目录中，审查员或监管机构可能将其误认为PT9L的设计输出，导致验证闭环边界不清。
- Challenge 理由：证据直接支持PT3SBT标签审核表错误归档于PT9L的T1样机文件夹这一事实（路径和文件名均明确）。核心问题成立，属于文件管控缺陷。但P2严重度偏高：该文件为标签审核表而非验证报告或技术规格，被误引用为PT9L符合性证据的实际风险较低，且文件名已明确标注PT3SBT，审查员不易混淆。建议降级为P3，表述调整为'文件归档管控缺陷'，重点指出需清理或移至正确位置，而非强调法规符合性风险。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:24` **历史版本记录**
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:26` \| **序号** \| **更改日期** \| **版本描述** \| **版本** \| **更改人** \| **批准人** \|

### S047. 软件图样评审计划及评审记录所指向的评审对象疑为BP3L图样而非PT9L图样，评审有效性存疑

- Finding ID：`LLM-0033`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Software Agent
- 类型：`software_diagram_review_object_mismatch`
- 审查理由：SW-020至SW-024（F0053）为软件图样评审计划，SW-025/SW-026（F0054）为软件图样评审记录，均与F0052（BP3L软件图样）同处"软件图样E0 23.11"子文件夹。若该评审计划和记录是针对BP3L图样发起的，则PT9L软件图样评审可能从未执行；若是针对PT9L但误用了BP3L图样文件，则评审输入有误。两种情形均构成一致性风险。
- Challenge 理由：核心问题成立：两份包装BOM文件确实存在文件编号字符不一致（'PBOM01'含空格 vs 'PB0M1'字母O与数字0混用），属于文件受控管理缺陷。但该问题本质为文件编号录入/OCR转换错误，尚未证明两份文件内容存在实质性差异（rationale仅称'物料条目基本相同'），实际制造引用风险相对可控。原P2严重度偏高，建议降为P3，同时建议表述聚焦于'文件编号不规范导致唯一受控版本不明确'而非暗示存在两个竞争版本。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\QR-7.3-08设计评审计划表-图样评审E0 23.11.via_lo_html.clean.md:12` **评审阶段：** 图样评审:□结构图样评审 □硬件图样评审 ☑软件图样评审
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\QR-7.3-08设计评审计划表-图样评审E0 23.11.via_lo_html.clean.md:30` 2.软件图样评审内容表中，所有条目需识别其适用性，适用的条目需评估其是否通过；
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\QR-7.3-08设计评审计划表-图样评审E0 23.11.via_lo_html.clean.md:50` 技术负责人:对软件图样设计询问信息、提出问题等，对其可行性、合理性等进行评审；

### S048. 结构类FMEA文件中产品型号KD-5915L与PT9L混用，同一文件内出现两个不同型号标识

- Finding ID：`LLM-0035`
- 严重度：`P3`
- Challenge：`keep`
- Agent：Software Agent
- 类型：`dfmea_product_model_inconsistency`
- 审查理由：SW-072/SW-073（F0074 line 13和line 189）显示产品型号为KD-5915L，而SW-074（同文件line 370）显示产品型号为PT9L。同一FMEA文件内型号标识不一致，表明该文件可能由旧型号文件修改而来且未完整替换，影响FMEA分析结论与PT9L产品的对应有效性。
- Challenge 理由：证据直接支持结论：设计输出清单一表头'提交：年月日 审核：年月日'字段均为空白，文件受控状态不完整。作为DHF核心索引文件，批准日期缺失影响设计冻结时间线可追溯性，属于文件控制程序缺陷（ISO 13485 4.2.4要求受控文件标识包括批准状态）。非误报，严重度P3合理（属模板/质量风险而非安全风险）。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:13` \| \| 产品型号： \| KD-5915L \| \| \| 审核： \| \| \| \| \| \| \| \| \| FMEA版本： \| V1.0 \| \| \| \| \| \| \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:189` \| \| 产品型号： \| KD-5915L \| \| \| 编制： \| \| \| \| \| \| \| \| \| \| FMEA版本： \| V1.0 \| \| \| \| \| \|
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:370` \| \| 产品型号： \| PT9L \| \| \| 审核： \| \| \| \| \| \| \| \| \| FMEA版本： \| V1.0 \| \| \| \| \| \| \|

### S049. 软件需求规格评审计划中引用的附表文件编号PT9L-RXPB01与软件方案评审计划引用的PT9L-RFPB01格式不一致，存在文件编号规则混乱风险

- Finding ID：`LLM-0038`
- 严重度：`P3`
- Challenge：`revise`
- Agent：Software Agent
- 类型：`software_requirement_spec_review_plan_doc_id_mismatch`
- 审查理由：SW-058（F0061）记录需求规格评审附表编号为PT9L-RXPB01，SW-038（F0057）记录方案评审附表编号为PT9L-RFPB01，两者编号中间段字母不同（RX vs RF），但对应的检查表文件（F0063和F0059）均已存在。编号规则差异属于轻微质量风险，但若编号体系不统一可能在文件索引和追溯时造成混淆。
- Challenge 理由：核心事实成立：两份评审计划引用的附表编号中间段字母确实不同（RXPB01 vs RFPB01），编号规则存在不一致。但证据同时显示对应检查表文件（F0063、F0059）均已实际存在，说明文件本身可追溯，不构成法规闭环断裂，仅为文件编号命名规范问题。原P3严重度已属较低，但表述中'文件编号规则混乱风险'略有夸大，建议修订为'文件编号命名不一致，建议统一编号规则以避免索引混淆'，严重度降为P3维持。
- 证据：
  - `07 软件设计方案E0 23.11\软件需求E0 23.11\QR-7.3-08设计评审计划表-方案评审E0 23.11.via_lo_html.clean.md:16` 1\. 对软件需求规格的评估:评审内容见附表（文件编号： PT9L -RXPB01 V1.0 ）；
  - `07 软件设计方案E0 23.11\软件方案E0 23.11\QR-7.3-08设计评审计划表-方案评审E0  23.11.via_lo_html.clean.md:16` 1\. 对软件设计方案的评估:评审内容见附表（文件编号： PT9L -R F PB01 V1.0 ）；
  - `07 软件设计方案E0 23.11\软件需求E0 23.11\软件需求规格书评审检查表E0 23.11.via_xlsx.clean.md:2` # 软件需求规格书评审检查表E0 23.11

### S050. 性能规格验证报告（F0112）Sheet名为"组件验证报告"，但文件标题和内容均为"性能规格部分"，存在Sheet命名与内容不符的一致性风险。

- Finding ID：`LLM-0058`
- 严重度：`P3`
- Challenge：`revise`
- Agent：V&V Agent
- 类型：`performance_verification_report_sheet_name_mismatch`
- 审查理由：VV-082显示Sheet名为"组件验证报告"，VV-083/VV-084显示内容标题为"设计验证报告-性能规格部分"，验证依据为"PT9L-YZXN01"（性能规格计划）。Sheet命名错误可能导致文件管理混乱，在审查时引发对报告归属的质疑。
- Challenge 理由：核心问题成立：Sheet名'组件验证报告'与文件内容标题'设计验证报告-性能规格部分'确实不符，存在文档管理一致性风险。但该问题属于Excel Sheet命名错误，不影响验证内容本身的完整性和可追溯性，实质危害有限，P2偏高。建议降为P3，并将表述调整为'文档命名一致性缺陷，可能在审查时引发混淆，建议更正Sheet名称'。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:6` ## Sheet: 组件验证报告
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:8` 设计验证报告-性能规格部分
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:14` 阶段：T1 验证依据：PT9L设计验证计划-性能规格部分（文件编号：PT9L-YZXN01 V1.0）


## 7. 语义待人工补证疑点（未计入确认错误）

### P001. 外观图（F0177）与外箱图纸（F0164）的Drawing NO.均为PT9L-F01，但两者为不同物件，图号冲突将导致图纸管理混乱和制造转移错误风险。

- Finding ID：`LLM-0062`
- 严重度：`P1`
- Agent：DMR/SOP Agent
- 类型：`drawing_number_collision`
- 未决原因：核心问题（同一图号PT9L-F01对应两个不同物件）若属实则严重，但关键证据存在可信度疑点：外观图证据行中的'⚠️ 与外箱 PT9L-F01 同号但不同件'标注格式高度疑似AI解析注释而非原始PDF内容，原始图纸标题栏通常不含此类警告文字。需人工核查原始PDF确认该标注是否真实存在于原始文件中，或仅为解析工具添加的推断注释。若注释为AI添加，则两图号相同的结论仍可能成立，但需独立验证。
- 现有证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-外观图-v1.0-20240627.pdf.md:14` \| **Drawing NO.** \| **PT9L-F01**（⚠️ 与外箱 PT9L-F01 同号但不同件） \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:20` \| **Drawing NO.** \| PT9L-F01 \|
  - `12 设计输出（含01、02）\设计输出清单二\包装\K040100014357620814-图纸-PT9L-F01+V1.0.pdf.md:23` \| **Model NO.** \| PT9L \|

### P002. 主范围风险控制验证报告（F0019）正文中出现旧型号PT3SBT，而非PT9L，导致预期用途描述与本项目不符。

- Finding ID：`LLM-0001`
- 严重度：`P1`
- Agent：Market & Category Scout Agent
- 类型：`legacy_model_in_primary_scope`
- 未决原因：rationale声称F0019第85行明确写'PT3SBT can transmit the temperature...'，但实际提供的证据文本（line 85）内容为通用预期用途描述'The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature...'，完全未出现'PT3SBT'字样。证据文本与claim所引用的具体字符串不匹配，无法从现有证据直接验证结论。同时F0020（line 78）的证据文本与F0019（line 85）内容几乎相同，亦未见PT9
- 现有证据：
  - `03 风险分析\Attachment 7 03 Verification of risk control measure and residual risk evaluation report IFT-FXYS01  V2.0 2024053-All appli.via_lo_html.clean.md:85` The Infrared Forehead Thermometer is intended for the intermittent measurement of body temperature from the forehead skin surface on people of all ages. It can be used by consumers in the household environment and by hea...

### P003. 结构类FMEA中将产品描述为'血压计'，与PT9L红外体温计品类不符，构成法规/验证闭环风险。

- Finding ID：`LLM-0012`
- 严重度：`P1`
- Agent：Regulatory Agent
- 类型：`dfmea_wrong_product_category_reference`
- 未决原因：证据显示两份BOM中均含PT9C-CNTP01料号，核心观察属实。但现有证据未能排除以下合理解释：PT9C-CNTP01可能是PT9L机芯中某子模块（如连接板）的共用PCB，型号前缀不同不必然意味着跨型号混入；BOM结构（行号43 vs 行号50）显示两块PCB可能分属不同子组件层级。需人工核查BOM层级结构、PT9C-CNTP01的实际用途说明及ECO记录，方可判定是否构成法规符合性风险。
- 现有证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:22` \| \| 铭牌 \| 给用户关于机器的信息 \| 铭牌印刷内容容易被擦拭掉 \| 用户无法识别血压计的相关法规信息 用户误用 \| 4 \| C \| 铭牌未覆膜 \| 2 \| \| 依IEC60601-1:2005 电气安全通用要求中7.1.3 标记耐久性要求 对铭牌进行试验 \| 2 \| 16 \| \| \| \| \| \| \| \| \| \|

### P004. DHF中存在两套平行风险文件：IFT前缀（F0017-F0020）与PT9L前缀（F0021-F0024），均为同名文件，未明确哪套为正式受控版本。

- Finding ID：`LLM-0040`
- 严重度：`P1`
- Agent：Risk Traceability Agent
- 类型：`duplicate_parallel_risk_file_set`
- 未决原因：证据确认DHF中存在IFT前缀和PT9L前缀两套同名风险文件，问题方向成立。但仅凭文件名和首行内容无法判断：(1)两套文件内容是否完全相同或存在实质差异；(2)是否有文件控制记录说明IFT版本为历史版本/草稿而PT9L版本为正式受控版本（或反之）；(3)是否存在文件变更说明解释前缀变更原因。若两套文件内容一致且有明确的版本迭代说明，则可能降级为P2文件管理问题；若内容存在差异且均处于受控状态，则应升级为P0。需人工核查两套文件的完整内容及文件控制记录后再做最终裁决。
- 现有证据：
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable
  - `03 风险分析\Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:6` DN ： IFT -FXJH01 V 1 .0 Risk Management Plan
  - `03 风险分析\PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 01 Risk Management Plan IFT-FXJH01 V1.0 20240202-All applicable

### P005. 生物相容性报告（皮肤刺激、皮肤致敏、细胞毒性）均以PT5为受试样品，未见PT9L专属生物相容性评价证据。

- Finding ID：`LLM-0053`
- 严重度：`P1`
- Agent：V&V Agent
- 类型：`biocompatibility_report_wrong_model`
- 未决原因：证据确认生物相容性报告均以PT5为受试样品，文件路径含"同PT5生物相容性报告"，报告标题指向PT5型号，这一事实无误。但核心判断依据在于PT9L与PT5的接触材料是否存在差异：若DHF中存在材料等同性声明（Material Equivalence Statement）或生物相容性评价总结报告明确说明PT9L与PT5接触材料相同并引用PT5数据，则直接引用PT5报告在ISO 10993框架下是合规的；若无此类桥接文件，则构成实质性法规缺口。当前证据仅显示报告存在，未能确认是否存在等同性桥接文件，需人工复核DHF中生物相容性评价总结或材料清单比对文件后方可定性。
- 现有证据：
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激1-SDWH-M201905262-4.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤刺激2-SDWH-M201905262-5.pdf.md:178` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。
  - `11 T1样机\生物相容性\同PT5生物相容性报告\PT5-生物相容性-皮肤致敏1-SDWH-M201905262-2.pdf.md:183` ISO/IEC 17025:2005 检测和校准实验室能力的通用要求（CNAS-CL01《检测和校准实验室能力认可准则》）中国合格评定国家认可委员会实验室认可注册号：CNAS L2954。

### P006. 散热器金属套图纸（75CEE0-Model.pdf）为外购供应商图号（GXT-001/天津小泉），尚未完成内部标准图号映射，制造转移资料中图号体系不统一。

- Finding ID：`LLM-0063`
- 严重度：`P2`
- Agent：DMR/SOP Agent
- 类型：`supplier_drawing_internal_number_not_mapped`
- 未决原因：证据仅证明该图纸为外购供应商图纸（天津小泉），但finding的核心主张——'尚未完成内部标准图号映射'——所依赖的关键证据（DMR-123中'是否需要换为本厂标准化T-Z1-Pxx图号'的待确认问题）未出现在所提供的evidence文本中，三条evidence均未包含该内容。无法排除该待确认问题本身是AI推断而非原始文档记录。外购件使用供应商图号在工业实践中也属常见做法，不必然构成合规风险。需提供DMR-123原始文本作为补充证据。
- 现有证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:8` > **关键背景**：本图非 T-Z1/PT9L 自制结构件，是 **外购供应商图纸**（天津小泉精密金属制品有限公司 2018-09-17），用于 PT9L 红外探头组件中的"散热器金属套"，与 `FDIR-V14_散热器压块_REV01_0714.pdf` 配合使用（见技术要求第 4 条）。
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:101` ## 4. 装配 / 约束推断（B 级）
  - `12 设计输出（含01、02）\设计输出清单二\图纸\75CEE0-Model.pdf.md:107` - **总长 11.79⁻⁰·⁰⁵⁻⁰**：**只能小不能大**——避免影响装配链。

### P007. T1样机评审检查表中含"电池不能和袖带相邻存放"检查项，袖带为血压计专用部件，与IFT品类不符。

- Finding ID：`LLM-0025`
- 严重度：`P2`
- Agent：Hardware Agent
- 类型：`sample_review_checklist_cross_contamination`
- 未决原因：证据仅能证明EMC型式试验报告要求pass/fail准则应纳入风险管理文件（line 622），以及风险管理报告文件存在（line 2/6）。但现有evidence未展示风险管理报告的实际内容，无法确认EMC免疫性风险条目是否已被识别和纳入。风险管理报告（F0024）的证据仅覆盖文件头部，缺少正文内容佐证。需人工查阅PT9L-FXGB01风险管理报告正文，确认是否包含EMC免疫性风险条目后方可定性。
- 现有证据：
  - `11 T1样机\10 评审E1 23.11\PT9L-T1样机评审检查表E0 23.11.via_xlsx.clean.md:38` \| 24 \| 装 配 检 查 \| 电池不能和袖带相邻存放 \| \| □通过 □不通过 □不适用 \|
  - `11 T1样机\10 评审E1 23.11\T1样机评审检查表E0 23.11.via_xlsx.clean.md:38` \| 24 \| 装 配 检 查 \| 电池不能和袖带相邻存放 \| \| □通过 □不通过 □不适用 \|

### P008. 主范围设计输入汇总表（F0031）与历史草稿（F0319）在EN ISO 80601-2-56和MDR 2017/745适用性勾选上存在矛盾，正式版本选项需复核。

- Finding ID：`LLM-0010`
- 严重度：`P2`
- Agent：Market & Category Scout Agent
- 类型：`regulatory_standard_applicability_discrepancy`
- 未决原因：现有证据仅展示两套文件中各一行文本完全一致，不足以证明
- 现有证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:134` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| ISO 80601-2-56:2017/Amd1:2018 \| 欧盟 \| □是 ■否 \| \|
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:143` \| 欧盟指令 \| MDR 2017/745 \| \| 欧盟 \| □是 ■否 \| \|
  - `历史记录\PT9LDHF-草稿\04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:127` \| 行业标准 \| EN ISO 80601-2-56:2017+A1:2018 \| \| 欧盟 \| ■是 □否 \| \|

### P009. 说明书声明符合ISO 80601-2-56但'except of clause 5.2.2'，该豁免条款未在设计输入或风险文件中找到正式说明。

- Finding ID：`LLM-0019`
- 严重度：`P2`
- Agent：Regulatory Agent
- 类型：`iso_80601_2_56_exception_clause_5_2_2_not_justified`
- 未决原因：证据仅引用了第16、17行两个条目显示为未勾选，原finding声称'所有评审条目结论栏均为空白'但证据不足以支持'全部'这一表述。更重要的是，xlsx文件经由转换工具（via_xlsx.clean.md）处理后，checkbox勾选状态在Markdown中可能无法正确还原——已勾选的☑可能被渲染为□。需要人工核查原始xlsx文件中的实际勾选状态，方可确认评审记录是否真正缺失结论。在文档转换保真度未确认前，存在较高误报风险。
- 现有证据：
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:134` (14) This infrared thermometer meets requirements established in ISO 80601-2-56:2017+A1:2018 and ASTM Standard(E1965-98) except of clause 5.2.2. It displays subject’s temperature over a range of 89.6℉~109.2℉(32℃-42.9℃). ...
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:133` \| 行业标准 \| ISO 80601-2-56:2017/Amd1:2018 \| \| 国际 \| ■是 □否 \| \|

### P010. 设计输入和设计验证报告均未勾选CE认证，但说明书和风险文件多处引用EN标准，市场范围与标准引用存在不一致。

- Finding ID：`LLM-0020`
- 严重度：`P2`
- Agent：Regulatory Agent
- 类型：`ce_market_not_selected_but_eu_standards_referenced`
- 未决原因：证据显示追溯表表头存在（序号、软件需求功能、软件需求描述、软件设计方法、有关子程序、测试方法），但填写内容未出现在证据目录中。这有两种解释：①追溯表确实未填写；②追溯表内容存在于同一文件的后续行或单独文件中，但未被纳入当前证据集。构建和编码文档（via_lo_html.clean.md）的截取范围不明，无法排除内容存在于文件其他部分的可能性。需人工核查完整的构建和编码文件及相关附件，确认追溯表是否有实质填写内容后再做最终裁决。
- 现有证据：
  - `04 设计输入E0 23.11\设计输入汇总表E0  20211118.via_xlsx.clean.md:22` \| 2 \| 销售地区及认证 Intended markets and certification \| 要求符合如下认证体系要求： □ CE 对应地区： 欧洲 ■ FDA 对应地区：美国 □ CFDA 对应地区：中国 □ 其他 \| \|
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:34` \| 2 \| 销售地区及认证 Intended markets and certification \| 要求符合如下认证体系要求： □ CE 对应地区： 欧洲 ■ FDA 对应地区：美国 □ CFDA 对应地区：中国 □ 其他 \| □手板□T1■设计确认 \| -- \| -- \| -- \| -- \|
  - `11 T1样机\PT9L-operation guide-20240828.via_lo_html.clean.md:506` IEC 60601-1:2005+A1:2012+A2:2020/ EN 60601-1:2006/A2:2021 (Medical electrical equipment - Part 1: General requirements for basic safety and essential performance).

### P011. 用户现场测试计划（F0260）文件名含PT9C，但内容包含风险评估条款，未见PT9L对应版本的用户测试计划证据。

- Finding ID：`LLM-0046`
- 严重度：`P2`
- Agent：Risk Traceability Agent
- 类型：`user_test_plan_wrong_model_residual`
- 未决原因：证据仅能证明文件名含'PT9C'且内容包含风险评估条款，但无法排除以下合理情形：(1)该PT9C版本测试计划被PT9L项目正式复用并经过适用性评审；(2)存在PT9L专属用户测试计划但未被检索到。当前证据不足以直接支持'PT9L风险闭环证据存疑'的结论，需人工确认PT9L项目是否存在独立用户测试计划或对PT9C版本的适用性声明。
- 现有证据：
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:87` 4\. 测试人员在评审用户现场测试记录表中的用户使用过程记录时，检查用户操作是否正确。若操作过程中发现异常情况或新的风险，应进行记录；
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:151` **风险评估：**
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:153` 是否发现新的风险 ｜ □未发现 □有新风险，解决方案：

### P012. EMC型式试验报告（F0456）明确要求免疫通过/失败准则应纳入风险管理文件，但现有证据目录中未见风险管理文件包含EMC免疫准则的对应条款。

- Finding ID：`LLM-0047`
- 严重度：`P2`
- Agent：Risk Traceability Agent
- 类型：`emc_immunity_criteria_risk_file_linkage_unverified`
- 未决原因：证据仅引用了EMC报告中的注释条款（要求准则应纳入风险管理文件），以及风险评估报告的文件标题行，并未实际检索风险评估报告的正文内容以确认EMC危害场景是否存在。结论'风险管理文件未包含EMC相关危害场景'属于未经验证的推断。需人工检索F0018/F0022正文，确认是否存在EMC相关危害识别和免疫准则条款后方可定性。
- 现有证据：
  - `实验报告\最终报告\2024-08-15 TX202303-07-078-01 PT9L EMC  型式试验报告英文.pdf.md:622` \| Note 1: Specific, detailed immunity pass/fail criteria, shall be based on applicable part two standards or risk management, for immunity with regard to em disturbances. These pass/fail criteria shall be included in the...
  - `03 风险分析\Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable
  - `03 风险分析\PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md:2` # PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable

### P013. 软件质量策划评审检查表、软件需求规格书评审检查表、软件设计方案评审检查表的评审结论栏全部为空白复选框，评审是否通过无法确认

- Finding ID：`LLM-0030`
- 严重度：`P2`
- Agent：Software Agent
- 类型：`review_checklist_result_blank`
- 未决原因：提供的证据（line 22、28、38）仅显示设计评审计划表的接收准则文本，并未直接展示'有设计验证报告'及四种验证完成状态均为□未选中的具体证据行。rationale中引用的VV-031~VV-036内容未在evidence中体现，无法从现有证据直接核实封皮/记录栏位的空选状态。此外，手板样机阶段（模具样机评审）与T1阶段验证报告的时序关系需要确认——若评审时验证尚未完成，空选可能是正常状态而非缺陷。需人工复核VV-031~VV-036原始记录及评审时间节点。
- 现有证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:16` \| 1 \| 软件生命周期及软件确认计划 \| 是否策划了软件生命周期 \| \| □通过 □不通过 □不适用 \| \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:17` \| 2 \| 软件生命周期及软件确认计划 \| 软件生命周期的划分是否适宜 \| \| □通过 □不通过 □不适用 \| \|
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:18` \| 3 \| 软件生命周期及软件确认计划 \| 是否按软件生命周期拟制了软件确认计划 \| \| □通过 □不通过 □不适用 \| \|

### P014. T1阶段设计验证报告封皮中三个子报告勾选框均为"□"（未勾选），无法确认T1验证已正式完成并通过。

- Finding ID：`LLM-0050`
- 严重度：`P2`
- Agent：V&V Agent
- 类型：`verification_report_cover_not_signed_off`
- 未决原因：证据来源为'.via_lo_html.clean.md'转换文件，复选框符号'□'在HTML/Markdown转换过程中极易出现渲染失真——原始文档中已勾选的'☑'或'✓'可能被转换为'□'。当前证据无法可靠区分'真实未勾选'与'转换失真'两种情形。若基于转换产物直接判定T1验证未正式完成，存在高误报风险。需人工核查原始Word/PDF封皮文件中的实际勾选状态后方可定性，在此之前不应维持P1严重度。
- 现有证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:22` □设计验证报告－通用要求部分 文件编号： PT9L-T1TY01 V1.0;
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:24` □设计验证报告－功能规格部分 文件编号： PT9L-T1GN01 V1.0;
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告封皮-T阶段 E0  23.11.via_lo_html.clean.md:26` □设计验证报告－性能规格部分 文件编号： PT9L-T1XN01 V1.0;

### P015. 设计验证计划封皮（F0118）中子计划勾选框状态无法从证据中确认，存在验证计划正式批准状态不明的风险。

- Finding ID：`LLM-0055`
- 严重度：`P2`
- Agent：V&V Agent
- 类型：`verification_plan_cover_subplan_not_checked`
- 未决原因：证据存在根本性局限：line 13提供的是HTML表格的CSS样式和colgroup标签片段，line 15仅显示文件编号和版本号，均未包含实际勾选框内容。当前截取的source_text无法判断封皮中子计划勾选框的实际状态（已勾选或未勾选），finding的核心断言"勾选状态无法确认"本身即承认了证据不足。需人工直接查阅原始文件"设计验证计划(封面)E0 23.11.md"的完整渲染内容，确认各子计划勾选框状态及审批签字情况后方可定性。在证据不足的情况下不应维持P2定级。
- 现有证据：
  - `11 T1样机\设计验证计划E0\设计验证计划(封面)E0 23.11.md:13` <div style="overflow-x:auto; border:1px solid #e5e7eb; border-radius:6px; padding:0; background:#fff; margin:6px 0;"><table style="border-collapse:collapse; width:max-content; font-size:13px; line-height:1.55;"><colgroup...
  - `11 T1样机\设计验证计划E0\设计验证计划(封面)E0 23.11.md:15` \| \| 文件编号： \| PT9L-YZJH01 \| V1.0 \| 设计验证计划 \| 表号: QR-7.3-06/E0 \| \|
  - `11 T1样机\设计验证计划E0\xingneng.via_xlsx.clean.md:14` 1.本设计验证计划需批准后方能使用执行，

### P016. 产品检验标准中允许对不合格温度计复测两次且两次合格即判合格，该规则是否已在验证计划判定准则中明确引用存疑。

- Finding ID：`LLM-0059`
- 严重度：`P3`
- Agent：V&V Agent
- 类型：`acceptance_criteria_retest_rule_consistency`
- 未决原因：现有证据仅显示：检验标准中存在复测规则，验证报告引用了检验标准但未显式提及复测规则。然而验证报告引用'全部测试结果均需符合检验标准'本身可能已隐含对检验标准全部条款（含复测规则）的引用，不能仅凭未显式提及即判定为缺陷。需人工复核验证计划（PT9L-YZXN01）原文是否对复测规则有明确排除或引用说明，以及实际测试记录中是否发生过复测情形，方可定性。
- 现有证据：
  - `11 T1样机\PT9L红外体温计产品检验标准 V1.0.doc.md:250` 4. 对测试结果不符合规定的温度计，可复测两次，两次复测合格，亦可作合格处理。</td>
  - `11 T1样机\PT9L红外体温计产品检验标准 V1.0.doc.md:267` 4. 对测试结果不符合规定的温度计，可复测两次，两次复测合格，亦可作合格处理。</td>
  - `11 T1样机\设计验证报告E0 23.11\性能规格部分（一）EN1060-1项.via_xlsx.clean.md:23` \| 1 \| 温度显示范围 \| 32.0℃～42.9℃ \| □手板■T1□设计确认 \| 参见《PT9L红外体温计产品检验标准V1.0 》第6项 \| 全部测试结果均需符合《PT9L红外体温计产品检验标准V1.0》中第6项的要求 \| 参见《PT9L红外体温计检测报告 V1.0》中第6项测试结果 \| 合格 \|


## 8. 关联输出文件

- `PT9L_mechanical_cluster_decision_table.md`：机械候选最终裁决总表，按 cluster 去重。
- `PT9L_mechanical_review_true_errors.md`：机械确认错误的候选行展开版。
- `PT9L_mechanical_review_dismissed.md`：机械候选驳回/非错误清单。
- `PT9L_full_audit_report_langgraph.md`：全量审查报告。