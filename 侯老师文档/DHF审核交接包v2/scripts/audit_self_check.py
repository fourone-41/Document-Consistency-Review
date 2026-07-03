# -*- coding: utf-8 -*-
"""审核系统自检:跑完一个型号后,核对'该做的都做了、不该犯的没犯',防跨型号忘事/漂移。
用法: python audit_self_check.py <型号> (默认PT7)
读: 错误总表.csv / 参数长表.csv / 证据核验.csv / MD语料 / 裁决库 _adjudications.csv
出: <型号>-自检报告.md + 控制台 ✅⚠️❗ 清单
"""
import sys, os, re, csv, glob
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding="utf-8")

MODEL = sys.argv[1] if len(sys.argv)>1 else "PT7"
CFG={
 "PT7":{"check":r"D:\AI_0415\03DHF\new_pt7_CHECK","md":r"D:\AI_0415\03DHF\new_pt7_MD",
        "errtbl":"PT7-错误总表.csv","params":"PT7-运行参数长表.csv","verify":"PT7-证据核验.csv",
        "prefix":"PT7","stage_col":"阶段","desc_col":"描述","ev_col":"证据","type_col":"类型",
        "role_col":"责任工程师","sug_col":"建议"},
 "PT9L":{"check":r"D:\AI_0415\03DHF\PT9L_CHECK","md":r"D:\AI_0415\03DHF\PT9L_MD",
        "errtbl":"PT9L-错误总表.csv","params":"PT9L-运行参数长表.csv","verify":"PT9L-证据核验.csv",
        "prefix":"PT9L","stage_col":"阶段","desc_col":"描述","ev_col":"证据","type_col":"类型",
        "role_col":"责任工程师","sug_col":"建议"},
 "PT9S":{"check":r"D:\AI_0415\03DHF\PT9S_CHECK","md":r"D:\AI_0415\03DHF\PT9S_MD",
        "errtbl":"PT9S-全链审核-错误总表-含维度轴.csv","params":"PT9S-参数明细.csv","verify":"PT9S-证据核验.csv",
        "prefix":"PT9S","stage_col":"阶段","desc_col":"错误描述","ev_col":"证据位置","type_col":"类型",
        "role_col":"责任工程师","sug_col":"建议动作"},
 "M10":{"check":r"D:\AI_0415\03DHF\m10_CHECK","md":r"D:\AI_0415\03DHF\m10_MD",
        "errtbl":"M10-错误总表.csv","params":"M10-运行参数长表.csv","verify":"M10-证据核验.csv",
        "prefix":"M10","stage_col":"阶段","desc_col":"描述","ev_col":"证据","type_col":"类型",
        "role_col":"责任工程师","sug_col":"建议",
        "reg_regex":r"GB ?9706|YY ?/?T? ?\d|NMPA|产品技术要求|PTR|注册|分类目录|14971|16886|62304|UDI|医疗器械"},
}[MODEL]
REG_REGEX=CFG.get("reg_regex", r"880\.2910|UDI|807|801|510\(?k|SDV|FLL|ASTM|80601")  # 默认美国;M10用中国
ADJ=r"D:\AI_0415\03DHF\_adjudications.csv"
CK=CFG["check"]
def P(f): return os.path.join(CK,f)

L=[]   # 报告行
def out(s): print(s); L.append(s)
def head(s): out(f"\n## {s}")

out(f"# {MODEL} 审核系统自检报告")
out(f"目录: {CK}")

# ---- 0 读数据 ----
def load(f):
    p=P(f)
    if not os.path.exists(p): return None
    return list(csv.DictReader(open(p,encoding="utf-8-sig")))
rows=load(CFG["errtbl"]); params=load(CFG["params"]); verify=load(CFG["verify"])

DESC=CFG["desc_col"]; EV=CFG["ev_col"]; TYP=CFG["type_col"]; ROLE=CFG["role_col"]; SUG=CFG["sug_col"]; ST=CFG["stage_col"]
def snum(s):
    m=re.match(r"\s*(\d+)",s or ""); return int(m.group(1)) if m else -1

PASS=[]; WARN=[]; FAIL=[]

# ---- 1 工具产物齐全 ----
head("1 工具产物齐全(每步都跑了吗)")
pf=CFG["prefix"]
need={CFG["errtbl"]:"错误总表",CFG["params"]:"参数长表(SSOT)",CFG["verify"]:"证据核验",
      f"{pf}-增量审核报告.md":"逐文件夹报告"}
htmls=glob.glob(os.path.join(CK,"*裁决版.html"))+glob.glob(os.path.join(CK,"*检测报告*.html"))
if htmls: out(f"  ✅ HTML报告 ({os.path.basename(htmls[0])})"); PASS.append("HTML报告")
for f,n in need.items():
    if os.path.exists(P(f)): out(f"  ✅ {n} ({f})"); PASS.append(n)
    else: out(f"  ❗ 缺 {n} ({f}) —— 这步可能忘了跑"); FAIL.append(f"缺产物:{n}")
md_cnt=len(glob.glob(os.path.join(CFG["md"],"**","*.md"),recursive=True))
out(f"  · 转换语料 {md_cnt} 个MD")

if not rows:
    out("\n❗❗ 无错误总表,后续检查跳过");
    open(P(f"{MODEL}-自检报告.md"),"w",encoding="utf-8").write("\n".join(L)); sys.exit()

# ---- 2 阶段覆盖 ----
head("2 阶段覆盖(有没有文件夹被悄悄漏掉)")
by_stage=Counter(snum(r[ST]) for r in rows)
present=sorted(i for i in by_stage if i>0)
out(f"  审到 {len(present)} 个阶段: {present}")
for i in present:
    out(f"  ✅ {i:02d}: {by_stage[i]}问题")
gaps=[j for j in range(1,max(present)+1) if j not in present] if present else []
if gaps: out(f"  ⚠️ 阶段号跳空: {gaps} —— 确认是合并阶段还是漏审"); WARN.append(f"阶段跳空{gaps}")

# ---- 3 字段完整 ----
head("3 字段完整(每条都能落地修吗)")
miss_ev=[r for r in rows if not (r.get(EV) or "").strip()]
miss_sug=[r for r in rows if not (r.get(SUG) or "").strip()]
miss_role=[r for r in rows if not (r.get(ROLE) or "").strip()]
for nm,lst in [("无证据",miss_ev),("无改法建议",miss_sug),("无责任人",miss_role)]:
    if lst: out(f"  ⚠️ {nm}: {len(lst)}条"); WARN.append(f"{nm}{len(lst)}")
    else: out(f"  ✅ {nm}: 0")

# ---- 4 七维度覆盖(有没有哪类完全没查) ----
head("4 七维度覆盖(方法论该查的维度都覆盖了吗)")
DIM={"数值一致":["数值","电流","电压","精度","量程","温度","≥","≤","放宽","收窄"],
     "可追溯断链":["追溯","断链","承接","未承接","来源","上游","下游"],
     "不收窄":["收窄","放宽","不一致","窄于"],
     "矛盾措辞":["矛盾","冲突","不一致","自相"],
     "BOM对账":["BOM","清单","物料","用量","图号","螺钉","EBOM","ABOM"],
     "版本漂移":["版本","V1.","V0","版次","漂移","定版"],
     "角色串联":["负责人","工程师","签名","角色","职责","王迪","马骏"],
     "模板残留":["残留","模板","串号","PT9L","PT3","PT5","血压","他型号","拼接"],
     "法规完备":["880.2910","UDI","807","801","510","法规","ISO","ASTM","强制","FDA"]}
text=lambda r:(r.get(DESC,"")+r.get(TYP,"")+r.get(EV,""))
dimc=Counter()
for r in rows:
    t=text(r)
    for d,kws in DIM.items():
        if any(k in t for k in kws): dimc[d]+=1
for d in DIM:
    c=dimc.get(d,0)
    if c==0: out(f"  ❗ {d}: 0条 —— 这个维度可能整个忘了查"); FAIL.append(f"维度0:{d}")
    else: out(f"  ✅ {d}: {c}条")

# ---- 5 已裁决误报重现(犯没犯老错) ----
head("5 已裁决误报重现(PM拍过的误报又报了吗)")
adj=[]
if os.path.exists(ADJ):
    for a in csv.DictReader(open(ADJ,encoding="utf-8-sig")):
        if a["裁决"]=="误报": adj.append((a["关键词(全含;分隔)"].split(";"),a["说明"]))
hit_adj=0
for kws,note in adj:
    matched=[r for r in rows if all(k in text(r) for k in kws)]
    if matched:
        hit_adj+=len(matched)
        out(f"  ⚠️ 候选:触及已裁决误报关键词【{'+'.join(kws)}】{len(matched)}条,人工瞄一眼是否真重报(关键词匹配偏松,常是顺带提及/不同问题) —— {note}")
        for r in matched[:3]: out(f"       {r[ST]} {r.get(DESC,'')[:60]}")
        WARN.append(f"误报候选:{'+'.join(kws)}×{len(matched)}")
if hit_adj==0: out(f"  ✅ 未触及任何已裁决误报关键词(裁决库{len(adj)}条规则)")
else: out(f"  (说明:以上是关键词撞库的候选,需人工确认;若确认非重报可忽略)")

# ---- 6 法规基线锚定(对应市场基线是否落实) ----
head("6 法规基线锚定(目标市场强制基线是否落实)")
us=sum(1 for r in rows if re.search(REG_REGEX,text(r)))
if us==0: out("  ❗ 0条提到目标市场强制法规 —— 法规基线可能没用上"); FAIL.append("无法规锚")
else: out(f"  ✅ {us}条锚定目标市场强制法规/标准(正则:{REG_REGEX[:40]}…)")

# ---- 7 证据核验摘要 ----
head("7 证据核验(agent有没有编造证据)")
if verify:
    vc=Counter(v["核验结果"] for v in verify)
    g=vc.get("有据",0)+vc.get("有据(部分)",0)
    out(f"  有据{g} / 缺失断言{vc.get('缺失断言',0)} / 部分可疑{vc.get('部分可疑',0)} / 可疑{vc.get('可疑',0)} / 无引文{vc.get('无引文',0)}")
    susp=[v for v in verify if v["核验结果"]=="可疑"]
    if susp:
        out(f"  ❗ {len(susp)}条引文全语料找不到(重点人工复核):")
        for v in susp: out(f"       [{v['严重度']}|{v[ST]}] {v['可疑引文'][:60]}")
        WARN.append(f"证据可疑{len(susp)}")
    else: out("  ✅ 无'可疑'(声称原文有却搜不到)的finding")
else:
    out("  ⚠️ 未跑证据核验(verify_findings.py)"); WARN.append("未跑证据核验")

# ---- 8 跨型号系统病对照(老型号有的病,新型号查到了吗) ----
head("8 跨型号系统病对照(PT9L/PT9S三大系统病,新型号都覆盖了吗)")
SYS={"模板残留他型号":["残留","串号","PT9L","PT3","血压","拼接","他型号"],
     "美国强制法规缺":["880.2910","UDI","807","801","强制","510"],
     "参数全链放宽/收窄":["放宽","收窄","≥","≤","窄于","不一致"]}
for nm,kws in SYS.items():
    c=sum(1 for r in rows if any(k in text(r) for k in kws))
    if c==0: out(f"  ❗ {nm}: 0条 —— 前两型号都有,新型号竟没查到?疑漏查"); FAIL.append(f"系统病漏:{nm}")
    else: out(f"  ✅ {nm}: {c}条(系统病复现,符合预期)")

# ---- 总结 ----
head("自检结论")
out(f"  ✅ 通过 {len(PASS)} 项基础产物")
out(f"  ⚠️ 提醒 {len(WARN)} 项: {'; '.join(WARN) if WARN else '无'}")
out(f"  ❗ 必查 {len(FAIL)} 项: {'; '.join(FAIL) if FAIL else '无'}")
verdict = "❗ 有必查项,先处理上面 ❗" if FAIL else ("⚠️ 基本通过,看提醒项" if WARN else "✅ 全部通过")
out(f"\n  判定: {verdict}")

open(P(f"{MODEL}-自检报告.md"),"w",encoding="utf-8").write("\n".join(L))
print(f"\n-> {P(MODEL+'-自检报告.md')}")
