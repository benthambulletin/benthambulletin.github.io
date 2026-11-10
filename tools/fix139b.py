"""No. 139 relayout (Garret, Nov 10: "pieces jammed together, not a cohesive unit"; mock approved).
Front half The News (National, Home, Marquee, Gridiron), back half The Almanac (Weather, Sky, Coming Up,
Ledger, On This Day, riddle). Plain section heads, no big temp, no sunset cell, Gridiron items get headlines."""
import json,re
P='/home/claude/site/data/edition-2026-11-10.json'
e=json.load(open(P)); b=e['body_html']
parts=b.split('<h2 class="sec">'); head=parts[0]; secs={}
for p in parts[1:]:
    t,rest=p.split('</h2>',1)
    name=re.sub(r'<span class="o">.*?</span>','',t).strip(); secs[name]=rest
assert list(secs)==['The Weather Glass','The Almanac Sky','The Ledger','The National Wire','The Home Wire','The Marquee','The Gridiron','On This Day','Question of the Day'],list(secs)
q=secs['Question of the Day']; i=q.index('<div class="dbl">'); tail=q[i:]; secs['Question of the Day']=q[:i]
a=head.index('<div class="calbox">'); z=head.index('\n</div>\n',a)+len('\n</div>\n'); cal=head[a:z]; head=head[:a]+head[z:]
assert cal.count('calrow')==3
cal=cal.replace('<div class="ch">Coming Up</div>\n','',1)
R='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n'
assert head.endswith(R) and head.count(R)==2; head=head[:-len(R)]
w=secs['The Weather Glass']
old='<div class="wx slim"><div class="bigtemp">60<sup>&deg;</sup></div><div class="wxtext"><span class="lede">Mostly sunny and windy, ten degrees above normal</span></div></div>'
assert w.count(old)==1; w=w.replace(old,'<p class="wlede">Mostly sunny and windy, ten degrees above normal</p>'); secs['The Weather Glass']=w
s=secs['The Almanac Sky']; old='  <div class="wxc"><div class="k">Sunset</div><div class="v">4:56</div><div class="s">p.m.</div></div>\n'
assert s.count(old)==1; secs['The Almanac Sky']=s.replace(old,'')
g=secs['The Gridiron']
def R1(o,n):
    global g; assert g.count(o)==1,o; g=g.replace(o,n)
R1('<div class="line"><b>Bills 23, Vikings 6</b> &middot; ','<div class="wire"><div><h3>Bills 23, Vikings 6</h3><p>')
R1('The Bills are 7&ndash;1.</div>','The Bills are 7&ndash;1.</p></div></div>')
R1('<div class="line"><b>Jets</b> &middot; ','<div class="wire"><div><h3>Jets Deal at the Deadline</h3><p>')
R1('Sunday they host the Bills at 1:00.</div>','Sunday they host the Bills at 1:00.</p></div></div>')
R1('<div class="pnote"><b>The Sunday Tax &middot; Week 10.</b> ','<div class="wire"><div><h3>The Sunday Tax &middot; Week 10</h3><p>')
R1('for the $95 pot.</div>','for the $95 pot.</p></div></div>')
secs['The Gridiron']=g
H=lambda t:f'<h2 class="sec">{t}</h2>'
part=lambda t:f'<div class="part"><span>{t}</span></div>\n'
out=head+part('The News')
for n in ['The National Wire','The Home Wire','The Marquee','The Gridiron']: out+=H(n)+secs[n]
out+=part('The Almanac')
for n in ['The Weather Glass','The Almanac Sky']: out+=H(n)+secs[n]
out+=H('Coming Up')+'\n'+cal
for n in ['The Ledger','On This Day','Question of the Day']: out+=H(n)+secs[n]
out+=tail
e['body_html']=out
json.dump(e,open(P,'w'),indent=1); json.dump(e,open('/home/claude/edition-2026-11-10.json','w'),indent=1)
print('ok',len(b),len(out))
