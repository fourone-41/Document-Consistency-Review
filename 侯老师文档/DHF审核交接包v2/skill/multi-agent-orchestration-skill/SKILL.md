---
name: multi-agent-orchestration-skill
description: 医疗器械 DHF/DMR 审核的多智能体编排层——把"找错"任务切成多个 agent 并行或串行跑,并保证结果可累积、可续跑、可对账。规定何时用并行 fan-out(各文件夹/各维度互不依赖)、何时必须用顺序增量(累积 SSOT 参数长表喂下一个 agent,做跨阶段关联);规定 structured output 的字段名必须 ASCII、值可中文(中文 key 会让 API 直接 400);规定断点续跑 resume(已完成 agent 命中缓存秒回)、长任务每 2 分钟回🐱心跳、批量并行转换/渲染分片的护栏。配套脚本:增量串行编排 _pt7_incremental_audit.js / 复审重跑 _pt9l_rerun_audit.js(同骨架 + 逐字证据强制 + 裁决库过滤)、汇总器 assemble_incremental.py、证据核验 verify_findings.py、裁决库 _adjudications.csv、图纸分片前处理 prep_2d.py。Use 在要把整套 DHF/DMR 审核或任意大规模逐文件审核拆给多个 agent 跑、要做 Phase1 单元并行 + Phase2 跨单元对账、要中断后续跑、要发起长后台任务时。
---

# Multi-Agent Orchestration Skill

## 目的

这一层不直接判任何对错,它只决定**怎么把"找错"这件事切给多个 agent**:谁先谁后、谁能看见谁的产出、谁的结果落在哪、断了怎么接。审核质量的上限由前面的提取层(转换不丢/覆盖不漏/SSOT 参数长表)和检查层(双轴算法)锁定;这一层决定的是**这个上限能不能被真正榨出来**——切错了,关联召回直接塌一半。

为什么朴素做法不行,两种都试过都不行:

- **做法 A:一个超级 agent 读完所有文件夹一次性审。** 一个型号 13~20 个文件夹的 MD(PDF 转的、带规格表、BOM、检测报告)轻松几百万 token,塞不进上下文窗口;就算塞得进,模型在超长上下文里对"第 04 文件夹某行温度范围"和"第 19 文件夹标签上某个量程"做精确比对的能力断崖式下降,关联错误大面积漏。
- **做法 B:无脑并行 fan-out,N 个 agent 各审各的文件夹,最后合并。** 吞吐高,但对 DHF 审核是**结构性错误**:第 12 文件夹(设计输出)要审的核心是"它的图号/物料码/参数有没有和前面 04~11 冲突、有没有被悄悄放宽"。fan-out 把每个 agent 关进信息孤岛,它根本看不到前序参数,这条关联无从查起——而**关联恰恰是这套审核的命门**。

正确解是**按任务依赖关系分别选择编排形态**:阶段链审核(下游依赖上游)必须**顺序增量**串行,累积 SSOT 喂下一个;维度横扫(7 维各扫一类,彼此独立)用**并行 fan-out**;跨单元对账放在 Phase2 收口。这是用吞吐量换关联召回,且用 resume/心跳把"长任务"这个硬成本扛住。

## 何时用

- 要把整套 DHF/DMR 审核(或任意"逐文件找跨文件不一致"的大任务)拆给多个 agent 跑。
- 要做 **Phase1 单元并行 + Phase2 跨单元对账**(阶段链承接 / 跨版本漂移 / BOM PTR 对账 / 设变回溯 / 7 维度横扫)。
- 长后台任务,中途可能撞会话限额/网络/限流,需要中断后**续跑**而不是从头重来。
- 批量并行转换/渲染分片(几百个文件转 MD、几十张图纸渲 PNG 再切片喂视觉 agent)。

不归这一层管:单个参数怎么判冲突(检查层 `check_params_numeric.py`)、文件怎么转 MD(提取层 `convert_*.py`)、最终报告怎么渲染(`gen_report_*`)。这一层只管"把这些 agent 怎么组织起来跑"。

## 输入

跑编排前先确认这些就位(否则切了也白切):

- 已转换好的型号 MD 语料根目录,如 `<型号>_MD`(每文件夹一组 `.md`,带 YAML 头部 `loss_flags`/`manual_review_required`)。
- 覆盖台账 `coverage_ledger.csv`——确认"该有的文件都在、都转好了",别在一个有缺口的语料上跑审核还以为查全了。
- 阶段检查项基线 `REF`(PT9L 方法论 MD,逐阶段检查项),要求每个 agent 的检查项 ⊇ 它。
- 法规基线 `USBASE`(`us_*.md`,同市场可复用)。
- (Phase2/复审才需要)上一轮的错误总表 CSV(供去重 vs 已有)、裁决库 `_adjudications.csv`(供过滤已裁决误报)。

## 强制工作流

> 总范式(四模板共用):**扇出 / 串行 → 收敛 → 证伪 → 接地**。每条结论必须回正文拿到逐字证据才算数。下面编号步骤给可直接套用的真实脚本路径与命令。规范路径:工具包 `D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\`(交接包另有同份拷贝);编排 JS、汇总器、证据核验、报告生成均在 `D:\AI_0415\03DHF\` 根目录。

1. **先加载通用工作方法 skill,守纪律。**
   - `D:/AI_0415/03DHF/skill/SKILL.md`(working-method)。
   - 它定义了🐱心跳、长任务每 1 分钟报进度、批量转换 gate、诚实标 UNKNOWN——本层全程沿用。

2. **判任务形态:这个切法该并行还是该串行?** 这是本层第一个、也是最容易切错的决策。
   - **有依赖、有方向(下游依赖上游)→ 顺序增量串行。** 阶段链审核(承接走样/参数放宽/设变回溯)属此类:第 i 个 agent 必须看到前 i-1 个累积的参数才能查关联。实现见 `_pt7_incremental_audit.js` 的 `for` 主循环(第 50~75 行)。
   - **无依赖、各扫一类 → 并行 fan-out。** 维度横扫(7 维各派一个 agent)、单元内部完备性、对抗证伪逐条核验属此类。实现见方法论模板 B/A 里的 `await parallel(UNITS.map(...))`。
   - 切错的代价:把阶段链拆成并行 = 关联全断;把独立维度强行串行 = 白白拖长跑时。

3. **顺序增量串行:维护两条累积器,把 SSOT 喂下一个 agent。** 这是关联召回的物理载体。
   - `ssot`(运行参数长表):每元素一行纯文本 `文件夹|参数名=参数值@源文件名`(`source_file` 用 `.split("\\").pop()` 砍成纯文件名省 token)。下一个 agent 拿到它就能看见"前面所有文件夹对'温度范围'这个槽位填过什么值",从而判自己文件夹的值是否被放宽/收窄。
   - `priorFind`(前序发现摘要):每条 finding 压成一行 `[文件夹|内/关联][严重度]类型:描述`,`.slice(0,160)` 截断。让后面 agent 知道前面报过什么、避免重复、能顺藤摸瓜。
   - 每轮 `agent()` prompt 固定七段:① RULES(铁律+审核轴);② 本次文件夹名+第几/共几;③ 去 REF 找对应阶段检查项(要求"你的检查项 ⊇ 它");④ 被审范围(glob 读全该文件夹下所有 `.md`);⑤ 法规基线 USBASE;⑥ **前序已审列表 + ssotDigest + findDigest**(增量精髓);⑦ 产出要求(抽参数 + intra_findings + cross_findings)。
   - 硬截断防爆窗口:`JSON.stringify(ssot).slice(0,55000)`、`priorFind.slice(-120).join("\n").slice(0,20000)`。取 `-120`(最近的)是因为越近的发现越可能和当前文件夹相关。

4. **structured output:字段名必须 ASCII,值可中文。** 这是本层最高频、最致命的踩坑。
   - schema 的 `properties` 键(字段名)**全部用 ASCII**:`folder`/`files_read`/`parameters`/`name`/`value`/`source_file`/`intra_findings`/`severity`/`type`/`desc`/`evidence`/`suggest`/`role`/`cross_findings`/`vs_folder`。**用中文 key(如 `图号`/`严重度`)→ 结构化输出 API 直接 400,整批 agent 失败。** 字段名正则约束 `^[a-zA-Z0-9_.-]{1,64}$`。
   - **枚举值和实际填的内容照样填中文**:`severity` 枚举里大方写 `"待PM确认"`、`"NEI"`;`desc`/`evidence`/`suggest` 全中文(报告是给中文工程师看的)。原因:schema 底层把字段名编进 grammar 的标识符位、非 ASCII 触发校验失败;枚举值只是 string 字面量取值约束,UTF-8 中文合法。
   - `additionalProperties:false` 封死模型加戏,保证回灌 ssot/priorFind 时 `r.parameters`/`r.intra_findings`/`r.cross_findings` 形状 100% 可预测。
   - 刻意的不对称:`intra_findings` 的 required 含 `role`(内部问题能定责任工程师),`cross_findings` 不含 `role`(跨文件夹承接问题往往跨多角色,强制填会逼模型编)。
   - `NEI`(No Evidence Indicator)是故意留的逃生舱:无正文证据时让模型诚实标 NEI,而不是被迫硬塞一个严重度制造误报;下游再把 NEI 过滤掉。

5. **Phase1 单元并行 + Phase2 跨单元对账(收口)。** 单阶段内查不出的,放到 Phase2 一次性拉直。
   - Phase1 `phase('StageAudit')`:`await parallel(UNITS.map(u=>()=>agent(...)))`,每单元抽参数 + 做单元内 4 子轴。
   - Phase2 `phase('CrossStage')`:把各单元摘要 `JSON.stringify(digest).slice(0,90000)` 喂给一个收口 agent,专查这五类跨单元问题:
     - **阶段链承接**:同一参数 `01→04→06→08→09→DMR` 是否被放宽/收窄(下游 ⊆ 上游,有向)。
     - **跨版本漂移**:同号多版本/整树副本/多版并存未作废/版本方向倒置。
     - **PTR/BOM 跨表对账**:EBOM↔ABOM↔组件清单↔WI 物料↔工序大纲↔PFMEA,漏录/多录/用量冲突/规格型号不一致/复用件串号。
     - **设变回溯**:设计变更影响是否回溯到受影响的输入/输出/验证/标签。
     - **维度横扫**:7 维各派一个 agent 横扫全库(模板 B),`Sweep → Dedup(vs 已有错误表)→ Verify(对抗证伪)`,只数净新增。
   - 收口 agent 的 cross schema 字段同样 ASCII(`units_involved`/`vs_folder` 等)。

6. **断点续跑 resume:已完成 agent 命中缓存秒回。** 长链跑一两个小时,中途任何失败都不能从 01 重来。
   - 编排框架以 `(phase, label)` 为键缓存每个 agent 的结构化结果。脚本里给**稳定 label**:PT7 用 `inc:${fo.f}`、PT9L 用 `pt9l:${fo.f}`(绑文件夹名,不用序号 i——中间插一个文件夹时序号会全错位、缓存全失效)。
   - resume 时 `for` 照常从 `i=0` 走,前半截每个 `agent()` 命中缓存秒回,`ssot`/`priorFind` 被缓存结果**重新填满到中断前状态**(回灌逻辑对缓存结果和新结果一视同仁),再从第一个没缓存的文件夹真跑。脚本不写任何"读进度文件、跳过已完成"的逻辑——状态全部从结果重建,没有藏在内存里跨 run 的隐式状态。
   - Workflow 工具层用 `resumeFromRunId` 续跑;撞会话限额时也可拆成单产品/单阶段分批跑。
   - **真实坑:中断没杀干净后台 agent,resume 会和残留进程打架。** 正确做法是中断时先确认后台 agent 已终止,再 resume;不能假设 Ctrl-C 就清干净了整条链。

7. **复审重跑用独立脚本 + 逐字证据强制 + 裁决库过滤,不在旧缓存上修补。** 见 `_pt9l_rerun_audit.js`(骨架与 PT7 同构:同样的 ssot/priorFind/for 累积),两处特化:
   - RULES 加**逐字原文证据强制**:每条 finding 的 `evidence` 必须摘抄文档逐字原文片段(引号括起、可被 grep 核验),否则判 NEI。
   - RULES 带**已裁决误报清单**(如"传感器焊点数 vs 线数不算矛盾""静音是拨动开关""仅美国正确裁剪欧盟是对的"),直接写进 prompt 让 agent 别再报。这串清单来自上一轮人工裁决导出的 CSV,闭环反馈回 prompt。
   - 整体重跑换新 label 命名空间(name=`pt9l-rerun-audit`),而不是在旧 label 缓存上修补——要强制重审某文件夹就让它的 label 失效。

8. **长任务每 2 分钟回🐱心跳。** MEMORY 里明确记着这是用户要的工作方式。
   - 用 `ScheduleWakeup`(调度型唤醒)约每 2 分钟触发一次,输出极简存活信号🐱,然后继续干活。它和审核主循环正交——for 照常跑,心跳是旁路脉冲。
   - 为什么固定周期而不是"每完成一个文件夹报一次":单个 agent 自己可能跑好几分钟(尤其 PT9L 标了"大文件夹"的 08/09/11),只在文件夹完成时报活会有长静默,外层误判死亡。每个 `log("✓ ${fo.f}: ...")` 也是进度信号。
   - 心跳证明"进程活着",不证明"在干正确的事"——它是存活探针,不是正确性探针,不替代看 log 进度。心跳和 resume 配合才完整:心跳告诉你死没死,死了靠 resume 续。

9. **批量并行转换/渲染分片:先 gate 后并行。** 转换/渲染是 fan-out 的天然场景,但必须先过 working-method 的 batch conversion gate。
   - 先按类型分组(DOC/DOCX/Excel/PDF/AI/DWG/ZIP/图片),每类先转 3 个代表文件,检查 source copy / Markdown / manifests / assets / page PNG / `conversion_loss` / 路径编码,样本全通过才跑全量。样本有乱码/空输出/缺 asset/渲染失败就先修转换器。
   - 图纸视觉审核走"渲染分片":前处理用 `prep_2d.py`(`fitz` 渲染 ≥300 DPI + `PIL` 裁切),每张图切成 `full.png + crop_r{0..1}c{0..2}.png`(3×2 分块,overlap 120px),再 fan-out 给视觉 agent 用 `Read` 打开 PNG(多模态)逐块读、最后对账。
   - 转换/渲染产物的 schema 头部字段同样全 ASCII(`source_file`/`loss_flags`/`manual_review_required`)。

10. **汇总落盘:把各 agent JSON 收成三份持久产物。**
    - `python D:\AI_0415\03DHF\assemble_incremental.py <型号> <workflow输出json> [输出目录]`
    - 产出:`<型号>-运行参数长表.csv`(SSOT 长表,4 列 `阶段/参数名/值/出处文件`,utf-8-sig)、`<型号>-错误总表.csv`(按 `SEV={critical:0,major:1,minor:2,待PM确认:3,NEI:4}` 排序、逐行编号)、`<型号>-增量审核报告.md`。
    - 列名跨型号保持一致(与 PT7 对齐),下游报告生成器 `gen_report_pt7_html.py` / `gen_report_review_html.py` 才能复用。改字段名要同步改三处:JS 回灌、Python 汇总映射、HTML 模板取值——改前先 grep 全。

11. **接地:证据核验 + 对抗证伪,把不可信的 finding 拦下来。** 这一步是把 agent 输出从"找出来"变成"可信"。
    - `python D:\AI_0415\03DHF\verify_findings.py`:把每条 finding 的引文拿回全语料 grep(归一化去噪后做子串/长片段三窗口匹配),裁决五类 `有据/有据(部分)/缺失断言/可疑/无引文`,把"可疑"(声称原文写了 X 但全语料找不到)单列成人工复核清单。它是确定性的、不再叫一次大模型——不让嫌疑人自证清白。
    - 维度轴候选**强制走对抗证伪**(模板 B 的 `phase('Verify')`,默认可疑、回原文核对),约毙掉 1/4 候选;证伪前不算结论。
    - 裁决库 `D:\AI_0415\03DHF\_adjudications.csv` 沉淀人工裁决,反哺下一轮 RULES 的"已裁决误报清单"(见步骤 7)。

## 与其它层的衔接

- **上游(提取层)**:`convert_*.py` + `coverage_ledger.py` 决定有多少参数能进 SSOT 长表——本层的关联召回上限被它锁死。先确认覆盖台账无静默缺口,再跑编排。
- **平级(检查层)**:本层把检查层的判定逻辑分发出去。确定性算法(`check_params_numeric.py` 数值一致、`check_table_diff.py` 同构表 diff、`check_bom_crosswalk.py` 跨异构表对账、`check_residue.py` 模板残留)是近零误报的一侧;本层调度的 LLM agent 是高召回的一侧。两侧互补:确定性版近零误报但只看 SSOT 长表(召回低),LLM 版召回高但需证伪。
- **下游(自验证层 + 报告层)**:本层产出的错误总表 CSV 交给 `verify_findings.py` 接地、交给 `gen_report_review_html.py` 渲染成可逐条裁决的离线网页;裁决结果回流 `_adjudications.csv`,闭环到下一轮 RULES。

## 边界与踩坑

- **诚实标边界一:硬截断会丢早期参数。** `slice(55000)`/`slice(20000)`/`slice(-120)` 都是硬截断。ssot 超过 5.5 万字符时(跑到后面文件夹很容易),早期文件夹的参数会被截掉,理论上第 19 文件夹可能看不到第 02 文件夹某个早期参数——超长链路的早期参数关联召回会下降。缓解:把根参数(01 立项的市场/品类)在 RULES 里反复强调让模型优先重抽;priorFind 取最近 120 条。
- **诚实标边界二:Tier1 确定性低召回。** `check_params_numeric.py` 在 PT9L 抓 0 组数值冲突,不是 PT9L 没冲突,而是那批冲突压根不在它的 408 行 SSOT 长表里(抽漏了,纵向链就追不到)。这是已知低召回边界,补召回靠 LLM 维度轴。
- **诚实标边界三:跨表对账非近零误报,漏录降级为 info。** `check_bom_crosswalk.py` 异构表范围天然不同(总装 ABOM 不含机芯件/WI 不列全部件),"某零件只在 BOM 出现"绝大多数不是冲突,所以漏录降级成 info 标"人工看",不假装机器能判;同义词词典手工维护有盲区、模糊归并 0.8 阈值对中文短名偏严会漏并。
- **resume 不解决"上游文件改了"**:缓存按 label 不按文件内容哈希,中断期间改了 04 文件夹的 MD,04 已缓存的话 resume 不会重读——改源文件要主动让对应 label 失效。
- **缓存命中秒回 = 不会重审已完成文件夹**:中断前某文件夹跑得不好(抽得少),resume 不会自动重跑它,会原样采纳。要重审改 label 或清缓存,或直接用独立 rerun 脚本。
- **缺口本身就是发现,不是"没查到"**:DMR 文件夹空 = 设计转换未完成,是 critical 缺口;不能当成"这个维度没问题"。
- **平台锁定**:Word COM 转换只在装 Office 的 Windows 上跑;依赖 `pip install pywin32 xlrd openpyxl pymupdf`。
- **File0N/file:// 链接的脆弱性**:报告里的本地文件链接依赖"agent 编号顺序 == Python sorted 顺序",换语料要重新生成 HTML;`file://` 跳转受浏览器安全策略限制,离线环境一般可用、严格策略下可能被拦。

## Quick Checklist

- [ ] 已加载 working-method skill(🐱心跳、诚实标 UNKNOWN)
- [ ] 任务形态判对:有依赖→串行增量,无依赖→并行 fan-out
- [ ] 覆盖台账确认无静默缺口,再跑编排
- [ ] 顺序增量维护 ssot + priorFind 两条累积器,喂下一个 agent
- [ ] structured output 字段名全 ASCII,值/枚举用中文
- [ ] schema 含 `additionalProperties:false`、`NEI` 逃生舱、intra/cross 的 role 不对称
- [ ] Phase1 单元并行 + Phase2 跨单元对账(阶段链/跨版本/PTR/设变回溯/维度横扫)
- [ ] agent 给稳定 label(绑文件夹名,非序号),支持 resume 命中缓存
- [ ] 复审重跑用独立脚本 + 逐字证据强制 + 裁决库过滤
- [ ] 长任务注册🐱心跳(约 2 分钟)+ log 进度信号
- [ ] 批量转换/渲染先 gate(每类 3 个样本)后并行;图纸走 prep_2d 分片
- [ ] assemble_incremental.py 汇总落盘三份产物(列名跨型号一致)
- [ ] verify_findings.py 接地 + 对抗证伪,"可疑"单列人工复核
- [ ] 中断时先确认后台 agent 终止再 resume
- [ ] 末尾回🐱

🐱
