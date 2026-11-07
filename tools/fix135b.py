import json,re
P=['/home/claude/edition-2026-11-06.json','/home/claude/site/data/edition-2026-11-06.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
R('<div class="tile urg"><div class="v">$4.06</div><div class="k">Gas, a gallon</div></div>','<div class="tile urg"><div class="v">3</div><div class="k">Days to Bills&ndash;Vikings</div></div>')
R('Sun &middot; Jets at KC, 1:00 &middot; NASCAR finale &middot; Mon &middot; Bills at MIN, 8:15','Sun &middot; Jets at KC, 1:00; NASCAR finale at Homestead &middot; Mon &middot; Bills at MIN, 8:15')
R('Garret, Monday into Tuesday; none since','Garret, Monday into Tuesday (Nov. 2&ndash;3); no one since')
R('<span class="lbl t">New moon</span>','<span class="lbl t">Planets</span> Saturn, high in the south around 10 p.m., if the showers break; the rest are morning planets now.<br>\n<span class="lbl t">New moon</span>')
stars={'Aries':'<b>Moon in Libra, opposite your sign, and opposite Saturn in it.</b> The rules feel heavier today; bend one.',
'Cancer':'<b>Moon in Libra squares your sign.</b> A small friction at home; let it pass.',
'Leo':'<b>Moon in Libra, sextile your sign.</b> Easy company today; make the call you\'ve owed.',
'Virgo':'<b>Moon in Libra, next door to your sign.</b> No pull either way; clear the list.',
'Scorpio':'<b>Moon in Libra, just behind your sign.</b> A quiet day; save the big ask.'}
for sg,txt in stars.items():
    m=re.search(r'(<div class="sg">'+sg+r'</div><div>)(.*?)( <span class="who">)',b); assert m,sg
    b=b[:m.start(2)]+txt+b[m.end(2):]
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
