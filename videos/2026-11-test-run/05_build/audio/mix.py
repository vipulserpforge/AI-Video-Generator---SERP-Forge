"""Deterministic mix for the test run (brand/STYLE-SHEET.md section 6, approved visual script).

Voice -16 LUFS. Music bed ducked 9 dB while the voice speaks (80 ms attack, 300 ms release).
SFX peak-normalised to their style-sheet level; whooshes placed so their loudest point is on the transition.
Master -14 LUFS integrated, true peak <= -1 dBTP. Writes mix.wav plus stems and cues.json.
Run: python -I mix.py   (from this folder)
"""
import json, os, subprocess
import numpy as np
import pyloudnorm as pyln

SR = 48000
DUR = 16.77
N = int(round(DUR * SR))
FF = "/opt/homebrew/bin/ffmpeg"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))       # project root
VID = os.path.abspath(os.path.join(HERE, "..", ".."))                      # videos/2026-11-test-run
MK = os.path.join(ROOT, "library", "sfx", "mixkit")
UI = os.path.expanduser("~/.claude/skills/real-sfx/vendor/node_modules/uisfx/sounds")

def load(path, start=0.0, dur=None):
    cmd = [FF, "-v", "error", "-ss", str(start), "-i", path]
    if dur: cmd += ["-t", str(dur)]
    cmd += ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)

def db(x): return 10 ** (x / 20)

def filt(x, af):
    out = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", af, "-f", "f64le", "-"],
                         input=x.astype(np.float64).tobytes(), capture_output=True, check=True).stdout
    y = np.frombuffer(out, np.float64)
    return np.pad(y, (0, max(0, len(x) - len(y))))[:len(x)]
meter = pyln.Meter(SR)

def lufs(x):
    x = x if len(x) > SR // 2 else np.pad(x, (0, SR // 2))
    return meter.integrated_loudness(x)

def peak_norm(x, target_db):
    p = np.max(np.abs(x)) or 1.0
    return x * (db(target_db) / p)

def fade(x, fin=0.004, fout=0.02):
    x = x.copy(); a, b = int(fin * SR), int(fout * SR)
    if a: x[:a] *= np.linspace(0, 1, a)
    if b and len(x) > b: x[-b:] *= np.linspace(1, 0, b)
    return x

# ---------------- voice ----------------
voice = load(os.path.join(VID, "02_audio", "final.mp3"))
voice = np.pad(voice, (0, max(0, N - len(voice))))[:N]
voice *= db(-16 - lufs(voice))

# speech intervals = inverse of silencedetect (-35 dB, 0.25 s) on final.mp3
silences = [(2.750, 3.990), (4.884, 5.148), (5.608, 6.026), (8.203, 8.772), (11.139, 11.541), (13.023, 13.990), (16.417, 16.771)]
speech, t = [], 0.16
for a, b in silences:
    if a > t: speech.append((t, a))
    t = b
duck = np.ones(N)
env_db = np.zeros(N)
for a, b in speech:
    i0, i1 = int((a - 0.08) * SR), int(b * SR)
    env_db[max(0, i0):i1] = -9.0 if a < 13.55 else -5.0   # s06: lighter duck keeps the end card's energy up (earshot: ending too quiet)
# smooth: 80 ms attack, 300 ms release (one-pole on the dB curve, forward pass)
att, rel = np.exp(-1 / (0.08 * SR)), np.exp(-1 / (0.30 * SR))
sm = np.empty(N); y = 0.0
for i in range(N):
    x = env_db[i]; c = att if x < y else rel
    y = c * y + (1 - c) * x; sm[i] = y
duck = db(sm)

# ---------------- music ----------------
MUSIC = os.path.join(ROOT, "library", "music", "mixkit", "mixkit-1167_close-up.mp3")
# stereo track: the mid (L+R)/2 goes through the mono mix; the side (L-R)/2 is added back at the end (earshot: nearly mono)
cmd = [FF, "-v", "error", "-ss", "21.27", "-i", MUSIC, "-t", str(DUR + 0.5), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
st = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64).reshape(-1, 2)[:N]
st = np.pad(st, ((0, N - len(st)), (0, 0)))
music, side = (st[:, 0] + st[:, 1]) / 2, (st[:, 0] - st[:, 1]) / 2
EQ = "highpass=f=50:poles=2,highpass=f=50:poles=2,lowshelf=f=90:g=-6"   # earshot: sub 20-60 Hz too high
music, side = filt(music, EQ), filt(side, EQ)
mg = db(-21 - lufs(music))              # gaps -21 LUFS; under the voice about -30 LUFS after the 9 dB duck
music, side = music * mg * duck, side * mg * duck * db(-17)   # narrow: refs sit at -40..-28 dB side/mid
fo = int(0.35 * SR); fi = int(0.02 * SR)
for x in (music, side):
    x[-fo:] *= np.linspace(1, 0, fo); x[:fi] *= np.linspace(0, 1, fi)

# ---------------- sfx cues (film time, file, level dB, align: onset|peak, note) ----------------
def mk(n): return os.path.join(MK, n)
def ui(p): return os.path.join(UI, p)
WH_AIR, WH_ARROW, WH_CINE = mk("mixkit-1489_whoosh_air.wav"), mk("mixkit-1491_whoosh_arrow.wav"), mk("mixkit-1492_whoosh_cinematic-fast.wav")
HIT, CLICK, TYPE = mk("mixkit-2299_hit_short-bass.wav"), mk("mixkit-1113_click_mouse-close.wav"), mk("mixkit-1387_typing_fast-keyboard.wav")
POP_A, POP_B = mk("mixkit-2356_pop_dry-notification.wav"), mk("mixkit-2357_pop_bubble-alert.wav")
DING_A, DING_B = mk("mixkit-951_ding_positive-notification.wav"), mk("mixkit-2870_ding_correct-answer.wav")
CHIME, TICK = ui("soft/achievement.mp3"), ui("studio/hover.mp3")

cues = [
    (1.00, TYPE, -28, "onset", "s01 question types in", 0.5),
    (1.89, POP_B, -22, "onset", "s01 row 1 lands", None),
    (1.95, POP_A, -26, "onset", "s01 row 2 lands", None),
    (2.01, POP_A, -26, "onset", "s01 row 3 lands", None),
    (3.80, WH_AIR, -18, "peak", "s01>s02 blur swap", None),
    (4.71, CLICK, -22, "onset", "s02 empty slot appears", None),
    (5.24, HIT, -16, "onset", "s02 'on' / Not listed", None),
    (5.95, WH_CINE, -18, "peak", "s02>s03 tile wipe", None),
    (6.14, CHIME, -18, "onset", "s03 logo on 'SERP'", None),
    (7.60, POP_A, -22, "onset", "s03 search card", None),
    (8.18, DING_A, -18, "onset", "s03 'found'", None),
    (8.45, WH_ARROW, -18, "peak", "s03>s04 whip", None),
    (8.85, POP_A, -22, "onset", "s04 card A on 'Google'", None),
    (9.05, TICK, -24, "onset", "s04 #1 tile", None),
    (9.52, HIT, -16, "onset", "s04 'and'", None),
    (10.05, POP_B, -22, "onset", "s04 card B on 'AI'", None),
    (10.26, DING_B, -18, "onset", "s04 'Cited' chip", None),
    (11.35, WH_CINE, -18, "peak", "s04>s05 zoom-through", None),
] + [(11.77 + k * 0.12, TICK, -28, "onset", f"s05 bar tick {k+1}", None) for k in range(6)] + [
    (12.52, DING_A, -18, "onset", "s05 green bar on 'visibility'", None),
    (13.55, WH_AIR, -18, "peak", "s05>s06 blur swap", None),
    (13.80, CHIME, -16, "onset", "s06 logo outro", None),
    (14.12, CLICK, -20, "onset", "s06 URL pill", None),
]

sfx = np.zeros(N)
report = []
for t, path, lvl, align, note, maxdur in cues:
    x = load(path, dur=maxdur)
    x = fade(peak_norm(x, lvl))
    if align == "peak":
        env = np.abs(x); k = int(np.argmax(np.convolve(env, np.ones(480) / 480, mode="same")))
    else:
        thr = 0.1 * np.max(np.abs(x)); k = int(np.argmax(np.abs(x) > thr))
    s = int(round(t * SR)) - k
    a, b = max(0, s), min(N, s + len(x))
    if b > a: sfx[a:b] += x[a - s:b - s]
    report.append({"t": round(t, 3), "file": os.path.relpath(path, ROOT) if path.startswith(ROOT) else "uisfx/" + os.path.relpath(path, UI),
                   "level_db": lvl, "align": align, "note": note, "frame": int(round(t * 30))})

# ---------------- master ----------------
sfx = filt(sfx, "highpass=f=50:poles=2,highpass=f=50:poles=2")
voice = filt(voice, "highpass=f=60:poles=2")                         # no useful voice energy below 60 Hz
raw_mix = voice + music + sfx

def limit(x, gain_db):
    """gain, then a 4x-oversampled look-ahead brickwall at -1.5 dBFS (alimiter), back to 48 kHz"""
    out = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-",
                          "-af", f"volume={gain_db}dB,aresample=192000,alimiter=limit=0.84:attack=3:release=60:level=disabled:asc=1,aresample={SR}",
                          "-f", "f64le", "-"], input=x.astype(np.float64).tobytes(), capture_output=True, check=True).stdout
    return np.frombuffer(out, np.float64)[:N]

def true_peak(x):
    over = subprocess.run([FF, "-v", "error", "-f", "f64le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", "aresample=192000", "-f", "f64le", "-"],
                          input=x.astype(np.float64).tobytes(), capture_output=True, check=True).stdout
    return 20 * np.log10(np.max(np.abs(np.frombuffer(over, np.float64))) + 1e-12)

def stereo(mid, gain_db):
    """limited mid (voice + sfx + music mid) plus the music's side, as L/R"""
    s = side * db(gain_db)
    return np.stack([mid + s, mid - s], axis=1)

def lufs_lr(lr): return meter.integrated_loudness(lr)

g = -14 - lufs_lr(np.stack([raw_mix, raw_mix], axis=1))
for _ in range(5):                      # converge on -14 LUFS (stereo, as delivered) after limiting
    lr = stereo(limit(raw_mix, g), g)
    g += -14 - lufs_lr(lr)
lr = stereo(limit(raw_mix, g), g)
tp_l, tp_r = true_peak(lr[:, 0]), true_peak(lr[:, 1])
if max(tp_l, tp_r) > -1.0:              # the side can push a channel over the limiter's ceiling: trim to -1 dBTP
    lr *= db(-1.0 - max(tp_l, tp_r))

def write(name, x, ch=1):
    p = os.path.join(HERE, name)
    subprocess.run([FF, "-v", "error", "-y", "-f", "f64le", "-ar", str(SR), "-ac", str(ch), "-i", "-", "-c:a", "pcm_s24le", p],
                   input=np.ascontiguousarray(x, dtype=np.float64).tobytes(), check=True)
    return p

write("mix.wav", lr, 2); write("stem_voice.wav", voice); write("stem_music.wav", np.stack([music + side, music - side], 1), 2); write("stem_sfx.wav", sfx)
json.dump({"duration": DUR, "music": {"file": os.path.relpath(MUSIC, ROOT), "start_in_track": 21.27, "gap_lufs": -21, "duck_db": -9, "duck_db_s06": -5, "stereo": True},
           "voice_lufs": -16, "master_lufs": -14, "cues": report}, open(os.path.join(HERE, "cues.json"), "w"), indent=1)
print("mix LUFS (stereo) %.1f, true peak L %.1f R %.1f dBTP before trim, cues %d" % (lufs_lr(lr), tp_l, tp_r, len(report)))
