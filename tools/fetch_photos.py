"""Download photos sent through the family form (Tally rjxDpl).
The build session can't reach Tally's file storage, so it lists the file URLs in
data/inbox/photo-queue.json as [{"id": "...", "url": "..."}]; this downloads each
to data/inbox/<id>.<ext> and empties the queue."""
import json, os, urllib.request
q = json.load(open("data/inbox/photo-queue.json"))
left = []
for item in q:
    try:
        req = urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        ext = os.path.splitext(item["url"].split("?")[0])[1].lower() or ".jpg"
        open(f"data/inbox/{item['id']}{ext}", "wb").write(data)
        print("ok", item["id"], len(data))
    except Exception as e:
        print("fail", item["id"], e); left.append(item)
json.dump(left, open("data/inbox/photo-queue.json", "w"), indent=1)
