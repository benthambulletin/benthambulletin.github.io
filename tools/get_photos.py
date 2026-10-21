#!/usr/bin/env python3
"""Fetch family-form photos privately (run from the build session).

Usage: python3 tools/get_photos.py '<json items>' <out_dir>
items = [{"id": "<submission id>", "url": "<Tally file url>"}]
Dispatches photos.yml, waits for it, downloads the artifact into out_dir (outside the
repo, e.g. /home/claude/inbox), then deletes the artifact so it doesn't linger.
"""
import json, subprocess, sys, time, zipfile, io, os
from datetime import datetime, timezone

REPO = "repos/benthambulletin/benthambulletin.github.io"


def gh(*args, raw=False):
    r = subprocess.run(["gh", "api", *args], capture_output=True)
    if r.returncode:
        raise SystemExit(f"gh api {' '.join(args)} failed: {r.stderr.decode()[:300]}")
    return r.stdout if raw else (json.loads(r.stdout) if r.stdout.strip() else None)


items, out = sys.argv[1], sys.argv[2]
json.loads(items)  # validate
start = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
gh("-X", "POST", f"{REPO}/actions/workflows/photos.yml/dispatches", "-f", "ref=main", "-f", f"inputs[items]={items}")
run = None
for _ in range(60):
    time.sleep(5)
    runs = gh(f"{REPO}/actions/workflows/photos.yml/runs?per_page=5")["workflow_runs"]
    runs = [r for r in runs if r["created_at"] >= start[:17]]
    if runs and runs[0]["status"] == "completed":
        run = runs[0]; break
if not run:
    raise SystemExit("photos run did not finish in 5 minutes")
if run["conclusion"] != "success":
    raise SystemExit(f"photos run {run['id']} ended {run['conclusion']}")
arts = gh(f"{REPO}/actions/runs/{run['id']}/artifacts")["artifacts"]
os.makedirs(out, exist_ok=True)
for a in arts:
    z = zipfile.ZipFile(io.BytesIO(gh(f"{REPO}/actions/artifacts/{a['id']}/zip", raw=True)))
    z.extractall(out)
    gh("-X", "DELETE", f"{REPO}/actions/artifacts/{a['id']}")
print("saved:", sorted(os.listdir(out)))
