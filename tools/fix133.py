import json
P=['/home/claude/edition-2026-11-04.json','/home/claude/site/data/edition-2026-11-04.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
R('Democrats won both houses of Congress overnight, and Kathy Hochul won a second full term.','Democrats won the Senate overnight and are winning the House, and Kathy Hochul won a second full term.')
R('<div class="touch-head">Democrats Take Congress</div>','<div class="touch-head">Democrats Win the Senate, Lead the House</div>')
R('<b>What it means.</b> From January, a Democratic Congress and a Republican president: new laws will need both, and Democrats will chair the committees. <b>What\'s next:</b>','<b>What\'s next:</b>')
R("the county races aren't in the tracker yet.","the county races have not been called.")
R('<div class="tile urg"><div class="v">7</div><div class="k">Senate seats flipped</div></div>','<div class="tile urg"><div class="v">$15.9B</div><div class="k">Royalties, a record</div></div>')
R('<b>Jets</b> &middot; At Kansas City Sunday at 1:00.</div>','<b>Jets</b> &middot; Sunday\'s trip to Kansas City, 1:00, pits the 2&ndash;6 Jets against a 5&ndash;2 Chiefs team.</div>')
R("though the suspension and his uneven play were seen as factors, the <i>Observer</i>'s report says. Next: Monday night at Minnesota, 8:15.","though the suspension and his uneven play were seen as factors. Next: Monday night at Minnesota, 8:15, two 6&ndash;1 teams.")
R('Langworthy (R) won, the AP called.','Langworthy (R) beat Gies (D); the AP called it.')
R('Clear head, clear words. Say the kind thing first.','Listen twice as long as you talk today; the table will thank you.')
e['body_html']=b; e['headline']='Democrats win the Senate · Hochul wins again · Near-record 77'
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
