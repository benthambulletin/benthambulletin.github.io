import json
P = ['/home/claude/site/data/edition-2026-11-22.json', '/home/claude/edition-2026-11-22.json']
ed = json.load(open(P[0])); s = ed['body_html']
def R(a, b):
    global s
    assert s.count(a) == 1, a[:60]; s = s.replace(a, b)
R("Within the hour Walter Cronkite read the bulletin", "About an hour later, Walter Cronkite read the bulletin")
R('<h3>Jets: Smith Likely in Los Angeles</h3><p>Geno Smith is expected to start at quarterback against the Chargers at 4:05, Gang Green Nation reports.</p>',
  '<h3>Jets at Chargers, 4:05</h3><p>The Jets play in Los Angeles this afternoon; kickoff is 4:05 Eastern.</p>')
R("linebacker Dorian Williams, both ruled out Friday, ProFootballTalk reports;", "linebacker Dorian Williams, both ruled out Friday, ProFootballTalk reports, and called up linebacker Shaq Thompson and cornerback Tre'Davious White from the practice squad to cover, Buffalo Rumblings reports;")
R("All day today; low 60s from 11 a.m. to about 3, the last warm afternoon of the week.", "All day today; in the 60s from 11 a.m. to about 5, the last warm afternoon of the week.")
R("the moon, 95 percent lit and in Aries, comes up", "the moon, 95 percent lit and among the stars of Aries, comes up")
R("The moon has moved on to Taurus and left you alone.", "The moon is in Taurus today and leaves you alone.")
R("and the Flaming Lips' Wayne Coyne, a longtime friend, officiated.", "and the Flaming Lips' Wayne Coyne, who made a 2015 album with her, officiated.")
R("Turkey prices usually ease after the holiday, when stores stop selling birds below cost to bring shoppers in. The survey runs again next November, and it is the number to compare against.",
  "The Farm Bureau runs the same survey again next November, and that is the number to compare against. With turkey supplies tight, the bird is the price to watch.")
R("ended the week Friday at 6,910, 11.6 percent below its Oct. 6 high.", "fell 5.6 percent on Thursday and Friday, 3.7 percent on Friday alone, to close the week at 6,910, 11.6 percent below its Oct. 6 high.")
R("Data: S&amp;P Dow Jones Indices.", "Data: Yahoo Finance.")
R("Closer to home, the trouble is timing rather than storms. The weather service has a chance of rain and snow showers here on Thanksgiving Day itself, after 7 a.m., with a high near 43.",
  "Closer to home, no big storm is in the forecast, but the weather service gives Thanksgiving Day about a 50-50 chance of rain and snow showers starting after 7 a.m., with a high near 43. That takes in the 9 a.m. Turkey Trot.")
s = s.replace("ProFootballTalk, Gang Green Nation;", "ProFootballTalk, Buffalo Rumblings;")
ed['body_html'] = s
for p in P: json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
