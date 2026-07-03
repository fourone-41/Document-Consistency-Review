# -*- coding: utf-8 -*-
# 通用增量审核汇总: python assemble_incremental.py <型号> <workflow输出json> [输出目录]
import sys, os, json, csv, datetime as dt
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")

MODEL=sys.argv[1] if len(sys.argv)>1 else "PT9L"
OUT=sys.argv[2]
DST=sys.argv[3] if len(sys.argv)>3 else {
    "PT9L":r"D:\AI_0415\03DHF\PT9L_CHECK",
    "PT9S":r"D:\AI_0415\03DHF\PT9S_CHECK",
    "PT7":r"D:\AI_0415\03DHF\new_pt7_CHECK",
}.get(MODEL, r"D:\AI_0415\03DHF\%s_CHECK"%MODEL)
os.makedirs(DST,exist_ok=True)
SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}
o=json.load(open(OUT,encoding="utf-8")); folders=o["result"]["folders"]
def P(suf): return os.path.join(DST,f"{MODEL}-{suf}")

# 运行参数长表(SSOT)
params=[]
for fo in folders:
    for p in fo.get("parameters",[]):
        params.append({"阶段":fo["folder"],"参数名":p.get("name",""),"值":p.get("value",""),"出处文件":p.get("source_file","")})
with open(P("运行参数长表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["阶段","参数名","值","出处文件"]); w.writeheader(); w.writerows(params)

# 错误总表(内部+关联) —— 列名与PT7一致,便于gen_report_pt7_html复用
rows=[]
for fo in folders:
    st=fo["folder"]
    for x in fo.get("intra_findings",[]):
        rows.append({"阶段":st,"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"内部","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":""})
    for x in fo.get("cross_findings",[]):
        rows.append({"阶段":st,"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"关联","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":x.get("vs_folder","")})
rows.sort(key=lambda r:(SEV.get(r["严重度"],9)))
for i,r in enumerate(rows,1): r["序号"]=i
with open(P("错误总表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["序号","阶段","原ID","严重度","轴","类型","描述","证据","建议","责任工程师","关联前序"]); w.writeheader(); w.writerows(rows)

# 逐文件夹增量报告 MD
sev=Counter(r["严重度"] for r in rows)
L=[f"# {MODEL} · 增量复审报告(逐字原文证据)",
   f"- 生成: {dt.datetime.now().replace(microsecond=0)}",
   f"- 抽取参数(运行长表): **{len(params)}** | 问题: **{len(rows)}**",
   f"- 严重度: 🔴critical {sev.get('critical',0)} / 🟠major {sev.get('major',0)} / 🟡minor {sev.get('minor',0)} / 🔵待PM {sev.get('待PM确认',0)} / ⚪NEI {sev.get('NEI',0)}",
   ""]
for fo in folders:
    ic=fo.get("intra_findings",[]); cc=fo.get("cross_findings",[])
    L.append(f"## {fo['folder']}　(读{fo.get('files_read',0)}文件 · 抽{len(fo.get('parameters',[]))}参数 · 内部{len(ic)} · 关联{len(cc)})")
    if not ic and not cc: L.append("- ✅ 本阶段未发现问题"); L.append(""); continue
    if ic:
        L.append("**内部问题：**")
        for x in sorted(ic,key=lambda v:SEV.get(v.get('severity',''),9)):
            L.append(f"- [{x.get('severity','')}] {x.get('type','')}：{x.get('desc','')}　_证据：{(x.get('evidence','') or '')[:140]}_")
    if cc:
        L.append("**关联问题（和前序文件夹）：**")
        for x in sorted(cc,key=lambda v:SEV.get(v.get('severity',''),9)):
            L.append(f"- [{x.get('severity','')}] →{x.get('vs_folder','')}　{x.get('type','')}：{x.get('desc','')}　_证据：{(x.get('evidence','') or '')[:140]}_")
    L.append("")
open(P("增量审核报告.md"),"w",encoding="utf-8").write("\n".join(L))

print(f"{MODEL} 增量复审汇总: 文件夹{len(folders)} | 参数{len(params)} | 问题{len(rows)} {dict(sev)}")
print(f"  关联(跨文件夹){sum(len(fo.get('cross_findings',[])) for fo in folders)}条")
print(f"  -> {P('增量审核报告.md')} / {P('错误总表.csv')} / {P('运行参数长表.csv')}")
for fo in folders: print(f"  {fo['folder']}: 内部{len(fo.get('intra_findings',[]))} 关联{len(fo.get('cross_findings',[]))}")
