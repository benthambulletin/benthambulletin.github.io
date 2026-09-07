"""Bentham Bulletin site generator.
Usage: python3 site.py <edition.json>   (see EDITION below for schema)
Writes into ./site/: index.html, YYYY/MM/DD/index.html, archive/index.html, issues.json
"""
import json, os, sys, shutil, datetime

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

CSS = r"""
@font-face{font-family:'PF';src:url(/assets/fonts/PlayfairDisplay.ttf);font-weight:100 900;font-display:swap}
@font-face{font-family:'PFI';src:url(/assets/fonts/PlayfairDisplay-Italic.ttf);font-weight:100 900;font-style:italic;font-display:swap}
@font-face{font-family:'LO';src:url(/assets/fonts/Lora.ttf);font-weight:100 900;font-display:swap}
@font-face{font-family:'LOI';src:url(/assets/fonts/Lora-Italic.ttf);font-weight:100 900;font-style:italic;font-display:swap}
@font-face{font-family:'AR';src:url(/assets/fonts/Archivo.ttf);font-weight:100 900;font-display:swap}
:root{--paper:#fbf5e4;--ink:#1c170f;--red:#c8302f;--teal:#0e8a8a;--gold:#e8b100;--soft:#5f5238;--rule:#d6cbaf}
*{box-sizing:border-box}
html{background:#ece4d1;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);font-family:'LO',Georgia,serif;color:var(--ink);font-size:1.15rem;line-height:1.5;font-weight:480}
.page{max-width:44rem;margin:0 auto;padding:1.2rem 1.1rem 2rem}
a{color:inherit}
.kicker{display:flex;justify-content:space-between;font-family:'AR';font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:.4rem}
.hr-thick{height:4px;background:var(--ink)}
.dbl{margin:1.4rem 0 .9rem}.dbl-tight{margin:.7rem 0 .6rem}
.dbl .a,.dbl-tight .a{height:3px;background:var(--ink)}
.dbl .b,.dbl-tight .b{height:1px;background:var(--ink);margin-top:3px}
.the{text-align:center;font-family:'PFI';font-style:italic;font-size:1.3rem;color:var(--red);margin-top:.6rem}
.mast{text-align:center;font-family:'PF';font-weight:800;font-size:clamp(2.4rem,11vw,4.4rem);line-height:.98;margin:0 0 .2rem;letter-spacing:-.02em}
.tag{text-align:center;font-family:'AR';font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--teal);font-weight:600}
.orn{text-align:center;color:var(--gold);font-size:1rem;letter-spacing:.9em;margin:.5rem 0 .4rem}
.dateline{text-align:center;font-family:'AR';font-weight:800;font-size:1.1rem;letter-spacing:.14em;text-transform:uppercase}
.place{text-align:center;font-family:'LOI';font-style:italic;font-size:.95rem;color:var(--soft);margin-top:.2rem}
.tiles{display:flex}
.tile{flex:1;text-align:center;padding:.5rem .2rem;border-right:1px solid var(--rule)}
.tile:last-child{border-right:0}
.tile .v{font-family:'PF';font-weight:800;font-size:clamp(1.4rem,6vw,2.2rem);line-height:1.05}
.tile .k{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);margin-top:.15rem}
.tile.good .v{color:var(--teal)}.tile.urg .v{color:var(--red)}
.plate-wrap{text-align:center;margin:1rem 0 0}
.frame{display:block;position:relative;padding:.6rem;border:2px solid var(--ink)}
.frame img{display:block;width:100%;height:auto}
.tick{position:absolute;width:.9rem;height:.9rem;border:2px solid var(--red)}
.tl{top:-2px;left:-2px;border-right:0;border-bottom:0}.tr{top:-2px;right:-2px;border-left:0;border-bottom:0}
.bl{bottom:-2px;left:-2px;border-right:0;border-top:0}.br{bottom:-2px;right:-2px;border-left:0;border-top:0}
.plate-cap{font-family:'AR';font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:.7rem}
.plate-sub{font-family:'LOI';font-style:italic;font-size:1.05rem;color:var(--soft);margin-top:.3rem;line-height:1.4}
.sec{text-align:center;font-family:'AR';font-weight:800;font-size:.95rem;letter-spacing:.3em;text-transform:uppercase;margin:0 0 .9rem;color:var(--red)}
.sec:nth-of-type(even){color:var(--teal)}
.sec .o{color:var(--gold);margin:0 .7rem;letter-spacing:0}
.wx{display:flex;align-items:flex-start;gap:1rem;margin-bottom:.8rem}
.bigtemp{font-family:'PF';font-weight:800;font-size:clamp(3.4rem,17vw,5.2rem);line-height:.82;letter-spacing:-.04em;white-space:nowrap}
.bigtemp sup{font-size:.36em;font-weight:500;vertical-align:top;position:relative;top:.15em}
.wxtext{padding-top:.2rem;font-size:1.05em}
.lede{display:block;font-family:'LOI';font-style:italic;font-size:1.1em;color:var(--soft);margin-bottom:.3rem}
.pnote{font-family:'LO';font-size:1rem;line-height:1.5;color:var(--ink);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.7rem .2rem;margin:.2rem 0 1rem}.pnote b{color:var(--red);font-family:'PF'}
.note{border:2px solid var(--teal);color:var(--teal);font-family:'AR';font-weight:700;font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;padding:.45rem .7rem;display:inline-block;margin-bottom:.8rem}
.towns{display:flex;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);margin-bottom:.7rem}
.town{flex:1;text-align:center;padding:.6rem .2rem;border-right:1px solid var(--rule)}
.town:last-child{border-right:0}
.town .n{font-family:'AR';font-weight:800;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal)}
.town .t{font-family:'PF';font-weight:700;font-size:1.9rem;margin-top:.15rem}
.town .t sup{font-size:.45em;vertical-align:top;position:relative;top:.2em}
.town .d{font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.1rem}
.line{margin-bottom:.5rem}
.lbl{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;margin-right:.3rem}
.lbl.r{color:var(--red)}.lbl.t{color:var(--teal)}
.baro-top{display:flex;align-items:center;gap:.9rem;margin-bottom:.4rem;flex-wrap:wrap}
.dial{border:2px solid var(--teal);color:var(--teal);font-family:'AR';font-weight:700;font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;padding:.4rem .65rem;white-space:nowrap}
.press{font-family:'PF';font-weight:800;font-size:2.3rem;letter-spacing:-.02em}
.trend{font-family:'LOI';font-style:italic;font-size:1.15rem;color:var(--red)}
.baro svg{display:block;width:100%;height:auto;margin:.2rem 0}
.ledger{display:flex;gap:1rem;align-items:center}
.ledger .cap{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);text-align:center}
.ledger .big{font-family:'PF';font-weight:800;font-size:clamp(2.2rem,10vw,3.4rem);color:var(--red);text-align:center;line-height:1.05}
.ledger .txt{flex:1}
.wire{display:flex;gap:.7rem;padding:.55rem 0;border-bottom:1px solid #e5dcc4}
.wire:last-child{border-bottom:0}
.wire .num{font-family:'PF';font-weight:800;font-size:1.5rem;color:var(--red);min-width:1.3rem;text-align:right;line-height:1.1}
.wire h3{font-family:'PF';font-weight:800;font-size:1.3rem;margin:0 0 .15rem;line-height:1.2}
.wire p{margin:0;font-size:.98em}
.touch-head{text-align:center;font-family:'PF';font-weight:700;font-size:1.5rem;color:var(--red);margin-bottom:.6rem}
.cards{display:flex;gap:.6rem;margin-top:.6rem}
.card{flex:1;border-top:2px solid var(--ink);padding-top:.35rem;min-width:0}
.card .h{font-family:'AR';font-weight:700;font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
.card .m{font-family:'PF';font-weight:700;font-size:1.05rem;margin-top:.1rem}
.card .s{font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft)}
.qbox{border-left:5px solid var(--gold);padding:.2rem 0 .2rem .8rem}
.fam{border:2px solid var(--gold);padding:.65rem .9rem}
.colo{text-align:center;margin-top:.3rem}
.colo .s{font-family:'LOI';font-style:italic;font-size:.82rem;color:var(--soft);line-height:1.5}
.sig{font-family:'PFI';font-style:italic;font-size:1.8rem;margin:.5rem 0 .2rem}
.nav{display:flex;justify-content:space-between;font-family:'AR';font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-top:1rem}
.nav a{text-decoration:none;font-weight:700}
.nav a:hover{color:var(--red)}
.strip5{display:flex;border-top:1px solid var(--rule);border-bottom:1px solid var(--ink);margin:.2rem 0 .7rem}
.strip5 div{flex:1;text-align:center;padding:.45rem .1rem;border-right:1px solid var(--rule)}
.strip5 div:last-child{border-right:0}
.strip5 .d{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft)}
.strip5 .i{font-size:1.3rem;line-height:1.3;color:var(--red)}
.strip5 .h{font-family:'PF';font-weight:700;font-size:1.15rem}
.strip5 .w{font-family:'LOI';font-style:italic;font-size:.7rem;color:var(--soft)}
.sky{display:flex;gap:1rem;align-items:center;margin-bottom:.6rem}
.sky svg{width:5rem;height:5rem;flex:none}
.stars{margin-top:.4rem}
.star{display:flex;gap:.6rem;padding:.35rem 0;border-bottom:1px solid #e5dcc4}
.star:last-child{border-bottom:0}
.star .sg{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--teal);min-width:4.6rem;padding-top:.3rem}
.star .who{font-family:'LOI';font-style:italic;color:var(--soft);font-size:.85em}
.tbl{width:100%;border-collapse:collapse;font-size:.85em;margin:.5rem 0}
.tbl th{font-family:'AR';font-weight:700;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);text-align:left;border-bottom:1px solid var(--ink);padding:.25rem .3rem}
.tbl td{padding:.3rem .3rem;border-bottom:1px solid #e5dcc4}
.tbl td.n{text-align:right;font-family:'AR'}
.tbl tr.us td{font-weight:700;color:var(--red)}
.cal{list-style:none;padding:0;margin:.4rem 0 0}
.cal li{display:flex;gap:.7rem;padding:.25rem 0}
.cal .dt{font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--red);min-width:4.2rem;padding-top:.3rem}
.ballot{border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);padding:.5rem 0;font-family:'AR';font-weight:700;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;text-align:center}
.ballot b{color:var(--red)}
.ask{font-family:'LOI';font-style:italic;color:var(--teal);font-size:.95em;margin-top:.5rem}
@media (max-width:480px){
 .kicker{font-size:.58rem;letter-spacing:.12em}
 .sec{letter-spacing:.18em;font-size:.85rem}
 .sec .o{margin:0 .4rem}
 .tile .k{font-size:.55rem;letter-spacing:.08em}
 .cards{flex-direction:column;gap:.4rem}
 .card{display:flex;align-items:baseline;gap:.5rem;flex-wrap:wrap;border-top:1px solid var(--rule);padding-top:.3rem}
 .card .h{min-width:100%}
}
/* archive */
.arch{list-style:none;padding:0;margin:0}
.arch li{display:flex;gap:.9rem;align-items:center;padding:.7rem 0;border-bottom:1px solid #e5dcc4}
.arch img{width:6rem;height:4rem;object-fit:cover;border:1px solid var(--ink);flex:none}
.arch a{text-decoration:none}
.arch .d{font-family:'PF';font-weight:700;font-size:1.1rem}
.arch .no{font-family:'AR';font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--soft)}
.arch .c{font-family:'LOI';font-style:italic;color:var(--soft);font-size:.95rem}
"""

import hashlib
def shell(title, body, og_image=None, desc="A daily almanac for the family"):
    CSSV = hashlib.md5(CSS.encode()).hexdigest()[:8]
    og = f'<meta property="og:image" content="https://benthambulletin.github.io{og_image}">' if og_image else ''
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">{og}
<meta property="og:type" content="article">
<link rel="stylesheet" href="/assets/style.css?v={CSSV}">
<link rel="icon" href="/assets/favicon.svg"></head><body><div class="page">
{body}
</div></body></html>"""

def build(edition):
    """edition: dict with keys date (YYYY-MM-DD), no, body_html (the paper from kicker to colophon,
    with <img src="__PLATE__">), plate_path (jpg on disk), plate_caption, headline."""
    d = datetime.date.fromisoformat(edition['date'])
    slug = d.strftime('%Y/%m/%d')
    outdir = os.path.join(SITE, slug); os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(SITE, 'assets'), exist_ok=True)
    os.makedirs(os.path.join(SITE, 'archive'), exist_ok=True)
    open(os.path.join(SITE,'assets','style.css'),'w').write(CSS)
    plate_rel = f'/{slug}/plate.jpg'
    shutil.copy(edition['plate_path'], os.path.join(outdir,'plate.jpg'))
    # manifest
    mpath = os.path.join(SITE,'issues.json')
    issues = json.load(open(mpath)) if os.path.exists(mpath) else []
    issues = [i for i in issues if i['date'] != edition['date']]
    issues.append({'date':edition['date'],'no':edition['no'],'slug':slug,'plate':plate_rel,
                   'caption':edition['plate_caption'],'headline':edition['headline']})
    issues.sort(key=lambda i:i['date'], reverse=True)
    json.dump(issues, open(mpath,'w'), indent=1)
    # prev/next nav
    idx = [i['date'] for i in issues].index(edition['date'])
    newer = issues[idx-1] if idx>0 else None
    older = issues[idx+1] if idx+1 < len(issues) else None
    nav = '<div class="nav">'
    nav += f'<a href="/{older["slug"]}/">&larr; {older["date"]}</a>' if older else '<span></span>'
    nav += '<a href="/archive/">Archive</a>'
    nav += f'<a href="/{newer["slug"]}/">{newer["date"]} &rarr;</a>' if newer else '<a href="/">Today</a>'
    nav += '</div>'
    pv = hashlib.md5(open(edition['plate_path'],'rb').read()).hexdigest()[:8]
    body = edition['body_html'].replace('__PLATE__', plate_rel+'?v='+pv) + nav
    title = f"The Bentham Bulletin · No. {edition['no']} · {d.strftime('%A, %B %-d, %Y')}"
    html = shell(title, body, plate_rel, edition['headline'])
    open(os.path.join(outdir,'index.html'),'w').write(html)
    # front page = newest issue
    newest = issues[0]
    if newest['date'] == edition['date']:
        open(os.path.join(SITE,'index.html'),'w').write(html)
    # archive
    items = ''.join(
        f'<li><a href="/{i["slug"]}/"><img src="{i["plate"]}" alt=""></a><div>'
        f'<div class="no">Vol. I &middot; No. {i["no"]}</div>'
        f'<a href="/{i["slug"]}/"><div class="d">{datetime.date.fromisoformat(i["date"]).strftime("%A, %B %-d, %Y")}</div></a>'
        f'<div class="c">{i["caption"]}</div></div></li>' for i in issues)
    abody = f"""<div class="kicker"><span>The Bentham Bulletin</span><span>Back Issues</span></div>
<div class="hr-thick"></div>
<div class="the">The</div><h1 class="mast">Archive</h1>
<div class="tag">Every edition, newest first</div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<ul class="arch">{items}</ul>
<div class="nav"><span></span><a href="/">Today's paper &rarr;</a></div>"""
    open(os.path.join(SITE,'archive','index.html'),'w').write(shell('The Bentham Bulletin · Archive', abody))
    open(os.path.join(SITE,'assets','favicon.svg'),'w').write(
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#f5e9bc"/>'
      '<text x="32" y="46" font-family="Georgia,serif" font-weight="700" font-size="40" text-anchor="middle" fill="#c8302f">B</text></svg>')
    return slug

if __name__ == '__main__':
    ed = json.load(open(sys.argv[1]))
    print(build(ed))
