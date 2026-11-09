import json
p='/home/claude/edition-2026-11-09.json'; ed=json.load(open(p)); s=ed['body_html']
def R(a,b):
    global s; assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
R("Buffalo plays at Minnesota at 8:15, both teams 6&ndash;1. It is the league's top-scoring offense, 33.3 points a game, against its stingiest defense, 13.3 allowed, Buffalo Rumblings says, and Carson Wentz starts at quarterback for the Vikings with Kyler Murray out. The full recap runs tomorrow.",
  "Buffalo plays at Minnesota at 8:15, both teams 6&ndash;1, and the Vikings start Carson Wentz at quarterback with Kyler Murray out with a hamstring injury, Buffalo Rumblings says. Minnesota leads the all-time series 9&ndash;6, and a loss would knock Buffalo out of the AFC's top seed. The full recap runs tomorrow.")
R("Gang Green Nation, Buffalo Rumblings, AP","Gang Green Nation, Buffalo Rumblings, ProFootballTalk, AP")
R("Rob Gronkowski, the Amherst native and Williamsville North star who became one of the great tight ends, was inducted into the Patriots Hall of Fame this weekend, WGRZ reports.",
  "Rob Gronkowski, the Amherst native and former Williamsville North standout who became an NFL star tight end, is being inducted into the Patriots Hall of Fame this weekend, WGRZ reports.")
R("with northwest gusts to 28</span>","with northwest gusts to 28 mph</span>")
R("<b>Jets 12, Chiefs 35</b>","<b>Chiefs 35, Jets 12</b>")
ed['body_html']=s
for q in [p,'/home/claude/site/data/edition-2026-11-09.json']: json.dump(ed,open(q,'w'),ensure_ascii=False,indent=1)
t=open('/home/claude/site/data/newscast/2026-11-09.txt').read()
for a,b in [("It's the league's highest-scoring offense against its toughest defense.","Minnesota leads the all-time series nine games to six, and a loss would knock Buffalo out of the top seed in the conference."),
 ("The first half was honestly their best of the year: more yards, more time with the ball, and they won the turnover battle.","In the first half they outgained Kansas City, won the turnover battle and scored on four of five drives."),
 ("Veterans Day on Wednesday is partly sunny and mild, around fifty-six, with showers possible that night.","Veterans Day on Wednesday is partly sunny, around fifty-six."),
 ("Lake Erie and Lake Ontario are both still fifty-eight degrees.","As of Sunday, Lake Erie and Lake Ontario were both fifty-eight degrees."),
 ("the head of the world's hottest computer chip company is under investigation by his own board.","the head of the chip company behind the artificial intelligence boom is under investigation by his own board."),
 ("REGGIE: And go Bills.","REGGIE: Go Bills tonight, and see you Sunday for Bills and Jets.")]:
    assert t.count(a)==1,a[:40]; t=t.replace(a,b)
open('/home/claude/site/data/newscast/2026-11-09.txt','w').write(t)
print('ok')
