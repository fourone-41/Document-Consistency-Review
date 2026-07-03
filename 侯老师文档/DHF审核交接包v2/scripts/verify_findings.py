# -*- coding: utf-8 -*-
"""证据核验器:把每条finding的引文(原文'...')拿回转换语料里全局搜,验证agent没编造证据。
用法: python verify_findings.py <错误总表.csv> <MD语料根目录> <输出csv>
默认跑 PT7。核验结果:
  有据      = 引文在真实语料里找到(grounded)
  有据(部分) = 引文整段没找到,但其中长片段找到(多为行号/标点漂移,基本真实)
  可疑      = 有引文但语料里完全找不到(可能编造/严重改写->人工复核重点)
  无引文    = 该条没有可grep的原文引文(多为'缺失/未出现'类结构判断->另行人工)
"""
import sys, os, re, csv, glob
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")

SRC = sys.argv[1] if len(sys.argv)>1 else r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-错误总表.csv"
MDROOT = sys.argv[2] if len(sys.argv)>2 else r"D:\AI_0415\03DHF\new_pt7_MD"
OUT = sys.argv[3] if len(sys.argv)>3 else r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-证据核验.csv"

def norm(s):
    # 去空白/全角空格/竖线/引号括号,保留CJK+字母数字+勾选框■□及法规号点号
    return re.sub(r"[\s　|｜'\"'\"『』「」（）()【】\[\]]", "", s or "")

# 建语料索引: {归一化全文 -> 路径}, 同时记录每个文件leading号
files=[]
for p in glob.glob(os.path.join(MDROOT,"**","*.md"), recursive=True):
    try: txt=open(p,encoding="utf-8").read()
    except: txt=open(p,encoding="utf-8",errors="ignore").read()
    folder=os.path.basename(os.path.dirname(p))
    m=re.match(r"\s*(\d+)",folder)
    files.append((os.path.basename(p), folder, (int(m.group(1)) if m else -1), norm(txt)))
print(f"语料: {len(files)} 个MD文件, 来自 {MDROOT}")

QUOTE_RE=[re.compile(r"'([^']{4,200}?)'"), re.compile(r"『([^』]{4,200}?)』"),
          re.compile(r"「([^」]{4,200}?)」"), re.compile(r"[\"“]([^\"”]{4,200}?)[\"”]"),
          re.compile(r"[''‘]([^''’]{6,200}?)[''’]")]

def extract_quotes(ev):
    qs=[]
    for r in QUOTE_RE:
        for m in r.findall(ev or ""):
            m=m.strip()
            if m and m not in qs: qs.append(m)
    out=[]
    for q in qs:
        if len(norm(q))<4: continue
        if re.match(r"^[\w一-鿿\-＋\+]+\.(?:md|xls|xlsx|docx?|pdf|mpp)", q): continue  # 纯文件指针,非原文引
        out.append(q)
    return out

NEG=["无","未","缺","没有","未出现","未锚定","未承接","缺失","全文无","均无","不存在","NEI",
     "未产出","留空","空白","应含","未见","应有","本应","未填","未提","查无","没出现","未涉及","未引用"]
DESCCOL="描述"; EVCOL="证据"   # 读到表后按实际列名覆盖(PT9S/PT9L=错误描述/证据位置)
def is_absence(r):
    ctx=(r.get(DESCCOL,"")+r.get("类型","")+r.get("严重度",""))
    return (r.get("严重度","")=="NEI") or any(k in ctx for k in NEG)

def find_quote(nq):
    """返回命中文件列表(basename),整段命中"""
    hits=[(bn,fol,num) for (bn,fol,num,ntxt) in files if nq in ntxt]
    return hits

def find_partial(nq):
    """长片段命中:取首/中/尾各12字窗口,任一命中即算"""
    if len(nq)<12: return []
    wins={nq[:12], nq[len(nq)//2-6:len(nq)//2+6], nq[-12:]}
    for (bn,fol,num,ntxt) in files:
        if any(w in ntxt for w in wins if w): return [(bn,fol,num)]
    return []

def stage_num(st):
    m=re.match(r"\s*(\d+)",st or ""); return int(m.group(1)) if m else -1

rows=list(csv.DictReader(open(SRC,encoding="utf-8-sig")))
if rows:
    EVCOL = "证据" if "证据" in rows[0] else ("证据位置" if "证据位置" in rows[0] else "证据")
    DESCCOL = "描述" if "描述" in rows[0] else ("错误描述" if "错误描述" in rows[0] else "描述")
print(f"列: 证据={EVCOL} 描述={DESCCOL}")
out=[]; tally=Counter()
for r in rows:
    ev=r.get(EVCOL,""); exp_num=stage_num(r.get("阶段",""))
    quotes=extract_quotes(ev)
    if not quotes:
        verdict="无引文"; hitfiles=""; cross=""; suspect=""
    else:
        all_hit=[]; suspect_q=[]; partial=False; crossfolder=False
        for q in quotes:
            nq=norm(q); hits=find_quote(nq)
            if not hits:
                ph=find_partial(nq)
                if ph: hits=ph; partial=True
            if hits:
                all_hit+=[h[0] for h in hits]
                if exp_num>0 and not any(h[2]==exp_num for h in hits): crossfolder=True
            else:
                suspect_q.append(q[:40])
        absc=is_absence(r)
        if suspect_q and not all_hit:
            verdict="缺失断言" if absc else "可疑"
        elif suspect_q:
            verdict="有据(部分)" if absc else "部分可疑"  # 缺失类:正向引文有据即可,缺失part本就搜不到
        elif partial:
            verdict="有据(部分)"
        else:
            verdict="有据"
        hitfiles=";".join(sorted(set(all_hit))[:4]); cross="是" if crossfolder else ""
        suspect="| ".join(suspect_q[:3])
    tally[verdict]+=1
    out.append({"序号":r.get("序号",""),"阶段":r.get("阶段",""),"严重度":r.get("严重度",""),
        "轴":r.get("轴",""),"核验结果":verdict,"引文数":len(quotes),
        "命中文件":hitfiles,"跨文件夹命中":cross,"可疑引文":suspect,"原ID":r.get("原ID","")})

with open(OUT,"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["序号","阶段","严重度","轴","核验结果","引文数","命中文件","跨文件夹命中","可疑引文","原ID"])
    w.writeheader(); w.writerows(out)

print(f"\n核验 {len(rows)} 条 -> {OUT}")
grounded=tally.get("有据",0)+tally.get("有据(部分)",0)
print(f"  ✅ 有据(证据已在真实语料命中) {grounded}  [整段{tally.get('有据',0)} + 长片段{tally.get('有据(部分)',0)}]")
print(f"  📋 缺失断言(断言'某项缺失',无法正向grep,需另用'确认缺失'核) {tally.get('缺失断言',0)}")
print(f"  ⚠️ 部分可疑(部分正向引文找不到) {tally.get('部分可疑',0)}")
print(f"  ❗ 可疑(声称文档写了X但全语料找不到->编造/严重改写重点查) {tally.get('可疑',0)}")
print(f"  ◽ 无引文(纯结构/汇总判断,无可grep原文) {tally.get('无引文',0)}")
print(f"\n【最该人工复核:可疑 {tally.get('可疑',0)} 条】(声称原文有但搜不到)")
for r in out:
    if r["核验结果"]=="可疑":
        print(f"  [{r['严重度']}|{r['轴']}|{stage_num(r['阶段']):>2}] {r['可疑引文'][:75]}")
