# VISUAL SCRIPT: Test run

- Audio: `02_audio/final.mp3`, 16.77 s (0:00.0 to 0:16.8). Word times: `02_audio/transcript.json`.
- Style: `brand/STYLE-SHEET.md` v2 (locked) and `brand/tokens.css`. 1080 x 1920, 30 fps.
- On every frame: the grid background, one teal glow behind the focal point, the watermark (white logo, 120 px, 18 %, top-left x 120 / y 250, never animated) and the subtitle band (y 1268). No other element enters y 1250 to 1380.
- Text zone: x 120 to 888 and y 288 to 1248, left-aligned. Below y 840, text stays left of x 780.
- Easing names: OUT = expo.out, BACK = back.out(1.4), IN = power3.in, INOUT = power2.inOut.
- Sound levels: whoosh -18 dB, pop -22 dB, tick -24 dB, ding -18 dB, impact -16 dB, click -20 dB, logo chime -16 dB. Voice -16 LUFS, music bed -30 LUFS, ducked a further 9 dB under the voice, master -14 LUFS.
- Music for the whole film: one modern lo-fi/tech bed, no vocals, soft beat, about 90 to 100 BPM. Source to be chosen (`library/music` is empty).

---

## s01-hook   (0:00.0 to 0:03.8)
AUDIO: "Your buyers ask AI for a shortlist."
ON SCREEN: Dark grid ground, teal glow centred at y 1000. Label top-left. Title in the upper third. Below it, an AI chat card (x 96 to 816, y 700 to 1220): a question bubble at the top, then an answer area with 3 shortlist rows (rank tile 1/2/3 + a grey name bar + a small "Agency" chip). No real brand names in the rows.
TEXT: label "AI SEARCH" (Outfit 600, 30 px, amber, +12 % tracking); title "Your buyers ask AI" / "for a *shortlist.*" (Outfit 700, 104 px, white; "shortlist." in Playfair Display Italic 500, 112 px, mint-to-peach gradient); chat bubble "Best SEO agency for SaaS?" (Outfit 400, 38 px, white); rows "Agency" chips (Outfit 400, 30 px, mist).
ANIMATION:
- 0:00.0: label and title are fully on screen (frame 0 is the thumbnail). They stay dead still.
- Chat card: rises y +60 to 0, scale 0.94 to 1, blur 8 to 0 px, 0.5 s OUT, starting 0:00.6 so it lands at 0:01.0 on "ask" (0.99).
- Question bubble: types in letter by letter from 0:01.0 to 0:01.5 (linear, it is typing), with a blinking-free cursor that disappears at 0:01.55.
- Shortlist rows 1, 2, 3: slide in from x -90 with -6° rotation to 0, 0.45 s BACK, staggered 0.06 s, row 1 landing on "shortlist" at 0:01.89 (rows land 1.89 / 1.95 / 2.01).
- "shortlist." gradient: a soft shine (gradient position sweeps left to right) once, 0:01.9 to 0:02.4, OUT.
- Camera: the whole stage drifts y 0 to -16 px over the scene, INOUT.
TRANSITION OUT: Blur swap, 0.2 s out / 0.25 s in, at 0:03.8. Only the title swaps. The chat card stays and carries into s02 (same position).
EFFECTS: Teal glow behind the card (radial, 1300 px). Card shadow `--shadow-card`. Light 6 px motion blur on the sliding rows.
SFX:
- 0:01.00: soft keyboard typing bed for 0.5 s under the bubble, -28 dB.
- 0:01.89: bubble pop (row 1 lands), -22 dB. 0:01.95 and 0:02.01: two softer pops, -26 dB.
- 0:03.70: soft air whoosh into the blur swap, peaking at 0:03.8, -18 dB.
MUSIC: The bed starts at 0:00.0 at -30 LUFS, ducked -9 dB under the voice from 0:00.16.
SUBTITLES: "Your buyers ask AI" (0:00.16 to 0:01.49) / "for a *shortlist.*" (0:01.49 to 0:02.75)

## s02-question   (0:03.8 to 0:05.95)
AUDIO: "Is your brand on it?"
ON SCREEN: The same chat card from s01 (carried across). Under row 3, a 4th row appears: a dashed-border empty slot labelled "Your brand", with a red "Not listed" chip. Title above.
TEXT: title "Is your brand" / "*on it?*" (Outfit 700, 104 px, white; "on it?" in Playfair Display Italic 112 px gradient, with the orange highlight box behind "on"); slot "Your brand" (Outfit 600, 34 px, muted); chip "Not listed" (Outfit 500, 30 px, red #F8534D, red 1.5 px border).
ANIMATION:
- Title words blur in (blur 6 to 0 px, opacity 0 to 1, 0.13 s each, 0.067 s apart): "Is" 0:04.24, "your" 0:04.29, "brand" 0:04.71, "on it?" 0:05.24.
- Orange highlight box wipes in behind "on", left to right, 0.25 s OUT, starting 0:05.24.
- Card: shortlist rows 1 to 3 dim to 55 % opacity at 0:04.7 (0.3 s OUT), so the empty slot becomes the focal point.
- Empty "Your brand" slot: card list grows by one row, the slot fades and rises in (y +24 to 0, 0.4 s OUT) landing on "brand" at 0:04.71.
- "Not listed" chip: pops in, scale 0.6 to 1, 0.35 s BACK, landing on "on" at 0:05.24.
TRANSITION OUT: Tile wipe (signature), 0.5 s INOUT, from 0:05.70 to 0:06.20: 120 px rounded squares in logo teal #008181, mint #ABDCD6 and orange #F8981D sweep diagonally from bottom-left to top-right and reveal s03.
EFFECTS: A faint red glow (red at 10 %) behind the empty slot from 0:05.24. 8 px motion blur on the tile wipe.
SFX:
- 0:04.71: soft UI click as the empty slot appears, -22 dB.
- 0:05.24: low soft hit (problem moment) on "on", -16 dB.
- 0:05.70: whoosh for the tile wipe, peaking at 0:05.95, -18 dB.
MUSIC: Ducked under the voice. Under the tile wipe (0:05.7 to 0:06.1) the bed lifts +3 dB in the gap, then ducks again for "SERP Forge".
SUBTITLES: "Is your brand" (0:04.24 to 0:05.19) / "*on* it?" (0:05.24 to 0:05.61)

## s03-serp-forge   (0:05.95 to 0:08.45)
AUDIO: "SERP Forge gets SaaS brands found"
ON SCREEN: The white SERP Forge logo (native 410 px wide, never upscaled) top-left in the text zone. Under it, the title. In the lower half, a search-result card (x 96 to 816, y 820 to 1220) with a "SaaS brand" result row and a green "Found" status.
TEXT: logo `serpforge-logo-white.png`; title "gets SaaS brands" / "*found.*" (Outfit 700, 104 px; "found." italic gradient); card label "SEARCH VISIBILITY" (Outfit 600, 30 px, amber); result row "Your SaaS brand" (Outfit 600, 46 px, white) with "yourbrand.com" (Outfit 400, 32 px, sage); status chip "Found" with a green dot (Outfit 600, 30 px, green #31CD88).
ANIMATION:
- Logo: scale 0.9 to 1, blur 8 to 0 px, opacity 0 to 1, 0.5 s OUT, landing on "SERP" at 0:06.14 (starts 0:05.95 under the tile wipe).
- Title words mask-reveal (rise 45 % inside the word box, blur 6 to 0 px, 0.4 s OUT): "gets" 0:06.88, "SaaS" 0:07.23, "brands" 0:07.60, "found." 0:08.18.
- Search card: rises in (y +60 to 0, scale 0.94 to 1, 0.5 s OUT) from 0:07.10, landing on "SaaS" at 0:07.60.
- "Found" chip: green dot scales in (0.6 to 1, BACK), then the chip text appears, 0.35 s, landing on "found" at 0:08.18.
- Camera: stage drifts y 0 to -16 px, INOUT.
TRANSITION OUT: Whip, 0.25 s, at 0:08.45: the whole stage smears upward (12 px vertical motion blur) and s04 arrives from below, landing blurred and sharpening in 0.13 s.
EFFECTS: Teal glow behind the logo. A soft green glow (green at 12 %) behind the "Found" chip from 0:08.18.
SFX:
- 0:06.14: short warm logo chime on "SERP", -18 dB.
- 0:07.60: card pop, -22 dB.
- 0:08.18: bright ding on "found", -18 dB.
- 0:08.35: fast air whoosh for the whip, peaking at 0:08.45, -18 dB.
MUSIC: Ducked under the voice. No change.
SUBTITLES: "SERP Forge gets" (0:06.14 to 0:07.23) / "SaaS brands found" (0:07.23 to 0:08.20)

## s04-google-ai   (0:08.45 to 0:11.35)
AUDIO: "on Google and in AI answers."
ON SCREEN: Title at the top. Two cards stacked: card A "Google" (x 96 to 816, y 640 to 900): a search result in position #1. Card B "AI answer" (x 96 to 816, y 940 to 1220): an AI answer box with 2 grey text lines and a "Cited: Your brand" chip. Both cards show a "Your brand" row in white, with the other rows dimmed.
TEXT: title "On Google" / "*and* in AI answers." (Outfit 700, 104 px; "and" in an orange highlight box; "in AI answers." italic gradient, 2 lines if needed, 3 words per line max); card A label "GOOGLE SEARCH" (Outfit 600, 30 px, amber), rank tile "#1" (Outfit 700, 52 px, ink on orange), result "Your brand" (Outfit 600, 46 px); card B label "AI ANSWER" (Outfit 600, 30 px, amber), chip "Cited: Your brand" (Outfit 600, 30 px, ink on teal #1F9492).
ANIMATION:
- Title words blur in (0.13 s, 0.067 s apart): "On" 0:08.71, "Google" 0:08.85, "and" 0:09.52, "in AI answers." 0:09.97.
- Card A: rises in (y +60 to 0, 0.5 s OUT) landing on "Google" at 0:08.85. Its "#1" tile pops (scale 0.6 to 1, 0.35 s BACK) at 0:09.05.
- "and": the orange highlight box wipes in, 0.25 s OUT, on 0:09.52, with a 1.06 to 1.0 scale settle on the word (BACK).
- Card B: rises in (y +60 to 0, 0.5 s OUT) landing on "AI" at 0:10.05.
- Card B text lines draw left to right (0.4 s OUT) from 0:10.05. The "Cited: Your brand" chip pops in (scale 0.6 to 1, 0.35 s BACK) landing on "answers" at 0:10.26.
- Card A dims to 70 % opacity at 0:10.05, so card B becomes the focal point.
TRANSITION OUT: Card zoom-through, 0.5 s IN, from 0:11.10 to 0:11.60: card B scales up past the frame (to about 250 %), its dark card fill becomes s05's background, and s05's content fades in while it is still growing.
EFFECTS: Teal glow behind card B. 8 px blur on the zoom-through peak.
SFX:
- 0:08.85: card pop, -22 dB.
- 0:09.05: small tick for the "#1" tile, -24 dB.
- 0:09.52: low soft hit on "and", -16 dB.
- 0:10.05: card pop, -22 dB.
- 0:10.26: bright ding for the "Cited" chip, -18 dB.
- 0:11.10: whoosh into the zoom-through, peaking at 0:11.35, -18 dB.
MUSIC: Ducked under the voice. It lifts +3 dB in the gap 0:11.14 to 0:11.52.
SUBTITLES: "on Google *and*" (0:08.71 to 0:09.84) / "in AI answers." (0:09.97 to 0:11.14)

## s05-build   (0:11.35 to 0:13.55)
AUDIO: "Let's build your visibility."
ON SCREEN: Title at the top. Below it, a "Visibility" card (x 96 to 816, y 760 to 1220) with a 9-bar chart in grey bars where the last bars grow tall and green, plus an upward trend line. No numbers (no data shown).
TEXT: title "Let's build your" / "*visibility.*" (Outfit 700, 104 px; "visibility." italic gradient, 112 px); card label "AI + SEARCH VISIBILITY" (Outfit 600, 30 px, amber); note "▲ growing" (Outfit 500, 30 px, green).
ANIMATION:
- Title words mask-reveal (0.4 s OUT, rise 45 %, blur 6 to 0): "Let's" 0:11.52, "build" 0:11.77, "your" 0:12.18, "visibility." 0:12.52.
- Card: already filling the frame from the zoom-through, it settles to its final size (scale 1.04 to 1, 0.5 s OUT) by 0:11.85.
- Bars: grow from scaleY 0 to their heights, 0.5 s OUT, staggered 0.06 s, starting on "build" at 0:11.77. The last (green) bar lands on "visibility" at 0:12.52.
- Trend line: draws left to right (stroke dash), 0.7 s OUT, from 0:12.0 to 0:12.7.
- "▲ growing" note: fades in (y +16 to 0, 0.35 s OUT) at 0:12.6.
TRANSITION OUT: Blur swap, 0.2 s out / 0.25 s in, at 0:13.55. The ground does not cut.
EFFECTS: Soft green glow (green at 12 %) behind the last bar from 0:12.52. Camera drift y 0 to -16 px, INOUT.
SFX:
- 0:11.77: a quick tick roll under the growing bars, 0.75 s, -28 dB.
- 0:12.52: bright ding as the green bar lands on "visibility", -18 dB.
- 0:13.45: soft whoosh for the blur swap, peaking at 0:13.55, -18 dB.
MUSIC: Ducked under the voice. It lifts +3 dB in the gap 0:13.02 to 0:14.12.
SUBTITLES: "Let's build your *visibility.*" (0:11.52 to 0:13.02)

## s06-outro   (0:13.55 to 0:16.77)
AUDIO: "serpforge.io"
ON SCREEN: Logo outro. Teal glow behind, warm orange glow under the URL pill. The white logo (410 px, native size) at the top of the text zone. Under it, a short line, then the URL in an orange pill with the arrow badge.
TEXT: logo `serpforge-logo-white.png`; line "Get found by" / "*AI and Google.*" (Outfit 700, 96 px; second line italic gradient 104 px). This line is not spoken: it is on-screen copy, not a subtitle, and sums up s04. URL pill "serpforge.io" (Outfit 600, 44 px, ink #0A0E0D on orange #F8640A, arrow badge).
ANIMATION:
- Logo: scale 0.9 to 1, blur 8 to 0, opacity 0 to 1, 0.5 s OUT, from 0:13.6, landed by 0:14.1.
- Line: whole line blurs in (8 to 0 px, 0.2 s OUT) at 0:13.8.
- URL pill: pops in, scale 0.85 to 1, 0.45 s BACK, landing on "serpforge.io" at 0:14.12. The arrow badge slides in from x -12 to 0 at 0:14.4 (0.3 s OUT).
- Everything holds dead still from 0:14.6 to the end (0:16.77): the last line holds 2.2 s.
TRANSITION OUT: None. The film ends on the held logo frame (no fade to black).
EFFECTS: Warm orange glow under the pill (`--g-glow-orange`) fades up 0:14.12 to 0:14.6. Pill shadow `--shadow-cta`.
SFX:
- 0:13.60: short warm logo chime, -16 dB.
- 0:14.12: soft click as the URL pill lands, -20 dB.
MUSIC: Ducked under the URL, then from 0:16.42 the bed rises +3 dB and fades out over the last 0.35 s, ending exactly at 0:16.77.
SUBTITLES: "*serpforge.io*" (0:14.12 to 0:16.42)

---

## Checks

- Coverage: 0:00.0 to 0:16.77, no gaps (3.8 + 2.15 + 2.5 + 2.9 + 2.2 + 3.22 s). Every scene is 2 to 6 s.
- Something new on screen at least every 2 to 3 s (biggest gap: 0:14.6 to 0:16.77, the final hold).
- Transitions: 2 blur swaps, 1 tile wipe, 1 whip, 1 card zoom-through. Each has a whoosh.
- Every key reveal has a sound: shortlist, on, SERP, found, Google, and, AI answers, visibility, URL.
- Subtitle groups: 10. Key words (orange box): shortlist, on, and, visibility, serpforge.io.
- No real third-party logos. "Google" and "AI answer" appear as text labels only.
- Needs before Step 9: real sound effects (`library/sfx` is empty) and a music bed (`library/music` is empty).
