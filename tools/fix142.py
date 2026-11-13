"""No. 142 review fixes (pre-publish)."""
import json
P='/home/claude/site/data/edition-2026-11-13.json'
e=json.load(open(P)); b=e['body_html']
def R(o,n):
    global b; assert b.count(o)==1,(o[:50],b.count(o)); b=b.replace(o,n)
R("Hotels skip me between the twelfth floor and the fourteenth, bakers toss me in to round out a dozen, and today I have landed on a Friday. What number am I?",
  "I stand on one leg in the front yard all year with my mouth shut, and I am fed six days a week but never on Sunday. What am I?")
R('<b>Question of the Day:</b> Thirteen.','<b>Question of the Day:</b> A mailbox.')
R('The day pushes back a little. Friday the 13th has nothing to do with it; go slow anyway.',"The day pushes back a little. Don't push harder; go slow and let it pass.")
R('<p>Microsoft says the trouble is in the systems behind Exchange Online, the service that runs its email, and that it has no sign the outage was caused by an attack.</p>',
  '<p>Microsoft says the outage is hitting the programs that depend on Exchange Online, the service that runs its email. The company is still working to pin down the cause and says it has no sign of an attack.</p>')
R('If work email is slow this morning, that is why.','If work email is slow this morning, this may be why.')
R(' &middot; pool from the Sunday Tax standings','')
R("""Sen. Chris Van Hollen of Maryland said Thursday he will run against Sen. Chuck Schumer for Senate majority leader, the top job in the chamber Democrats won in last week's midterms, CBS reports. "We need new leadership," Van Hollen wrote, and Sen. Bernie Sanders of Vermont quickly backed him.""",
  """Sen. Chris Van Hollen of Maryland, whose aide said last week he would not run, said Thursday he will challenge New York's Sen. Chuck Schumer for Senate majority leader, the top job in the chamber Democrats won in last week's midterms, CBS reports. Van Hollen wrote that "we need new leadership," and Sen. Bernie Sanders of Vermont quickly backed him; Schumer answered, "I have the votes," with the vote expected early next month.""")
R('WGRZ reports.</p><p>They did it on the ground:','WGRZ reports. They did it on the ground:')
R('and it missed three field goals.</p>','and it missed three field goals. Central Michigan visits Wednesday night.</p>')
R('<h3>Buffalo &middot; Masks Return to Hospital Floors</h3><p>Starting Monday, Catholic Health will require','<h3>Buffalo &middot; Catholic Health Staff to Mask Up</h3><p>Starting Monday, Catholic Health, the hospital system, will require')
R('One priority is repaying the village water fund about $500,000 already spent on engineering and related costs.',
  'With the project on pause, the first step would be repaying the village water fund about $500,000 already spent on engineering and related costs; the note could be ready by December.')
R('Late morning through mid-afternoon is the mildest stretch, near 41,','Noon through late afternoon is the mildest stretch, near 41,')
R('<h3>Reader Poll: The Paper at 6 a.m. or 8 a.m.?</h3>','<h3>Reader Poll: The Paper at 6&nbsp;a.m. or 8&nbsp;a.m.?</h3>')
e['body_html']=b
json.dump(e,open(P,'w'),indent=1); json.dump(e,open('/home/claude/edition-2026-11-13.json','w'),indent=1)
