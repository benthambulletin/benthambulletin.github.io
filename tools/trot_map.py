# Turkey Trot feature: schematic map (old vs new) + guide. Schematic: east-west stretched 3x, not to scale.
LAT0, LAT1, LON0, LON1 = 42.957, 42.871, -78.888, -78.858
W, H = 340, 470
def P(lat, lon):
    x = 120 + (lon - LON0) / (LON1 - LON0) * (W - 230)
    y = 64 + (LAT0 - lat) / (LAT0 - LAT1) * (H - 100)
    return round(x,1), round(y,1)
pts = {
 'tacoma': (42.9525,-78.8680), 'gates': (42.9166,-78.8693), 'delnorth': (42.9012,-78.8737),
 'niagsq': (42.8866,-78.8784), 'cc': (42.8879,-78.8723), 'start': (42.8950,-78.8755),
 'finish': (42.8869,-78.8743), 'keybank': (42.8750,-78.8764), 'ferrylin': (42.9133,-78.8672),
 'mainut': (42.9040,-78.8690),
}
p = {k: P(*v) for k,v in pts.items()}
def path(*keys): return 'M ' + ' L '.join(f'{p[k][0]},{p[k][1]}' for k in keys)
rust, ink, gray, green, blue = '#9c3216', '#24170c', '#b9a585', '#2f5e3e', '#5b87a8'
svg = f'''<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:340px;display:block;margin:0 auto" xmlns="http://www.w3.org/2000/svg" font-family="Archivo,Arial,sans-serif">
<rect x="0" y="0" width="{W}" height="{H}" fill="#f3e6cc" rx="6"/>
<path d="{path('tacoma','gates')}" stroke="{gray}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="2 7"/>
<path d="{path('gates','delnorth','niagsq')}" stroke="{rust}" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M {p['start'][0]},{p['start'][1]} C {p['start'][0]+40},{p['start'][1]-30} {p['mainut'][0]+30},{p['mainut'][1]} {p['ferrylin'][0]},{p['ferrylin'][1]} L {p['gates'][0]},{p['gates'][1]}" stroke="{rust}" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="9 6"/>
<path d="M {p['niagsq'][0]},{p['niagsq'][1]} L {p['finish'][0]},{p['finish'][1]}" stroke="{rust}" stroke-width="5" fill="none" stroke-linecap="round"/>
<circle cx="{p['tacoma'][0]}" cy="{p['tacoma'][1]}" r="6" fill="#fff" stroke="{gray}" stroke-width="3"/>
<text x="{p['tacoma'][0]-12}" y="{p['tacoma'][1]+1}" font-size="12" fill="{ink}" font-weight="700" text-anchor="end">Old start</text>
<text x="{p['tacoma'][0]-12}" y="{p['tacoma'][1]+15}" font-size="10" fill="{ink}" text-anchor="end">Delaware &amp; Tacoma,</text>
<text x="{p['tacoma'][0]-12}" y="{p['tacoma'][1]+28}" font-size="10" fill="{ink}" text-anchor="end">the Target lot</text>
<circle cx="{p['gates'][0]}" cy="{p['gates'][1]}" r="4" fill="{rust}"/>
<text x="{p['gates'][0]-10}" y="{p['gates'][1]+4}" font-size="10" fill="{ink}" text-anchor="end">Gates Circle</text>
<text x="{p['delnorth'][0]-10}" y="{p['delnorth'][1]+4}" font-size="10" fill="{rust}" font-weight="700" text-anchor="end">back on Delaware</text>
<text x="{p['mainut'][0]+34}" y="{p['mainut'][1]-6}" font-size="10" fill="{rust}" font-weight="700">out on the</text>
<text x="{p['mainut'][0]+34}" y="{p['mainut'][1]+7}" font-size="10" fill="{rust}" font-weight="700">east side</text>
<circle cx="{p['niagsq'][0]}" cy="{p['niagsq'][1]}" r="4" fill="{rust}"/>
<text x="{p['niagsq'][0]-10}" y="{p['niagsq'][1]+12}" font-size="10" fill="{ink}" text-anchor="end">Niagara Sq.</text>
<rect x="{p['start'][0]-6}" y="{p['start'][1]-6}" width="12" height="12" fill="{green}"/>
<text x="{p['start'][0]-12}" y="{p['start'][1]-2}" font-size="12" fill="{ink}" font-weight="700" text-anchor="end">Start</text>
<text x="{p['start'][0]-12}" y="{p['start'][1]+11}" font-size="10" fill="{ink}" text-anchor="end">Franklin at Chippewa</text>
<rect x="{p['cc'][0]-9}" y="{p['cc'][1]-7}" width="18" height="14" fill="{ink}"/>
<text x="{p['cc'][0]+14}" y="{p['cc'][1]+4}" font-size="12" fill="{ink}" font-weight="700">Convention Center</text>
<circle cx="{p['finish'][0]}" cy="{p['finish'][1]}" r="5" fill="{green}"/>
<text x="{p['cc'][0]+14}" y="{p['cc'][1]+17}" font-size="10" fill="{ink}">finish at Franklin &amp; W. Eagle</text>
<circle cx="{p['keybank'][0]}" cy="{p['keybank'][1]}" r="6" fill="{blue}"/>
<text x="{p['keybank'][0]+12}" y="{p['keybank'][1]+1}" font-size="11" fill="{ink}" font-weight="700">KeyBank Center lots</text>
<text x="{p['keybank'][0]+12}" y="{p['keybank'][1]+14}" font-size="10" fill="{ink}">shuttles to the start</text>
<g font-size="10" fill="{ink}"><line x1="16" y1="18" x2="34" y2="18" stroke="{rust}" stroke-width="4"/><text x="40" y="22">New 8K loop (dashed leg: see official map)</text>
<line x1="16" y1="36" x2="34" y2="36" stroke="{gray}" stroke-width="4" stroke-dasharray="2 5"/><text x="40" y="40">The old course's first half, now gone</text></g>
<text x="{W-8}" y="{H-10}" font-size="10" fill="{ink}" text-anchor="end">N &#8593;</text>
</svg>'''
open('/home/claude/trot/map.svg','w').write(svg)
print('ok')
