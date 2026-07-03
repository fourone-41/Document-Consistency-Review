# 00 · 从这里开始（DHF/DMR 审核交接包 v2 · 自包含）

你好。本包是一套**医疗器械 DHF/DMR/注册 跨文档审核**的完整方法论 + 全部工具 + 全部 skill，目标:让你**不依赖任何原始对话,独立把一个新型号审一遍**,产出错误总表 + 可交互裁决报告,且**自己能证明没瞎报、没跳步**。

## ★ 第一步:只读一个文件
**`DHF-DMR审核-SKILL.md`** —— 这是总纲(orchestrator)。它规定全流程、调用本包其它 skill、并要求你结尾交《完成自检表》。**先读它,按它干。**

## 三条最重要的铁律(SKILL 里有详述,先记住)
1. **先核市场+品类,禁止默认**:每个型号的目标市场(中国NMPA/美国FDA/…)和品类,**必须从它自己的客户需求书读出来**(用 `skill/stage-01-dhf-check-skill`)。别假设别人是美版这个就是美版(这是真摔过的坑)。
2. **不许跳步 + 结尾交《完成自检表》**:每个算法/检查要么做(✅)、要么写明为什么不适用(⏭️)。最容易被偷工的是:机械层(残留/数值/表diff)、对抗证伪、Excel转2套、转换后查乱码。
3. **以本包 `skill/` + `tools/` 为权威**:转换用 `skill/conversion-toolkit` + 各格式 skill(**Excel 必须转2套**:结构通道+页面视觉通道);逐阶段查用 `skill/stage-01~11-dhf-check-skill`;DMR用 `skill/dmr-mfg-sop-check-skill`;写中文用 `tools/unicode_safe_write.py`,转换后跑 `tools/scan_text_integrity.py` 查乱码。

## 包里有什么
| 路径 | 作用 |
|---|---|
| `DHF-DMR审核-SKILL.md` | **总纲,先读这个**(强制流程+完成自检表) |
| `skill/` | **你的执行权威 skill 库**:working-method 总则 + conversion-toolkit + doc/docx/pdf/**xls(转2套)**/remaining-format + stage-01~11 逐阶段check + dmr-mfg-sop-check + drawing(2D/3D) |
| `tools/` | unicode_safe_write(安全写中文) + scan_text_integrity(扫乱码) |
| `dhf_audit_toolkit/` | Tier1/2 确定性算法:check_residue / check_params_numeric / check_table_diff / check_bom_crosswalk / dhf_pipeline |
| `scripts/` | verify_findings(证据核验) / audit_self_check(自检) / gen_report_review_html(裁决版HTML) / assemble_* / convert_m10(并行转换范例) |
| `_adjudications.csv` | 裁决库(已裁决误报,撞库防重报;PM每否一个加一行) |
| `docs/` | 方法与算法-详尽版(12万字深度) / V2双轴实战版 / 完整交接版runbook |
| `参考基线/` | 两个市场×品类示例:美国体温计 + 中国雾化器(照这个给新市场/品类建基线) |
| `品类参数槽位参考表.md` | 各品类该抽什么参数 + 串品类残留识别表 |

## 新型号一键启动 prompt(复制粘贴给 agent)
```
按 <本包>/DHF-DMR审核-SKILL.md 这个 skill,审核型号 <型号名>,原始件在 <原始件路径>。
要求:
1. 先加载 skill/SKILL.md 总则(喵/进度/批量转换闸门);
2. 先从该型号客户需求书读出"目标市场+品类",据此建法规基线(参照 参考基线/ 两个示例),禁止默认;
3. 转换用 skill/conversion-toolkit + 各格式 skill(Excel 转2套),转后跑 tools/scan_text_integrity 查乱码;
4. 逐阶段用 skill/stage-01~11-dhf-check-skill,DMR 用 dmr-mfg-sop-check-skill;
5. 机械层四脚本(残留/数值/表diff/对账)+ 对抗证伪 都要跑;
6. 出错误总表 + gen_report_review_html 裁决版HTML;
7. 跑 verify_findings 证据核验 + audit_self_check 自检;
8. 结尾交《完成自检表》,逐项 ✅/⏭️(理由);末尾回🐱。
```

## ★真·一句话全跑(主控 workflow,代码强制不跳步)
光"按 SKILL 做"是给 LLM 的指引,可能跳步。要**代码强制全跑**,用主控 workflow `run_full_audit.js`——它按顺序自动:侦察(读客户需求书定市场+品类+列单元)→ 逐单元并行审 → 跨单元对账 → **确定性层 run_audit + 自检硬闸门** → 汇总报告。agent 没有跳步余地;闸门有"必查"项会 exit 1。

**调用(在 Claude Code 里)——⚠️必须用"内联启动器",不能直接 `Workflow({scriptPath,args})`!**
> 踩过的坑:`Workflow({scriptPath, args})` 的 **args 不会注入**到脚本的 args 全局 → run_full_audit 默认 model="MODEL"+空路径 → Scout 乱找 → **审错型号**(PT9L 任务因此跑去审了 M10)。只有 `workflow(ref, args)` **函数**会把参数传给子工作流。

正确做法:给 Workflow 传一段**内联 script**(把参数硬编码进去,经 workflow() 传):
```
Workflow({ script:
  "export const meta={name:'launch',description:'启动器',phases:[{title:'run'}]}\n" +
  "phase('run')\n" +
  "const P={model:'<型号>', mdRoot:'<型号>_MD\\\\02_RnD_DHF或对应根 绝对路径', checkDir:'<型号>_CHECK 绝对路径', pkgDir:'<本包绝对路径>'," +
  " market:'', category:'',  /* 留空=让Scout从客户需求书侦察,别默认 */" +
  " baselinePath:'参考基线/对应基线.md 或留空让它建', foreign:'血压计,体温计,血糖仪,冲牙器...', models:'KD,BPM,PT3,PT5,...'}\n" +
  "return await workflow({scriptPath:'<本包绝对路径>/run_full_audit.js'}, P)"
})
```
run_full_audit.js 顶部有 guard:缺 model/mdRoot/checkDir 会直接 throw,不会默默审错。**resume 时**:resume 这个内联启动器(它已写死参数)即可,无需再传 args。
(前提:先按 skill/conversion-toolkit + xls-skill 把原始件转成 `<型号>_MD`。Finalize 偶发 API Overloaded 失败时,从 task output 取 result 的 {units,crosschecks} 手动 `assemble_audit.py`+`run_audit.py post` 补跑。)

## 其他 agent 能不能用?(诚实)
- **另一台机器/另一个 Claude Code agent**:✅ 能。把本包拷过去、改本机路径、转好 MD,然后用**内联启动器**(见上节,参数硬编码经 `workflow()` 传)跑全套。⚠️**不能**直接 `Workflow({scriptPath, args})`——args 不会传进去、会审错型号。脚本可移植,参数全走启动器。
- **非 Claude Code 的通用 agent**(没有 Workflow 引擎):⚠️ 用不了这个 workflow,但能**读 `DHF-DMR审核-SKILL.md` 按步做 + 手动跑 python 脚本**(`run_audit.py`/`dhf_audit_toolkit`/`verify_findings`/`audit_self_check` 都是普通 Python,任何环境能跑)。即:确定性层+闸门哪都能用;并行编排那层要 Claude Code。

## 两个落地提醒
1. **路径**:本包文档里的 `D:\AI_0415\03DHF\...` 是源机器路径,你这台几乎一定不同——**先把脚本顶部路径常量改成你本机的**(尤其 `dhf_audit_toolkit/dhf_pipeline.py` 的 BASE/MODELS、scripts 里的硬编码路径)。**别在脚本里硬编码中文路径**(用 manifest/Path/Unicode escape)。
2. **环境**:Windows + Office(.doc/.xls 要 Word/Excel COM);`pip install pymupdf openpyxl xlrd pillow pandas pywin32 pytesseract`(OCR 另需装 Tesseract + chi_sim/eng/osd 语言包);Workflow schema 字段名必须 ASCII。
3. **包内脚本说明**:`scripts/` 已含全部被引用脚本(转换 convert_pt9s/convert_m10、覆盖台账 coverage_ledger、汇总 assemble_*、报告 gen_report_*、自验证 verify_findings/audit_self_check、执行器 run_audit、图纸 prep_2d、PT9L wiki/转换辅助等);`dhf_audit_toolkit/` 含 Tier1/2 四脚本+pipeline;`skill/conversion-toolkit-skill/scripts/check_conversion_tools.py` 是环境就绪检查。**两个非实体**:`pytesseract`=pip 包(非本项目文件)、`generate_customer_requirements_vs_regulations_report.py`=stage-01 skill 里"每项目自己生成"的报告脚本示例名(不随包发)。

## 实证基准(对标你的复现度)
PT9L 191 / PT9S 169 / PT7 286 / **M10 199(中国NMPA雾化器,首个跨品类跨市场)**;证据有据率参考 76%~85%;对抗证伪毙约 1/4。

🐱
