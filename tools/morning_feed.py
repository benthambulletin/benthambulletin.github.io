#!/usr/bin/env python3
"""Morning feed for the Bulletin: official forecasts and a headline scan.

Run by .github/workflows/morning.yml at about 6:30 a.m. Eastern, before the
6:59 build. Writes:
  data/forecast.json  NWS point forecast + latest observation for the three towns
  data/news.json      recent headlines from national, local and entertainment RSS feeds
Every source is fetched independently; one failure never stops the rest, and
failures are recorded in the output so the editor knows what is missing.
"""
import json, re, html
import urllib.request
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

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
    },
    "entertainment": {
        "Variety": "https://variety.com/feed/",
        "Deadline": "https://deadline.com/feed/",
        "Billboard": "https://www.billboard.com/feed/",
        "Hollywood Reporter": "https://www.hollywoodreporter.com/feed/",
    },
}


def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


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
                st = json.loads(get(pt["observationStations"]))["features"][0]["properties"]["stationIdentifier"]
                ob = json.loads(get(f"https://api.weather.gov/stations/{st}/observations/latest"))["properties"]
                c = (ob.get("temperature") or {}).get("value")
                t["observation"] = {"station": st, "time": ob.get("timestamp"), "text": ob.get("textDescription"),
                                    "temp_f": None if c is None else round(c * 9 / 5 + 32)}
            except Exception as e:
                out["errors"].append(f"{town} observation: {e}")
            out["towns"][town] = t
        except Exception as e:
            out["errors"].append(f"{town} forecast: {e}")
    return out


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
        out["sections"][section] = rows[:80]
    return out


if __name__ == "__main__":
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "forecast.json").write_text(json.dumps(forecasts(), indent=1))
    (ROOT / "data" / "news.json").write_text(json.dumps(news(), indent=1))
    print("ok")
