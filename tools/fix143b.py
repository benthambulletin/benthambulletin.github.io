"""Nov 14, after publication (Garret: the 24-hour curve "needs more data points... it's bare"; mock approved, "I love it").
Swap the sparkline for tools/curve.py's fuller chart."""
import json, re, sys
sys.path.insert(0, '/home/claude/site/tools'); from curve import curve
p = '/home/claude/site/data/edition-2026-11-14.json'; e = json.load(open(p))
f = json.load(open('/home/claude/site/data/forecast.json'))
new = curve(f['towns']['North Tonawanda']['hourly'], 7 * 60 + 6, 16 * 60 + 52)
s, k = re.subn(r'<svg viewBox="0 0 320 62".*?</svg>\n', lambda m: new, e['body_html'], count=1, flags=re.S); assert k == 1
e['body_html'] = s
for q in [p, '/home/claude/edition-2026-11-14.json']: json.dump(e, open(q, 'w'), ensure_ascii=False, indent=1)
