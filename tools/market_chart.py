"""The S&P 500 chart for a market story (Garret, Nov 20: "put the stock market graph in").
Drawn by the paper from data/market.json (daily closes from FRED); never a screenshot of another outlet's chart.

    from market_chart import market_chart
    html = market_chart(json.load(open('site/data/market.json')), year=2026)

Returns a <div class="line"> label plus an inline svg; put it inside the story, after the first paragraph.
Check `last` in market.json before writing: the chart and the story must end on the same trading day.
"""
import datetime

def market_chart(m, year=None, label="S&amp;P 500, daily close"):
    rows = [(datetime.date.fromisoformat(d), v) for d, v in m["closes"]]
    if year: rows = [r for r in rows if r[0].year == year]
    W, H, L, Rm, T, B = 640, 300, 46, 64, 16, 30
    d0, d1 = rows[0][0], rows[-1][0]
    lo = min(v for _, v in rows); hi = max(v for _, v in rows)
    step = 500 if hi - lo > 900 else 250 if hi - lo > 400 else 100
    y0 = int(lo // step) * step; y1 = (int(hi // step) + 1) * step
    X = lambda d: L + (W - L - Rm) * (d - d0).days / max(1, (d1 - d0).days)
    Y = lambda v: T + (H - T - B) * (1 - (v - y0) / (y1 - y0))
    o = ['<svg class="mkt" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Line chart of the S&amp;P 500" style="display:block;width:100%%;height:auto;margin:.4rem 0 .2rem">' % (W, H)]
    for g in range(y0, y1 + 1, step):
        o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#d3b88f" stroke-width="1" stroke-dasharray="2 4"/>' % (L, W - Rm, Y(g), Y(g)))
        o.append('<text x="%d" y="%.1f" font-family="Archivo,Arial,sans-serif" font-size="13" fill="#664a2c" text-anchor="end">%s</text>' % (L - 6, Y(g) + 4, format(g, ",")))
    mon = d0.replace(day=1)
    while mon <= d1:
        if mon.month % 2 == 1:
            o.append('<text x="%.1f" y="%d" font-family="Archivo,Arial,sans-serif" font-size="13" fill="#664a2c">%s</text>' % (max(X(mon), L), H - 8, mon.strftime("%b")))
        mon = (mon.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
    pts = " ".join("%.1f,%.1f" % (X(d), Y(v)) for d, v in rows)
    o.append('<polyline points="%s" fill="none" stroke="#2f5e3e" stroke-width="2.5" stroke-linejoin="round"/>' % pts)
    hd, hv = max(rows, key=lambda r: r[1]); ld, lv = rows[-1]
    o.append('<circle cx="%.1f" cy="%.1f" r="4" fill="#24170c"/>' % (X(hd), Y(hv)))
    o.append('<text x="%.1f" y="%.1f" font-family="Archivo,Arial,sans-serif" font-size="13" font-weight="700" fill="#24170c" text-anchor="end">High %s</text>' % (X(hd) - 8, Y(hv) - 4, format(round(hv), ",")))
    o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#9c3216"/>' % (X(ld), Y(lv)))
    o.append('<text x="%.1f" y="%.1f" font-family="Archivo,Arial,sans-serif" font-size="14" font-weight="700" fill="#9c3216">%s</text>' % (X(ld) + 9, Y(lv) + 5, format(round(lv), ",")))
    o.append("</svg>")
    cap = '<div class="line"><span class="lbl t">%s</span> through %s. Data: %s.</div>' % (label, ld.strftime("%A, %b. ") + str(ld.day), (m.get("source") or "Yahoo Finance").split(",")[0])
    return "".join(o) + cap
