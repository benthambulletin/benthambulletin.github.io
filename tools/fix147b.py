"""Nov 18, after publication: the cover search was fixed (it had been dropping every Wikimedia Commons photo) and today's
paper, published without a cover, gets one: the Erie Canal at Gateway Harbor, from Commons, credited."""
import json
from PIL import Image
im = Image.open('/home/claude/site/spool/cover/c1.jpg').convert('RGB')
c = im.resize((1500, round(im.height * 1500 / im.width)), Image.LANCZOS); c.save('/home/claude/plate147.jpg', quality=88); print(c.size)
y = json.load(open('/home/claude/site/data/edition-2026-11-17.json'))['body_html']
a = y.find('<div class="plate-wrap">'); b = y.find('<div class="part"><span>The News</span></div>'); blk = y[a:b]; assert 0 < a < b
i = blk.find('<img src="__PLATE__"'); j = blk.find('>', i) + 1
CAP = 'The Erie Canal at Gateway Harbor, seen from North Tonawanda, in a file photo. Photo: Andre Carrotflower, CC BY-SA 4.0'
blk = blk[:i] + '<img src="__PLATE__" alt="The Erie Canal at Gateway Harbor under a blue sky, seen from the North Tonawanda side">' + blk[j:]
assert blk.count('<div class="plate-sub">A test drive at the store</div>') == 1 and blk.count('Plate I &middot; The Family Album') == 1
blk = blk.replace('<div class="plate-sub">A test drive at the store</div>', '<div class="plate-sub">%s</div>' % CAP).replace('Plate I &middot; The Family Album', 'The Cover')
p = '/home/claude/site/data/edition-2026-11-18.json'; e = json.load(open(p)); s = e['body_html']
k = s.find('<div class="part"><span>The News</span></div>'); assert k > 0 and 'plate-wrap' not in s
e['body_html'] = s[:k] + blk + s[k:]; e['plate_path'] = '/home/claude/plate147.jpg'; e['plate_caption'] = CAP
for q in [p, '/home/claude/edition-2026-11-18.json']: json.dump(e, open(q, 'w'), ensure_ascii=False, indent=1)
