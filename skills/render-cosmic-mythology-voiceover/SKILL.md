---
name: render-cosmic-mythology-voiceover
description: Assemble a cosmic-mythology-voiceover reel from a config — a warm spoken
  voiceover carries the whole narrative while N curated cosmic stills are weighted
  beat-synced across the delivered VO duration…
status: active
source_repo: gooseworks-ai/goose-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# render-cosmic-mythology-voiceover

Assemble a **cosmic-mythology-voiceover** reel from a config: a faceless, cinematic storytelling
video where a warm, contemplative spoken **voiceover** carries the whole narrative (a "myth as
teacher" reframe) over a slow, weighted **Ken-Burns zoom** across curated cosmic / mythology stills
in ONE ethereal deep-indigo + gold look, with ONE on-screen hook line and burned captions. This
capability is the **FREE, deterministic assembly** — the weighted beat-sync sequencing, the
Ken-Burns render, the concat, the VO composite, the hook overlay, and the caption burn.

`scripts/config.example.json` is the worked example (WishAstro "Saturn isn't your villain", ~31s
1080×1920 9:16, 12 weighted Ken-Burns cuts); `scripts/PIPELINE.md` maps every config block to its
source step and `scripts/README.md` documents the free assembly.

## Run

There is a single runnable script — `scripts/render.py` (config-driven, ffmpeg + Pillow only, NO
API keys and NO `drawtext`/`libass` required):

```bash
python3 scripts/render.py --config config.json --vo working/vo2/vo_atempo.mp3 \
  --stills-dir working/stills --out working/final.mp4 \
  [--words working/vo2/words.json] [--endcard working/endcard.png]
```

This is the **FREE, deterministic** assembly stage — it spends nothing. The paid inputs are
separate capabilities — the spoken VO (`create-vo-elevenlabs`, ElevenLabs `eleven_v3` from a
tone-tagged script, atempo time-stretched so the delivered duration sets the timeline) and the 4–6
hero stills in one look pack (`create-image-fal`, Flux Pro 1.1, reused as repeats to reach the
~10–12 cuts). Given the VO + the stills + the per-cut weight array + the hook line, `render.py`
distributes the cuts across the VO duration by the weighted formula, Ken-Burns-renders each still,
concats, composites the VO, fades the hook line on over the open, burns the captions, and (if
`--endcard` is passed) appends a brand end card → the master + a poster. Re-cuts reuse the existing
VO / stills and cost **$0**. See `scripts/README.md` §0 for the full arg contract.

## Contract (the free assembly)

- **The spoken VO carries the narrative — no talking head, no sung song.** The generated/supplied
  VO IS the audio bed (no music bed by default); do not add a presenter or a second bed.
- **Plan the timeline AROUND the delivered VO duration.** The VO is atempo time-stretched (clamp
  the factor ≤ ~1.25 so the voice never chipmunks); its delivered length sets the timeline — never
  trim the VO to a pre-planned grid.
- **Weighted beat-sync, not a fixed grid.** For each cut, `cut_dur = VO_dur × weight / Σweights` —
  heavier weights hold longer on the emotional beats (the open, the reframe, the close); the setup
  cuts run shorter. Every cut stays proportional to the whole VO.
- **Ken-Burns per still.** Render each still with scale 2×, center crop, and a `zoompan` to the
  configured `zoom_end` (~1.10); apply `zoom_out` on the flagged cuts; `fade_in` on the FIRST cut
  and `fade_out` on the LAST. Stills are reusable — the sequence repeats a few across the cuts.
- **ONE cosmic look, no in-world text.** Every still reads in the single deep-indigo + gold +
  volumetric-light look; the reel's only text is the hook + the captions, added in post (the "no
  text, no words" descriptor keeps words off the stills).
- **ONE hook line, alpha-faded on over the open.** Burn the single reframe line over the OPEN only
  (fade in ~0.5s, hold, fade out ~0.6s) — never a persistent caption, never in-world. `render.py`
  does this with a PIL PNG + ffmpeg `fade=…:alpha=1` (no `drawtext` dependency, since stock ffmpeg
  often lacks it); an ffmpeg `drawtext` alpha window is an equivalent alternative where available.
- **Captions from Whisper — bottom, white.** VEED/Whisper subtitle burn tracks the spoken VO in the
  bottom third, white `#FFFFFF`. If the host ffmpeg lacks libass (no `subtitles`/`ass` filter),
  render the cues as timed PIL PNG overlays (ffmpeg `overlay=…:enable='between(t,st,en)'`) at the
  same bottom placement — a free local Whisper + ffmpeg burn is the fallback to the VEED tier.
- **FFmpeg composite, deterministic, FREE.** ffmpeg-concat the Ken-Burns clips, composite the VO
  under the picture (libx264 `crf 18` + aac 192k), burn the hook alpha-fade + the caption track →
  a 1080×1920 h264+aac master (~31s). No paid calls, no keys (the local caption fallback is free).

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
