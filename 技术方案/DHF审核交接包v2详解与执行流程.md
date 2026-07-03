# DHF审核交接包 v2 详解与执行流程

> 适用对象：需要接手、复用或评审 `D:\项目文档一致性审查\侯老师文档\DHF审核交接包v2` 的同事。  
> 目标：让读者不依赖原始对话，也能理解这套交接包的设计思想、目录资产、执行流程、工具脚本、产物要求和常见踩坑。

---

## 1. 一句话理解这套交接包

这是一套面向医疗器械 DHF / DMR / 注册资料的跨文档一致性审查方法包。它不是单个脚本，也不是只让 AI “通读文档后给意见”，而是把审查拆成：

```text
文档可靠转换
-> 市场/品类/法规基线确认
-> 覆盖台账
-> SSOT 参数长表
-> 阶段轴语义审查
-> 维度轴横向审查
-> Tier1/Tier2 确定性脚本复核
-> 对抗证伪
-> 证据核验
-> 裁决报告与完成自检
```

它的核心追求是三件事：

1. **查得全**：不能因为文件没转出来、表格没读到、扫描页没 OCR，就假装没问题。
2. **查得准**：候选问题要经过确定性工具、对抗证伪和证据核验过滤。
3. **能自证**：每条结论都要能追溯到原文证据；每个必查步骤要么执行，要么明确说明为什么不适用。

---

## 2. 交接包的总体定位

该包面向的是医疗器械项目文档审查，尤其是 DHF、DMR、注册资料之间的一致性问题。

它主要检查：

- 上游客户需求、设计输入、风险控制、设计输出、验证确认之间是否闭环。
- 同一参数在不同文档中的值、单位、工况、上下限是否冲突或退化。
- 法规/标准基线是否与目标市场和产品品类匹配。
- BOM、设计输出、作业指导书、检验规程、DMR 是否对得上。
- 模板残留、旧型号残留、异类品类残留、占位符是否未清。
- 文档、表格、扫描页、图纸、代码等证据是否被可靠读取。
- 审查报告里的每条 finding 是否有真实原文证据。

它不直接判断：

- 某个工程参数“本身是否设计合理”。  
  例如一个电流阈值是否工程上正确，要由工程师/PM 拍板；系统只判断文档之间是否一致、是否完整、是否有证据。

---

## 3. 最重要的三条铁律

### 3.1 先核市场和品类，禁止默认

每个型号必须从它自己的客户需求书、立项资料或注册需求中确认：

- 目标市场：中国 NMPA / 美国 FDA / 欧盟等。
- 产品品类：体温计、雾化器、血压计、冲牙器等。
- 注册路径和适用法规。

不能因为之前审过某个型号，就默认新型号的市场、品类、法规相同。

典型风险：

- 用美国体温计法规审中国雾化器。
- 用 FDA / 510(k) 逻辑审仅中国注册项目。
- 把欧盟 EN 标准当成中国强制基准。

### 3.2 不许跳步，结尾必须交《完成自检表》

每个必查动作要么执行，要么明确写：

```text
⏭️ 不适用，理由：……
```

不能默默省略。交接包里反复强调最容易漏掉的是：

- 机械层脚本：残留、数值一致、表 diff、BOM 对账。
- Excel 双通道转换。
- 转换后乱码扫描。
- 对抗证伪。
- 证据核验。
- 图纸/代码分支。

### 3.3 以 `skill/` 和 `tools/` 为执行权威

转换、检查、审查、验证都优先按包内 skill 和工具来：

- 转换：`skill/conversion-toolkit-skill` + 各格式 skill。
- Excel：必须按 `xls-skill` 转两套，结构通道 + 页面视觉通道。
- 逐阶段审查：`stage-01` 到 `stage-11`。
- DMR/SOP：`dmr-mfg-sop-check-skill`。
- 中文安全写入：`tools/unicode_safe_write.py`。
- 乱码扫描：`tools/scan_text_integrity.py`。

---

## 4. 交接包目录总览

交接包根目录：

```text
D:\项目文档一致性审查\侯老师文档\DHF审核交接包v2
```

主要内容如下：

| 路径 | 作用 |
|---|---|
| `00_START_HERE.md` | 入口说明。告诉接手者先读什么、怎么启动、有哪些铁律。 |
| `DHF-DMR审核-SKILL.md` | 总纲。规定完整审核流程、必跑步骤、完成自检表和执行约束。 |
| `run_full_audit.js` | Claude Code workflow 主控脚本。用于代码强制全流程跑完，防止 agent 自觉漏步。 |
| `_MANIFEST.txt` | 包内文件清单。 |
| `_adjudications.csv` | 裁决库。记录已被人工否掉或裁决过的误报，防止重复上报。 |
| `品类参数槽位参考表.md` | 各品类应抽取的参数槽位，以及串品类残留识别词表。 |
| `docs/` | 方法论文档，包括详尽算法版、完整交接版、双轴实战版。 |
| `skill/` | 执行 skill 库，包含转换、阶段审查、维度轴、机械层、自验证、图纸、代码等。 |
| `tools/` | 通用安全工具，主要用于中文安全写入和乱码扫描。 |
| `dhf_audit_toolkit/` | 确定性机械层工具包，包含残留、数值、表 diff、BOM 对账等脚本。 |
| `scripts/` | 转换、覆盖台账、汇总、证据核验、自检、报告生成等流程脚本。 |
| `参考基线/` | 法规基线示例：美国体温计、中国雾化器。 |

---

## 5. 包内核心文档说明

### 5.1 `00_START_HERE.md`

这是接手者的入口文档。它说明：

- 本包目标：独立审一个新型号，产出错误总表和可交互裁决报告。
- 第一步应该读 `DHF-DMR审核-SKILL.md`。
- 三条铁律：市场/品类先确认、不许跳步、以 skill/tools 为权威。
- 如何用新型号 prompt 启动审核。
- 如果使用 `run_full_audit.js`，必须用内联启动器，不能直接 `Workflow({scriptPath,args})`。
- 新机器落地时要改路径、装环境、避免中文路径硬编码。

### 5.2 `DHF-DMR审核-SKILL.md`

这是总纲，也是最重要的执行规范。它规定完整审查步骤：

1. 加载 working-method 总则。
2. 从本型号客户需求书确认市场和品类。
3. 建法规基线和参数槽位清单。
4. 用转换 skill 做可靠转换。
5. 建 SSOT 参数长表。
6. 调用 stage-01 到 stage-11 做逐阶段审查。
7. 调用 DMR/SOP skill 审制造资料。
8. 跑机械层确定性算法。
9. 做对抗证伪。
10. 汇总错误总表和裁决 HTML。
11. 跑证据核验和系统自检。
12. 交《完成自检表》。

### 5.3 `docs/方法与算法-详尽版.md`

这是技术深挖文档，适合想理解算法和设计取舍的人看。它详细讲：

- 文档转换管线。
- 覆盖台账。
- SSOT 参数长表。
- 阶段轴和维度轴。
- Tier1 数值一致性算法。
- 同构表 diff。
- 跨异构表对账。
- 模板残留扫描。
- 证据核验、对抗证伪、裁决库、自检。
- 多智能体编排和交互裁决输出。

### 5.4 `docs/DHF-DMR审核方法论-完整交接版.md`

这是面向另一台机器/另一个同事复用的完整 runbook。它包含：

- 新机器要拷哪些文件。
- 双轴审核方法。
- 五层地基。
- 七维度检查。
- 机械层脚本。
- 多智能体 workflow 模板。
- 图纸分支。
- 代码分支。
- 新型号执行 SOP。

### 5.5 `docs/DHF-DMR审核方法论-V2-双轴实战版.md`

这是方法论压缩版，重点说明：

- 阶段轴 + 维度轴为什么是 V2 的核心。
- 七个横向检查维度。
- 五层地基。
- 四条铁律和三条信条。
- 两个型号的实证结果。

---

## 6. 方法论整体架构

这套方法可以分成七层。

### 6.1 第 1 层：工作方法层

对应：

```text
skill/SKILL.md
```

它不绑定具体医学或 DHF 场景，而是规定通用做事原则：

- 实际看到才算数。
- 一步一验。
- 不确定就标 UNKNOWN / FALLBACK。
- 先查再做，不凭记忆。
- 多证据交叉确认。
- 卡住看现象，不盲调。
- 关键参数、脚本、产物要可复现。
- 长任务要定期报进度。
- 批量转换必须先抽样 3 个样本过闸门。

### 6.2 第 2 层：文档转换和可读性层

对应：

```text
skill/conversion-toolkit-skill
skill/doc-skill
skill/docx-skill
skill/pdf-skill
skill/xls-skill
skill/remaining-format-skill
scripts/convert_*.py
tools/scan_text_integrity.py
tools/unicode_safe_write.py
```

目标：把 AI 和脚本读不了或容易漏读的原始文件，转换成可审查材料：

- Markdown 正文。
- CSV / Markdown 表格。
- PDF / 页面 PNG。
- Excel 页面视觉通道。
- 图片和 OCR 文本。
- manifest。
- conversion_loss。

关键原则：

- 转换失败是覆盖缺口，不是“没发现问题”。
- Word 的勾选框、OLE、浮动形状要记录损失风险。
- PDF 少文本页要渲染为 PNG，走视觉/OCR。
- Excel 必须结构通道 + 页面视觉通道并行。
- 转换后必须扫乱码。

### 6.3 第 3 层：覆盖台账层

对应：

```text
scripts/coverage_ledger.py
scripts/build_ai_readiness_report.py
skill/extraction-ssot-skill
```

目标：证明该审的文件确实被纳入审查。

它对账三类东西：

```text
DHF/DMR 清单应有文件
文件夹实有文件
转换后可读文件
```

典型输出：

- `coverage_ledger.csv`
- `coverage_ledger.md`
- AI readiness 报告

如果某文件夹为空、某文件转换失败、某 PDF 只有扫描图，这些都必须显式记录。

### 6.4 第 4 层：SSOT 参数事实层

对应：

```text
skill/extraction-ssot-skill
scripts/assemble_incremental.py
scripts/assemble_audit.py
```

SSOT 是 Single Source of Truth，即参数实例长表。它不是判断结果，而是审查事实底座。

每条参数实例一般包括：

```text
阶段
参数名
参数值
单位
限定词/工况
来源文件
原文证据
```

后续数值一致性、横向参数槽位、证据核验都依赖它。

### 6.5 第 5 层：语义审查层

语义层分两根主轴：

```text
阶段轴
维度轴
```

阶段轴对应：

```text
skill/stage-01-dhf-check-skill
...
skill/stage-11-dhf-check-skill
skill/dmr-mfg-sop-check-skill
```

维度轴对应：

```text
skill/dimension-axis-skill
```

阶段轴负责按 DHF 生命周期顺序检查。  
维度轴负责跨全库横向扫阶段轴容易漏的接口问题。

### 6.6 第 6 层：机械层确定性算法

对应：

```text
dhf_audit_toolkit/
skill/mechanical-tier12-skill
scripts/run_audit.py
```

机械层不是 LLM 判断，而是纯脚本。它追求近零误报，主要抓：

- 模板残留。
- 旧型号残留。
- 占位符未替换。
- 数值冲突。
- 同构表差异。
- BOM / WI / 清单跨表对账。

### 6.7 第 7 层：自验证和交付层

对应：

```text
skill/self-verification-skill
scripts/verify_findings.py
scripts/audit_self_check.py
scripts/gen_report_review_html.py
_adjudications.csv
```

它负责：

- 把 finding 引文拿回全语料搜索，验证证据是否真实存在。
- 让独立 agent 对候选问题做对抗证伪。
- 记录人工裁决，防止误报反复出现。
- 跑完成自检，检查是否漏步骤。
- 生成可交互裁决 HTML。

---

## 7. 完整执行流程

下面按“新型号从零审一遍”的顺序说明。

### Phase 0：准备环境和路径

先确认：

```text
原始文件目录：<型号>_RAW 或原始 DHF/DMR 目录
转换输出目录：<型号>_MD
审查输出目录：<型号>_CHECK
交接包目录：DHF审核交接包v2
```

环境要求：

- Windows。
- Microsoft Office，尤其 Word COM 和 Excel COM。
- Python 3。
- 常用 Python 包：`pymupdf`、`openpyxl`、`xlrd`、`pillow`、`pandas`、`pywin32`、`pytesseract`。
- Tesseract OCR，建议含 `chi_sim`、`eng`、`osd` 语言包。
- 可选 LibreOffice，作为部分转换 fallback。

注意：

- 包内有些脚本仍带源机器路径，例如 `D:\AI_0415\03DHF`，新机器要改成本机路径。
- 不建议在脚本里硬编码中文路径。优先从 manifest、Path 对象、配置文件传参。
- 终端显示乱码时，不要把显示出来的问号当真实文件名。用 `Path.exists()` 或 PowerShell `Test-Path` 判断。

### Phase 1：确认市场、品类和法规基线

执行目标：

```text
从本型号自己的客户需求书/立项资料中确认市场和品类。
```

要确认：

- 型号。
- 项目编号。
- 目标市场。
- 产品品类。
- 注册路径。
- 项目负责人。
- 本品类参数槽位。

参考文件：

```text
品类参数槽位参考表.md
参考基线/m10_cn_nebulizer_regulatory_baseline.md
参考基线/us_forehead_thermometer_regulatory_baseline.md
```

输出建议：

```text
<型号>_CHECK/<型号>_<市场>_<品类>_regulatory_baseline.md
<型号>_CHECK/<型号>_parameter_slots.md
```

这一阶段最重要的是不要默认。市场/品类一旦错，后面所有法规判断都可能错。

### Phase 2：转换原始文件

执行目标：

```text
把原始 DHF/DMR/注册资料转换成 AI 和脚本能可靠读取的 Markdown、CSV、页面 PNG 和 manifest。
```

必须先做转换就绪检查：

```text
skill/conversion-toolkit-skill/scripts/check_conversion_tools.py
```

批量转换规则：

1. 先按文件类型分组：`.doc`、`.docx`、`.xls`、`.xlsx`、`.pdf`、图片、AI、DWG、ZIP 等。
2. 每类先抽 3 个代表性文件试转。
3. 检查样本输出：
   - Markdown 是否非空。
   - CSV 是否可读。
   - 页面 PNG 是否生成。
   - manifest 是否记录源路径。
   - OCR 是否工作。
   - conversion_loss 是否合理。
   - 中文路径是否没损坏。
4. 样本通过后才全量转换。

各格式要求：

| 格式 | 要求 |
|---|---|
| Word `.doc/.docx` | 尽量用 Word COM 或对应 skill，记录表格数、勾选框、OLE、浮动形状等损失风险。 |
| PDF | 取文本；少文本页渲染 PNG；扫描件或图像页必须标为视觉/OCR复核。 |
| Excel `.xls/.xlsx` | 必须结构通道 + 页面视觉通道。不能只转 CSV。 |
| 图片/AI/DWG/ZIP | 用 remaining-format skill，能 OCR 的 OCR，不能转的显式标高风险或人工复核。 |

Excel 双通道是重点：

```text
结构通道：
sheet CSV / sheet MD / 公式 / 合并单元格 / 隐藏行列 / 注释 / 超链接 / 颜色语义 / 图片清单

页面视觉通道：
sheet 导 PDF / PNG / 页面视觉 Markdown / page_manifest
```

转换完成后必须跑：

```text
python tools/scan_text_integrity.py <型号>_MD
```

如果出现连续问号、替换字符、UTF-8 被当作 CP1252 解码后的错显等乱码标记，不能直接进入审查，要先修转换或写入链路。

### Phase 3：建立覆盖台账

执行目标：

```text
确认“应有文件、实有文件、已转换文件、可读文件”之间是否一致。
```

可用脚本：

```text
scripts/coverage_ledger.py
scripts/build_ai_readiness_report.py
```

覆盖台账至少要回答：

- DHF 清单列出的文件是否都存在？
- 文件夹里的实物文件是否都被转换？
- 转换是否成功？
- 是否有空输出、低文本页、乱码、图像页？
- 哪些文件需要人工打开原件复核？

关键判断：

```text
0 个问题 ≠ 没问题
0 个文件被读到 = 覆盖缺口
```

### Phase 4：构建 SSOT 参数长表

执行目标：

```text
把所有关键参数抽成统一事实表，为后续数值一致性和横向比对提供地基。
```

建议字段：

```text
stage
doc_id
file_path
parameter_name
canonical_name
value
unit
qualifier
source_text
page_or_line
confidence
```

注意：

- 同一参数要记录工况/限定词。
- 不同限定词不要粗暴合并。
- 参数值本身对不对不由系统拍板，系统只查一致性和完整性。

### Phase 5：阶段轴语义审查

阶段轴按 DHF 生命周期逐阶段检查。核心规则是：

```text
下游必须大于等于上游。
```

下游可以更详细、更严格，但不能收窄、放松、漏项。

#### Stage 01：立项 / 客户需求 / 市场品类

对应：

```text
skill/stage-01-dhf-check-skill
```

重点：

- 产品身份。
- 销售区域。
- 产品品类。
- 客户需求。
- 法规路径。
- 适用标准。
- Stage 13 法规资料是否支撑。

输出：

- Stage 01 baseline。
- 客户需求与法规基线。
- 市场/品类确认依据。
- Stage 01 findings。

#### Stage 02：开发计划

对应：

```text
skill/stage-02-dhf-check-skill
```

重点：

- Stage 01 到 Stage 02 是否承接。
- 开发计划是否覆盖后续 DHF 输出。
- 项目团队、职责、进度、评审、设计变更流程是否明确。
- 后续各阶段是否有计划中的输出物。

#### Stage 03：风险管理

对应：

```text
skill/stage-03-dhf-check-skill
```

重点：

- 风险分析是否与产品用途和法规基线一致。
- Hazard / Risk / RiskControl 是否完整。
- 风险控制是否能追溯到设计输入、设计输出、验证。
- 剩余风险和风险收益是否闭环。

#### Stage 04：设计输入

对应：

```text
skill/stage-04-dhf-check-skill
```

重点：

- 客户需求是否转化为设计输入。
- 法规/标准要求是否纳入设计输入。
- 风险控制要求是否纳入。
- 关键参数是否可验证。
- 设计输入是否被下游放宽或遗漏。

#### Stage 05：结构方案 / 图纸

对应：

```text
skill/stage-05-dhf-check-skill
```

重点：

- 结构方案是否覆盖设计输入。
- 关键结构件、包装、标签、尺寸、材料、表面处理是否一致。
- 风险控制中结构相关项是否落地。
- 结构评审和图纸评审是否闭环。

#### Stage 06：硬件方案

对应：

```text
skill/stage-06-dhf-check-skill
```

重点：

- 电路、传感器、电池、电源、接口等是否承接设计输入。
- 硬件风险控制是否落地。
- 硬件参数与后续测试是否一致。
- 与结构、软件接口是否矛盾。

#### Stage 07：软件方案

对应：

```text
skill/stage-07-dhf-check-skill
```

重点：

- 软件需求规格说明。
- 软件设计方案。
- 软件安全等级。
- SOUP 清单。
- 软件配置项。
- 版本记录。
- 软件测试和验证。
- 软件需求与硬件/风险/设计输入的一致性。

#### Stage 08：T1 样机验证

对应：

```text
skill/stage-08-dhf-check-skill
```

重点：

- T1 验证计划和报告是否覆盖设计输入。
- 验证接受准则是否不低于上游。
- T1 未关闭项是否进入后续阶段。
- DFMEA、检验标准、寿命、电池、包装、标签、生物相容等验证证据是否完整。
- 不能用文件名、标题、清单行代替报告正文证据。

#### Stage 09：设计输出

对应：

```text
skill/stage-09-dhf-check-skill
```

重点：

- 设计输出清单是否完整。
- 输出文件是否存在、受控、有编号和版本。
- 输出是否覆盖 Stage 04 到 Stage 08。
- EBOM / ABOM / 包装 / 标签 / 图纸是否一致。
- 复用文件是否有受控复用或等同性理由。

#### Stage 10：试产 / 设计转移

对应：

```text
skill/stage-10-dhf-check-skill
```

重点：

- 是否实际试产或豁免试产。
- 豁免理由和批准是否充分。
- 试产申请、试产报告、总结、附件是否齐全。
- 接受准则、问题整改、复试、量产结论是否闭环。
- DMR 和设计输出适宜性是否有正文证据支持。

#### Stage 11：设计确认

对应：

```text
skill/stage-11-dhf-check-skill
```

重点：

- 最终设计确认是否覆盖设计输入、风险控制、设计输出。
- 用户现场试验、临床、软件确认、可用性、外部测试报告是否闭环。
- 外部报告排除项是否有额外证据覆盖。
- 设计输出版本和确认版本是否一致。
- 最终结论、签名、日期、批准是否完整。

#### DMR / SOP / 制造资料

对应：

```text
skill/dmr-mfg-sop-check-skill
```

重点：

- DMR 与设计输出是否一致。
- BOM、工序、作业指导书、检验规程是否对账。
- 生产记录和过程参数是否与设计要求一致。
- 标签、包装、UDI、说明书是否与注册/设计输出一致。

### Phase 6：维度轴横向审查

对应：

```text
skill/dimension-axis-skill
```

维度轴不是按阶段走，而是跨全库横扫。它专门补阶段轴的盲区。

七个主要维度：

1. **数值一致**：同一参数在多文件中是否冲突。
2. **可追溯断链**：需求、风险、控制、测试、报告之间是否断裂。
3. **不收窄**：下游是否放宽或缩小上游要求。
4. **矛盾措辞**：同一事项在不同文件中描述冲突。
5. **BOM 对账**：EBOM、ABOM、WI、清单是否配平。
6. **版本漂移**：文件编号、版本、BOM 版本是否无控制地漂移。
7. **角色串联**：按硬件、结构、软件、法规、包装、品质、工艺等角色串起来看是否自相矛盾。

外加三类横向机制：

- 横向参数槽位：每个参数全文件横向排比。
- 工程师角色串联：按人/角色聚合责任范围。
- 反向完备性：拿法规基线逐条反查缺失。

### Phase 7：机械层确定性检查

机械层工具在：

```text
dhf_audit_toolkit/
```

#### 7.1 `check_residue.py`

用途：

- 扫模板残留。
- 扫异类品类词。
- 扫旧型号。
- 扫占位符。

典型命令：

```bash
python check_residue.py "<型号>_MD" --product <型号> --foreign 体温计,血压计,冲牙器 --models 旧型号A,旧型号B --out 机械校验-残留.csv
```

输出类型：

- 异类品类残留。
- 异类型号残留。
- 占位符未替换。

注意：复用件和残留需要人工区分。

#### 7.2 `check_params_numeric.py`

用途：

- 基于 SSOT 参数长表做数值一致性检查。
- 单位归一。
- 区间、容差、边界解析。
- 点落区间判一致。

典型命令：

```bash
python check_params_numeric.py 参数明细.csv --product <型号> --out 数值冲突.csv
```

特点：

- 近零误报。
- 低召回。
- 抽漏了参数它查不到。
- 精度/分辨率等复杂语义场景交给 LLM。

#### 7.3 `check_table_diff.py`

用途：

- 比较两份同构表。
- 适合 BOM、组件清单、版本前后差异。
- 按主键对齐，输出仅 A、仅 B、字段不同。

典型命令：

```bash
python check_table_diff.py A.xlsx B.xlsx --labelA T1 --labelB 设计输出 --out 表差异.csv
```

边界：

- 只适合结构相近的同构表。
- 跨异构表要用 `check_bom_crosswalk.py`。

#### 7.4 `check_bom_crosswalk.py`

用途：

- BOM ↔ 清单 ↔ WI 跨异构对账。
- 输入统一记录表，字段如来源、品名、用量、规格、图号、物料编码。
- 按品名规范化和模糊匹配聚合。

典型命令：

```bash
python check_bom_crosswalk.py BOM记录表.csv --out BOM对账.csv
```

输出：

- 用量冲突。
- 规格冲突。
- 图号冲突。
- 范围差异。

边界：

- 它是候选生成器，不是自动最终结论。
- WI 散文如果由 LLM 抽取，可能有瑕疵，需要人审。

#### 7.5 `dhf_pipeline.py`

用途：

- 将转换、覆盖台账、残留、数值等机械步骤串起来。
- 需要先按新机器路径修改 `BASE` 和 `MODELS`。

### Phase 8：对抗证伪

对应：

```text
skill/self-verification-skill
docs/方法与算法-详尽版.md 的 CoVe 部分
```

对抗证伪的思路：

```text
候选 finding 不是直接进最终报告，
而是让独立 agent 专门尝试推翻它。
```

反驳点包括：

- 是否不同工况。
- 是否不同版本。
- 是否法规不适用。
- 是否把标题/文件名当正文证据。
- 是否旧型号作为复用件合法出现。
- 是否参数限定词不同。
- 是否引用真实但推理错误。

输出结果：

```text
保留
毙掉
降级
待人工确认
```

历史经验：大约四分之一候选会被毙掉。这个比例不是失败，而是质量闸门生效。

### Phase 9：证据核验、自检和裁决库

#### 9.1 `verify_findings.py`

用途：

```text
把每条 finding 的原文引用拿回全语料搜索，验证证据是否真实存在。
```

分类：

- 有据。
- 部分有据。
- 缺失断言。
- 可疑。
- 无引文。

它验证的是“引文是否存在”，不是“结论是否一定正确”。  
结论正确性还需要对抗证伪和人工裁决。

#### 9.2 `audit_self_check.py`

用途：

```text
跑完一个型号后，检查该做的步骤有没有漏。
```

检查内容包括：

- 工具产物是否齐全。
- 阶段覆盖是否完整。
- 字段是否完整。
- 七维度有没有整类漏查。
- 已裁决误报是否重现。
- 法规基线锚定是否落实。
- 证据核验摘要是否达标。
- 跨型号系统病是否被检查。

#### 9.3 `_adjudications.csv`

用途：

```text
记录人工已经裁决过的误报或重复问题，防止后续反复上报。
```

建议使用方式：

- 开审时注入已裁决误报。
- 自检时撞库检查。
- PM 每否掉一条误报，就补一行。

### Phase 10：生成交付物

主要脚本：

```text
scripts/assemble_audit.py
scripts/assemble_incremental.py
scripts/assemble_m10.py
scripts/gen_report_review_html.py
scripts/gen_report_pt7_html.py
```

常见交付物：

| 产物 | 作用 |
|---|---|
| `<型号>-错误总表.csv` | 最核心问题清单。 |
| `<型号>-运行参数长表.csv` | SSOT 参数实例表。 |
| `<型号>-审核报告.md` | 审查摘要和问题说明。 |
| 裁决版 HTML | 给 PM/工程师逐条接受、不接受、待定。 |
| 覆盖台账 | 证明文件覆盖情况。 |
| 证据核验报告 | 证明 finding 引文是否真实。 |
| 完成自检表 | 证明流程没有漏步骤。 |

---

## 8. 特殊分支

### 8.1 图纸分支

对应：

```text
skill/drawing/SKILL_2D_Drawing_Reading.md
skill/drawing/SKILL_3D_Model_Analysis.md
skill/drawing/SKILL_3D_Section_Analysis.md
scripts/prep_2d.py
```

何时启用：

- 有 2D 工程图、PDF 图纸、丝印、铭牌、结构件图。
- 有 3D STEP/STP 模型。
- 图纸参数需要和设计输入、BOM、标签、结构文件对账。

2D 图纸流程：

1. 渲染到不低于 300 DPI。
2. 分块切图。
3. 视觉 agent 读取标题栏、尺寸、公差、材料、版本、图号。
4. 与设计输入、设计输出、BOM、DMR 对账。

注意：图纸结论必须“实际看到”，不能只靠文件名。

### 8.2 代码分支

对应：

```text
skill/code-branch-skill
```

何时启用：

- 拿到了 C 固件源码工程。
- 有 `FWLIB/`、`User/`、`.uvprojx`、`.si4project` 等。

用途：

- 用固件源码中的常量和版本作为“机器实际行为”证据。
- 对账固件 ↔ 检验标准 ↔ 设计/SRS。

关键铁律：

- 先认正源，排除 `.si4project/Backup` 和带编号的历史副本。
- grep 身份：MCU、传感器、版本宏。
- grep 行为常量：电压、关机、量程、单位、标定等。
- 定点常量必须读注释和换算函数，不能想当然除以 100。
- 引用必须是正源路径 + 行号。

---

## 9. `skill/` 目录资产说明

### 9.1 通用 skill

| Skill | 作用 |
|---|---|
| `skill/SKILL.md` | working-method 总则，规定工具、做事方法、批量转换闸门。 |
| `conversion-toolkit-skill` | 检查转换工具链是否就绪。 |
| `doc-skill` | `.doc` 老 Word 格式转换与审查。 |
| `docx-skill` | `.docx` 转换与审查。 |
| `pdf-skill` | PDF 文本抽取、页面渲染、扫描页处理。 |
| `xls-skill` | Excel 双通道转换，结构 + 页面视觉。 |
| `remaining-format-skill` | 非主流格式、图片、AI、DWG、ZIP 等处理。 |

### 9.2 审查 skill

| Skill | 作用 |
|---|---|
| `stage-01-dhf-check-skill` | 立项、客户需求、市场/品类、法规路径。 |
| `stage-02-dhf-check-skill` | 开发计划、团队、输出物计划。 |
| `stage-03-dhf-check-skill` | 风险管理和风险控制闭环。 |
| `stage-04-dhf-check-skill` | 设计输入。 |
| `stage-05-dhf-check-skill` | 结构方案、结构图纸。 |
| `stage-06-dhf-check-skill` | 硬件方案。 |
| `stage-07-dhf-check-skill` | 软件方案。 |
| `stage-08-dhf-check-skill` | T1 样机验证。 |
| `stage-09-dhf-check-skill` | 设计输出。 |
| `stage-10-dhf-check-skill` | 试产、设计转移。 |
| `stage-11-dhf-check-skill` | 设计确认。 |
| `dmr-mfg-sop-check-skill` | DMR、制造、SOP、工艺、检验。 |

### 9.3 补层 skill

| Skill | 作用 |
|---|---|
| `extraction-ssot-skill` | 覆盖台账和 SSOT 参数长表。 |
| `dimension-axis-skill` | 7 维横向审查、槽位、角色串联、反向完备性。 |
| `mechanical-tier12-skill` | Tier1/Tier2 确定性脚本。 |
| `self-verification-skill` | 证据核验、对抗证伪、裁决库、自检。 |
| `multi-agent-orchestration-skill` | 多智能体并行、增量、resume、心跳。 |
| `code-branch-skill` | 固件代码分支。 |
| `llm-wiki-skill` | 构建给 LLM 读取的 wiki/索引层。 |

### 9.4 图纸 skill

| Skill | 作用 |
|---|---|
| `SKILL_2D_Drawing_Reading.md` | 2D 工程图读取。 |
| `SKILL_3D_Model_Analysis.md` | 3D 模型分析。 |
| `SKILL_3D_Section_Analysis.md` | 3D 剖面分析。 |

---

## 10. `scripts/` 目录资产说明

| 脚本 | 作用 |
|---|---|
| `convert_pt9s.py` | 示例转换器，按 Word/Excel/PDF 分流，生成 Markdown 和 manifest。 |
| `convert_m10.py` | M10 分片并行转换示例。 |
| `convert_remaining_to_pt9l_md.py` | 处理 AI、图片、DWG、ZIP 等剩余格式。 |
| `recover_word_with_markitdown.py` | 用 MarkItDown/Word/LibreOffice 补救 Word 转换。 |
| `audit_word_conversion_loss.py` | 检查 Word 转换损失，如勾选框、OLE、浮动形状。 |
| `coverage_ledger.py` | 清单 vs 实物 vs 转换的覆盖台账。 |
| `build_ai_readiness_report.py` | 构建 AI 可读性报告。 |
| `build_knowledge_layer.py` | 构建知识层、基线、清单、索引。 |
| `build_pt9l_llm_wiki.py` | 构建 PT9L LLM wiki。 |
| `extend_pt9l_llm_wiki_excel_pdf.py` | 扩展 Excel/PDF wiki。 |
| `extend_pt9l_llm_wiki_remaining.py` | 扩展剩余格式 wiki。 |
| `assemble_audit.py` | 通用汇总 workflow 输出，生成参数长表、错误总表、报告。 |
| `assemble_incremental.py` | 增量审核汇总。 |
| `assemble_m10.py` | M10 专用汇总示例。 |
| `run_audit.py` | 确定性 runner + 自检硬闸门。 |
| `verify_findings.py` | 证据核验器。 |
| `audit_self_check.py` | 审核系统自检。 |
| `gen_report_review_html.py` | 生成可交互裁决 HTML。 |
| `gen_report_pt7_html.py` | PT7 风格 HTML 报告。 |
| `auto_table_diff.py` | 自动配对同构表并跑 diff。 |
| `prep_2d.py` | 2D 图纸渲染和分块前处理。 |

---

## 11. `tools/` 目录资产说明

### 11.1 `scan_text_integrity.py`

用途：

```text
扫描 Markdown、CSV、JSON、HTML、YAML、PY 等文本文件里的乱码风险。
```

它会标记：

- 连续问号标记。
- Unicode replacement character。
- 常见 UTF-8 被当 CP1252 的错显。
- UTF-8 解码失败。

转换完成后必须跑。建议命令：

```bash
python tools/scan_text_integrity.py <型号>_MD
```

### 11.2 `unicode_safe_write.py`

用途：

```text
在 Windows/PowerShell 环境下安全写中文文件，避免命令行参数传递时中文变成问号。
```

支持：

- 从 UTF-8 文本文件写入。
- 从 JSON 字段写入。
- 从 base64 文件写入。
- 从 stdin base64 写入。

它写完会回读校验，如果发现连续问号或替换字符会拒写。

---

## 12. `dhf_audit_toolkit/` 目录资产说明

| 工具 | 类型 | 作用 |
|---|---|---|
| `check_residue.py` | Tier1 | 模板残留、异类型号、占位符。 |
| `check_params_numeric.py` | Tier1 | 数值一致性，单位归一，区间判定。 |
| `check_table_diff.py` | Tier1 | 同构表 key-join diff。 |
| `check_bom_crosswalk.py` | Tier2 | BOM/清单/WI 跨异构对账。 |
| `dhf_pipeline.py` | 编排脚本 | 机械层流程串联。 |
| `README.md` | 使用说明 | 给同事快速复用的机械层说明。 |
| `PT9L机械校验报告.csv` | 示例产物 | PT9L 机械校验结果示例。 |

---

## 13. 法规基线和品类参数槽位

### 13.1 `品类参数槽位参考表.md`

它有两种用途：

1. 开审前确定本品类要抽哪些参数进 SSOT。
2. 识别串品类残留。

示例：

- 体温计重点参数：量程、分辨率、精度、工作环境、自动关机、低压阈值、IP、防护、显示单位、测量距离等。
- 雾化器重点参数：雾化率、MMAD、可吸入比例、储药杯容量、残留药量、噪音、振荡频率、电压、电流、续航、自清洁、防护等级等。
- 血压计参数在非血压计项目中出现，通常是串品类残留信号。

### 13.2 `参考基线/m10_cn_nebulizer_regulatory_baseline.md`

用途：

- 中国 NMPA 雾化器基线示例。
- 说明中国注册路径、PTR、GB 9706.1、YY/T 0316、GB/T 16886、UDI 等。
- 特别强调 M10 是中国项目，不应反向套 FDA / 510(k) / EU MDR。

### 13.3 `参考基线/us_forehead_thermometer_regulatory_baseline.md`

用途：

- 美国额温计/临床电子体温计基线示例。
- 包含 21 CFR 880.2910、880.9、807、801、FDA 产品码 SDV/FLL 等。
- 说明 ISO 80601-2-56、ASTM E1965、IEC 60601 等标准适用逻辑。

---

## 14. Workflow 模式和手工模式

交接包里提供了 `run_full_audit.js` 主控 workflow。它用于在 Claude Code 中代码强制执行：

```text
Scout 侦察市场/品类
-> 逐单元并行审查
-> 跨单元对账
-> assemble 汇总
-> run_audit 确定性闸门
```

### 14.1 使用 workflow 时的红线

不能直接：

```text
Workflow({scriptPath, args})
```

因为历史上这个方式可能导致 args 没注入，脚本用默认 model 和空路径，最后审错型号。

必须用内联启动器，通过：

```text
workflow({scriptPath: '<包路径>/run_full_audit.js'}, P)
```

把参数传进去。

### 14.2 非 Claude Code 环境怎么用

如果没有 Workflow 引擎，也能用这套包：

1. 读 `DHF-DMR审核-SKILL.md`。
2. 手动按步骤执行转换、覆盖、机械层、自验证。
3. 用普通 agent 按 stage skill 和 dimension skill 做语义审查。
4. 用 Python 脚本汇总、自检、生成报告。

换句话说：

- 并行 fan-out 编排依赖 Claude Code workflow。
- 确定性工具、证据核验、自检、报告脚本都是普通 Python，任何环境都可以复用。

---

## 15. 最终交付物标准

一个合格审查包至少应包含：

| 交付物 | 必要性 | 说明 |
|---|---|---|
| 法规基线 | 必须 | 由本型号市场/品类确认而来。 |
| 参数槽位清单 | 必须 | 本品类应抽参数。 |
| 转换 manifest | 必须 | 证明原始件如何转成可读材料。 |
| 转换损失记录 | 必须 | 证明哪些内容需人工复核。 |
| 乱码扫描结果 | 必须 | 应为 0 命中，或有解释和修复记录。 |
| 覆盖台账 | 必须 | 清单、实物、转换三方对账。 |
| SSOT 参数长表 | 必须 | 后续数值和横向槽位比对地基。 |
| 阶段审查报告 | 必须 | Stage 01-11 和 DMR/SOP。 |
| 维度轴报告 | 必须 | 7 维横扫结果。 |
| 机械层报告 | 必须 | 残留、数值、表 diff、BOM 对账。 |
| 错误总表 | 必须 | 最终问题清单。 |
| 证据核验报告 | 必须 | 每条 finding 的证据状态。 |
| 裁决版 HTML | 建议必须 | 供 PM/工程师逐条裁决。 |
| 完成自检表 | 必须 | 没有自检表视为未完成。 |

---

## 16. 完成自检表模板

| 步骤 | 状态 | 证据/产物或跳过理由 |
|---|---|---|
| 加载 working-method 总则 | ✅/⏭️ | |
| 从客户需求书确认市场/品类 | ✅/❌ | |
| 建法规基线 | ✅/❌ | |
| 建品类参数槽位清单 | ✅/❌ | |
| 转换就绪检查 | ✅/❌ | |
| 批量转换抽样闸门 | ✅/❌ | |
| Word 转换并记录损失 | ✅/⏭️ | |
| PDF 文本/页面 PNG/OCR 处理 | ✅/⏭️ | |
| Excel 双通道转换 | ✅/⏭️ | |
| remaining formats 处理 | ✅/⏭️ | |
| 跑乱码扫描 | ✅/❌ | |
| 建覆盖台账 | ✅/❌ | |
| 建 SSOT 参数长表 | ✅/❌ | |
| Stage 01-11 阶段轴审查 | ✅/⏭️ | |
| DMR/SOP 审查 | ✅/⏭️ | |
| 维度轴 7 维横扫 | ✅/⏭️ | |
| `check_residue.py` | ✅/⏭️ | |
| `check_params_numeric.py` | ✅/⏭️ | |
| `check_table_diff.py` | ✅/⏭️ | |
| `check_bom_crosswalk.py` | ✅/⏭️ | |
| 对抗证伪 | ✅/⏭️ | |
| 证据核验 | ✅/❌ | |
| 自检硬闸门 | ✅/❌ | |
| 裁决库撞库 | ✅/⏭️ | |
| 图纸分支 | ✅/⏭️ | |
| 代码分支 | ✅/⏭️ | |
| 错误总表 | ✅/❌ | |
| 裁决版 HTML | ✅/⏭️ | |

要求：

- 任一必查项是 ❌，审查不合格。
- 任一 ⏭️ 必须写明理由。
- 不能用“没发现问题”替代“没检查”。

---

## 17. 常见踩坑清单

### 17.1 审错型号

原因：

- workflow 参数没传进去。
- 默认 model/path 被使用。
- Scout 在错误目录里找文件。

规避：

- `run_full_audit.js` 必须用内联启动器。
- 顶部 guard 缺 model/mdRoot/checkDir 要直接 throw。
- 输出里检查型号、路径、客户需求书是否一致。

### 17.2 市场/品类默认

原因：

- 继承上一个项目经验。
- 未读本型号客户需求书。

规避：

- Stage 01 必须先确认市场/品类。
- 法规基线必须按本型号生成。

### 17.3 Excel 只转结构，不转页面

后果：

- 颜色语义、勾选、图标、盖章、版式、图片证据丢失。

规避：

- `xls-skill` 要求结构通道 + 页面视觉通道。

### 17.4 转换失败被当成没问题

后果：

- 文件没有被审查，却输出“无问题”。

规避：

- 覆盖台账必须列出失败文件。
- conversion_loss 必须进入人工复核清单。

### 17.5 证据引用找不到原文

原因：

- Agent 改写了证据。
- 引用太短或太泛。
- 证据来自文件名/标题，不是正文。

规避：

- finding 必须带逐字原文。
- 跑 `verify_findings.py`。
- 对可疑项人工复核。

### 17.6 schema 字段名用中文

后果：

- 多智能体结构化输出可能 API 400。

规避：

- JSON schema key 用 ASCII。
- 值可以是中文。

### 17.7 中文路径硬编码

后果：

- 开源工具静默失败。
- 终端乱码导致路径判断错误。

规避：

- 用 Path/manifest。
- 必要时复制到英文临时路径处理。
- 写中文用 `unicode_safe_write.py`。

### 17.8 数值检查误用

原因：

- 忽略限定词/工况。
- 把动态电流和静态电流硬比。

规避：

- SSOT 中保留 qualifier。
- `check_params_numeric.py` 按参数名 + 限定词分组。

---

## 18. 实证基准

交接包中给出的已跑结果可作为复现参考：

| 型号 | 结果数量 | 备注 |
|---|---:|---|
| PT9L | 191 | 美国体温计方向，重跑后证据有据率显著提升。 |
| PT9S | 169 | 发现数值冲突和 BOM/WI 对账问题。 |
| PT7 | 286 | 大量跨文件夹关联问题和模板残留。 |
| M10 | 199 | 中国 NMPA 雾化器，跨品类跨市场验证。 |

证据有据率参考：

```text
约 76% - 85%
```

对抗证伪历史参考：

```text
约 1/4 候选被毙掉
```

这些数字不是硬性 KPI，而是用来判断新机器复现是否离谱。

---

## 19. 推荐给接手同事的阅读顺序

如果时间很少：

1. `00_START_HERE.md`
2. `DHF-DMR审核-SKILL.md`
3. 本文档
4. `dhf_audit_toolkit/README.md`
5. `品类参数槽位参考表.md`

如果要真正接手跑新型号：

1. `skill/SKILL.md`
2. `skill/conversion-toolkit-skill/SKILL.md`
3. 对应格式 skill，特别是 `xls-skill`
4. `stage-01` 到 `stage-11`
5. `dimension-axis-skill`
6. `mechanical-tier12-skill`
7. `self-verification-skill`
8. `docs/DHF-DMR审核方法论-完整交接版.md`

如果要理解算法原理：

1. `docs/方法与算法-详尽版.md`
2. `docs/DHF-DMR审核方法论-V2-双轴实战版.md`

---

## 20. 给新型号的最小执行 SOP

下面是一条最小但完整的执行链。

### 20.1 建目录

```text
<型号>_RAW      原始文件
<型号>_MD       转换后 Markdown/CSV/PNG/manifest
<型号>_CHECK    审查产物
```

### 20.2 读总纲

```text
DHF-DMR审核-SKILL.md
```

### 20.3 确认市场/品类

从客户需求书读出：

```text
市场
品类
型号
项目号
注册路径
```

产出法规基线和参数槽位清单。

### 20.4 转换

按格式 skill 转换，先抽样再全量。

转完：

```bash
python tools/scan_text_integrity.py <型号>_MD
```

### 20.5 覆盖台账

运行或手动构建：

```text
清单应有
文件实有
转换成功
AI 可读
人工复核
```

### 20.6 SSOT 参数长表

抽参数实例，形成：

```text
<型号>-运行参数长表.csv
```

### 20.7 阶段轴

按 stage-01 到 stage-11 审查。  
DMR 用 dmr skill。

### 20.8 维度轴

跑 7 维横扫，补阶段轴盲区。

### 20.9 机械层

至少运行：

```bash
python check_residue.py ...
python check_params_numeric.py ...
python check_table_diff.py ...
python check_bom_crosswalk.py ...
```

不适用的要写理由。

### 20.10 对抗证伪

对候选 finding 做反驳，过滤误报。

### 20.11 汇总和报告

生成：

```text
错误总表
参数长表
审核报告
裁决版 HTML
```

### 20.12 证据核验和自检

运行：

```bash
python verify_findings.py ...
python audit_self_check.py <型号>
```

最后交完成自检表。

---

## 21. 这套包的核心价值

这套交接包最值得复用的不是某一个脚本，而是一套审查纪律：

```text
没有确认市场/品类，就不能审法规。
没有可靠转换，就不能说没问题。
没有覆盖台账，就不能说审全了。
没有原文证据，就不能进报告。
没有对抗证伪，就不能信候选 finding。
没有自检表，就不能算完成。
```

它把 AI 的语义理解、脚本的确定性复核、人工裁决和经验沉淀串在一起，形成一个能逐步迁移到新型号、新品类、新市场的审查体系。
