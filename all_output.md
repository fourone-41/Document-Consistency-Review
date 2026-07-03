# all_output

> 用途：集中记录每一版 PT9L 文档一致性审查结果，方便后续迭代、复核、整改和版本对比。
> 维护方式：每次生成新结果后，在“版本索引”新增一行，并复制“下一版记录模板”追加一个新章节。

## 版本索引

| 版本 | 结果来源 | 生成时间 | 运行模式 | 合并 Findings | 证据可回溯 | P1 | P2 | P3 | 当前状态 |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| V1 | `pt9l_full_audit_output_langgraph_v2/08_reports` | 2026-06-24 15:04:31 | full_langgraph_llm | 519 | 519 | 17 | 361 | 141 | 待人工复核 |

## V1 - PT9L 全量 Markdown 一致性审查结果

### 来源文件

- 全量报告：`pt9l_full_audit_output_langgraph_v2/08_reports/PT9L_full_audit_report_langgraph.md`
- 高优先级语义问题：`pt9l_full_audit_output_langgraph_v2/08_reports/PT9L_high_priority_semantic_findings.md`
- 运行摘要：`pt9l_full_audit_output_langgraph_v2/08_reports/run_summary_full_langgraph.json`

### 运行摘要

| 指标 | 数值 |
|---|---:|
| run_mode | full_langgraph_llm |
| llm_provider | GPT55 via OpenAI-compatible SDK |
| manifest_docs | 470 |
| primary_scope_docs | 227 |
| auxiliary_scope_docs | 243 |
| page_index_sections | 4222 |
| parameter_instances | 12168 |
| relation_nodes | 2893 |
| relation_edges | 4 |
| mechanical_candidate_findings | 484 |
| llm_semantic_findings | 35 |
| merged_findings | 519 |
| evidence_verified | 519 |

### 严重度分布

| 等级 | 数量 | 占比 |
|---|---:|---:|
| P1 | 17 | 3.3% |
| P2 | 361 | 69.6% |
| P3 | 141 | 27.2% |
| 合计 | 519 | 100.0% |

### Agent 分布

| Agent | 数量 | 说明 |
|---|---:|---|
| Mechanical Check Agent | 480 | 机械候选问题为主体，需要后续抽样确认误报率 |
| Market & Category Scout Agent | 5 | 产品型号、品类、市场适用性相关语义问题 |
| Regulatory Agent | 5 | 法规适用性、标准、标签、生物相容性相关语义问题 |
| Hardware Agent | 5 | BOM、硬件参数、样机评审相关语义问题 |
| Software Agent | 5 | 软件 DHF、软件评审、追溯链相关语义问题 |
| Risk Traceability Agent | 5 | 风险文件版本、风险闭环、DFMEA 追溯相关语义问题 |
| V&V Agent | 5 | 验证确认闭环、封皮结论、生物相容性证据相关语义问题 |
| DMR/SOP Agent | 5 | 设计输出、图纸、BOM、制造转移相关语义问题 |
| SSOT Parameter Agent / Mechanical Check Agent | 4 | 参数一致性类候选问题 |

### Challenge 结果

| Challenge 状态 | 数量 | 处理含义 |
|---|---:|---|
| keep | 19 | 证据与结论匹配度较高，优先进入人工确认和整改台账 |
| revise | 9 | 问题可能成立，但需调整表述、严重度或证据边界 |
| needs_more_context | 7 | 现有证据不足，需要补充受控范围、版本或背景材料 |

### 本版总体判断

本次结果的核心特征是：总量上以机械候选 findings 为主，语义 findings 数量较少但信号密度高。519 条合并 findings 均已完成证据回溯，但这里的 verified 只表示能定位到 Markdown 原文，不等于人工已经接受该问题。

优先风险集中在六类：跨型号/跨品类文件混入、风险管理文件版本与前缀并存、验证确认闭环表单缺失、设计输出与 DMR 图纸/BOM 配置冲突、法规标准适用性矛盾、生物相容性桥接证据不足。其中 P1 共 17 条，第一批建议先处理 Challenge 为 keep 的 15 条 P1；P1 但 needs_more_context 的 LLM-0001、LLM-0012 放入第二批背景核查。

### 第一批高优先级复核清单

| 序号 | Finding ID | 领域 | 问题摘要 | 建议动作 |
|---:|---|---|---|---|
| 1 | LLM-0002 | 设计输出/型号边界 | 设计输出清单二大量使用 PT3SBT 型号编号，封面产品型号也为 PT3SBT，与 PT9L 不符。 | 确认是否误归档；若为正式文件，需更正清单或移出 PT9L DHF。 |
| 2 | LLM-0003 | 品类一致性 | DHF 中存在血压计品类文件，与 PT9L 红外体温计品类不符。 | 按文件编号逐项判定正式范围，建立剔除或替换记录。 |
| 3 | LLM-0004 | 测试报告/风险文件号 | PT9L -2-56 正式实验报告引用 PT9C-FXGB01 V1.0 风险管理报告。 | 核对实验报告原件和风险管理引用，必要时出具修订或偏差说明。 |
| 4 | LLM-0006 | 法规/DFMEA | 结构类 FMEA 铭牌失效描述出现“血压计”字样。 | 更正 DFMEA 模板残留，并评估是否影响风险控制结论。 |
| 5 | LLM-0008 | 法规标准适用性 | 设计输入将 EN ISO 80601-2-56 标记为欧盟不适用，但说明书声明符合 EN 版本。 | 明确目标市场和标准适用性决策，统一设计输入、说明书和法规清单。 |
| 6 | LLM-0011 | 硬件/DHF 边界 | T1 样机文件夹混入 PT3SBT 标签审核表，且内容不属于 PT9L。 | 从 PT9L 正式包中剔除或标记为历史参考，补齐 PT9L 标签审核证据。 |
| 7 | LLM-0016 | 软件/DHF 边界 | 软件设计方案文件夹下存在 BP3L 血压计软件图样。 | 核查是否误放；若非 PT9L 证据，应移出正式 DHF 范围。 |
| 8 | LLM-0017 | 软件/DMR 完整性 | T1 文件夹存在 PT3SBT/PT2L 旧型号标签审核表。 | 与 LLM-0011 合并整改，统一处理标签证据边界。 |
| 9 | LLM-0021 | 风险管理/版本控制 | IFT- 与 PT9L- 两套风险管理文件并存，版本不一致，缺少有效版本判定。 | 建立风险文件版本矩阵，明确受控有效版本和废止关系。 |
| 10 | LLM-0022 | 风险/DFMEA | 结构类 DFMEA 严重度评级准则描述“影响血压计的安全运行”。 | 清理模板残留，确认严重度准则是否适用于 PT9L。 |
| 11 | LLM-0026 | V&V 闭环 | T 阶段设计验证报告封皮三份子报告均未勾选。 | 补正封皮勾选和审批记录，确保验证报告闭环成立。 |
| 12 | LLM-0027 | 设计确认闭环 | 设计确认阶段验证报告封皮“设计验证合格”未勾选。 | 补齐书面结论或确认是否存在正式签署版本。 |
| 13 | LLM-0028 | 生物相容性 | T1 文件夹生物相容性报告均来自 PT5，未见 PT9L 专属评价或桥接分析。 | 补充材料等同性/桥接评价，或重新建立 PT9L 评价证据。 |
| 14 | LLM-0031 | DMR/图纸归档 | 设计输出清单二归档 PT3 双联弹簧图纸，缺少正式跨型号引用说明。 | 明确共用件引用依据、受控状态和设计输入追溯。 |
| 15 | LLM-0032 | DMR/图号冲突 | 外观图与外箱图纸 Drawing NO. 均为 PT9L-F01，但对应不同物件。 | 立即核查图号唯一性，修订其中一份图号或建立变更记录。 |

### 35 条 LLM 语义 Findings 全量清单

| ID | 等级 | Agent | Challenge | 类型 | 结论摘要 |
|---|---|---|---|---|---|
| LLM-0001 | P1 | Market & Category Scout Agent | needs_more_context | legacy_model_contamination_in_risk_docs | 风险管理文件预期用途描述中出现旧型号 PT3SBT，产品身份与 PT9L 项目不符。 |
| LLM-0002 | P1 | Market & Category Scout Agent | keep | legacy_model_in_design_output_list | 设计输出清单二大量条目使用 PT3SBT 型号编号，且封面产品型号标注为 PT3SBT。 |
| LLM-0003 | P1 | Market & Category Scout Agent | keep | wrong_product_category_documents_in_dhf | DHF 中存在多份明确标注血压计品类的文件，与 PT9L 红外体温计不符。 |
| LLM-0004 | P1 | Market & Category Scout Agent | keep | test_report_references_wrong_model_number | 正式实验报告引用 PT9C-FXGB01 V1.0 风险管理报告，而非 PT9L 对应文件号。 |
| LLM-0005 | P3 | Market & Category Scout Agent | revise | legacy_label_audit_table_in_dhf | T1 样机阶段存在 PT3SBT 标签审核表，内容引用 PT2L 标签文件编号。 |
| LLM-0006 | P1 | Regulatory Agent | keep | cross_model_document_contamination | PT9L 结构类 FMEA 铭牌失效模式描述误植入血压计字样。 |
| LLM-0007 | P2 | Regulatory Agent | revise | cross_model_label_audit_evidence | PT3SBT 标签审核表引用 PT2L 检查记录，不能作为 PT9L 标签合规证据。 |
| LLM-0008 | P1 | Regulatory Agent | keep | eu_standard_applicability_inconsistency | 设计输入将 EN ISO 80601-2-56 标记为欧盟不适用，但说明书声明符合 EN 版本。 |
| LLM-0009 | P2 | Regulatory Agent | keep | biocompatibility_bridging_evidence_gap | PT9L 生物相容性报告全部来自 PT5，未见 PT9L 专属评价或桥接分析。 |
| LLM-0010 | P2 | Regulatory Agent | needs_more_context | duplicate_risk_file_without_differentiation | DHF 中存在两套高度重复的风险管理文件，无法判断哪套为 PT9L 正式受控版本。 |
| LLM-0011 | P1 | Hardware Agent | keep | cross_model_document_contamination | T1 样机文件夹混入 PT3SBT 标签审核表，构成 DHF 文件边界污染。 |
| LLM-0012 | P1 | Hardware Agent | needs_more_context | bom_cross_model_part_number | PT9L 机芯 BOM 中同时列有 PT9L 主 PCB 和 PT9C 型号 PCB。 |
| LLM-0013 | P3 | Hardware Agent | revise | battery_parameter_inconsistency | 电池寿命测试报告电池为 3V/1000mAh，包装 BOM 为 1.5V/1200mAh LR03。 |
| LLM-0014 | P2 | Hardware Agent | keep | prototype_review_checklist_incomplete | 三份样机评审检查表关键硬件装配项结论栏为空白。 |
| LLM-0015 | P3 | Hardware Agent | revise | blood_pressure_terminology_residue_in_battery_requirement | 设计验证计划电池条目含“次血压测量”字样，为血压计模板残留。 |
| LLM-0016 | P1 | Software Agent | keep | legacy_model_document_contamination | 软件设计方案文件夹下存在 BP3L 血压计软件图样文件。 |
| LLM-0017 | P1 | Software Agent | keep | legacy_model_label_document_in_t1_folder | T1 样机文件夹中存在 PT3SBT/PT2L 旧型号标签审核表。 |
| LLM-0018 | P2 | Software Agent | revise | cross_model_pcb_reference_in_bom | PT9L 机芯类组件清单中 PCB 图号引用 PT9C-CNTP01。 |
| LLM-0019 | P2 | Software Agent | needs_more_context | review_checklist_conclusion_blank | 软件质量策划评审检查表所有评审条目结论栏均为空白。 |
| LLM-0020 | P2 | Software Agent | needs_more_context | traceability_matrix_completeness_unverifiable | 构建和编码文件中有追溯表框架，但未见需求-设计-测试完整填写内容。 |
| LLM-0021 | P1 | Risk Traceability Agent | keep | duplicate_risk_file_set_without_clear_supersession | F0017-F0020 与 F0021-F0024 两套风险管理文件并存，缺少替代/废止关系。 |
| LLM-0022 | P1 | Risk Traceability Agent | keep | dfmea_product_description_cross_contamination | 结构类 DFMEA 严重度准则描述“影响血压计的安全运行”。 |
| LLM-0023 | P3 | Risk Traceability Agent | revise | pt9c_design_validation_document_in_pt9l_dhf | PT9C 设计确认文件混入 PT9L DHF，且引用 PT9L 风险管理报告。 |
| LLM-0024 | P2 | Risk Traceability Agent | keep | risk_management_report_version_inconsistency_in_traceability | 可追溯性分析报告引用 PT9L-FXPJ01 V1.0，但风险评价报告已出现 V2.0。 |
| LLM-0025 | P2 | Risk Traceability Agent | needs_more_context | emc_immunity_risk_criteria_traceability_gap | EMC 报告要求免疫性准则纳入风险管理，但未见直接风险条目证据。 |
| LLM-0026 | P1 | V&V Agent | keep | verification_report_cover_incomplete | T 阶段设计验证报告封皮三份子报告均为空选，验证闭环形式上未成立。 |
| LLM-0027 | P1 | V&V Agent | keep | design_confirmation_conclusion_not_checked | 设计确认阶段验证报告封皮结论栏“设计验证合格”未勾选。 |
| LLM-0028 | P1 | V&V Agent | keep | biocompatibility_reports_wrong_product | T1 文件夹全部生物相容性报告均属 PT5，未见 PT9L 专属或桥接证据。 |
| LLM-0029 | P3 | V&V Agent | revise | cross_model_label_audit_table_in_pt9l_dhf | PT3SBT 标签审核表混入 PT9L 的 T1 样机文件夹。 |
| LLM-0030 | P2 | V&V Agent | needs_more_context | design_review_verification_linkage_gap | 手板样机设计评审记录中验证报告关联栏为空选，验证状态无法确认。 |
| LLM-0031 | P1 | DMR/SOP Agent | keep | cross_model_drawing_in_dhf | 设计输出清单二归档 PT3 双联弹簧图纸，缺少正式跨型号引用说明。 |
| LLM-0032 | P1 | DMR/SOP Agent | keep | duplicate_drawing_number_conflict | 外观图与外箱图纸 Drawing NO. 均为 PT9L-F01，但对应不同物件。 |
| LLM-0033 | P3 | DMR/SOP Agent | revise | packaging_bom_document_number_inconsistency | 两份 PT9L 包装 BOM 文件编号存在 PBOM/PB0M、BOM/B0M 混用。 |
| LLM-0034 | P2 | DMR/SOP Agent | revise | supplier_drawing_not_standardized_in_dhf | 供应商散热器金属套图纸未转换为本厂标准图号，且散热器压块以 PT3-M01 入账。 |
| LLM-0035 | P3 | DMR/SOP Agent | keep | design_output_list_missing_submission_date | 设计输出清单一提交日期、审核日期字段为空白。 |

### 第二批待补充上下文

| Finding ID | 缺口 | 需要补充的信息 |
|---|---|---|
| LLM-0001 | 风险文件中出现 PT3SBT，但证据摘要尚不足以确认是否属于正式受控文本污染。 | 查看完整风险文件原文、文件封面、DN 编号、受控状态和同名 PT9L 版本。 |
| LLM-0012 | BOM 中出现 PT9C PCB，可能是共板/共用件，也可能是跨型号混入。 | 核查 EBOM、实物 PCB、设计输出图纸和变更记录，确认 PT9C-CNTP01 是否被批准用于 PT9L。 |
| LLM-0010 | 两套风险文件高度重复但前缀不同。 | 建立 F0017-F0024 文件矩阵，确认 IFT 与 PT9L 前缀关系、版本差异和正式使用版本。 |
| LLM-0019 | 软件质量策划评审表结论为空白。 | 查看原始 Excel/PDF 是否为转换遗漏；如非转换问题，补充签署版或整改记录。 |
| LLM-0020 | 软件追溯表只有框架，未见完整填写内容。 | 搜索是否存在独立追溯矩阵；若不存在，需补齐需求-设计-代码-测试追溯。 |
| LLM-0025 | EMC 免疫性准则与风险管理条目未形成直接证据链。 | 在风险管理报告中定位 EMC 相关 hazard、risk control、verification 记录。 |
| LLM-0030 | 设计评审与验证状态的关联栏为空选。 | 查看设计评审原件和会议记录，确认是否已评估本阶段验证状态。 |

### 建议整改台账字段

| 字段 | 说明 |
|---|---|
| Finding ID | 沿用 LLM-xxxx 或机械 finding ID |
| 问题分类 | 型号边界、法规标准、风险管理、V&V、DMR/SOP、硬件、软件等 |
| 责任人 | 指定实际整改负责人 |
| 人工判定 | 成立/部分成立/误报/需补证 |
| 处置方式 | 修订文件、移出范围、补充桥接、出具偏差说明、建立版本矩阵等 |
| 目标完成时间 | 建议按 P1、P2、P3 分批设定 |
| 关闭证据 | 修订后文件路径、评审记录、批准记录、变更单等 |
| 关闭状态 | open / in_progress / closed / rejected |

## 下一版记录模板

### Vx - 版本标题

| 项目 | 内容 |
|---|---|
| 结果目录 | `待填写` |
| 生成时间 | `待填写` |
| 运行模式 | `待填写` |
| 与上一版差异 | `新增/减少/关闭/复发 findings` |
| 当前状态 | `待复核/整改中/已关闭` |

#### 核心统计

| 指标 | 数值 |
|---|---:|
| manifest_docs |  |
| primary_scope_docs |  |
| auxiliary_scope_docs |  |
| merged_findings |  |
| evidence_verified |  |
| P1 |  |
| P2 |  |
| P3 |  |

#### 本版新增问题

| Finding ID | 等级 | 分类 | 摘要 | 处理建议 |
|---|---|---|---|---|
|  |  |  |  |  |

#### 本版关闭问题

| Finding ID | 关闭证据 | 关闭说明 |
|---|---|---|
|  |  |  |

#### 仍需人工确认

| Finding ID | 卡点 | 下一步 |
|---|---|---|
|  |  |  |
