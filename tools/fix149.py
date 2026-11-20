import json
P = ['/home/claude/site/data/edition-2026-11-20.json', '/home/claude/edition-2026-11-20.json']
ed = json.load(open(P[0])); s = ed['body_html']
def R(a, b):
    global s
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
R("died Thursday, days after swallowing a knit hat that landed in her enclosure, CBS reports.", "has died, about a week after swallowing a knit hat that landed in her enclosure, the zoo announced Thursday, CBS reports.")
R("From the Group Chat &middot; Gregg", "From the Group Chat &middot; Gregg, Thursday morning")
R("who died in 2024 at 83, the BBC reports.", "who died in 2024, the BBC reports.")
R("Martin Short admitted he took a fork to a cake", "Martin Short retold how he took a fork to a cake")
R("is up until 2:27 a.m., still in Pisces.", "is up until 2:27 a.m.")
R(" Most people kept typing commands for a few more years.", "")
OLD = "Highmark Stadium in Orchard Park, the Bills' home when Andre Reed played, in a 2023 file photo."
NEW = "The stadium in Orchard Park where Andre Reed played his home games, in a 2023 file photo."
R(OLD, NEW); ed['plate_caption'] = ed['plate_caption'].replace(OLD, NEW)
i = s.find('<div class="wire"><div class="num">3</div><div><h3>Niagara Falls'); j = s.find('<h2 class="sec">The Marquee</h2>'); assert 0 < i < j
tip = s[i:j].replace('<div class="num">3</div>', '<div class="num">2</div>')
s = s[:i] + s[j:]
R('<div class="wire"><div class="num">1</div><div><h3>Finger Lakes', '''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; The State Sues Over a Downtown Hotel</h3><p>Attorney General Letitia James is suing the former owner of the downtown Rochester Holiday Inn, its renovation contractor and the chain's parent company, IHG, over what her office calls a forced-labor scheme, WXXI reports. The suit says dozens of immigrant workers were promised hourly pay and housing, then went months unpaid while working as many as 112 hours a week.</p></div></div>
''' + tip + '<div class="wire"><div class="num">3</div><div><h3>Finger Lakes')
i = s.find('<div class="wire"><div class="num">2</div><div><h3>Fredonia'); j = s.find('<h2 class="sec">The Marquee</h2>'); assert 0 < i < j
s = s[:i] + s[i:j].replace('<div class="num">2</div>', '<div class="num">4</div>') + s[j:]
ed['body_html'] = s
for p in P: json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
