import json
P = ['/home/claude/site/data/edition-2026-11-21.json', '/home/claude/edition-2026-11-21.json']
ed = json.load(open(P[0])); s = ed['body_html']
def R(a, b):
    global s
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
R("His family's statement at the time had spoken of", "The statement announcing his death had spoken of")
R("only a third of the corrections since 1983 went on to become bear markets", "only five of the last 15 corrections from record highs since 1983 went on to become bear markets")
R('<div class="i">&#127782;</div><div class="h">48</div><div class="w">early showers</div>', '<div class="i">&#9925;</div><div class="h">48</div><div class="w">shower early, then sun</div>')
R("The moon has no business with you today. Do not check the retirement account.", "The moon has no business with you today. Enjoy being left alone.")
R("ProFootballTalk says, citing ESPN.", "ProFootballTalk says, citing ESPN. He has no ligament damage, and would likely return only if New England is still in the playoff hunt.")
ed['body_html'] = s
for p in P: json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
