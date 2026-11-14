#!/usr/bin/env python3
"""Fetch one shopper screenshot privately (run by the Porta Potty checking session).

Usage: python3 deals/tools/get_shot.py <submission id> <screenshot https url> [out_dir]
Makes a one-time key pair, dispatches deals-shot.yml (which commits the screenshot
ENCRYPTED to deals/inbox/), pulls, decrypts it to out_dir/<id>.jpg (default
/home/claude/shots, outside the repo), then removes the encrypted copy and pushes.
The screenshot itself is never committed or published.
"""
import base64, os, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = "repos/benthambulletin/benthambulletin.github.io"
sid, url = sys.argv[1], sys.argv[2]
out = Path(sys.argv[3] if len(sys.argv) > 3 else "/home/claude/shots"); out.mkdir(parents=True, exist_ok=True)
tmp = Path(tempfile.mkdtemp()); priv = tmp / "k.pem"; pub = tmp / "k.pub"
sh = lambda *a, **k: subprocess.run(a, check=True, capture_output=True, **k)
sh("openssl", "genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048", "-out", str(priv))
sh("openssl", "pkey", "-in", str(priv), "-pubout", "-out", str(pub))
sh("gh", "api", "-X", "POST", f"{REPO}/actions/workflows/deals-shot.yml/dispatches", "-f", "ref=main",
   "-f", f"inputs[id]={sid}", "-f", f"inputs[url]={url}", "-f", "inputs[pub]=" + base64.b64encode(pub.read_bytes()).decode())
enc, key = ROOT / "deals" / "inbox" / f"{sid}.enc", ROOT / "deals" / "inbox" / f"{sid}.key"
for _ in range(48):
    time.sleep(5)
    subprocess.run(["git", "pull", "--rebase", "-q", "origin", "main"], cwd=ROOT, capture_output=True)
    if enc.exists() and key.exists():
        break
else:
    raise SystemExit("screenshot did not arrive in 4 minutes; check the deals-shot.yml run")
k = sh("openssl", "pkeyutl", "-decrypt", "-inkey", str(priv), "-pkeyopt", "rsa_padding_mode:oaep", "-in", str(key)).stdout
kf = tmp / "aes"; kf.write_bytes(k)
sh("openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-in", str(enc), "-out", str(out / f"{sid}.jpg"), "-pass", f"file:{kf}")
for f in (kf, priv, pub): f.unlink()
sh("git", "rm", "-q", f"deals/inbox/{sid}.enc", f"deals/inbox/{sid}.key", cwd=ROOT)
sh("git", "commit", "-q", "-m", f"Porta Potty: screenshot for {sid} read and removed", cwd=ROOT)
for _ in range(3):
    subprocess.run(["git", "pull", "--rebase", "-q", "origin", "main"], cwd=ROOT, capture_output=True)
    if subprocess.run(["git", "push", "-q", "origin", "main"], cwd=ROOT, capture_output=True).returncode == 0:
        break
    time.sleep(10)
print("saved:", out / f"{sid}.jpg")
