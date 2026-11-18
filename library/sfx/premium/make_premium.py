"""Make smooth, pleasant ("premium") versions of the six SFX categories.

Each source is a real recording (Mixkit, uisfx). The chain only cleans and softens it, never synthesises:
  trim leading silence -> cap length -> high-pass -> soften highs (high shelf / low-pass) -> tiny fade-in (no snap)
  -> long natural fade-out -> peak-normalise to a common preview level.
Outputs (library/sfx/premium/):
  <category>_A.wav, <category>_B.wav   the processed variants (preview level, peak -6 dBFS)
  preview_<category>.wav                A, 0.9 s silence, B  (for listening in chat)
Run: python -I make_premium.py
"""
import os, subprocess
FF = "/opt/homebrew/bin/ffmpeg"
HERE = os.path.dirname(os.path.abspath(__file__))
MK = os.path.abspath(os.path.join(HERE, "..", "mixkit"))
UI = os.path.expanduser("~/.claude/skills/real-sfx/vendor/node_modules/uisfx/sounds")

def chain(maxlen, hp, shelf_db=-4, lp=None, fin=0.004, fout_frac=0.45, pre=""):
    f = [pre] if pre else []
    f += ["silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.005",
          f"atrim=0:{maxlen}", "asetpts=PTS-STARTPTS",
          f"highpass=f={hp}:poles=2"]
    if shelf_db: f.append(f"highshelf=f=6000:g={shelf_db}")
    if lp: f.append(f"lowpass=f={lp}:poles=1")
    f += [f"afade=t=in:st=0:d={fin}:curve=qsin",
          f"afade=t=out:st={maxlen*(1-fout_frac):.3f}:d={maxlen*fout_frac:.3f}:curve=exp",
          "aresample=48000", "aformat=channel_layouts=stereo"]
    return ",".join(f)

# category: [(label, source, filter chain), ...]
SPEC = {
  "1_whoosh":   [("A", f"{MK}/mixkit-1489_whoosh_air.wav",              chain(0.75, 120, -4, None, 0.02, 0.5)),
                 ("B", f"{MK}/mixkit-1461_whoosh_short-wind-swoosh.wav", chain(0.75, 120, -4, None, 0.02, 0.5))],
  "2_riser":    [("A", f"{MK}/mixkit-790_riser_cinematic-trailer.wav",   chain(2.2, 90, -3, 11000, 0.35, 0.18)),
                 ("B", f"{MK}/mixkit-645_riser_cinematic-synth.wav",     chain(2.2, 90, -3, 11000, 0.35, 0.18))],
  "3_subdrop":  [("A", f"{MK}/mixkit-2300_subdrop_knocking-sub-bass.wav", chain(1.3, 30, -6, 6000, 0.006, 0.6)),
                 ("B", f"{MK}/mixkit-2299_hit_short-bass.wav",            chain(1.3, 30, -6, 6000, 0.006, 0.6))],
  "4_pop_blip": [("A", f"{MK}/mixkit-2356_pop_dry-notification.wav",      chain(0.45, 150, -4, 12000, 0.003, 0.55)),
                 ("B", f"{UI}/soft/hover.mp3",                            chain(0.35, 150, -3, 12000, 0.003, 0.55))],
  "5_click_tap":[("A", f"{MK}/mixkit-2568_click_cool-interface-tone.wav", chain(0.35, 150, -5, 9000, 0.002, 0.6)),
                 ("B", f"{MK}/mixkit-1125_click_typewriter-soft.wav",     chain(0.30, 150, -5, 9000, 0.002, 0.6))],
  "6_shutter":  [("A", f"{MK}/mixkit-1432_shutter_digital.wav",           chain(0.6, 150, -5, 10000, 0.002, 0.5)),
                 ("B", f"{MK}/mixkit-1440_shutter_classic-camera-click.wav", chain(0.6, 150, -5, 10000, 0.002, 0.5))],
}

def run(args):
    subprocess.run([FF, "-v", "error", "-y"] + args, check=True)

def peak_norm(src, dst, target=-6.0):
    out = subprocess.run([FF, "-v", "info", "-i", src, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    mx = float(out.split("max_volume:")[1].split("dB")[0])
    run(["-i", src, "-af", f"volume={target - mx}dB", "-c:a", "pcm_s24le", dst])

tmp = os.path.join(HERE, "_tmp.wav")
for cat, items in SPEC.items():
    outs = []
    for lab, src, af in items:
        run(["-i", src, "-af", af, "-c:a", "pcm_s24le", tmp])
        dst = os.path.join(HERE, f"{cat}_{lab}.wav"); peak_norm(tmp, dst); outs.append(dst)
    # flashbulb: shutter A + a very short soft airy shimmer (the start of the air whoosh, high-passed) a few ms later
    if cat == "6_shutter":
        run(["-i", f"{MK}/mixkit-1432_shutter_digital.wav", "-i", f"{MK}/mixkit-1489_whoosh_air.wav", "-filter_complex",
             "[0]" + chain(0.6, 150, -5, 10000, 0.002, 0.5) + "[s];"
             "[1]atrim=0.25:0.65,asetpts=PTS-STARTPTS,highpass=f=3500:poles=2,lowpass=f=12000,volume=-9dB,"
             "afade=t=in:d=0.03:curve=qsin,afade=t=out:st=0.12:d=0.28:curve=exp,adelay=25|25,aresample=48000,aformat=channel_layouts=stereo[f];"
             "[s][f]amix=inputs=2:normalize=0", "-c:a", "pcm_s24le", tmp])
        dst = os.path.join(HERE, f"{cat}_C-flash.wav"); peak_norm(tmp, dst); outs.append(dst)
    # preview: variants separated by 0.9 s silence
    inputs, fc = [], ""
    for i, o in enumerate(outs):
        inputs += ["-i", o]; fc += f"[{i}]apad=pad_dur=0.9[a{i}];"
    fc += "".join(f"[a{i}]" for i in range(len(outs))) + f"concat=n={len(outs)}:v=0:a=1"
    run(inputs + ["-filter_complex", fc, "-c:a", "pcm_s24le", os.path.join(HERE, f"preview_{cat}.wav")])
    print(cat, "->", ", ".join(os.path.basename(o) for o in outs))
os.remove(tmp)
