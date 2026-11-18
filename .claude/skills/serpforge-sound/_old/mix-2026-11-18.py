"""SERP Forge mixer: voice + ducked music + approved premium SFX -> mastered stereo soundtrack.

Usage:  python -I mix.py <path/to/cues.json>
cues.json (paths relative to the project root, the folder holding CLAUDE.md):
{
  "voice": "videos/<video>/02_audio/final.mp3",
  "duration": 16.77,                       # optional, default = voice length
  "music": {"file": "library/music/mixkit/mixkit-324_smooth-meditation.mp3", "start": 20.0,     # OPTIONAL, house default is NO music: only when the user asks
            "gap_lufs": -32, "duck_db": -10, "end_card_from": 13.55, "end_card_duck_db": -6, "width_db": -17},
  "cues": [ {"t": 3.80, "type": "whoosh", "note": "s01>s02 handover"},
            {"t": 5.24, "type": "subdrop"}, {"t": 1.00, "type": "click", "level": -30, "note": "typing"} ]
}
Types: whoosh (peak-aligned), riser (end-aligned), subdrop, pop, click, shutter (onset-aligned). "level" overrides the default.
Writes next to cues.json: mix.wav (stereo, -14 LUFS, <= -1 dBTP), stem_voice.wav, stem_music.wav, stem_sfx.wav, mix_report.json.
Rules from SKILL.md are checked and printed as WARN lines.
"""
import json, os, subprocess, sys
import numpy as np
import pyloudnorm as pyln

SR = 48000
FF = "/opt/homebrew/bin/ffmpeg" if os.path.exists("/opt/homebrew/bin/ffmpeg") else "ffmpeg"
SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPES = {   # file, default peak level dB, alignment, strong?
    "whoosh":  ("whoosh.wav",  -22, "peak",  True),
    "riser":   ("riser.wav",   -24, "end",   True),
    "subdrop": ("subdrop.wav", -18, "onset", True),
    "pop":     ("pop.wav",     -24, "onset", False),
    "click":   ("click.wav",   -26, "onset", False),
    "shutter": ("shutter.wav", -22, "onset", False),
}
LIMITS = {"riser": 2, "subdrop": 3, "shutter": 2}

def root_of(path):
    d = os.path.dirname(os.path.abspath(path))
    while d != "/" and not os.path.exists(os.path.join(d, "CLAUDE.md")):
        d = os.path.dirname(d)
    return d

def db(x): return 10 ** (x / 20)
meter = pyln.Meter(SR)
def lufs(x):
    x = x if len(x) > SR // 2 else np.pad(x, ((0, SR // 2),) + ((0, 0),) * (x.ndim - 1))
    return meter.integrated_loudness(x)

def load(path, start=0.0, dur=None, ch=1):
    cmd = [FF, "-v", "error", "-ss", str(start), "-i", path] + (["-t", str(dur)] if dur else [])
    cmd += ["-ac", str(ch), "-ar", str(SR), "-f", "f32le", "-"]
    a = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)
    return a.reshape(-1, ch) if ch > 1 else a

def filt(x, af):
    out = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", af, "-f", "f64le", "-"],
                         input=np.ascontiguousarray(x).tobytes(), capture_output=True, check=True).stdout
    y = np.frombuffer(out, np.float64)
    return np.pad(y, (0, max(0, len(x) - len(y))))[:len(x)]

def speech_intervals(voice_path, total):
    err = subprocess.run([FF, "-v", "info", "-i", voice_path, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(l.split("silence_start: ")[1]) for l in err.splitlines() if "silence_start: " in l]
    ends = [float(l.split("silence_end: ")[1].split()[0]) for l in err.splitlines() if "silence_end: " in l]
    sil = list(zip(starts, ends + [total] * (len(starts) - len(ends))))
    out, t = [], 0.0
    for a, b in sil:
        if a > t + 0.02: out.append((t, a))
        t = b
    if t < total - 0.05: out.append((t, total))
    return out

def write(path, x):
    ch = 1 if x.ndim == 1 else x.shape[1]
    subprocess.run([FF, "-v", "error", "-y", "-f", "f64le", "-ar", str(SR), "-ac", str(ch), "-i", "-", "-c:a", "pcm_s24le", path],
                   input=np.ascontiguousarray(x, dtype=np.float64).tobytes(), check=True)

def main(cues_path):
    cfg = json.load(open(cues_path)); ROOT = root_of(cues_path); OUT = os.path.dirname(os.path.abspath(cues_path))
    lib = os.path.join(ROOT, "library", "sfx", "premium", "approved")
    voice_path = os.path.join(ROOT, cfg["voice"])
    voice = load(voice_path)
    dur = float(cfg.get("duration") or len(voice) / SR); N = int(round(dur * SR))
    voice = np.pad(voice, (0, max(0, N - len(voice))))[:N]
    voice = filt(voice * db(-16 - lufs(voice)), "highpass=f=60:poles=2")
    warns = []

    # ---- music: stereo bed, ducked under speech
    m = cfg.get("music"); music = np.zeros(N); side = np.zeros(N); speech = speech_intervals(voice_path, dur)
    if m:
        st = load(os.path.join(ROOT, m["file"]), start=m.get("start", 0), dur=dur + 0.5, ch=2)[:N]
        st = np.pad(st, ((0, N - len(st)), (0, 0)))
        # music is a near-silent bed: no lows that boom, and a permanent dip where the words live (speech band)
        EQ = ("highpass=f=50:poles=2,highpass=f=50:poles=2,lowshelf=f=90:g=-6,"
              "equalizer=f=900:t=q:w=1.0:g=-5,equalizer=f=2600:t=q:w=1.0:g=-6")
        music, side = filt((st[:, 0] + st[:, 1]) / 2, EQ), filt((st[:, 0] - st[:, 1]) / 2, EQ)
        env = np.zeros(N)
        for a, b in speech:
            d = m.get("duck_db", -10)
            if m.get("end_card_from") is not None and a >= m["end_card_from"]: d = m.get("end_card_duck_db", -6)
            env[max(0, int((a - 0.08) * SR)):int(b * SR)] = d
        att, rel = np.exp(-1 / (0.08 * SR)), np.exp(-1 / (0.30 * SR)); sm = np.empty(N); y = 0.0
        for i in range(N):
            c = att if env[i] < y else rel; y = c * y + (1 - c) * env[i]; sm[i] = y
        g = db(m.get("gap_lufs", -32) - lufs(music)) * db(sm)
        music, side = music * g, side * g * db(m.get("width_db", -17))
        fo, fi = int(0.35 * SR), int(0.02 * SR)
        for x in (music, side):
            x[-fo:] *= np.linspace(1, 0, fo); x[:fi] *= np.linspace(0, 1, fi)

    # ---- speech mask (voice first: effects that overlap speech are made quieter and moved out of the speech band)
    spm = np.zeros(N, bool)
    for a, b in speech:
        spm[max(0, int((a - 0.05) * SR)):min(N, int((b + 0.05) * SR))] = True
    VOICE_DUCK_DB, VOICE_EQ = -5.0, "equalizer=f=2500:t=q:w=1.2:g=-5"   # SKILL.md section 4

    # ---- effects
    sfx = np.zeros(N); placed = []; seen = {}; segs = []; contrib = []
    for c in sorted(cfg["cues"], key=lambda c: c["t"]):
        if c["type"] not in TYPES: warns.append(f"unknown type {c['type']} at {c['t']}"); continue
        fname, lvl, align, strong = TYPES[c["type"]]
        k = seen.get(c["type"], 0); seen[c["type"]] = k + 1
        var_db, var_rate = [0, -1.2, -0.6, -1.8][k % 4], [1.0, 1.025, 0.98, 1.012][k % 4]   # deterministic variation
        x = load(os.path.join(lib, fname))
        if var_rate != 1.0:
            x = filt(x, f"asetrate={int(SR*var_rate)},aresample={SR}")
        p = np.max(np.abs(x)) or 1.0
        x = x * db(c.get("level", lvl) + var_db) / p
        env = np.convolve(np.abs(x), np.ones(480) / 480, mode="same")
        if align == "peak": anchor = int(np.argmax(env))
        elif align == "end": anchor = int(np.flatnonzero(env > 0.05 * env.max())[-1])
        else: anchor = int(np.argmax(np.abs(x) > 0.1 * np.max(np.abs(x))))
        s = int(round(c["t"] * SR)) - anchor; a, b = max(0, s), min(N, s + len(x))
        # active part of the effect (envelope above 20 % of its peak), in film samples
        act = np.flatnonzero(env > 0.2 * env.max()); aa, ab = max(0, s + act[0]), min(N, s + act[-1] + 1)
        overlap = spm[aa:ab].mean() if ab > aa else 0.0
        ducked = bool(overlap > 0.25)
        if ducked:   # voice first: lower it and carve the 2.5 kHz speech-presence band out of it
            x = filt(x, VOICE_EQ) * db(VOICE_DUCK_DB)
        contrib.append((s, x))
        segs.append((aa, ab))
        placed.append({"t": c["t"], "type": c["type"], "level_db": round(c.get("level", lvl) + var_db + (VOICE_DUCK_DB if ducked else 0), 1),
                       "align": align, "strong": strong, "under_voice": ducked, "speech_overlap": round(float(overlap), 2),
                       "note": c.get("note", ""), "frame": int(round(c["t"] * 30))})

    # ---- audible but never over the voice (SKILL.md section 4): calibrate every effect against its surroundings
    #      1. raise it until its loudest 50 ms sits NOTICE_DB above the music around it (at most +MAX_BOOST dB)
    #      2. but under speech never let it come closer than VOICE_GAP dB to the voice in the speech band (300 Hz - 4 kHz)
    #      3. if it still cannot be noticed, make room: dip the music (max 4 dB, smooth 40 ms) for that moment only
    NOTICE_DB, VOICE_GAP, MAX_BOOST = 4.0, 13.0, 10.0
    NOTICE_UNDER_VOICE_DB, MAX_DIP, MAX_DIP_UNDER_VOICE = 1.0, 4.0, 6.0   # under speech an effect only has to be felt
    BAND = "highpass=f=300:poles=2,lowpass=f=4000:poles=2"
    def rms_db(x): return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)
    def peak50(x):
        w = int(0.05 * SR)
        return max(rms_db(x[i:i + w]) for i in range(0, max(1, len(x) - w + 1), w // 2))
    voice_b = filt(voice, BAND); mdip = np.zeros(N); pad = int(0.04 * SR)
    for i, (p, (aa, ab), (s, x)) in enumerate(zip(placed, segs, contrib)):
        if ab - aa < int(0.02 * SR): continue
        seg = filt(x, "highpass=f=50:poles=2")[aa - s:ab - s]
        mu = rms_db(music[aa:ab]) if m else -120.0
        sp = spm[aa:ab]; under = sp.mean() > 0.25
        target = NOTICE_UNDER_VOICE_DB if under else NOTICE_DB
        gain = min(MAX_BOOST, max(0.0, target - (peak50(seg) - mu)))
        if under:
            room = rms_db(voice_b[aa:ab][sp]) - rms_db(filt(seg, BAND)[sp]) - VOICE_GAP
            gain = min(gain, max(0.0, room))
        contrib[i] = (s, x * db(gain)); p["boost_db"] = round(gain, 1); p["level_db"] = round(p["level_db"] + gain, 1)
        short = target - (peak50(seg) + gain - mu)
        if m and short > 0.5:
            d = -min(MAX_DIP_UNDER_VOICE if under else MAX_DIP, short + 1.0); lo, hi = max(0, aa - pad), min(N, ab + pad)
            mdip[lo:hi] = np.minimum(mdip[lo:hi], d); p["music_dip_db"] = round(d, 1)
    if m and mdip.min() < 0:
        k = np.ones(pad) / pad; g = db(np.convolve(mdip, k, mode="same"))
        music, side = music * g, side * g
    for s, x in contrib:
        a, b = max(0, s), min(N, s + len(x))
        if b > a: sfx[a:b] += x[a - s:b - s]

    # ---- rule checks (SKILL.md sections 2-3)
    strong_t = [p["t"] for p in placed if p["strong"]]
    for x1, x2 in zip(strong_t, strong_t[1:]):
        if x2 - x1 < 0.15: warns.append(f"two strong sounds {x2-x1:.2f} s apart at {x1:.2f}/{x2:.2f}")
    for typ, lim in LIMITS.items():
        n = sum(p["type"] == typ for p in placed)
        if n > lim: warns.append(f"{n} x {typ}, limit {lim}")
    wt = [p["t"] for p in placed if p["type"] == "whoosh"]
    for x1, x2 in zip(wt, wt[1:]):
        if x2 - x1 < 1.5: warns.append(f"whooshes {x2-x1:.2f} s apart at {x1:.2f}")
    sd = [p["t"] for p in placed if p["type"] == "subdrop"]
    for x1, x2 in zip(sd, sd[1:]):
        if x2 - x1 < 6: warns.append(f"sub-drops {x2-x1:.2f} s apart at {x1:.2f}")
    for t0 in np.arange(0, max(dur - 9.99, 0.01), 5.0):
        ts = [0] + [p["t"] - t0 for p in placed if t0 <= p["t"] < t0 + 10] + [min(10, dur - t0)]
        if max(np.diff(sorted(ts))) < 1.5: warns.append(f"no 1.5 s of air between {t0:.0f} and {t0+10:.0f} s")
    for t0 in np.arange(0, dur, 1.0):
        n = sum(t0 <= p["t"] < t0 + 1 and p["type"] == "pop" for p in placed)
        if n > 3: warns.append(f"{n} pops within 1 s at {t0:.0f} s")
    dens = len(placed) / dur
    if not 0.6 <= dens <= 1.8: warns.append(f"density {dens:.2f} effects/s (aim 0.6 to 1.8)")

    # ---- voice-first level check per effect (SKILL.md section 4):
    #      under speech the effect sits >= 10 dB below the voice; everywhere it sits >= 3 dB above the music so it is noticed
    #      "disturbs the voice" is measured in the speech band (300 Hz - 4 kHz), where words are understood;
    #      "is noticed" compares the effect's loudest 50 ms with the music around it (a short sound is heard by its attack).
    sfx_hp = filt(sfx, "highpass=f=50:poles=2,highpass=f=50:poles=2")
    sfx_b, voice_b = filt(sfx_hp, BAND), filt(voice, BAND)
    w = int(0.05 * SR)
    for p, (aa, ab) in zip(placed, segs):
        if ab - aa < int(0.02 * SR): continue
        seg = sfx_hp[aa:ab]
        pk = max(rms_db(seg[i:i + w]) for i in range(0, max(1, len(seg) - w + 1), w // 2))
        mu = rms_db(music[aa:ab]) if m else -120.0
        p["peak50_db"] = round(pk, 1); p["above_music_db"] = round(pk - mu, 1)
        sp = spm[aa:ab]
        if sp.mean() > 0.25:
            v, e = rms_db(voice_b[aa:ab][sp]), rms_db(sfx_b[aa:ab][sp])
            p["below_voice_speechband_db"] = round(v - e, 1)
            if v - e < 10: warns.append(f"{p['type']} at {p['t']:.2f}: only {v-e:.1f} dB under the voice in the speech band (needs >= 10): lower it")
        under = sp.mean() > 0.25
        if m and not under and pk - mu < 3:
            warns.append(f"{p['type']} at {p['t']:.2f}: only {pk-mu:.1f} dB over the music in a pause (needs >= 3): raise it a little")
        if m and under and pk - mu < -1.0:   # voice wins: it cannot get louder without crowding the words
            warns.append(f"{p['type']} at {p['t']:.2f}: under a spoken word it can only reach {pk-mu:.1f} dB vs the music: "
                         f"keep it subtle (felt, not heard) or move it to the nearest pause / a softer moment")

    # ---- master: -14 LUFS stereo, <= -1 dBTP
    sfx = filt(sfx, "highpass=f=50:poles=2,highpass=f=50:poles=2")
    mid = voice + music + sfx
    def limit(x, g):
        out = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af",
                              f"volume={g}dB,aresample=192000,alimiter=limit=0.84:attack=3:release=60:level=disabled:asc=1,aresample={SR}",
                              "-f", "f64le", "-"], input=mid.tobytes() if x is None else x.tobytes(), capture_output=True, check=True).stdout
        return np.frombuffer(out, np.float64)[:N]
    def lr(g):
        mm = limit(mid, g); s = side * db(g); return np.stack([mm + s, mm - s], 1)
    g = -14 - lufs(np.stack([mid, mid], 1))
    for _ in range(5):
        g += -14 - lufs(lr(g))
    out = lr(g)
    over = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af", "aresample=192000", "-f", "f64le", "-"],
                          input=np.ascontiguousarray(out).tobytes(), capture_output=True, check=True).stdout
    tp = 20 * np.log10(np.max(np.abs(np.frombuffer(over, np.float64))) + 1e-12)
    if tp > -1.0: out *= db(-1.0 - tp)

    write(os.path.join(OUT, "mix.wav"), out); write(os.path.join(OUT, "stem_voice.wav"), voice)
    write(os.path.join(OUT, "stem_music.wav"), np.stack([music + side, music - side], 1)); write(os.path.join(OUT, "stem_sfx.wav"), sfx)
    rep = {"duration": dur, "lufs": round(lufs(out), 2), "true_peak_dbtp": round(min(tp, -1.0), 2), "speech": speech,
           "density_per_s": round(dens, 2), "cues": placed, "warnings": warns}
    json.dump(rep, open(os.path.join(OUT, "mix_report.json"), "w"), indent=1)
    print(f"mix.wav  {rep['lufs']} LUFS, true peak <= {rep['true_peak_dbtp']} dBTP, {len(placed)} effects, {dens:.2f}/s")
    for w in warns: print("WARN", w)
    if not warns: print("rules: all passed")

if __name__ == "__main__":
    main(sys.argv[1])
