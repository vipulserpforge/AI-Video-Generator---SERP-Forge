# VISUAL SCRIPT: Test run v2

- Audio: `02_audio/final.mp3` (approved), 16.77 s. Word times: `02_audio/transcript.json`.
- Style: `brand/STYLE-SHEET.md` v6 (locked) and `brand/tokens.css`; sound: serpforge-sound skill (no music); assets: serpforge-visual-assets skill.
- Every frame: dark grid, the colour drop behind the visuals zone, the three zones (transcription y 240-495, visuals x 80-1000 / y 585-1510, watermark "serpforge.io" at 30 %), everything centred on x 540.
- Fonts: transcription and the s06 outro in Outfit (+ Playfair Display Italic accent); every text inside the visuals zone in Inter. Every box is a window card.
- Motion: one continuous canvas, no full-frame transitions; entrances 24-80 px with opacity + scale 0.92-1 + blur 6-0; exits overlap entrances; at most 2 fast things at once.
- Easing: OUT = expo.out, SOFT = power3.out, BACK = back.out(1.2) (chips only), EXIT = power2.in, INOUT = power2.inOut.

## ASSETS

| # | Asset | Type | Needed by (spoken word, time) | Scene | Source / file | Licence | Finishing |
|---|---|---|---|---|---|---|---|
| 1 | ChatGPT (OpenAI) mark | LOGO | "AI" 0:01.29 | s01, s04 | theSVG `openai` default -> `assets/logos/chatgpt.svg` | MIT | white mark on a deep tile |
| 2 | Google "G" (four-colour) | LOGO | "Google" 0:08.85 | s04 | theSVG `google` default -> `assets/logos/google.svg` | CC0 | on a white tile |
| 3 | Gemini star | LOGO | "AI answers" 0:10.05 | s04 | theSVG `gemini` default -> `assets/logos/gemini-alt.svg` | MIT | deep tile |
| 4 | Perplexity mark | LOGO | "AI answers" 0:10.05 | s04 | theSVG `perplexity` default -> `assets/logos/perplexity.svg` | CC0 | deep tile |
| 5 | Claude mark | LOGO | "AI answers" 0:10.05 | s04 | theSVG `claude` default -> `assets/logos/claude.svg` | CC0 | deep tile |
| 6 | SERP Forge logo | LOGO | "SERP Forge" 0:06.14, URL 0:14.12 | s06 | `brand/logos/serpforge-logo-white.png` | own | native size |
| 7 | serpforge.io homepage hero | IMAGE | "SERP Forge" 0:06.14 | s03 | user's own screenshot `brand/screenshots/brand visuals-1.png` -> `assets/images/serpforge-home.png` | own site | image.py look screenshot, 1720x900, browser window "serpforge.io", 3 % push-in |
| 8 | sparkle | ICON | "ask AI" 0:00.99 | s01 | phosphor `sparkle` duotone, amber | MIT | in the prompt row |
| 9 | list-numbers | ICON | "shortlist" 0:01.89 | s01 | phosphor `list-numbers` duotone, mint | MIT | answer header |
| 10 | warning | ICON | "on it?" 0:05.24 | s02 | phosphor `warning` fill, red | MIT | in the stamp |
| 11 | seal-check | ICON | "found" 0:08.18 | s03 | phosphor `seal-check` fill, green | MIT | "Found" chip |
| 12 | ranking | ICON | "Google" 0:09.05 | s04 | phosphor `ranking` duotone, white + orange | MIT | "#1" chip |
| 13 | check-circle | ICON | "answers" 0:10.26 | s04 | phosphor `check-circle` fill, green | MIT | "cited" ticks |
| 14 | browser | ICON | "brand" 0:08.55 | s04 | phosphor `browser` duotone, mint | MIT | the hub card |
| 15 | trend-up | ICON | "visibility" 0:12.52 | s05 | phosphor `trend-up` bold, green | MIT | chart header, "growing" chip |
| 16 | cursor-click | ICON | "serpforge.io" 0:14.12 | s06 | phosphor `cursor-click` duotone, orange | MIT | CTA badge |
| 17 | magnifying-glass | ICON | "ask" 0:00.99 | s01 | phosphor `magnifying-glass` duotone | MIT | prompt row |

Formats used: F6, F2, F6, F8, F7, F17 (5 different, never the same twice in a row). Key-word styles: bold, selection frame, italic accent, highlight box, bold, italic accent.

---

## s01-ask-ai   (0:00.0 to 0:03.8)
AUDIO: "Your buyers ask AI for a shortlist."
TRANSCRIPTION ZONE: "Your buyers ask AI / for a *shortlist.*" (white Outfit 400, 76 px, 2 lines; "shortlist." bold). On screen from frame 0.
FORMAT: F6 Real UI card
VISUALS ZONE: one window card "chatgpt" (860 px wide, centred). Body: a header row (ChatGPT logo tile + "ChatGPT"), a prompt row (search icon + the question + sparkle), then the answer: "Here's a shortlist" with the list-numbers icon and three ranked rows.
- LOGO: ChatGPT (theSVG openai, white on deep tile) - header row
- ICON: phosphor magnifying-glass duotone (mint) + sparkle duotone (amber) - prompt row
- ICON: phosphor list-numbers duotone (mint) - answer header
TEXT: "ChatGPT" (Inter 600 46 px), "Best SEO agency for SaaS?" (Inter 400 42 px), "Here's a shortlist" (Inter 500 34 px, mist), rows "Agency A / B / C" (Inter 500 38 px) with rank tiles 1-3 (Inter 700). Window title "chatgpt" (Inter 500 24 px).
ANIMATION: window rises 40 px + scale 0.94-1 + blur 8-0, 0.6 s OUT, landing on "ask" 0:00.99. The question types in 0:01.00-1.50. Answer header fades up 0:01.55 (0.4 s SOFT). Rows build in one by one (fade + y 24 + scale 0.96, 0.45 s SOFT) on "shortlist" 0:01.89 / 1.97 / 2.05. Stage drifts up 16 px over the scene (INOUT).
HANDOVER OUT: carry - the transcription fades 0:03.50-3.80; the window shrinks to 0.6 and moves up 235 px (0.6 s INOUT, 0:03.80-4.40) and stays as context in s02.
EFFECTS: colour drop; soft window shadow.
SFX: click (typing) 0:01.00 -30 dB · pop 0:01.89 -24 dB (rows land) · whoosh peak 0:04.00 -22 dB (carry)
MUSIC: none

## s02-not-listed   (0:03.8 to 0:05.95)
AUDIO: "Is your brand on it?"
TRANSCRIPTION ZONE: "Is your brand / *on it?*" (white Outfit 400, 76 px; "on it?" bold in an orange selection frame)
FORMAT: F2 Stamp
VISUALS ZONE: the carried, smaller chatgpt window (0.6 scale) at the top of the zone; below it a dashed "Your brand" row that appears empty; then a large rotated stamp "NOT LISTED" in red with the warning icon, landing over the lower half.
- ICON: phosphor warning fill (red) - inside the stamp
TEXT: "Your brand" (Inter 600 44 px, sage) with "?" tile; stamp "NOT LISTED" (Inter 800 96 px, red, +4 % tracking).
ANIMATION: words fade in on their times (Is 0:04.24, your 4.29, brand 4.71, on it? 5.24); the selection frame draws on 0:05.24 (0.3 s). The "Your brand" row fades + rises 24 px on "brand" 0:04.71 (0.45 s SOFT). The stamp lands on "on" 0:05.24: scale 1.25-1, rotation -12 to -6 deg, opacity 0-1, blur 6-0, 0.5 s OUT (no bounce). The carried window dims to 70 % at 0:05.24.
HANDOVER OUT: soft crossfade 0:05.70-6.10 (out: opacity 0, blur 6, scale 0.96 in 0.4 s; s03 in from scale 0.94 over 0.5 s).
EFFECTS: faint red glow behind the stamp.
SFX: pop 0:04.71 -24 dB (row) · sub-drop 0:05.24 -18 dB (stamp) · whoosh peak 0:05.95 -22 dB (crossfade)
MUSIC: none

## s03-serp-forge   (0:05.95 to 0:08.70)
AUDIO: "SERP Forge gets SaaS brands found"
TRANSCRIPTION ZONE: "SERP Forge gets / SaaS brands / *found.*" (white Outfit 400, 64 px, 3 lines; "found." Playfair italic gradient accent)
FORMAT: F6 Real UI (real image)
VISUALS ZONE: a browser window card titled "serpforge.io" filling the zone width, showing the real SERP Forge homepage hero (the user's own screenshot). Below it, a "search" window with the serpforge.io result (logo, domain, title "SERP Forge: SEO and AI visibility for SaaS") builds in on "SaaS" 0:07.23, and a green "Found" chip with the seal-check icon lands in it.
- IMAGE: serpforge.io homepage hero, user's own screenshot, image.py look screenshot, 3 % push-in over the scene
- ICON: phosphor seal-check fill (green) - "Found" chip
TEXT: window title "serpforge.io" (Inter 500 24 px); chip "Found" (Inter 600 32 px, green).
ANIMATION: words fade in (SERP 6.14, Forge 6.48, gets 6.88, SaaS 7.23, brands 7.60, found. 8.18). The browser window fades + rises 40 px + scale 0.94-1, 0.65 s OUT, landing on "SERP" 0:06.14; the screenshot inside pushes in 1.00-1.03 over the scene (INOUT). The "Found" chip pops (scale 0.9-1 BACK, 0.35 s) on "found" 0:08.18.
HANDOVER OUT: carry 0:08.45-8.70 - both windows shrink to 0.6 and fade as the s04 hub (which keeps the "Found" chip) grows in their place.
EFFECTS: colour drop; soft green glow at the chip.
SFX: shutter 0:06.14 -22 dB (the real page is shown) · pop 0:08.18 -30 dB (Found; lowered by the voice-first check) · whoosh peak 0:08.60 -22 dB (carry)
MUSIC: none

## s04-google-and-ai   (0:08.70 to 0:11.35)
AUDIO: "on Google and in AI answers."
TRANSCRIPTION ZONE: "On Google *and* / in AI answers." (white Outfit 400, 76 px; "and" bold on an orange highlight box)
FORMAT: F8 Flow / network
VISUALS ZONE: a small hub card in the middle ("Your brand" + browser icon + the green "Found" chip carried from s03). A connector draws up to a "google search" window (Google logo + "Your brand" + "#1" ranking chip); a second connector draws down to an "ai answers" window holding four logo tiles in a row (ChatGPT, Gemini, Perplexity, Claude), each with a green "cited" tick.
- LOGO: Google (white tile), ChatGPT, Gemini, Perplexity, Claude (deep tiles)
- ICON: phosphor browser duotone (hub), ranking duotone (#1 chip), check-circle fill (ticks)
TEXT: "Your brand" (Inter 600 40 px); window titles "google search", "ai answers"; chip "#1" (Inter 700 32 px); "cited" (Inter 500 26 px, green).
ANIMATION: hub grows in (scale 0.6-1, 0.6 s INOUT, 0:08.70-9.30). Connector up draws 0:08.75-9.15 (SOFT); Google window lands on "Google" 0:08.85 (0.55 s OUT); "#1" chip pops 0:09.05 (BACK). Highlight box on "and" 0:09.52. Connector down draws 0:09.70-10.10; the AI window lands on "AI" 0:10.05; logo tiles build in 0:10.05 + 0.07 s each; ticks pop on "answers" 0:10.26 + 0.06 s each.
HANDOVER OUT: soft crossfade 0:11.10-11.35 out, s05 in 0:11.35-11.95.
EFFECTS: connectors in mint at 40 %, a soft glow on the hub.
SFX: pop 0:08.85 -24 dB (Google) · pop 0:10.05 -24 dB (AI row) · whoosh peak 0:11.35 -22 dB (crossfade)
MUSIC: none

## s05-visibility   (0:11.35 to 0:13.55)
AUDIO: "Let's build your visibility."
TRANSCRIPTION ZONE: "Let's build your / *visibility.*" (white Outfit 400, 76 px; "visibility." bold)
FORMAT: F7 Chart
VISUALS ZONE: an "analytics" window: header (trend-up icon + "AI + SEARCH VISIBILITY" + a "growing" chip), a smooth line chart with a soft green area under it, light gridlines and weekly ticks, the end point glowing.
- ICON: phosphor trend-up bold (green) - header and chip
TEXT: "AI + SEARCH VISIBILITY" (Inter 600 30 px, amber, +10 %), "growing" (Inter 500 28 px, green), axis ticks "W1 ... W8" (Inter 400 22 px, sage). No made-up numbers.
ANIMATION: window fades + rises (0.6 s OUT) landing on "build" 0:11.77. Gridlines fade 0:11.80. The line draws 0:11.80-12.52 (INOUT), ending on "visibility" 0:12.52 where the end dot pops (scale 0.6-1, 0.35 s) and the area fades up (0.4 s). Chip fades in 0:12.60.
HANDOVER OUT: soft crossfade 0:13.35-13.75.
EFFECTS: green glow at the end point.
SFX: riser ending 0:12.52 -24 dB (builds into "visibility") · whoosh peak 0:13.55 -22 dB (crossfade)
MUSIC: none

## s06-outro   (0:13.55 to 0:16.24)
AUDIO: "serpforge.io"
TRANSCRIPTION ZONE: "*serpforge.io*" (Playfair italic gradient, 84 px)
FORMAT: F17 CTA
VISUALS ZONE: the SERP Forge logo (native size), the line "Get found by / *AI and Google.*" (Outfit 700 64 px + Playfair italic) and the orange "serpforge.io" pill with the cursor-click icon. Outro scene: Outfit, not Inter.
- LOGO: SERP Forge white (brand/logos)
- ICON: phosphor cursor-click duotone (orange) - pill badge
ANIMATION: crossfades in 0:13.55; logo 0:13.60 (0.5 s OUT); line 0:13.80; the pill lands on "serpforge.io" 0:14.12 (scale 0.92-1, 0.5 s OUT); badge 0:14.40; the cursor clicks the pill at 0:14.60 (badge dips to 0.84, pill to 0.97, springs back by 0:14.95). Holds still to the end. (Voice: "serpforge.io" sped up 1.45x, pitch kept, now 0:14.0-15.68.)
HANDOVER OUT: none (ends on the held frame).
EFFECTS: warm orange glow under the pill.
SFX: sub-drop 0:14.12 -18 dB (URL / logo lands) · click 0:14.60 -26 dB (cursor presses the pill)
MUSIC: none
