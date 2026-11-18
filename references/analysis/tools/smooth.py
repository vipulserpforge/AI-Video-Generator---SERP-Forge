"""Motion smoothness: compare how picture change is spread over frames.
For each video: per-frame mean abs difference (luma, 180x320). A 'pop' is a frame whose change is
>3x both neighbours and above a floor: something appeared/jumped in one frame with no easing.
'Burstiness' = share of all motion that happens in the top 5% of frames (high = jerky, low = spread / eased).
Also the median length (frames) of continuous motion runs: longer = moves are eased over more frames."""
import subprocess, sys
import numpy as np

def frames(path):
    raw = subprocess.run(["/opt/homebrew/bin/ffmpeg", "-v", "error", "-i", path, "-vf", "scale=180:320,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, 320, 180).astype(np.float32)

for path in sys.argv[1:]:
    f = frames(path)
    d = np.abs(np.diff(f, axis=0)).mean((1, 2))
    floor = 0.6
    moving = d > floor
    pops = [i for i in range(1, len(d) - 1) if d[i] > floor * 3 and d[i] > 3 * d[i - 1] and d[i] > 3 * d[i + 1]]
    top = np.sort(d)[::-1]; k = max(1, int(0.05 * len(d)))
    burst = top[:k].sum() / max(d.sum(), 1e-9)
    runs, r = [], 0
    for m in moving:
        if m: r += 1
        elif r: runs.append(r); r = 0
    if r: runs.append(r)
    dur = len(f) / 30
    print(f"{path.split('/')[-1]:<22} dur {dur:5.1f}s  moving {100*moving.mean():4.0f}%  pops {len(pops):3d} ({len(pops)/dur:.2f}/s)  "
          f"burstiness {100*burst:4.0f}%  median move run {np.median(runs) if runs else 0:4.0f} fr  mean change {d.mean():.2f}")
