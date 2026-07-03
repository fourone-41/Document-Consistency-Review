# -*- coding: utf-8 -*-
"""自动配对同构表(同名多版本BOM/清单 V1.0/V1.1/V1.2...)并跑 check_table_diff。
用法: python auto_table_diff.py <rawRoot> <型号> <CHECK目录>
只对"同一基名、多个版本"的 .xls/.xlsx 成对(相邻版本)做 diff;没有多版本对就报0,不报错。
"""
import sys, os, re, glob, subprocess
sys.stdout.reconfigure(encoding="utf-8")
RAW=sys.argv[1]; MODEL=sys.argv[2]; CHECK=sys.argv[3]
TK=os.path.join(os.path.dirname(os.path.abspath(__file__)),"PT9L_CHECK","dhf_audit_toolkit","check_table_diff.py")
if not os.path.exists(TK):
    TK=r"D:\AI_0415\03DHF\PT9L_CHECK\dhf_audit_toolkit\check_table_diff.py"
os.makedirs(CHECK,exist_ok=True)

VER=re.compile(r"[ _\-]*V?(\d+)\.(\d+)(?:\.(\d+))?", re.I)
def stem_ver(path):
    b=os.path.splitext(os.path.basename(path))[0]
    m=VER.search(b)
    if not m: return None
    ver=tuple(int(x) if x else 0 for x in m.groups())
    stem=(b[:m.start()]+b[m.end():]).strip(" _-")  # 去掉版本号后的基名
    stem=re.sub(r"\s+"," ",stem)
    return (stem, ver, path)

files=[p for p in glob.glob(os.path.join(RAW,"**","*.xls"),recursive=True)+glob.glob(os.path.join(RAW,"**","*.xlsx"),recursive=True)
       if not os.path.basename(p).startswith("~$")]
groups={}
for p in files:
    sv=stem_ver(p)
    if sv: groups.setdefault(sv[0],[]).append((sv[1],sv[2]))
pairs=[]
for stem,lst in groups.items():
    if len(lst)<2: continue
    lst=sorted(set(lst))
    for i in range(len(lst)-1):
        pairs.append((stem,lst[i],lst[i+1]))
print(f"[{MODEL}] 扫到多版本同构表组 {sum(1 for v in groups.values() if len(v)>=2)} 个,相邻版本对 {len(pairs)} 对")
done=0
for stem,(va,pa),(vb,pb) in pairs:
    la=".".join(str(x) for x in va); lb=".".join(str(x) for x in vb)
    safe=re.sub(r"[^\w一-鿿]+","_",stem)[:40]
    out=os.path.join(CHECK,f"{MODEL}-表diff-{safe}-V{la}_V{lb}.csv")
    r=subprocess.run(f'python "{TK}" "{pa}" "{pb}" --labelA "V{la}" --labelB "V{lb}" --out "{out}"',shell=True,capture_output=True,text=True,encoding="utf-8")
    tail=(r.stdout or "").strip().splitlines()
    summ=[l for l in tail if "仅" in l or "值不同" in l]
    print(f"  ✓ {stem[:30]} V{la}↔V{lb}: {summ[-1] if summ else 'done'}")
    done+=1
print(f"[{MODEL}] 表diff 完成 {done} 对 -> {CHECK}\\{MODEL}-表diff-*.csv")
if not pairs: print(f"[{MODEL}] 未发现多版本同构表对(无需table_diff,或版本命名不规范需手工)")
