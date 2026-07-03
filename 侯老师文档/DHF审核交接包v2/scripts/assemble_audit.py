# -*- coding: utf-8 -*-
# 通用汇总(任意型号): python assemble_audit.py <workflow_json> <型号> <CHECK目录>
# json 顶层 {units:[...],crosschecks:[...]} 或 {result:{...}};units项含 folder/files_read/parameters/intra_findings;crosschecks项含 axis/findings(带vs_folder)
import sys, os, json, csv, datetime as dt
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
JS=sys.argv[1]; MODEL=sys.argv[2]; DST=sys.argv[3]
os.makedirs(DST,exist_ok=True)
SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}
o=json.load(open(JS,encoding="utf-8")); R=o.get("result",o)
units=R.get("units",R.get("folders",[])); cross=R.get("crosschecks",[])
def P(s): return os.path.join(DST,f"{MODEL}-{s}")
def fk(u,*ks):
    for k in ks:
        if k in u: return u[k]
    return ""
params=[]
for u in units:
    for p in u.get("parameters",[]):
        params.append({"阶段":fk(u,"folder","unit"),"参数名":p.get("name",""),"值":p.get("value",""),"出处文件":p.get("source_file","")})
with open(P("运行参数长表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["阶段","参数名","值","出处文件"]); w.writeheader(); w.writerows(params)
rows=[]
for u in units:
    st=fk(u,"folder","unit")
    for x in u.get("intra_findings",[]):
        rows.append({"阶段":st,"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"内部","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":""})
    for x in u.get("cross_findings",[]):
        rows.append({"阶段":st,"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"关联","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":x.get("vs_folder","")})
for c in cross:
    for x in c.get("findings",[]):
        rows.append({"阶段":c.get("axis",""),"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"关联","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":x.get("vs_folder","")})
rows.sort(key=lambda r:SEV.get(r["严重度"],9))
for i,r in enumerate(rows,1): r["序号"]=i
with open(P("错误总表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["序号","阶段","原ID","严重度","轴","类型","描述","证据","建议","责任工程师","关联前序"]); w.writeheader(); w.writerows(rows)
sev=Counter(r["严重度"] for r in rows)
L=[f"# {MODEL} · 审核报告",f"- 生成 {dt.datetime.now().replace(microsecond=0)}",
   f"- 单元 {len(units)} + 跨单元轴 {len(cross)} | 参数 **{len(params)}** | 问题 **{len(rows)}** (🔴{sev.get('critical',0)} 🟠{sev.get('major',0)} 🟡{sev.get('minor',0)} 🔵{sev.get('待PM确认',0)} ⚪{sev.get('NEI',0)})",""]
for u in units:
    ic=u.get("intra_findings",[]); L.append(f"## {fk(u,'folder','unit')} (读{u.get('files_read',0)} 抽{len(u.get('parameters',[]))} 内部{len(ic)})")
    for x in sorted(ic,key=lambda v:SEV.get(v.get('severity',''),9)): L.append(f"- [{x.get('severity','')}] {x.get('type','')}：{x.get('desc','')}")
    L.append("")
for c in cross:
    L.append(f"## 对账轴:{c.get('axis','')} ({len(c.get('findings',[]))})")
    for x in sorted(c.get('findings',[]),key=lambda v:SEV.get(v.get('severity',''),9)): L.append(f"- [{x.get('severity','')}] →{x.get('vs_folder','')} {x.get('desc','')}")
    L.append("")
open(P("审核报告.md"),"w",encoding="utf-8").write("\n".join(L))
print(f"{MODEL}: 单元{len(units)}+轴{len(cross)} 参数{len(params)} 问题{len(rows)} {dict(sev)} -> {DST}")
