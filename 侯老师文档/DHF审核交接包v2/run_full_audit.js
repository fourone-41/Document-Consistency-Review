// ⚠️启动方式(重要):不能用 Workflow({scriptPath:本文件, args:{...}}) —— 那样 args 不会注入到下面的 args 全局,
//   会默认 model="MODEL"+空路径, Scout 乱找审错型号(PT9L 曾因此跑去审 M10)。
// 正确:给 Workflow 传一段内联 script 当"启动器",里面硬编码参数 P, 然后 return await workflow({scriptPath:本文件}, P);
//   workflow(ref,args) 这个函数会把 P 注入为本脚本的 args 全局。resume 时 resume 那个启动器即可(已写死参数)。
// 真·全跑(2026-06-20升级):Scout → Units(读对应 stage skill) → Cross(5轴) → 图纸/代码分支(有就跑) → 对抗证伪(毙误报) → Finalize(assemble+自动table_diff+run_audit闸门)。
export const meta = {
  name: 'run-full-audit',
  description: 'DHF/DMR审核主控·真全跑:侦察→逐单元(调stage skill)→跨单元对账→图纸/代码分支→对抗证伪→Finalize(汇总+自动table_diff+run_audit硬闸门)。args:model/mdRoot/checkDir/pkgDir/market/category/baselinePath/foreign/models/rawRoot/codeRoot。经内联启动器+workflow()传参。',
  phases: [{title:'Scout侦察'},{title:'Units逐单元'},{title:'Cross跨单元'},{title:'图纸代码分支'},{title:'对抗证伪'},{title:'Finalize确定性+闸门'}],
}
const A = (typeof args==='object'&&args)?args:{}
if(!A.model || !A.mdRoot || !A.checkDir){
  throw new Error("run_full_audit 缺 args.model/mdRoot/checkDir。⚠️RESUME 时也必须重新传 args(用内联启动器)!否则会审错型号")
}
const MODEL=A.model, MD=A.mdRoot, CHECK=A.checkDir
const PKG=A.pkgDir||"D:\\AI_0415\\03DHF\\DHF审核交接包v2"
const SKILLD=PKG+"\\skill"
const MARKET=A.market||"", CAT=A.category||"", BASELINE=A.baselinePath||""
const FOREIGN=A.foreign||"", XMODELS=A.models||"", RAWROOT=A.rawRoot||"", CODEROOT=A.codeRoot||""
const SLOTREF=PKG+"\\品类参数槽位参考表.md", ADJ=PKG+"\\_adjudications.csv"

const RULES=`你在审 **${MODEL}**(品类:${CAT||"以侦察为准"} / 市场:${MARKET||"以侦察为准"})。先读基线:${BASELINE||"(空则按侦察市场+品类建)"};参数槽位:${SLOTREF};裁决库:${ADJ}。`+
`铁律:①只按本型号实际市场(其它市场标准非强制,正确裁剪对,反向当强制基准才真错)②下游≥上游③正文封闭(没写判NEI不编)④一致性≠正确性。`+
`已裁决误报别报:传感器焊点数vs线数不矛盾、静音拨动开关、一致性≠正确性。**evidence必摘逐字原文可grep。** 重点:串品类残留/模板残留他型号/参数放宽收窄/编号唯一/版本漂移/角色串联/法规该有却没有。`

const SCH_SCOUT={type:"object",additionalProperties:false,properties:{market:{type:"string"},category:{type:"string"},market_evidence:{type:"string"},
  units:{type:"array",items:{type:"object",additionalProperties:false,properties:{unit:{type:"string"},path:{type:"string"},stage_no:{type:"integer"}},required:["unit","path"]}}},required:["market","category","units"]}
const F_PROPS={id:{type:"string"},severity:{type:"string",enum:["critical","major","minor","待PM确认","NEI"]},type:{type:"string"},desc:{type:"string"},evidence:{type:"string"},suggest:{type:"string"},role:{type:"string"}}
const SCH1={type:"object",additionalProperties:false,properties:{unit:{type:"string"},files_read:{type:"integer"},sampled:{type:"string"},used_stage_skill:{type:"string"},
  parameters:{type:"array",items:{type:"object",additionalProperties:false,properties:{name:{type:"string"},value:{type:"string"},source_file:{type:"string"}},required:["name","value","source_file"]}},
  intra_findings:{type:"array",items:{type:"object",additionalProperties:false,properties:F_PROPS,required:["id","severity","type","desc","evidence","suggest","role"]}}},required:["unit","files_read","parameters","intra_findings"]}
const XF_PROPS=Object.assign({vs_folder:{type:"string"}},F_PROPS)
const SCH2={type:"object",additionalProperties:false,properties:{axis:{type:"string"},findings:{type:"array",items:{type:"object",additionalProperties:false,properties:XF_PROPS,required:["id","severity","type","desc","vs_folder","evidence","suggest"]}}},required:["axis","findings"]}
const SCH_DRAW={type:"object",additionalProperties:false,properties:{drawing_present:{type:"boolean"},files_checked:{type:"string"},findings:{type:"array",items:{type:"object",additionalProperties:false,properties:XF_PROPS,required:["id","severity","type","desc","vs_folder","evidence","suggest"]}}},required:["drawing_present","findings"]}
const SCH_CODE={type:"object",additionalProperties:false,properties:{code_present:{type:"boolean"},src_used:{type:"string"},findings:{type:"array",items:{type:"object",additionalProperties:false,properties:XF_PROPS,required:["id","severity","type","desc","vs_folder","evidence","suggest"]}}},required:["code_present","findings"]}
const SCH_REF={type:"object",additionalProperties:false,properties:{verdicts:{type:"array",items:{type:"object",additionalProperties:false,properties:{k:{type:"integer"},refuted:{type:"boolean"},reason:{type:"string"}},required:["k","refuted","reason"]}}},required:["verdicts"]}
const SCH_FIN={type:"object",additionalProperties:false,properties:{gate_pass:{type:"boolean"},must_fix:{type:"integer"},verify_grounded:{type:"string"},table_diff:{type:"string"},ran:{type:"array",items:{type:"string"}},note:{type:"string"}},required:["gate_pass","must_fix","ran","note"]}

// stage 号 → 对应 stage skill 路径
function stageSkill(name,no){
  const n = (typeof no==="number"&&no>0)?no : (parseInt((String(name).match(/^\s*(\d+)/)||[])[1])||0)
  if(/DMR|工序|SOP|作业指导/i.test(name)) return SKILLD+"\\dmr-mfg-sop-check-skill\\SKILL.md"
  if(n>=1&&n<=11) return SKILLD+"\\stage-"+String(n).padStart(2,"0")+"-dhf-check-skill\\SKILL.md"
  return ""  // 无对应则通用
}

phase('Scout侦察')
const scout = await agent(`${RULES}\n=== 侦察 ===\n1) 读 ${MD} 下"01立项/客户需求书"类文件,从客户需求书读出**目标市场+品类**(销售地区勾选/注册方/环保栏),写 market/category/market_evidence(引哪行),禁止默认。\n2) glob ${MD} 列审核单元(各阶段文件夹;DMR多版本/注册子目录也各算一个),写 units[{unit,path(相对${MD}),stage_no(阶段号,无则0)}]。`,
  {label:`scout:${MODEL}`, phase:'Scout侦察', schema:SCH_SCOUT})
const UNITS=(scout&&scout.units)||[]
const mk=(scout&&scout.market)||MARKET, cat=(scout&&scout.category)||CAT
log(`Scout: 市场=${mk} 品类=${cat} 单元${UNITS.length}`)

phase('Units逐单元')
const u1 = await parallel(UNITS.map(un => () => {
  const ss=stageSkill(un.unit, un.stage_no)
  return agent(`${RULES}\n市场=${mk} 品类=${cat}\n=== 审核单元【${un.unit}】 ===\n`+
    (ss?`**先读对应阶段检查skill: ${ss}** —— 按它列的提取项+检查项审,你的检查必须⊇它(used_stage_skill写该路径);若该skill是体温计/美国示例而本型号品类/市场不同,检查"方法"照用、法规基线换成${BASELINE}。\n`:`(本单元无对应stage skill,用通用方法)\n`)+
    `被审:glob+读 ${MD}\\${un.path} 下 .md(跳过 *.assets\\ 噪声);大文件夹按关键件取样并在sampled注明。\n`+
    `产出:①尽量多抽参数②intra_findings(对照stage skill检查项与基线,evidence带逐字原文,无原文判NEI)。`,
    {label:`u:${un.unit}`.slice(0,40), phase:'Units逐单元', schema:SCH1})
}))
const units=UNITS.map((un,i)=>({folder:un.unit,files_read:(u1[i]&&u1[i].files_read)||0,sampled:(u1[i]&&u1[i].sampled)||"",used_stage_skill:(u1[i]&&u1[i].used_stage_skill)||"",parameters:(u1[i]&&u1[i].parameters)||[],intra_findings:(u1[i]&&u1[i].intra_findings)||[]}))
let ssot=[]
for(const u of units) for(const p of u.parameters) ssot.push(`${u.folder}|${p.name}=${p.value}@${(p.source_file||'').split("\\").pop()}`)
const ssotDigest=JSON.stringify(ssot).slice(0,110000)

phase('Cross跨单元')
const AXES=[
 {a:"纵向阶段链(下游≥上游)",f:"每参数顺设计流程拉通,查下游放宽/收窄/未承接,给冲突参数全链取值+出处。"},
 {a:"跨版本对账(DMR/BOM多版本)",f:"比多版本DMR/BOM差异,版本间是否受控、与设计变更/注册发补对应(无多版本则空)。"},
 {a:"注册/PTR↔设计输出对账",f:"以注册技术要求/确认版为基准,反查设计输出/DMR/标签/检验是否一致(无注册件则空)。"},
 {a:"设计变更回溯",f:"设变改的参数/件,是否回溯更新设计输入/风险/BOM/图样/PTR(无设变则空)。"},
 {a:"维度横扫(模板残留/版本漂移/角色串联/数值一致/编号唯一/串品类)",f:"不分阶段横扫:他型号他品类模板残留、版本号漂移、人名职责串号、编号唯一、数值跨文件不一致。"},
]
const u2 = await parallel(AXES.map(ax => () =>
  agent(`${RULES}\n市场=${mk} 品类=${cat}\n=== 跨单元对账【${ax.a}】 ===\n任务:${ax.f}\n全局参数SSOT:\n${ssotDigest}\nfindings每条:severity/type/desc/evidence逐字原文/vs_folder/suggest/role。无据判NEI。`,
    {label:`x:${ax.a}`.slice(0,38), phase:'Cross跨单元', schema:SCH2})))
const crosschecks=AXES.map((ax,i)=>({axis:ax.a,findings:(u2[i]&&u2[i].findings)||[]}))

// ---- 图纸 + 代码 分支(有就跑) ----
phase('图纸代码分支')
const branch = await parallel([
  ()=>agent(`${RULES}\n=== 图纸视觉审核(有图样才做) ===\n①glob ${MD} 找图样/图纸文件夹,或 *.assets\\ 里 page_*.png(低字PDF页渲的图)。若没有→drawing_present=false、findings空、直接返回。\n②有→按 ${SKILLD}\\drawing\\SKILL_2D_Drawing_Reading.md 的读图法,用 Read 工具读关键图纸PNG(标题栏/图号/关键尺寸/技术要求),抽图号并与设计输出清单/SSOT对账:图号唯一?尺寸=方案?他型号残留?files_checked写读了哪些。findings每条带证据(图名+看到什么)+vs_folder。`,
    {label:`draw:${MODEL}`, phase:'图纸代码分支', schema:SCH_DRAW}),
  ()=> CODEROOT ? agent(`${RULES}\n=== 代码分支(固件源码) ===\n源码根:${CODEROOT}。①认正源排副本(排 .si4project\\Backup 和文件名带(数字)的)②grep关键常量(电压阈值/量程/单位/关机时间/标定/低压)③与SSOT里设计/规格值对账,**代码是ground truth**。src_used写正源路径。findings每条带 文件:行 证据 + vs_folder(冲突的设计参数)。`,
    {label:`code:${MODEL}`, phase:'图纸代码分支', schema:SCH_CODE}) : Promise.resolve({code_present:false,findings:[]})
])
const draw=branch[0], code=branch[1]
if(draw && (draw.findings||[]).length) crosschecks.push({axis:"图纸视觉审核", findings:draw.findings})
if(code && (code.findings||[]).length) crosschecks.push({axis:"代码对账(固件vs规格)", findings:code.findings})
log(`图纸:${draw&&draw.drawing_present?(draw.findings||[]).length+'条':'无图样'} | 代码:${CODEROOT?((code&&code.findings||[]).length+'条'):'未提供codeRoot'}`)

// ---- 对抗证伪(毙误报):对 critical/major/待PM 逐条反驳 ----
let K=0; const pool=[]
for(const u of units) for(const f of (u.intra_findings||[])){ f._k=K++; if(["critical","major","待PM确认"].includes(f.severity)) pool.push({k:f._k,sev:f.severity,type:f.type,desc:(f.desc||"").slice(0,300),evidence:(f.evidence||"").slice(0,300),where:u.folder}) }
for(const c of crosschecks) for(const f of (c.findings||[])){ f._k=K++; if(["critical","major","待PM确认"].includes(f.severity)) pool.push({k:f._k,sev:f.severity,type:f.type,desc:(f.desc||"").slice(0,300),evidence:(f.evidence||"").slice(0,300),where:c.axis}) }
const CHK=10, batches=[]; for(let i=0;i<pool.length;i+=CHK) batches.push(pool.slice(i,i+CHK))
phase('对抗证伪')
const verds = await parallel(batches.map((b,bi)=>()=>
  agent(`${RULES}\n=== 对抗证伪 ===\n逐条**试图反驳**下面的finding(独立怀疑视角)。判 refuted=true 当:证据站不住/原文grep不到/其实是对的/属已裁决误报(传感器焊点/静音/正确裁剪非目标市场)/越界去判"值本身对错"(一致性≠正确性)。站得住才 refuted=false。**存疑宁可判refuted(宁缺勿滥)**。\nfindings(JSON,k是编号):\n${JSON.stringify(b)}\n返回 verdicts[{k,refuted,reason一句}]。`,
    {label:`refute#${bi}`, phase:'对抗证伪', schema:SCH_REF})))
const killed=new Set()
for(const v of verds){ if(!v) continue; for(const x of (v.verdicts||[])) if(x.refuted) killed.add(x.k) }
const killedList=[]
for(const u of units){ const keep=[]; for(const f of (u.intra_findings||[])){ if(killed.has(f._k)) killedList.push({where:u.folder,sev:f.severity,desc:(f.desc||'').slice(0,80)}); else { delete f._k; keep.push(f) } } u.intra_findings=keep }
for(const c of crosschecks){ const keep=[]; for(const f of (c.findings||[])){ if(killed.has(f._k)) killedList.push({where:c.axis,sev:f.severity,desc:(f.desc||'').slice(0,80)}); else { delete f._k; keep.push(f) } } c.findings=keep }
log(`对抗证伪:候选${pool.length}条,毙掉${killed.size}条`)

// ---- Finalize:确定性层 + 自动table_diff + 硬闸门 ----
phase('Finalize确定性+闸门')
const payload=JSON.stringify({units,crosschecks}).slice(0,168000)
const fin = await agent(
  `你是收尾agent,跑确定性层+硬闸门(不许省)。\n`+
  `1) 把下面JSON原样写到 ${CHECK}\\${MODEL}-_wf.json(UTF-8,可用 tools\\unicode_safe_write.py 或 Write):\n${payload}\n`+
  `2) python "${PKG}\\scripts\\assemble_audit.py" "${CHECK}\\${MODEL}-_wf.json" ${MODEL} "${CHECK}"  → 错误总表/参数长表/审核报告\n`+
  (RAWROOT?`3) **自动表diff**: python "${PKG}\\scripts\\auto_table_diff.py" "${RAWROOT}" ${MODEL} "${CHECK}"  → 自动配多版本同构表跑diff\n`:`3) (未提供rawRoot,跳过自动表diff)\n`)+
  `4) python "${PKG}\\scripts\\run_audit.py" ${MODEL} post --md "${MD}" --check "${CHECK}" --prefix ${MODEL} --foreign "${FOREIGN}" --models "${XMODELS}"  → 残留/数值/证据核验/系统自检硬闸门(必查项exit1);如实回报exit code与必查数\n`+
  `5) python "${PKG}\\scripts\\gen_report_review_html.py" ${MODEL} (若MODELS已配该型号;没配则跳过并在note说明)\n`+
  `回报:gate_pass(必查0则true)/must_fix/verify_grounded(有据率)/table_diff(几对)/ran/note。`,
  {label:`finalize:${MODEL}`, phase:'Finalize确定性+闸门', schema:SCH_FIN})

return { model:MODEL, market:mk, category:cat, market_evidence:(scout&&scout.market_evidence)||"",
  units, crosschecks, refuted_count:killed.size, refuted_list:killedList.slice(0,60),
  drawing:{present:!!(draw&&draw.drawing_present), n:(draw&&draw.findings||[]).length},
  code:{present:!!(code&&code.code_present), n:(code&&code.findings||[]).length},
  finalize:fin }
