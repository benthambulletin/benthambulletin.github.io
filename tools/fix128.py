import json
P=['/home/claude/edition-2026-10-30.json','/home/claude/site/data/edition-2026-10-30.json']
e=json.load(open(P[1]));b=e['body_html']
F=[("Days since the last migraine: Garret 1, Dad 24, Mom 21. October so far: Garret four, Dad one, Mom one.","Days since the last migraine: Garret 1, Dad 24, Mom 1. October so far: Garret four, Dad one, Mom two."),
("<b>The sun trines the moon in your sign</b>.","<b>The sun trines the moon</b>."),
("Five employees will stay on.","All but five of the plant's workers are on the layoff list, according to the notice, which was posted Monday but dated Oct. 1."),
("<p>Google lost about $500 billion in stock market value after its own executive said its conversational \"AI mode\" is cutting into the money it makes from ads beside ordinary search results, the BBC reports. The BBC notes millions now ask chatbots such as ChatGPT and Claude instead of searching.</p>",
 "<p>Google's parent lost about $500 billion in stock market value after quarterly results in which its business chief said its conversational \"AI mode\" is eating into the money it makes from ads beside ordinary search results, the BBC reports. Revenue still grew 25 percent, to $127.6 billion; the BBC notes millions now ask chatbots such as ChatGPT and Claude instead of searching.</p>"),
('<div class="pnote"><b>From the Group Chat &middot; Kaylani</b> &middot; <i>Tommy\'s 2 Cents, satire</i><br>','<div class="pnote" style="border:1px solid var(--rule,#d3b88f);padding:.6rem .75rem"><b>From the Group Chat &middot; Kaylani</b> &middot; <i>Tommy\'s 2 Cents (satire, not a real ballot question)</i><br>'),
("<b>Joanne:</b> This is an OUTRAGE.","<b>Joanne (as Kaylani imagines her):</b> This is an OUTRAGE."),
("It's the second Hillbillies playoff win this week, after volleyball's quarterfinal sweep.","That leaves the Hillbillies one win from a sectional title."),
("<p>Noah Kahan is bringing his \"The Last of the Bugs\" world tour to the new Highmark Stadium, WKBW reports. It's part of a 2027 stadium tour, Rochester First says.</p>","<p>Noah Kahan is bringing his \"The Last of the Bugs\" world tour to Highmark Stadium on Saturday, June 12, 2027, WKBW reports. He teased the dates Tuesday on the social media of several stadiums, including Fenway Park and Ford Field, WIVB says.</p>"),
('<div class="line"><span class="lbl t">Election Day</span>','<div class="line"><span class="lbl t">The Turning</span> Monroe County, around Scottsville, is expected to reach 80 percent color this week, the state\'s weekly report says.</div>\n<div class="line"><span class="lbl t">Election Day</span>'),
('<div class="ledger"><div class="num"><div class="cap">Ballots already cast in the midterms</div><div class="big">43 million+</div></div>\n<div class="txt">Early voting nationwide is surging with four days to go, the BBC reports.</div></div>',
 '<div class="ledger"><div class="num"><div class="cap">Raise for TV cartoon voice actors over four years</div><div class="big">12.6%</div></div>\n<div class="txt">SAG-AFTRA members ratified new animation contracts Thursday with 94.95 percent voting yes, Deadline reports; they also add protections around AI.</div></div>'),
("Behind the front: a breezy, partly sunny 57, and a cold night for carving","Behind the front: a partly sunny 57 with a northwest wind, and a cold night for carving"),
("the better quarterback, the AP reports:","the better quarterback, the <i>Observer</i> reports:"),
("Dunkirk Observer, AP, WKBW, WIVB, Rochester First, Hollywood Reporter","Dunkirk Observer, WKBW, WIVB, Hollywood Reporter, Deadline")]
for a,c in F:
  assert b.count(a)==1,a[:70]; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
