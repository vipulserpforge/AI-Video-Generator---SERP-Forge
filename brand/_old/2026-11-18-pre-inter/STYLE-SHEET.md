# SERP Forge video style sheet

> **Status: LOCKED, v6 approved 2026-11-17, sound section updated with the approved premium effects (serpforge-sound skill):** visuals fill the marked box (x 80 to 1000, y 585 to 1510), and every boxed visual is a window card (title bar, window dots, lowercase title). Builds on v5 (white transcription, smoothness rules, handovers, 17-format library). Reference check: `videos/2026-11-test-run/04_storyboard/storyboard-v9.png`, build `videos/2026-11-test-run/05_build/project-v8-check/`. v5 is in `brand/_old/2026-11-17-v5/`. Change only when asked, and move the old version to `brand/_old/` first.

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
| Transcription, normal words | Outfit | **400**, white | 76 (2 lines) / 64 (3 lines) | 1.12 | -1 % | 5 |
| Transcription, key words | Outfit | **700 (bold)**, white | same as the line | 1.12 | -1 % | 1 to 3 words |
| Transcription, italic key phrase | Playfair Display Italic | 500 | line size + 8 | 1.0 | -1 % | 3 |
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

- **Platform safe zone** (the TikTok, Reels and Shorts zones combined, from `hyperframes check`): all readable text inside **x 120 to 888 px, y 288 to 1248 px**. Below y = 840 px, text also stays left of x = 780 px (TikTok's button rail). The frame zones (below) were set by hand and take priority: the transcription zone starts at y 240 and the visuals zone runs to y 1510. Inside the visuals zone, keep readable text above y 1248 where possible, because the apps draw their caption and buttons lower down.
- **Alignment: center-aligned.** Every title, label, number, card and visual sits on the frame's vertical centre line (x = 540 px), with text set `text-align: center`. Text inside a UI card (rows, chips, lists) may stay left-aligned like real UI, but the card itself is centred.
- **Grid:** centred text column **x 192 to 888 (696 px, centre 540)**. Below y = 840 px a centred text line is at most 480 px wide (x 300 to 780). 8 px spacing unit (gaps of 16, 24, 32, 48, 64, 96).
- **Cards:** centred, sized to fill the visuals zone (about 860 to 920 px wide). Text inside cards may reach the card's right edge; note that below y = 840 px TikTok's button rail can sit over x 780 to 1000.
- **Frame zones (fixed, every video, every scene).** Each zone holds only its own content, centred on x = 540 px:

  | Zone | Box (1080 x 1920) | Holds |
  |---|---|---|
  | **Transcription** | x 108 to 972, **y 240 to 495** | The words spoken in the scene, revealed word by word (section 7). Nothing else. |
  | **Visuals** | **x 80 to 1000, y 585 to 1510** (920 x 925, centre x 540, y 1047) | Every visual, animation and UI element: cards, charts, icons, numbers, the logo. An invisible area (no box) lit by the colour drop. Nothing else. |
  | **Watermark** | x 108 to 972, **y 1656 to 1718** | The text "serpforge.io" (section 8). Nothing else. |

  Between and around the zones: only background and glow.
- **Visuals fill their zone.** Every visual composition (cards, charts, icons, logo, diagrams, together) is centred on x 540, y 1047 and **fills 85 to 100 % of the zone's width or height**, whichever it reaches first. It never spills outside the zone and is never a small object floating in empty space. Scale the whole composition up (cards about 860 to 920 px wide, card text about 1.25 times the base sizes) rather than adding more elements.
- **Colour drop (light behind the visuals zone):** not a box. A soft radial teal-green light centred on the visuals zone (x 540, y 1047), about 1500 x 1500 px, from `rgb(22,84,66)` at the centre through `rgb(16,62,50)` to nothing at the edge, so it fades into the background with no edge, border or shadow (matched to the website hero: `#0D2D25` glow on `#0A1110`). The teal-tinted grid stays visible through it. The visuals zone itself is only an area: every visual, animation and UI element appears inside it, centred, on top of this light.
- **Background:** `--c-bg` with a faint teal-tinted 56 px grid (`--c-grid`, mint at 6 %), lit by the colour drop behind the visuals zone. Optional warm orange glow under a CTA.
- **Corner radius:** cards 32 px, inner elements and inputs 20 px, buttons and pills 999 px (fully round), icon tiles 20 px.
- **Window card (every boxed visual):** whenever a visual sits in a box (UI, a chat, a report, a repo, a chart, a terminal), it is a premium desktop-app window, like a macOS window:
  - **Frame:** `--c-surface` fill, radius 28 px, 1.5 px `--c-border` border, shadow `0 24px 60px rgba(0,0,0,.45)`.
  - **Title bar:** 56 px tall, a slightly darker fill (`--win-bar` `#0E1514`) with a 1 px `--c-border` line under it.
  - **Window dots:** three 14 px dots, 10 px apart, 24 px from the left edge, vertically centred: red `#F8534D`, amber `#E2A63D`, green `#31CD88`, each at 85 % opacity.
  - **Title:** centred in the bar, lowercase, Outfit 500, 24 px, sage `#77918C`, letter spacing +2 % (for example "repository", "ai search", "analytics", "terminal").
  - **Body:** 32 px padding under the bar. A small breadcrumb line (icon + "owner / **name**") and an outlined pill tag are good openers, as in the reference.
  - The title bar replaces a separate uppercase card label when they would say the same thing.
  - Not every visual needs a box: hero objects, stamps, counters, constellations and orbits stay free-standing. When there is a box, it is always a window card.
- **Icons, logos and images** (full rules: the serpforge-visual-assets skill): icons from **Phosphor** (duotone for features, fill for tiny status marks; Lucide only as a fallback), chosen for the exact idea, mint or white with a meaning-coloured second tone, in a 20 px-radius tile (`--c-bg-deep`, mint border at 15 %). Never letters, numbers or emoji standing in for an icon. **Logos are always the official marks** (theSVG / Simple Icons / the brand's own files), never redrawn; on dark use the light variant or a white tile. **Real images and Chrome screenshots** wherever the script names something real, lightly finished (crop, clarity, a gentle teal grade for photos) and shown inside a window card.
- **Elements:** at most 4 meaningful elements on screen (title + up to 3). One focal point.

## 4. Motion

**The goal is smooth, never jumpy:** fast pace, but every change is spread over several frames on one continuous canvas, like references 4 and 5. Measured with `references/analysis/tools/smooth.py` on every render: **burstiness at most 60 %** (refs 48 to 57 %, our first test 78 %) and **no single-frame pops**.

| Token | Curve | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` (expo.out) | Arrivals of big elements (cards, charts, the stage) |
| `--ease-soft` | `cubic-bezier(.22, 1, .36, 1)` (power3.out) | Arrivals of text, icons and small items |
| `--ease-back` | `cubic-bezier(.34, 1.3, .64, 1)` (back.out 1.2) | Only small chips and badges (overshoot about 3 %). Never on cards, charts or text |
| `--ease-exit` | `cubic-bezier(.55, 0, 1, .45)` (power2.in) | Exits |
| `--ease-inout` | `cubic-bezier(.65, 0, .35, 1)` (power2.inOut) | Morphs, carries, camera drift |

**Smoothness rules (every video):**
1. **One continuous canvas.** The background, grid, colour drop and zones never cut or move. Only the objects in the visuals zone change. No hard cuts and no full-frame wipes, whips or zooms.
2. **Objects become the next object.** Hand a scene over by turning what is on screen into what comes next (section 5): a card shrinks and moves aside as the next one grows, a chip grows into a panel, an icon bursts into the next set of icons.
3. **Build, don't swap.** Lists, grids, timelines and charts grow one item per spoken word instead of appearing whole.
4. **Short travel.** Entrances move 24 to 80 px at most (never in from off-screen), always combining opacity 0 to 1, scale 0.92 to 1 and blur 6 px to 0.
5. **Durations:** big elements enter in 0.55 to 0.75 s, text and small items in 0.35 to 0.5 s. Exits take 0.3 to 0.4 s (opacity to 0, blur to 6 px, scale to 0.96). Nothing visible changes in under 0.25 s.
6. **Overlap.** The next element starts when the previous one is 30 to 50 % done. An exit always overlaps the next entrance by at least 0.15 s, so the frame is never empty.
7. **One or two fast things at a time.** Everything else holds still or drifts slowly. Never more than 2 elements in fast motion in the same 0.3 s.
8. **Nothing pops.** No element appears at full size in one frame, jumps position, or flashes. Colour changes (word fill, highlight) take at least 0.2 s.
9. **Stagger:** words 0.06 to 0.1 s, list items and grid cells 0.04 to 0.08 s, cards 0.12 to 0.18 s.
10. **Gentle life.** The stage drifts 12 to 24 px over a scene (power2.inOut), so the canvas is never fully frozen. Landed text stays dead still. No floating, breathing or pulsing loops.
11. **Motion blur:** `data-motion-blur="on"` for moves faster than about 800 px/s.
12. **Numbers:** count over 0.8 to 1.4 s (expo.out on the value) while a bar, ring or line grows with them. Land with a 1.03 to 1.0 settle.
13. **Rhythm:** something new every 1.5 to 3 s, never more than 3.5 s without a change. Scenes 2 to 6 s long.

## 5. Scene handovers (no full-frame transitions)

| Handover | How | When |
|---|---|---|
| **Morph** | The focal object reshapes into the next one (a chip widens into a panel, a card becomes a phone, a number becomes a chart's last point) in 0.5 to 0.7 s, power2.inOut | The next idea grows out of this one (the most common) |
| **Carry** | The focal object shrinks to 0.6 to 0.7 and moves aside (or up), staying on screen, while the next object grows in beside it | Cause and effect, before and after, "and then" |
| **Build-on** | Nothing leaves: new items, rows, branches or connectors are added to the current visual | Lists, steps, growth, "and also" |
| **Soft crossfade** | The old visual fades to 0 with 6 px blur and scale 0.96 over 0.4 s while the new one fades in from scale 0.94 over 0.5 s, overlapping 0.2 s. Only inside the visuals zone | A new topic with nothing to morph from |

The old tile wipe, whip and card zoom-through are retired: they moved the whole frame at once and made the test video feel jumpy.

## 6. Sound

The full sound rules live in the **serpforge-sound** skill (`.claude/skills/serpforge-sound/SKILL.md`). It is used automatically in every video (CLAUDE.md steps 5 and 9). Summary:

- **Six approved premium effects only** (`library/sfx/premium/approved/`, approved by ear 2026-11-17): whoosh, riser, sub-drop, pop/blip, click/tap, camera shutter. Real recordings, cleaned to be smooth (soft start, no harsh highs, long natural tail). Nothing synthesised, nothing random.
- **Use only where the picture needs it:** whoosh on handovers, riser into a key reveal (ending on it), sub-drop for weight (big claim, stat, problem, logo), pops for things appearing, clicks for UI interactions, shutter for capturing proof. Not every type in every video.
- **Restraint:** at most 2 risers, 3 sub-drops and 2 shutters per video; never two strong sounds within 0.15 s; at least 1.5 s of air in every 10 s; 0.6 to 1.8 effects per second.

| Type | Level (peak) | Aligned to |
|---|---|---|
| Whoosh | -22 dB | its peak on the fastest frame |
| Riser | -24 dB | its end on the reveal frame |
| Sub-drop | -18 dB | its onset |
| Pop / blip | -24 dB | its onset |
| Click / tap | -26 dB (typing -30 dB) | its onset |
| Shutter | -22 dB | its onset |

- **Voice first:** effects are noticed but never disturb the voice-over. Under a spoken word an effect is lowered 5 dB, its 2.5 kHz speech band is carved out, and it stays at least 10 dB below the voice in the speech band; it still sits at least level with the music (3 dB above it in pauses). When an effect is too quiet the music dips briefly to make room; the voice is never lowered. Important effects go in the pauses between phrases.
- **Voice:** -16 LUFS on its own, always the loudest thing.
- **Music: none by default.** The soundtrack is the voice-over plus the premium effects only (decided 2026-11-17: music made the voice less clear). Only if music is requested for a specific video: a soft ambient pad with no drums, vocals or lead melody, about 24 dB under the voice (-32 LUFS in pauses, ducked 10 dB more under speech, speech band cut out), as the serpforge-sound skill describes.
- **Master:** -14 LUFS integrated (stereo, as delivered), true peak at most -1 dBTP. Built by the skill's mixer (`scripts/mix.py`), checked with earshot critique.

## 7. Transcription zone

Premium, light and readable, like references 4 and 5. Same fonts (Outfit + Playfair Display), lighter weights.

- **What:** the exact words spoken in the scene (from `02_audio/transcript.json`), never paraphrased. No bottom subtitle pill.
- **Where:** the transcription zone, y 240 to 495, centred, `text-align: center`, text column x 192 to 888 (696 px).
- **Type:** every word is **white** `#FFFFFF` (19.4:1 on the background). Normal words Outfit **400**; highlighted key words **bold**, Outfit **700**. The italic accent is the one exception (style 2 below keeps its gradient). Size: **76 px for up to 2 lines, 64 px for 3 lines**, line height 1.12, tracking -1 %. Never more than 3 lines.
- **Shadow (subtle):** `text-shadow: 0 2px 10px rgba(0,0,0,.45), 0 1px 2px rgba(0,0,0,.35)`. It lifts the words off the grid and glow without a visible halo.
- **Key words:** 1 to 3 words per scene, in **one** of these styles per scene (vary them across the video):
  1. **Bold:** the key word is set in Outfit 700, white, like the rest of the line but bold. It appears bold from its first frame (no weight animation).
  2. **Italic accent (unchanged):** the word or short phrase in Playfair Display Italic with the mint-to-peach gradient (`--g-italic`).
  3. **Selection frame:** a thin 1.5 px orange (`--c-orange`) rectangle with four 7 px square corner handles around the key word or phrase, like a design-tool selection (from Ref 5). It draws on in 0.3 s after the word is spoken; the word itself is bold (Outfit 700), white.
  4. **Highlight box (rare):** a 12 px-radius orange box at 18 % behind the bold white word, wiping in left to right in 0.3 s.
- **Reveal (subtle):** each word fades in on its spoken start time: opacity 0 to 1, blur 4 px to 0 and y 10 px to 0 over 0.35 s (power3.out). No mask jumps. The previous phrase fades and blurs out over 0.3 s while the first new word arrives (overlap 0.1 s). Frame 0's hook phrase is fully on screen (thumbnail).

## 8. Watermark

- **What:** the text **serpforge.io** (not the logo).
- **Where:** the watermark zone, centred on x = 540, vertical centre y = 1687 px.
- **Type:** Outfit 600, 30 px, letter spacing +4 %, white at **30 % opacity** (low, subtle, still readable).
- On every frame, no animation, above the background. Nothing else in its zone.
- Note: on TikTok and Reels the app's own caption and username can sit over this area.

## 9. Do and do not

1. **Do** have the hook fully on screen at frame 0 (it is the thumbnail): a bold line or a number. No intro, no logo first. The other elements build in around it.
2. **Do** reveal the transcription word by word in time with the voice: white, regular weight, 1 to 3 key words in bold or one key-word style (section 7).
3. **Do** use real-looking UI (reports, dashboards, search results, chat) instead of abstract shapes.
4. **Do** make every number move: count, grow a bar, draw a line.
5. **Do** use colour for meaning: orange = action or attention, green = good, red = bad, amber = labels.
6. **Do** keep motion smooth: one canvas, objects become objects, short soft moves, overlapping exits (section 4). **Don't** use full-frame wipes, whips or zooms.
7. **Do** keep each thing in its zone: spoken words in the transcription zone, visuals on the colour drop, "serpforge.io" in the watermark zone. **Don't** add a bottom subtitle pill or a logo watermark.
8. **Don't** use random circles, lines, blobs or "floating" decoration. The grid and glow are the only texture.
9. **Don't** repeat a visual format in two scenes in a row, or use more than 4 elements and one focal point on screen (section 10).
10. **Don't** copy the reference videos' words, products, numbers, logos or colours. Take techniques only.

## 10. Visual formats (variety in every video)

Every scene picks one format from this library and names it in the visual script. Shown in our colours and fonts, never copied.

| # | Format | What it looks like | Good for |
|---|---|---|---|
| F1 | **Hero object** | One large icon, logo mark or product tile with a soft glow, maybe a gentle tilt | A name, a reveal, "it's called…" |
| F2 | **Stamp** | A big rotated value in a rounded outlined stamp ("FREE", "$0", "2x") that lands and settles | Price, a bold claim |
| F3 | **Big counter** | A huge number counting up with a spark line, ring or bar growing with it | Stats, growth, results |
| F4 | **Icon constellation** | Many small icons around a centre object or number, bursting out or gathering in | "10 ideas", many tools, abundance |
| F5 | **Terminal / command** | A terminal or input box where a command types in, then a success pill | Setup, "one command", how it works |
| F6 | **Real UI card** | A realistic card: search result, report, repo, chat answer, feed post | Proof, "this is what you get" |
| F7 | **Chart** | Line or curve with points, bar chart, or a staircase drop, drawing on | Change over time, a problem, a win |
| F8 | **Flow / network** | One node branching to several cards with connectors drawing out | "It connects to…", workflows, distribution |
| F9 | **Before / after** | Two cards side by side with ≠ or ✗ / ✓ and a checklist of differences | Comparisons, "not this, but this" |
| F10 | **Timeline / tracks** | Editor-style rows or a timeline filling one track per spoken word | Steps over time, building something |
| F11 | **Grid of many** | A grid of small tiles filling cell by cell (e.g. 100 tiles) | Scale, "100 variants", volume |
| F12 | **Steps with progress pills** | "01 · Setup" pills with the active one filled, plus a short checklist | Multi-step explainers |
| F13 | **Phone / app mockup** | A phone or app frame with the product working inside | Mobile, social, real usage |
| F14 | **People / audience** | Rows of person icons, one highlighted, or a crowd forming | Customers, buyers, "nobody" / "everybody" |
| F15 | **Orbit / cycle** | Icons orbiting a centre number or logo on a circular path | Loops, ecosystems, "every step" |
| F16 | **Receipt / pricing** | A receipt or price card with a total and a green check | Cost, value, "free" |
| F17 | **Comment / CTA card** | A comment box or button with the keyword stamped big above it | The call to action |

**Variety rules:**
- Never the same format in two scenes in a row.
- A video uses at least **5 different formats** (or one per scene when it has fewer than 5 scenes).
- Change the composition too: centred hero, two side by side, a stack, a grid, a diagram. Not every scene is a single card.
- Pick the format that shows the spoken idea literally (a number → F3, a comparison → F9, a cost → F16).
