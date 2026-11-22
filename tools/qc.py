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
    REQUIRED=['The Weather Glass','The Almanac Sky','The Ledger',
              'The National Wire','The Home Wire','The Gridiron','The Chase','The Marquee',
              'On This Day','Question of the Day']
    if dt.weekday()==6: REQUIRED=[x for x in REQUIRED if x not in('The Marquee',)]
    if str(dt) > '2026-11-09' and str(dt) < '2027-02-01': REQUIRED.remove('The Chase')  # Chase rests between seasons (Nov 9)
    if str(dt) >= '2026-11-22': REQUIRED.remove('The Ledger')  # Ledger runs only on strong-number days (Nov 21)
    for sec in REQUIRED:
        if sec not in s: fails.append(f'MISSING SECTION: {sec}')
    if str(dt) >= '2026-11-10' and 'class="towns lakes"' not in s: fails.append('MISSING: lake row under the towns (Garret, Nov 9)')
    if str(dt) >= '2026-11-10':   # Nov 10 layout: two halves, each fact once
        if s.count('<div class="part">')!=2: fails.append('LAYOUT: need the two part dividers (The News, The Almanac)')
        if 'class="bigtemp"' in s: fails.append('LAYOUT: no big temperature in the Weather Glass (the tile has it)')
        if '<span class="o">' in s.split('<h2 class="sec">',1)[-1].split('<div class="colo">')[0]: fails.append('LAYOUT: section heads are plain, no ornament spans')
        if 0 <= s.find('The Weather Glass') < s.find('The National Wire'): fails.append('LAYOUT: The News comes before The Almanac')
    # Nov 21 (Garret: "do them all"): quotes and Niagara coverage, checked against the morning feed. Warnings only.
    try:
        _news = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'news.json')) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'news.json')) else open('site/data/news.json'))
        _norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t).replace('&#8217;', "'").replace('&rsquo;', "'").replace('\u2019', "'").replace('\u2018', "'").replace('&amp;', '&').replace('\u201c', '"').replace('\u201d', '"')).lower().strip()
        _bodies = _norm(' '.join((it.get('body') or '') + ' ' + it.get('title', '') for sec in _news['sections'].values() for it in sec))
        _fam = s.split('From the Group Chat', 1)[-1][:600] if 'From the Group Chat' in s else ''
        for q in [q for para in re.findall(r'<p[^>]*>(.*?)</p>|<div class="pull">(.*?)<br>', s, re.S) for t in para for q in re.findall(r'"([^"\n]+?)"', re.sub(r'<[^>]+>', '', t).replace('&quot;', '"').replace('\u201c', '"').replace('\u201d', '"'))]:
            if len(q) < 25: continue
            frag = _norm(q).strip(' .,')
            if frag[:40] and frag[:40] in _norm(_fam): continue
            _parts = [x.strip(' .,') for x in re.split(r'\.\.\.|\u2026', frag) if len(x.strip(' .,')) >= 10]
            if not all(x[:40] in _bodies for x in _parts):
                warns.append(f'QUOTE NOT IN FEED (check it word for word against the source): "{q[:70]}"')
        _hw = s[s.find('The Home Wire'):s.find('<h2', s.find('The Home Wire') + 20)]
        if not re.search(r'Niagara|Tonawanda|Lockport|Lewiston|Wheatfield', _hw):
            _cut = (datetime.datetime.combine(dt, datetime.time(10)) - datetime.timedelta(hours=48)).isoformat()
            _hits = [it['title'] for it in _news['sections'].get('local', []) if it.get('published', '') >= _cut and re.search(r'Niagara|Tonawanda|Lockport|Lewiston|Wheatfield', it['title'] + ' ' + (it.get('body') or '')[:600])]
            if _hits: warns.append(f'NIAGARA: no Niagara County item in the Home Wire, but the feed has {len(_hits)}: ' + ' | '.join(h[:60] for h in _hits[:4]))
    except Exception as _e:
        warns.append(f'feed checks skipped: {_e}')
    # riddle: the answer must not have run before (Nov 12: an umbrella repeat got out)
    import glob as _g
    def _ans(html):
        m = re.search(r'Question of the Day:</b>\s*([^<]+)', html)
        return re.sub(r'^(an?|the)\s+', '', m.group(1).strip().rstrip('.').lower()) if m else None
    _a = _ans(s)
    if _a:
        for _f in sorted(_g.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site', 'data', 'edition-*.json')) + _g.glob('/home/claude/site/data/edition-*.json')):
            if str(dt) in _f: continue
            try: _b = _ans(json.load(open(_f))['body_html'])
            except Exception: continue
            if _b and _b == _a:
                fails.append(f'RIDDLE: answer "{_a}" already ran in {os.path.basename(_f)}'); break
    if str(dt) >= '2026-11-14' and 'Next 24 hours' in s and not re.search(r'<svg[^>]*data-start="\d{1,2}"', s):
        fails.append('LIVE: the 24-hour curve svg needs data-start="<hour of its first point, 0-23>" for the NOW marker')
    if str(dt) >= '2026-11-15' and 'Next 24 hours' in s and 'BARS: CHANCE OF RAIN OR SNOW' not in s:
        fails.append('CURVE: build the 24-hour curve with tools/curve.py (the old sparkline is retired, Nov 14)')
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
    # 9b. every visible web address must be a clickable link (Garret, Oct 18: older readers won't copy and paste)
    _vis=re.sub(r'<a [^>]*>.*?</a>','',s,flags=re.S)
    _vis=re.sub(r'<[^>]+>',' ',_vis)
    for _u in sorted(set(re.findall(r'\b(?:https?://\S*|tally\.so/\S*|benthambulletin\.github\.io\S*|(?:www\.)?[a-z0-9-]+\.(?:com|org|gov|net|edu)\b\S*)',_vis))):
        fails.append(f'UNLINKED URL: {_u}')
    # 9c. barometric pressure retired from the paper (Garret, Oct 21)
    if TODAY>='2026-10-22':
        for _bad,_why in (('The Barograph','Barograph section'),('class="baro','barograph trace/dial'),('&#8243;','inches-of-mercury reading')):
            if _bad in s: fails.append(f'PRESSURE RETIRED: {_why} still in the paper')
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
    broken=pg.evaluate("[...document.images].filter(i=>!i.naturalWidth && !i.closest('.radar')).length")
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
