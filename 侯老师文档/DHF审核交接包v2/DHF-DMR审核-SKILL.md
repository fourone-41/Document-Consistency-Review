---
name: dhf-dmr-audit-orchestrator
description: 医疗器械 DHF/DMR/注册 跨文档审核的【总纲/编排】。它不重写细活,而是按顺序调用 D:\AI_0415\03DHF\skill\ 下你已有的细分 skill(working-method 总则 + 转换工具箱 + 各格式转换 + 逐阶段 check + DMR-SOP check),再补上它们没有的层:确定性算法(Tier1/2)、对抗证伪、证据核验、系统自检、裁决库、并行编排。当用户说"按我们的方法论审某型号"时用本 skill,全程不跳步,结尾必须交《完成自检表》。
---

# DHF/DMR 审核 · 总纲（编排你已有的 skill + 补缺的层）

## ★0 最高铁律
1. **不许跳步。** 下面每一步要么做(✅)、要么在结尾《完成自检表》写明 ⏭️+理由。禁止默默省略(M10 教训:漏了残留扫描/数值一致/表diff/对抗证伪/图纸/代码)。
2. **结尾必交《完成自检表》**(第 8 节)。没有它=审核未完成。
3. **先加载你的总则 skill**:`D:\AI_0415\03DHF\skill\SKILL.md`(working-method)——它管:🐱**喵信号**(每条回复末尾)、**长任务每分钟报进度**、**批量转换闸门**(每类先抽3个样验过再全量)、文件该用什么工具打开、做事方法(实际看到才算/一步一验/诚实标UNKNOWN)。本总纲全程遵守它。
4. **禁止跨型号默认市场/品类/法规/参数。** 每个型号从它自己的客户需求书读(你的 stage-01 skill 本就要求"Sales region/Product category confirmed";M10 错就错在我没用它)。
5. **★执行靠代码,不靠自觉。** 确定性层(残留/数值/表diff/对账/证据核验/自检)**必须走 `run_audit.py`,不准手动逐个挑着跑**:
   - `python run_audit.py <型号> pre`(LLM前:残留;转换/覆盖按 skill\ 另跑) → 语义层 LLM workflow(逐阶段/维度/对抗证伪,出错误总表+参数长表) → `python run_audit.py <型号> post`(数值+表diff+对账+证据核验+**自检硬闸门**)。
   - **post/gate 阶段自检若有"必查"项 → runner exit 1**,即未达标,修完重跑。markdown SKILL 是指引,**`run_audit.py` 的闸门才是"漏跑就卡住"的保证**(M10 实测:漏逐文件夹报告→exit 1 逮住)。表diff/对账需手工指定表对的,runner 会明着 ⏭️标出,不是悄悄漏。

---

## 1 开审前置（Phase 0）
- 加载 `skill\SKILL.md`(总则)。
- 读本型号客户需求书/立项,**确认 市场 / 品类 / 型号 / 项目号 / 项目负责人**(用 `skill\stage-01-dhf-check-skill` 的提取+确认流程)。
- 按市场+品类**建/选法规基线**(中国 NMPA:分类目录/PTR/GB9706.1/YY0316/GB16886/YY0664/中国UDI;美国 FDA:产品码/21 CFR/510k或豁免/ISO/ASTM…)。写成 `<型号>_CHECK\<型号>_<市场>_<品类>_regulatory_baseline.md`。
- 定本品类参数槽位清单(雾化器:雾化率/MMAD/可吸入比例/储药/残留/噪音…;体温计:量程/精度/环境/电池/关机…)。

## 2 转换层 ——【用你的 skill,权威,别用我那套粗的】
> 我的 `convert_*.py` 只转**单套粗表格**,会丢公式/颜色判定/嵌入图/版式——**不达标**。转换必须按你的:
1. **就绪检查**:`skill\conversion-toolkit-skill\SKILL.md` + 跑 `scripts\check_conversion_tools.py --install`(Excel COM/PyMuPDF/Tesseract chi_sim 等)。
2. **批量转换闸门**(总则 0.2,强制):**每种格式先抽 3 个样转、验产物(MD/CSV/页面PNG/manifest/conversion_loss),过了再全量。** 不准一上来全量(M10 我违反了)。
3. **按格式调对应 skill**:`doc-skill` / `docx-skill` / `pdf-skill` / `xls-skill` / `remaining-format-skill`。
4. **Excel 必须按 `xls-skill` 转"2 套"**:①结构通道(每 sheet CSV/MD + 公式 data_only 两遍 + 合并单元格 + 隐藏行/列/sheet + 注释 + **颜色/条件格式语义** + 嵌入图 + 各 manifest)②**页面视觉通道**(sheet 导 PDF/PNG + 页面视觉 MD,保留盖章/图标/版式/作业指导书)。两套都要,缺一不可。
5. 转换失败/低字 PDF 渲 PNG/损失项,全部显式记录(conversion_loss),失败=覆盖缺口。
6. **★中文路径/文本完整性防护**(总则要求,M10 我犯规过——硬编码了中文路径、没跑完整性扫):
   - **脚本不要硬编码中文路径**;从 manifest / `Path` 对象 / Unicode escape 拿路径。
   - **不信终端乱码**:判断文件是否存在用 `Path.exists()`/`Test-Path`,别把终端显示的 `???` 当真实文件名。
   - **写中文内容用 `tools\unicode_safe_write.py`**(从 JSON/base64/文件读入,绕开命令行把 CJK 变 `???`;写后回读校验、见 `???`/`�` 拒写)。
   - **转换后必跑 `tools\scan_text_integrity.py <型号>_MD`** 查乱码(`???`/`�`/UTF8-当CP1252/解码失败),**0 命中才算干净**(M10 实测 0)。
   - 开源工具(LibreOffice 等)遇中文/空格路径会**静默失败** → 先复制到纯英文临时路径再处理。

## 3 提取层（SSOT）
- 建 **参数实例长表**(阶段,参数名,值,出处文件+行号),尽量多抽。后面 Tier1/证据核验的地基。

## 4 检查层
### 4a 逐阶段语义 check ——【用你的 skill,权威】
- **逐阶段调 `skill\stage-01-dhf-check-skill` … `stage-11-dhf-check-skill`**:每个阶段的提取项+检查项+下游≥上游+EU/非目标市场证据链测试,以它们为准(注:它们示例是体温计/美国;换品类/市场时,检查"方法"照用,法规基线换成第1节建的那份)。
- **DMR/工序/SOP 用 `skill\dmr-mfg-sop-check-skill`**。
- 四子轴贯穿:①纵向阶段链(下游≥上游)②横向参数槽位③工程师角色串联(7角色)④反向完备性(拿第1节基线逐条反查);维度横扫7维。每条 finding **必带逐字原文**。
- 大型号用 Workflow 并行 fan-out(每阶段/单元一 agent)+ 跨单元对账(阶段链/跨DMR版本/注册PTR↔设计输出/设变回溯/维度横扫)。schema 字段名 ASCII,值中文。

### 4b 机械层确定性算法 ——【本总纲补,你的 skill 没有,★必跑】
脚本 `PT9L_CHECK\dhf_audit_toolkit\`,纯 Python 近零误报:
1. `check_residue.py`(模板残留扫描,**必跑**):`--foreign <异类品类> --models <异类型号>`。(M10 实测 7587 命中,远超 LLM。)
2. `check_params_numeric.py`(数值一致,**必跑**):喂 SSOT 长表,单位归一+区间/容差/边界+点落区间判一致。
3. `check_table_diff.py`(同构表 diff,有多版本就**必跑**):多版本 BOM(V1.0/V1.1/V1.2)、多版本 DMR、T1↔设计输出同名清单,按主键精确 diff。
4. `check_bom_crosswalk.py`(跨异构表对账,有 BOM↔工序WI↔清单就跑)。

## 5 对抗证伪 ——【本总纲补,★必跑】
- 对候选 finding 派**独立 agent 逐条/分批反驳**(默认倾向证伪),多数驳成立就毙。历史毙约 1/4。不做=误报没过滤。

## 6 输出层
- `assemble_*` → `<型号>-错误总表.csv`/`运行参数长表.csv`/`审核报告.md`。
- `gen_report_review_html.py <型号>` → **裁决版 HTML**(每条 接受/不接受/待定+原因,出处可点开,File0N 翻译)。给其 MODELS 加该型号一段。

## 7 自验证层 ——【本总纲补,★必跑】
1. `verify_findings.py`:每条引文拿回语料 grep,出 有据/缺失断言/可疑。可疑逐条人审。(达标参考有据率 PT9S76%/M10 85%。)
2. `audit_self_check.py <型号>`(给 CFG 加该型号段;法规锚定关键词 reg_regex 按市场设):8 项,看判定。
3. `_adjudications.csv` 裁决库:开审注入"已裁决误报别报";自检撞库;PM 每否一误报加一行。

## 7b 图纸/代码分支（有则做）
- 图纸:`skill\SKILL_2D_Drawing_Reading`(及 3D 那两个)≥300DPI 视觉读图。
- 代码:固件关键常数 vs 设计规格/DMR。

---

## 8 《完成自检表》（结尾必填,逐项交代）
| 步骤 | 状态 | 证据/产物 或 跳过理由 |
|---|---|---|
| 0 加载 skill\SKILL.md 总则(喵/进度/闸门) | ✅ | |
| 0 市场/品类从本型号客户需求书确认(非默认) | ✅/❌ | 市场=? 依据=哪行 |
| 0 法规基线按市场+品类建好 | ✅ | 文件名 |
| 2 转换就绪检查(conversion-toolkit) | ✅/⏭️ | |
| 2 批量转换闸门(每类抽3验) | ✅/❌ | |
| 2 Excel 按 xls-skill 转2套(结构+页面视觉) | ✅/❌ | 否则丢公式/颜色/图 |
| 2 doc/docx/pdf/remaining 按各格式skill | ✅ | ok/失败数 |
| 2 转换后跑 scan_text_integrity 查乱码 | ✅/❌ | 命中数(应0) |
| 2 脚本无硬编码中文路径·写中文用unicode_safe_write | ✅/⏭️ | |
| 3 SSOT 参数长表 | ✅ | 参数数 |
| 4a 逐阶段用 stage-01~11-check-skill | ✅/⏭️ | 哪些阶段 |
| 4a DMR 用 dmr-mfg-sop-check-skill | ✅/⏭️ | |
| 4b check_residue 残留扫描 | ✅/⏭️ | 命中数 |
| 4b check_params_numeric 数值一致 | ✅/⏭️ | 冲突组 |
| 4b check_table_diff 表diff(多版本) | ✅/⏭️ | 比了哪些对 |
| 4b check_bom_crosswalk 跨表对账 | ✅/⏭️ | |
| 5 对抗证伪 | ✅/⏭️ | 毙几条 |
| 6 错误总表+裁决版HTML | ✅ | 路径 |
| 7 verify_findings 证据核验 | ✅ | 有据率/可疑 |
| 7 audit_self_check 自检 | ✅ | 判定 |
| 7b 图纸2D / 代码分支 | ✅/⏭️ | 有无 |
| 末尾有🐱喵 | ✅ | |

> 任一行 ❌ 或无理由 ⏭️ = 不合格,补做。

---

## 附:你的 skill 清单(权威,在 `D:\AI_0415\03DHF\skill\`)
- `SKILL.md` working-method 总则(喵/进度/闸门/工具表/做事法)
- `conversion-toolkit-skill` 转换就绪+工具检查 · `doc/docx/pdf/xls/remaining-format-skill` 各格式转换(**xls=2套**)
- `stage-01 … stage-11 -dhf-check-skill` 逐阶段内容审 · `dmr-mfg-sop-check-skill` DMR/工序审
- **(新)补层 skill**(把详尽版各层都成skill):`extraction-ssot-skill`(提取层/覆盖台账+SSOT) · `dimension-axis-skill`(维度轴7维+槽位+角色串联+反向完备) · `mechanical-tier12-skill`(Tier1/2确定性4脚本) · `self-verification-skill`(证据核验+对抗证伪+裁决库+自检) · `multi-agent-orchestration-skill`(并行fan-out/增量/resume/心跳) · `code-branch-skill`(固件代码分支)
- **强制执行器**:`run_audit.py <型号> pre|post|gate`——确定性层一条命令全跑 + 自检硬闸门(必查项→exit 1),"漏跑就卡住"的保证(见 ★0 第5条)
- **★主控 workflow**:`run_full_audit.js`——一次调用**代码强制**跑全流程:侦察(读客户需求书定市场品类)→逐单元并行审→跨单元对账→Finalize(assemble+run_audit闸门)。配 `assemble_audit.py`(通用汇总)。⚠️**启动必须用"内联启动器"经 `workflow(ref,args)` 传参,绝不能 `Workflow({scriptPath,args})`**——后者 args 不threading,会默认MODEL+空路径→Scout审错型号(PT9L跑去审了M10的血泪坑)。具体写法见 START_HERE。run_full_audit.js 顶部已加 guard(缺args直接throw)。已在PT9L端到端验证通过(33单元/248问题/闸门通过)。
- 桌面/交接包:`SKILL_2D_Drawing_Reading` / `SKILL_3D_Model_Analysis` / `SKILL_3D_Section_Analysis`
- **通用安全工具 `D:\AI_0415\03DHF\tools\`**:`unicode_safe_write.py`(UTF-8 安全写中文,绕命令行乱码+回读校验) · `scan_text_integrity.py`(扫 MD/CSV 乱码,转换后必跑)

**本总纲新增层(你的 skill 没有的)**:Tier1/2 确定性算法 · 对抗证伪 · 证据核验 verify_findings · 系统自检 audit_self_check · 裁决库 _adjudications · 并行编排 · 跨DMR版本/PTR对账 · 完成自检表。深度原理见 `方法与算法-详尽版.md`。

🐱
