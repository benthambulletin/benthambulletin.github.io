import json
P=['/home/claude/edition-2026-10-27.json','/home/claude/site/data/edition-2026-10-27.json']
e=json.load(open(P[1]));b=e['body_html']
a='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today'
assert b.count(a)==1
plate='''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
<img src="__PLATE__" alt="A grinning little boy and a man in glasses wearing woven baskets upside down as hats"></div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Hats on</div></div>
'''
b=b.replace(a,plate+a)
e['body_html']=b;e['plate_path']='/home/claude/plate125.jpg';e['plate_caption']='Hats on'
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
