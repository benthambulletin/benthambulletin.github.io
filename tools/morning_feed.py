#!/usr/bin/env python3
"""Morning feed for the Bulletin: official forecasts and a headline scan.

Run by .github/workflows/morning.yml at about 6:30 a.m. Eastern, before the
6:59 build. Writes:
  data/forecast.json  NWS point forecast + latest observation for the three towns
  data/news.json      recent headlines from national, local and entertainment RSS feeds,
                      plus "body": the first paragraphs of each article (Garret, Oct 21: the build
                      session can't open news pages, so the feed fetches them here for real sourcing)
Every source is fetched independently; one failure never stops the rest, and
failures are recorded in the output so the editor knows what is missing.
"""
import json, re, html
import urllib.request
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "bentham-bulletin (noreply@anthropic.com)", "Accept": "application/geo+json, application/json, application/rss+xml, application/xml, text/xml, */*"}
TOWNS = {"North Tonawanda": (43.0387, -78.8642), "Dunkirk": (42.4795, -79.3339), "Scottsville": (43.0259, -77.7453)}
FEEDS = {
    "national": {
        "NPR News": "https://feeds.npr.org/1001/rss.xml",
        "NPR National": "https://feeds.npr.org/1003/rss.xml",
        "NPR Politics": "https://feeds.npr.org/1014/rss.xml",
        "PBS NewsHour": "https://www.pbs.org/newshour/feeds/rss/headlines",
        "BBC US & Canada": "https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
        "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
        "CBS News": "https://www.cbsnews.com/latest/rss/main",
    },
    "local": {
        "WIVB Buffalo": "https://www.wivb.com/feed/",
        "WKBW Buffalo": "https://www.wkbw.com/news/local-news.rss",
        "Rochester First": "https://www.rochesterfirst.com/feed/",
        "WXXI Rochester": "https://www.wxxinews.org/local-news.rss",
        "Dunkirk Observer": "https://www.observertoday.com/feed/",
        "Niagara Gazette": "https://www.niagara-gazette.com/search/?f=rss&t=article&c=news/local_news&l=50&s=start_time&sd=desc",
        "Lockport Journal": "https://www.lockportjournal.com/search/?f=rss&t=article&l=50&s=start_time&sd=desc",
        "WGRZ Buffalo": "https://www.wgrz.com/feeds/syndication/rss/news/local",
    },
    "entertainment": {
        "Variety": "https://variety.com/feed/",
        "Deadline": "https://deadline.com/feed/",
        "Billboard": "https://www.billboard.com/feed/",
        "Hollywood Reporter": "https://www.hollywoodreporter.com/feed/",
        "Us Weekly": "https://www.usmagazine.com/feed/",
        "Page Six": "https://pagesix.com/feed/",
        "E! News": "https://www.eonline.com/syndication/feeds/rssfeeds/topstories.xml",
        "Rolling Stone": "https://www.rollingstone.com/feed/",
        "TVLine": "https://tvline.com/feed/",
    },
    # Bills and Jets news for the midweek Gridiron (Garret, Nov 6).
    "sports": {
        "Buffalo Rumblings": "https://www.buffalorumblings.com/rss/index.xml",
        "Gang Green Nation": "https://www.ganggreennation.com/rss/index.xml",
        "ProFootballTalk": "https://www.nbcsports.com/profootballtalk.rss",
        "WGRZ Sports": "https://www.wgrz.com/feeds/syndication/rss/sports",
    },
}


def get(url, timeout=30, tries=3):
    import time, urllib.error
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < tries - 1:
                try: wait = min(90, int(e.headers.get('Retry-After') or 0))
                except (TypeError, ValueError): wait = 0
                time.sleep(max(wait, 30 * (i + 1))); continue
            raise
        except OSError:
            if i < tries - 1:
                time.sleep(5); continue
            raise


def forecasts():
    out = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "towns": {}, "errors": []}
    for town, (lat, lon) in TOWNS.items():
        try:
            pt = json.loads(get(f"https://api.weather.gov/points/{lat},{lon}"))["properties"]
            fc = json.loads(get(pt["forecast"]))["properties"]
            t = {"issued": fc.get("updateTime") or fc.get("generatedAt"),
                 "periods": [{"name": p["name"], "temp": p["temperature"], "wind": f'{p.get("windDirection","")} {p.get("windSpeed","")}'.strip(),
                              "pop": (p.get("probabilityOfPrecipitation") or {}).get("value"),
                              "short": p["shortForecast"], "detail": p["detailedForecast"]} for p in fc["periods"][:10]]}
            try:
                feats = json.loads(get(pt["observationStations"]))["features"]
                st = feats[0]["properties"]["stationIdentifier"]
                ob = json.loads(get(f"https://api.weather.gov/stations/{st}/observations/latest"))["properties"]
                c = (ob.get("temperature") or {}).get("value")
                t["observation"] = {"station": st, "time": ob.get("timestamp"), "text": ob.get("textDescription"),
                                    "temp_f": None if c is None else round(c * 9 / 5 + 32)}
                if c is None:
                    # The town's own station has no thermometer reading (Dunkirk, Nov 21): take the
                    # nearest station that does, and say which one, so the paper can name it.
                    for ft in feats[1:6]:
                        try:
                            s2 = ft["properties"]["stationIdentifier"]
                            o2 = json.loads(get(f"https://api.weather.gov/stations/{s2}/observations/latest"))["properties"]
                            c2 = (o2.get("temperature") or {}).get("value")
                            if c2 is not None:
                                t["observation"]["fallback"] = {"station": s2, "name": ft["properties"].get("name"),
                                    "time": o2.get("timestamp"), "text": o2.get("textDescription"), "temp_f": round(c2 * 9 / 5 + 32)}
                                break
                        except Exception:
                            continue
            except Exception as e:
                out["errors"].append(f"{town} observation: {e}")
            if town == "North Tonawanda":
                try:
                    hr = json.loads(get(pt["forecastHourly"]))["properties"]["periods"][:24]
                    t["hourly"] = [{"start": h["startTime"], "temp": h["temperature"], "short": h["shortForecast"], "pop": (h.get("probabilityOfPrecipitation") or {}).get("value")} for h in hr]
                except Exception as e:
                    out["errors"].append(f"hourly: {e}")
            out["towns"][town] = t
        except Exception as e:
            out["errors"].append(f"{town} forecast: {e}")
    return out


def lakes(out):
    """Lake temperatures from the NWS Buffalo lake page (Garret, Nov 6: run them daily).
    Stores the parsed readings and the page's own text so the build can check the date."""
    try:
        raw = get("https://www.weather.gov/buf/LakeTemp").decode("utf-8", "ignore")
        text = clean(raw)
        out["lakes"] = {"fetched_utc": out["generated_utc"], "text": text[:9000]}
        found = {}
        for name, pat in (("Lake Erie (Buffalo)", r"Buffalo[^0-9]{0,60}?(\d{2})\s*(?:&deg;|°|degrees|F\b)"),
                          ("Lake Ontario (Rochester)", r"Rochester[^0-9]{0,60}?(\d{2})\s*(?:&deg;|°|degrees|F\b)")):
            m = re.search(pat, text)
            if m:
                found[name] = int(m.group(1))
        out["lakes"]["readings"] = found
    except Exception as e:
        out["errors"].append(f"lakes: {e}")


NORMAL_STATIONS = {"North Tonawanda": "USW00014733", "Scottsville": "USW00014768"}  # Buffalo and Rochester airports


SNOW_PLACES = {"North Tonawanda": (43.0387, -78.8642), "Orchard Park": (42.7676, -78.7439),
               "Dunkirk": (42.4795, -79.3339), "Scottsville": (43.0259, -77.7453)}
SNOW_NORMAL_FALLBACK = {"North Tonawanda": "BUF", "Orchard Park": "BUF", "Dunkirk": "BUF", "Scottsville": "ROC"}


def snow():
    """Season-to-date snowfall (since Jul 1) for the four places Garret asked for (Nov 21), from the
    nearest station that reports snow daily, via ACIS (NOAA Regional Climate Centers). Writes
    data/snow.json. Normal-to-date comes from that station's 1991-2020 normals when it has them,
    otherwise from the nearest airport (named in normal_from). Never fatal."""
    import math
    def acis(path, params):
        req = urllib.request.Request("https://data.rcc-acis.org/" + path, data=json.dumps(params).encode(),
                                     headers={**UA, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.loads(r.read())
    def num(v):
        if v in ("T",): return 0.0
        try: return float(v)
        except (TypeError, ValueError): return None
    now = datetime.now(timezone.utc) - timedelta(hours=5)
    end = (now - timedelta(days=0)).strftime("%Y-%m-%d")
    yr = now.year if now.month >= 7 else now.year - 1
    start = f"{yr}-07-01"
    out = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "season_start": start,
           "source": "ACIS, NOAA Regional Climate Centers", "places": {}}
    def season_normal(sid):
        try:
            d = acis("StnData", {"sid": sid, "sdate": start, "edate": end, "elems": [{"name": "snow", "normal": "1"}]})
            vals = [num(r[1]) for r in d.get("data", [])]
            vals = [v for v in vals if v is not None]
            return round(sum(vals), 1) if len(vals) > 20 else None
        except Exception:
            return None
    for place, (lat, lon) in SNOW_PLACES.items():
        try:
            meta = acis("StnMeta", {"bbox": [lon - 0.25, lat - 0.2, lon + 0.25, lat + 0.2], "elems": "snow",
                                    "sdate": start, "edate": end, "meta": ["name", "ll", "sids", "uid"]})
            cands = []
            for m in meta.get("meta", []):
                if not m.get("ll"): continue
                dx = (m["ll"][0] - lon) * 69 * math.cos(math.radians(lat)); dy = (m["ll"][1] - lat) * 69
                cands.append((math.hypot(dx, dy), m))
            cands.sort(key=lambda c: c[0])
            got = None
            for dist, m in cands[:12]:
                d = acis("StnData", {"uid": m["uid"], "sdate": start, "edate": end, "elems": [{"name": "snow"}]})
                rows = d.get("data", [])
                vals = [(r[0], num(r[1])) for r in rows]
                have = [v for _, v in vals if v is not None]
                recent = [dt for dt, v in vals[-4:] if v is not None]
                if not recent or len(have) < 0.6 * len(vals): continue   # must report most days and in the last 4
                last_day = recent[-1]
                got = {"station": m["name"].title(), "dist_mi": round(dist, 1), "last_date": last_day,
                       "season_in": round(sum(have), 1),
                       "last_day_in": next(v for dt, v in vals if dt == last_day),
                       "days_reported": len(have), "days_in_season": len(vals)}
                sids = [x.split()[0] for x in m.get("sids", [])]
                for sid in sids:
                    nm = season_normal(sid)
                    if nm is not None:
                        got["normal_in"] = nm; got["normal_from"] = got["station"]; break
                break
            if got and "normal_in" not in got:
                fb = SNOW_NORMAL_FALLBACK[place]
                nm = season_normal(fb)
                if nm is not None:
                    got["normal_in"] = nm
                    got["normal_from"] = {"BUF": "Buffalo airport", "ROC": "Rochester airport"}[fb]
            out["places"][place] = got or {"error": "no nearby station reporting snow daily"}
            try:   # NWS forecast snowfall, next 48 hours (Garret, Nov 21)
                pt2 = json.loads(get(f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}"))["properties"]
                grid = json.loads(get(pt2["forecastGridData"]))["properties"]
                now_u = datetime.now(timezone.utc); tot = 0.0
                for v in grid.get("snowfallAmount", {}).get("values", []):
                    t0 = datetime.fromisoformat(v["validTime"].split("/")[0])
                    if now_u - timedelta(hours=3) <= t0 < now_u + timedelta(hours=48) and v.get("value"):
                        tot += v["value"]
                out["places"][place]["fcst_48h_in"] = round(tot / 25.4, 1)
            except Exception as e:
                out["places"][place]["fcst_error"] = str(e)[:120]
            print("snow", place, out["places"][place])
        except Exception as e:
            out["places"][place] = {"error": str(e)[:200]}
            print("snow failed", place, e)
    (ROOT / "data" / "snow.json").write_text(json.dumps(out, indent=1))


def climate_day():
    """Records for the date, this date last year, and Lake Erie ice cover (Garret, Nov 21: "Do them all").
    Writes data/climate.json. Records and last year from ACIS (NOAA Regional Climate Centers) for the
    Buffalo airport (long record, used for North Tonawanda) and the Rochester airport (Scottsville).
    Ice cover from NOAA GLERL. Never fatal."""
    def acis(params):
        req = urllib.request.Request("https://data.rcc-acis.org/StnData", data=json.dumps(params).encode(),
                                     headers={**UA, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    def num(v):
        if v == "T": return 0.0
        try: return float(v)
        except (TypeError, ValueError): return None
    now = datetime.now(timezone.utc) - timedelta(hours=5)
    md = now.strftime("%m-%d")
    out = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "date": now.strftime("%Y-%m-%d"),
           "source": "ACIS, NOAA Regional Climate Centers; ice cover NOAA GLERL", "stations": {}}
    for sid, label in (("BUF", "Buffalo airport"), ("ROC", "Rochester airport")):
        try:
            d = acis({"sid": sid, "sdate": f"1870-{md}", "edate": now.strftime("%Y-%m-%d"),
                      "elems": [{"name": n, "interval": [1, 0, 0]} for n in ("maxt", "mint", "pcpn", "snow")]})
            rows = [r for r in d.get("data", []) if r[0][5:] == md]
            hi = [(num(r[1]), r[0][:4]) for r in rows if num(r[1]) is not None and r[0][:4] != now.strftime("%Y")]
            lo = [(num(r[2]), r[0][:4]) for r in rows if num(r[2]) is not None and r[0][:4] != now.strftime("%Y")]
            st = {"name": label, "since": rows[0][0][:4] if rows else None}
            if hi:
                m = max(v for v, _ in hi); st["record_high"] = {"f": int(m), "years": [y for v, y in hi if v == m]}
            if lo:
                m = min(v for v, _ in lo); st["record_low"] = {"f": int(m), "years": [y for v, y in lo if v == m]}
            ly = str(now.year - 1)
            r = next((r for r in rows if r[0][:4] == ly), None)
            if r:
                st["last_year"] = {"date": r[0], "high": num(r[1]), "low": num(r[2]), "precip_in": num(r[3]),
                                   "snow_in": num(r[4]), "trace_precip": r[3] == "T", "trace_snow": r[4] == "T"}
            out["stations"][sid] = st
            print("climate", sid, st)
        except Exception as e:
            out["stations"][sid] = {"error": str(e)[:200]}; print("climate failed", sid, e)
    # Lake Erie ice cover: GLERL daily per-lake files (columns = ice years, named for the January year;
    # rows = days; NA = not recorded). Find the Erie file in the directory listing.
    base = "https://www.glerl.noaa.gov/data/ice/glicd/daily/"
    try:
        listing = get(base, timeout=30).decode(errors="replace")
        files = sorted(set(re.findall(r'href="([^"?/]+\.(?:txt|csv|dat))"', listing)))
        print("ice files", files[:40])
        erie = [f for f in files if re.search(r"eri", f, re.I)]
        ice = {"files": files[:40]}
        if erie:
            raw = get(base + erie[0], timeout=30).decode(errors="replace")
            rows = [re.split(r"[\s,]+", l.strip()) for l in raw.splitlines() if l.strip()]
            head = rows[0]; iy = str(now.year + 1 if now.month >= 7 else now.year)
            ice.update({"file": erie[0], "header": head[:6] + ["..."] + head[-3:], "ice_year": iy, "sample_row": rows[-1][:4] if len(rows) > 1 else None})
            if iy in head:
                c = head.index(iy)
                if len(rows) > 1 and len(rows[1]) == len(head) + 1: c += 1   # data rows lead with the day; the header doesn't
                vals = [(r[0], r[c]) for r in rows[1:] if len(r) > c and r[c] not in ("NA", "")]
                if vals: ice["last"] = {"row": vals[-1][0], "pct": float(vals[-1][1])}
            print("ice", ice.get("file"), ice.get("header"), ice.get("last"))
        out["erie_ice"] = ice
    except Exception as e:
        out["erie_ice"] = {"error": str(e)[:200]}; print("ice failed", e)
    (ROOT / "data" / "climate.json").write_text(json.dumps(out, indent=1))


def alerts():
    """Active NWS watches, warnings and advisories for the four places (Garret, Nov 21: winter storms).
    Writes data/alerts.json. Never fatal."""
    places = {"North Tonawanda": (43.0387, -78.8642), "Orchard Park": (42.7676, -78.7439),
              "Dunkirk": (42.4795, -79.3339), "Scottsville": (43.0259, -77.7453)}
    out = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "source": "National Weather Service", "alerts": {}}
    for place, (lat, lon) in places.items():
        try:
            d = json.loads(get(f"https://api.weather.gov/alerts/active?point={lat},{lon}", timeout=30))
            for f in d.get("features", []):
                p = f.get("properties", {})
                a = out["alerts"].setdefault(p.get("id") or f.get("id"), {
                    "event": p.get("event"), "headline": p.get("headline"), "severity": p.get("severity"),
                    "onset": p.get("onset"), "ends": p.get("ends") or p.get("expires"), "sender": p.get("senderName"),
                    "description": (p.get("description") or "")[:1200], "instruction": (p.get("instruction") or "")[:400], "places": []})
                if place not in a["places"]: a["places"].append(place)
        except Exception as e:
            out.setdefault("errors", []).append(f"{place}: {str(e)[:150]}")
    print("alerts", [(a["event"], a["places"]) for a in out["alerts"].values()])
    (ROOT / "data" / "alerts.json").write_text(json.dumps(out, indent=1))


def normals():
    """30-year (1991-2020) daily normal highs and lows from NOAA NCEI, fetched once into data/normals.json."""
    path = ROOT / "data" / "normals.json"
    if path.exists():
        return
    import csv, io
    res = {"source": "NOAA NCEI U.S. Climate Normals 1991-2020, daily", "stations": {}}
    for town, sid in NORMAL_STATIONS.items():
        try:
            rows = list(csv.DictReader(io.StringIO(get(f"https://www.ncei.noaa.gov/data/normals-daily/1991-2020/access/{sid}.csv").decode())))
            res["stations"][town] = {"station": sid, "days": {r["DATE"]: {"tmax": float(r["DLY-TMAX-NORMAL"]), "tmin": float(r["DLY-TMIN-NORMAL"])} for r in rows}}
        except Exception as e:
            res.setdefault("errors", []).append(f"{town}: {e}")
    if res["stations"]:
        path.write_text(json.dumps(res, indent=1))


def travel_forecasts(out):
    """Weather for family members away from home (Garret, Oct 21). data/travel.json:
    [{"who": "Garret", "place": "Long Island (Rocky Point)", "lat": 40.95, "lon": -72.93,
      "start": "2026-10-20", "end": "2026-10-23"}]  (end may be null until known)
    Active trips (start <= tomorrow, end >= today or null) go into out["travel"]."""
    path = ROOT / "data" / "travel.json"
    if not path.exists():
        return
    today = datetime.now(timezone(timedelta(hours=-4))).date()
    out["travel"] = {}
    for t in json.loads(path.read_text()):
        try:
            start = datetime.fromisoformat(t["start"]).date()
            end = datetime.fromisoformat(t["end"]).date() if t.get("end") else None
            if start > today + timedelta(days=1) or (end and end < today):
                continue
            pt = json.loads(get(f"https://api.weather.gov/points/{t['lat']},{t['lon']}"))["properties"]
            fc = json.loads(get(pt["forecast"]))["properties"]
            out["travel"][t["place"]] = {"who": t["who"], "start": t["start"], "end": t.get("end"),
                "periods": [{"name": p["name"], "temp": p["temperature"], "pop": (p.get("probabilityOfPrecipitation") or {}).get("value"),
                             "short": p["shortForecast"], "detail": p["detailedForecast"]} for p in fc["periods"][:10]]}
        except Exception as e:
            out["errors"].append(f"travel {t.get('place')}: {e}")


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def parse_feed(raw):
    root = ET.fromstring(raw)
    items = []
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        f = {c.tag.split("}")[-1]: c for c in it}
        title = clean(f["title"].text if "title" in f else "")
        link = ""
        if "link" in f:
            link = (f["link"].text or f["link"].get("href") or "").strip()
        when = None
        for k in ("pubDate", "published", "updated", "date"):
            if k in f and f[k].text:
                try:
                    when = parsedate_to_datetime(f[k].text.strip())
                except Exception:
                    try:
                        when = datetime.fromisoformat(f[k].text.strip().replace("Z", "+00:00"))
                    except Exception:
                        pass
                break
        d = f.get("description") if f.get("description") is not None else f.get("summary")
        desc = clean(d.text if d is not None else "")
        if title:
            items.append({"title": title, "link": link, "published": when.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%MZ") if when else None, "summary": desc[:300]})
    return items


PAGE_UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml"}
SKIP = re.compile(r"(subscribe|sign up|newsletter|all rights reserved|copyright|cookie|advertis|click here|download the app|follow us|share this|read more:|related:|^photo|getty images|\(ap photo|story idea|^hello! i'm)", re.I)


def article_text(url, max_paras=8, max_chars=2400):
    """First real paragraphs of an article page, or None. Best-effort, never raises."""
    if not url or not url.startswith("http"):
        return None
    try:
        req = urllib.request.Request(url, headers=PAGE_UA)
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read(1_500_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
    except Exception:
        return None
    for blob in re.findall(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', raw):
        m = re.search(r'"articleBody"\s*:\s*"((?:[^"\\]|\\.)*)"', blob)
        if m:
            try:
                body = clean(json.loads('"' + m.group(1) + '"'))
            except Exception:
                body = ""
            if len(body) > 200:
                return body[:max_chars]
    raw = re.sub(r"(?is)<(script|style|noscript|aside|nav|footer|header|figure|form)[^>]*>.*?</\1>", " ", raw)
    m = re.search(r"(?is)<article[^>]*>(.*?)</article>", raw)
    scope = m.group(1) if m and len(m.group(1)) > 800 else raw
    paras, total = [], 0
    for p in re.findall(r"(?is)<p[^>]*>(.*?)</p>", scope):
        t = re.sub(r"^(?:(?:Facebook|Twitter|LinkedIn|Email|Print|X)\s+){2,}", "", clean(p))
        if len(t) < 60 or SKIP.search(t) or t in paras:
            continue
        paras.append(t); total += len(t)
        if len(paras) >= max_paras or total >= max_chars:
            break
    return "\n\n".join(paras) if paras else None


def add_bodies(rows, limit=45):
    todo = [r for r in rows[:limit] if r.get("link")]
    with ThreadPoolExecutor(max_workers=8) as ex:
        for r, body in zip(todo, ex.map(lambda r: article_text(r["link"]), todo)):
            if body:
                r["body"] = body


def news(hours=48):
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    out = {"generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "window_hours": hours, "sections": {}, "errors": []}
    for section, feeds in FEEDS.items():
        rows = []
        for name, url in feeds.items():
            try:
                for it in parse_feed(get(url)):
                    if it["published"]:
                        t = datetime.strptime(it["published"], "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
                        if t < cutoff:
                            continue
                    it["source"] = name
                    rows.append(it)
            except Exception as e:
                out["errors"].append(f"{name}: {e}")
        rows.sort(key=lambda r: r["published"] or "", reverse=True)
        rows = rows[:120]
        add_bodies(rows, limit=60)
        out["sections"][section] = rows
    return out


def market():
    """S&P 500 daily closes for the last year, for The Market (daily from Nov 22, Garret).
    Same-day sources first (Yahoo Finance chart data, then Stooq), FRED as the fallback
    (FRED runs a day or two behind). Each close is kept with its date. Never fatal."""
    rows, source = [], None
    try:
        d = json.loads(get("https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?range=1y&interval=1d", timeout=30))
        r = d["chart"]["result"][0]
        for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
            if c is not None:
                rows.append([(datetime.fromtimestamp(t, timezone.utc) - timedelta(hours=5)).strftime("%Y-%m-%d"), round(c, 2)])
        source = "Yahoo Finance"
    except Exception as e:
        print("market yahoo failed:", e); rows = []
    if len(rows) < 50:
        try:
            raw = get("https://stooq.com/q/d/l/?s=%5Espx&i=d", timeout=30).decode()
            start = (datetime.now(timezone.utc) - timedelta(days=370)).strftime("%Y-%m-%d")
            rows = []
            for line in raw.splitlines()[1:]:
                f = line.split(",")
                if len(f) >= 5 and f[0] >= start:
                    try: rows.append([f[0], round(float(f[4]), 2)])
                    except ValueError: pass
            source = "Stooq"
        except Exception as e:
            print("market stooq failed:", e); rows = []
    if len(rows) < 50:
        try:
            start = (datetime.now(timezone.utc) - timedelta(days=370)).strftime("%Y-%m-%d")
            raw = get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500&cosd=" + start, timeout=40).decode()
            rows = []
            for line in raw.splitlines()[1:]:
                dd, _, v = line.partition(",")
                try: rows.append([dd.strip(), round(float(v), 2)])
                except ValueError: pass
            source = "FRED, Federal Reserve Bank of St. Louis"
        except Exception as e:
            print("market fred failed:", e); rows = []
    # one row per day, in order
    seen = {}
    for dd, v in rows: seen[dd] = v
    rows = sorted(seen.items())
    if len(rows) > 50:
        (ROOT / "data" / "market.json").write_text(json.dumps({
            "series": "S&P 500 daily close", "source": source,
            "fetched_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "last": list(rows[-1]),
            "closes": [list(r) for r in rows]}))
        print("market ok", source, rows[-1])


if __name__ == "__main__":
    import sys
    if "--market" in sys.argv:   # market data alone (market.yml)
        market(); sys.exit(0)
    (ROOT / "data").mkdir(exist_ok=True)
    fc = forecasts()
    travel_forecasts(fc)
    lakes(fc)
    normals()
    alerts()
    snow()
    climate_day()
    market()
    (ROOT / "data" / "forecast.json").write_text(json.dumps(fc, indent=1))
    (ROOT / "data" / "news.json").write_text(json.dumps(news(), indent=1))
    print("ok")
