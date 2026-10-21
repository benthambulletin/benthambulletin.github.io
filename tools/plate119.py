import json
d=json.load(open('edition-2026-10-21.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A little boy, seen from behind, watches through a window as a garbage truck passes under autumn trees"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Garbage truck viewing</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today')
d['body_html']=b; d['plate_path']='/home/claude/plate119.jpg'; d['plate_caption']='Garbage truck viewing'
json.dump(d,open('edition-2026-10-21.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-21.json','w'),ensure_ascii=False,indent=1)
print('plated')
