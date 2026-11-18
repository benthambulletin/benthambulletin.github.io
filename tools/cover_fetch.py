#!/usr/bin/env python3
"""Fetch candidate cover photos for the day's lead story (runs in GitHub Actions; Garret, Nov 16:
no more drawn covers; "act independently"). The build session cannot download images itself.

Env: QUERIES = JSON list of search phrases, most specific first, e.g. ["Voyager 1 spacecraft", "Voyager spacecraft"].
Searches NASA's image library (public domain) and Wikimedia Commons (public domain / CC0 / CC BY / CC BY-SA only),
keeps landscape images at least 1000px wide, and writes up to 8 into spool/cover/ as c1.jpg... (max 1600px wide)
with spool/cover/candidates.json: [{file, source, title, credit, license, page, query, w, h}].
The build looks at them, picks one or none, crops it to the plate, credits it in the caption and deletes spool/cover/.
"""
import io, json, os, re, sys, urllib.parse, urllib.request
from PIL import Image
UA = {'User-Agent': 'BenthamBulletin/1.0 (family newspaper; https://benthambulletin.github.io)'}
OUT = 'spool/cover'; os.makedirs(OUT, exist_ok=True)
def get(url, raw=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        b = r.read()
    return b if raw else json.loads(b)
def strip(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()
def nasa(q, n=4):
    out = []
    try:
        items = get('https://images-api.nasa.gov/search?media_type=image&q=' + urllib.parse.quote(q))['collection']['items']
    except Exception as e:
        print('nasa search failed', q, e); return out
    for it in items[:12]:
        if len(out) >= n: break
        d = it['data'][0]; nid = d['nasa_id']
        try:
            files = [x['href'] for x in get('https://images-api.nasa.gov/asset/' + urllib.parse.quote(nid))['collection']['items']]
        except Exception as e:
            print('nasa asset failed', nid, e); continue
        pick = next((f for k in ('~large.jpg', '~medium.jpg', '~orig.jpg') for f in files if f.endswith(k)), None)
        if not pick: continue
        credit = 'NASA' + ('/' + d['center'] if d.get('center') and d['center'] not in ('HQ',) else '')
        if d.get('secondary_creator'): credit = strip(d['secondary_creator'])[:80]
        out.append(dict(url=pick.replace('http://', 'https://').replace(' ', '%20'), source='NASA Image and Video Library', title=strip(d.get('title'))[:140],
                        desc=strip(d.get('description'))[:300], credit=credit, license='Public domain (NASA)',
                        page='https://images.nasa.gov/details/' + urllib.parse.quote(nid), date=d.get('date_created', '')[:10]))
    return out
OKLIC = re.compile(r'^(public domain|pd|cc0|cc by(-sa)? ?\d|cc-by(-sa)?-\d)', re.I)
def commons(q, n=4):
    out = []
    u = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=20'
         '&gsrsearch=' + urllib.parse.quote('filetype:bitmap ' + q) + '&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1600')
    try:
        resp = get(u); pages = sorted(resp.get('query', {}).get('pages', {}).values(), key=lambda p: p.get('index', 99))
        print('commons', repr(q), 'pages', len(pages), 'keys', list(resp.keys()), str(resp.get('error') or resp.get('warnings') or '')[:300])
    except Exception as e:
        print('commons search failed', q, e); return out
    for p in pages:
        if len(out) >= n: break
        ii = (p.get('imageinfo') or [{}])[0]; m = ii.get('extmetadata', {})
        lic = strip(m.get('LicenseShortName', {}).get('value'))
        if not OKLIC.match(lic) or ii.get('width', 0) < 1000 or ii.get('width', 0) < ii.get('height', 1) * 1.15:
            print('  skip', p.get('title', '')[:50], '|', lic, '|', ii.get('width'), ii.get('height')); continue
        if not re.search(r'\.jpe?g$', ii.get('url', '').split('?')[0], re.I):   # Commons URLs carry a ?utm_ query string
            print('  not jpg', ii.get('url', '')[-40:]); continue
        artist = strip(m.get('Artist', {}).get('value'))[:80] or strip(m.get('Credit', {}).get('value'))[:80] or 'Wikimedia Commons'
        out.append(dict(url=ii.get('thumburl') or ii['url'], source='Wikimedia Commons', title=p['title'].replace('File:', '')[:140],
                        desc=strip(m.get('ImageDescription', {}).get('value'))[:300], credit=artist, license=lic,
                        page=ii.get('descriptionurl', ''), date=strip(m.get('DateTimeOriginal', {}).get('value'))[:20]))
    return out
queries = json.loads(os.environ['QUERIES']); cands = []; seen = set()
for q in queries:
    found = nasa(q) + commons(q); print('query', repr(q), 'found', len(found), [c['source'][:4] + ':' + c['url'][-40:] for c in found])
    for c in found:
        if c['url'] in seen or len(cands) >= 8: continue
        seen.add(c['url'])
        try:
            im = Image.open(io.BytesIO(get(c['url'], raw=True))).convert('RGB')
        except Exception as e:
            print('download failed', c['url'], e); continue
        if im.width < 1000 or im.width < im.height * 1.15:
            print('  too small or not landscape', im.size, c['url'][-50:]); continue
        if im.width > 1600: im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        c['file'] = f'c{len(cands)+1}.jpg'; c['w'], c['h'] = im.size; c['query'] = q
        im.save(os.path.join(OUT, c['file']), quality=88); cands.append(c); print('saved', c['file'], c['source'], c['title'])
json.dump(cands, open(os.path.join(OUT, 'candidates.json'), 'w'), indent=1, ensure_ascii=False)
print(len(cands), 'candidates')
