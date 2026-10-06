#!/usr/bin/env python3
"""Build, commit and push the pool, retrying through races. Prints LANDED <sha> or FAILED <why> as its last line.
usage: python3 pool/tools/land.py "Pool: Week N refresh"     (run from the repo root or anywhere)"""
import subprocess, sys, os, time
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
msg = sys.argv[1] if len(sys.argv) > 1 else "Pool: refresh"
def sh(*a, check=True):
    r = subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(f"{' '.join(a)}: {r.stderr.strip() or r.stdout.strip()}")
    return r
sh("git", "config", "user.email", "noreply@anthropic.com"); sh("git", "config", "user.name", "Claude")
for attempt in range(1, 4):
    try:
        sh("python3", "pool/build.py")
        sh("git", "add", "pool")
        if sh("git", "diff", "--cached", "--quiet", check=False).returncode:
            sh("git", "commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude <noreply@anthropic.com>")
        # every build stamps page.json/index.html and score.py stamps season.json, so two runs always touch the
        # same lines; on a clash keep this run's side (-X theirs = the commit being replayed), then rebuild from the
        # merged data so the generated files match it
        sh("git", "pull", "-q", "--rebase", "-X", "theirs", "origin", "main")
        sh("python3", "pool/build.py")
        sh("git", "add", "pool")
        if sh("git", "diff", "--cached", "--quiet", check=False).returncode:
            ahead = sh("git", "rev-list", "--count", "origin/main..HEAD").stdout.strip() != "0"
            if ahead: sh("git", "commit", "-q", "--amend", "--no-edit")      # fold into this run's own commit
            else: sh("git", "commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude <noreply@anthropic.com>")
        sh("git", "push", "-q", "origin", "HEAD:main")
        sha = sh("git", "rev-parse", "--short", "HEAD").stdout.strip()
        remote = sh("git", "ls-remote", "origin", "refs/heads/main").stdout.split()[0][:len(sha)]
        if remote == sha: print(f"LANDED {sha}"); sys.exit(0)
        raise RuntimeError(f"origin/main is {remote}, local is {sha}")
    except Exception as e:
        print(f"attempt {attempt}: {e}", file=sys.stderr)
        subprocess.run(["git", "rebase", "--abort"], cwd=ROOT, capture_output=True)
        time.sleep(5 * attempt)
print("FAILED push did not land after 3 tries (see errors above)"); sys.exit(1)
