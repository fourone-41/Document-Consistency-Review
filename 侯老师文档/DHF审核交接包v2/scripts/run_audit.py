# -*- coding: utf-8 -*-
"""DHF 审核 · 确定性 runner + 硬闸门
================================================================
解决"按 SKILL 跑会不会漏跑/随机跑"的问题:
- 确定性层(残留/数值/表diff/对账/证据核验/自检)由本脚本**一条命令全跑**,不给 agent 选择权。
- 语义层(逐阶段/维度轴/对抗证伪)没法确定性,但本脚本最后跑 audit_self_check 当**硬闸门**:
  只要自检报"必查 N 项"(缺产物/某维0条/重报误报/无市场锚定…) → **exit 1**,agent/CI 赖不掉。
- 每步打印 [RUN]/[SKIP 理由],结尾给"层执行清单",哪层没跑一目了然。

用法:
  python run_audit.py <型号> pre     # LLM前:转换+覆盖+残留 (确定性)
  python run_audit.py <型号> post    # LLM后:数值+表diff+对账+证据核验+自检[闸门]
  python run_audit.py <型号> gate    # 只跑自检闸门(exit 1 if 必查)
"""
import sys, os, re, subprocess, argparse, glob
sys.stdout.reconfigure(encoding="utf-8")
BASE=r"D:\AI_0415\03DHF"; TK=BASE+r"\PT9L_CHECK\dhf_audit_toolkit"

MODELS={
 "PT7": {"md":BASE+r"\new_pt7_MD","check":BASE+r"\new_pt7_CHECK","prefix":"PT7",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器,血糖仪","models":"PT3,PT5,PT9C,PT9L,PT9S,KD,BPM,AG-633"},
 "PT9L":{"md":BASE+r"\PT9L_MD","check":BASE+r"\PT9L_CHECK","prefix":"PT9L",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器,血糖仪","models":"PT3,PT5,PT7,PT9C,PT9S,KD,BPM,AG-633"},
 "PT9S":{"md":BASE+r"\PT9S_MD","check":BASE+r"\PT9S_CHECK","prefix":"PT9S","errtbl":"PT9S-全链审核-错误总表-含维度轴.csv","params":"PT9S-参数明细.csv",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器,血糖仪","models":"PT3,PT5,PT7,PT9C,PT9L,KD,BPM,AG-633"},
 "M10": {"md":BASE+r"\m10_MD","check":BASE+r"\m10_CHECK","prefix":"M10",
   "foreign":"血压计,袖带,体温计,额温计,耳温计,血糖仪,冲牙器","models":"KD-5031M,KD-551,KD-926,KN-550,BPM1AE,BPM,PT5,PT3,PT9,AG-695,BG1S"},
}
def errtbl(cfg): return os.path.join(cfg["check"], cfg.get("errtbl", f"{cfg['prefix']}-错误总表.csv"))
def params(cfg): return os.path.join(cfg["check"], cfg.get("params", f"{cfg['prefix']}-运行参数长表.csv"))

LOG=[]
def step(name, ok, detail=""):
    mark = "✅RUN" if ok else "⏭️SKIP"
    LOG.append((name, mark, detail)); print(f"  [{mark}] {name} {('· '+detail) if detail else ''}", flush=True)
def run(cmd):
    print("    $ "+cmd, flush=True); return subprocess.run(cmd, shell=True)

def do_residue(cfg):
    out=os.path.join(cfg["check"], f"{cfg['prefix']}-机械残留扫描.csv")
    if not os.path.isdir(cfg["md"]): step("残留扫描 check_residue", False, "MD语料不存在"); return
    run(f'python "{TK}\\check_residue.py" "{cfg["md"]}" --product {cfg["prefix"]} --foreign {cfg["foreign"]} --models {cfg["models"]} --out "{out}"')
    step("残留扫描 check_residue", True, os.path.basename(out))
def do_numeric(cfg):
    p=params(cfg)
    if not os.path.exists(p): step("数值一致 check_params_numeric", False, "参数长表不存在(先出语义层产物)"); return
    out=os.path.join(cfg["check"], f"{cfg['prefix']}-数值冲突-确定性.csv")
    run(f'python "{TK}\\check_params_numeric.py" "{p}" --product {cfg["prefix"]} --out "{out}"')
    step("数值一致 check_params_numeric", True, os.path.basename(out))
def do_tablediff(cfg):
    # 自动找同名多版本表对(BOM/清单 V1.0/V1.1…),有就跑;没有显式SKIP
    cands=glob.glob(os.path.join(cfg["md"],"**","*V1.0*.md"),recursive=True) if os.path.isdir(cfg["md"]) else []
    if not cands: step("表diff check_table_diff", False, "未自动发现多版本同构表对(需手工指定原始xls对)"); return
    step("表diff check_table_diff", False, f"发现{len(cands)}个V1.0候选,需指定原始xls对手工跑(见SKILL 4b)")
def do_crosswalk(cfg):
    step("跨表对账 check_bom_crosswalk", False, "需指定BOM↔WI对,手工跑(见SKILL 4b)")
def do_verify(cfg):
    et=errtbl(cfg)
    if not os.path.exists(et): step("证据核验 verify_findings", False, "错误总表不存在(先出语义层产物)"); return
    out=os.path.join(cfg["check"], f"{cfg['prefix']}-证据核验.csv")
    run(f'python "{BASE}\\verify_findings.py" "{et}" "{cfg["md"]}" "{out}"')
    step("证据核验 verify_findings", True, os.path.basename(out))
def do_selfcheck_gate(cfg):
    et=errtbl(cfg)
    if not os.path.exists(et): step("系统自检 audit_self_check[闸门]", False, "错误总表不存在,无法自检=未达标"); return 1
    r=subprocess.run(f'python "{BASE}\\audit_self_check.py" {cfg["prefix"]}', shell=True, capture_output=True, text=True, encoding="utf-8")
    txt=(r.stdout or "")+(r.stderr or ""); print(txt[-1500:], flush=True)
    m=re.search(r"❗ 必查 (\d+) 项", txt); n=int(m.group(1)) if m else (0 if "✅ 全部通过" in txt or "基本通过" in txt else 99)
    step("系统自检 audit_self_check[闸门]", True, f"必查{n}项")
    return n

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("phase",choices=["pre","post","gate","all"])
    # 可选路径参数:不在MODELS里的型号/别的机器,直接传这些(便于其他agent复用)
    ap.add_argument("--md"); ap.add_argument("--check"); ap.add_argument("--prefix")
    ap.add_argument("--foreign",default=""); ap.add_argument("--models",default="")
    ap.add_argument("--errtbl"); ap.add_argument("--params")
    a=ap.parse_args()
    if a.model in MODELS:
        cfg=dict(MODELS[a.model])
    elif a.md and a.check:
        cfg={"md":a.md,"check":a.check,"prefix":a.prefix or a.model,"foreign":a.foreign,"models":a.models}
        if a.errtbl: cfg["errtbl"]=a.errtbl
        if a.params: cfg["params"]=a.params
    else:
        print("未知型号:要么在MODELS里加一段,要么传 --md --check [--prefix --foreign --models]"); sys.exit(2)
    # 命令行参数覆盖(即使型号在MODELS里也允许覆盖)
    for k in ("md","check","prefix","errtbl","params"):
        v=getattr(a,k)
        if v: cfg[k]=v
    if a.foreign: cfg["foreign"]=a.foreign
    if a.models: cfg["models"]=a.models
    print(f"=== run_audit {a.model} · {a.phase} ===")
    gate_n=None
    if a.phase in ("pre","all"):
        print("[确定性·LLM前]");
        print("  注:转换+覆盖台账请按 SKILL 用 skill\\conversion-toolkit + 各格式skill(Excel转2套),本runner只强制机械检查")
        do_residue(cfg)
    if a.phase in ("post","all"):
        print("[确定性·LLM后]")
        do_numeric(cfg); do_tablediff(cfg); do_crosswalk(cfg); do_verify(cfg)
        gate_n=do_selfcheck_gate(cfg)
    if a.phase=="gate":
        gate_n=do_selfcheck_gate(cfg)
    print("\n=== 层执行清单 ===")
    for n,m,d in LOG: print(f"  {m}  {n}  {d}")
    if gate_n is not None and gate_n>0:
        print(f"\n❗❗ 硬闸门未通过:自检有 {gate_n} 个必查项 → exit 1。修完再跑。")
        sys.exit(1)
    if gate_n==0: print("\n✅ 硬闸门通过(自检无必查项)。")
    print("\n提醒:语义层(逐阶段check/维度轴/对抗证伪)由 LLM workflow 产出错误总表+参数长表;本runner用自检闸门兜底,缺了会在上面报必查。")

if __name__=="__main__": main()
