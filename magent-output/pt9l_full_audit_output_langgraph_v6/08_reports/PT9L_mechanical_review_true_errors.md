# PT9L 机械候选二轮复审确认问题

> 生成时间：2026-06-30T15:36:40
> 范围：仅包含 mechanical_review_node 判定为 confirm 的机械候选。

## 1. 摘要

- 确认问题数：156

## 2. 问题清单

### 1. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Finding ID：`MR-0001`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:2` # 客户需求书E0-血压计 23.6

### 2. 结构设计方案评审检查表文件标题使用"血压计"，但该文件属于PT9L额温计Stage 05正式结构设计阶段文件，存在产品身份标签污染。

- Finding ID：`MR-0002`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件"结构设计方案评审检查表-血压计E0 23.11"位于Stage 05结构设计方案目录，属于PT9L DHF正式受控文件。文件标题中"血压计"与PT9L（红外额温计）产品类别不符，构成文件命名层面的产品身份污染。虽然仅有1个候选（MF-0030），但其位于正式主审范围，文件标题直接标注错误品类，影响文件可追溯性和产品身份一致性。
- 证据：
  - `05 结构设计方案E0 23.11\结构设计方案评审检查表-血压计E0 23.11.via_xlsx.clean.md:2` # 结构设计方案评审检查表-血压计E0 23.11

### 3. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0003`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 4. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0004`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 5. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0005`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:20` \| **Drawing NO.** \| （待填 - 见右下标题栏） \|

### 6. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0006`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:21` \| **Part name** \| （待填 - 见右下标题栏中文零件名） \|

### 7. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0007`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:22` \| **Pro material** \| （待填） \|

### 8. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0008`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:23` \| **Surf dispose** \| （待填） \|

### 9. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0009`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:24` \| **Scale** \| （待填） \|

### 10. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0010`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:25` \| **Tolerance** \| （待填 - 见标题栏 Tolerance 表） \|

### 11. 硬件设计方案E0读图报告（Stage 06正式文件）标题栏中Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance等关键字段均为"待填"占位符，文件头注释亦明确标注"自动生成模板+待填"，属于正式受控文件中关键设计信息未填写的实质性质量问题。

- Finding ID：`MR-0011`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 06主审范围（primary_scope=true），路径为正式硬件设计方案目录。文件头HTML注释明确写明"2026-05-14 自动生成模板+待填"，说明该MD文件是由工具自动生成的读图报告，但标题栏A级字段（图号、零件名、材料、表面处理、比例、公差）均未填写实际内容，仅保留"（待填）"占位符。这些字段是工程图纸标题栏的核心受控信息，缺失将导致DHF中硬件设计证据链不完整，无法追溯具体零件的图号与规格。虽然注释提示"见右下标题栏"，但MD文件作为受控文档副本本身应包含完整信息，不能以"参见原PDF"为由留空。构成P1级受控文件信息缺失问题。
- 证据：
  - `06 硬件设计方案E0 23.11\硬件设计方案E0.md:33` > 待填 - 通常位于左下角或右下角，逐条完整录入（不可跳过）。

### 12. 软件质量策划评审检查表（Stage 07正式文件）中存在名为"模板修改记录"的Sheet，内容为空白行，属于Excel模板结构未实例化、修改记录未填写的受控文件质量问题。

- Finding ID：`MR-0012`
- 二审 Agent：Document Control Agent
- 严重度：`P2`
- 二审理由：该文件位于Stage 07主审范围（primary_scope=true），为软件质量策划评审检查表的正式受控版本。"模板修改记录"Sheet包含修改日期、修改人、修改内容三列表头，但所有数据行均为空白，说明该Sheet为模板原始结构，从未被实际填写。受控文件的修改记录是版本管理的重要组成部分，空白修改记录表明文件版本变更历史未被记录，影响文件受控完整性。定为P2级，因其影响版本追溯但不直接影响设计输出内容。
- 证据：
  - `07 软件设计方案E0 23.11\质量策划E0 23.11\软件质量策划评审检查表E0  23.11.via_xlsx.clean.md:70` ## Sheet: 模板修改记录

### 13. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0013`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:2` # BP3L 软件图样E0 23.11

### 14. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0014`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:50` ![图片 13](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_d468a82f.png)

### 15. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0015`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:54` ![图片 23](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_cd06a829.png)

### 16. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0016`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:58` ![图片 24](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_7adb510b.png)

### 17. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0017`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:62` ![图片 25](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_e758576.png)

### 18. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0018`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:66` ![图片 27](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_91561bdc.png)

### 19. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0019`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:70` ![图片 18](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_9bff6abd.png)

### 20. PT9L正式软件设计文件（软件图样）的文件标题、文件名及所有图片资产路径均使用旧型号"BP3L"命名，文件编号虽已更新为PT9L，但文件主体身份标识未完成型号转换，存在旧型号残留污染。

- Finding ID：`MR-0020`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0041至MF-0048均来自同一文件"BP3L 软件图样E0 23.11.via_lo_html.clean.md"，该文件位于Stage 07软件设计方案正式目录，属于PT9L DHF主审范围。文件编号（第6行）已标注"PT9L-RJTY01 V1.0"，说明该文件意图归属PT9L，但文件标题、文件名及全部图片资产路径（如BP3L 软件图样E0 23.11_html_d468a82f.png等）仍使用"BP3L"命名，未完成型号转换。这不是合理引用，而是文件身份标识与文件编号不一致的旧型号残留，影响软件设计证据链的产品身份一致性，严重性较高。
- 证据：
  - `07 软件设计方案E0 23.11\软件图样E0 23.11\BP3L 软件图样E0 23.11.via_lo_html.clean.md:74` ![图片 19](BP3L 软件图样E0 23.11.via_lo_html_assets/BP3L 软件图样E0 23.11_html_4f8d1455.png)

### 21. 软件需求规格文件（Stage 07正式文件）中出现"第0页/共5页 模板版本：I"字样，为模板页码占位符及模板版本标识未替换，属于正式文件中模板残留问题。

- Finding ID：`MR-0021`
- 二审 Agent：Document Control Agent
- 严重度：`P2`
- 二审理由：该文件位于Stage 07主审范围（primary_scope=true），为软件需求规格说明书的正式受控版本。"第0页/共5页"是明显的模板占位符（正式文件页码不应为0），"模板版本：I"是模板管理标识，均应在文件正式化时替换为实际内容。这些残留标识表明文件可能未经完整的模板实例化处理即进入受控状态，影响文件的正式性和可信度。定为P2级，因其属于格式/标识问题，不直接影响需求内容本身，但影响文件受控状态的判断。
- 证据：
  - `07 软件设计方案E0 23.11\软件需求E0 23.11\2-1 软件需求规格E0 23.11.via_lo_html.clean.md:177` 第 0 页 / 共 5 页 模板版本： I

### 22. Stage 11 DFMEA文件中FMEA编号含"XXXX"占位符（KD-XXXX-PDFM01 V1.0、KD-XXXX-ODFM01 V1.0），且产品型号字段填写为KD-5915L而非PT9L，存在文件编号未受控及型号不符的双重质量问题。

- Finding ID：`MR-0022`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），为结构类FMEA正式文件。FMEA编号中的"XXXX"是明确的占位符，表明文件编号未被正式分配，违反受控文件编号唯一性要求。同时，产品型号字段填写为KD-5915L，而本DHF/DMR审查对象为PT9L，型号不符可能意味着该FMEA文件是从其他产品模板复制而来且未完成适配，或存在错误引用。FMEA编号未受控直接影响设计风险分析的可追溯性，型号不符影响证据链的归属确认，两者叠加构成P1级问题。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:12` \|  \| 分类： \| 包装类 \|  \|  \| 编制人： \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA编号：KD-XXXX-PDFM01 V1.0 \|  \|  \|  \|  \|  \|  \|  \|

### 23. Stage 11 DFMEA文件中FMEA编号含"XXXX"占位符（KD-XXXX-PDFM01 V1.0、KD-XXXX-ODFM01 V1.0），且产品型号字段填写为KD-5915L而非PT9L，存在文件编号未受控及型号不符的双重质量问题。

- Finding ID：`MR-0023`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），为结构类FMEA正式文件。FMEA编号中的"XXXX"是明确的占位符，表明文件编号未被正式分配，违反受控文件编号唯一性要求。同时，产品型号字段填写为KD-5915L，而本DHF/DMR审查对象为PT9L，型号不符可能意味着该FMEA文件是从其他产品模板复制而来且未完成适配，或存在错误引用。FMEA编号未受控直接影响设计风险分析的可追溯性，型号不符影响证据链的归属确认，两者叠加构成P1级问题。
- 证据：
  - `11 T1样机\05 DFMEA E0 23.11\结构类FMEA  E0(1)(1).via_xlsx.clean.md:188` \|  \| 分类： \| 辅料类 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \| FMEA编号：KD-XXXX-ODFM01 V1.0 \|  \|  \|  \|  \|  \|  \|

### 24. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0024`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）

### 25. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0025`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:2` # PT3SBT标签审核表（海外更新）

### 26. PT3SBT标签审核表（Stage 11正式文件）中包含PT2L（美亚）和PT9L的标签检查报告模板，所有Sheet的拟制、审核、检查签署日期均为空白（"年月日"占位符），且文件名含PT3SBT与内容型号不一致，属于标签审核文件未完成签署及型号标识混乱的受控质量问题。

- Finding ID：`MR-0026`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），文件名为PT3SBT标签审核表，但内容中Sheet"标签报告模板-美"对应PT2L（美亚），Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"对应PT9L，文件名与部分内容型号不一致，存在型号混用风险。更关键的是，所有Sheet中的拟制、审核、检查签署日期均为"年月日"空白占位符，表明标签审核活动从未被正式签署确认。标签审核表是医疗器械上市前的重要合规文件，签署缺失意味着审核活动无法被证明已实际执行，构成P1级受控合规问题。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:6` ## Sheet: 标签报告模板 -美

### 27. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0027`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:8` PT2L(美亚)标签检查报告

### 28. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0028`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:12` 产品型号： PT2L 项目编号： 2020-DEV01 产品/项目名称：红外体温计

### 29. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0029`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:16` \| ▉说明书 □彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-SMSP09 \|  \|  \|  \|  \|

### 30. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0030`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:17` \| □说明书 ▉彩包装 □铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-CBZP07 \|  \|  \|  \|  \|

### 31. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0031`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:18` \| □说明书 □彩包装 ▉铭牌 □外箱 □其他： \|  \|  \|  \| PT2L-F96 \|  \|  \|  \|  \|

### 32. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0032`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:19` \| □说明书 □彩包装 □铭牌 ▉外箱 □其他： \|  \|  \|  \| PT2L-F97 \|  \|  \|  \|  \|

### 33. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0033`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:22` \| IEC 60601-1 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ01 V1.0 \|

### 34. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0034`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:23` \| IEC 60601-1-2 \| A \|  \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| ▉Pass □Fail \| PT2L(美亚)-ZXBQ02 V1.0 \|

### 35. PT3SBT标签审核表（Stage 11正式文件）中包含PT2L（美亚）和PT9L的标签检查报告模板，所有Sheet的拟制、审核、检查签署日期均为空白（"年月日"占位符），且文件名含PT3SBT与内容型号不一致，属于标签审核文件未完成签署及型号标识混乱的受控质量问题。

- Finding ID：`MR-0035`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），文件名为PT3SBT标签审核表，但内容中Sheet"标签报告模板-美"对应PT2L（美亚），Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"对应PT9L，文件名与部分内容型号不一致，存在型号混用风险。更关键的是，所有Sheet中的拟制、审核、检查签署日期均为"年月日"空白占位符，表明标签审核活动从未被正式签署确认。标签审核表是医疗器械上市前的重要合规文件，签署缺失意味着审核活动无法被证明已实际执行，构成P1级受控合规问题。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:39` ## Sheet: 标签报告模板 -美  (2)

### 36. PT3SBT标签审核表（Stage 11正式文件）中包含PT2L（美亚）和PT9L的标签检查报告模板，所有Sheet的拟制、审核、检查签署日期均为空白（"年月日"占位符），且文件名含PT3SBT与内容型号不一致，属于标签审核文件未完成签署及型号标识混乱的受控质量问题。

- Finding ID：`MR-0036`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），文件名为PT3SBT标签审核表，但内容中Sheet"标签报告模板-美"对应PT2L（美亚），Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"对应PT9L，文件名与部分内容型号不一致，存在型号混用风险。更关键的是，所有Sheet中的拟制、审核、检查签署日期均为"年月日"空白占位符，表明标签审核活动从未被正式签署确认。标签审核表是医疗器械上市前的重要合规文件，签署缺失意味着审核活动无法被证明已实际执行，构成P1级受控合规问题。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:68` ## Sheet: 标签报告模板 -简版

### 37. PT3SBT标签审核表（Stage 11正式文件）中包含PT2L（美亚）和PT9L的标签检查报告模板，所有Sheet的拟制、审核、检查签署日期均为空白（"年月日"占位符），且文件名含PT3SBT与内容型号不一致，属于标签审核文件未完成签署及型号标识混乱的受控质量问题。

- Finding ID：`MR-0037`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该文件位于Stage 11主审范围（primary_scope=true），文件名为PT3SBT标签审核表，但内容中Sheet"标签报告模板-美"对应PT2L（美亚），Sheet"标签报告模板-美(2)"、"标签报告模板-简版"、"标签报告模板-欧美"对应PT9L，文件名与部分内容型号不一致，存在型号混用风险。更关键的是，所有Sheet中的拟制、审核、检查签署日期均为"年月日"空白占位符，表明标签审核活动从未被正式签署确认。标签审核表是医疗器械上市前的重要合规文件，签署缺失意味着审核活动无法被证明已实际执行，构成P1级受控合规问题。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:101` ## Sheet: 标签报告模板 -欧美

### 38. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0038`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:156` \|  \| – the date of manufacture or use by date, if applicable. – 如果适用，生产日期或使用截止日期。 The serial number, lot or batch identifier, and the date of manufacture may be provided in a hum

### 39. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0039`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:156` \|  \| – the date of manufacture or use by date, if applicable. – 如果适用，生产日期或使用截止日期。 The serial number, lot or batch identifier, and the date of manufacture may be provided in a hum

### 40. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0040`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:161` \|  \| When consulting the ACCOMPANYING DOCUMENTS is a mandatory action, safety sign IEC 60878 Safety 01 (see Table D.2, safety sign 10) shall be used instead of symbol ISO 7000-16

### 41. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0041`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:161` \|  \| When consulting the ACCOMPANYING DOCUMENTS is a mandatory action, safety sign IEC 60878 Safety 01 (see Table D.2, safety sign 10) shall be used instead of symbol ISO 7000-16

### 42. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0042`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:186` \|  \| ME EQUIPMENT or its parts shall be marked with a symbol, using the letters IP followed by the designations described in IEC 60529, according to the classification in 6.3 (se

### 43. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0043`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:186` \|  \| ME EQUIPMENT or its parts shall be marked with a symbol, using the letters IP followed by the designations described in IEC 60529, according to the classification in 6.3 (se

### 44. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0044`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:189` \|  \| TYPE B APPLIED PARTS with symbol IEC 60417-5840,/B型应用部分以IEC60417-5840符号标记（DB:2002-10全部） \| NA \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_010.png](PT3SBT标签审核表（海外更新）.vi

### 45. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0045`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:189` \|  \| TYPE B APPLIED PARTS with symbol IEC 60417-5840,/B型应用部分以IEC60417-5840符号标记（DB:2002-10全部） \| NA \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_010.png](PT3SBT标签审核表（海外更新）.vi

### 46. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0046`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:196` \| 7.2.11 \| 符号Symbols \| —— \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_011.png](PT3SBT标签审核表（海外更新）.via_xlsx_assets/PT3SBT标签审核表（海外更新）_image_011.png) \| —— \|

### 47. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0047`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:196` \| 7.2.11 \| 符号Symbols \| —— \| —— \| —— \| —— \| —— ![PT3SBT标签审核表（海外更新）_image_011.png](PT3SBT标签审核表（海外更新）.via_xlsx_assets/PT3SBT标签审核表（海外更新）_image_011.png) \| —— \|

### 48. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0048`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:280` \|  \| For mains-operated ME EQUIPMENT with an additional power source not automatically maintained in a fully usable condition, the instructions for use shall include a warning st

### 49. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0049`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:280` \|  \| For mains-operated ME EQUIPMENT with an additional power source not automatically maintained in a fully usable condition, the instructions for use shall include a warning st

### 50. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0050`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:282` \|  \| If an INTERNAL ELECTRICAL POWER SOURCE is replaceable, the instructions for use shall state its specification./如果内部电源是可更换的，使用说明书应陈述其规格。 \| A \| 检查说明书是否有此描述 \| OK \|  \| Prod

### 51. PT3SBT标签审核表（海外更新）文件内容实际引用PT2L型号数据，存在型号错误引用的实质性合规缺陷

- Finding ID：`MR-0051`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：文件标题为'PT3SBT标签审核表（海外更新）'，位于Stage 11正式T1样机目录（primary_scope=true），但文件内容中产品型号填写为'PT2L'，项目编号为'2020-DEV01'，产品名称为'红外体温计'，文件编号均以'PT2L-'开头（PT2L-SMSP09、PT2L-CBZP07、PT2L-F96、PT2L-F97），检查记录引用'PT2L(美亚)-ZXBQ01 V1.0'等。PT3SBT为腕式血压计，PT2L为红外体温计，两者为完全不同的产品类别。该标签审核表实质上是PT2L的标签审核内容被错误地放入PT3SBT文件中，或文件内容未更新为PT3SBT对应内容，导致PT3SBT缺乏有效的标签合规审核证据。这是正式DHF文件中的实质性型号混用缺陷，影响标签合规证据链完整性。
- 证据：
  - `11 T1样机\PT3SBT标签审核表（海外更新）.via_xlsx.clean.md:282` \|  \| If an INTERNAL ELECTRICAL POWER SOURCE is replaceable, the instructions for use shall state its specification./如果内部电源是可更换的，使用说明书应陈述其规格。 \| A \| 检查说明书是否有此描述 \| OK \|  \| Prod

### 52. PT9L正式BOM（EBOM和T1样机BOM）中PCB图号引用了PT9C型号编号（PT9C-CNTP01 V1.0），构成异型号零件编号污染受控BOM。

- Finding ID：`MR-0052`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0095和MF-0096均为primary_scope=true的正式受控BOM文件（PT9L-EBOM01 V1.0和PT9L-T1EB01 V1.0），两份文件第50行均出现PCB图号"PT9C-CNTP01 V1.0"，该图号前缀明确为PT9C而非PT9L。在正式受控BOM中，零件图号应与目标产品型号一致或有明确的共用件说明。当前证据中无任何共用件声明或跨型号引用说明，属于异型号编号直接写入PT9L正式BOM，影响产品身份证据链完整性，应予confirm。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-EBOM01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 53. PT9L正式BOM（EBOM和T1样机BOM）中PCB图号引用了PT9C型号编号（PT9C-CNTP01 V1.0），构成异型号零件编号污染受控BOM。

- Finding ID：`MR-0053`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0095和MF-0096均为primary_scope=true的正式受控BOM文件（PT9L-EBOM01 V1.0和PT9L-T1EB01 V1.0），两份文件第50行均出现PCB图号"PT9C-CNTP01 V1.0"，该图号前缀明确为PT9C而非PT9L。在正式受控BOM中，零件图号应与目标产品型号一致或有明确的共用件说明。当前证据中无任何共用件声明或跨型号引用说明，属于异型号编号直接写入PT9L正式BOM，影响产品身份证据链完整性，应予confirm。
- 证据：
  - `11 T1样机\机芯类组件清单PT9L-T1EB01 V1.0.via_xlsx.clean.md:50` \| 2 \| PCB \| K0118000084609A1106 \| FR4 \| PT9C-CNTP01 V1.0 \|  \|  \| 1 \| PCB \| √ \| C \|  \|  \|

### 54. PT9L设计验证报告（正式文件）中存在名为"血压计法规标准清单20160719"的Sheet，该Sheet名未更新为PT9L专属标识，暗示文件模板来源于旧版通用血压计模板且未完成产品身份转换。

- Finding ID：`MR-0054`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0097所在文件为primary_scope=true的正式设计验证报告（Stage 11），Sheet名"血压计法规标准清单20160719"中的日期"20160719"与PT9L项目时间线不符，且未包含PT9L型号标识，表明该Sheet系从旧型号或通用模板直接沿用，未完成产品身份更新。设计验证报告作为核心DHF文件，其内部Sheet名称应明确对应PT9L，否则影响法规符合性证据的可追溯性，予以confirm。
- 证据：
  - `11 T1样机\设计验证报告E0 23.11\设计验证报告-通用要求和法规部分E0 20210927 23.11.via_xlsx.clean.md:127` ## Sheet: 血压计法规标准清单20160719

### 55. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0055`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:26` \| 3 \| 接口板PCB图 \| Top Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 56. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0056`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:27` \| 3 \| 接口板PCB图 \| Top Overlay 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 57. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0057`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:28` \| 3 \| 接口板PCB图 \| Bottom Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 58. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0058`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:29` \| 3 \| 接口板PCB图 \| Bottom Overlay 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 59. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0059`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:30` \| 3 \| 接口板PCB图 \| Drill Layer 层 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 60. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0060`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:31` \| 3 \| 接口板PCB图 \| 拼板示意图(顶层) \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 61. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0061`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:32` \| 3 \| 接口板PCB图 \| 拼板示意图(底层) \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 62. PT9L正式设计输出清单一（Stage 12）中接口板PCB图（序号3）全部8个图层条目均引用PT9C-CNTP01 V1.0作为文件编号，缺乏共用件声明或跨型号借用评审记录，构成产品身份污染。

- Finding ID：`MR-0062`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0143至MF-0150均位于Stage 12 primary_scope=true的正式设计输出清单文件中。同一清单内序号2主板PCB图全部使用PT9L-HFMP01前缀，序号3接口板PCB图全部8个图层（Top Layer、Top Overlay、Bottom Layer、Bottom Overlay、Drill Layer、拼板顶层、拼板底层、T-Z1-P14）却统一引用PT9C-CNTP01 V1.0，型号前缀与主审产品PT9L不一致。在当前全部证据中未发现任何共用件评审记录、设计借用声明或型号转换说明可解释该引用的受控合理性。正式设计输出清单中列入异型号文件编号而无受控说明，属于文件受控缺陷和产品身份混淆，证据充分，予以confirm。
- 证据：
  - `12 设计输出（含01、02）\PT9L-设计输出清单一\设计输出清单一\设计输出清单一.via_xlsx.clean.md:33` \| 3 \| 接口板PCB图 \| T-Z1-P14 \|  \|  \| PT9C-CNTP01 V1.0 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 63. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0063`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\37ed31b4835c1e57463e2ca2628ef51.via_xlsx.clean.md:26` \| 6 \| 防拆签 \| T040800073941030093 \| PET \|  \| PT3-F21 \|  \|  \| PT3 \|  \| 2 \|  \| √ \| C \|  \|  \|

### 64. PT9L包装BOM及总装BOM中多处引用PT3型号零部件（PT3-F21、PT3-P10、PT3-M02、PT3-M01），型号归属明确标注为PT3，与MC-CLUSTER-0032同源，构成跨型号共用件引用问题。

- Finding ID：`MR-0064`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0152（PT9L包装BOM）、MF-0197、MF-0198、MF-0199（总装类组件清单PT9L-ABOM01 V1.0）均为Stage 12 primary_scope=true的正式受控BOM文件。防拆签PT3-F21（型号归属PT3）、双联弹簧PT3-P10（型号归属PT3）、金属套PT3-M02（型号归属PT3）、压块PT3-M01（型号归属PT3）在PT9L正式BOM中明确标注来源型号为PT3。这与MC-CLUSTER-0032的问题性质相同，均为PT9L正式BOM中引用PT3型号零部件且未见共用件受控说明。属于正式文件中的实质性产品身份问题，应confirm。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\PT9L包装BOM.via_xlsx.clean.md:19` \| 6 \| 防拆签 \| T040800073941030093 \| PET \| PT3-F21 \| PT3 \|  \| 2 \|  \| √ \| C \|  \|

### 65. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0065`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 66. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0066`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:1` <!-- 主源 = PDF; SKILL_2D_Drawing_Reading; 2026-05-14 自动生成模板 + 待填 -->

### 67. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0067`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:2` # T040800073941030093-PT3-F21 2D 图读图报告

### 68. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0068`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:4` > 源文件：`T040800073941030093-PT3-F21.pdf`（PDF 尺寸 741×488 pt，文字层字符 < 400，矢量图纸）。

### 69. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0069`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:12` ![T040800073941030093-PT3-F21 概览](_assets/T040800073941030093-PT3-F21/overview.png)

### 70. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0070`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:20` \| **Drawing NO.** \| （待填 - 见右下标题栏） \|

### 71. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0071`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:21` \| **Part name** \| （待填 - 见右下标题栏中文零件名） \|

### 72. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0072`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:22` \| **Pro material** \| （待填） \|

### 73. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0073`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:23` \| **Surf dispose** \| （待填） \|

### 74. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0074`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:24` \| **Scale** \| （待填） \|

### 75. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0075`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:25` \| **Tolerance** \| （待填 - 见标题栏 Tolerance 表） \|

### 76. Stage 12主审范围设计输出清单二中PT3包装图纸自动读图报告标题栏关键字段全部为"待填"，设计输出文件信息未提取完整，构成实质性文件受控缺陷

- Finding ID：`MR-0076`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），文件路径为"12 设计输出（含01、02）\\设计输出清单二\\包装\\T040800073941030093-PT3-F21.pdf.md"。文件头注释明确标注"自动生成模板 + 待填"，且标题栏A级字段Drawing NO.、Part name、Pro material、Surf dispose、Scale、Tolerance、Edition、Model NO.均为"（待填）"占位符，未完成实际内容提取。这些字段是图纸受控的核心标识信息（图号、零件名、材料、版次、型号等），全部缺失意味着该设计输出文件的可追溯性和受控完整性无法验证，属于实质性DHF设计输出受控问题。9个候选均指向同一文件的不同待填字段，集中确认。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:26` \| **Edition** \| （待填） \|

### 77. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0077`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:89` \| ![r0c0](_assets/T040800073941030093-PT3-F21/r0c0.png) \| ![r0c1](_assets/T040800073941030093-PT3-F21/r0c1.png) \|

### 78. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0078`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:90` \| ![r1c0](_assets/T040800073941030093-PT3-F21/r1c0.png) \| ![r1c1](_assets/T040800073941030093-PT3-F21/r1c1.png) \|

### 79. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0079`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:96` - 源 PDF：`T040800073941030093-PT3-F21.pdf`

### 80. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0080`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\包装\T040800073941030093-PT3-F21.pdf.md:97` - 视觉块图：`_assets/T040800073941030093-PT3-F21/`（4 张 PNG，300 DPI）

### 81. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0081`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:6` > **关联**：[疑点表 §4.1](../../../../wiki/drawings/pt9l-2d-audit-doubts.md#41-75cee0-散热器金属套图号-5b44cgxt-001) **75CEE0 黄铜套 2m 跌落要求** 的配合件；[疑点表 §6.3 新增](#疑点新增) 总装图 BOM 编号 13 PT3-M01 = 本图

### 82. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0082`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:28` **iHealth 内部图号映射**：根据 [总装图 BOM](PT9L-总装图-v1.0-20240627.pdf.md) 编号 13，本件在 PT9L BOM 中以 **PT3-M01** 入账（"压块"）。

### 83. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0083`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:98` - **PT9L BOM 中位置**：[总装图序号 13 (PT3-M01)](PT9L-总装图-v1.0-20240627.pdf.md)

### 84. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0084`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:99` - **配合 75CEE0 在 BOM 中位置**：序号 14 (PT3-M03)

### 85. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0085`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:108` \| 2 \| **FDIR-V14 = PT3-M01？**（Famidoc 图号 = iHealth 内部 BOM 号） \| 是 \|

### 86. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0086`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:112` \| 6 \| iHealth 内部是否有"压块"独立图（带 PT3-M01 图号）补归档 \| 推测无 \|

### 87. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0087`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:120` - **设计日期**：2017-06-28（早于 PT9L 项目，PT9L 沿用 PT3 系列散热器组件）

### 88. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0088`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\FDIR-V14_散热器压块_REV01_0714.pdf.md:122` - **供应商**：**Famidoc**（深圳法米德 / 厦门法米德医疗器械有限公司，PT3 散热器组件供应商）

### 89. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0089`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:1` # PT3 双联弹簧 REV01 (V1.0) 2D 图读图报告

### 90. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0090`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:3` > **来源 PDF**：`02_RnD_DHF/PT9L DHF-历史文件/设计输出/设计输出清单二/图纸/PT3_双联弹簧_REV01.pdf`

### 91. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0091`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:6` > **共用件**：**PT3 项目原件**，被 PT9L DHF 借用归档（外购件 / 设计参照）

### 92. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0092`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:14` \| **Drawing NO.** \| **PT3-P10** \|

### 93. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0093`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:17` \| **Model NO.** \| **PT3**（注：归档于 PT9L DHF，实为 PT3 项目原件） \|

### 94. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0094`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:80` - 与正极 PT5-M02 / 负极 PT5-M03 **功能等价**，但合二为一（PT3 项目使用，PT9L 借用归档）

### 95. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0095`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:81` - **PT9L 实际装配**：以分离的 PT5-M02 + PT5-M03 为准（详见 wiki 主页 §2.4），PT3-P10 双联弹簧**不一定**进入 PT9L 量产 BOM

### 96. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0096`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT3_双联弹簧_REV01.pdf.md:89` \| 1 \| PT9L 量产 BOM 是否使用 PT3-P10 双联弹簧？还是分离的 PT5-M02 + M03？ \| 分离件（PT5 系列） \|

### 97. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0097`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:42` \| 20 \| **PT3-P10** \| **双连弹簧** \| 1 \|

### 98. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0098`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:48` \| 14 \| **PT3-M03** \| **金属套**（=75CEE0 黄铜套？） \| 1 \|

### 99. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0099`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:49` \| 13 \| **PT3-M01** \| **压块**（=散热器压块 FDIR-V14？） \| 1 \|

### 100. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0100`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:74` 6. **散热组**：压块 (13, PT3-M01) + 金属套 (14, PT3-M03)

### 101. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0101`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:77` 9. **电池组**：电池盖 (18, T-Z1-P04) + 7# 碱性电池 × 2 (19) + 双联弹簧 (20, PT3-P10) + 负极弹簧 (21, PT5-M03) + 正极弹簧 (22, PT5-M02) + 螺钉 M2X5 × 3 (23)

### 102. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0102`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:93` \| **图号格式** \| T-Z1-PXX（结构件） / PT3-MXX（散热器 / 双联弹簧借用 PT3） / PT5-MXX（弹簧借用 PT5） / PT9L-LXX（液晶专属） ✓ \|

### 103. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0103`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:108` ### 6.2 金属套（14）= PT3-M03 vs 75CEE0（外购）

### 104. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0104`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\PT9L-总装图-v1.0-20240627.pdf.md:110` - 总装图 BOM 中 **金属套 = PT3-M03**（PT3 项目原件号）

### 105. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0105`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\正极弹簧PT5-M02.pdf.md:96` \| 4 \| 与 PT3 双联弹簧 REV01 的功能区别（PT3 为双联，PT5/PT9L 为分离的正/负 2 件） \| — \|

### 106. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0106`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\图纸\负极弹簧PT5-M03.pdf.md:116` - **关联**：[正极弹簧 PT5-M02](正极弹簧PT5-M02.pdf.md)、[PT3 双联弹簧 REV01](PT3_双联弹簧_REV01.pdf.md)、[wiki/drawings/pt9l-drawings.md §2.4](../../../../wiki/drawings/pt9l-drawings.md)

### 107. PT9L包装BOM及总装BOM中多处引用PT3型号零部件（PT3-F21、PT3-P10、PT3-M02、PT3-M01），型号归属明确标注为PT3，与MC-CLUSTER-0032同源，构成跨型号共用件引用问题。

- Finding ID：`MR-0107`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0152（PT9L包装BOM）、MF-0197、MF-0198、MF-0199（总装类组件清单PT9L-ABOM01 V1.0）均为Stage 12 primary_scope=true的正式受控BOM文件。防拆签PT3-F21（型号归属PT3）、双联弹簧PT3-P10（型号归属PT3）、金属套PT3-M02（型号归属PT3）、压块PT3-M01（型号归属PT3）在PT9L正式BOM中明确标注来源型号为PT3。这与MC-CLUSTER-0032的问题性质相同，均为PT9L正式BOM中引用PT3型号零部件且未见共用件受控说明。属于正式文件中的实质性产品身份问题，应confirm。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:28` \| 15 \| 双联弹簧 \| T030100000482550143 \| 0.5mm弹簧钢 \| PT3-P10 \| PT3 \|  \| 1 \|  \| √ \| C \|  \|  \|

### 108. PT9L包装BOM及总装BOM中多处引用PT3型号零部件（PT3-F21、PT3-P10、PT3-M02、PT3-M01），型号归属明确标注为PT3，与MC-CLUSTER-0032同源，构成跨型号共用件引用问题。

- Finding ID：`MR-0108`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0152（PT9L包装BOM）、MF-0197、MF-0198、MF-0199（总装类组件清单PT9L-ABOM01 V1.0）均为Stage 12 primary_scope=true的正式受控BOM文件。防拆签PT3-F21（型号归属PT3）、双联弹簧PT3-P10（型号归属PT3）、金属套PT3-M02（型号归属PT3）、压块PT3-M01（型号归属PT3）在PT9L正式BOM中明确标注来源型号为PT3。这与MC-CLUSTER-0032的问题性质相同，均为PT9L正式BOM中引用PT3型号零部件且未见共用件受控说明。属于正式文件中的实质性产品身份问题，应confirm。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:35` \| 22 \| 金属套 \| T030100000507180765 \| 黄铜 \| PT3-M02 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|

### 109. PT9L包装BOM及总装BOM中多处引用PT3型号零部件（PT3-F21、PT3-P10、PT3-M02、PT3-M01），型号归属明确标注为PT3，与MC-CLUSTER-0032同源，构成跨型号共用件引用问题。

- Finding ID：`MR-0109`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0152（PT9L包装BOM）、MF-0197、MF-0198、MF-0199（总装类组件清单PT9L-ABOM01 V1.0）均为Stage 12 primary_scope=true的正式受控BOM文件。防拆签PT3-F21（型号归属PT3）、双联弹簧PT3-P10（型号归属PT3）、金属套PT3-M02（型号归属PT3）、压块PT3-M01（型号归属PT3）在PT9L正式BOM中明确标注来源型号为PT3。这与MC-CLUSTER-0032的问题性质相同，均为PT9L正式BOM中引用PT3型号零部件且未见共用件受控说明。属于正式文件中的实质性产品身份问题，应confirm。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\总装类组件清单PT9L-ABOM01 V1.0.via_xlsx.clean.md:36` \| 23 \| 压块 \| T030100000497180765 \| 黄铜 \| PT3-M01 \| PT3 \|  \| 1 \|  \| √ \| B \|  \|  \|

### 110. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0110`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:35` \| 15 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 111. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0111`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:38` \| 18 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 112. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0112`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:39` \| 19 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 113. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0113`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:63` \| 32 \| PT3总装类组件清单 \| PT9L-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 114. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0114`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:139` \| 14 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 115. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0115`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:147` \| 22 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 116. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0116`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:148` \| 23 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 117. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0117`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:173` \| 38 \| 防拆签 \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 118. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0118`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:185` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 119. Stage 12主审范围设计输出清单二中PT3SBT参考Sheet的提交、审核、批准日期及签署全部空白，构成正式文件受控签署缺失问题

- Finding ID：`MR-0119`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），两个候选（MF-0211、MF-0226）分别来自设计输出清单二的两个版本文件，均指向Sheet"PT3参考"中产品型号PT3SBT的签署行："提交: 年 月 日 审核: 年 月 日 批准: 年 月 日"——三项签署栏均为空白占位符，未填写实际日期和签署人。设计输出清单二作为DHF核心受控文件，其提交/审核/批准签署是文件受控的必要条件。即使该Sheet标注为"PT3参考"，其出现在正式设计输出清单二文件中且签署栏空白，仍构成文件受控完整性缺陷，需要确认是否为有效参考页或应完成签署。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:237` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日

### 120. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0120`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:261` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 121. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0121`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:262` \| 15 \| 胶垫 \| PT3SBT-P02 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 122. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0122`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:270` \| 19 \| 装配说明 \| PT3SBT（国内）-ZPSM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 123. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0123`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:291` \| 33 \| PT3总装类组件清单 \| PT3SBT-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 124. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0124`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:293` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 125. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0125`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:35` \| 15 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 126. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0126`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:38` \| 18 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 127. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0127`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:39` \| 19 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 128. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0128`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:56` \| 28 \| 防拆签 \|  \|  \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 129. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0129`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:141` \| 14 \| 双联弹簧 \|  \|  \| PT3-P10 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 130. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0130`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:149` \| 22 \| 金属套 \|  \|  \| PT3-M03 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 131. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0131`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:150` \| 23 \| 压块 \|  \|  \| PT3-M01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 132. PT9L正式设计输出清单二（BOM及设计输出清单）中多处引用PT3型号零部件（防拆签PT3-F21、双联弹簧PT3-P10、金属套PT3-M02、压块PT3-M01等），且型号归属列明确标注为"PT3"，构成跨型号共用件引用，需确认是否有正式共用件受控说明。

- Finding ID：`MR-0132`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0151（设计输出清单二）和MF-0152（PT9L包装BOM）均为Stage 12 primary_scope=true的正式受控文件。其中防拆签（T040800073941030093，PT3-F21，型号归属PT3）、双联弹簧（T030100000482550143，PT3-P10，型号归属PT3）、金属套（T030100000507180765，PT3-M02，型号归属PT3）、压块（T030100000497180765，PT3-M01，型号归属PT3）等多个零部件在PT9L的BOM中明确标注来源型号为PT3。这些零部件的型号归属列直接写"PT3"而非"PT9L"，说明这些是从PT3型号借用的共用件，但在PT9L DHF中未见对应的共用件声明或设计借用评审记录。candidate_count=50，影响范围广，且涉及包装和结构件，属于实质性产品身份问题，应confirm并要求补充共用件受控说明。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:175` \| 38 \| 防拆签 \| PT3-F21 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 133. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0133`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:187` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 134. Stage 12主审范围设计输出清单二中PT3SBT参考Sheet的提交、审核、批准日期及签署全部空白，构成正式文件受控签署缺失问题

- Finding ID：`MR-0134`
- 二审 Agent：Document Control Agent
- 严重度：`P1`
- 二审理由：该cluster位于Stage 12主审范围（primary_scope=true），两个候选（MF-0211、MF-0226）分别来自设计输出清单二的两个版本文件，均指向Sheet"PT3参考"中产品型号PT3SBT的签署行："提交: 年 月 日 审核: 年 月 日 批准: 年 月 日"——三项签署栏均为空白占位符，未填写实际日期和签署人。设计输出清单二作为DHF核心受控文件，其提交/审核/批准签署是文件受控的必要条件。即使该Sheet标注为"PT3参考"，其出现在正式设计输出清单二文件中且签署栏空白，仍构成文件受控完整性缺陷，需要确认是否为有效参考页或应完成签署。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:239` 产品型号:PT3SBT 提交部门:智能产品部 提交: 年 月 日 审核: 年 月 日

### 135. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0135`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:263` \| 14 \| 收纳盒 \| PT3SBT-P01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 136. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0136`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:264` \| 15 \| 胶垫 \| PT3SBT-P02 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 137. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0137`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:272` \| 19 \| 装配说明 \| PT3SBT（国内）-ZPSM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 138. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0138`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:293` \| 33 \| PT3总装类组件清单 \| PT3SBT-ABOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 139. PT9L设计输出清单二中包含PT3SBT型号的完整设计输出体系（BOM文件编号PT3SBT-PBOM01、PT3SBT-ABOM01及零部件PT3SBT-P01、PT3SBT-P02），该清单同时覆盖PT9L和PT3SBT两个产品，存在产品身份混淆或文件归档错误的重大风险。

- Finding ID：`MR-0139`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0210、MF-0212、MF-0213、MF-0214、MF-0215、MF-0216（设计输出清单二E0）及MF-0225、MF-0227等均位于Stage 12 primary_scope=true的正式设计输出清单二中。该清单文件路径为"12 设计输出（含01、02）\\设计输出清单二"，应属于PT9L的设计输出清单，但其中明确列出了PT3SBT的独立BOM文件（PT3SBT-PBOM01 V1.0为PT3包装类组件清单、PT3SBT-ABOM01 V1.0为PT3总装类组件清单）以及PT3SBT专属零部件（收纳盒PT3SBT-P01、胶垫PT3SBT-P02、装配说明PT3SBT（国内）-ZPSM01）。这表明PT9L的设计输出清单二实际上是PT9L与PT3SBT的合并清单，或PT3SBT的设计输出被错误归入PT9L DHF。无论哪种情况，均构成产品身份污染：若为合并清单，需明确说明PT9L与PT3SBT的关系及共用范围；若为误归档，则PT9L DHF中存在外来产品的设计输出文件。candidate_count=12，影响范围覆盖BOM和装配说明，严重性定为P1。
- 证据：
  - `12 设计输出（含01、02）\设计输出清单二\设计输出清单二E0.via_xlsx.clean.md:295` \| 34 \| PT3包装类组件清单 \| PT3SBT-PBOM01 \| V1.0 \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|  \|

### 140. 正式设计确认文件（Stage 18主范围）以PT9C命名，且用户测试计划标题亦为PT9C，构成PT9L DHF产品身份污染。

- Finding ID：`MR-0140`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0232所在文件路径为'18 设计确认\\PT9C设计确认E0 23.11.via_xlsx.clean.md'，文件标题直接为'PT9C设计确认E0 23.11'，primary_scope=true，属于Stage 18正式主审范围内的设计确认文件，文件名及标题均以PT9C标识，而非PT9L。MF-0276所在文件'用户现场测试计划 PT9C V1.0'标题亦为PT9C，但文件编号行显示'PT9L-RYCJ01 V1.0'，说明文件内容编号已更新为PT9L，但标题仍残留PT9C，存在型号不一致问题。两份文件均在正式设计确认目录下，非废案/备份，属于实质性产品身份不一致，需确认文件是否为PT9C遗留文件误归入PT9L DHF，或标题未同步更新，影响PT9L DHF证据链完整性。
- 证据：
  - `18 设计确认\PT9C设计确认E0  23.11.via_xlsx.clean.md:2` # PT9C设计确认E0  23.11

### 141. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Finding ID：`MR-0141`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:3` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0

### 142. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Finding ID：`MR-0142`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:14` ![第 1 页原始整页图](_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_1.png)

### 143. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Finding ID：`MR-0143`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:88` ![第 3 页原始整页图](_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_3.png)

### 144. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Finding ID：`MR-0144`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:113` - 源 PDF：`02_RnD_DHF/PT9L DHF-历史文件/设计确认/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf`

### 145. Stage 18正式设计确认目录下存在文件名同时含PT9L与PT2L（美亚）的Checklist，文件编号虽为PT9L-UETR01 V1.0，但PT2L作为独立型号标识出现在正式受控文件标题中，且该文件源路径位于历史文件子目录，其是否已被当前受控版本替代及PT2L身份未经文件明确说明，构成可确认的文件受控与产品身份标识缺陷。

- Finding ID：`MR-0145`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0233至MF-0237均来自Stage 18 primary_scope=true的正式设计确认目录（18 设计确认\\），文件标题'PT9L Checklist of (EN 60601-1-6...) PT2L（美亚）-UETR01 V1.0'中PT2L以独立型号形式出现，而非仅作为市场后缀说明。文件编号DN字段为PT9L-UETR01 V1.0，但源路径显示该文件实际存储于'PT9L DHF-历史文件/设计确认/'子目录，说明该文件属于历史版本归档，而非当前受控版本。在正式Stage 18目录下存放历史文件目录下的文件，且文件标题中PT2L身份未经任何受控说明（如共用件声明、市场版本对应关系说明），构成文件受控管理缺陷。同类证据（03风险分析\\2L风险改-历史文件）亦显示PT2L为独立历史型号系列。当前证据足以证明正式DHF目录中存在历史/异型号文件混入且缺乏受控说明，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.pdf.md:114` - 证据原图（签字/盖章/照片页）：`_assets/PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0/page_*.png`

### 146. Stage 18正式设计确认目录下PT2L（美亚）Checklist的clean.md版本与MC-CLUSTER-0040同源，同样存在PT2L型号标识混入正式文件标题且缺乏受控说明的问题。

- Finding ID：`MR-0146`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：MF-0238为MC-CLUSTER-0040所涉同一文件的via_lo_html.clean.md转换版本，primary_scope=true，位于Stage 18正式目录。文件标题同样含PT2L（美亚），文件编号DN字段为PT9L-UETR01 V1.0。与MC-CLUSTER-0040属于同一文件的不同格式版本，问题性质完全相同：正式DHF目录中存在历史/异型号文件且PT2L身份缺乏受控说明。依据与MC-CLUSTER-0040相同的裁决逻辑，予以confirm。
- 证据：
  - `18 设计确认\PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0.via_lo_html.clean.md:2` # PT9L Checklist of （ EN 60601-1-62010+A12015+A22021) PT2L（美亚）-UETR01 V1.0

### 147. 正式设计确认文件（Stage 18主范围）以PT9C命名，且用户测试计划标题亦为PT9C，构成PT9L DHF产品身份污染。

- Finding ID：`MR-0147`
- 二审 Agent：Product Identity Agent
- 严重度：`P1`
- 二审理由：MF-0232所在文件路径为'18 设计确认\\PT9C设计确认E0 23.11.via_xlsx.clean.md'，文件标题直接为'PT9C设计确认E0 23.11'，primary_scope=true，属于Stage 18正式主审范围内的设计确认文件，文件名及标题均以PT9C标识，而非PT9L。MF-0276所在文件'用户现场测试计划 PT9C V1.0'标题亦为PT9C，但文件编号行显示'PT9L-RYCJ01 V1.0'，说明文件内容编号已更新为PT9L，但标题仍残留PT9C，存在型号不一致问题。两份文件均在正式设计确认目录下，非废案/备份，属于实质性产品身份不一致，需确认文件是否为PT9C遗留文件误归入PT9L DHF，或标题未同步更新，影响PT9L DHF证据链完整性。
- 证据：
  - `18 设计确认\用户测试\用户现场测试计划 PT9C V1.0.via_lo_html.clean.md:2` # 用户现场测试计划 PT9C V1.0

### 148. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Finding ID：`MR-0148`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:577` \| 4.2 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Intended use and identification of characteristics related to cleaning analyzed and recorded \| P \|

### 149. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Finding ID：`MR-0149`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:578` \| 4.3 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Hazard analysis recorded \| P \|

### 150. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Finding ID：`MR-0150`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:579` \| 4.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk estimation recorded \| P \|

### 151. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Finding ID：`MR-0151`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:580` \| 5 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Risk evaluation recorded \| P \|

### 152. PT9L 正式外部测试报告中 ISO 14971 符合性验证表引用的风险管理报告文件编号为 PT9C-FXGB01 V1.0，与受审产品型号 PT9L 不符，导致风险管理合规证据链存在型号归属错误。

- Finding ID：`MR-0152`
- 二审 Agent：Regulatory Agent
- 严重度：`P1`
- 二审理由：证据来源为 PT9L 的正式外部测试报告（2025.02.12，primary_scope=true），属于正式主审范围文件。报告第 573–581 行的 ISO 14971 符合性结果表（RM RESULTS TABLE）在 Clause 4.2、4.3、4.4、5、6.4 共五处均将 'Risk Management Report (file No.: PT9C-FXGB01 V1.0)' 列为对应的 RMF 文件参考，而受审产品为 PT9L。PT9C 与 PT9L 为不同型号，若该风险管理报告并非 PT9L 的受控共用件或经正式转换认可的等效文件，则测试报告所声明的 ISO 14971 各条款通过（Verdict: P）均缺乏有效的 PT9L 专属风险管理文件支撑，构成实质性证据链断裂。此缺陷不属于合理历史引用或草稿范围，而是直接影响 PT9L DHF/DMR 中风险管理合规性的正式记录错误，严重程度定为 P1（主要合规证据缺陷，需提供 PT9L 对应受控风险管理报告或证明 PT9C 文件经正式授权适用于 PT9L）。
- 证据：
  - `实验报告\最终报告\2025.02.12 ETX202303-07-078-03 PT9L -2-56 报告-正式.pdf.md:581` \| 6.4 \| Risk Management Report ( file No.: PT9C-FXGB01 V1.0 ) \| Residual risk evaluated. \| P \|

### 153. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Finding ID：`MR-0153`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:104` \| 3 \| 测量误差 \| ≥35℃且≤42℃：±0.2℃，其它：±0.3℃ \|  \|

### 154. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Finding ID：`MR-0154`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:132` \| 11 \| 错误分类显示 \| □No \| ■错误种类：2种 （1、超出工作环境温度 2、超过量程 ） \|  \|  \|  \|

### 155. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Finding ID：`MR-0155`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:85` \| 8 \| 产品寿命 \| 见附件3：《客户需求书－性能规格部分》V1.0 \|  \|  \|

### 156. 客户需求书文件标题及文件名使用"血压计"，但内容实为红外额温计PT9L，存在产品品类标签与实际产品不符的身份污染问题。

- Finding ID：`MR-0156`
- 二审 Agent：Product Identity Agent
- 严重度：`P2`
- 二审理由：文件路径"客户需求书E0-血压计 23.6.via_xlsx.clean.md"及文件标题第2行均以"血压计"命名，但文件内容（PF-0001至PF-0004）描述的是红外测温、额头温度测量、温度显示范围32.0℃～42.9℃等额温计特征，与血压计产品类别完全不符。该文件位于Stage 01正式立项批准书目录，属于PT9L DHF正式受控范围。文件标题/命名中的"血压计"不是合理引用，而是品类标签错误，可能导致产品身份识别混淆，影响DHF证据链的产品一致性。
- 证据：
  - `01 立项批准书E0 23.11\客户需求书E0-血压计 23.6.via_xlsx.clean.md:6` ## Sheet: 历史版本记录
