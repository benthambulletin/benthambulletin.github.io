#!/usr/bin/env python3
"""The Almanac Sky in one call (Nov 6): sun, moon, icon path, planets tonight, and the
moon-based Stars for every family sign.

    python3 site/tools/sky.py 2026-11-07

Rules it follows (CLAUDE.md "Sky"): lat 43.0438, lon -78.8659; Eastern time (EDT UTC-4,
EST UTC-5 from the first Sunday in November to the second Sunday in March); sun with
default refraction and horizon 0; moon with pressure 0 and horizon -0:34. The moon is
named by its constellation in the Sky line.

The Stars (Garret, Nov 6): every sign's line is built on the MOON, which changes daily.
For each sign it gives the moon's zodiac sign today and how that sits with the family
sign (same sign, sextile, square, trine, opposition, or no aspect), plus any aspect the
moon makes to a planet within 6 degrees at local noon. Write each horoscope from those.
"""
import sys, math, datetime as dt
import ephem

LAT, LON = '43.0438', '-78.8659'
SIGNS = 'Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio Sagittarius Capricorn Aquarius Pisces'.split()
FAMILY = {'Aries': 'Kaylani, Luka', 'Cancer': 'Gregg', 'Leo': 'Leah, Tommy', 'Virgo': 'Derek, Joanne',
          'Scorpio': 'Ariel, Claire, Garret'}
ASPECTS = {0: 'conjunct', 60: 'sextile', 90: 'square', 120: 'trine', 180: 'opposite'}
SIGN_REL = {0: 'in your sign', 2: 'sextile your sign', 3: 'square your sign', 4: 'trine your sign', 6: 'opposite your sign'}


def utc_offset(d):
    y = d.year
    # second Sunday in March, first Sunday in November
    mar = dt.date(y, 3, 8); mar += dt.timedelta(days=(6 - mar.weekday()) % 7)
    nov = dt.date(y, 11, 1); nov += dt.timedelta(days=(6 - nov.weekday()) % 7)
    return -4 if mar <= d < nov else -5


def main(day):
    d = dt.date.fromisoformat(day)
    off = utc_offset(d)
    loc = lambda e: (ephem.Date(e).datetime() + dt.timedelta(hours=off))
    fmt = lambda e: loc(e).strftime('%-I:%M %p').lower().replace('am', 'a.m.').replace('pm', 'p.m.') + ('' if loc(e).date() == d else loc(e).strftime(' %a'))
    midnight = ephem.Date(dt.datetime(d.year, d.month, d.day) - dt.timedelta(hours=off))
    noon = ephem.Date(dt.datetime(d.year, d.month, d.day, 12) - dt.timedelta(hours=off))

    o = ephem.Observer(); o.lat, o.lon = LAT, LON; o.elevation = 180
    o.date = midnight; o.horizon = '0'
    sun = ephem.Sun()
    sr, ss = o.next_rising(sun), o.next_setting(sun)
    o.date = midnight - 1; ys = o.next_setting(sun); yr = o.next_rising(sun)
    length = (ss - sr) * 1440; ylength = (ys - yr) * 1440
    print(f"SUN  rise {fmt(sr)}  set {fmt(ss)}  day {int(length // 60)}h {round(length % 60)}m  ({length - ylength:+.1f} min vs yesterday)")

    mo = ephem.Observer(); mo.lat, mo.lon = LAT, LON; mo.elevation = 180; mo.pressure = 0; mo.horizon = '-0:34'
    mo.date = midnight
    m = ephem.Moon()
    mr, ms = mo.next_rising(m), mo.next_setting(m)
    m.compute(noon)
    p = m.phase / 100
    waxing = ephem.next_full_moon(noon) < ephem.next_new_moon(noon)
    k = 46 * abs(2 * p - 1)
    sweep_term = (1 if p < .5 else 0) if not waxing else (0 if p < .5 else 1)
    if waxing:
        path = f"M50 4 A46 46 0 0 1 50 96 A{k:.1f} 46 0 0 {sweep_term} 50 4Z"
    else:
        path = f"M50 4 A46 46 0 0 0 50 96 A{k:.1f} 46 0 0 {sweep_term} 50 4Z"
    name = ('new' if p < .02 else 'full' if p > .98 else
            ('waxing ' if waxing else 'waning ') + ('crescent' if p < .48 else 'gibbous' if p > .52 else 'quarter'))
    print(f"MOON {name}, {round(p * 100)}% lit, constellation {ephem.constellation(m)[1]}; rise {fmt(mr)}  set {fmt(ms)}")
    print(f"     icon path (lit side {'right' if waxing else 'left'}): {path}")
    print(f"     next new {loc(ephem.next_new_moon(noon)):%a %b %-d}, next full {loc(ephem.next_full_moon(noon)):%a %b %-d}")

    # planets tonight: up at 7 p.m. or rising before midnight, above 10 degrees at some point 7 p.m.-midnight
    po = ephem.Observer(); po.lat, po.lon = LAT, LON; po.elevation = 180
    print("TONIGHT (7 p.m. to midnight):")
    for pl in ('Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn'):
        b = getattr(ephem, pl)()
        best = None
        for h in range(19, 24):
            po.date = ephem.Date(dt.datetime(d.year, d.month, d.day, h) - dt.timedelta(hours=off))
            b.compute(po)
            alt = math.degrees(b.alt)
            if best is None or alt > best[0]:
                best = (alt, math.degrees(b.az), h, b.mag)
        po.date = midnight + .5
        try:
            rise, sett = fmt(po.next_rising(b)), fmt(po.next_setting(b))
        except Exception:
            rise = sett = '-'
        if best[0] > 10:
            az = best[1]; compass = 'N NE E SE S SW W NW'.split()[int((az + 22.5) // 45) % 8]
            print(f"  {pl}: up, highest {best[0]:.0f} deg in the {compass} around {best[2] - 12} p.m., mag {best[3]:.1f}; rises {rise}, sets {sett}")
        else:
            print(f"  {pl}: not up in the evening (rises {rise}, sets {sett})")

    # Stars: the moon
    lon = {}
    for pl in ('Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'):
        b = getattr(ephem, pl)(); b.compute(noon)
        lon[pl] = math.degrees(ephem.Ecliptic(b, epoch=noon).lon)
    msign = SIGNS[int(lon['Moon'] // 30)]
    print(f"STARS: the moon is in {msign} (zodiac) at noon, {lon['Moon'] % 30:.0f} deg in")
    hits = []
    for pl, v in lon.items():
        if pl == 'Moon':
            continue
        diff = abs(lon['Moon'] - v) % 360; diff = min(diff, 360 - diff)
        for a, n in ASPECTS.items():
            if abs(diff - a) <= 6:
                hits.append(f"moon {n} {pl} ({abs(diff - a):.1f} deg; {pl} in {SIGNS[int(v // 30)]})")
    print("  moon aspects within 6 deg: " + ("; ".join(hits) if hits else "none"))
    for s, who in FAMILY.items():
        dist = (SIGNS.index(msign) - SIGNS.index(s)) % 12
        dist = min(dist, 12 - dist)
        print(f"  {s} ({who}): moon in {msign}, {SIGN_REL.get(dist, 'no classic aspect to your sign')}")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat())
