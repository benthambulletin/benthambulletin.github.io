"""Nov 15, after publication: Garret's photo (7:55 a.m., "Add for today") replaces the drawn cover."""
import json
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open('/mnt/user-data/attachments/001a10af-13f9-5479-8fec-28bf86d9c496/b24c5862-image.jpg')).convert('RGB')
W, H = im.size; print(W, H)
box = (int(W * .145), int(H * .20), int(W * .905), int(H * .775))
c = im.crop(box); c = c.resize((1500, round(c.height * 1500 / c.width)), Image.LANCZOS); c.save('/home/claude/plate144.jpg', quality=88); print(c.size)
p = '/home/claude/site/data/edition-2026-11-15.json'; e = json.load(open(p)); s = e['body_html']
i = s.find('<svg viewBox="0 0 750 375"'); j = s.find('</svg>', i) + 6; assert i > 0 and j > i and 'football' in s[i:j]
s = s[:i] + '<img src="__PLATE__" alt="A boy in mid-air, jumping off the back of a gray couch in a living room">' + s[j:]
a = '<div class="plate-sub">Game day under a gray sky</div>'; assert s.count(a) == 1
s = s.replace(a, '<div class="plate-sub">Liftoff from the couch</div>')
e['body_html'] = s; e['plate_path'] = '/home/claude/plate144.jpg'; e['plate_caption'] = 'Liftoff from the couch'
for q in [p, '/home/claude/edition-2026-11-15.json']: json.dump(e, open(q, 'w'), ensure_ascii=False, indent=1)
