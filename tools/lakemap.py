"""Lake map for the Weather Glass (Garret, Nov 9: "a small map with the temperatures on the lakes").
lake_map(erie, ontario, towns, asof) -> inline SVG. towns = [(name, dawn_temp, high)] for
North Tonawanda, Dunkirk, Scottsville. Shapes are simplified from real coordinates."""
X0, X1, Y0, Y1, W, H = -80.05, -77.35, 42.15, 43.72, 360, 230
def P(lon, lat): return ((lon - X0) / (X1 - X0) * W, (Y1 - lat) / (Y1 - Y0) * H)
def poly(pts): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in (P(*p) for p in pts))
ERIE = [(-80.1,42.12),(-79.76,42.27),(-79.5,42.39),(-79.33,42.49),(-79.15,42.57),(-79.0,42.68),(-78.92,42.8),(-78.89,42.88),(-79.0,42.9),(-79.25,42.87),(-79.6,42.86),(-80.1,42.83)]
ONT = [(-79.06,43.26),(-78.6,43.37),(-78.2,43.375),(-77.9,43.36),(-77.6,43.26),(-77.3,43.28),(-77.3,43.7),(-79.45,43.7),(-79.38,43.63),(-79.6,43.45),(-79.78,43.29),(-79.4,43.2),(-79.06,43.26)]
TOWNS = {'North Tonawanda': (-78.86, 43.04), 'Dunkirk': (-79.33, 42.48), 'Scottsville': (-77.75, 43.02)}
def lake_map(erie, ontario, towns, asof):
    rx, ry = P(-78.9, 42.88); mx, my = P(-79.06, 43.26)
    s = [f'<svg class="lakemap" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Map: Lake Erie {erie} degrees, Lake Ontario {ontario} degrees; dawn temperatures ' + ', '.join(f'{n} {t}' for n, t, _ in towns) + '" style="display:block;width:100%;max-width:440px;height:auto;margin:.3rem auto .2rem">',
         f'<rect width="{W}" height="{H}" fill="#efe3c8" rx="6"/>',
         f'<polygon points="{poly(ERIE)}" fill="#9cc3cf" stroke="#5f8f9c" stroke-width="1"/>',
         f'<polygon points="{poly(ONT)}" fill="#9cc3cf" stroke="#5f8f9c" stroke-width="1"/>',
         f'<path d="M{rx:.1f} {ry:.1f} C{rx-6:.1f} {ry-30:.1f},{mx+4:.1f} {my+40:.1f},{mx:.1f} {my:.1f}" fill="none" stroke="#5f8f9c" stroke-width="2"/>']
    ex, ey = P(-79.55, 42.62); ox, oy = P(-78.45, 43.56)
    for x, y, name, t in ((ex, ey, 'LAKE ERIE', erie), (ox, oy, 'LAKE ONTARIO', ontario)):
        s.append(f'<text x="{x:.1f}" y="{y-14:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="8.5" letter-spacing="1.5" fill="#2f5f6c">{name}</text>'
                 f'<text x="{x:.1f}" y="{y+10:.1f}" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-weight="700" font-size="24" fill="#1f4652">{t}&deg;</text>')
    for name, t, hi in towns:
        x, y = P(*TOWNS[name])
        lx, anchor, dy = (x + 7, 'start', 0) if name != 'Scottsville' else (x, 'middle', 22)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#9c3216" stroke="#fbf5e4" stroke-width="1.2"/>'
                 f'<text x="{lx:.1f}" y="{y-2+dy:.1f}" text-anchor="{anchor}" font-family="Archivo,Arial" font-size="8" letter-spacing=".5" fill="#24170c">{name.upper()}</text>'
                 f'<text x="{lx:.1f}" y="{y+11+dy:.1f}" text-anchor="{anchor}" font-family="Lora,Georgia,serif" font-size="11" fill="#24170c"><tspan font-weight="700">{t}&deg;</tspan><tspan font-size="9" fill="#6b5a48"> now, high {hi}&deg;</tspan></text>')
    s.append(f'<text x="{W-6}" y="{H-6}" text-anchor="end" font-family="Lora,Georgia,serif" font-style="italic" font-size="8.5" fill="#6b5a48">Lake temperatures {asof}, NWS Buffalo</text></svg>')
    return ''.join(s)
if __name__ == '__main__':
    print(lake_map(58, 58, [('North Tonawanda', 46, 52), ('Dunkirk', 48, 52), ('Scottsville', 46, 51)], "Sunday"))
