import json
d=json.load(open('edition-2026-10-20.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="Southwest jets at the gate under a clear blue sky, seen through the terminal window"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">At the gate, bound for Long Island</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today')
R("<div class=\"fam\"><b>Birthday week.</b> Claire's birthday is Friday,","<div class=\"fam\"><b>Garret is off to Long Island</b>; the cover is his view from the gate this morning. <b>Birthday week:</b> Claire's birthday is Friday,")
d['body_html']=b; d['plate_path']='/home/claude/plate118.jpg'; d['plate_caption']='At the gate, bound for Long Island'
json.dump(d,open('edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
print('plated')

# --- review fix --- recrop landscape: exif_transpose, crop (400,700,1932,1920) on the 1932x2576 original, resize to 1500 wide
