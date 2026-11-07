import json
p='/home/claude/edition-2026-11-07.json'; ed=json.load(open(p)); s=ed['body_html']
def R(a,b):
    global s; assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
R('The Warmest Lake Erie on Record for November','Lake Erie Sets a Record for Early November')
R("Lake Erie hit 60 degrees off Buffalo on Thursday, the warmest it has ever been this deep into November, WKBW reports; the old mark was 58. It was still 59 this morning, the National Weather Service says, with Lake Ontario at 58 off Rochester. Last week's record warm air did it.",
  "Lake Erie hit 60 degrees off Buffalo on Thursday, WKBW reports, two degrees above the old record for the date and even with the warmest November reading on the books, set Nov. 1&ndash;3. It was 59 on Friday, the National Weather Service says, another record for the date; normal for early November is about 53. Lake Ontario was 58 off Rochester.")
R("On southwest winds, Erie's bands hit the Southtowns and Chautauqua County hardest, Dunkirk and Fredonia included. North Tonawanda gets the big totals only when the wind lines up just so. The cover shows what that looked like on Nov. 14, 2014.",
  "Which towns get buried depends on the wind. One direction aims the bands at the Southtowns, the scene on the cover; swing it a little and they land on Chautauqua County's hills, Dunkirk and Fredonia included. North Tonawanda gets the big totals only when the wind lines up just so.")
R('<div class="pull">A 60-degree lake is a loaded battery.</div>\n','')
R('<div class="line"><span class="lbl t">The lakes</span> Erie 59&deg; off Buffalo, Ontario 58&deg; off Rochester.</div>\n','')
# Home Wire
i=s.index('<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; Veterans Day'); j=s.index('<h2 class="sec"><span class="o">&#9733;</span>The Marquee')
s=s[:i]+s[j:]
R('<div class="num">2</div><div><h3>Newfane','<div class="num">3</div><div><h3>Newfane')
R('<div class="wire"><div class="num">1</div><div><h3>Dunkirk','<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Flu Comes Early</h3><p>Flu cases across New York jumped 77 percent in a week, to 7,696, the state Health Department says, and Monroe County is seeing an early-season surge, Rochester First reports. The county has logged 243 cases so far this season.</p></div></div>\n<div class="wire"><div class="num">2</div><div><h3>Dunkirk')
R("I'm warmer in November than in May, and I make snow without ever leaving my bed. What am I?","I have a tongue but never taste, a sole but never pray, and in November I come out of the closet. What am I?")
R("<b>Question of the Day:</b> Lake Erie.","<b>Question of the Day:</b> A winter boot.")
R('<b>Bills</b> &middot; Tackle Dion Dawkins and Alec Anderson are still out ahead of Monday night at Minnesota, while tight end Dalton Kincaid was upgraded to full practice, Buffalo Rumblings reports. The Vikings are starting Carson Wentz at quarterback over Kyler Murray.',
  '<b>Bills</b> &middot; Left tackle Dion Dawkins (ribs) and Alec Anderson (ankle) missed a second straight practice, though Dawkins says he plans to play Monday night at Minnesota, Buffalo Rumblings reports; tight end Dalton Kincaid was upgraded to full practice. The Vikings are starting Carson Wentz at quarterback while Kyler Murray rests a strained hamstring.')
R('The "My Heart Will Go On" singer looked like she knew every riff.',"Slash and members of No Doubt were in the suite too, Billboard says; Dion has said Metallica is one of her twins' favorite bands.")
R('After Knicks guard Tyler Kolek called Taylor Swift a "very performative" fan, the team\'s spokesperson thanked her for "many years" of support, Deadline reports. So much for that.',
  'Knicks guard Tyler Kolek called Taylor Swift a "very performative" fan, meaning one who shows up to be seen, Deadline reports. The reigning NBA champions took her side within hours: a team spokesperson thanked the 14-time Grammy winner for "many years" of support.')
R('and the family has been throwing parties for her every year since she turned 99.','and her family has thrown her a lot of parties since she turned 99.')
R('on the shortlist; nothing is confirmed','in recent screen tests; nothing is confirmed')
R('The Pope Goes Home, Sort Of','The Pope Travels After Surgery')
R('; from tomorrow, sunset comes before 5 p.m.',', about two and a half minutes shorter than Friday')
R('Saturn, high in the south around 10 p.m., if the clouds break.','Saturn, the only bright planet up this evening, highest in the south around 10.')
R('Garret, Nov. 2&ndash;3; no one since','Garret, 4 days ago (2 this month); no one else this week')
R('NASCAR points via Sportradar','schedule and NASCAR points via Sportradar')
R('his White House chief of staff Friday','his White House chief of staff, the president\'s top aide who runs the White House, on Friday')
ed['body_html']=s; ed['headline']='A record-warm Lake Erie · Miller in, Wiles out · Bond screen tests'
for q in [p,'/home/claude/site/data/edition-2026-11-07.json']: json.dump(ed,open(q,'w'),ensure_ascii=False,indent=1)
print('ok')
