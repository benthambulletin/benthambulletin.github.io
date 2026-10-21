#!/usr/bin/env python3
"""Fetch family-form photos privately (run from the build session).

Usage: python3 tools/get_photos.py '<json items>' [out_dir]
items = [{"id": "<submission id>", "url": "<Tally file url>"}]
Dispatches photos.yml (which commits the photos ENCRYPTED to data/inbox/), pulls,
decrypts each into out_dir (default /home/claude/inbox, outside the repo) with the
private key at /home/claude/.bulletin_photo_key.pem, then git-rms the encrypted files.
Commit that removal with the day's build.

If the private key is missing (workspace reset): make a new pair with
  openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out /home/claude/.bulletin_photo_key.pem
  openssl pkey -in /home/claude/.bulletin_photo_key.pem -pubout -out tools/photo_pubkey.pem
commit the new public key, and re-run (photos are still in Tally).
"""
import json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIV = "/home/claude/.bulletin_photo_key.pem"
REPO = "repos/benthambulletin/benthambulletin.github.io"
items = json.loads(sys.argv[1]); out = sys.argv[2] if len(sys.argv) > 2 else "/home/claude/inbox"
ids = [i["id"] for i in items]
run = lambda *a: subprocess.run(a, cwd=ROOT, check=True, capture_output=True)
subprocess.run(["gh", "api", "-X", "POST", f"{REPO}/actions/workflows/photos.yml/dispatches", "-f", "ref=main",
                "-f", "inputs[items]=" + json.dumps(items)], check=True, capture_output=True)
inbox = ROOT / "data" / "inbox"
for _ in range(60):
    time.sleep(5)
    subprocess.run(["git", "pull", "--rebase", "-q"], cwd=ROOT, capture_output=True)
    if all((inbox / f"{i}.enc").exists() for i in ids):
        break
else:
    raise SystemExit("photos did not arrive in 5 minutes; check the photos.yml run")
os.makedirs(out, exist_ok=True)
for i in ids:
    key = subprocess.run(["openssl", "pkeyutl", "-decrypt", "-inkey", PRIV, "-pkeyopt", "rsa_padding_mode:oaep",
                          "-in", str(inbox / f"{i}.key")], check=True, capture_output=True).stdout
    kf = Path(out) / f".{i}.k"; kf.write_bytes(key)
    subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-in", str(inbox / f"{i}.enc"),
                    "-out", str(Path(out) / f"{i}.jpg"), "-pass", f"file:{kf}"], check=True)
    kf.unlink()
    run("git", "rm", "-q", f"data/inbox/{i}.enc", f"data/inbox/{i}.key")
print("saved:", [f"{out}/{i}.jpg" for i in ids], "(encrypted copies git-rm'd; commit with the build)")
