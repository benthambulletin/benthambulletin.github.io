"""Download photos sent through the family form (Tally rjxDpl) and encrypt them.
Run by photos.yml with ITEMS=[{"id": "...", "url": "..."}]. For each photo: a random
32-byte key encrypts the file (openssl aes-256-cbc, pbkdf2) -> data/inbox/<id>.enc, and
the key is sealed with tools/photo_pubkey.pem (RSA-OAEP) -> data/inbox/<id>.key.
The plain photo never touches the repo. URLs are not printed to the public log."""
import json, os, re, subprocess, tempfile, urllib.request
items = json.loads(os.environ["ITEMS"])
ok = 0
for item in items:
    sid = re.sub(r"[^A-Za-z0-9_-]", "", item["id"])
    try:
        req = urllib.request.Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        with tempfile.TemporaryDirectory() as td:
            src, key = os.path.join(td, "p"), os.path.join(td, "k")
            open(src, "wb").write(data)
            open(key, "wb").write(os.urandom(32).hex().encode())
            subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-salt", "-in", src,
                            "-out", f"data/inbox/{sid}.enc", "-pass", f"file:{key}"], check=True)
            subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", "tools/photo_pubkey.pem",
                            "-pkeyopt", "rsa_padding_mode:oaep", "-in", key, "-out", f"data/inbox/{sid}.key"], check=True)
        print("ok", sid, len(data)); ok += 1
    except Exception as e:
        print("fail", sid, type(e).__name__)
if not ok:
    raise SystemExit("no photos downloaded")
