import json
P=['/home/claude/edition-2026-11-04.json','/home/claude/site/data/edition-2026-11-04.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
R("Outside, it's near-record warm, 77, before the rain tonight.","Outside, it's summer-warm, 77, before the rain tonight.")
R("Summer's last word: partly sunny and 77, near the record, then rain moves in tonight","Summer's last word: partly sunny and 77, then rain moves in tonight")
R("pits the 2&ndash;6 Jets against a 5&ndash;2 Chiefs team.</div>","pits the 2&ndash;6 Jets against a 5&ndash;2 Chiefs team. A week later, Nov. 15 at 1:00, the Bills come to the Meadowlands.</div>")
e['body_html']=b; e['headline']='Democrats win the Senate · Hochul wins again · 77, then rain'
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
