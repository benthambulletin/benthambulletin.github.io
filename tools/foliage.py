"""Render the I LOVE NY foliage report in a real browser and save what it shows.
Writes data/foliage.json: {fetched_utc, url, text, json_responses:[{url, body}]}.
The page loads its numbers by script, so a plain fetch sees nothing."""
import json, datetime
from playwright.sync_api import sync_playwright
URL = "https://www.iloveny.com/things-to-do/fall/foliage-report/"
out = {"fetched_utc": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), "url": URL, "json_responses": []}
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    def on_resp(r):
        try:
            ct = r.headers.get("content-type", "")
            if "json" in ct and ("foliage" in r.url.lower() or "report" in r.url.lower() or "rest" in r.url.lower()):
                out["json_responses"].append({"url": r.url, "body": r.text()[:200000]})
        except Exception:
            pass
    pg.on("response", on_resp)
    pg.goto(URL, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(5000)
    out["text"] = pg.inner_text("body")[:200000]
    b.close()
json.dump(out, open("data/foliage.json", "w"), indent=1)
print(len(out["text"]), len(out["json_responses"]))
