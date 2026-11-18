# Video studio rules (follow these for every video, every time)

## Video format
- Resolution: 1080 x 1920 px (Full HD)
- Aspect ratio: 9:16 vertical
- Frame rate: 30 fps
- File format: MP4 (H.264 video, AAC audio)
- Three fixed frame zones on every video (brand/STYLE-SHEET.md sections 3, 7 and 8). Each zone holds only its own content:
  - Transcription zone (top, y 240 to 495): the exact spoken words of the scene, typed in letter by letter like live typing, in time with the voice, with a thin orange caret (brand/STYLE-SHEET.md section 7). No bottom subtitle pill.
  - Visuals zone (middle, x 80 to 1000, y 585 to 1510): an invisible area (no box) where every visual, animation and UI element appears and fills 85 to 100% of it (never small in empty space), lit from behind by the colour drop (a soft radial teal-green light that fades into the background, like the website hero).
  - Watermark zone (bottom, y 1656 to 1718): the text "serpforge.io", white at 30% opacity, no animation, on every frame. Not the logo.
- Layout is center-aligned: everything sits on the frame's vertical centre line (x = 540 px).

## Voice
- Tool: the ElevenLabs connector (already connected). If it is not available, stop and tell me.
- Voice: a free ElevenLabs library voice, young Indian male, conversational tone.
- Voice name: Rocky-entrepreneur
- Voice ID: 8NdlidUZHOB6WALorwRR
- If the name and ID above are still placeholders: on the first audio, list the library voices, pick the best young Indian male conversational voice, tell me its name and ID, and write them here in CLAUDE.md. From then on, always use that voice.
- Later we will clone our own voice, named SERP Forge Narrator, and replace the name and ID above.
- Model: eleven_v3
- Stability: Natural
- Always use exactly this voice. If it is not found, stop and tell me. Never pick another voice.

## Workflow, in this order, no skipping

STEP 1. Audio script
- I paste the audio script in the chat or attach it as a .md file, and ask for the audio.
- For a new video, copy videos/_template to videos/<YYYY-MM>-<name>.
- Save the script word for word as 01_audio-script/script.md. If no script was sent, ask for it. Never write one yourself.

STEP 2. Audio
- Generate the audio with the ElevenLabs connector, using the Voice settings above.
- Turn the delivery notes into eleven_v3 audio tags ([excited], [serious], [whispers]...), CAPITALS for stressed words, and "..." for pauses.
- Show me the audio in the chat so I can listen.

STEP 3. APPROVAL 1: audio
- STOP and wait. If I ask for changes, regenerate only what I mention and show me again.
- When I type APPROVED, save the approved audio as 02_audio/final.mp3. If you cannot download it from ElevenLabs, ask me to download it and attach it.

STEP 4. Timing
- Run npx hyperframes transcribe on 02_audio/final.mp3. Save 02_audio/transcript.json with the start and end time of every word.
- Split the audio into scenes at natural pauses (one idea per scene, 2 to 6 seconds each).

STEP 5. Visual script (write it yourself, automatically)
- Read brand/STYLE-SHEET.md and references/analysis/REFERENCE-ANALYSIS.md first. If either is empty, stop and tell me.
- Asset pass (automatic, before writing any scene; serpforge-visual-assets skill section 5): read 01_audio-script/script.md and 02_audio/transcript.json and find, word by word, everything that needs a real asset:
  - every brand, company, tool, platform, product, app or website named (Google, ChatGPT, Reddit, a client, serpforge.io...) -> a LOGO (official mark);
  - every concept, action, metric or idea that a visual shows (rank, growth, search, citation, cost, time, warning, success...) -> an ICON (library icon chosen for that exact meaning);
  - every real thing that can be shown as it really is (a website or page, a search result, a dashboard, a tool's UI, a report, a product, a place) -> an IMAGE (Chrome capture of the official page, the user's own screenshots, or a free-licence photo), with its source URL.
  Write the result as an ASSETS table at the top of 03_visual-script/visual-script.md (asset, type, the spoken word and timestamp that needs it, scene, source, licence, finishing). Every scene uses at least one real logo, icon or image from it; if the script names nothing real, use meaning icons and real-looking UI. Then use these exact assets in the scenes' ICON / LOGO / IMAGE lines.
- Write 03_visual-script/visual-script.md. The scenes must cover the whole audio, from 0:00 to the end, with no gaps.
- For every scene, use exactly this format:

  ## s01-<name>   (0:00.0 to 0:04.2)
  AUDIO: <the exact words spoken in this scene>
  TRANSCRIPTION ZONE: "<the same spoken words, as they appear in the top zone>" (white Outfit 400, 76 px for 2 lines or 64 px for 3; key words marked like *this* and their style named: bold, italic accent, selection frame or highlight box; reveal: typing, each word typed from its start to its end time)
  FORMAT: <one format from the style sheet's visual format library, e.g. F9 Before / after>
  VISUALS ZONE: <every element on the colour drop and how it is placed and composed; then one line per real asset (serpforge-visual-assets skill): ICON: <library name, weight, colours>, LOGO: <brand, source, variant>, IMAGE: <what, source URL or Chrome capture, finishing look>>
  TEXT: "<any other on-screen words inside the visuals zone>" (Inter, size from the style sheet; the outro scene uses Outfit)
  ANIMATION: <for each element: how it enters, moves and leaves, the easing, and the word and timestamp it lands on>
  HANDOVER OUT: <morph, carry, build-on or soft crossfade, what becomes what, and the duration>
  EFFECTS: <camera drift, glow, blur, highlights, masks>
  SFX: <from the serpforge-sound skill only: each effect type (whoosh, riser, sub-drop, pop, click, shutter), its timestamp, alignment and level, and why>
  MUSIC: none (house default: no background music; only if I ask for music on this video, follow the serpforge-sound skill's near-silent ambient rules)

- Something new happens on screen every 1.5 to 3 seconds. Every handover gets a soft sound. Every key reveal gets a sound.
- Visual assets: always load and follow the serpforge-visual-assets skill (.claude/skills/serpforge-visual-assets). Real official logos only (never redrawn), meaningful icons from the local Phosphor/Lucide libraries (never letters, numbers or emoji standing in for icons), and real images or Chrome screenshots, lightly finished, wherever the script names something real. Every image source is listed in the visual script; APPROVAL 2 covers fetching exactly those.
- Sound design: always load and follow the serpforge-sound skill (.claude/skills/serpforge-sound). Use only its six approved effects, its rulebook (when, how often, priorities, air) and its levels. Not every effect is used in every video: only where it supports the picture.
- Clicks and typing sounds (serpforge-sound section 2a): every visible click in the visuals zone (cursor, button, CTA pill, toggle, tab) gets a click sound on the press frame, with the press shown in the picture; typing sounds (soft clicks every 2 to 3 characters) only when the visuals zone shows something being typed or filled in (search box, AI prompt, form, code, URL). Never on the subtitles.
- Voice first: sound effects must be noticed but never disturb the voice-over. Under a spoken word an effect stays at least 10 dB below the voice in the speech band and is softened; the music, never the voice, makes room. Put important effects in the small pauses between phrases (serpforge-sound section 4).
- Variety (style sheet section 10): never the same FORMAT in two scenes in a row; at least 5 different formats per video (one per scene if fewer than 5 scenes); vary the composition (hero, side by side, stack, grid, diagram) and the key-word style.
- Smoothness (style sheet section 4): one continuous canvas, objects become the next object, build instead of swap, short soft moves (24 to 80 px, opacity + scale + blur), overlapping exits, never more than 2 fast things at once. No full-frame wipes, whips or zooms.
- Every element is center-aligned and stays inside its zone. The watermark zone always shows "serpforge.io" and is not listed per scene.

STEP 6. APPROVAL 2: visual script
- STOP and show me the visual script, including its ASSETS table (every logo, icon and image with its source). If I ask for changes, update only those scenes and show me again. Continue only when I type APPROVED: that approval also allows fetching exactly the images in the ASSETS table.

STEP 7. Storyboard
- From the approved visual script, make a still frame of each scene with HyperFrames (npx hyperframes snapshot), in the real style, at 1080 x 1920.
- Before the stills: fetch and finish every ICON, LOGO and IMAGE listed in the approved visual script into 05_build/project/assets/ (serpforge-visual-assets skill) and record them in assets/SOURCES.md, so the stills show the real assets.
- Create 04_storyboard/storyboard.html and storyboard.pdf: one card per scene with the scene ID, start and end time, still frame (showing all 3 zones), words spoken, transcription-zone text, visuals-zone elements and text, animation, transition and sound effects. Timings must match the approved audio exactly.

STEP 8. APPROVAL 3: storyboard
- STOP and show me the storyboard. If I ask for changes, update the visual script and only those cards, then show me again. Continue only when I type APPROVED.

STEP 9. Final video
- Build every scene in 05_build with HyperFrames, exactly as the approved storyboard says. Use Remotion only if I ask.
- Use 02_audio/final.mp3 as the only voice track. Every animation and sound effect lands on its word from transcript.json (within 2 frames).
- Sound: follow the serpforge-sound skill. Write 05_build/audio/cues.json from the approved visual script and run its mixer (scripts/mix.py): the voice plus the approved premium effects, NO background music (unless I ask for it on this video), mastered to -14 LUFS. Fix every WARN it prints, then use mix.wav as the single soundtrack.
- Build the 3 zones: the transcription text, typed in letter by letter (each word starts typing on its start time from transcript.json, within 2 frames, and finishes by its end time, 0.025 to 0.06 s per letter, 2-frame soft fade per letter, one solid orange caret, fixed layout with no reflow; style sheet section 7), the colour drop behind the visuals, and the "serpforge.io" watermark on every frame.
- Write font names literally in CSS ("Outfit", "Playfair Display", "Inter"), and check a frame of the rendered MP4, not only snapshots.
- Before rendering: the serpforge-visual-assets human-made checklist on every scene, npx hyperframes lint (zero errors), the motionmaxxing checks, and earshot critique on the mixed audio. Fix every problem.
- After rendering: run references/analysis/tools/smooth.py on the MP4. Burstiness must be 60 % or less and there must be no single-frame pops; if not, soften the motion and render again.
- Render to 06_exports/<name>.mp4 in the Video format above, then tell me where the file is.

## Never
- Never render before all 3 approvals (audio, visual script, storyboard).
- Never reveal the transcription any other way than typing (no word fades, no wipes), and never put any sound (typing, click or other) on the subtitles: the subtitle typing is silent.
- Never add a bottom subtitle pill or any second line that repeats the voice: the spoken words appear only in the transcription zone.
- Never put anything in a zone that does not belong there, and never use the logo as the watermark.
- Never add background music unless I ask for it on that video.
- Never change the words of the audio script without asking me.
- Never delete files. Move old versions into an _old folder.

## Design (always follow brand/STYLE-SHEET.md and brand/tokens.css)
- Use only the style sheet's colours, fonts, motion and sound rules.
- Center-aligned layout: text and visuals on the vertical centre line. One focal point per frame. Rounded corners on everything.
- Every boxed visual is a window card (style sheet section 3): a title bar with the three window dots and a centred lowercase title, then the content. In the visual script, name each window's title (e.g. window "ai search").
- No abstract decorative shapes (random circles, lines, blobs). Use meaningful icons, UI, charts or diagrams.
- Real, premium assets (serpforge-visual-assets skill): official logos, one premium icon family (Phosphor duotone), real screenshots and images. The video must look made by a human designer, never AI-generated: no placeholders, no emoji, no generic glyphs, no look-alike logos.
- Text contrast at least 4.5:1 for body text, 3:1 for large titles.
- Smooth motion only (style sheet section 4): no linear movement, no element appears or jumps in one frame, elements land on the spoken word.
- Premium transcription type (style sheet section 7): white, regular weight, subtle shadow; key words bold (or the italic gradient accent, unchanged).
- Fonts: Inter for all text inside the visuals zone (cards, window titles, labels, chips, UI, numbers); Outfit + Playfair Display only for the transcription zone, the watermark and the logo outro scene.
