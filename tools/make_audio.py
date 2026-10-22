#!/usr/bin/env python3
"""Record the day's paper as audio (Garret, Oct 22: the parents won't download better phone voices).
Usage: python3 tools/make_audio.py YYYY-MM-DD MODEL.onnx OUT.mp3
Reads data/edition-DATE.json, turns the paper into plain spoken lines (same idea as the
read-aloud button), synthesizes with Piper (offline neural TTS), encodes a small mono MP3.
Run by .github/workflows/audio.yml; the MP3 goes to the repo's "audio" release, not into git."""
import json, re, sys, wave, subprocess, tempfile, os, html
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
date, model, out = sys.argv[1], sys.argv[2], sys.argv[3]
ed = json.load(open(ROOT / "data" / f"edition-{date}.json"))
soup = BeautifulSoup(ed["body_html"], "html.parser")
for sel in [".tools", ".nav", ".kicker", "svg", "script", "img", ".sig", ".orn", ".frame", "style"]:
    for t in soup.select(sel): t.decompose()
BLOCK = {"h1","h2","h3","p","div","li","tr","table","ul","br"}
lines, buf = [], []
def flush():
    t = " ".join(buf).strip(); buf.clear()
    if t: lines.append(t)
def walk(n):
    for c in n.children:
        if getattr(c, "name", None) is None:
            buf.append(str(c))
        elif c.name in BLOCK:
            flush(); walk(c); flush()
        else:
            walk(c)
walk(soup); flush()

def speakable(l):
    l = html.unescape(l)
    l = re.sub(r"(\d)″", r"\1 inches", l).replace("°", " degrees")
    l = re.sub(r"[·—|]", ", ", l).replace("–", " to ")
    l = re.sub(r"(\d)a\b", r"\1 a.m.", l); l = re.sub(r"(\d)p\b", r"\1 p.m.", l)
    l = l.replace("½", " and a half")
    l = re.sub(r"https?://", "", l)
    l = re.sub(r"[^\x20-\x7EÀ-ɏ‘-”]", " ", l)
    l = re.sub(r"\s+", " ", l).strip()
    if l == l.upper() and re.search(r"[A-Z]{3}", l): l = l[0] + l[1:].lower()
    return l
lines = [speakable(l) for l in lines]
lines = [l for l in lines if re.search(r"[A-Za-z0-9]", l)]
text = "\n".join(l if re.search(r"[.!?:;]$", l) else l + "." for l in lines)
print(f"{len(lines)} lines, {len(text)} chars")

from piper import PiperVoice
voice = PiperVoice.load(model)
with tempfile.TemporaryDirectory() as td:
    wav = os.path.join(td, "p.wav")
    with wave.open(wav, "wb") as w:
        if hasattr(voice, "synthesize_wav"):
            voice.synthesize_wav(text, w)
        else:
            voice.synthesize(text, w)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-ac", "1", "-ar", "22050",
                    "-codec:a", "libmp3lame", "-b:a", "48k", out], check=True)
print("wrote", out, os.path.getsize(out))
