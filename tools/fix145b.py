"""Nov 16, after publication (Garret: the drawn cover is "embarrassing"; use a real picture of Voyager).
Swap the drawing for NASA's rendering, fetched by cover.yml, credited."""
import json
from PIL import Image
im = Image.open('/home/claude/site/spool/cover/c2.jpg').convert('RGB')   # 1600x1200, NASA/JPL-Caltech, "Model of Voyager Artist Concept"
c = im.crop((60, 150, 1600, 1016)); c = c.resize((1500, round(c.height * 1500 / c.width)), Image.LANCZOS); c.save('/home/claude/plate145.jpg', quality=88); print(c.size)
p = '/home/claude/site/data/edition-2026-11-16.json'; e = json.load(open(p)); s = e['body_html']
i = s.find('<svg viewBox="0 0 750 375"'); j = s.find('</svg>', i) + 6; assert i > 0 and 'space probe' in s[i:j]
s = s[:i] + '<img src="__PLATE__" alt="The Voyager spacecraft, with its large dish antenna and long instrument boom, in a NASA rendering">' + s[j:]
def R(a, b):
    global s
    assert s.count(a) == 1, a; s = s.replace(a, b)
R('<div class="plate-sub">A light-day from home</div>', '<div class="plate-sub">Voyager, in a NASA rendering. Image: NASA/JPL-Caltech</div>')
R('<div class="plate-cap">Plate I &middot; The Family Album</div>', '<div class="plate-cap">The Cover</div>')
e['body_html'] = s; e['plate_path'] = '/home/claude/plate145.jpg'; e['plate_caption'] = 'Voyager, in a NASA rendering. Image: NASA/JPL-Caltech'
for q in [p, '/home/claude/edition-2026-11-16.json']: json.dump(e, open(q, 'w'), ensure_ascii=False, indent=1)
