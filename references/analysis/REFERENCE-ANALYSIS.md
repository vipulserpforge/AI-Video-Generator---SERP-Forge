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

**Subtitles (added 2026-11-16):** Ref 1's subtitle pill (2 to 3 words, pale words turning dark as they are spoken, a solid box on the key word, about 75 % down the frame) and Ref 2's grey-to-white word fill. We restyle both in our colours: a dark pill, sage to white, an orange key-word box, left-aligned at y 1268 px (see STYLE-SHEET.md section 7).

**Not taken:** the off-edge headline bleed (it breaks our safe margins), their product names, UI copies, numbers, logos and colour palettes.
