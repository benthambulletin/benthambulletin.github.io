import json
P=['/home/claude/edition-2026-11-04.json','/home/claude/site/data/edition-2026-11-04.json']
e=json.load(open(P[1]));b=e['body_html']
i=b.find('<div class="plate-wrap">'); j=b.find('<div class="dbl-tight">',i); assert i>0 and j>i
cap='The moon over the pines at first light'
b=b[:i]+'''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
<img src="__PLATE__" alt="A crescent moon high in a pink-streaked blue sky over a row of dark pines and a small shed at first light"></div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">'''+cap+'''</div></div>
'''+b[j:]
e['body_html']=b; e['plate_path']='/home/claude/plate133.jpg'; e['plate_caption']=cap
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
