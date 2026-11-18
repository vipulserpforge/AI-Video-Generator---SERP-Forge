"""Smooth "premium" versions of the new SFX types: light (shine/glow), pop-in, breaking. Same chain as make_premium.py.
Real Mixkit recordings only (free Mixkit licence), never synthesised. Outputs to _alternates/ and _previews/.
Run: python3 -I make_premium_v2.py
"""
import os, subprocess
FF = "/opt/homebrew/bin/ffmpeg"
HERE = os.path.dirname(os.path.abspath(__file__))
MK = os.path.abspath(os.path.join(HERE, "..", "mixkit"))
DL = os.path.join(MK, "_download-2026-11-18")

def chain(maxlen, hp, shelf_db=-4, lp=None, fin=0.004, fout_frac=0.45):
    f = ["silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.005",
         f"atrim=0:{maxlen}", "asetpts=PTS-STARTPTS", f"highpass=f={hp}:poles=2"]
    if shelf_db: f.append(f"highshelf=f=6000:g={shelf_db}")
    if lp: f.append(f"lowpass=f={lp}:poles=1")
    f += [f"afade=t=in:st=0:d={fin}:curve=qsin",
          f"afade=t=out:st={maxlen*(1-fout_frac):.3f}:d={maxlen*fout_frac:.3f}:curve=exp",
          "aresample=48000", "aformat=channel_layouts=stereo"]
    return ",".join(f)

SPEC = {
  "7_light":  [("A", f"{DL}/mixkit-3083_light_magic-sparkle-touch.mp3", chain(1.2, 300, -5, 11000, 0.02, 0.55)),
               ("B", f"{DL}/mixkit-871_light_fairy-magic-sparkle.mp3",  chain(1.1, 300, -5, 11000, 0.02, 0.55)),
               ("C", f"{MK}/mixkit-3108_chime_crystal.wav",              chain(1.2, 300, -4, 11000, 0.01, 0.6))],
  "8_popin":  [("A", f"{MK}/mixkit-3005_pop_explainer-light.wav",        chain(0.18, 150, -4, 12000, 0.003, 0.5)),
               ("B", f"{DL}/mixkit-2354_popin_message-pop-alert.mp3",    chain(0.4, 150, -4, 12000, 0.003, 0.55)),
               ("C", f"{DL}/mixkit-2925_popin_soap-bubble.mp3",          chain(0.4, 150, -4, 12000, 0.003, 0.55))],
  "9_break":  [("A", f"{DL}/mixkit-759_break_glass-hammer-thud.mp3",     chain(1.0, 70, -5, 10000, 0.003, 0.5)),
               ("B", f"{DL}/mixkit-2952_break_tech-impact.mp3",          chain(1.0, 50, -4, 10000, 0.003, 0.5)),
               ("C", f"{DL}/mixkit-2951_break_digital-glitch.mp3",       chain(0.8, 120, -5, 10000, 0.003, 0.5))],
}

def run(args): subprocess.run([FF, "-v", "error", "-y"] + args, check=True)
def peak_norm(src, dst, target=-6.0):
    out = subprocess.run([FF, "-v", "info", "-i", src, "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    mx = float(out.split("max_volume:")[1].split("dB")[0])
    run(["-i", src, "-af", f"volume={target - mx}dB", "-c:a", "pcm_s24le", dst])

tmp = os.path.join(HERE, "_tmp.wav")
for cat, items in SPEC.items():
    outs = []
    for lab, src, af in items:
        run(["-i", src, "-af", af, "-c:a", "pcm_s24le", tmp])
        dst = os.path.join(HERE, "_alternates", f"{cat}_{lab}.wav"); peak_norm(tmp, dst); outs.append(dst)
    inputs, fc = [], ""
    for i, o in enumerate(outs):
        inputs += ["-i", o]; fc += f"[{i}]apad=pad_dur=1.0[a{i}];"
    fc += "".join(f"[a{i}]" for i in range(len(outs))) + f"concat=n={len(outs)}:v=0:a=1"
    run(inputs + ["-filter_complex", fc, "-c:a", "pcm_s16le", os.path.join(HERE, "_previews", f"preview_{cat}.wav")])
    print(cat, "->", ", ".join(os.path.basename(o) for o in outs))
os.remove(tmp)
