import subprocess,sys,time,json,re,datetime,os
TODAY=sys.argv[1] if len(sys.argv)>1 else None
ed=None;prev=None
if TODAY:
    ed=json.load(open(f'edition-{TODAY}.json'))
    dt=datetime.date.fromisoformat(TODAY)
    d=dt-datetime.timedelta(days=1)
    p=f'edition-{d.isoformat()}.json'
    if os.path.exists(p): prev=json.load(open(p))
fails=[];warns=[]
if ed:
    s=ed['body_html']
    # 1. every standing section present
    REQUIRED=['Family Today','The Weather Glass','The Almanac Sky','The Barograph','The Ledger',
              'The National Wire','The Home Wire','The Gridiron','The Chase','The Marquee',
              'On This Day','Question of the Day']
    if dt.weekday()==6: REQUIRED=[x for x in REQUIRED if x not in('The Marquee',)]
    for sec in REQUIRED:
        if sec not in s: fails.append(f'MISSING SECTION: {sec}')
    # 2. issue number consistent
    nos=set(re.findall(r'No\.\s*(\d+)',s))-{'1'}
    if nos and nos!={str(ed['no'])}: fails.append(f'ISSUE NO mismatch: {nos} vs {ed["no"]}')
    # 3. big temperature matches the masthead tile
    tile=re.search(r'<div class="tile good"><div class="v">(\d+)&deg;',s)
    big=re.search(r'<div class="bigtemp">(\d+)<sup>',s)
    if tile and big and tile.group(1)!=big.group(1):
        fails.append(f'TEMP mismatch: tile {tile.group(1)} vs bigtemp {big.group(1)}')
    # 4. yesterday's date must not appear
    if prev and prev['date'] in s: fails.append(f'STALE DATE {prev["date"]} in body')
    # 5. recycled text from yesterday (long identical blocks)
    if prev:
        def blocks(x):
            out=set()
            for pat in (r'<p>(.*?)</p>', r'<div class="line"[^>]*>(.*?)</div>'):
                out |= set(b.strip() for b in re.findall(pat,x,flags=re.S) if len(b)>120)
            return out
        dupes=blocks(s)&blocks(prev['body_html'])
        for dpe in list(dupes)[:6]: warns.append('RECYCLED: '+re.sub('<[^>]+>','',dpe)[:70])
    # 6. duplicate headlines inside today's paper
    heads=[re.sub('<[^>]+>','',h).strip() for h in re.findall(r'<h3>(.*?)</h3>',s,flags=re.S)]
    seen={}
    for h in heads: seen[h]=seen.get(h,0)+1
    for h,c in seen.items():
        if c>1: fails.append(f'DUPLICATE HEADLINE: {h}')
    # 8. stacked rules
    if re.search(r'(?:<div class="dbl"><div class="a"></div><div class="b"></div></div>\n){2,}',s):
        fails.append('STACKED RULES')
    # 9. one-day items must not persist
    for once in ['From the Group Chat','Sunday Spotlight','The Week Ahead','The Week in the Glass',
                 'The Sunday Question','Monday Morning Quarterback']:
        if once in s:
            ok = (once=='Monday Morning Quarterback' and dt.weekday()==0) or \
                 (once in('Sunday Spotlight','The Week Ahead','The Week in the Glass','The Sunday Question') and dt.weekday()==6) or \
                 (once=='From the Group Chat')
            if not ok: fails.append(f'ONE-DAY ITEM PERSISTED: {once}')
    # 10. barograph number matches pressure.json
    pr={x['date']:x['in'] for x in json.load(open('site/data/pressure.json'))}
    m=re.search(r'<div class="press">([\d.]+)',s)
    if m and TODAY in pr and abs(float(m.group(1))-pr[TODAY])>0.001:
        fails.append(f'BAROGRAPH {m.group(1)} vs pressure.json {pr[TODAY]}')
srv=subprocess.Popen([sys.executable,'-m','http.server','8765'],cwd='/home/claude/site',
                     stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1.2)
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.goto('http://localhost:8765/'); pg.wait_for_timeout(1500)
    pg.screenshot(path='shot.png',full_page=True)
    for sel in ['.fam','h1.mast','.wire p','.press','.bigtemp']:
        v=pg.evaluate(f"(e=>e?getComputedStyle(e).fontSize:'absent')(document.querySelector('{sel}'))")
        print(f'{sel:12} {v}')
        if sel=='.fam' and v!='absent' and float(v[:-2])>22: fails.append(f'TYPE TOO BIG: {sel} {v}')
    pw=pg.evaluate("(e=>e?e.naturalWidth:0)(document.querySelector('.frame img'))")
    broken=pg.evaluate("[...document.images].filter(i=>!i.naturalWidth).length")
    fonts=pg.evaluate("document.fonts.check('16px LO') && document.fonts.check('16px PF') && document.fonts.check('16px AR')")
    print('plate',pw,'broken',broken,'fonts',fonts)
    if broken: fails.append(f'{broken} BROKEN IMAGES')
    if not fonts: fails.append('FONTS NOT LOADED')
srv.terminate()
im=Image.open('shot.png'); w,h=im.size
for i in range(5): im.crop((0,i*h//5,w,(i+1)*h//5)).resize((w//2,h//10)).save(f'r{i}.png')
print('\n--- WARNINGS ---'); [print(' ?',x) for x in warns] or print(' none')
print('--- FAILURES ---'); [print(' X',x) for x in fails] or print(' none')
print('\nRESULT:', 'BLOCKED' if fails else 'clear')
