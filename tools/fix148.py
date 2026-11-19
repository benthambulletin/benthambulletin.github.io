import json
P = ['/home/claude/site/data/edition-2026-11-19.json', '/home/claude/edition-2026-11-19.json']
ed = json.load(open(P[0])); s = ed['body_html']
def R(a, b):
    global s
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
R("Cornerbacks Christian Benford and Dee Alford and tight end Dalton Kincaid all sat out Wednesday's practice, the first of the week before Sunday's game with the Dolphins, ProFootballTalk and Buffalo Rumblings report. The good news is up front: none of the starting offensive linemen missed practice with an injury.",
  "Cornerbacks Christian Benford and Dee Alford and tight end Dalton Kincaid were all listed as out on Wednesday's injury report, the first of the week before Sunday's game with the Dolphins, ProFootballTalk and Buffalo Rumblings report. The team held only a walkthrough, a light run-through, so the listings are estimates. Up front, the only starting lineman listed as out was right guard O'Cyrus Torrence, for personal reasons rather than an injury.")
R("Saturn is close by in the southern sky through the evening.", "Saturn is up in the southern sky through the evening.")
R("Trump met each of the others alone.", "Trump met each of the others separately.")
R("Xi opened by calling relations between China and the United States stable.", 'Xi opened by calling relations between China and the United States "stable and improved."')
R("raised more than $81.3 billion by selling shares to the public for the first time, at $83 apiece, NPR reports; that tops", "sold shares to the public for the first time at $83 apiece, a sale that totaled more than $81.3 billion, NPR reports; that tops")
R("The Bulls won their sixth straight Wednesday night at home. Next is a trip to Akron on Friday, Nov. 27.", "The Bulls won their sixth straight Wednesday night at home.")
R('<span class="kick">The Lead</span>', '<span class="kick">The Lead &middot; Update</span>')
ed['body_html'] = s
for p in P: json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
