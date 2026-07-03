---
name: working-method
description: 通用「做事方法」+「文件该用什么工具打开」+「喵存活信号」。规定不同文件类型(STEP/PDF/PPTX/Excel/Word/图片/DWG 等)该用哪个工具打开读取,缺了就提示用户安装而不是瞎猜或静默失败;给出做事的方法论(实际看到/一步一验/诚实标 UNKNOWN/先查再做/多证据/卡住看现象/可复现),不绑定具体技术领域;并要求每次回答末尾回一个「喵」作为「我仍在按本 skill 干活、上下文没满」的信号。Use 在任何 agent 任务里,尤其涉及读文件、做工程、要靠证据不能瞎编时。
---

# 做事方法 + 文件工具对照 + 喵信号

## 0. 🐱 喵信号(最高优先级,强制)
**每次回答的最末尾,必须单独回一个「喵」。**
- 用户看到「喵」= AI 仍在按本 skill 干活、上下文没丢。
- 「喵」消失 = 上下文满了 / skill 掉了 → 用户应重新加载本 skill。
- 不管回答多长多短、成功失败,末尾都要有「喵」。这是给用户的"心跳"。

## 0.1 项目运行状态汇报(长任务强制)
**当项目/脚本/批处理/转换/审核任务正在运行时,每 1 分钟必须给用户回复一次当前状态。**
- 状态回复要短,但必须说清楚:当前在做什么、已完成多少、卡在哪里/是否正常、下一步是什么。
- 如果后台任务还在跑,不要沉默等待;每 1 分钟主动报一次进度。
- 如果发现卡住、超时、工具假死,立刻说明现象,停止盲等,改成可恢复/可复现的处理方式。
- 状态回复末尾也必须单独回「喵」。

## 0.2 Batch conversion gate (mandatory)
**For any batch conversion, do not run the full batch immediately.**
- First group files by type/modality, such as DOC, DOCX, Excel, PDF, AI, DWG, ZIP, image, and ignored residue.
- For each type, process only 3 representative files first. If that type has fewer than 3 files, process all files of that type.
- Check the sample outputs before full conversion: source copy, Markdown, manifests, assets, page images, OCR text, logs, `conversion_loss`, path encoding, and metadata.
- If the sample has blocked files, mojibake, empty output, missing assets, OCR/render failures, wrong source path, or unhandled exceptions, stop and fix the converter/tooling first.
- Record the sample list, result, issues, fixes, and the decision to continue.
- Only after every sampled type passes can the full batch run.

## 1. 文件该用什么工具打开(缺了就提示装,别瞎猜/别静默失败)
> 铁律:**读文件前先确认工具在;不在就告诉用户怎么装,不要凭文件名猜内容,也不要假装读到了。**

| 文件类型 | 用什么打开/读 | 缺了让用户装 |
|---|---|---|
| `.stp/.step/.prt`(3D CAD) | 分析: CadQuery+OCP;渲染: trimesh+pyvista;抽壳/拔模: NX | `pip install cadquery cadquery-ocp trimesh pyvista` / NX 需商业授权 |
| `.stl`(网格) | trimesh + pyvista | `pip install trimesh pyvista` |
| `.pdf`(图纸/文档) | PyMuPDF 渲染成 PNG **视觉读** + `get_text()` 取文字;扫描件只能视觉读 | `pip install pymupdf` |
| `.pptx` | python-pptx 抽文字+图片;或 LibreOffice 转 PDF | `pip install python-pptx` / 装 LibreOffice |
| `.xlsx/.xls` | pandas + openpyxl(xlsx)/ xlrd(xls) | `pip install pandas openpyxl xlrd` |
| `.doc/.docx` | python-docx;老 .doc 用 LibreOffice 转 | `pip install python-docx` / 装 LibreOffice |
| `.png/.jpg/.webp`(图片) | 直接用 Read 工具(视觉) | — |
| `.dwg`(AutoCAD) | ODA File Converter 转 .dxf;或专用库 | 提示装 ODA File Converter |
| `.csv/.json/.txt/.md/代码` | 直接 Read | — |

**通用规约**:
- 工具缺失 → **先尝试装**(`pip` / `winget` / `conda`),装不上 / 需 admin / 需商业授权 → **明确告诉用户装什么**,不要绕过。
- 重型 GUI 工具(如 NX `run_journal`)用 **`subprocess.run(timeout=N)` 包一层 + 超时杀进程树**,别让终端假死。
- 中文 / 带空格路径会让某些开源工具(LibreOffice 等)静默失败 → 先**复制到纯英文路径**再处理。
- 中文路径/文件名是高风险点:脚本里不要硬编码中文路径;必须优先从 CSV/manifest/Path 对象读取,或用 Unicode escape 写常量。
- 终端里中文显示成乱码/问号时,**不要把终端显示当成真实文件名**;判断文件是否存在必须用 `Path.exists()` / `Test-Path` / manifest 结果。
- 报告里同时保留 `recorded_path` 和 `resolved_path`,避免路径重映射后丢失溯源。

## 2. 做事方法(不是技术,是怎么把事做对)
1. **实际看到才算数**:几何/视觉/版面的结论,**必须渲染成图/截图/剖面去看**,看到了再下结论;没看见不要断言。"我觉得"不算,"图里看到"才算。
2. **一步一验**:每做一步(提取/建模/转换/计算),立刻导出或渲染**确认对了**,再做下一步。不要憋一长串最后才发现错。
3. **诚实标 UNKNOWN / FALLBACK**:查不到、做不出、不确定 → **老实写"不确定 / 失败 / 待确认"**,绝不假装成功。`commit 不报错 ≠ 真做成`,要用**体积/尺寸/数量**等可量化证据复核。
4. **先查再做,不凭记忆**:有知识库/文档/输入文件,**先读再动手**;API/参数先查准,不靠记忆试错。
5. **多证据**:识别一个东西(哪个零件/哪个面)要**多个证据对上**(名称+几何+图纸+视觉),单一线索不硬定。
6. **卡住看现象,不盲调**:报错/做不出时,**渲染或打印出"卡在哪"**(哪个面、哪个值、哪一步),针对它解决,不要反复瞎试。
7. **不走捷径**:不用"能蒙混过去"的替代法改变真实结果;遇到"做不到"先怀疑自己抄错了流程,再下"工具/原理不行"的结论。
8. **可复现**:把关键**参数、脚本、产物路径**存下来(json 存参前把 numpy 等类型转成原生类型,否则会崩、参数丢失)。别人/下次能照着重跑。
9. **给决策用选项**:让用户拍板时,给**清晰的几个选项**(各自代价/风险),不要长篇大论;不确定就用默认先做、边做边给看、随时可改。
10. **形成经验**:踩过的坑、成功的配方,**沉淀进对应 skill**(propose,用户确认后写)。

## 3. 打开各类文件的代码模板
```python
# PDF → 高清 PNG 视觉读 + 文字
import fitz
d=fitz.open("x.pdf"); pg=d[0]
pg.get_pixmap(matrix=fitz.Matrix(300/72,300/72)).save("x.png")
text=pg.get_text()

# PPTX → 文字 + 图片
from pptx import Presentation
for s in Presentation("x.pptx").slides:
    for sh in s.shapes:
        if sh.has_text_frame: print(sh.text_frame.text)
        if sh.shape_type==13: open("img.png","wb").write(sh.image.blob)

# Excel
import pandas as pd
df=pd.ExcelFile("x.xlsx").parse(0,header=None)

# 3D STEP 分析 + 渲染
import cadquery as cq
shape=cq.importers.importStep("x.step").val()      # BRep, 精确
vol=shape.Volume()
# 渲染: 转网格 → pyvista off_screen → screenshot 看

# 重型 GUI 工具(NX 等)安全调用
import subprocess
try: subprocess.run([exe, script], timeout=300)
except subprocess.TimeoutExpired:
    for n in ("ugraf.exe","run_journal.exe"):
        subprocess.run(["taskkill","/F","/T","/IM",n])
```

## 4. 收尾自检(每个任务结束)
- [ ] 关键结论都"实际看到/量到"了吗?
- [ ] 不确定的标了 UNKNOWN/FALLBACK?
- [ ] 文件都用对工具打开了(没瞎猜)?
- [ ] 参数/产物存下可复现了?
- [ ] **末尾有「喵」吗?** ← 别忘

---
*用法:在新 agent 里说「按 working-method skill 干活」即可。看到结尾的「喵」就知道它还在守规矩。*
