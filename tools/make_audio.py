#!/usr/bin/env python3
"""Record the day's paper as audio (Garret, Oct 22: the parents won't download better phone voices).
Usage: python3 tools/make_audio.py YYYY-MM-DD VOICE OUT.mp3 [max_chars]
VOICE is a Kokoro voice name (e.g. af_heart) or a Piper .onnx model path. max_chars trims for samples.
Reads data/edition-DATE.json, turns the paper into plain spoken lines (same idea as the
read-aloud button), synthesizes with Kokoro (open-source neural TTS, Apache-2.0) or Piper, encodes a small MP3 (lameenc).
Since Nov 7 it is a three-anchor morning newscast (names Garret's): Linda of Scottsville (VOICE, af_heart) on news,
John of North Tonawanda (VOICE2, am_michael) on weather and sky, Reggie of Dunkirk (VOICE3, am_fenrir, a touch faster) on sports.
Nov 7 "level up": Kokoro's top-graded American voices, 64 kbps, loudness evened per anchor, beats after headlines and hand-offs; with short original chimes between segments; SCRIPT_ONLY=1 prints the script without recording.
Run by .github/workflows/audio.yml; the MP3 is committed to audio/<date>.mp3 (32 kbps mono, ~3 MB; last 7 days kept)."""
import json, re, sys, wave, subprocess, tempfile, os, html
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
date, model, out = sys.argv[1], sys.argv[2], sys.argv[3]
maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 0
ed = json.load(open(ROOT / "data" / f"edition-{date}.json"))
soup = BeautifulSoup(ed["body_html"], "html.parser")
for sel in [".tools", ".nav", "nav", ".kicker", "svg", "script", "img", ".sig", ".orn", ".frame", "style", ".tiles", ".inside", ".plate-cap", ".the", ".mast", ".tag", ".dateline", ".place", ".bigtemp"]:
    for t in soup.select(sel): t.decompose()
for t in soup.select(".lbl"):
    t.string = t.get_text(" ", strip=True).capitalize() + ":"
for t in soup.select(".lede"):
    t.string = t.get_text(" ", strip=True).rstrip(".") + ". "
BLOCK = {"h1","h2","h3","p","div","li","tr","table","ul","br"}
def lines_of(node):
    out, buf = [], []
    def flush():
        t = " ".join(buf).strip(); buf.clear()
        if t: out.append(t)
    def walk(n):
        for c in n.children:
            if getattr(c, "name", None) is None: buf.append(str(c))
            elif c.name in BLOCK: flush(); walk(c); flush()
            else: walk(c)
    walk(node); flush()
    return out

# ---- The newscast (Garret, Nov 7: "a newscast vibe"). Three anchors, named by Garret: Linda from Scottsville
# (VOICE, news), John from North Tonawanda (VOICE2, weather and sky), Reggie from Dunkirk (VOICE3, sports);
# a short original chime between segments.
A, B, C = "A", "B", "C"
import datetime as _dt
d = _dt.date.fromisoformat(date)
nth = lambda n: f"{n}{'th' if 11 <= n % 100 <= 13 else {1:'st',2:'nd',3:'rd'}.get(n % 10, 'th')}"
day = f"{d:%A}, {d:%B} {nth(d.day)}"
segs = []   # (speaker, text) or ("CHIME", kind)
def say(who, *ls):
    for l in ls:
        if l and l.strip(): segs.append((who, l))
def text(el): return " ".join(lines_of(el))

colo = soup.select_one(".colo")
answer = ""
if colo:
    for dv in colo.find_all("div"):
        t = dv.get_text(" ", strip=True)
        if t.startswith("Question of the Day:"): answer = t.split(":", 1)[1].strip()
    colo.decompose()

lead = soup.select_one(".wire.lead")
heads = []
if lead:
    k = lead.select_one(".kick"); k and k.decompose()
    for pq in lead.select(".pull"): pq.decompose()
    heads.append(lead.find("h3").get_text(" ", strip=True))
NAME = {A: "Linda", B: "John", C: "Reggie"}
TOWN = {A: "in Scottsville", B: "in North Tonawanda", C: "in Dunkirk"}
SPEAKER = {"weather": B, "sky": B, "gridiron": C, "chase": C, "monday morning": C, "sunday tax": C}
INTRO = {"weather glass": "The Weather Glass.", "almanac sky": "Now, the sky above us.",
         "ledger": "The number of the day.", "national wire": "Across the country.",
         "home wire": "Closer to home.", "marquee": "In entertainment.", "gridiron": "The Gridiron.",
         "monday morning": "Monday Morning Quarterback.", "chase": "On the track, the Chase.",
         "on this day": "On this day in history.", "question of the day": "And finally, the riddle of the day.",
         "sunday spotlight": "This week's Sunday Spotlight.", "week ahead": "A look at the week ahead.",
         "sunday question": "The Sunday Question.", "family today": "Family news.", "group chat": "From the group chat."}
SKIP_SECTIONS = ("the chase",) if False else ()

# walk the body into sections
sections, cur = [], ["", []]
for el in list(soup.children):
    if getattr(el, "name", None) is None: continue
    if el.name == "h2" and "sec" in (el.get("class") or []):
        sections.append(cur); cur = [el.get_text(" ", strip=True), []]
    else:
        cur[1].append(el)
sections.append(cur)
for want in ("national", "marquee", "home wire"):
    for name, els in sections:
        if want in name.lower():
            h = next((el.find("h3") for el in els if el.find("h3") and el is not lead and "lead" not in (el.get("class") or [])), None)
            t = h.get_text(" ", strip=True) if h else ""
            if t and t not in heads and len(heads) < 3: heads.append(re.sub(r"^[^·]+·\s*", "", t))
            break

DAYS = {"Sun":"Sunday","Mon":"Monday","Tue":"Tuesday","Wed":"Wednesday","Thu":"Thursday","Fri":"Friday","Sat":"Saturday"}
TEAMS = {"KC":"Kansas City","MIN":"Minnesota","MIA":"Miami","NE":"New England","BAL":"Baltimore","PIT":"Pittsburgh","CIN":"Cincinnati","CLE":"Cleveland","HOU":"Houston","IND":"Indianapolis","JAX":"Jacksonville","TEN":"Tennessee","DEN":"Denver","LV":"Las Vegas","LAC":"the Chargers","LAR":"the Rams","NYG":"the Giants","NYJ":"the Jets","BUF":"Buffalo","DAL":"Dallas","PHI":"Philadelphia","WAS":"Washington","CHI":"Chicago","DET":"Detroit","GB":"Green Bay","ATL":"Atlanta","CAR":"Carolina","NO":"New Orleans","TB":"Tampa Bay","ARI":"Arizona","SF":"San Francisco","SEA":"Seattle"}
cal = ""
cover = ""
front = []
for name, els in sections[:1]:
    for el in els:
        c = el.get("class") or []
        if "calline" in c:
            for l in lines_of(el):
                if l.startswith("Coming up"):
                    l = re.sub(r"\b(KC|MIN|MIA|NE|BAL|PIT|CIN|CLE|HOU|IND|JAX|TEN|DEN|LV|LAC|LAR|NYG|NYJ|BUF|DAL|PHI|WAS|CHI|DET|GB|ATL|CAR|NO|TB|ARI|SF|SEA)\b", lambda m: TEAMS[m.group(1)], l)
                    l = re.sub(r"\b(Sun|Mon|Tue|Wed|Thu|Fri|Sat)\b", lambda m: DAYS[m.group(1)], l)
                    parts = [x.strip() for x in l[len("Coming up"):].split("·")]
                    # pairs: day, what
                    items = [f"{parts[i]}, {parts[i+1]}" for i in range(0, len(parts) - 1, 2)]
                    cal = "On the calendar: " + "; ".join(items) + "."
        elif "plate-wrap" in c:
            cover = text(el)
        elif el.get_text(strip=True):
            front.append(el)

segs.append(("CHIME", "open"))
say(A, f"Good morning. It's {day}, and this is The Bentham Bulletin. I'm Linda, {TOWN[A]}.")
say(B, f"I'm John, {TOWN[B]}, with your weather.")
say(C, f"And I'm Reggie, {TOWN[C]}, with sports.")
if heads:
    say(A, "Here's what we're following this morning.", *[h.rstrip(".?!") + ("?" if h.endswith("?") else ".") for h in heads])
segs.append(("CHIME", "sting"))
cur_who = A
if lead:
    say(A, "Our top story.", *lines_of(lead))
    lead.decompose()
for el in front:
    say(A, *lines_of(el))
if cal: say(A, cal)
if cover: say(A, "On the cover of today's paper: " + cover)

def handoff(to):
    """Hand the mic from whoever spoke last to `to`, by name."""
    global cur_who
    if to == cur_who: return
    if to == A:
        say(A, f"Thanks, {NAME[cur_who]}.")
    else:
        say(cur_who, f"Now to {NAME[to]}, {TOWN[to]}." if to == B else f"For sports, here's {NAME[to]}, {TOWN[to]}.")
        say(to, f"Thanks, {NAME[cur_who]}.")
    cur_who = to

for name, els in sections[1:]:
    low = name.lower()
    match = next((k for k in INTRO if k in low), None)
    who = next((v for k, v in SPEAKER.items() if k in low), A)
    if not any(el.get_text(strip=True) for el in els): continue
    segs.append(("CHIME", "sting"))
    handoff(who)
    say(who, INTRO[match] if match else re.sub(r"^[^A-Za-z]+|[^A-Za-z?!.]+$", "", name) + ".")
    for el in els:
        if not el.get_text(strip=True): continue
        c = el.get("class") or []
        if "towns" in c:
            parts = []
            for t in el.select(".town"):
                n = t.select_one(".n").get_text(strip=True); v = t.select_one(".t").get_text("", strip=True).replace("°", "")
                d_ = t.select_one(".d").get_text(", ", strip=True).lower()
                sky, _, hi = d_.partition(", high")
                parts.append(f"{n}, {v} and {sky}, headed for {hi.strip().replace(chr(176), '')}")
            say(who, "At dawn: " + "; ".join(parts) + ".")
        elif "strip5" in c:
            parts = []
            for t in el.find_all("div", recursive=False):
                g = lambda s: (t.select_one(s).get_text(strip=True) if t.select_one(s) else "")
                parts.append(f"{DAYS.get(g('.d'), g('.d'))}, {g('.w')}, {g('.h')}")
            say(who, "The five-day: " + "; ".join(parts) + ".")
        elif "radar" in c or el.get_text(strip=True).startswith("Next 24 hours") or el.name == "svg":
            continue
        elif "stars" in c:
            for st in el.select(".star"):
                sg = st.select_one(".sg").get_text(strip=True); w = st.select_one(".who")
                wn = w.get_text(strip=True) if w else ""; w and w.decompose(); st.select_one(".sg").decompose()
                say(who, (f"{sg}, for {' and '.join([', '.join(wn.split(', ')[:-1]), wn.split(', ')[-1]]) if ', ' in wn else wn}." if wn else f"{sg}.") + " " + text(st))
        elif "wire" in c:
            n = el.select_one(".num"); n and n.decompose()
            ls = lines_of(el)
            if ls: ls[0] = re.sub(r"\s*·\s*", ": ", ls[0], count=1)
            say(who, *ls)
        elif "ledger" in c:
            big = el.select_one(".big"); cap = el.select_one(".cap"); tx = el.select_one(".txt")
            say(who, f"{big.get_text(strip=True) if big else ''}. {cap.get_text(' ', strip=True) if cap else ''}.", tx.get_text(" ", strip=True) if tx else "")
        elif "qotd" in c:
            q = text(el).replace("Answer below the fold.", "").replace("Tap for the answer", "").strip()
            say(who, q)
            if answer and "question of the day" in low:
                segs.append(("PAUSE", 3.0)); say(who, "The answer: " + answer[0].lower() + answer[1:] if answer[:2] in ("A ", "An") else "The answer: " + answer)
        else:
            say(who, *[re.sub(r"^(\w[\w' ]{0,24}) · ", r"\1. ", l) for l in lines_of(el)])

segs.append(("CHIME", "sting"))
handoff(A)
say(A, f"That's The Bentham Bulletin for this {d:%A}. For John and Reggie, I'm Linda. Have a good day.")
say(C, "See you tomorrow morning.")
segs.append(("CHIME", "close"))

def speakable(l):
    import unicodedata
    l = html.unescape(l)
    l = l.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    l = re.sub(r"(\d)\u2033", r"\1 inches", l).replace("\u00b0", " degrees").replace("\u00bd", " and a half")
    l = re.sub(r"(\d[ap]?)\s*\u2013\s*(\d)", r"\1 to \2", l).replace("\u2013", ", ")
    l = re.sub(r"\s*[\u00b7\u2014|]\s*", ", ", l)
    l = re.sub(r"(\d)a\b", r"\1 a.m.", l); l = re.sub(r"(\d)p\b", r"\1 p.m.", l)
    l = re.sub(r"\b(\d+)h (\d+)m\b", r"\1 hours \2 minutes", l)
    l = re.sub(r"(\d)%", r"\1 percent", l); l = re.sub(r"\s*\(fcst\)", " (forecast)", l); l = re.sub(r"\bmph\b", "miles per hour", l)
    l = re.sub(r"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(?=, [A-Z])", lambda m: {"Mon":"Monday","Tue":"Tuesday","Wed":"Wednesday","Thu":"Thursday","Fri":"Friday","Sat":"Saturday","Sun":"Sunday"}[m.group(1)], l)
    l = re.sub(r"\b(Jan|Feb|Mar|Apr|Aug|Sept?|Oct|Nov|Dec)\.? (?=\d)", lambda m: {"Jan":"January","Feb":"February","Mar":"March","Apr":"April","Aug":"August","Sep":"September","Sept":"September","Oct":"October","Nov":"November","Dec":"December"}[m.group(1)] + " ", l)
    l = re.sub(r"(at )?(https?://)?tally\.so/r/\w+", "on the family form", l); l = re.sub(r"https?://\S+", "", l)
    l = re.sub(r"\bfcst\b", "forecast", l, flags=re.I); l = l.replace(" & ", " and ").replace("&", " and ")
    l = re.sub(r"\b(\d+) hours 0 minutes", r"\1 hours", l)
    l = re.sub(r"\s*\(([^)]*)\)", r", \1,", l); l = re.sub(r",\s*([.;:!?])", r"\1", l)
    l = unicodedata.normalize("NFKD", l).encode("ascii", "ignore").decode()  # accents break the voice engine
    l = re.sub(r"\s+([,.;:])", r"\1", l); l = re.sub(r",\s*,", ",", l); l = re.sub(r"^[,\s]+", "", l)
    l = re.sub(r"\s+", " ", l).strip()
    if l == l.upper() and re.search(r"[A-Z]{3}", l): l = l[0] + l[1:].lower()
    return l
segs = [(w, speakable(t)) if w in (A, B, C) else (w, t) for w, t in segs]
segs = [(w, t if re.search(r"[.!?:;][\"')]?$", t) else t + ".") if w in (A, B, C) else (w, t) for w, t in segs if w not in (A, B, C) or re.search(r"[A-Za-z0-9]", t)]
if maxc:
    n, keep = 0, []
    for sgm in segs:
        n += len(sgm[1]) if sgm[0] in (A, B, C) else 0
        if n > maxc: break
        keep.append(sgm)
    segs = keep
text = "\n".join(t for w, t in segs if w in (A, B, C))
print(f"{len(segs)} segments, {len(text)} chars")
if os.environ.get("SCRIPT_ONLY"):
    for w, t in segs: print(f"[{w}] {t}")
    sys.exit(0)

import lameenc
def mp3(pcm16, rate, path):
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(rate)
    enc.set_channels(1); enc.set_quality(2)
    open(path, "wb").write(enc.encode(pcm16) + enc.flush())

if model.endswith(".onnx"):
    from piper import PiperVoice
    voice = PiperVoice.load(model)
    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "p.wav")
        with wave.open(wav, "wb") as w:
            (voice.synthesize_wav if hasattr(voice, "synthesize_wav") else voice.synthesize)(text, w)
        with wave.open(wav, "rb") as r:
            mp3(r.readframes(r.getnframes()), r.getframerate(), out)
else:
    import numpy as np
    from kokoro import KPipeline
    R = 24000
    VOICES = {A: model, B: os.environ.get("VOICE2", "am_michael"), C: os.environ.get("VOICE3", "am_fenrir")}
    PIPES = {}
    for k, v in VOICES.items():
        lc = "a" if v[0] == "a" else "b"
        PIPES[k] = next((p for kk, p in PIPES.items() if VOICES[kk][0] == v[0]), None) or KPipeline(lang_code=lc)
    def tone(notes, dur=0.55, vol=0.22):
        out = []
        for f in notes:
            t = np.arange(int(R * dur)) / R
            env = np.exp(-t * 5.5) * np.minimum(1, t * 200)
            out.append((np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)) * env * vol)
        x = np.zeros(int(R * dur * (len(notes) - 1) * 0.5 + R * dur))
        for i, o in enumerate(out):
            s0 = int(i * R * dur * 0.5); x[s0:s0 + len(o)] += o
        return x.astype(np.float32)
    CHIMES = {"open": tone([523.25, 659.25, 783.99, 1046.5]), "sting": tone([783.99, 1046.5], 0.45, 0.16),
              "close": tone([1046.5, 783.99, 659.25, 523.25])}
    sil = lambda sec: np.zeros(int(R * sec), dtype=np.float32)
    parts, prev = [], None
    SPEED = {A: 1.0, B: 1.0, C: 1.07}
    for w, t in segs:
        if w == "CHIME":
            parts += [sil(0.25), CHIMES[t], sil(0.35)]; continue
        if w == "PAUSE":
            parts.append(sil(t)); continue
        try:
            chunk = []
            for _, _, audio in PIPES[w](t, voice=VOICES[w], speed=SPEED[w]):
                a_ = audio.numpy() if hasattr(audio, "numpy") else np.asarray(audio)
                chunk.append(a_.astype(np.float32))
            if chunk:
                x = np.concatenate(chunk)
                rms = float(np.sqrt(np.mean(x ** 2))) or 1.0
                x = x * min(4.0, 0.08 / rms)          # even loudness across the three anchors
                short = len(t) < 70                   # headlines and hand-offs get a beat after them
                if prev is not None and prev != w: parts.append(sil(0.25))   # a breath when the anchor changes
                parts += [x, sil(0.6 if short else 0.4)]
                prev = w
        except Exception as e:
            print("skipped line:", t[:60], type(e).__name__)
    pcm = np.clip(np.concatenate(parts), -1, 1)
    mp3((pcm * 32767).astype("<i2").tobytes(), R, out)
print("wrote", out, os.path.getsize(out))
