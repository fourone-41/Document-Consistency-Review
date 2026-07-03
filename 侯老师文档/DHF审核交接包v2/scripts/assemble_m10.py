# -*- coding: utf-8 -*-
# 汇总 M10 审核(units + crosschecks 结构) -> 运行参数长表 + 错误总表 + 报告
import sys, os, json, csv, datetime as dt
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
OUT=sys.argv[1]
DST=r"D:\AI_0415\03DHF\m10_CHECK"; os.makedirs(DST,exist_ok=True)
SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}
o=json.load(open(OUT,encoding="utf-8")); R=o["result"]
units=R.get("units",[]); cross=R.get("crosschecks",[])
def P(s): return os.path.join(DST,f"M10-{s}")

# SSOT
params=[]
for u in units:
    for p in u.get("parameters",[]):
        params.append({"阶段":u["folder"],"参数名":p.get("name",""),"值":p.get("value",""),"出处文件":p.get("source_file","")})
with open(P("运行参数长表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["阶段","参数名","值","出处文件"]); w.writeheader(); w.writerows(params)

# 错误总表(内部=单元intra + 关联=跨单元对账)
rows=[]
for u in units:
    for x in u.get("intra_findings",[]):
        rows.append({"阶段":u["folder"],"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"内部","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":""})
for c in cross:
    for x in c.get("findings",[]):
        rows.append({"阶段":c.get("axis",""),"原ID":x.get("id",""),"严重度":x.get("severity",""),"轴":"关联","类型":x.get("type",""),
            "描述":x.get("desc",""),"证据":x.get("evidence",""),"建议":x.get("suggest",""),"责任工程师":x.get("role",""),"关联前序":x.get("vs_folder","")})
rows.sort(key=lambda r:SEV.get(r["严重度"],9))
for i,r in enumerate(rows,1): r["序号"]=i
with open(P("错误总表.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["序号","阶段","原ID","严重度","轴","类型","描述","证据","建议","责任工程师","关联前序"]); w.writeheader(); w.writerows(rows)

# 报告
sev=Counter(r["严重度"] for r in rows)
L=[f"# M10 雾化器（仅中国 NMPA）· 审核报告",
   f"- 生成: {dt.datetime.now().replace(microsecond=0)}",
   f"- 并行审 {len(units)} 单元(18 DHF + 3 DMR + 4 注册) + {len(cross)} 轴跨单元对账",
   f"- 参数 **{len(params)}** | 问题 **{len(rows)}**  (🔴{sev.get('critical',0)} 🟠{sev.get('major',0)} 🟡{sev.get('minor',0)} 🔵{sev.get('待PM确认',0)}待PM ⚪{sev.get('NEI',0)}NEI)",
   ""]
for u in units:
    ic=u.get("intra_findings",[])
    L.append(f"## {u['folder']}　(读{u.get('files_read',0)}文件{(' · 取样:'+u.get('sampled','')) if u.get('sampled') else ''} · 抽{len(u.get('parameters',[]))}参数 · 内部{len(ic)})")
    if not ic: L.append("- ✅ 内部未发现问题"); L.append(""); continue
    for x in sorted(ic,key=lambda v:SEV.get(v.get('severity',''),9)):
        L.append(f"- [{x.get('severity','')}] {x.get('type','')}：{x.get('desc','')}　_证据：{(x.get('evidence','') or '')[:140]}_")
    L.append("")
L.append("\n# 跨单元对账（Phase2）\n")
for c in cross:
    fs=c.get("findings",[])
    L.append(f"## 轴：{c.get('axis','')}（{len(fs)} 条）")
    for x in sorted(fs,key=lambda v:SEV.get(v.get('severity',''),9)):
        L.append(f"- [{x.get('severity','')}] →{x.get('vs_folder','')}　{x.get('type','')}：{x.get('desc','')}　_证据：{(x.get('evidence','') or '')[:140]}_")
    L.append("")
open(P("审核报告.md"),"w",encoding="utf-8").write("\n".join(L))

print(f"M10 汇总: {len(units)}单元 + {len(cross)}对账轴 | 参数{len(params)} | 问题{len(rows)} {dict(sev)}")
xc=sum(len(c.get('findings',[])) for c in cross)
print(f"  内部{sum(len(u.get('intra_findings',[])) for u in units)} 关联{xc}")
print(f"  -> {P('审核报告.md')} / {P('错误总表.csv')} / {P('运行参数长表.csv')}")
for u in units: print(f"  {u['folder']}: 内部{len(u.get('intra_findings',[]))} 参数{len(u.get('parameters',[]))}")
for c in cross: print(f"  [对账]{c.get('axis','')[:24]}: {len(c.get('findings',[]))}")
