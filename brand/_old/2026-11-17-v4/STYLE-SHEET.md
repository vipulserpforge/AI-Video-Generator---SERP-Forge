# SERP Forge video style sheet

> **Status: LOCKED, v4 approved 2026-11-17: three fixed frame zones (transcription, visuals lit by a soft radial colour drop, "serpforge.io" watermark at 30 %), center-aligned.** Reference check: `videos/2026-11-test-run/04_storyboard/storyboard-v5.png`, build `videos/2026-11-test-run/05_build/project-v5-check/`. v3 is in `brand/_old/2026-11-17-v3/`. Change only when asked, and move the old version to `brand/_old/` first.

Vertical 1080 x 1920, 30 fps. Colours, fonts and design come from our website (`brand/screenshots/`). Pacing, motion and sound come from `references/analysis/REFERENCE-ANALYSIS.md`. Every value here is also a variable in `brand/tokens.css`: use the variable, never a raw value.

**The look in one line:** a dark charcoal-green UI world with a faint grid and a soft teal glow, white geometric headlines with one italic serif phrase in a mint-to-peach gradient, orange for action, and real-looking cards and data.

## 1. Colours

Every hex was sampled from the screenshots or the logo by script (k-means plus median samples at fixed points), not picked by eye.

| Token | Hex | Name | Role |
|---|---|---|---|
| `--c-bg` | `#0A0E0D` | Ink | Main background |
| `--c-bg-deep` | `#0D2421` | Deep green | Section and stat card background, glow zones |
| `--c-bg-raise` | `#0E1917` | Raised | Large panels |
| `--c-surface` | `#121A19` | Card | Card fill |
| `--c-border` | `#2C3534` | Line | 1 px card border, dividers |
| `--c-grid` | `#FFFFFF` at 4 % | Grid | Background grid lines |
| `--c-glow` | `#0F3832` | Teal glow | Radial glow behind the focal point |
| `--c-text` | `#FFFFFF` | White | Headlines, numbers |
| `--c-text-2` | `#B2B4B4` | Mist | Body and secondary text |
| `--c-muted` | `#77918C` | Sage | Captions, labels, inactive |
| `--c-orange` | `#F8640A` | Forge orange | The one action colour: CTA, key highlight, problem markers |
| `--c-orange-2` | `#F8981D` | Logo orange | Logo, gradient end, warm glow |
| `--c-amber` | `#E2A63D` | Amber | Small uppercase labels, "medium" status |
| `--c-teal` | `#1F9492` | Teal | Toggles, progress, connection lines |
| `--c-teal-logo` | `#008181` | Logo teal | Logo, icons, large fills only (never text) |
| `--c-mint` | `#ABDCD6` | Mint | Gradient start, soft accent text |
| `--c-peach` | `#FCBB82` | Peach | Gradient end on the italic phrase |
| `--c-red` | `#F8534D` | Red | Bad numbers, losses |
| `--c-green` | `#31CD88` | Green | Good numbers, "live" dots, gains |

Signature gradient (the italic serif phrase only): `--g-italic` = `#C2E4DC` to `#FCBB82` (mint to peach, left to right).

### Contrast (WCAG ratio; body text needs 4.5, large titles 3.0)

| Text | on `#0A0E0D` bg | on `#121A19` card | on `#0D2421` deep |
|---|---|---|---|
| White `#FFFFFF` | 19.4 | 17.7 | 16.3 |
| Mist `#B2B4B4` | 9.3 | 8.5 | 7.8 |
| Sage `#77918C` | 5.7 | 5.2 | 4.8 |
| Forge orange `#F8640A` | 6.3 | 5.7 | 5.3 |
| Amber `#E2A63D` | 9.0 | 8.2 | 7.6 |
| Teal `#1F9492` | 5.3 | 4.8 | **4.4: FAIL for body**, large only |
| Logo teal `#008181` | **4.1: FAIL for body** | **3.8: FAIL for body** | **3.5: FAIL for body** (large titles pass) |
| Mint `#ABDCD6` | 12.9 | 11.7 | 10.8 |
| Peach `#FCBB82` | 11.6 | 10.6 | 9.7 |
| Red `#F8534D` | 5.9 | 5.3 | 4.9 |
| Green `#31CD88` | 9.5 | 8.6 | 7.9 |

| Button text | Ratio | |
|---|---|---|
| Ink `#0A0E0D` on orange `#F8640A` | 6.3 | Pass: **our button style** |
| White on orange `#F8640A` | 3.1 | **FAIL for body**, large titles only |
| Ink on teal `#1F9492` | 5.3 | Pass |
| White on teal `#1F9492` | 3.7 | **FAIL for body**, large titles only |
| Ink on amber `#E2A63D` | 9.0 | Pass |

## 2. Typography

| Use | Font | Weight | Size (px) | Line height | Tracking | Max words per line |
|---|---|---|---|---|---|---|
| Title / hook | Outfit | 700 | 104 | 1.02 | -2 % | 3 |
| Italic phrase in a title | Playfair Display Italic | 500 | 112 | 1.0 | -1 % | 3 |
| Hero number | Outfit | 700 | 220 | 0.95 | -3 % | 1 number (5 characters max) |
| Heading | Outfit | 600 | 72 | 1.1 | -1 % | 5 |
| Body | Outfit | 400 | 44 | 1.35 | 0 | 6 |
| Card title | Outfit | 600 | 48 | 1.2 | 0 | 4 |
| Label (uppercase) | Outfit | 600 | 30 | 1.2 | +12 % | 3 |
| Small note (minimum) | Outfit | 400 | 32 | 1.3 | 0 | 6 |

- Outfit is the closest free Google Font to the site's geometric sans. Playfair Display Italic matches its italic serif. Both come bundled with HyperFrames.
- Numbers use `font-variant-numeric: tabular-nums` so counters don't jitter.
- One italic serif phrase per title, at most. It always carries `--g-italic`.
- Nothing readable under 30 px. Cut words rather than shrinking text.

## 3. Layout

- **Platform safe zone** (the TikTok, Reels and Shorts zones combined, from `hyperframes check`): all readable text inside **x 120 to 888 px, y 288 to 1248 px**. Below y = 840 px, text also stays left of x = 780 px (TikTok's button rail). The frame zones (below) were set by hand and take priority: the transcription zone starts at y 240 and the visuals zone runs to y 1587. Inside the visuals zone, keep readable text above y 1248 where possible, because the apps draw their caption and buttons lower down.
- **Alignment: center-aligned.** Every title, label, number, card and visual sits on the frame's vertical centre line (x = 540 px), with text set `text-align: center`. Text inside a UI card (rows, chips, lists) may stay left-aligned like real UI, but the card itself is centred.
- **Grid:** centred text column **x 192 to 888 (696 px, centre 540)**. Below y = 840 px a centred text line is at most 480 px wide (x 300 to 780). 8 px spacing unit (gaps of 16, 24, 32, 48, 64, 96).
- **Cards:** centred, **x 180 to 900 (720 px)**. Below y = 840 px, text inside a card ends by x = 780 px (keep the lines short, or right-pad the card 120 px).
- **Frame zones (fixed, every video, every scene).** Each zone holds only its own content, centred on x = 540 px:

  | Zone | Box (1080 x 1920) | Holds |
  |---|---|---|
  | **Transcription** | x 108 to 972, **y 240 to 495** | The words spoken in the scene, revealed word by word (section 7). Nothing else. |
  | **Visuals** | x 108 to 972, **y 563 to 1587** | Every visual, animation and UI element: cards, charts, icons, numbers, the logo. An invisible area (no box) lit by the colour drop. Nothing else. |
  | **Watermark** | x 108 to 972, **y 1656 to 1718** | The text "serpforge.io" (section 8). Nothing else. |

  Between and around the zones: only background and glow. Visuals are centred vertically and horizontally inside the visuals zone.
- **Colour drop (light behind the visuals zone):** not a box. A soft radial teal-green light centred on the visuals zone (x 540, y 1075), about 1500 x 1650 px, from `rgb(22,84,66)` at the centre through `rgb(16,62,50)` to nothing at the edge, so it fades into the background with no edge, border or shadow (matched to the website hero: `#0D2D25` glow on `#0A1110`). The teal-tinted grid stays visible through it. The visuals zone itself is only an area: every visual, animation and UI element appears inside it, centred, on top of this light.
- **Background:** `--c-bg` with a faint teal-tinted 56 px grid (`--c-grid`, mint at 6 %), lit by the colour drop behind the visuals zone. Optional warm orange glow under a CTA.
- **Corner radius:** cards 32 px, inner elements and inputs 20 px, buttons and pills 999 px (fully round), icon tiles 20 px.
- **Card style:** `--c-surface` fill, 1.5 px `--c-border` border, 32 px padding, soft shadow `0 24px 60px rgba(0,0,0,.45)`. The hero card can carry a 1.5 px orange or teal border instead.
- **Icons:** 2 px outline line icons in `--c-text-2`, or a filled icon inside a 20 px-radius tile tinted `--c-bg-deep`. Real tool logos are shown only as small marks on cards.
- **Elements:** at most 4 meaningful elements on screen (title + up to 3). One focal point.

## 4. Motion

| Token | Curve | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` (expo.out) | All arrivals |
| `--ease-back` | `cubic-bezier(.34, 1.56, .64, 1)` (back.out 1.4) | Tiles, badges, number landings (overshoot ~6 %) |
| `--ease-in` | `cubic-bezier(.7, 0, .84, 0)` (power3.in) | Exits, zoom-through |
| `--ease-inout` | `cubic-bezier(.65, 0, .35, 1)` (power2.inOut) | Camera moves, colour floods |

- **Durations:** entrance 0.5 s (cards and titles), 0.35 s for small items. Exit 0.25 s (about half the entrance). Transitions 0.35 to 0.6 s.
- **Stagger:** words 0.08 s, list items 0.06 s, cards 0.12 s. The next element starts when the previous one is about 40 % done.
- **Text reveal:** per word, a mask wipe from below (the word rises 40 % of its height inside a clipped line box) plus blur 6 px to 0, over 0.4 s. Each word lands on its spoken word (within 2 frames). The highlighted word lands last.
- **Highlight:** the key word gets a 16 px-radius orange box (`--c-orange` at 18 %) that wipes in left to right in 0.25 s after the word lands.
- **Numbers:** count up over 0.8 to 1.4 s with an accelerating start and a soft landing (expo.out on the value). A bar, ring or line grows with them. On landing: a 1.06 to 1.0 scale settle (back.out) plus the number sound.
- **Camera:** the whole stage drifts 12 to 24 px vertically over a scene, with power2.inOut. A scale drift is allowed only on full-frame imagery with no text near the safe-zone edges, because scaling pushes edge text out of the zone. Never a creeping zoom on a landed title.
- **Landed titles stay dead still.** No floating, breathing or pulsing loops.
- **Motion blur:** 6 to 12 px on fast moves (whips, tile wipes) only.
- **Rhythm:** something new every 2 to 3 s, never more than 3.5 s without a change. Scenes 2 to 6 s long.

## 5. Transitions (use only these four)

| Transition | How | When |
|---|---|---|
| **Tile wipe** (signature) | A grid of 120 px rounded squares in the logo's teal, mint and orange sweeps diagonally across in 0.5 s (ease-inout) and reveals the next scene | Between chapters and big ideas (at most 3 per video) |
| **Card zoom-through** | The focal card scales up past the frame in 0.5 s (ease-in); its fill becomes the next background | Going "into" a tool, report or detail |
| **Blur swap** | Out: opacity to 0 with 8 px blur in 0.2 s. In: blur 8 to 0 in 0.25 s. The background stays | Between points inside the same idea (the most common) |
| **Whip** | 0.25 s vertical smear (12 px motion blur), the arriving element lands blurred and sharpens | Fast lists, "but" turns, pace boosts |

No crossfades between scenes and no hard cut without a sound. At most a third of scene changes are plain cuts.

## 6. Sound

Real recorded sounds from `library/sfx` (the Real SFX skill), checked with earshot.

| Moment | Sound | Level |
|---|---|---|
| Transition (tile wipe, whip, zoom) | Soft air whoosh, 0.25 to 0.5 s, peaks on the transition's fastest frame | -18 dB |
| Text reveal (key title) | Light UI tick or soft pop on the highlighted word | -24 dB |
| Card or UI element in | Bubble pop or click | -22 dB |
| Number count | A quick tick roll during the count and a bright ding on landing | ticks -28 dB, ding -18 dB |
| Impact (big claim, problem) | Low soft hit or sub thump | -16 dB |
| Click (button, toggle) | Real mouse click | -20 dB |
| Logo outro | Short warm chime or riser into a soft hit | -16 dB |

- **Voice:** -16 LUFS on its own, peaks no higher than -3 dBFS. Always the loudest thing.
- **Music:** modern tech or lo-fi bed with no vocals and a soft beat. -30 LUFS under the voice (about 14 to 18 dB below it). Ducks a further 8 to 10 dB whenever the voice speaks and returns within 0.3 s in pauses.
- **Effects:** -18 to -28 dB (table above) so they never mask a word.
- **Master:** -14 LUFS integrated, true peak -1 dBTP.
- Every transition gets a sound. Every key reveal gets a sound. Never two strong sounds within 0.15 s.

## 7. Transcription zone

- **What:** the exact words spoken in the scene (from `02_audio/transcript.json`), never paraphrased. One phrase of the voice per scene, as the title. No other line repeats the voice: there is no bottom subtitle pill.
- **Where:** the transcription zone, y 240 to 495, centred, `text-align: center`, text column x 192 to 888 (696 px).
- **Type:** Outfit 700 with one italic Playfair phrase (gradient), sized to fit the zone: **2 lines at 104 px**, or **3 lines at 80 px** (italic 88 px) when the phrase needs 3 lines. Never more than 3 lines, never cut words.
- **Motion:** each word reveals on its own start time (mask rise + blur, section 4), the key word gets the orange highlight box. Frame 0's hook phrase is fully on screen (thumbnail).

## 8. Watermark

- **What:** the text **serpforge.io** (not the logo).
- **Where:** the watermark zone, centred on x = 540, vertical centre y = 1687 px.
- **Type:** Outfit 600, 30 px, letter spacing +4 %, white at **30 % opacity** (low, subtle, still readable).
- On every frame, no animation, above the background. Nothing else in its zone.
- Note: on TikTok and Reels the app's own caption and username can sit over this area.

## 9. Do and do not

1. **Do** have the hook fully on screen at frame 0 (it is the thumbnail): a bold line or a number. No intro, no logo first. The other elements build in around it.
2. **Do** reveal text word by word in time with the voice, with one accented word per line.
3. **Do** use real-looking UI (reports, dashboards, search results, chat) instead of abstract shapes.
4. **Do** make every number move: count, grow a bar, draw a line.
5. **Do** use colour for meaning: orange = action or attention, green = good, red = bad, amber = labels.
6. **Do** give every transition a whoosh and every key reveal a sound.
7. **Do** keep each thing in its zone: spoken words in the transcription zone, visuals on the colour drop, "serpforge.io" in the watermark zone. **Don't** add a bottom subtitle pill or a logo watermark.
8. **Don't** use random circles, lines, blobs or "floating" decoration. The grid and glow are the only texture.
9. **Don't** use more than 4 elements or more than one focal point on screen.
10. **Don't** copy the reference videos' words, products, numbers, logos or colours. Take techniques only.
