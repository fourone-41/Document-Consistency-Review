# DHF/DMR 跨文档审核方法论 · 完整交接版（给另一台机器）

> **读者**：另一台机器上的 **Claude Code（Opus 4.8，ultracode 开启）**，没有原始对话上下文。
> **目标**：读完本文，你应当能在本机**独立把一个新型号的 DHF/DMR 审一遍**，产出错误总表 + 检测报告，并大致复现下文"实证基准"的产出规模。
> **方法与机器无关；路径都是源机器(PT9L/PT9S)的占位符，到你这台几乎一定不同——先全局替换成你本机路径再跑。**

---

## 0. 先决条件 & 要从源机器拷过来的文件

**本机环境**：Windows + 装了 Office（`.doc/.xls` 要 Word/Excel COM）；Python 3 + 包 `xlrd openpyxl PyMuPDF Pillow`（`pip install pymupdf openpyxl xlrd pillow`）；Claude Code（Opus 4.8 + ultracode，要有 Workflow 工具）。

**要拷贝的资产（缺了跑不全）**：
| 拷什么 | 源位置 | 作用 |
|---|---|---|
| `dhf_audit_toolkit/`（6 个 .py 全套） | `…\PT9L_CHECK\dhf_audit_toolkit\` | 工具层+机械层全部脚本 |
| 3 个图纸 skill | `用户桌面 SKILL_2D_Drawing_Reading.md / SKILL_3D_Model_Analysis.md / SKILL_3D_Section_Analysis.md` | 图纸分支视觉读图方法 |
| 本方法论（V2 + 详细版 + 本交接版） | `…\03DHF\DHF-DMR审核方法论-*.md`、`…\PT9L_CHECK\…详细版-全阶段-同事版.md` | 方法+逐阶段检查项基线 |
| 美国法规基线（如适用同市场） | `…\PT9L_CHECK\02_RnD_DHF\01 立项批准书E0\us_*.md` | 法规判断基线（用它，别网搜） |

**最小动作链**（详见各章）：原始件本地放好 → `convert`(转MD) → `coverage`(台账) → 机械层(残留/数值/表diff/crosswalk) → 语义层 workflow(阶段轴+维度轴+去重+证伪) → 图纸分支 → (有源码则)代码分支 → 汇总(错误总表+HTML)。

## 文档结构
1. 核心方法（双轴/5层/4铁律3信条/7维度/逐阶段速查/最小动作链）
2. 工具层与机械层脚本（确定性 Tier1/Tier2 + 确切命令）
3. **多智能体 Workflow 模式（阶段轴/维度轴/图纸视觉 三个可直接套用模板 + 必避的坑）**
4. 图纸分支（渲染分块 + 视觉读图 + 对账）
5. 代码分支（固件常量 ↔ 设计规格 对账）
6. 实证基准与踩坑
7. 新型号执行清单（SOP + 自检）


---

## 核心方法

> 本章是整套方法论的"心脏":一句话说清审什么、怎么扫、违反什么就出假结论。后续"地基/流水线/逐阶段清单"都是这一章的展开。
> **路径提示**:本章所有 `D:\AI_0415\...` 仅为 PT9L 机器上的真实路径占位符。新机器请把根目录(型号文件夹、`XXXX_MD/`、脚本目录)整体替换成你本机的实际路径,再往下跑。

---

### 1. 一个底层认知:DHF 是一条"派生链",不是一堆平行文档

DHF/DMR 不是 N 份独立文件,而是一条**单向派生链**:根决策(01 立项)定死"市场+品类",由它推出全链强制法规集合;往下每一阶段都从上游**派生**出更具体的要求,直到 DMR 翻译成"产线怎么做"。

```
01立项(市场/品类=根) → 02计划 → 03风险 → 04设计输入(枢纽闸门)
   → 05结构 / 06硬件 / 07软件(并行派生) → 08 T1验证(收口闸)
   → 09设计输出(出料口) → 10试产(放行闸) → 11设计确认(最终关口) → DMR(末端落地)
```

两条推论,决定整个审核怎么做:
- **根字段歧义 = 全链歧义**。01 把"仅美国"写错一次,下游 100+ 文件一起塌。
- **错误最爱藏在接缝里**。工种与工种、阶段与阶段的交界(04 的值有没有传到 06、09 的图号有没有进 DMR)正是按阶段切分时被"劈成两半、谁都不看"的地方。这直接催生了下面的双轴。

---

### 2. 双轴审核(硬要求:缺一漏一半)

只按阶段扇出会对"接口"失明。必须沿**两条正交轴各扫一遍**,先阶段轴再维度轴。

| 轴 | 怎么扫 | 抓什么 | 一句话定位 |
|---|---|---|---|
| **阶段轴** | 按文件夹 01→DMR,每阶段一个 agent,查阶段内完备性 + 4 子轴(纵向下游≥上游 / 横向参数槽位 / 角色串联 / 反向完备性) | 漏项、收窄、**单阶段内**矛盾 | "每个人活干完没"=完备性 |
| **维度轴**(正交) | 按 7 种检查类型,每类一个 agent **横扫全库** | **跨文档/跨工种接口处**的对不齐、断链、收窄、矛盾、BOM 不配平、版本混用 | "大家的活对不对得上"=一致性 |

实证:两型号上,维度轴在阶段轴之外**净挖 +54 条**经去重+证伪确认的真问题(PT9L 73→104,PT9S 146→169)。**维度轴不是锦上添花,是补阶段轴对接口的盲区。**

---

### 3. 五层地基(决定"能不能审")

| 层 | 做什么 | 关键 |
|---|---|---|
| ① 工具层 | .doc/.xls/.pdf → Markdown + 截图 | AI 读不了原始件;勾选框/图必配 PNG。脚本 `convert_*.py`(Word COM + xlrd + openpyxl + fitz) |
| ② 提取层(**地基中的地基**) | 抽**参数实例长表**:行=参数实例,列=参数名/值/单位/上下限/出处文件/版本/阶段 | 维度轴的数值/不收窄/BOM **全站在这张表上**;抽错=满盘错 |
| ③ 检查层 | 阶段轴 4 子轴 + 维度轴 7 维度 | 双轴在这一层落地 |
| ④ 输出层 | 错误总表(严重度/证据/建议/责任人)+ 检测报告 HTML | 给工程师能直接派工 |
| ⑤ 封闭层 | 结论必须正文逐字证据支撑 | 标题/文件名/清单一行/空勾选都不算 |

---

### 4. 四铁律 + 三信条(违反任一 → 假结论)

**四铁律**

| # | 铁律 | 判错标准 |
|---|---|---|
| 1 | **下游 ≥ 上游** | 只能覆盖/扩大,不能收窄。下游收窄即真错(量程/人群/环境/精度/限值) |
| 2 | **正文封闭** | 结论要正文逐字证据;标题、文件名、清单一行、空勾选框**都不算**关闭 |
| 3 | **看清市场(本案仅美国)** | EU(EN)/中国(GB)非强制,裁剪写 N/A 理由;**反向引用 EN/GB 作美国判定 = 真错** |
| 4 | **一致性 ≠ 正确性** | 审核只判一致性+完备性;值本身对不对要工程师/PM 拍,但可疑值要标出来 |

**三信条**(从"建议"升为硬规则)

| # | 信条 | 要点 |
|---|---|---|
| 5 | **NEI 纪律** | 找不到正文证据 → 判"证据不足(NEI)";**绝不默认通过、绝不编**。NEI 不是失败,缺口本身也是发现 |
| 6 | **双向原文引用** | 判定必须给**具体冲突值 + A 文件值 vs B 文件值**两侧原文;不能只说"对不上";相似 ≠ 一致 |
| 7 | **逐条对抗证伪** | 每条发现派一个"挑刺"agent 回正文试图反驳;证据不实/其实一致/写法误报就毙掉。**实测会毙掉约 1/4 候选**(PT9S 33→23、PT9L 37→31)——这是防"自信地错"的关键 |

---

### 5. 七维度(维度轴横扫的内容,每个一句话)

| 维度 | 一句话查什么 | 算法思路 |
|---|---|---|
| **数值一致** | 同一参数多处取值,**区间+单位归一**后比对,剔写法误报 | 区间算术 + pint 单位归一 + Decimal 精确判定 |
| **可追溯断链** | 需求→输入→输出→验证→确认 逐参数查断链(含**反向**:下游有验证而上游没输入);每个风险控制有无验证;DHF 清单每项是否落地 | 属性图多跳 + 闭世界完备性约束 |
| **不收窄** | 下游区间是否 ⊆ 上游(量程/人群/环境/精度/限值),不得收窄 | 区间包含判定(双向算) |
| **矛盾措辞** | 对立陈述对撞:需临床 vs 免临床 / 版本日期打架 / 同参数互斥值 / **单文件内部**判据矛盾(操作步骤 vs 要求列) | 对立子断言对撞 + 簇级长上下文整读 |
| **BOM 对账** | EBOM/ABOM/包装BOM/组件清单/WI物料/工序大纲/PFMEA **跨表配平**(料号/数量/装箱数) | 列级 schema 匹配 + 单元格 key-join diff + 公差 |
| **版本漂移** | 同号多版本 / 整树副本 / 多版并存未作废 / 版本方向倒置 | MinHash + containment 归族定方向 |
| **角色串联** | 同一工程师名下文件参数自洽;评审独立性(一人多职、审核=批准塌缩) | 按责任人归并 + 同对象多文件对值 |

> 经验:**越成熟的 DHF(有完整 DMR/工序),数值/BOM/版本类跨文档冲突越多**;DMR 未产出的型号则以断链/版本/不收窄为主。最大增量往往来自原本薄弱/没做的维度。

---

### 6. 逐阶段速查表(每阶段:提取什么参数 + 查什么重点)

> 用法:每阶段套同一模板 ——**提取参数 → CHK(基础检查项)+ ADD(操作化加强项)→ 主责工程师 → 实际错**。下表是精简骨架,展开见"逐阶段清单"章。所有阶段都按铁律处理签名/日期/勾选框:**电子版不查签名、无日期不查、空勾选不据此判错**(只在完整性层提示)。

| 阶段 | 提取的核心参数 | 查什么重点(加强项 ADD) |
|---|---|---|
| **01 立项** | 目标市场(仅美国)、产品品类、预期用途、注册路径(510k vs SDV豁免)、客户需求逐条、强制法规基线 | 根决策**唯一性+一致性种子**(市场只定义一次、全链引用);强制清单逐条"锚定"而非"考虑过"(每条法规一行);注册路径口径锁定;模板残留扫(异类品类/旧型号) |
| **02 计划** | 产品身份、计划/名单/进度三张基线文件号、人员基线(项目负责人=谁)、计划阶段链、QP-7.3 九要素 | 项目负责人**唯一锚定**(表头↔表身↔评审同一人);计划文件号全链逐字一致;计划输出↔下游 DHF **双向**对账;九要素逐条覆盖矩阵;阶段适用性逐子项给理由 |
| **03 风险** | 评分规则(P/S/矩阵/剩余/验证准则)、法规来源(24971/60601-1/-1-2)、风险行 R1–Rn、法规↔风险映射(RLOG) | 法规→风险**逐条覆盖矩阵**(每条强制条款落到 ≥1 个 R-ID);每条控制措施**三点闭环**(风险→设计输入→验证);降频有据;EU/中国映射标 N/A 不作美国基准;临床本质性能风险;DFMEA↔风险表一致 |
| **04 设计输入(枢纽)** | 身份、受控件图号、市场/认证口径、量程/分辨率/精度/工作&贮存环境/寿命&电池/防护等级/尺寸重量、法规标准清单 | 受控件齐套+图号唯一锚定;**逐参数 下游≥上游 可判矩阵**(每槽标 equal/broader/narrower);美国强制清单逐条落地;环保栏不得比 01 收窄;**单文件内部矛盾自洽**(电池栏=无 vs 包装含 2×AAA) |
| **05 结构** | 身份、八大结构方案点、整机尺寸/重量、复用件(T-Z1/PT5)、方案&图样评审检查表覆盖 | 整机尺寸/重量**逐值回填**(空白≠通过);复用件版本/图号唯一性跨文件锚定;弹簧参数链自洽(图纸↔ABOM↔T1);方案正文 vs 检查表勾选自洽;**空白测量字段=未证明,不得当已闭环**;图样体系唯一性(模板残留) |
| **06 硬件** | 身份、MCU 型号、升压IC、电源(2×AAA/电压/电流)、低压检测阈值、传感器、显示/按键、PCB 规则 | 传感器型号跨阶段承接(04/05 已定型号 → 06 不得只写"通用");低压阈值跨链一致(设计 2.7/2.5V vs 产线单点);接线根数 设计输出↔作业指导一致;硬件文件版本唯一+产线 WI 去旧型号抬头;旧型号/血压计模板残留 |
| **07 软件** | 身份、MCU 运行环境、内存口径、目标代码产物(.MTP/.BIN)、软件版本号、软件安全等级、功能集、错误阈值、硬件接口表 | **软件版本号全链唯一**(多写法收敛到定版记录);**IEC 62304 安全等级显式声明**(物料分级不能顶替);MCU/烧录对象唯一(.MTP 源 vs .BIN 产物);内存口径三处对齐(SRS/硬件/设计方案) |
| **08 T1验证(收口闸)** | 身份、量程/分辨率/精度/环境/寿命/电池、软件版本、电安判定标准、寿命样本量准则、彩盒版本 | **全参数闭环五点对齐**(设计输入→验证计划→检验标准→验证报告→检测报告逐字一致);判定基准**仅用美国认可标准**(反向引 GB9706/EN=真错);**实测台数 ≥ 准则台数**;软件定版唯一;DFMEA↔风险报告双轨同步;**T1关闭 vs 设计确认延期 边界要正文证据**(空白勾选≠关闭) |
| **09 设计输出(出料口)** | 清单一/二、EBOM、ABOM、复用件、关键图号、目标代码物料码 | **图号唯一性**(一物一号/一号一物);**物料编码跨文件唯一**(同一料同一码);09 ≥ 04–08 逐项不收窄;复用件三要素(等同性依据+受控母图+极性/方向对齐实物);清单/BOM 模板残留与转换残值;清单 vs 实物/作业指导书一致 |
| **10 试产(放行闸)** | 身份、试产模式(实测 vs 免试产)、数量/日期、技术依据(清单1/2/3)、责任人、验收准则、附件、总结字段 | **免试产=审核对象本身**(理由必须正文给出且与"实际试产目的"等价覆盖);引用的清单1/2/3 逐张落地;责任人 vs 02 团队基线一致或有变更理由;问题/整改/量产/再试产四组字段**正文实选,非空模板**(无问题须显式写"本次无问题") |
| **11 设计确认(最终关口)** | 市场口径、身份、临床证据、软件版本、硬件/IFU 版本、可用性结论、风险闭环件、外部报告、标准版本、标签强制要素 | 软件定版唯一性(三处对账);**标签逐元素强制清单**(UDI 801.20-57/801.18 日期/警告/年龄段 三栏:适用性+符合性+验证);外部报告排除项↔替代证据兜底映射;标准版本全链唯一(ASTM/ISO 年号);**仅美国口径**+欧盟基准/符号反向引用排查;血压计/旧型号模板残留 |
| **DMR(末端落地)** | 主记录身份(N 项受控)、工作/静态电流限值、标定/测试温度容差、成品精度温度点、扭力、装箱数、接线根数、目标代码身份、出货放行口径 | **DMR↔DHF 逐参数不放宽矩阵**(每个限值 DMR 只能 ≤DHF,放宽=真错);多产品模板残留扫描;目标代码版本承接(文件名/校验和/MCU 逐字写入烧录 WI);同一参数全链多值收敛(可问责到人);**同一检验单文件内部判据唯一**(操作步骤 vs 要求列);出货放行口径不松于 DHF(AQL/外观限值/抽样) |

---

### 7. 跑一个新型号的最小动作链

```
① 原始件本地放好(替换为你本机路径)
② convert_*.py            原始件 → XXXX_MD/(.doc/.xls/.pdf 全转 MD + PNG)
③ coverage_ledger.py      清单 vs 实物 vs 转换台账,保证"0% 悄悄漏掉"(看分母/缺口)
④ 阶段轴 workflow          每阶段 1 agent:阶段内完备性 + 4 子轴
⑤ 维度轴 workflow          7 维度横扫全库:接口处一致性
⑥ 去重 + 逐条对抗证伪      vs 已有发现去重 → 挑刺 agent 回正文证伪 → 只留确认的净新增
⑦ finalize_*.py / gen_report_html.py   错误总表 + 参数明细 + 按工程师分组 + 检测报告 HTML
```

**复用提示**:`convert_*.py` / `coverage_ledger.py` / `finalize_*.py` / `gen_report_html.py` 都是改路径即可复用;Workflow 两套(阶段轴 + 维度轴)。形式化算法库(SHACL/属性图/MinHash/Z3)是**可选的下一档,不是前提**——本方法用 LLM agent 按算法思路做,已在两型号验证够用;别过度工程(Z3/完整本体/多智能体辩论多被高估)。

**别越界**:审核抓"对不对得上、全不全",值本身对不对要工程师拍(传感器几根线、静音是按钮还是开关,都是 PM 纠的);抽不到证据如实标 NEI;空文件夹(如 DMR 未产出)= 设计转换未完成,本身是 critical,不是"没查到"。


---

## 第X章 工具层与机械层脚本（确定性 Tier1/Tier2）

> 读者：另一台机器上的 Claude Code，无本对话上下文，要据此独立审一个新型号。
> 本章只讲"不需要语义判断、秒出、近零误报或低误报"的确定性部分。语义审核（槽位法/下游≥上游/角色串联）在其它章。
> **第一件事**：把 `dhf_audit_toolkit/` 整个目录拷到新机器（含 6 个 .py），这些脚本就是本章全部资产。源在 `D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\`。

### 0. 整体心智图：两层 + 一道夹缝

| 层 | 谁干 | 脚本 | 误报率 | 产物用途 |
|---|---|---|---|---|
| 工具层（前处理） | 纯 Python，无 AI | `dhf_pipeline.py`（编排）调 `check_residue.py` | — | 老格式 .doc/.xls/.pdf → MD+PNG；覆盖台账；残留扫描 |
| ——夹缝—— | **Claude（你）** 跑语义审核 | 无脚本 | — | 产出"参数明细 CSV"和"BOM 记录表 CSV"喂回机械层 |
| 机械层 Tier1 | 纯 Python，确定性 | `check_residue.py` / `check_params_numeric.py` / `check_table_diff.py` | 近零 | 残留、数值一致、同构表 diff |
| 机械层 Tier2 | LLM 抽取 + 确定性核对 | `check_bom_crosswalk.py` | 低（候选生成器，进人审） | 跨异构 BOM↔清单↔WI 对账 |

执行顺序固定：`setup`（工具层）→ 你跑语义审核产出 CSV → `mechanical`（机械层）。

> **路径占位符提示**：本章所有 `D:\AI_0415\03DHF\...` 是 PT9L 机器的路径。新机器**几乎一定不同**。两处必改：
> 1. `dhf_pipeline.py` 顶部 `BASE = r"D:\AI_0415\03DHF"` → 改成你的工作根。
> 2. `dhf_pipeline.py` 顶部 `MODELS = {...}` 字典 → 复制一段，改成你的型号配置（见 §6）。
> 直接调单个脚本时，命令行里的路径自己换。

---

### 1. 工具层：为什么必须本地转换（网盘/edoc2 读不了老格式）

九安的 DHF 大量是 **老 `.doc` / `.xls`**（Office 97-2003 二进制）。AI 和后续脚本都**读不了原始二进制**；edoc2（九安网盘）MCP 是远端 SSE，**无法读本机文件、也不替你转老格式**。所以第一步必须在**装了 Office 的 Windows 本机**把整个 DHF 文件夹转成 Markdown(+PNG)。

`dhf_pipeline.py` 的 `convert(cfg)` 用四条引擎按扩展名分流（代码见 `dhf_pipeline.py:61-131`）：

| 扩展名 | 引擎 | 怎么转 | 损失标记 |
|---|---|---|---|
| `.doc` / `.docx` | **Word COM**（`win32com.client.DispatchEx("Word.Application")`，`pythoncom.CoInitialize`） | 打开为只读，抽 `doc.Range().Text` + 数表格数 + **遍历 FormFields 数勾选框/勾选数** | `checkbox=N(checked=M)` |
| `.xls` | **xlrd** | 逐 sheet → markdown 表 | — |
| `.xlsx` | **openpyxl**（`read_only, data_only`） | 逐 sheet → markdown 表 | — |
| `.pdf` | **PyMuPDF / fitz** | 有字直接抽；**某页字数<40 视为图，渲 150dpi PNG** 落到 `*.assets/page_NNN.png` | `pdf_low_text=N` |

每个 MD 带 YAML front-matter（`source_file / conversion_status / loss_flags / converted_at`），转换台账写 `<MD>\_manifest_conversion.csv`（列 `rel,type,status,text_len,loss_flags,md,error`）。

**关键边界 / 坑：**
- **必须有桌面版 Office**：Word COM 走 DispatchEx，无 Office 直接失败。这是为什么只能本机跑、不能在网盘侧跑。
- **勾选框、图章、手绘必须看 PNG**：`loss_flags` 标了 `checkbox=` 或 `pdf_low_text=` 的，正文文字不可信，要去看 `*.assets/` 下的 PNG（语义层判断勾没勾、签没签）。
- 转换器跳过 `~$` 开头的 Office 锁定临时文件。
- Windows 控制台默认 GBK，所有脚本开头都 `sys.stdout.reconfigure(encoding="utf-8")`，CSV 一律 `utf-8-sig`（Excel 直接双击不乱码）。

依赖一次装齐（新机器）：
```bash
pip install pywin32 xlrd openpyxl pymupdf
```

转换命令（占位符按 §6 配好 MODELS 后）：
```bash
python dhf_pipeline.py <型号> convert      # 只转换
# 或 setup 一把跑：转换+台账+残留
python dhf_pipeline.py <型号> setup
```

---

### 2. 覆盖台账：清单 vs 实物，防"0% 悄悄漏掉"

`coverage(cfg)`（`dhf_pipeline.py:134-168`）解决一个隐蔽风险：**DHF 清单（分母）里写了某文件，但实物根本不在文件夹里**——若不主动比对，这类整份缺失会被"我只审了在场的文件"悄悄掩盖。

做法：读 DHF 清单 xls（分母，名字由 `dhf_list_glob` 配置，如 `*DHF清单*.xls`），对清单每一项用**强归一化文件名**（去版本号 `vN.N`、去 `eN` 后缀、去标点、去"封面/首页"）和实物文件做 `SequenceMatcher` 模糊匹配，打分判档：

| status | 判据 | 含义 |
|---|---|---|
| `ok` | score ≥ 0.55，或归一名被实物名包含（≥0.9） | 找到对应实物 |
| `review` | 0.45 ≤ score < 0.55 | 像但不确定，**人工看** |
| `missing` | score < 0.45 且清单 form 不含"纸" | **电子件应在却没有 → 重点** |
| `paper` | form 含"纸" | 纸质归档，不在文件夹正常 |

产物 `<CHECK>\coverage_ledger.csv`（列 `stage,seq,name,no,form,status,match,score`）。**先看 `missing` 和 `review` 两类**。

命令：
```bash
python dhf_pipeline.py <型号> coverage
```
边界：清单 xls 的表头/列位若与默认（清单从第 3 行起、列序 阶段|序号|名称|编号|形式）不同，需调 `coverage()` 里读取下标；模糊匹配可能误判同名不同版，`review` 行务必人工复核。

---

### 3. Tier1 — `check_residue.py`：模板残留 / 异类型号 / 占位符

**用途**：扫 MD 文件夹，抓三类最高频、最低级、最该机器扫的残留——别的产品名混进来、旧型号没清、占位符没填。文件 `dhf_audit_toolkit\check_residue.py`。

三类命中（`scan()` 逐行正则，`check_residue.py:32-65`）：

| 严重度 | 类型 | 命中什么 | 怎么处理 |
|---|---|---|---|
| 高 | 异类品类残留 | 血压计/血压/袖带/耳机/雾化器/冲牙器/PC Link（`DEFAULT_FOREIGN`）+ `--foreign` 追加 | **基本都是错**，模板没改干净，优先清 |
| 中 / 待确认 | 异类型号残留 | PT3/PT5/PT9C/AG-633/... + `--models` 追加；命中 `--allow-reuse` 列表 → 降为"待确认(可能复用)" | 区分**合法复用件** vs **真残留** |
| 低 | 占位符未替换 | `XXXX` / 待填 / 待定 / TODO / `○○` / `＿＿＿` / `____`（`PLACEHOLDER`）；"年 月 日"空栏按规则**不报** | 模板没填，要补 |

异类型号匹配用单词边界 `(?<![A-Za-z0-9])...(?![A-Za-z0-9])` 防误命中子串。自动跳过 `_manifests / llm_wiki / __pycache__ / dhf_audit_toolkit` 目录。输出按严重度排序的 CSV（列 `严重度,类型,文件,行号,命中,原文`）。

**确切命令行：**
```bash
# 直接调（路径换成你的 MD 文件夹）
python check_residue.py "<你的MD文件夹>" --product <型号> --out 残留.csv

# 冲牙器例：把体温计/雾化器当异类，补自己旧型号
python check_residue.py "D:/.../CYQ_MD" --product CYQ \
  --foreign 体温计,雾化器,血压计 --models 旧型号A,旧型号B --out 冲牙器残留.csv

# 经 pipeline 调（自动用 MODELS 里的 foreign/models，输出到 <CHECK>\机械校验-残留.csv）
python dhf_pipeline.py <型号> residue
```
参数：`--product`（本型号，仅标注用）、`--foreign`（追加异类品类，逗号分隔）、`--models`（追加异类型号）、`--allow-reuse`（合法复用件型号，命中只标"待确认"不算错，默认 `PT5,PT3,T-Z1,Public,KD,PT1`）、`--out`。

**边界**：异类型号的"复用件 vs 残留"机器分不清，必须人工拍（看是否合法沿用成熟机型）。"年 月 日"空栏不报是刻意的（日期空栏交语义层）。PT9L 实测：一次扫出血压计/袖带 20 条、FDIR/PT9C 真残留、占位符 65 条。

---

### 4. Tier1 — `check_params_numeric.py`：数值一致性（单位归一 + 区间 + 近零误报）

**用途**：读你（Claude）语义审核产出的"参数实例长表"，对**同一规范参数**的多个取值做确定性一致性核对，只报"归一后仍冲突"的。文件 `dhf_audit_toolkit\check_params_numeric.py`。这是全工具包**最讲究"近零误报"**的一个。

输入是一张 CSV 长表，每行一个参数实例（列名兼容多种叫法）：

| 逻辑列 | 兼容列名 |
|---|---|
| 参数名 | 参数名 / 名称 / 条目 |
| 值 | 值 / 取值 / 参数值 / 数值/要求 / 数值 |
| 出处文件 | 出处文件 / 来源文件 / 文件 / 来源位置 / 文档 |
| 阶段 | 阶段 / 来源阶段 / 阶段角色 |

四步管线（`check_params_numeric.py:36-188`）：
1. **规范参数名**（`canon`）：同义词归并到 canonical（工作电流/静态电流/显示量程/工作温度/存储温度/标定温度/自动关机时间/低压阈值/电池容量/防护等级/整机重量/整机尺寸/装箱数）。带负向护栏：整机重量/尺寸命中"箱/包装/运输/托盘"则丢弃（不与包装尺寸混）。
2. **单位归一**：温度 ℃/℉→℃；电流 A/mA/µA→mA（低压阈值是电压 V 不换算）；长度 cm/in→mm；时间 分/时→s；重量 kg→g。
3. **解析成签名**（`signature`）：识别 `IP`(防护)/`DIM`(尺寸三元组)/`RNG`(区间，含"最大X最小Y"还原为区间)/`TOL`(a±b)/`BND`(≤/≥边界)/`PT`(单点)。解析不了 → `None` → **跳过**（保近零误报）。
4. **分组比对**：按 `(规范参数, 限定词)` 分组（限定词如"静态/动态/物温/体温"）。点落在某区间/容差内**不算冲突**；组内出现 ≥2 个归一后仍不同的取值才报。

**为什么近零误报（核心卖点）**：
- `34-43` vs `34~43` → 都归一成区间 `[34,43]` → 同签名 → **不报**（剔写法误报）。
- `最大42.9最小32` vs `32~42.9` → 都还原成 `[32,42.9]` → **不报**。
- `32~42.9` vs `34-43` → 不同 → **报**，并给每个取值 + 出处文件（可签字定位）。
- 过滤实测/装箱噪声：值含"实测/水槽/号机/次测/逐次/measured"跳过；电池容量含"说明书/装箱/一台"等跳过。

**主动放弃（诚实边界）**：测量精度/分辨率**不做确定性比对**——它们带温度段 + 重复性歧义，确定性不可靠，**交给语义层（你）判断**。这是设计取舍，不是漏。

**确切命令行：**
```bash
python check_params_numeric.py 参数明细.csv --product <型号> --out 数值冲突.csv

# 经 pipeline（需 MODELS 里 params 指到你的明细 CSV）
python dhf_pipeline.py <型号> numeric     # 或 mechanical
```
输出 CSV 列：`序号,规范参数,限定词,冲突取值数,取值A,出处A,取值B,出处B,其它取值`。
**边界**：输入质量决定一切——这张长表是你语义审核抽的，抽错/漏抽它无能为力；它只查"对不对得上"，**值本身对不对要工程师拍**。

---

### 5. Tier1 — `check_table_diff.py`：同构表 key-join 精确 diff

**用途**：比两份**同构**表（同一 BOM 在两阶段/两版本，或组件清单前后），按主键对齐，出"仅 A 有 / 仅 B 有 / 两边都有但某列不同"。文件 `dhf_audit_toolkit\check_table_diff.py`。治"同一 BOM 跨阶段/版本是否漂移"，给可签字的定位级差异。

机制（`check_table_diff.py:34-101`）：自动探测表头行（找含"物料编码+序号/品/图号"的行）；主键默认 `物料编码/物料编号/图号/料号`，主键空时用 `品名|型号` 兜底；比对列取两表交集（去主键、去序号），逐列 `norm` 后比对。直接读 `.xls`(xlrd) / `.xlsx`(openpyxl)，**无需先转 MD**。

**确切命令行：**
```bash
python check_table_diff.py A.xls B.xls \
  --labelA T1 --labelB 设计输出 --out diff.csv

# 指定主键/比对列/表头行（不给则自动探测）
python check_table_diff.py A.xls B.xlsx \
  --key 物料编码 --cols 材质,规格,型号,封装形式,配比 --header 2 \
  --labelA BOM_v1 --labelB BOM_v2 --out diff.csv
```
参数：`a` `b`（两文件）、`--key`、`--cols`（比对列，逗号分隔）、`--header`（表头行号，0 基）、`--labelA/--labelB`（输出里的列名）、`--out`。输出列：`类型,主键,列,labelA,labelB`，并打印重复键数。
**边界**：**仅适用同构表**（列结构一致）。跨异构表（BOM↔清单↔WI，列名/口径不同）对账**用不了这个**，要走 §6 的 crosswalk。表头自动探测可能失手，必要时手动 `--header`。

---

### 6. Tier2 — `check_bom_crosswalk.py`：跨异构 BOM↔清单↔WI 对账（LLM 抽 + 确定性核对）

**用途**：把**结构不同**的 BOM、组件清单、装配 WI（工艺指导，散文）放一起对账，抓"同一零件在不同来源用量/规格/图号对不上"。文件 `dhf_audit_toolkit\check_bom_crosswalk.py`。这是**混合**脚本：标准表确定性抽、WI 散文由**你（LLM）**抽，工具只做确定性聚合核对。

工作流（关键：分工）：
1. **标准表（BOM/清单）**：列同义词映射确定性抽 → 统一记录表。
2. **WI 散文**：**你（Claude）**逐工步读，抽成同 schema 记录（"3 颗螺钉拧后壳" → 来源=WI, 品名=螺钉, 用量=3, ...）。
3. 全部汇到一张统一记录表 CSV，列固定：`来源, 品名, 用量, 规格, 图号, 物料编码`。
4. 工具（`check_bom_crosswalk.py:50-147`）做：品名规范化（`SYN` 同义词表 + `SequenceMatcher` 模糊归并；**弹簧按正/负/双联极性不合并**）→ 中文数字"三颗/两个"→数字 → 按零件聚合每来源用量(求和，覆盖 WI 多工步)/规格/图号 → 核对。

输出三个 CSV：

| 文件 | 内容 | 性质 |
|---|---|---|
| `对账.csv` | **真冲突**：用量冲突 / 规格冲突 / 图号冲突（归一后跨来源无交集才报） | 重点查 |
| `对账-info范围差异.csv` | 仅部分来源出现（如 ABOM 不含机芯件、WI 不列全部件） | **信息项，人工看，非自动放行** |
| `对账-crosswalk.csv` | 零件 × 来源 的用量/图号矩阵 | 总览 |

**确切命令行：**
```bash
python check_bom_crosswalk.py 记录表.csv --out 对账.csv
```
参数：`csv`（统一记录表）、`--out`。

**为什么不用嵌入模型**：这些标准化 DHF 表用**列同义词映射**就能对齐列，**不需要 bge-m3 嵌入**。真遇到任意陌生表头再上嵌入召回。

**边界（诚实，必须告诉用户）**：
- **不是近零误报**——这是"候选生成器 → 低置信进人审"，不是自动放行。
- 范围差异已降级为信息项；LLM 抽取瑕疵（如把"3 颗螺钉"误挂到后壳）难免。
- 同义词表 `SYN` 是体温计/小家电域定制的，新品类（如冲牙器）要补自己的零件别名和**不可合并**项（类似弹簧极性）。
- 实证（PT9S 总装 ABOM↔装配 WI）：确定性复现了原先只靠 LLM 发现的 **螺钉 ABOM=10 vs WI=9** 真冲突。

---

### 7. 编排器 `dhf_pipeline.py`：一条命令跑完前处理

文件 `dhf_audit_toolkit\dhf_pipeline.py`，把 §1–§4 串成两段（中间夹你的语义审核）：

```bash
python dhf_pipeline.py <型号> setup        # ①转换 ②覆盖台账 ③残留扫描（纯确定性前处理）
# --- 这里你（Claude）跑语义审核：阶段轴+维度轴，产出 参数明细CSV / BOM记录表CSV / 错误总表 ---
python dhf_pipeline.py <型号> mechanical   # ④数值一致（⑤表diff/对账按需手动调）
```
子命令也可单跑：`convert / coverage / residue / numeric`。

**加新型号（两处必改）：**
1. 顶部 `BASE = r"D:\AI_0415\03DHF"` → 你的工作根。
2. 复制 `MODELS` 里一段（PT9S/PT9L 是现成样板，`dhf_pipeline.py:21-43`），改：

| 键 | 含义 | 示例 |
|---|---|---|
| `raw` | 原始 DHF 文件夹 | `BASE+r"\PT9S\PT9S_DHF"` |
| `md` | 转换输出 MD 文件夹 | `BASE+r"\PT9S_MD"` |
| `check` | 检查/报告输出 | `BASE+r"\PT9S_CHECK"` |
| `dhf_list_glob` | DHF 清单文件名 glob | `"*DHF清单*.xls"` |
| `market` / `category` | 市场 / 品类（仅打印） | `"仅美国"` / `"红外体温计"` |
| `foreign` | 异类品类词（残留扫描） | `"血压计,袖带,耳机,雾化器,冲牙器"` |
| `models` | 异类型号（残留扫描） | `"PT3,PT5,PT9C,..."` |
| `params` | **你语义审核后产出的参数明细 CSV**（数值检查输入） | `BASE+r"\PT9S_CHECK\PT9S-参数明细.csv"` |

注意 `params` 在 `setup` 时还不存在，要先跑完语义审核产出它，再跑 `mechanical/numeric`（脚本检测不存在会提示而非崩溃）。

### 8. 四条铁律（机械层产物交人/交语义层时复述）
1. **下游≥上游**：下游只能覆盖/扩大，不能收窄。
2. **正文封闭**：结论要正文逐字证据；标题/文件名/勾选行不算。
3. **仅美国时**：欧盟/中国标准非强制（裁剪写 N/A 理由；反向引用作美国判定 = 真错）。
4. **一致性 ≠ 正确性**：脚本（和你）只查"对不对得上"，**"值本身对不对"必须工程师拍**（如传感器几根线、静音是按钮还是开关）。

### 9. 文件清单（拷到新机器 `dhf_audit_toolkit/`）
| 文件 | 角色 |
|---|---|
| `dhf_pipeline.py` | 编排器（改 BASE + MODELS） |
| `check_residue.py` | Tier1 残留/型号/占位符 |
| `check_params_numeric.py` | Tier1 数值一致（近零误报） |
| `check_table_diff.py` | Tier1 同构表 diff |
| `check_bom_crosswalk.py` | Tier2 跨异构 BOM 对账（LLM 抽+确定性核对） |
| `README.md` | 同事自助版说明 |

源目录：`D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\`（新机器路径自改）。依赖：`pip install pywin32 xlrd openpyxl pymupdf`，本机需 Windows + 桌面版 Office。

---

## 第3章 多智能体 Workflow 模式（语义层的引擎）

> 语义审核（双轴 + 图纸视觉）靠 Workflow 工具的多智能体并行跑。下面 3 个模板**可直接改路径套用**。范式统一：**扇出 → 收敛 → 证伪 → 接地**（每条结论回正文拿证据才算）。

### ⚠️ 必避的坑（先看，全是真摔过的）
1. **结构化 schema 的字段名(property keys)必须 ASCII**（`^[a-zA-Z0-9_.-]{1,64}$`）。**用中文 key（如 `图号`/`严重度`）→ API 直接 400，整批 agent 失败。** 解法：key 用英文（`dwg_no`/`severity`），**值照样填中文**。
2. **图片(PNG)给视觉 agent**：agent 用 `Read` 打开 PNG 即可看图（多模态）；图纸/扫描件走这条。
3. **对抗证伪会毙掉约 1/4 候选**——这是诚实，不是损失；留下的每条都回过正文。
4. **去重要 vs 已有发现**（dedup agent 读已有错误总表 CSV），只数"净新增"。
5. **会话限额**：长 workflow 可能中途撞限额；用 `resumeFromRunId` 续跑（已完成 agent 走缓存），或拆成单产品/单阶段分批跑。
6. **DMR/某文件夹为空** = 设计转换未完成，是 critical 缺口，不是"没查到"。

---

### 模板 A：阶段轴审核（按文件夹 01→DMR，每阶段一个 agent + 跨阶段收尾）

```js
export const meta = { name:'dhf-stage-axis', description:'阶段轴:每阶段内完备性+4子轴, 再跨阶段下游≥上游/角色串联',
  phases:[{title:'StageAudit'},{title:'CrossStage'}] }
const MD="<新型号>_MD 根目录"            // 改成本机路径
const REF="…详细版-全阶段-同事版.md"      // 逐阶段检查项基线
const USBASE="…us_*.md"                  // 法规基线(同市场可复用)
const RULES=`审 <型号>(市场/品类)。4轴:①纵向下游≥上游②横向参数槽位③角色串联④反向完备性(强制清单逐条).
铁律:仅美国(EN/GB反向引用=真错)/正文封闭(无正文判NEI)/电子版不查签名/值对不对工程师拍但要标可疑.
抽参数尽量多(为差评归因预留). 已知模式重点撞:参数全链放宽/模板残留多型号/标签法规缺(UDI 880.2910)/市场口径矛盾/编号唯一性/验证不足.`
// 每阶段一个单元:folders=该阶段MD子文件夹, ref=去REF找对应阶段那节, focus=本阶段重点
const UNITS=[ {id:"01",name:"立项",folders:["01 立项阶段"],ref:"01 立项",focus:"根决策唯一+强制法规逐条锚定"},
  /* 02 开发计划 / 03 风险 / 04 设计输入 / 05结构 / 06硬件 / 07软件 / 08 T1 / 09设计输出 / DMR / 10试产 / 11设计确认 / 19上市 … 同样列出 */ ]
const STAGE_SCHEMA={type:"object",additionalProperties:false,properties:{
  unit_id:{type:"string"}, files_read:{type:"integer"},
  parameters:{type:"array",items:{type:"object",additionalProperties:false,
    properties:{name:{type:"string"},value:{type:"string"},source_file:{type:"string"}},required:["name","value","source_file"]}},
  findings:{type:"array",items:{type:"object",additionalProperties:false,properties:{
    id:{type:"string"},severity:{type:"string",enum:["critical","major","minor","待PM确认"]},
    axis:{type:"string"},type:{type:"string"},desc:{type:"string"},
    evidence:{type:"string"},suggest:{type:"string"},role:{type:"string"}},
    required:["id","severity","axis","type","desc","evidence","suggest","role"]}}},
  required:["unit_id","files_read","parameters","findings"]}
phase('StageAudit')
const res = await parallel(UNITS.map(u=>()=>agent(
  `${RULES}\n单元:${u.id} ${u.name}\nPT9L对应阶段(去 ${REF} 找检查项):${u.ref}\n重点:${u.focus}\n`+
  `被审文件夹(glob读全.md):\n${u.folders.map(f=>"  "+MD+"\\"+f).join("\n")}\n法规相关读:${USBASE}\n`+
  `步骤:读全→尽量多抽参数→对照检查项做4轴检查(我的检查项要⊇基线)→每条finding给正文逐字证据+文件+责任工程师.`,
  {label:`audit:${u.id}`,phase:'StageAudit',schema:STAGE_SCHEMA})))
const ok=res.filter(Boolean)
const digest=ok.map(s=>({unit:s.unit_id,params:(s.parameters||[]).map(p=>`${p.name}=${p.value}@${p.source_file}`),
  findings:(s.findings||[]).map(f=>`[${f.severity}]${f.id} ${f.type}:${f.desc}`)}))
phase('CrossStage')
const cross=await agent(`跨阶段(单阶段查不出的):①纵向同一参数 01→04→06→08→09→DMR 是否被放宽/收窄②同工程师名下跨文件自洽③市场口径全链一致/标准版本唯一/模板残留跨阶段. 给双向引用+责任人.\n各单元摘要:\n${JSON.stringify(digest).slice(0,90000)}`,
  {label:'cross',phase:'CrossStage',schema:{type:"object",additionalProperties:false,properties:{
    cross_findings:{type:"array",items:{type:"object",additionalProperties:false,properties:{
      id:{type:"string"},severity:{type:"string"},type:{type:"string"},desc:{type:"string"},
      units_involved:{type:"string"},evidence:{type:"string"},role:{type:"string"}},
      required:["id","severity","type","desc","evidence","role"]}}},required:["cross_findings"]}})
return {units:ok, cross:cross||{cross_findings:[]}}
```
跑完用 Python 把 units[].findings + cross.cross_findings 拍平成错误总表 CSV（severity 排序、编号），再出 HTML（见第2章 finalize/gen_report）。

---

### 模板 B：维度轴审核（7 维度横扫 → 去重 → 对抗证伪，挖接口盲区）

```js
export const meta={name:'dhf-dimension-axis',description:'7维度横扫全库→vs已有去重→逐条证伪→净新增',
  phases:[{title:'Sweep'},{title:'Dedup'},{title:'Verify'}]}
const P={id:"<型号>", params:"…参数明细.csv(阶段轴产出的参数长表)", err:"…已有错误总表.csv", md:"<型号>_MD"}
const DIMS=[
 {k:"数值一致",hint:"参数表按参数名group-by,同参多处取值区间+单位归一比对,剔写法误报,双向原文引用"},
 {k:"可追溯断链",hint:"需求→输入→输出→验证→确认逐参数查断链(含反向:下游有验证上游无输入);每个风险控制有无验证;清单每项落地"},
 {k:"不收窄",hint:"下游区间⊆上游(量程/人群/环境/精度/限值),⊄=收窄"},
 {k:"矛盾措辞",hint:"对立陈述:需临床vs免临床/版本日期打架/同参数互斥值/单文件内部判据矛盾"},
 {k:"BOM对账",hint:"EBOM/ABOM/组件清单/WI物料/工序大纲/PFMEA跨表对账:漏录/多录/用量冲突/规格型号不一致/复用件串号"},
 {k:"版本漂移",hint:"同号多版本/整树副本/多版并存未作废/版本方向倒置"},
 {k:"角色串联",hint:"同工程师名下参数自洽;一人多职评审独立性"}]
const RULES=`维度轴重审,挖阶段轴漏在接口缝隙的新问题. 铁律:仅美国(EN/GB反向=真错)/正文封闭(无证据判NEI不编)/电子版不查签名/值对不对工程师拍. 相似≠一致,判定给具体冲突值+双向原文引用. **专找已有错误总表里没有的新问题**.`
const FIND={type:"object",additionalProperties:false,properties:{dimension:{type:"string"},
  findings:{type:"array",items:{type:"object",additionalProperties:false,properties:{
    id:{type:"string"},severity:{type:"string",enum:["critical","major","minor","待PM确认","NEI"]},
    type:{type:"string"},desc:{type:"string"},evidence_a:{type:"string"},evidence_b:{type:"string"},files:{type:"string"}},
    required:["id","severity","type","desc","evidence_a","evidence_b","files"]}}},required:["dimension","findings"]}
phase('Sweep')
const sweep=await parallel(DIMS.map(d=>()=>agent(
  `${RULES}\n产品:${P.id} 维度:【${d.k}】\n${d.hint}\n必读:参数表 ${P.params};已有错误表 ${P.err}(只找它没有的);需原文去 ${P.md} 读对应.md.\n每条给严重度/双向原文引用(evidence_a文件A值,evidence_b文件B值)/文件;无证据判NEI.`,
  {label:`${P.id}:${d.k}`,phase:'Sweep',schema:FIND})))
const all=sweep.filter(Boolean).flatMap(r=>(r.findings||[]).map(f=>({...f,dimension:r.dimension})))
phase('Dedup')
const dd=await agent(`读已有错误表 ${P.err},逐条判下列发现 NEW(未覆盖真新增) 还是 DUP. 只留NEW(排除NEI).\n${JSON.stringify(all).slice(0,120000)}`,
  {label:`dedup:${P.id}`,phase:'Dedup',schema:{type:"object",additionalProperties:false,properties:{
    new_findings:{type:"array",items:{type:"object",additionalProperties:true}},dup_count:{type:"integer"},new_count:{type:"integer"}},required:["new_findings","dup_count","new_count"]}})
phase('Verify')
const ver=await parallel((dd?.new_findings||[]).map(f=>()=>agent(
  `**对抗式核验**(默认可疑):回 ${P.md} 原文核对 evidence_a/evidence_b 是否真实且确实冲突. 真问题→confirmed=true;证据不实/其实一致/写法误报/无支撑→false. 守铁律(仅美国裁剪不算错).\n${JSON.stringify(f)}`,
  {label:`vf`,phase:'Verify',schema:{type:"object",additionalProperties:false,properties:{confirmed:{type:"boolean"},final_severity:{type:"string"},reason:{type:"string"}},required:["confirmed","final_severity","reason"]}})
  .then(v=>v?{...f,confirmed:v.confirmed,final_severity:v.final_severity}:null)))
return {confirmed_new:ver.filter(Boolean).filter(x=>x.confirmed)}
```

---

### 模板 C：图纸视觉审核（render 分块 → 视觉 agent 按 SKILL_2D 读 → 对账）

**前处理(Python，先跑)**：把关键图纸 PDF 渲成 **≥300 DPI** 再 **3×2 分块切图(overlap 120px)**（代码同 `prep_2d.py`：`fitz` 渲染 + `PIL` 裁切；输出每张图 `full.png + crop_r{0..1}c{0..2}.png`）。

```js
export const meta={name:'dhf-drawing-vision',description:'按用户SKILL_2D视觉读图+对账',phases:[{title:'SkillRead'},{title:'Reconcile'}]}
const SKILL="…SKILL_2D_Drawing_Reading.md"   // 用户的2D读图方法
const D2="…_drawings2d"                        // 前处理输出目录
const ABOM="…BOM记录.csv"; const PARAMS="…参数明细.csv"
const NAMES=["外观图","总装图","上盖","下盖","按键","透镜","原理图", /*…*/]
const imgs=(dir)=>["full.png","crop_r0c0.png","crop_r0c1.png","crop_r0c2.png","crop_r1c0.png","crop_r1c1.png","crop_r1c2.png"].map(f=>`${D2}\\${dir}\\${f}`)
// ⚠️ schema 字段名 ASCII!
const S={type:"object",additionalProperties:false,properties:{drawing:{type:"string"},readability:{type:"string"},
  titleblock:{type:"object",additionalProperties:false,properties:{dwg_no:{type:"string"},name:{type:"string"},material:{type:"string"},scale:{type:"string"},edition:{type:"string"},model_no:{type:"string"}},required:["dwg_no","edition"]},
  tech_req:{type:"array",items:{type:"string"}},
  dims:{type:"array",items:{type:"object",additionalProperties:false,properties:{no:{type:"string"},symbol:{type:"string"},prefix:{type:"string"},value:{type:"string"},tol:{type:"string"},note:{type:"string"},conf:{type:"string"}},required:["value","conf"]}},
  anomalies:{type:"array",items:{type:"string"}}},required:["drawing","readability","titleblock","dims","anomalies"]}
phase('SkillRead')
const reads=await parallel(NAMES.map(nm=>()=>agent(
  `按2D读图方法审一张图纸. 第一步 Read 通读方法:${SKILL}. 第二步 Read 看图(整页+6块切图,细节看切图):\n${imgs(nm).map(p=>"  "+p).join("\n")}\n`+
  `这是${nm}. 严格按skill输出(值填中文进英文key):标题栏8项/技术要求逐条/逐编号尺寸(符号①vsΦ视觉确认·前缀·公差形式不简化·括号逐字·A B C可信度)/异常(他型号残留PT3PT5/内部矛盾/看不清需更高DPI). **无3D方位校准→角度含义标"待确认"禁止下n个均布**. 只报图上确实看到的,不猜功能/运动量.`,
  {label:`2d:${nm}`,phase:'SkillRead',schema:S}).then(r=>r?{...r,_n:nm}:null)))
phase('Reconcile')
const rec=await agent(`对账产出图纸轴findings:①图纸dwg_no vs 文件名/BOM图号(${ABOM})②图纸尺寸 vs 设计输入(${PARAMS}整机尺寸行)③材料 vs BOM材质④版本 vs 清单⑤异常(他型号残留/看不清重渲/角度待3D). 每条:drawing/type/severity/desc/dwg_side/ref_side/suggestion. 看不清判NEI不猜.\n${JSON.stringify(reads.filter(Boolean)).slice(0,90000)}`,
  {label:'recon',phase:'Reconcile',schema:{type:"object",additionalProperties:false,properties:{findings:{type:"array",items:{type:"object",additionalProperties:true}},summary:{type:"string"}},required:["findings"]}})
return {reads:reads.filter(Boolean),reconcile:rec}
```

> 3D(STP)分支：用户另有 `SKILL_3D_Model_Analysis` / `SKILL_3D_Section_Analysis`（cadquery/OCP，bbox+剖面，信息边界铁律：bbox≠形状、不猜功能、HLR 方位校准枚举 8 种 gp_Ax2）。需 `pip install cadquery`（重）。按需启用；只做 2D 也能覆盖图号/版本/材料/标题栏 + 技术要求。


---

## 第N章 图纸分支(2D工程图 / 3D STP)

### 0. 为什么图纸要单开分支

主链(DHF/DMR跨文档审核)处理的是可被文本/表格直接解析的文档(Word/Excel/PDF文字层)。**工程图纸是主链读不了的特殊内容**:它是矢量线条+图形符号,文字层往往缺失或乱码,圆圈编号①与希腊字母Φ在低分辨率下视觉混淆,公差是上下标小字,中心区域线条密集。直接把图纸PDF喂给文本解析=必然误读。

所以图纸单独走一条**视觉分支**:渲染成高DPI位图 → 分块切图 → 每张分块图交给视觉agent,而视觉agent必须**先读图纸skill当方法论、再读图**。读完产出结构化尺寸表,最后回到主链做对账(图号/尺寸/材料/版本 vs BOM和设计输入)。

分两种载体:
- **2D图(PDF)**: 主力分支。本章详述。已有可直接复用的前处理脚本 `prep_2d.py`。
- **3D模型(STP/STEP)**: 按需启用。需要重型依赖`cadquery`,仅当2D读到极限仍分不清三维结构时才上。

---

### 1. 必须先拷贝用户的3个图纸skill(硬前置)

新机器**没有本对话上下文**,这3个skill文件是2D/3D读图的全部方法论,必须随项目一起拷过去。**它们是Read进上下文的方法文档,不是自动加载的**——视觉agent每读一类图前要先`Read`对应skill:

| Skill文件 | 作用 | 何时读 |
|---|---|---|
| `SKILL_2D_Drawing_Reading.md` | 2D图读图法(标题栏/技术要求/逐编号尺寸/6项自检/可信度分级/9大误读案例) | 读**每张2D分块图之前** |
| `SKILL_3D_Model_Analysis.md` | 3D整体形状/bbox/装配空间(cadquery+OCP) | 启用3D分支时 |
| `SKILL_3D_Section_Analysis.md` | 3D剖面/壁厚/配合间隙 | 验证配合区时 |

源位置(本次确认存在的): `C:\Users\Humiture\Desktop\SKILL_2D_Drawing_Reading.md`。另两个3D skill在用户机器同类目录。

> **新机器提示**: 这些是用户私有skill,不在任何公共仓库。交接时必须把3个文件一并打包拷贝到新机器,路径自定(如`<NEW_SKILLS_DIR>/`)。视觉agent的Read调用要指向新机器实际路径,**别照抄`C:\Users\Humiture\Desktop\`**。

---

### 2. 2D分支:前处理(渲染+分块)

复用脚本 `D:\AI_0415\03DHF\prep_2d.py`(确认存在)。它做的事,完全对齐SKILL_2D的Step1/Step2:

- **渲染 DPI=320**(SKILL硬要求≥300;200DPI下①↔Φ必混淆,是已知翻车场景)。用`PyMuPDF(fitz)`: `page.get_pixmap(dpi=320)`。
- **分块切图 3列×2行=6块, overlap=120px**(块间重叠防标注被切断)。A3图320DPI约3700×2600px,一次读全图细节会丢,必须分块。
- 同时存`full.png`(全图,看版面)和6张`crop_rXcY.png`(分块,逐块视觉读)。
- 输出`_2d_manifest.csv`(图名/源PDF/尺寸px/full/crops路径),供主链对账时索引。

脚本里3个路径占位符,新机器**必须改**:
```python
SRC = r"<图纸PDF所在目录, 原: D:\AI_0415\03DHF\PT9S\PT9S_DHF>"
OUT = r"<输出目录, 原: D:\AI_0415\03DHF\PT9S_CHECK\_drawings2d>"
WANT = ["外观图","总装图","上盖","下盖","-按键",...]  # 高价值图关键词, 按新型号零件名改
```
`WANT`是关键词白名单——只渲染有标题栏+尺寸、需对设计输入/BOM的高价值图(结构件/外观/总装/原理图),跳过纯示意图。脚本还按"设计输出签字档>普通"打分去重同名图。

运行: `python <NEW>\prep_2d.py`(脚本头已`sys.stdout.reconfigure(encoding="utf-8")`,Windows中文不乱码)。依赖: `pip install pymupdf pillow`。

> 中心/密集区不够清时,SKILL_2D允许临时把DPI升到600/1200,或裁200×200px小窗逐条数线(Step2手段1)。这是"读到极限"的兜底,不是默认。

---

### 3. 2D分支:每张图的强制工作流(视觉agent执行)

视觉agent对**每张分块图**:先`Read SKILL_2D_Drawing_Reading.md`(把方法装进上下文),再`Read crop_rXcY.png`(视觉读图)。然后严格按SKILL_2D的9步跑。逐项产出,**禁止简化**:

| 步骤 | 产出 | 禁止简化的红线 |
|---|---|---|
| **标题栏8项** | Drawing NO./Part name(中文零件名)/Pro material/Surf dispose/Scale/Tolerance(默认公差表)/Edition/Model NO. | Scale决定尺寸真实值;Part name替代P0X代号 |
| **技术要求逐条** | 全部条目,**第1条必标**(几乎总是"与XX配合无干涉/转动有卡顿"=装配关系最权威证据) | 不只读第1条;"符合3D图纸"标注→必入C级清单 |
| **逐编号尺寸** | 按①②③…顺序,每号5项:编号/视图位置/几何符号/前缀/数值+公差/注释 | 见下方4条铁律 |

**逐编号尺寸的4条铁律(SKILL_2D Step5,违反=误读)**:
1. **几何符号不简化也不臆造**: `Φ/R/SΦ/SR/C/无`如实记。Φ不能丢,但更不能凭空加(见第4节①vsΦ)。
2. **前缀不丢**: `2c-3.9`不能写成`3.9`(2c-=2个c类型特征,影响周向分布理解)。
3. **公差形式不简化**: `⁺⁰·¹⁻⁰`(只能向正)≠`±0.1`(允许向负);`0⁻ᵃ`/`⁺ᵇ⁰`是单边偏移,中值不在标称。无公差项取标题栏默认公差表。
4. **括号注释逐字保留**: `(P07连接筋位)`不能复述成`(P07连接部位)`——"筋位"特指有筋条结构的配合区,改一字即误读。

---

### 4. 2D分支:符号与角度的两个专项确认

**① vs Φ 视觉确认(Step6.6, 每个"看似Φ"项都要做)**:
- 引出线**横向(径向)/圆视图引出**→大概率是Φ;引出线**竖向(轴向)/侧视图**→大概率不是Φ(是编号圆圈①)。
- 与技术要求交叉:弹簧"自由高度45mm"→侧视图标的45必为高度,即使看着像Φ45。
- 任一信号触发→单独裁200×200px局部放大复核。经典翻车:`①45.0`被读成`①Φ45.0`(45是自由高度,无Φ)。

**角度θ:360°/θ只是候选,无3D方位校准则标"待确认"(Step6.2系列,SKILL_2D最大翻车区)**:
- `360 % θ == 0` 只产出"**可能**有n个均布特征"的**候选假设**,绝不是结论。
- 圆视图中心放射出的细实线**不一定是从圆心出发的半径**——可能是某条结构实体边(只存在于某段半径范围)的延伸线,延伸到圆心只是几何巧合。
- 圆周上"短矩形"特征**可能是倾斜凹槽的长边(60°/120°斜向)**,不是径向均布小齿。
- **铁律**: 在没有做3D HLR投影方位校准之前,任何角度的"均布数/位置角/解锁角"含义一律标 **"待确认"**。即便几何含义已定,**运动量(解锁角/行程)也不能从图纸几何直接写**,必须来自技术要求/装配图/工程师(运动量vs几何量,Step6.2-quater)。
- 真要定角度含义,需上3D分支做方位校准:`gp_Ax2(P,N,Vx)`画面y方向=N×Vx(叉积,非Vx本身),需枚举8种(2 view×4 Vx)组合,用≥2个**非对称基准**(模穴号字母/非对称凸台/编号圆圈)对齐(差值≤5°)才能信。这是重活,2D审核阶段一般直接标"待确认"交工程师即可,不强行做。

**可信度三级**(每条结论必标): **A**=直接读出(标题栏/技术要求/数字尺寸+公差); **B**=识图判断(视图类型/字母分组/360°反推); **C**=必查3D或工程师(三维形状/接触模式/运动行程/"符合3D图纸"项)。

---

### 5. 2D分支:回主链对账(图纸 vs DHF其它文档)

读完出尺寸表后,图纸分支汇入主链,做4项跨文档对账:

| 对账项 | 图纸侧 | 对方文档 | 查什么 |
|---|---|---|---|
| **图号 vs BOM** | 标题栏Drawing NO. | BOM/物料清单 | 图号在BOM中存在且唯一;无孤儿图、无BOM缺图 |
| **尺寸 vs 设计输入** | 逐编号关键尺寸+公差 | 设计输入/需求规格 | 关键尺寸覆盖设计输入指标;公差满足要求 |
| **材料 vs BOM** | 标题栏Pro material | BOM材料列 | 材料牌号一致 |
| **版本 vs 清单** | 标题栏Edition | 文档/图纸清单 | 图纸版本=清单登记版本,无旧版残留 |

> 配合关系交叉验证(Step6.5): A声明与B配合,则B也应声明与A配合;配合直径自动算单边间隙`(孔径−轴径)/2`,合理区间约0.025~0.5mm,越界标疑问。

---

### 6. 3D分支(STP):按需启用,默认不上

**何时启用**: 仅当2D已读到极限(DPI升到600/1200、局部裁切仍分不清)、且需要确认三维形状/内部结构/配合接触模式时。这是**重型分支**,默认跳过。

**依赖(重)**: `pip install cadquery`(连带OCP/OpenCASCADE,装包慢、体积大)。**新机器按需才装**,不要默认装进环境。

**方法(读对应skill)**:
- `SKILL_3D_Model_Analysis.md`: cadquery加载STP → bbox(包围盒尺寸)+整体形状+装配空间。
- `SKILL_3D_Section_Analysis.md`: 剖面分析 → 壁厚/内部结构/配合间隙。

**信息边界铁律(必须刻进脑子)**:
- **bbox ≠ 形状**: 包围盒只给最大外廓尺寸,不等于零件实际几何。不能用bbox反推轮廓。
- **不猜功能**: 3D只读几何事实(尺寸/相对位置/剖面)。卡扣触发条件、解锁动作、运动行程等功能性结论,3D**给不了**,只能工程师确认或查专利说明书。
- 3D HLR投影读角度前**必须方位校准**(第4节末已述,8组合枚举+≥2非对称基准),否则整图可能旋转/镜像90°而不自知,所有角度全错。

**三件套协作顺序**: 2D(建A级事实基础) → 3D Model(整体形状/bbox) → 3D Section(配合区剖面)。冲突时**优先2D技术要求与2D标注**(3D模型常有简化)。

---

### 7. 工程铁律:schema字段名必须ASCII

图纸读图产出要结构化(尺寸表/manifest/对账结果),若要走API(如StructuredOutput或任何JSON schema工具)回传:**schema的key(字段名)必须是ASCII英文**。中文key(如`"图号"`、`"公差"`)会被API直接拒绝(InputValidationError)。

做法: schema字段用英文(`drawing_no`/`part_name`/`material`/`edition`/`symbol`/`prefix`/`value`/`tolerance`/`note`/`confidence`),**中文只能放在value里**。`prep_2d.py`写本地CSV时用中文表头无所谓(那是本地文件不过API),但任何经schema/工具调用回传的结构,key一律ASCII。

---

### 8. 新机器落地清单

- [ ] 拷贝3个图纸skill到`<NEW_SKILLS_DIR>/`(SKILL_2D + 2个3D),记下新路径
- [ ] 拷贝`prep_2d.py`,改`SRC`/`OUT`/`WANT`三个占位符为新型号实际值
- [ ] `pip install pymupdf pillow`(2D分支必装);`pip install cadquery`仅3D分支按需
- [ ] 跑`python <NEW>\prep_2d.py` → 得`full.png`+6×`crop`+`_2d_manifest.csv`
- [ ] 视觉agent对每张crop: 先`Read SKILL_2D...md`再`Read crop`,按9步产出(标题栏8项/技术要求逐条/逐编号尺寸/①vsΦ/角度待确认/A·B·C分级)
- [ ] 公差形式·前缀·括号注释·几何符号 四不简化
- [ ] 回主链对账: 图号vsBOM / 尺寸vs设计输入 / 材料vsBOM / 版本vs清单
- [ ] 所有回传schema字段名ASCII,中文只进value

---

## 代码分支（拿到 C 固件源码时单开）

### 0. 什么时候开这条分支
DHF 包里**通常没有源码**——源码在软件团队/MCU 供应商手里，DHF 只放需求(SRS)、软件设计说明、V&V 报告。**只有当你确实拿到 C 固件工程**（一个带 `FWLIB/`、`User/`、`*.uvprojx`/`*.si4project` 的目录树）时，才开这条分支。

**为什么值得开**：固件常量是产品行为的**最终真值**——机器实际执行的就是这些数。文档（检验标准、设计输出、SRS）是人写的、会抄错、会版本漂移。所以本分支的**杀手锏 = 固件常量 ↔ 设计/检验三方对账，代码当真值裁决文档**。当检验标准写"低电压 2.6V"、设计输出写"2.4V"、而固件写 `2.70/2.50` 时，**代码说了算**，文档两边都得改。

> 本章所有数字、路径、宏名取自真实样本 `PT9S` 体温计固件（MCU=杭州士兰微 SD82P253，传感器 TSD14）。**新型号路径/宏名几乎一定不同，下面的路径和常量名都是占位符，必须按实际工程自改。**

---

### 1. 第一步：认正源，排除旧副本（最容易踩的坑）

源码工程里到处是同名 `.h`/`.c`，**只有一份是真的**。判定规则：

| 目录 | 是否正源 | 说明 |
|---|---|---|
| `FWLIB/inc/`、`FWLIB/src/` | ✅ 正源（芯片库 + 全局宏） | 全局 `define.h`、外设驱动在这 |
| `User/`、`HARDWARE/`、`APP/` | ✅ 正源（业务逻辑） | 测温/校准/显示/按键逻辑 |
| `*.si4project/Backup/` | ❌ **旧副本，禁用** | Source Insight 自动备份，文件名带编号如 `define(7999).h`、`define(2988).h`，是历史快照不是当前代码 |
| `*.uvguix.*`、`Objects/`、`Listings/`、`DebugConfig/` | ❌ 编译产物 | 跟对账无关 |
| `.git/`、`~$*`、`*.bak` | ❌ | 同理 |

实测样本：正源只有 1 份 `FWLIB/inc/define.h`，而 `PT9S_SD82P253.si4project/Backup/` 下有 **30+ 个** `define(NNNN).h`。**用编号副本对账 = 拿历史数据裁决，结论作废。**

```bash
# 占位符：把 <CODE_ROOT> 换成你的固件工程根目录
CODE_ROOT="D:/AI_0415/03DHF/<型号>/<...>_SRC_..._Vx.x.x/<...>_SRC_..._Vx.x.x"

# 1) 找全局 define.h，先确认哪份是正源（应在 FWLIB/inc 或 User 下，不带括号编号）
find "$CODE_ROOT" -iname "define.h" | grep -vi "Backup"

# 2) 一眼区分正源 vs 副本：副本路径含 ".si4project/Backup" 且文件名带 (数字)
```

---

### 2. 第二步：grep 固件关键常量 + 身份（对账素材清单）

正源定位后，**只 grep 正源目录**（`FWLIB/inc`、`User`），抓两类东西：**身份**（这份代码是谁）+ **行为常量**（机器实际阈值）。

#### 2a. 身份信息（确认对的型号/版本，防止拿错工程对账）
| 抓什么 | 在哪/怎么找 | PT9S 实测值 | 对账谁 |
|---|---|---|---|
| MCU 型号 | `#include "SD82P253.h"`、库前缀 `SD82P253_*` | 士兰微 **SD82P253** | BOM / 原理图 / 设计输出 |
| 传感器型号 | 目录名/`sensor.h`/注释 | **TSD14** | BOM / SRS |
| 固件版本号 | `VER_NUM` / `VER_DATE` 等宏 | `VER_NUM 102`(=V1.0.2)、`VER_DATE 260430` | 软件版本记录 / 标签页 / DHF 版本 |

#### 2b. 行为常量（裁决文档的真值，逐条对账）
| 类别 | 宏名（占位，按实际改） | PT9S 实测 | 含义/换算 | 对账目标 |
|---|---|---|---|---|
| 低电压一级 | `VBAT_1ST_LINE` | `270` | 2.70 V（低电量提示） | 检验标准/设计输出"低压报警值" |
| 低电压二级 | `VBAT_2ND_LINE` | `250` | 2.50 V（关机/禁测） | 检验标准"欠压关机值" |
| 电压恢复 | `VBAT_RST_LINE` | `300` | 3.00 V（解除低压） | 设计输出"恢复阈值" |
| 量程上限 | `TAMB_HI_LINE` | `4100` | 环温/测量上限阈值 | SRS 量程 / 检验标准 |
| 量程下限 | `TAMB_LO_LINE` | `500` | 环温/测量下限阈值 | SRS 量程 / 检验标准 |
| ℃/℉ 默认 | `UNIT_F_VERSION`/`UNIT_C_VERSION` | F=1, C=0 | 出厂单位版本开关 | SRS"默认温标"/包装/说明书 |

> 通用还要 grep（不同产品名不同）：**自动关机时间**(`*AUTO_OFF*`/`*POWEROFF*`/`*SHUTDOWN*`)、**标定/校准表**(`*CALI*`/`*ADJUST*`/查找表数组)、**测量上下限/超温报警**(`*HI*`/`*LO*`/`*LIMIT*`/`*OVER*`)、**默认温标/单位**(`*UNIT*`/`*FAHREN*`/`*CELSIUS*`)、**电池/电压**(`*VBAT*`/`*BATT*`/`*VOLT*`)、**版本**(`*VER*`/`*VERSION*`/`*FW*`)。

```bash
# 只搜正源，排除 Backup/编译产物。-rn 给行号便于回溯到具体宏
INC="$CODE_ROOT/FWLIB/inc"; USR="$CODE_ROOT/User"

# 身份
grep -rn -iE "VER_NUM|VER_DATE|VERSION" "$INC" "$USR"
grep -rn -iE "#include .*(SD82|STM32|HC32|N32|MM32|nRF|ESP)" "$INC" "$USR"   # MCU 系列名按实际换

# 行为常量（阈值/量程/单位/电压/关机/标定）
grep -rn -iE "VBAT|BATT|VOLT|LOWBAT" "$INC" "$USR"
grep -rn -iE "AUTO.?OFF|POWER.?OFF|SHUTDOWN|SLEEP.*TIME" "$INC" "$USR"
grep -rn -iE "HI_LINE|LO_LINE|LIMIT|RANGE|OVER|UNDER" "$INC" "$USR"
grep -rn -iE "UNIT|FAHREN|CELSIUS|_F_|_C_" "$INC" "$USR"
grep -rn -iE "CALI|CALIB|ADJUST|OFFSET|COMPENSAT" "$INC" "$USR"
```

> 注意单位/定点：固件常量几乎都是**定点整数**，需按代码里的标度换算（如电压 `270`→ ÷100 = 2.70 V；温度常量可能是 ADC 码、0.1℃ 或 0.01℃，**必须读取注释/换算函数确认标度**，别想当然 ÷100）。换算依据写进对账记录。

---

### 3. 第三步：三方对账（代码裁决文档）

把抓到的每个常量与文档逐条对，结论列**代码值为准**：

| 项 | 固件(正源, 真值) | 检验标准写 | 设计输出/SRS 写 | 裁决 | 动作 |
|---|---|---|---|---|---|
| 低压一级 | 2.70 V (`VBAT_1ST_LINE=270`) | 2.6 V | 2.6 V | **2.70** | 检验+设计均改 2.70，或确认是否代码需改 |
| 低压二级 | 2.50 V (`VBAT_2ND_LINE=250`) | 2.4 V | — | **2.50** | 同上 |
| 默认温标 | F (`UNIT_F_VERSION=1`) | — | 说明书写默认℃ | **F** | 核实出厂烧录版本，文档对齐 |
| 固件版本 | V1.0.2 (`VER_NUM=102`) | 标签 V1.0.1 | DHF V1.0 | **V1.0.2** | 版本记录补齐 |

**裁决方向不是绝对"代码永远对"**：代码是"机器实际行为"的真值。若文档是**法规/安规约束的设计意图**（如标准要求欠压必须 2.5V 关机）而代码写错，则反过来——**判定为固件缺陷，开 CAPA/软件变更**。所以每条对账要标注：①代码值 ②文档值 ③哪个是"应然"（看法规/风险/设计意图）④结论是改文档还是改代码。

---

### 4. 产出（接到错误总表）
对账结果并入主审核错误总表，每条至少含：
`项目 | 固件正源值(文件:行) | 文档值(文件:位置) | 差异 | 裁决依据 | 结论(改文档/改代码/CAPA)`

固件侧引用务必写**正源相对路径 + 行号**（如 `FWLIB/inc/define.h:84 VBAT_1ST_LINE=270`），**严禁引用 `*.si4project/Backup/define(NNNN).h`** —— 这是审核作废的红线。

---

### 5. 速查 checklist（新机器照做）
- [ ] 确认拿到的是 **C 固件源码工程**（有 `FWLIB`/`User`/`*.uvprojx` 或 `*.si4project`），否则不开本分支
- [ ] `find -iname define.h | grep -vi Backup` 定位正源；**排除 `*.si4project/Backup/` 全部编号副本**
- [ ] grep 身份：MCU(`#include`/库前缀)、传感器、`VER_*`
- [ ] grep 行为常量：电压(`VBAT*`)、关机(`AUTO_OFF*`)、量程(`*_LINE`/`LIMIT`)、单位(`UNIT*`)、标定(`CALI*`)
- [ ] 每个常量确认**标度/单位换算**（读注释与换算函数，勿臆测 ÷100）
- [ ] 三方对账：固件 ↔ 检验标准 ↔ 设计/SRS，标注裁决方向（改文档 or 判固件缺陷）
- [ ] 结论入错误总表，固件引用带**正源路径:行号**


---

## 第N章 实证基准与踩坑

> 本章给"另一台机器"两样东西:一是**跑完一个新型号后,你的产出应该长什么样**(实证基准,用于自检"我是不是漏了一大半");二是**前人踩过的坑**(务必避开,否则会卡在 API 报错、读不出文件、或把对的值当错报)。所有数字均来自已归档的两份真实错误总表,非估计。

---

### 1. 实证基准(跑完后拿你的产出对标)

两份**真实**错误总表(已逐行核过行数与严重度):

| 文件(绝对路径) | 数据行 | 阶段轴 | 维度轴(净新增) |
|---|---|---|---|
| `D:\AI_0415\03DHF\PT9L_CHECK\PT9L-全链审核-错误总表-含维度轴.csv` | **103** | 72 | **31** |
| `D:\AI_0415\03DHF\PT9S_CHECK\PT9S-全链审核-错误总表-含维度轴.csv` | **169** | 146(含跨阶段22) | **23** |

> 路径提示:新机器如不在 `D:\AI_0415` 下,把 `D:\AI_0415\03DHF\<型号>_CHECK\` 改成你的实际审核目录。

**基准口径(写汇报时按这个说,别说错)**

- PT9L:阶段轴基线 **73** 项 → 叠加维度轴后 **104**(维度轴 **+31**)。
- PT9S:阶段轴基线 **146** → 叠加维度轴后 **169**(维度轴 **+23**)。
- 合计 **维度轴 +54** 项为"**确认净新增**"——即过了**去重**(与已有阶段轴条目不重复)+**对抗证伪**(有 A/B 双侧正文证据、非误报)后的结果。维度轴是在阶段轴跑完之后,沿 BOM对账 / 下游⊆上游 / 可追溯断链 / 数值一致 / 版本漂移 / 矛盾措辞 / 角色串联 等"横切维度"二次扫出来的,**不是**重数一遍阶段轴。

> 注:CSV 是多行字段(证据列会换行),**不能用 `wc -l` 数行数**——必须按"行首是 `序号,`"的模式计数(见踩坑 §2.8)。PT9L 文件 135 物理行≠103 数据行;PT9S 193 物理行≠169 数据行。

**严重度分布(逐行核实,供你判断自己的产出比例是否离谱)**

| 型号 | critical | major | minor |
|---|---|---|---|
| PT9L | 2 | ~64(含1条"待PM判断") | 37 |
| PT9S | 12 | 71 | 49(余数为责任列错位,非真 critical) |

经验:**critical 极少(个位数),major 是主体,minor 占 1/4~1/3**。如果你跑出来 critical 占一大半,基本是把"值本身存疑(待工程师拍)"误升级成了 critical(见踩坑 §2.5)。PT9S 的 critical 比 PT9L 多,是因为它**模板残留更重**(整篇 PT9L/血压计文件复制未改、DMR 文件夹空),这类身份污染与设计转换缺失天然判 critical。

**典型错误模式(7 类,新型号大概率复现,逐类去主动找)**

| # | 模式 | 抓法 / 信号 | 实证锚点 |
|---|---|---|---|
| 1 | **参数全链放宽**(下游≥上游被违反) | 同一参数沿"设计输入→验证→设计输出→DMR/产线"越往下限值越松;实测超标却判合格 | PT9L 工作电流 DHF≤20mA vs 工序大纲1~50mA;静态电流 0.02mA vs 产线0.20mA(10倍)。PT9S 工作电流06评估10mA→实测12.7/11.5mA仍判合格→09回写≤10mA |
| 2 | **模板残留(多型号串用)** | grep 别型号名/旧项目号/血压计要素(cuff/袖带/Sphygmomanometer/腕枕/气囊) | PT9L 夹 AG-633耳机/BG5S/FDIR-V14/PT3 整页;PT9S 整篇文件型号写 PT9S9L、项目号3000009478、可追溯报告整篇是PT9L、usability file 整份是PT9L且写"EU上市" |
| 3 | **标签法规/UDI 缺失** | grep `880.2910` / `807` / `801` / `UDI` / `830` 全链命中数;EN协调版被当美国基准 | 两型号 880.2910(Class II分类)+807 Subpart E(510k)全链缺;UDI 801.20/.30/.35与日期格式空白;标签用 EN ISO 80601-2-56 作美国判定(应为FDA认可ISO版) |
| 4 | **市场口径矛盾** | "仅美国"决策 vs 文件里出现 CE/EU/中美欧并列 | PT9S 开发计划写"评估CE申请阶段";铭牌印CE标志;风险计划并列 EN ISO 14971/A11(欧盟MDR用) |
| 5 | **编号唯一性破坏** | 同一图号一号两用;同一物料两个料号;项目号/版本多套 | PT9L PT9L-F01外观图+外箱共号;MCU两处料号不同。PT9S 项目号出现30000094/30000078/2025-PT9S-01/2020-DEV01 四套 |
| 6 | **验证不足 / 降频无据** | 实测样本不足判合格;残余风险 P 直降无理由;声明项只验"存在"未验"准确" | PT9L 整机寿命仅1台(要5台)判合格;物温模式只验"可切换"未验精度。PT9S 多条 P4→P1 仅填报告名无降频依据 |
| 7 | **DMR空 = 设计转换未完成** | DMR/工序转化文件夹为空或只有占位登记 | PT9S 13/16 DMR转化两文件夹**完全为空**,工序大纲/WI/PFMEA/检验QI未产出,登记在册(柯顿)但实体不存在——直接 critical |

---

### 2. 踩坑清单(逐条务必避开,否则会卡死或误判)

#### 2.1 workflow 结构化 schema 字段名必须 ASCII
若你用 workflow / 结构化输出(JSON schema)驱动审核,**schema 的 key 一律用英文**。中文 key(如 `"严重度"`)→ 接口直接 **API 400**。中文只能放在 value 里。报错时先查是不是 key 带了非 ASCII。

#### 2.2 edoc2 网盘读不了老 `.doc`/`.xls` → 必须本地转
九安网盘(edoc2)MCP **读不了老二进制 `.doc`/`.xls`**(老 OLE 格式)。流程:先把文件落到本地,转成 `.docx`/`.xlsx` 或 `.md`,再喂给审核。另外 edoc2 大文件(**≥18MB 必断连**),下大文件要分块或换通道。**不要**反复重试同一个老 `.doc`——它不会突然成功。

#### 2.3 Word COM 需 Windows + Office
用 COM 自动化抽 Word/Excel 正文(`win32com` / PowerShell `New-Object -ComObject Word.Application`)**只能在装了 Office 的 Windows 上跑**。Linux/无 Office 机器会直接失败。如果新机器没 Office,改用 `python-docx`/`openpyxl`/`pandoc` 这类纯库,或先在有 Office 的机器把源文档转成 `.md` 资产再传过去(本项目的 `*_MD` 目录就是这么来的)。

#### 2.4 对抗证伪会毙约 1/4 候选——这是诚实,不是损失
LLM 初筛会给出一批"疑似错误"候选。**必须**对每条做对抗证伪:回原文找 A 侧+B 侧双向正文证据,找不到对立证据的就毙掉。经验上**约 1/4 候选会被毙**(写法差异/单位差异剔除后其实不冲突、或本就一致)。**别为了凑数留下证伪不过的条目**——总表的 +54 是"证伪后"的净数,可信度正来自这一步。被毙不是产能损失,是质量保证。

#### 2.5 一致性 ≠ 正确性:值本身对不对,要工程师拍
审核机器能判的是"**跨文件是否一致**",**判不了"这个值本身工程上对不对**"。传感器线数(3根 vs 4根)、静音/低电压开关阈值、电流真值、盐雾时长 24h vs 48h 这类——**真值由 PM/工程师拍板**。这些应标"**待工程师确认/真值待 PM 拍**"(PT9S 总表里专门有"待PM确认"列),**不要当成已坐实的错报去判 critical**。把"PM 已纠过、确认维持"的项当错报报出去,是典型误报(如 PT9L 误诊S3、传感器线数)。

#### 2.6 确定性层 高精度低召回,LLM 层兜召回
两层架构:
- **确定性层**(脚本/正则/grep,如 `check_residue.py`):只看得见"参数长表里结构化、可正则的项",**精度高但召回低**——表外的、措辞型的、跨文件语义型的它抓不到。
- **LLM 层**:负责兜住确定性层漏掉的(语义矛盾、模板残留语气、角色串联、"声明已验但其实没验")。
**两层都要跑,顺序是先确定性后 LLM**。只跑确定性层会漏掉大半 major;只跑 LLM 会漏掉精确参数比对。维度轴 +54 里很大一部分正是 LLM 层兜回来的。

#### 2.7 NEI:无正文证据 → 判"证据不足",不硬判通过
**No-Evidence-Implies(NEI)原则**:某条款/某验证项在 DHF 里**找不到正文证据**时,判**"证据不足/无法核验"**,**绝不**因为"没看到反例"就默认判通过。空白字段 ≠ 已闭环(PT9S 试产总结四组问题全空、判据全空,就是把空模板当已关闭)。"网表与原理图一致 ■通过"但原理图正本根本不在图纸夹里——结论无可核验对象,应判证据不足而非通过。

#### 2.8 CSV 多行字段:别用 `wc -l` 数结论数
证据列含换行,物理行数 ≠ 错误条数。**按行首 `^[0-9]+,` 模式计数**才是真条数(也别用 awk 取末列做统计——换行会把证据正文当成"来源"列污染结果)。严重度/轴这类统计取**字段4/字段5**(在每条记录首行),可靠。

---

### 3. 自检清单(交付前对自己跑一遍)

- [ ] 阶段轴跑完后,**单独**再跑维度轴(BOM对账/下游⊆上游/可追溯断链/数值一致/版本漂移/矛盾措辞/角色串联),不是重数阶段轴。
- [ ] 维度轴每条都过了**去重 + 对抗证伪**(有 A/B 双侧正文证据)。预期约 1/4 候选被毙属正常。
- [ ] 7 类典型模式逐类主动搜过(尤其:grep 别型号名/项目号查模板残留;grep `880.2910|807|801|UDI` 查法规缺项;沿全链比对关键参数查放宽)。
- [ ] critical 是个位数、major 为主体、minor 约 1/4~1/3——比例离谱说明把"待拍真值"误升级了。
- [ ] "值本身存疑"的条目标了"待工程师/PM确认",没当坐实错报。
- [ ] 找不到正文证据的判"证据不足",没硬判通过。
- [ ] 结论数用行首模式计数,不是 `wc -l`。


---

## 【新型号执行清单】给另一台机器的执行 SOP

> 读者：另一台机器上的 Claude Code（无本对话上下文）。本章按 0→7 顺序可独立跑一个新型号。**所有路径都是占位符，新机器盘符/目录大概率不同，按本机实际改**。源机器工作根是 `D:\AI_0415\03DHF`（下文记作 `<BASE>`）。

---

### 0. 前提（开跑前一次性确认）

| 项 | 要求 | 怎么验 |
|---|---|---|
| OS | Windows（`.doc/.xls` 转换依赖 Word COM，只在 Windows+本机 Office 上能跑；网盘 MCP 对老格式全打不开，本地工具完胜） | `winver` |
| Office | 已装 Word（COM 自动化，转 `.doc/.docx`） | 能打开 Word |
| Python 包 | `xlrd`(.xls) `openpyxl`(.xlsx) `pymupdf`/`fitz`(.pdf 渲染) `Pillow` `pywin32`(Word COM) | `python -c "import xlrd,openpyxl,fitz,PIL,win32com.client"` 无报错 |
| 拷到本机的资产 | ① `dhf_audit_toolkit/`（4 个 check 脚本 + `dhf_pipeline.py` + README） ② 3 个图纸 skill（PDF 渲染/视觉读图/对账，对应 `skill/pdf-skill` 及转换 skill 里渲 PNG 的部分） ③ V2 方法论 `DHF-DMR审核方法论-V2-双轴实战版.md` ④ 详细版 `PT9L-DHF审核方法论-详细版-全阶段.md`（逐阶段 CHK 清单） | 文件都在 `<BASE>` 下 |
| **根决策（最重要，开跑前必须拿用户拍板）** | **市场 + 品类 → 强制法规集合**。例：PT9L/PT9S=红外体温计/**仅美国**→510(k) 或 880.2910 SDV 豁免 + 807 + UDI；EU EN / 中国 GB **非强制**（裁剪要写 N/A 理由，**反向引用 EN/GB 作美国判定 = 真错误**）。基线**只用用户自己的合规模板/法规 pageindex，不联网另建、不质疑其合规性**；联网仅用于补用户本地缺失的 CFR 正文。 | 用户口头/书面确认市场=? 品类=? 注册路径=? |

**两条预置铁律**（贯穿全程）：①签名/日期/审批勾选不查（老板签字时才勾，电子版不审）；②**一致性 ≠ 正确性**——脚本和 AI 只判"对不对得上 / 全不全"，**值本身对不对（传感器几根线、静音是按钮还是开关）必须工程师拍**，AI 只把可疑值标出。

**加新型号的唯一配置点**：编辑 `dhf_audit_toolkit/dhf_pipeline.py` 顶部，把 `BASE` 改成本机根，并在 `MODELS={}` 里复制一段（照 `PT9S` 那段）改 `raw/md/check/dhf_list_glob/market/category/foreign/models/params`。之后所有命令用 `python dhf_pipeline.py <型号> <phase>` 一条龙跑。

---

### 1. 转换（原始件 → Markdown + 页面 PNG）

AI 和脚本都读不了原始 `.doc/.xls/.pdf`。先转。

```bash
cd <BASE>\dhf_audit_toolkit
python dhf_pipeline.py <型号> convert
# 等价于：递归扫 raw 下所有 .doc/.docx/.xls/.xlsx/.pdf → <型号>_MD\，
# 每个 MD 带 YAML 头(source/status/loss_flags)，PDF 少字页(<40字)自动渲 PNG(dpi=150)到 .assets\
```

- 产物：`<型号>_MD\` + `_manifest_conversion.csv`（转换台账：status=ok/empty/failed、loss_flags）。
- **关键坑**：勾选框 ■/□ 是转换最易错处。`loss_flags` 里有 `checkbox=N(checked=M)`，但**凡涉及勾选/图的判定必须看 `.assets\page_*.png` 原件页面，不能只信文本 MD**。
- 目标：`status` 全 ok / 已知 empty。失败项逐个看 `error` 列补。源机 PT9S 实测 200/200 成功 0 失败。

---

### 2. 覆盖台账（清单 vs 实物 vs 转换，保证"0% 悄悄漏掉"）

```bash
python dhf_pipeline.py <型号> coverage
# 读 raw 下 *DHF清单*.xls(dhf_list_glob)，模糊匹配清单每项↔实际文件↔已转MD
```

- 产物：`<型号>_CHECK\coverage_ledger.csv`，每项标 `ok / review / missing / paper(纸档)` + 匹配分。
- 看法：`missing`=分母里有、实物/转换找不到（**真缺口，可能 critical，如 PT9S 的 DMR 文件夹整片空=设计转换未完成**）；`review`/低分多为中文清单名 vs 英文/编号文件名的匹配噪声，人工扫一眼即可。**缺口本身是发现，不是"没查到"**。

---

### 3. 机械层（纯 Python，确定性，近零误报；先跑掉低级高频问题）

| 步 | 命令 | 抓什么 |
|---|---|---|
| 3a 残留扫描 | `python dhf_pipeline.py <型号> residue` | 异类**品类**残留(血压计/袖带/耳机…→基本都是错)、异类**型号**残留(区分复用件 vs 残留)、占位符(XXXX/待填/＿＿) |
| 3b 数值一致 | `python dhf_pipeline.py <型号> mechanical`（读 AI 产出的参数明细，见 §4） | 单位归一(℃/℉、A/mA/µA、mm、s)+区间/容差/边界，点落区间判一致，剔写法误报；**只报归一后仍冲突的** |
| 3c 表 diff（可选） | `python check_table_diff.py A.xls B.xls --key 物料编码 --labelA T1 --labelB 设计输出 --out diff.csv` | 同构表(BOM/清单/版本前后)行级 key-join：仅A/仅B/值不同 |
| 3d 跨异构表对账（可选） | 先把 BOM/清单(确定性)+WI(LLM 抽)汇成统一记录表(列=`来源,品名,用量,规格,图号,物料编码`)，再 `python check_bom_crosswalk.py 记录表.csv --out 对账.csv` | 用量/规格/图号冲突(如 螺钉 ABOM=10 vs WI=9) |

3a 单独跑法（如不走 pipeline）：
```bash
python check_residue.py "<型号>_MD" --product <型号> --foreign 血压计,袖带,耳机,雾化器,冲牙器 --models PT3,PT5,PT7,PT9C,AG-633,FDIR --allow-reuse <确认的复用型号> --out 机械校验-残留.csv
```
> 边界：3c 仅同构表；3d 跨异构表**非近零误报**（范围差异降级为信息项、LLM 抽取有瑕疵），属"低置信进人审"候选生成器，非自动放行。数值的精度/分辨率（带温度段+重复性歧义）不做确定性比对，交 §4 LLM。

---

### 4. 语义层 workflow（双轴；本章核心，先阶段轴后维度轴）

> 用 Claude Code 跑。给 Claude 的基线：根决策(§0) + 用户法规 pageindex/合规模板 + 已拍板事实（市场、注册路径、签名日期不查）+ 详细版逐阶段 CHK 清单。

**阶段轴（13 单元并行）**——按文件夹 01→DMR 各派一个 agent，查阶段内**完备性 + 4 子轴**（①纵向下游≥上游 ②横向参数槽位 ③角色串联 ④反向完备性）。13 单元 = 01 立项 / 02 开发计划 / 03 风险 / 04 设计输入 / 05 结构 / 06 硬件 / 07 软件 / 08 T1 样机 / 09 设计输出 / 10 试产 / 11 设计确认 / DMR(03_Mfg_SOP) / **跨阶段串联**（限额挂了就用单 agent 补跑）。每阶段查什么参数/谁主责见详细版表（如 04 抽量程/精度/环境/电池/法规清单查不收窄；06 抽 MCU/传感器/电池/电流；DMR 逐参数 DMR↔DHF 不放宽 + 模板残留）。

> **提取层是地基中的地基**：阶段轴产出**参数实例长表**（行=参数实例，列=参数名/值/单位/上下限/出处文件/版本/阶段），存 `<型号>_CHECK\<型号>-参数明细.csv`——§3b 数值检查、维度轴的数值/不收窄/BOM 全站在这张表上，**抽错=满盘错**。

**维度轴（7 维度横扫全库，正交，V2 新增——补阶段轴对"接口"的盲区）**——按检查类型各派一个 agent 扫整库：

| 维度 | 查什么 |
|---|---|
| 可追溯断链 | 需求→输入→输出→验证→确认 逐参数断链；每个风险控制有无验证；DHF 清单每项是否落地 |
| BOM 对账 | EBOM/ABOM/包装BOM/组件清单/WI物料/工序大纲/PFMEA 跨表配平 |
| 角色串联 | 同一工程师名下文件参数自洽；评审独立性(一人多职=审核批准塌缩) |
| 矛盾措辞 | 需临床 vs 免临床 / 版本日期打架 / 同参数互斥值 / 单文件内部判据矛盾 |
| 版本漂移 | 同号多版本 / 整树副本 / 多版并存未作废 / 版本方向倒置 |
| 不收窄 | 下游区间 ⊆ 上游（量程/人群/环境/精度），containment 双向判 |
| 数值一致 | 同一参数多处取值，区间+单位归一比对（与 §3b 互为人/机两路） |

**去重 + 对抗证伪（信条，不可省）**：维度轴候选先 **dedup vs 阶段轴已有**，再**逐条派"挑刺"agent 回正文试图反驳**——证据不实/其实一致/写法误报就毙掉。源机实测证伪毙掉约 1/4 候选（PT9S 33→23、PT9L 37→31）。**留下的每条都回过正文**。

**NEI 纪律**：找不到正文逐字证据 → 判"证据不足(NEI)"，**绝不默认通过、绝不编**。判定必须给**双向原文引用**（A 文件值 vs B 文件值 + 具体冲突值），不能只说"对不上"。

---

### 5. 图纸分支（PDF 图纸/丝印/铭牌：渲染分块 → 视觉读 → 对账）

图纸里的尺寸/图号/极性/盐雾时长等只在标题栏和图面里，文本抽不到。用 3 个图纸 skill：

1. **渲染分块**：PDF 图纸页渲成 PNG（转换器对少字页已自动渲 dpi=150；大图/小字处用图纸 skill 提高 dpi 并按区域分块，避免一张图塞太多看不清）。
2. **视觉读**：Claude 直接看 PNG，读标题栏（图号/版本/材质/表面处理）、关键尺寸、极性标注、丝印文案。
3. **对账**：图面值 ↔ BOM/清单/ABOM/WI ↔ 上游设计输出 逐项核。源机典型真错：正/负极弹簧**图号与极性颠倒**（清单/ABOM 写正极=PT5-M03，实物图正极=PT5-M02）；弹簧**盐雾 24h(图纸) vs 48h(ABOM/T1)**；丝印/标签 UDI/日期缺失。结果并入维度轴的 BOM 对账/版本漂移/角色串联。

---

### 6. 代码分支（仅当该型号有源码，如 M10 这类含固件的）

若拿到固件/源码：抽**固件里的常量/阈值/版本宏**（如工作电流上限、低压阈值、安全等级、版本号），与**规格书/设计输入/软件需求**比对。判定挂"下游≥上游 + 数值一致"——固件实现值不得**收窄**规格、版本号须与 07 软件阶段声明自洽（源机 PT9L 软件版本 V0009/V0029/V00029 互不一致=疑似错误）。无源码则跳过本步。

---

### 7. 汇总（错误总表 + 按工程师 + HTML 检测报告）

```bash
# 汇总(把阶段轴+维度轴净新增合并去重) → 错误总表/参数明细/按工程师
python dhf_pipeline.py <型号> mechanical   # 先补跑确定性数值检查并回灌
# 然后用 Claude/finalize 脚本产出三件套(参照 PT9S 的 assemble/finalize 脚本，改路径)
```

产物放 `<型号>_CHECK\`：
- `<型号>-全链审核-错误总表.csv`：每条含 严重度(critical/major/minor/待PM) + 双向证据 + 改法建议 + **责任工程师** + 系统性归类。
- `<型号>-最终错误总表-按工程师.md`：按 7 角色（硬件/结构/软件/法规认证/包装/品质/工艺）派工。
- `<型号>-审核报告-带截图.html`：给工程师，按文件夹组织，每条带出处文件+证据+改法。
- `<型号>-新增问题-维度轴.csv`：维度轴 delta 明细。

> 角色定位：审核**只列错误清单，不改源文件**（如软件版本冲突、市场口径错——都只标"这里错了"，不动原件）。

---

### 自检清单（交付前逐条过，每条都要能答"是"）

- [ ] **每条结论都回正文了吗？**（标题/文件名/清单一行/空勾选都不算证据；拿不到 → NEI，不许判通过）
- [ ] **双向引用了吗？**（给出 A 文件原文值 vs B 文件原文值 + 具体冲突值，不止"对不上"）
- [ ] **去重了吗？**（维度轴候选 vs 阶段轴已有，无重复计数）
- [ ] **NEI 标了吗？**（抽不到证据如实标"证据不足"，没有假装通过、没有编造数字/总数）
- [ ] **可信度分级了吗？**（critical/major/minor/待PM；机械层近零误报 vs Tier2 跨表/LLM 抽取为低置信进人审，已分开标）
- [ ] **对抗证伪跑了吗？**（每条派挑刺 agent 回正文反驳过；预期毙掉约 1/4 候选——毙不掉说明证伪没做严）
- [ ] **市场口径对了吗？**（按根决策；EU/中国标准非强制的裁剪写了 N/A 理由；没有把 EN/GB 反向当本市场判据）
- [ ] **一致性 vs 正确性分清了吗？**（"值本身对不对"的项已标"待工程师拍"，没替工程师下结论）
- [ ] **双轴都跑了吗？**（阶段轴 13 单元 + 维度轴 7 维度都覆盖；缺一漏一半）

---

**相关文件（源机绝对路径，新机按 `<BASE>` 自改）**
- 工具包：`D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\`（`dhf_pipeline.py` 编排 + `check_residue.py` / `check_params_numeric.py` / `check_table_diff.py` / `check_bom_crosswalk.py` / `README.md`）
- V2 方法论：`D:\AI_0415\03DHF\DHF-DMR审核方法论-V2-双轴实战版.md`
- 详细版逐阶段 CHK：`D:\AI_0415\03DHF\PT9L_CHECK\PT9L-DHF审核方法论-详细版-全阶段.md`
- 汇报版(阶段×参数×主责 总表)：`D:\AI_0415\03DHF\PT9L_CHECK\PT9L-DHF审核方法论-汇报版.md`
- 样板产物(照抄结构)：`PT9S_CHECK\` 与 `PT9L_CHECK\`（错误总表/参数明细/按工程师/维度轴 delta/HTML 报告）
