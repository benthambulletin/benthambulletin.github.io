import json
P = ['/home/claude/site/data/edition-2026-11-21.json', '/home/claude/edition-2026-11-21.json']
ed = json.load(open(P[0])); s = ed['body_html']
def R(a, b):
    global s
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
# Dunkirk: the station has no thermometer reading today; run the NWS forecast low for the morning (42), labeled.
if '<div class="t">&mdash;</div>' in s: R('<div class="town"><div class="n">Dunkirk</div><div class="t">&mdash;</div><div class="d">Clear<br>high 64&deg;</div></div>',
  '<div class="town"><div class="n">Dunkirk</div><div class="t">42<sup>&deg;</sup></div><div class="d">forecast low<br>high 64&deg;</div></div>')
# Chart caption: a small italic note, not a body-size line.
i = s.find('<div class="line"><span class="lbl t">S&amp;P 500, daily close</span>'); j = s.find('</div>', i) + 6; assert i > 0
s = s[:i] + '<p style="font-style:italic;font-size:.8rem;line-height:1.35;color:var(--soft,#664a2c);margin:.1rem 0 .8rem">S&amp;P 500, daily close, through Thursday, Nov. 19; Friday\'s fall is not yet in the data. Source: S&amp;P Dow Jones Indices, via the St. Louis Fed.</p>' + s[j:]
# Rain cell: keep the small line to one row like its neighbors.
R('<div class="v">None</div><div class="s">until late Sunday night</div>', '<div class="v">None</div><div class="s">this weekend</div>')
# Monday's five-day cell: two lines like the others.
if 'shower early, then sun' in s: R('<div class="w">shower early, then sun</div>', '<div class="w">early shower</div>')
s = s.replace("through Thursday, Nov. 19; Friday's fall is not yet in the data. Source: S&amp;P Dow Jones Indices, via the St. Louis Fed.", "through Thursday, Nov. 19, the day before Friday's fall.")
ed['body_html'] = s
for p in P: json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
