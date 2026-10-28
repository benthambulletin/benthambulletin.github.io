import json
P=['/home/claude/edition-2026-10-28.json','/home/claude/site/data/edition-2026-10-28.json']
e=json.load(open(P[1]));b=e['body_html']
F=[("<b>The moon over the Chautauqua Ridge</b>, on the cover, came in from Garret Tuesday night.","<b>The moon over the Chautauqua Ridge</b>, on the cover, is Gregg's photo."),
('<div class="plate-sub">Moonrise on the Chautauqua Ridge</div>','<div class="plate-sub">Moonrise on the Chautauqua Ridge &middot; Photo by Gregg</div>')]
for a,c in F:
  assert b.count(a)==1,a; b=b.replace(a,c)
e['body_html']=b; e['plate_caption']='Moonrise on the Chautauqua Ridge · Photo by Gregg'
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
