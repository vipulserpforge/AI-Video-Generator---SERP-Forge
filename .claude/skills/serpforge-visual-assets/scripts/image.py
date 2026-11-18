"""Finish a real image (Chrome screenshot or downloaded photo) so it sits naturally in a SERP Forge video.

Usage:
  python -I image.py <in> <out.png> --size 860x540 [--fit cover|contain] [--focus 0.5,0.4] [--look screenshot|photo] [--strength 1.0]
Light, honest edits only (never changes what the image shows):
  - crop to the frame's aspect around a focus point (cover) or letterbox it on the card colour (contain), Lanczos resize
  - screenshot: a touch of contrast and clarity, crisp text (unsharp), no colour cast
  - photo: contrast + clarity, slightly richer colour, a gentle cool-teal grade in the shadows to match the brand,
           and a soft vignette so the eye stays in the frame
Output: PNG at exactly the requested size (2x for retina sharpness is recommended: ask for 1720x1080 to show at 860x540).
"""
import argparse
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageChops
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--size", required=True); ap.add_argument("--fit", default="cover", choices=["cover", "contain"])
ap.add_argument("--focus", default="0.5,0.4"); ap.add_argument("--look", default="screenshot", choices=["screenshot", "photo"])
ap.add_argument("--strength", type=float, default=1.0)
a = ap.parse_args()
W, H = (int(v) for v in a.size.lower().split("x")); fx, fy = (float(v) for v in a.focus.split(","))
k = a.strength

im = Image.open(a.src); im = ImageOps.exif_transpose(im).convert("RGB")
if a.fit == "cover":
    im = ImageOps.fit(im, (W, H), method=Image.LANCZOS, centering=(fx, fy))
else:
    im.thumbnail((W, H), Image.LANCZOS)
    bg = Image.new("RGB", (W, H), (18, 26, 25)); bg.paste(im, ((W - im.width) // 2, (H - im.height) // 2)); im = bg

if a.look == "screenshot":
    im = ImageEnhance.Contrast(im).enhance(1 + 0.04 * k)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=int(60 * k), threshold=2))
else:
    im = ImageEnhance.Contrast(im).enhance(1 + 0.08 * k)
    im = ImageEnhance.Color(im).enhance(1 + 0.06 * k)
    im = im.filter(ImageFilter.UnsharpMask(radius=2.0, percent=int(45 * k), threshold=3))
    arr = np.asarray(im).astype(np.float32) / 255.0
    lum = arr.mean(2, keepdims=True); shadow = np.clip(1 - lum * 1.6, 0, 1)            # teal only in the shadows
    teal = np.array([0.06, 0.22, 0.19], np.float32)
    arr = arr * (1 - 0.10 * k * shadow) + teal * (0.10 * k * shadow)
    yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    arr = arr * (1 - 0.18 * k * np.clip((r - 0.6) / 0.8, 0, 1))[..., None]               # soft vignette
    im = Image.fromarray(np.clip(arr * 255, 0, 255).astype(np.uint8))
im.save(a.out, optimize=True)
print(f"{a.out}  {W}x{H}  look={a.look} strength={k}")
