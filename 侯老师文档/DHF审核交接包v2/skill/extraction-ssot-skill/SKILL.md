---
name: extraction-ssot-skill
description: DHF/DMR审核「提取层」——把转换好的Markdown收拢成两份地基产物：①覆盖台账（DHF清单应有 vs 实物实有 vs 转换可读，三方对账，专防「0%悄悄漏」，没有总清单时如何兜底）；②SSOT参数实例长表（阶段/参数名/值/出处文件+行号，尽量多抽，增量累积喂下一个agent）。它是Tier1数值检查与证据核验的地基，抽取量就是跨阶段一致性审核的召回天花板。配套脚本：coverage_ledger.py、assemble_incremental.py、convert_*.py（convert_pt9s.py/convert_m10.py）、dhf_audit_toolkit\check_residue.py。Use 在任何型号开审之前、或转换跑完之后，要确认「该有的都在、能读的都抽出来了」时。
---

# Extraction & SSOT Skill（提取层：覆盖台账 + 参数实例长表）

## 目的

这一层是整个审核系统的**地基**。它不下任何审核结论，只保证两件事：

1. **不悄悄漏文件**——该有的 DHF 文件都在、都转成功了，缺的精确点名。
2. **不悄悄漏参数**——能从文本里读出来的参数实例，尽量多地抽进一张可溯源的长表（SSOT，Single Source of Truth）。

为什么必须单独把它写透：**后面所有 agent 的判断质量，上限都被这一层锁死。**

- 一个参数如果在转换时丢了、或没被抽进长表，那么后面再聪明的模型也永远看不到它，只会误判「该参数缺失/没冲突」——而真相是「它在，只是没被提取出来」。SSOT 长表收录的参数实例数，就是跨阶段一致性审核能发现的矛盾数的**天花板**。
- 审核系统最危险的不是「看错」，是「没看到却以为看全了」。这一层全部的设计哲学，就是把「没看到」变成**显式、可量化、可追责**的台账条目。

朴素做法为什么不行：

- **只看「转换成功率」**：假设清单上有 100 个文件，实物只有 70 个、这 70 个全转成功——纯转换台账会报「成功率 100%」，而真相是覆盖率只有 70%，30 个文件**从未进入流水线，连「失败」都算不上，它们是「不存在」**。这就是「0% 悄悄漏」：一个文件压根没出现，任何只看「已处理文件」的统计都发现不了它。必须有一个**独立的分母（清单）**来做减法。
- **让一个大 agent 一口气读完所有文件找矛盾**：上下文窗口装不下整个 DHF；就算装得下，「大海捞针」式的跨文件比对召回率极低、不可复现。必须把散落在几十个文件里的每个参数实例，连同出处，沉淀成结构化中间产物，才能跨 agent 传递、跨阶段比对。

## 何时用

- 任何型号开审**之前**、或文档转换（`convert_*.py`）跑完**之后**的第一道关口。
- 怀疑「某个文件该有却没找到」「某个参数该有却没抽到」时，先回到这一层查台账，不要急着下「缺失」结论。
- 给下游 Tier1 数值检查器（`check_params_numeric.py`）和证据核验（`verify_findings.py`）准备输入时。

## 输入

读这些再动手：

- 转换产物：`<型号>_MD/**/*.md`（每个 MD 顶部有 ASCII front-matter：`source_file` / `source_relative` / `source_type` / `conversion_status` / `loss_flags` / `manual_review_required`）。
- 转换台账：`<型号>_MD/_manifest_conversion.csv`（或分片转换器产出的 `_manifest_<tag>.csv`），列 `rel/type/status/text_len/loss_flags/md/error`。
- **DHF 清单（覆盖率的分母）**：受控的《DHF清单》Excel，如 `<型号>-DHF清单-常规.xls`。这是法规意义上「这个设计项目应该有哪些文件」的权威定义。
- 实物原始件目录：`<型号>` 原始 DHF 根目录（用来列「实有」）。
- workflow 各 agent 的输出 JSON（含每个 folder 的 `parameters` / `intra_findings` / `cross_findings`），喂给 `assemble_incremental.py`。

真实脚本位置：

- 转换器：`D:\AI_0415\03DHF\PT9S\convert_pt9s.py`（单进程 Word 复用）/ `D:\AI_0415\03DHF\convert_m10.py`（`--shard i/N` 分片并行）。
- 覆盖台账：`D:\AI_0415\03DHF\PT9S\coverage_ledger.py`。
- SSOT 汇总器：`D:\AI_0415\03DHF\assemble_incremental.py`。
- 工具包：`D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\`，内含 `check_residue.py`（模板残留扫描）、`check_params_numeric.py`（Tier1 数值一致性，吃 SSOT 长表）、`check_table_diff.py`、`check_bom_crosswalk.py`、`dhf_pipeline.py`。
- 证据核验（下游）：`D:\AI_0415\03DHF\verify_findings.py`。

## 强制工作流（编号步骤，不许跳步）

> 纪律：**先确认工具在，再确认文件在，最后才确认内容**。每一步都落盘可复现，任何损失/缺口都要写进台账而不是吞掉。

**1. 先加载通用做事方法 skill。**
   - `D:/AI_0415/03DHF/skill/SKILL.md`（working-method：实际看到才算数、一步一验、诚实标 UNKNOWN、末尾回喵、长任务报活）。

**2. 确认转换已诚实完成（不静默丢）。**
   - 读 `_manifest_conversion.csv`，确认没有大片 `failed`；`status` 三态 `ok/empty/failed` 要分清：`empty` = 转换没报错但正文为空（往往是纯图/纯 OLE 件，要单独关注），不是 `ok`。
   - 凡 `loss_flags` 非空（`checkbox=.. (checked=..)` / `embedded_ole=..` / `floating_shapes=..` / `pdf_low_text=..`）的文件，`manual_review_required=yes`，登记为「文本管线可能不全，需看 PNG 或人工复核」。
   - 边界诚实：勾选框只数到「N 个框勾了 M 个」，**不还原哪一题勾了**；OLE 只数个数，**不抽里面的表**。这些信息只能定性，**不能直接入参数长表**。
   - 若是 `convert_m10.py` 分片跑的，确认每个 `--shard i/N` 都产出了 `_manifest_<tag>.csv` 且都跑完，再合并看全貌。

**3. 跑覆盖台账，三方对账（DHF清单 应有 × 实物 实有 × 转换 可读）。**
   - 命令（以 PT9S 为例，按型号改路径/常量）：
     ```
     python D:\AI_0415\03DHF\PT9S\coverage_ledger.py
     ```
   - 它做的事（对每个清单条目）：
     - 解析清单 `parse_list()`：从第 3 行起读，阶段列是稀疏列，用 `if row[0]: stage=row[0]` **向下填充（forward-fill）**；用正则 `re.sub(r"\s*V\d+(\.\d+)*\s*$","",no)` 把编号尾部版本号剥成 `doc_no_core`；`if not name: continue` 跳空行。
     - 归一化 `norm_name()` / `norm_no()`：小写化、全角括号转半角、删空白与分隔符、删版本号 `v\d+(\.\d+)*` 与尾部版次 `e\d+`、删「封面/首页」无意义词；编号统一破折号。直接字符串比对必失败，靠这两个归一器。
     - 最佳匹配 `best_match()` 多信号加权：`SequenceMatcher(name).ratio()` 是基础分；名字整体出现在路径里 → 至少 `0.9`；阶段名前 3 字符命中路径 `+0.15`；编号出现在路径 `+0.4`；**编号出现在转换出的正文里（前 60000 字）`+0.5`（最强证据）**。文件名可乱起，但受控编号印在正文里几乎不会错。
     - 定状态：`name_score >= 0.55` 或编号命中 → `ok`；名字弱（<0.55）且编号没命中、即便加权分够也降级 `review`（交人，不让机器拍板）；都不沾 → `missing`。
     - 纸档豁免：`status==missing` 且 `form` 含「纸」→ 改判 `paper_only_no_ecopy`，并从有效覆盖率分母里剔除。
   - 看两个输出：`coverage_ledger.csv`（全量）+ `coverage_ledger.md`（行动清单，只列 `missing`/`review`/转换失败）。
   - **盯死「有效覆盖率」**：`有效覆盖率 = (covered + review) / (total - paper)`。分母是清单总数减纸档，这才精确回答「剔除合理缺席后到底覆盖了多少应有文件」。
   - 同时看反向列表「实物有·清单无」（`extra`，限前 60 条）：这是**未受控/多版本残留**嫌疑，只标嫌疑不下定论，交人判断。

**4. 没有总清单时如何兜底（不能因为没分母就放弃对账）。**
   - 兜底分母按优先级取：(a) 设计控制阶段目录结构本身（每个阶段文件夹 = 应有一组文件）；(b) `_manifest_conversion.csv` 全量实物清单当「实有」基线，至少能跑「实物有·清单无」那一侧；(c) 同产品线已审型号的清单做**模板对照**（如 PT9L 清单套到新冲牙器型号），逐条标「本型号是否适用」。
   - 兜底产出必须**显式标注**：`coverage_basis=folder_structure` / `=manifest_only` / `=template_from_<型号>`，并把有效覆盖率标成 `estimated`，不能伪装成有权威清单的精确值。
   - 诚实边界：没有受控清单时，**抓不到「清单上有、实物彻底没有」这一类漏交**——只能抓「转换失败」和「实物有疑似未受控」。这一点必须在台账里写明，不要让人误以为已全覆盖。

**5. 扫模板残留（防「填空没填、占位符没替」混入参数池）。**
   - 命令：
     ```
     python D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\check_residue.py
     ```
   - 目的：揪出 `XXX` / `待填` / `TBD` / `公司模板默认值` / 错误型号串号等模板残留。这些是「看起来有值、其实是空壳」的假参数，必须在进 SSOT 前识别，否则会污染参数池、引出假冲突或假一致。

**6. 抽 SSOT 参数实例长表（尽量多抽，这是天花板）。**
   - 每个阶段一个 agent，从该阶段 `<型号>_MD/**` 逐字读，把每一个参数实例抽成一条记录。字段（ASCII key，给机器解析；值可中文，给人看）：
     - `stage`（阶段）、`name`（参数名）、`value`（值，**带原始单位与写法**，如 `≤10mA` / `32.0℃～42.9℃` / `3.7V`）、`source_file`（出处文件）、`source_line`（行号/页码，溯源关键）。
   - **抽取原则**：宁可多抽不要漏。同一个参数（如「工作电压」）在不同阶段/文件出现就是**多条记录**——这正是抓「漂移」所需的长表形态。出处必须能回到具体文件、具体行/页，任何一个值都可逐字复核。
   - 增量喂下一个 agent：本阶段抽出的参数**追加进越来越全的 SSOT 长表**，这张表再作为上下文喂给下一阶段的 agent，使后一个阶段能「看见」前序所有阶段的参数，从而产出 `cross_findings`（本阶段 vs 前序阶段 `vs_folder`）。
   - 不要把第 2 步里「只数到个数」的勾选框/OLE 当作已抽参数；它们标 `manual_review_required`，不进长表的 `value`。

**7. 汇总落盘三份持久产物。**
   - 命令：
     ```
     python D:\AI_0415\03DHF\assemble_incremental.py <型号> <workflow输出json> [输出目录]
     ```
   - 产出（`utf-8-sig` 编码，Excel 双击不乱码）：
     - `<型号>-运行参数长表.csv`——**长表（long format）**，列 `阶段/参数名/值/出处文件`。同一参数多值即漂移在 SSOT 里的样子。
     - `<型号>-错误总表.csv`——内部 + 关联 findings 拍平，列 `序号/阶段/原ID/严重度/轴/类型/描述/证据/建议/责任工程师/关联前序`，按 `SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}` 升序、`.get(x,9)` 兜底未知档。列名与 PT7 一致，便于下游报告器复用。
     - `<型号>-增量审核报告.md`——逐阶段小节，头部统计参数总数/问题分桶。
   - 顶层 `o["result"]["folders"]` 是**硬契约**（无兜底）：上游 JSON 结构破了就该响亮 `KeyError`，而不是静默产出空表。

**8. 把长表交给 Tier1 数值检查器，闭环回看召回。**
   - 命令：
     ```
     python D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\check_params_numeric.py
     ```
   - 它吃 SSOT 长表，按 canonical 参数名 + 限定词分组、单位归一、解析五种形态（区间/容差/边界/单点/特殊），做近零误报的数值一致性判定。
   - **闭环纪律**：如果 Tier1 报 0 组冲突，**不能据此断言「无冲突」**——很可能是冲突压根不在长表里（抽漏了）。把 Tier1 的低召回缺口记下来，交给 LLM 维度轴去补。抽取是天花板，Tier1 只能检到天花板以下。

## 与其它层的衔接

- **上游（工具层 `convert_*.py`）→ 本层**：转换决定了有多少原始信息能进到台账和长表。`loss_flags` / `conversion_status` 是本层判「这个文件能不能信、参数抽没抽全」的依据。转换不丢，本层才有料可对、可抽。
- **本层 → Tier1 检查层（`check_params_numeric.py` 等）**：SSOT 长表是 Tier1 子轴①（纵向阶段链）和子轴②（横向参数槽位）的同一张总账——纵着读是阶段链，把一个参数横着拉出来是槽位。Tier1 的召回上限 = 本层抽取量。
- **本层 → 自验证层（`verify_findings.py`）**：每条 finding 的 `证据` 要能回到 SSOT 长表里的 `出处文件 + 行号`，证据核验才有锚点。
- **覆盖台账 → 全局**：有效覆盖率是「这次审核到底覆盖了多少应有文件」的唯一可信指标，所有「未发现问题」的结论都必须在覆盖率语境下解读。

## 边界与踩坑（诚实标）

- **覆盖匹配是启发式，不是真值**：`name_score>=0.55` 和那串加权常数（0.4/0.5/0.15/0.9）是经验调出来的，不同型号命名习惯可能要重调。它会误匹配（把 A 的文件配给 B 的清单条目），所以 `review` 档兜底，把不确定的全推给人。**注意：跨表对账/覆盖匹配是「近零误报」的对立面——它是低精度高召回的启发式，必须靠 `review` + 人工，不能当确定性结论。**
- **Tier1 数值检查是低召回**：它「宁可漏掉，绝不误报」（解析不了就跳过、点落区间判一致、写法差异归一后不报）。0 组冲突 ≠ 无冲突。这是已知边界，补召回靠 LLM 层。
- **长表不做去重/规整**：「工作电压」「额定工作电压」「工作电压(V)」在长表里是三个不同 `参数名`，不会自动聚类。漂移检测按 `参数名` 精确 group by 会漏掉「同义不同名」。规整是抽取 agent 的责任，或需后续单独归一化步骤。
- **`assemble_incremental.py` 本身不抽参数、不判矛盾**：它是纯汇总器，参数和 findings 全来自上游 agent JSON。长表完整性、findings 正确性全在上游，别误以为漂移检测逻辑在这里。
- **纸档豁免依赖 `form` 字段填得对**：`"纸" in item.form` 才豁免；清单里写成「硬拷贝」之类不含「纸」字的，会被误报 `missing`。依赖源数据规范性。
- **`used` 集合可能一对多**：两个清单条目撞同一个实物文件，当前实现不做全局一对一指派，靠 `review` 和人工兜。
- **平台锁定**：Word `.doc/.docx` 转换走 COM，只在装 Office 的 Windows 上能跑；中文/带空格路径对部分开源工具是静默失败高风险点，脚本里不要硬编码中文路径，优先从 manifest/Path 读。
- **字段名必须 ASCII**：SSOT 与台账的 schema key（`source_file`/`loss_flags`/`stage`/`name`/`value`/`source_line`/`coverage_basis` 等）一律英文下划线；值可中文。不要把问号 mojibake 字符串写进机器可读文件。
- **终端乱码 ≠ 文件不存在**：判断文件在不在用 `Path.exists()` / manifest 结果，不要把终端显示当真实文件名。

## Quick Checklist

- [ ] 转换台账已看，无大片 `failed`，`empty` 与 `ok` 已区分
- [ ] 所有 `loss_flags` 非空文件已登记 `manual_review_required`
- [ ] 覆盖台账已跑，`coverage_ledger.csv` + `coverage_ledger.md` 生成
- [ ] 有效覆盖率算出（`(covered+review)/(total-paper)`），缺失项精确点名
- [ ] 「实物有·清单无」嫌疑列表已看，标为嫌疑未下定论
- [ ] 无总清单时已用兜底分母并显式标 `coverage_basis` + `estimated`
- [ ] 模板残留（`check_residue.py`）已扫，假参数未混入长表
- [ ] SSOT 长表尽量多抽，每条带 `阶段/参数名/值/出处文件/行号`
- [ ] 同参数多阶段记成多行（漂移可见），出处可逐字回溯
- [ ] 长表增量累积、已喂下一阶段 agent
- [ ] 三份产物落盘（运行参数长表 / 错误总表 / 增量审核报告），编码 `utf-8-sig`
- [ ] 已交 `check_params_numeric.py`，并记录「0 组冲突 ≠ 无冲突」的召回缺口
- [ ] 机器可读文件 schema key 全 ASCII，无问号 mojibake
- [ ] 回答末尾有「喵」

喵
