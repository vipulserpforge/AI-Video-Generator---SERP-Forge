---
name: serpforge-sound
description: SERP Forge's house sound design for every video - which of the six approved premium effects (whoosh, riser, sub-drop, pop/blip, click/tap, camera shutter) to use, when, how often and how loud, no background music by default, plus the reusable mixer that places the effects on the transcript and mixes them with the voice to -14 LUFS. Use it automatically in every SERP Forge video: when writing the SFX lines of a visual script (CLAUDE.md step 5) and when building the final soundtrack (step 9). Also use it when the user asks to add, change, fix, soften or review sound effects, music levels or the mix of a SERP Forge video.
---

# SERP Forge sound design

Goal: every video sounds as if a professional sound editor cut it. Effects **support** the picture and the voice; they never compete with them. Fewer, softer, perfectly timed sounds beat many loud ones. Silence is a tool.

The library is fixed and approved (2026-11-17). Never synthesise a sound, never pull a random one, never use an effect that is not listed here unless the user approves it first.

## 1. The approved library (`library/sfx/premium/approved/`)

All six are real recordings (Mixkit, uisfx), already cleaned to be smooth: start trimmed to the transient, rumble cut, harsh highs softened, soft fade-in, long natural fade-out.

| Type | File | Length | Character |
|---|---|---|---|
| Whoosh / swoosh | `whoosh.wav` | 0.75 s | Soft airy woosh |
| Riser / buildup | `riser.wav` | 1.9 s | Gentle cinematic swell that climbs to its end |
| Sub-drop / downer | `subdrop.wav` | 1.3 s | Deep, warm, knocking sub drop |
| Pop / blip | `pop.wav` | 0.28 s | Dry, soft pop |
| Click / tap | `click.wav` | 0.20 s | Soft interface tap |
| Camera shutter | `shutter.wav` | 0.60 s | Digital shutter |

Sources and the processing chain: `library/sfx/premium/make_premium.py` (re-creates the files exactly). Alternates and previews: `_alternates/`, `_previews/`. Licences: Mixkit Sound Effects Free License (commercial and social use, no credit needed, no redistribution as stand-alone sounds), uisfx CC0.

## 2. When to use each one (rulebook)

Pick sounds from what happens **on screen and in the voice**, never to fill time. Not every type is used in every video.

| Type | Use it for | Never | Max |
|---|---|---|---|
| **Whoosh** | A scene handover (morph, carry, soft crossfade); a big element crossing or growing fast; a camera move | On build-on handovers (use a pop/tick), on every small element, two whooshes within 1.5 s | 1 per handover, about 1 per 2 to 4 s |
| **Riser** | The build into a key reveal: the big number, the product name, the answer, the CTA. It ends **exactly** on the reveal frame, then a sub-drop or a pop lands there | Under a sentence that is not leading to a reveal; stacked risers; any riser that does not resolve | 1 per 20 s, at most 2 per video |
| **Sub-drop** | The weight of a big moment: a bold claim, a shocking stat, the problem ("Not listed"), the logo/brand reveal, the end of a riser | On small UI events, twice in a row, closer than 6 s to another sub-drop | About 1 per 15 s, at most 3 per video |
| **Pop / blip** | Elements appearing: cards, chips, badges, list items, icons, tiles, a key word's highlight | Machine-gun pops on every word; more than 3 in 1 s | As many as there are real appearances, thinned so they never feel busy |
| **Click / tap** | UI interactions in the visuals zone, **always**: a cursor click, a button or pill press, a toggle, selecting a row or tab, and **typing** in the visuals zone (section 2a) | As a generic "something moved" sound, and **never for the subtitles** (the transcription-zone typing is silent) | Matches the visible interactions |
| **Camera shutter** | Capturing proof: a screenshot, a result being "saved", a report or a frame freezing, a before/after snapshot | As a transition or a decoration | 1 or 2 per video |

### 2a. Clicks and typing (required whenever the picture shows them)

- **Click:** every visible click in the visuals zone gets one click sound: a cursor icon or pointer pressing a button, a CTA pill being pressed, a toggle, a tab or row being selected. Show the press in the picture too (the cursor or button dips to about 0.85 to 0.97 scale for 2 to 3 frames, then springs back) and put the click's onset on the press frame. Level -26 dB (the mixer softens it under a spoken word). The outro CTA pill with the cursor badge always gets its click.
- **Typing:** only when the visuals zone shows something being typed or filled in: a search box or AI prompt typing a query, a form field being filled, code or a command being typed, a URL being entered. Use soft clicks at -30 dB, one per 2 to 3 typed characters, slightly irregular (the mixer varies repeats), starting on the first typed character and stopping on the last. Never more than one typing run at a time.
- **Never on the subtitles:** the transcription zone types in letter by letter (STYLE-SHEET section 7) **silently**. No click, typing or any other sound is ever tied to subtitle letters or words; the voice carries them.
- In the visual script, write each one in the SFX line, e.g. `click 0:14.60 -26 dB (cursor presses the serpforge.io pill)` and `typing 0:01.00-0:01.50 clicks every 2-3 chars -30 dB (prompt typed in the chatgpt window)`.

**Priorities when moments collide:** voice > sub-drop > riser end > whoosh > pop > click > shutter. Keep the stronger one and drop or soften the weaker one.

## 3. Placement and sync

- Every effect lands on its picture event and, when there is one, its spoken word from `02_audio/transcript.json`, within 2 frames (66 ms).
- **Alignment:** pops, clicks, shutters and sub-drops align their **onset** to the event. Whooshes align their **peak** to the fastest frame of the move. Risers align their **end** to the reveal frame.
- Never two strong sounds (sub-drop, riser end, whoosh peak) within 0.15 s.
- Leave air: in every 10 s there is at least one 1.5 s stretch with no effect at all. Overall density 0.6 to 1.8 effects per second.
- Avoid stressed words: if an effect lands on a stressed or key spoken word, use the softer type or lower it 3 dB.
- Repeated sounds are varied automatically by the mixer (small level and pitch changes), so a run of pops never sounds copy-pasted.

## 4. Voice first: noticed, never in the way

The voice-over is the most important sound in every video. Effects must be **noticed** by the viewer but must **never cover, mask or distract from a word**. The mixer enforces this automatically for every effect; never turn these rules off.

1. **Under a spoken word,** an effect is lowered 5 dB and the 2.5 kHz speech-presence band is carved out of it (a 5 dB dip), so the words stay clear.
2. **Voice gap:** under speech, an effect always stays **at least 10 dB below the voice in the speech band (300 Hz to 4 kHz)**. The mixer targets 13 dB and never raises an effect past it.
3. **Noticed:** with no music (the default) every effect plays at its house level and is clearly heard in the pauses. If music is used on request, an effect's loudest 50 ms sits **at least 3 dB above the music** around it in a pause, and at least level with the music (within 1 dB) under speech, where it only has to be felt.
4. **Make room, don't shout:** when an effect would be too quiet, the mixer first raises it (at most +10 dB over its house level, never past the voice gap), then dips the music for that moment only (up to 4 dB in pauses, 6 dB under speech, smooth 40 ms edges). It never makes the voice quieter.
5. **Best placement:** put important effects (sub-drop, riser end, shutter, the key pop) in the small pauses between phrases, or on the first syllable of a word, not on top of a stressed word. If the mixer says an effect "can only reach" a level under a spoken word, either keep it subtle or move it to the nearest pause (within 2 frames of its picture event when possible).
6. **Final check:** `mix_report.json` lists, per effect, `below_voice_speechband_db` and `above_music_db`. Every effect must pass, then earshot critique must score every metric in range. Listen-check the riser and sub-drops against the voice before rendering.

## 5. Levels (house peak level, before the voice-first calibration and the master gain)

| Type | Level |
|---|---|
| Whoosh | -22 dB |
| Riser | -24 dB (it swells, so it reads louder than its peak) |
| Sub-drop | -18 dB |
| Pop / blip | -24 dB |
| Click / tap | -26 dB (typing -30 dB) |
| Shutter | -22 dB |

Voice -16 LUFS on its own, always the loudest thing. Master -14 LUFS integrated (as delivered, stereo), true peak at most -1 dBTP.

### Music: none by default

- **Default: no background music.** The soundtrack is the voice-over plus the premium effects only. Leave `music` out of `cues.json` and write `MUSIC: none` in the visual script. (Decided 2026-11-17: music made the voice less clear and less focused.)
- **Only when the user asks for music on a specific video,** use a near-silent bed that never competes with the voice:
  - **Track:** a soft, pleasant ambient pad with no drums, no vocals and no lead melody: under 1 note onset per second, a steady level (under 10 dB spread), checked with earshot (`dreamy`, `ambient pad`). Approved candidate: `library/music/mixkit/mixkit-324_smooth-meditation.mp3` (Mixkit Stock Music Free License: web and social OK, no TV/radio).
  - **Level:** -32 LUFS in pauses, ducked a further 10 dB while the voice speaks (80 ms attack, 300 ms release), -6 dB duck on the end card, so it sits about 24 dB under the voice. The mixer also cuts the speech band out of it permanently (around 900 Hz and 2.6 kHz). These are the mixer's defaults when a `music` block is given.

## 6. How to use it in the workflow

**Step 5 (visual script):** write each scene's `SFX:` line from this rulebook only, naming the type, the exact timestamp, the alignment and the level, for example:
`SFX: whoosh peak 0:03.80 -22 dB (handover) · pop 0:04.71 -24 dB (slot appears) · sub-drop 0:05.24 -18 dB ("on" / Not listed)`

**Step 9 (final video):**
1. Write `05_build/audio/cues.json` from the approved visual script (format: `cues.example.json` in this skill). No `music` block unless the user asked for music on this video.
2. Run the mixer from the video folder:
   `~/.local/share/uv/tools/earshot/bin/python -I .claude/skills/serpforge-sound/scripts/mix.py videos/<video>/05_build/audio/cues.json`
   (any Python with numpy + pyloudnorm works; the earshot tool's Python has both). It writes `mix.wav` (stereo, the soundtrack for HyperFrames), stems and `mix_report.json`, and prints warnings for rule breaks (voice gap, noticeability, gaps between strong sounds, density, missing air).
3. Fix every warning, then run `earshot critique` on `mix.wav` (with `--video` once the picture is rendered) against `references/analysis/earshot-profile.json`. Every scored metric in range, **except the music-related ones** (music presence, and onset density when it is low only because there is no music): the reference films carry music, our house rule is no music, so those are information only. Loudness, true peak, realness, sync, spectrum and the ending must still pass.
4. Put `mix.wav` in the HyperFrames project as the single `<audio>` track.

## 7. Adding a new sound

Only after the user approves it by ear. Source a real recording (Mixkit, Freesound CC0/CC BY, Pixabay; check the licence on the item's own page), add it to `make_premium.py` with the same smoothing chain, send a preview, and on approval copy it into `approved/` and add a row to sections 1, 2 and 5.
