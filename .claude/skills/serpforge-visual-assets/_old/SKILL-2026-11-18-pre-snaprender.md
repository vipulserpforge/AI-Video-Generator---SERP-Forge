---
name: serpforge-visual-assets
description: SERP Forge's rules and tools for real, premium visual assets in every video - official brand logos (never redrawn), meaningful icons from free premium icon libraries (Phosphor duotone first, Lucide fallback) instead of generic glyphs, letters or emoji, and real images or website screenshots captured with Chrome and finished with light professional edits - so every video looks hand-made by a human designer, not AI-generated. Use it automatically in every SERP Forge video when writing the VISUALS ZONE of the visual script (CLAUDE.md step 5), when building stills and scenes (steps 7 and 9), and whenever the user asks for a logo, icon, image, screenshot or a more real / premium / less AI-looking visual.
---

# SERP Forge visual assets

**Goal:** every frame looks like a human designer made it for this exact video. Specific beats generic: the real logo, the icon that means this exact idea, the real screenshot of the real page. Never a placeholder, a letter in a box, an emoji or a look-alike.

Tools (offline, in this skill's `scripts/`, run from the project root):
```
node .claude/skills/serpforge-visual-assets/scripts/assets.mjs search <idea words>       # best icons for an idea
node .claude/skills/serpforge-visual-assets/scripts/assets.mjs icon <name> --out <svg> [--weight duotone] [--color #hex] [--accent #hex] [--lib lucide]
node .claude/skills/serpforge-visual-assets/scripts/assets.mjs brands <words>            # find a brand
node .claude/skills/serpforge-visual-assets/scripts/assets.mjs logo <brand> --out <svg> [--mono #fff]
npx hyperframes@0.9.56 media-use resolve --type logo --entity <brand> --intent "<brand> logo" --project <build> --json
~/.local/share/uv/tools/earshot/bin/python -I .claude/skills/serpforge-visual-assets/scripts/image.py <in> <out.png> --size 1720x1080 --look screenshot|photo
```
Libraries (installed in `library/icons/node_modules`, never fetched at render time): **Phosphor** 2.1 (MIT, 1,512 icons x 6 weights), **Lucide** (ISC, 2,401 icons), **Simple Icons** (CC0, 3,400+ brand marks with official colours).

## 1. Logos: always the real mark

1. **Our own logo:** `brand/logos/` (white on dark, colour on light). Never another version.
2. **Any other brand** (Google, ChatGPT/OpenAI, Claude, Perplexity, Reddit, a client, a tool), in this order:
   1. `npx hyperframes media-use resolve --type logo` (theSVG: official marks with light / dark / wordmark variants and a pinned licence). Pick the variant that reads on a dark background.
   2. `assets.mjs logo <brand>` (Simple Icons: official single-colour mark in the brand's own hex, or `--mono #FFFFFF`).
   3. Not in either, or the brand's real mark is multi-coloured and only a one-colour version came back (for example Google's four-colour "G"): open the brand's own brand/press page or Wikimedia Commons in **Chrome** and take the official SVG/PNG (see section 3 for capture and permission).
3. **Never** redraw, trace, recolour (except the brand's official mono variant), stretch, add effects to, or approximate a logo, and never type a brand name in a font to stand in for its logo.
4. **On dark backgrounds:** use the official light/white variant, or set the full-colour mark on a small white tile (radius 20 px, 16 px padding). Keep clear space of at least half the mark's height around it.
5. **Trademark care:** third-party logos only name the product or platform being talked about (nominative use). Never imply a partnership or endorsement, never put a third-party logo bigger than ours in the outro.
6. File the result in the build's `assets/logos/` and list it in `assets/SOURCES.md` (brand, source, variant, licence).

## 2. Icons: specific, premium, one family

- **Meaning first.** Search by the idea in the sentence, not by the shape: `assets.mjs search rank first winner` gives `ranking` (a medal), not a generic star. Pick the icon a designer would choose for that exact word.
- **Never generic stand-ins:** no letters, numbers or symbols in a box acting as an icon ("#1" in a square becomes a `ranking`/`trophy` icon with the number as a label beside it), no plain arrow when a specific action exists (visit a site = `globe`/`arrow-square-out`/`cursor-click`), no emoji, no clip-art, no hand-drawn SVG when a library icon exists.
- **One family per video:** Phosphor. Use Lucide only for an idea Phosphor does not cover, and then in a matching weight (`--lib lucide`, 1.75 stroke).
- **Style:**
  - **Duotone** for feature icons (`--weight duotone`): main colour mint `#ABDCD6` or white, the soft second tone from meaning colours via `--accent`: orange `#F8640A` action/attention, green `#31CD88` good/growth, red `#F8534D` problem/loss, amber `#E2A63D` labels.
  - **Fill** for tiny status icons in chips (16 to 28 px). **Regular/bold** only to match a UI that is line-based.
  - **Sizes:** 28 to 40 px inside chips and rows, 56 to 96 px in feature tiles, up to 220 px as a hero object.
  - **Icon tile:** 20 px radius, fill `#0D2421`, 1.5 px border mint at 15 %, the icon at 55 to 60 % of the tile.
- **Motion:** icons arrive with the element they belong to (fade + scale 0.92 to 1 + blur 6 to 0), never spin, bounce or pulse in a loop.

## 3. Real images and screenshots

When the voice-over names something real (a website, a tool or its UI, a search result, a dashboard, a product, a place), **show the real thing**, finished with light edits. Sources, in this order:
1. **The user's own material:** `brand/screenshots/`, their websites, their product. Prefer these.
2. **A live Chrome capture of the official page:** open it in Chrome (Claude in Chrome, or the built-in browser if Chrome is unavailable), set a 1440 x 900 or 390 x 844 (mobile) window, dismiss cookie banners with the most private choice, and screenshot only the relevant part. Never capture pages behind a login that show private data, and never capture personal information.
3. **Free-licence photos:** Unsplash or Pexels: read the licence on the photo's own page and record it. No people's faces unless the licence covers it and it fits.
4. **Official press kits** of the brand being discussed.

**Never:** random results from image search, watermarked stock, AI-generated images presented as real, images of private individuals, anything whose licence cannot be confirmed.

**Permission:** every image or capture is listed in the visual script with its source (`IMAGE:` lines, section 5). The user's APPROVAL 2 of the visual script covers fetching exactly those. Anything new found later is shown to the user (file, source, size) before downloading.

**Finishing (light, honest edits):** `image.py`: crop to the window's aspect around the focus point, Lanczos resize at 2x for sharpness, a touch of contrast and clarity; `--look photo` adds a gentle teal grade in the shadows and a soft vignette so it belongs to our palette. Never change what the image shows. Then present it inside a **window card** (title = the site's domain, for example `serpforge.io`) with a subtle 2 to 3 % push-in or a slow scroll for long pages. For deeper grades, use `npx hyperframes media-treatment` (never CSS filters on footage).

Record every image in `05_build/project/assets/SOURCES.md`: file, what it shows, source URL, licence, capture date, edits.

## 4. The human-made checklist (every scene)

- [ ] All text inside the visuals zone (cards, window titles, labels, chips, UI copy, numbers) is set in **Inter**; Outfit/Playfair only in the transcription zone and the logo outro.

- [ ] Real names, numbers and words from the script on screen; no lorem ipsum, and grey placeholder bars only where text would be unreadable anyway (keep them short and few).
- [ ] Every logo is the official mark; every icon comes from the library and means the exact idea.
- [ ] One icon family and one style per video; meaning colours used consistently.
- [ ] Real UI, real screenshots and real images where the script names something real.
- [ ] Small human details: a real domain in a browser bar, a cursor that clicks the thing being described, a realistic timestamp or count.
- [ ] No emoji, no clip-art, no generic stock-looking illustration, no symmetrical "AI art" decoration.

## 5. How it plugs into the workflow

### Asset discovery (automatic, every video, before the visual script is written)

Run this from the audio script and the transcript; never wait to be asked.
1. **Read** `01_audio-script/script.md` and `02_audio/transcript.json` (word timings).
2. **Logos:** mark every proper name of a brand, company, tool, platform, product, app or website (including domains like `serpforge.io` and generic-but-branded words like "Google", "ChatGPT", "Reddit", "LinkedIn"). Check each one: `assets.mjs brands <name>`, then `npx hyperframes media-use resolve --type logo` (section 1).
3. **Icons:** mark every concept, action, metric or feeling a visual will show (rank, growth, drop, search, citation, AI, cost, time, speed, warning, success, audience, content, link). For each, run `assets.mjs search <idea words>` and pick the icon that means that exact idea (section 2).
4. **Images:** mark every real thing that can be shown as it is: a website or landing page, a search result page, an AI answer, a dashboard or report, a tool's UI, a product, a place, a document. For each, choose the source (user's own > Chrome capture of the official page > free-licence photo > press kit) and note the URL and capture size (section 3).
5. **Write the ASSETS table** at the top of `03_visual-script/visual-script.md`:

   | # | Asset | Type | Needed by (spoken word, time) | Scene | Source / file | Licence | Finishing |
   |---|---|---|---|---|---|---|---|
   | 1 | Google "G" | LOGO | "Google" 0:08.85 | s04 | theSVG `google` default | CC0 | white tile |
   | 2 | ranking | ICON | "#1" 0:09.05 | s04 | phosphor `ranking` duotone | MIT | white + orange accent |
   | 3 | serpforge.io homepage | IMAGE | "serpforge.io" 0:14.12 | s06 | Chrome capture https://serpforge.io 1440x900 | own site | look screenshot, browser window "serpforge.io" |

6. **Use them:** every scene's `VISUALS ZONE` lists its `ICON:` / `LOGO:` / `IMAGE:` lines from this table, and every scene uses at least one real logo, icon or image. A scene that names nothing real still gets meaning icons and real-looking UI, never placeholders.
7. **Approval 2** shows the table to the user; their APPROVED covers fetching exactly the listed images. **Step 7** fetches and finishes everything into the build's `assets/` and fills `assets/SOURCES.md` before the storyboard stills.

### Visual script lines

- **Step 5 (visual script):** inside `VISUALS ZONE`, list every asset on its own line:
  - `ICON: phosphor ranking (duotone, mint, accent orange) - next to "Your brand"`
  - `LOGO: Google (theSVG default, on white tile) - window title bar`
  - `IMAGE: serpforge.io homepage hero, Chrome capture 1440x900, look screenshot - in a browser window "serpforge.io"`
- **Step 7 (storyboard):** fetch and finish the listed assets into the build's `assets/` (icons, logos, images) and fill `assets/SOURCES.md`, so the stills already show the real assets.
- **Step 9 (final video):** reuse those exact files; run the section 4 checklist before rendering.
