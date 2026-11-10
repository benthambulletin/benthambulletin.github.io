import json
p='/home/claude/edition-2026-11-10.json'; ed=json.load(open(p)); s=ed['body_html']
def R(a,b):
    global s; assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
R('Fall Out Boy announced a 36-date 2027 stadium-and-arena tour of Europe and North America with The Offspring and Good Charlotte, and released "ACES," their first new song in more than three years, Billboard reports.',
  'Fall Out Boy announced a 36-date 2027 stadium-and-arena tour of Europe and North America and released "ACES," their first new song in more than three years, Billboard reports. The North American leg runs 21 stadium dates from July 13 to Aug. 26, including Toronto\'s Rogers Stadium and Citi Field in Queens, with The Offspring and Good Charlotte along.')
R('It peaked at $4.56 earlier this year.','It was $4.56 earlier this year.')
R('are mostly warm, Variety reports, with critics calling it a "wickedly fun holiday treat" and a strong comeback for its star.',
  'are mostly warm after press screenings and a London premiere Monday night, Variety reports, with critics calling it a "wickedly fun holiday treat" and a strong comeback for its star. Full reviews come out Thursday, and the film opens in theaters Friday, Nov. 13.')
R('Friday night rain turns to a chance of snow showers, low around 31, with snow showers possible Saturday morning.','Friday night\'s showers may mix with snow after 10, low around 31, with a chance of snow showers Saturday morning.')
R('<div class="w">morning snow showers</div>','<div class="w">chance of snow</div>')
R('James Cook ran one in from 5 in the fourth, and Tyler Bass made all three field goals, the longest from 52.','James Cook carried 31 times for 107 yards and ran one in from 5 in the fourth, and Tyler Bass kicked three field goals, the longest from 52.')
R("Nvidia chief Jensen Huang's affair","the affair of Jensen Huang, head of AI chip giant Nvidia,")
R('turned down the press secretary job, Us Weekly reports.','turned down the press secretary job President Trump had floated over the weekend and then called a joke, Us Weekly reports.')
R('<div class="k">Sunny, Windy</div>','<div class="k">Mostly Sunny</div>')
R('<div class="w">sunny, windy</div>','<div class="w">mostly sunny</div>')
R('Rolling Stone, Variety, Billboard,','Rolling Stone, Variety, the Hollywood Reporter, Billboard, ProFootballTalk, the Dunkirk <i>Observer</i> (AP),') if False else None
R('Rolling Stone, Variety, Billboard, Gang Green Nation','Rolling Stone, Variety, the Hollywood Reporter, Billboard, Gang Green Nation, ProFootballTalk, AP')
ed['body_html']=s
for q in [p,'/home/claude/site/data/edition-2026-11-10.json']: json.dump(ed,open(q,'w'),ensure_ascii=False,indent=1)
print('ok')
