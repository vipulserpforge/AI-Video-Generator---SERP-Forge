# SERP Forge build kit (start every new video's build from here)

Copy these into `05_build/project/assets/` of every new video (CLAUDE.md step 7/9), together with `brand/tokens.css`:

| File | What it gives you |
|---|---|
| `shared.css` | scene root, the **dotted background** (`.grid`), the colour drop, the 3 zones (`.tx` transcription, `.vz` visuals in Inter), **window cards** (`.wcard` + `data-title`), logo/icon tiles, chips, the **animated selection frame** (`.k-frame` > `.fr` > `.sel` with 4 `<i>` handles), the **highlight box** (`.hl` > `.box` + `.txt`, solid #F8981C, dark ink word), the italic accent, and the typing letters + caret |
| `subtitle-typing.js` | `window.sfType(tl, "#sXX")`: types every `.tx [data-t][data-e]` word letter by letter (silent), with the orange caret; italic letters keep the gradient; sets `data-done` / `data-dur` on each word for key-word styles |

How to use in a scene (see `videos/2026-11-test-run-v2/05_build/project` as the working example):
- `index.html` head: `tokens.css`, `shared.css`, gsap, then `<script src="assets/subtitle-typing.js"></script>`; the watermark div `#wm`.
- Transcription: `<h1 class="tx">` with each spoken word as `<span class="wd" data-t="start" data-e="end">` (scene-local seconds from transcript.json); key words keep their style class (`b`, `italic`, `k-frame`, `hl`). Then call `window.sfType(tl, "#sXX")` in the scene script.
- Selection frame: open at the first key word's start (`.sel` opacity 0 to 1 in 2 frames) and stretch `width` 34% to 100% with `back.out(1.2)` (never scaleX).
- Highlight box: `scaleX` 0 to 1 from the word's `data-t` over its `data-dur` + 0.08 s.
- Frame 0's hook line in s01 is plain text, fully on screen (no typing, no caret).
