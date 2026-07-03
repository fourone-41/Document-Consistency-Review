# -*- coding: utf-8 -*-
# 2D图纸分支·前处理: 按 SKILL_2D 要求 渲染≥300DPI + 分块切图(3x2 overlap)
import sys,os,glob,csv,fitz,re
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
SRC=r"D:\AI_0415\03DHF\PT9S\PT9S_DHF"
OUT=r"D:\AI_0415\03DHF\PT9S_CHECK\_drawings2d"
os.makedirs(OUT,exist_ok=True)
DPI=320  # SKILL要求≥300
# 高价值2D图(有标题栏+尺寸,需对设计输入/BOM):结构件+外观+总装+原理图
WANT=["外观图","总装图","上盖","下盖","-按键","静音","透镜","导光板","JFXS","主板原理图"]
pdfs=[p for p in glob.glob(os.path.join(SRC,"**","*.pdf"),recursive=True)
      if any(k in os.path.basename(p) for k in WANT)]
# 去重(同名取一)
seen={}
for p in pdfs:
    b=os.path.basename(p)
    key=re.sub(r"[ \-]?\d{8}.*|\.pdf$","",b)[:24]
    sc=("设计输出签字档" in p)*2+("12 设计输出01" in p)
    if key not in seen or sc>seen[key][0]: seen[key]=(sc,p)
rows=[]
for key,(sc,p) in sorted(seen.items()):
    safe=re.sub(r'[\\/:*?"<>|（）()]',"_",key)
    dd=os.path.join(OUT,safe); os.makedirs(dd,exist_ok=True)
    d=fitz.open(p); pg=d[0]
    full=os.path.join(dd,"full.png"); pg.get_pixmap(dpi=DPI).save(full)
    im=Image.open(full); W,H=im.size
    cols,rowsN,ov=3,2,120; cw,ch=W//cols,H//rowsN; crops=[]
    for r in range(rowsN):
        for c in range(cols):
            x0,y0=max(0,c*cw-ov),max(0,r*ch-ov); x1,y1=min(W,(c+1)*cw+ov),min(H,(r+1)*ch+ov)
            cp=os.path.join(dd,f"crop_r{r}c{c}.png"); im.crop((x0,y0,x1,y1)).save(cp); crops.append(cp)
    d.close()
    rows.append({"图":key,"源PDF":os.path.relpath(p,SRC),"尺寸px":f"{W}x{H}","full":full,"crops":";".join(crops)})
    print(f"  {key}: {W}x{H}px @{DPI}dpi, 6块 -> {dd}")
with open(os.path.join(OUT,"_2d_manifest.csv"),"w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["图","源PDF","尺寸px","full","crops"]); w.writeheader(); w.writerows(rows)
print(f"\n共 {len(rows)} 张2D图渲染+分块 -> {OUT}")
