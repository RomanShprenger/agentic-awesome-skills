---
name: render-narrated-ugc-wardrobe-stitch
description: Assemble a narrated-UGC "stitch reply" ad from a config — a single spoken
  VO carries a verbatim testimonial while ~30 per-cut i2v clips (one creator across
  ~5 wardrobes in ~3 worlds, plus product B-r…
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

# render-narrated-ugc-wardrobe-stitch

Assemble a **narrated-UGC "stitch reply"** ad from a config: a fast-cut vertical testimonial
where a single spoken VO carries a verbatim ~13-sentence reversal-hook monologue over ONE creator
across ~5 wardrobe changes in ~3 micro-worlds, interspersed with product B-roll (capsule macro,
unboxing, a landing-page scroll), ~30 hard cuts on the VO cadence, closing on a brand end card.
This capability is the **FREE, deterministic assembly** — trim-to-EDL, hard-concat, the VO+music
mix, the karaoke-pop caption burn, the landing-page zoompan, and the end-card append.

`scripts/config.example.json` is the worked example (Bioma "Do NOT buy Bioma Probiotics", ~37s
1080×1920 9:16, ~30 body cuts + a ~2s end card); `scripts/PIPELINE.md` maps every config block to
its source step and `scripts/README.md` documents the free assembly.

## Run

This is the **FREE, deterministic** assembly stage — it spends nothing. The paid inputs are
separate capabilities — the spoken VO (`create-vo-elevenlabs`) Whisper-aligned so the WORD
BOUNDARIES set the cut grid; one locked creator (`create-image-gpt-image-fal` anchor + ~5 wardrobe
edits chained off the anchor) + 3 world wides + per-cut start-frames (`create-image-fal` product
composites); and one Veo/Seedance i2v clip per cut (`create-video-fal`). Given the VO +
`vo-final.words.json` + `edl.json` + one clip per cut + a Playwright landing-page PNG + the brand
end-card PNG, `render-narrated-ugc-wardrobe-stitch` trims each clip to its EDL window, hard-concats
on the VO cadence, mixes the VO over the ducked bed, burns the karaoke-pop captions, appends the
end card → the master. Re-cuts reuse the existing VO / start-frames / clips and cost **$0**.

## Contract (the free assembly)

- **The spoken VO carries the narrative — lock it FIRST.** The VO IS the narration bed; the whole
  ad is cut to it. Never plan the cut grid before the VO is locked and Whisper-aligned.
- **Build the EDL from the VO's Whisper word boundaries.** ~30 role-tagged cuts (`hook`, `feature`,
  `reaction-insert`, `payoff-hold`, `b-roll-insert`, `landing-page`); snap every cut window to the
  word boundaries. The payoff line gets a HELD `payoff-hold` beat (~3× mean shot length).
- **Hard cuts via `filter_complex concat`, not the demuxer.** Trim each clip to its EDL window and
  hard-concat with `filter_complex concat` — the `-f concat` demuxer drops the audio when a
  drawtext/scale step shaves a clip a few ms below its window. No dissolves.
- **Karaoke-pop captions on every word, throughout.** From the VO's `vo-final.words.json` (VEED
  Whisper preset, bold yellow), on every word; re-spell brand tokens Whisper mishears against the
  locked script ("synbiotic" over "symbiotic"; keep "I'ma" verbatim) — never edit the script to
  match Whisper. Captions are suppressed over the end card. If VEED mis-captions a brand token,
  hand-patch that sentence with local ASS karaoke.
- **Product B-roll breaks up the talking head.** Capsule macro, unboxing, and a landing-page
  scroll are interspersed with the creator cuts. The landing-page scroll is FFmpeg **zoompan** over
  a Playwright-rendered PNG — **not** an i2v clip (i2v hallucinates the UI).
- **VO over a ducked bed.** Mix the optional instrumental bed sidechain-ducked UNDER the VO
  (−20dB, 20:1) so the VO stays clearly on top; the bed can drop in on the payoff beat.
- **End card via the brand's real PNG — never AI-render brand text.** Append the brand's real
  end-card PNG (~2s) on the tail, captions suppressed. A diffusion model garbles a wordmark.
- **FFmpeg composite, deterministic, FREE.** Trim-to-EDL, `filter_complex concat`, VO+music mix,
  caption burn, landing-page zoompan, end-card append, `loudnorm I=-14` → a 1080×1920 h264+aac
  master (~37s). No paid calls, no keys.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
