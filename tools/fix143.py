import json
p='/home/claude/site/data/edition-2026-11-14.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b):
    global s
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
R('Rainbow Air Helicopter Tours began night flights over Niagara Falls on Friday, the first in its 32 years, the <i>Niagara Gazette</i> reports. They run','Rainbow Air Helicopter Tours was set to begin night flights over Niagara Falls on Friday, the first in its 32 years, the <i>Niagara Gazette</i> reports. The tours run')
R('The FAA blamed a telecommunications outage.','Officials blamed a telecommunications outage.')
R('is due to steer back toward the pad today for a first attempt at catching it.','is to steer back toward the pad today for a first attempt at catching it, barring further trouble.')
R('none in critical condition, and the Coast Guard\'s Capt. Melanie Burnham said, "There seems to be some type of a loss of steering."','none in critical condition. The Coast Guard\'s Capt. Melanie Burnham said, "There seems to be some type of a loss of steering," according to the BBC.')
R('about 12:30 p.m. Friday near','about 12:30 p.m. local time Friday near')
R('who has been dealing with a neck injury, Buffalo Rumblings reports.','who has been dealing with a neck injury, Buffalo Rumblings reports. Right tackle Spencer Brown is doubtful with an ankle injury.')
R('Bills: The Line Gets Healthier','Bills: Dawkins and Anderson Back')
R('Cloudy and 37 at dawn, with flakes','Cloudy and cold at dawn, with flakes')
R('ordered a nationwide ground stop Friday afternoon, an order that holds planes at the gate instead of letting them take off, on every departing flight in the United States, citing','ordered a nationwide ground stop on every departing flight in the United States Friday afternoon, an order that holds planes at the gate instead of letting them take off, citing')
R('posted a rare message to fans Friday praising','sent fans a rare message Friday, shared on the movie\'s Instagram, praising')
R('after the outage that led Friday\'s paper, the BBC reports.','after the worldwide outage that began Thursday, the BBC reports.')
R('Most covers are drawings because the album is short on pictures, so send','The album is short on pictures, so send')
R('I eat sticks for supper and grow taller with every bite, but one bucket of water puts me to bed. What am I?','I have dozens of teeth and never bite, and one long pull of me shuts the cold out of your coat. What am I?')
R('<b>Question of the Day:</b> A campfire.','<b>Question of the Day:</b> A zipper.')
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-14.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
print('fixed')
