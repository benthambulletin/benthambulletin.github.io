"""Download photos sent through the family form (Tally rjxDpl) for the build.
The build session can't reach Tally's file storage, so it dispatches photos.yml with
items=[{"id": "...", "url": "..."}]. This saves each to photo-out/<id>.<ext>, which the
workflow uploads as a 1-day artifact. Nothing is committed to the public repo."""
import json, os, urllib.request
items = json.loads(os.environ["ITEMS"])
os.makedirs("photo-out", exist_ok=True)
ok = 0
for item in items:
    try:
        req = urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        ext = os.path.splitext(item["url"].split("?")[0])[1].lower() or ".jpg"
        open(f"photo-out/{item['id']}{ext}", "wb").write(data)
        print("ok", item["id"], len(data)); ok += 1
    except Exception as e:
        print("fail", item["id"], type(e).__name__)
if not ok:
    raise SystemExit("no photos downloaded")
