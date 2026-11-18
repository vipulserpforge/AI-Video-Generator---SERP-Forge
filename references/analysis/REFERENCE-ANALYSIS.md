# Reference analysis

Three vertical explainers (720 x 1280, 30 fps). All are kinetic-type product/tool explainers driven by a voice-over.
We take **techniques only**. Their words, products, logos, names, numbers and colours are not ours and are never reused.

Method: FFmpeg scene detection (threshold 0.30 for hard cuts, 0.12 for soft changes), one frame per second plus one frame at each cut, 10 fps motion strips of key moments, a 10 fps frame-difference count of "change onsets", and earshot `timeline` plus a 100 ms RMS level spread for the audio.
Frames and contact sheets: `references/analysis/reference-N/` (`1fps/`, `cuts/`, `contact-1fps.jpg`, `motion_*.jpg`, `cuts.txt`, `soft-changes.txt`).

## Numbers at a glance

| | Ref 1 | Ref 2 | Ref 3 |
|---|---|---|---|
| Length | 50.0 s | 32.7 s | 54.3 s |
| Hard cuts (scene > 0.30) | 0 | 4 (2.6, 11.6 s) | 16 |
| Average shot length | one continuous canvas | ~8 s (continuous scenes) | **3.2 s** |
| Something new on screen | every 1.2 s (median 0.9 s) | every 1.2 s (median 0.9 s) | every 0.9 s (median 0.6 s) |
| Longest still moment | 2.6 s | 3.6 s | 3.6 s |
| Frames with motion | 37 % | 27 % | 73 % |
| Background | light grey + faint pixel grid | near-black navy | alternates light grey / dark green |
| Loudness | -14.1 LUFS | -16.1 LUFS | -14.1 LUFS |
| Bed under voice peaks | ~19 dB | ~16 dB | ~12 dB |
| Sound events | 6.7 / s | 6.1 / s | 7.6 / s |
| Cuts with a sound within 100 ms | 80 % | 85 % | **100 %** |

## Reference 1: light "countdown list" explainer

- **Structure:** a numbered list ("0/5" progress tiles at the top) that fills in as each item is covered. The viewer always knows where they are.
- **Text:** a one-line caption near the bottom, word by word. The spoken word is dark and the next words are pale grey, so you read ahead of the voice. Big headline text sits up top in a bold geometric sans (black), with one key phrase in a blue accent.
- **Motion:** dark number tiles are tossed in from off-screen left with a spin (about 15 to 25°) and land with an overshoot and a small settle. About 0.4 s each, staggered about 0.1 s. Counters (e.g. star counts) count up in about 1 s with a star icon that pops on. Product cards slide up and fade in.
- **Transitions:** almost no hard cuts. Elements leave and new ones arrive on one continuous canvas. One dark section (33 to 39 s) arrives as a full-frame colour change.
- **Open:** the hook headline is on screen at 0.0 s and builds word by word. **End:** a "comment KEYWORD" call to action with a fake comment card.
- **Sound:** corporate/tech bed, glockenspiel-like notes on reveals, bubble pops on cards, one riser into the dark section. A sound hits within 100 ms of 80 % of the changes.
- **Best at:** progress tracking (the 0/5 tiles) and the pre-read caption.

## Reference 2: dark "data story" explainer

- **Structure:** proof (a chart), then the problem (retention graphs), then the fix (old vs new comparison), then the call to action.
- **Text:** small centred caption at the top, word by word. The keyword gets a **filled highlight box** (blue) behind it as it is spoken.
- **Motion:** the big counter **accelerates** (ease-in, close to exponential) from 737 to 1.3 M in about 1.5 s while a line chart draws in step. Highlight rings (amber outline) pop around a number. Cards blur and scale in from about 92 %. A big title lands from about 130 % scale down to 100 %.
- **Transitions:** a hard cut to a white frame behind a **scale-up icon** (about 0.3 s), then the screen dims and a whip whoosh plays.
- **Colour:** near-black navy with amber for warnings and blue for growth. Colour carries meaning: amber = problem, blue = good.
- **Open:** a split comparison of two posts (good vs bad) answers "why?" at 0.0 s. **End:** a "comment GROW" card with a DM preview.
- **Sound:** whip-pan whooshes on transitions, plucked notes on reveals, soft UI pops. The quietest of the three (-16 LUFS) and the most room for the voice.
- **Best at:** turning numbers into a story (counter + chart together) and using colour for meaning.

## Reference 3: fast light/dark "product feature" explainer

- **Structure:** claim, proof number, feature 1, feature 2, comparison, feature 3, call to action. A new idea every 3 to 4 s.
- **Text:** large bold headline at the top, word by word, in a tight geometric sans with negative tracking. One word per line turns brand green or gets a green underline. Sometimes the headline is so large it bleeds off the edges for impact.
- **Motion:** a pixel-block wipe/dissolve between light and dark scenes (about 0.3 to 0.4 s). Numbers roll like an odometer, settling in about 0.6 s. UI cards tilt in 3D and scale. Small square "pixel" particles drift as a texture.
- **Transitions:** the pixel-block wipe is the signature, plus straight cuts when the background stays the same.
- **Colour:** one accent green on both light grey and charcoal-green backgrounds, with soft glows behind the hero element.
- **Open:** a big brand word plus a product card at 0.0 s. **End:** "Just comment WORD", the logo, a profile card.
- **Sound:** tech-house/funk bed, a UI pop or swish on every cut (100 % of cuts have a sound within 100 ms, median 21 ms). The music sits loudest under the voice (only ~12 dB below).
- **Best at:** pace and sync. Every cut has a sound, and something new happens every 0.6 to 0.9 s.

## What all three share

1. **The first frame is already the hook.** No intro, no logo sting, no blank frame.
2. **Text appears word by word, in time with the voice.** Never a full paragraph at once. One keyword per line is accented.
3. **One hero element per moment** (a number, a card or a chart). Everything else is pushed back or dimmed.
4. **Real-looking UI** (cards, dashboards, chat bubbles, charts) instead of abstract shapes.
5. **Numbers always move**: they count up, roll or draw a chart.
6. **Something changes every 0.6 to 1.2 s.** Nothing is ever still for more than about 3.6 s.
7. **Sound follows the picture.** 80 to 100 % of changes get a sound within 100 ms: pops for UI, whooshes for transitions, notes for reveals.
8. **The music bed is low** (12 to 19 dB under the voice) and has no strong beat grid, so it never fights the voice.
9. **Masters at -14 to -16 LUFS** for social platforms.
10. **They all end on a "comment X" call to action** with the brand mark.

## What we take from each

| From | We take | Our rule |
|---|---|---|
| Ref 1 | Progress tiles for list videos; dark word = spoken, pale = coming; tile toss with overshoot | Use progress tiles in any "N things" video. Tiles land with overshoot (back-out). |
| Ref 2 | Counter + chart moving together; filled highlight box on keywords; colour = meaning | Numbers count with an accelerating ease and a chart or bar that grows with them. Keywords get a highlight box. Orange = problem/attention, green = good. |
| Ref 3 | 0.6 to 3 s pacing; a sound on every cut; one bold accent colour on light and dark; the signature transition | New element at least every 2 to 3 s, a sound on every transition, and our own signature transition (a rounded-square "tile wipe", based on our logo). |

**Subtitles:** tried in v2 (Ref 1's bottom pill), removed on 2026-11-17: it repeated the on-screen title. Our only speech-following text is the centred title revealed word by word.

**Not taken:** the off-edge headline bleed (it breaks our safe margins), their product names, UI copies, numbers, logos and colour palettes.

---

# References 4 and 5 (added 2026-11-17): variety, smoothness, premium subtitles

Two newer vertical explainers (720 x 1280, 30 fps): Ref 4 (71.6 s, light canvas, blue accent) and Ref 5 (43.7 s, warm light canvas, peach accent). Frames: `reference-4/`, `reference-5/` (1fps, cuts, contact sheet, `motion_*.jpg`). Subtitle crops: `subtitle-study/subs-4-5.png`, motion strips: `subtitle-study/motion-4-5.jpg`.
We take techniques only, never their content, products, names or colours.

## Measured smoothness (`tools/smooth.py`)

| | Ref 4 | Ref 5 | Ref 3 | Our test-run |
|---|---|---|---|---|
| Hard cuts | 1 in 71 s | 0 in 44 s | 16 | 0 (but 4 full-frame transitions) |
| Frames with motion | 39 % | 13 % | 83 % | 14 % |
| Burstiness (share of all motion in the busiest 5 % of frames) | **48 %** | **57 %** | 53 % | **78 %** |
| Single-frame pops | 0.08 /s | 0.57 /s | 0.33 /s | 0 /s |

Why ours felt jumpy: the motion was clumped into a few big full-frame events (tile wipe, whip, zoom-through, blur swaps of the whole stage) with still holds between them. The references spread change over many frames and never move the whole frame at once.

## How they stay smooth while fast

1. **One continuous canvas.** No scene cuts. The background and the stage persist; only the objects on it change.
2. **Objects become the next object.** A repo card shrinks into a phone card, lines grow out of it to more cards (Ref 5); a small input box grows into a full field, a badge fades and blurs as icons burst out of it (Ref 4).
3. **Build, don't swap.** Timelines add one track per spoken word, grids fill cell by cell, lists add a row per word. The visual grows instead of being replaced.
4. **Short travel, soft combos.** Elements move tens of pixels, not across the screen, always combining opacity + small scale (about 0.92 to 1) + blur (about 6 px to 0). Long ease-out tails, no hard stops.
5. **Exits overlap entrances.** The old element blurs and fades (0.3 to 0.4 s) while the new one is already arriving.
6. **Only one or two things move fast at once.** Everything else holds still or drifts slowly.

## Variety of visual formats (no two beats look alike)

Ref 4: hero app icon with blur glow, a field of app tiles with one highlighted, flow diagram (logo → line chart → app), rotated price stamp ("$0"), icon constellation around a big number, terminal with typing, easing-curve graph with keyframe diamonds, audio waveform with timed caption chips, bouncing-square physics arc, mini dashboard with a bar chart, stacked cards with a red ✗, search bar + messy scribble → clean upward line, list of people with "?" questions, staircase drop chart with a calendar, lightbulb idea tile, crowd of people icons, dark keyboard close-up while typing, script page with an Approve button, storyboard grid of icons, circular workflow orbit with a big number, comment card with a CTA pill.
Ref 5: repo card with a star counter and spark line, phone card branching into a network of cards, centred product name card, feed card with view counts, terminal-style agent command, script page with highlighted lines, editing timeline with tracks filling per word, before/after ≠ comparison with a checklist, giant number + grid of 100 tiles, receipt card with "$0" and a green check, install command with a success pill, comment card with a giant stamped keyword.

## Premium subtitles

- **Regular weight, not bold.** Normal words in a regular/light sans (about 400) in mid grey; only the key words switch to a dark semibold (about 600).
- **Key-word styles:** Ref 4: the key word in an accent-coloured italic serif ("*broke*") or the last word in semibold; Ref 5: a thin accent **selection frame** with tiny square corner handles around the key word or phrase (design-tool look).
- **Reveal:** words appear one by one with the voice; the previous phrase blurs out as the new one starts. One or two lines, centred.
- **Context line above:** a tiny spaced-caps label (brand name or "01 · SET UP" chapter pills) sits above the subtitle.

## What we take

| Take | Our rule (STYLE-SHEET v5) |
|---|---|
| Continuous canvas, objects become objects | No full-frame transitions; scenes hand over by morph, carry, build-on or a soft overlapped crossfade (section 5) |
| Spread, soft motion | Smoothness rules + a measured target: burstiness at most 60 %, no single-frame pops (section 4) |
| Format variety | A visual format library; never the same format twice in a row; at least 5 formats per video (section 10) |
| Premium subtitles | Outfit 400 for normal words, 600 for key words, subtle shadow, three key-word styles incl. the selection frame (section 7) |
