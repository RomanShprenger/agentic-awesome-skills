---
name: create-music-elevenlabs
description: Generate an instrumental music bed via ElevenLabs Music, ROUTED THROUGH
  THE elevenlabs-proxy so it bills the Ads agent. Trims any sparse intro, loudnorm,
  fades the tail. Prompt + length from the temp…
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

# create-music-elevenlabs

Generate an instrumental music bed via ElevenLabs Music, ROUTED THROUGH THE elevenlabs-proxy so it bills the Ads agent. Trims any sparse intro, loudnorm, fades the tail. Prompt + length from the template recipe. Use for the music layer of any video-ad format.

## Run
gen_music.py --prompt '...' --duration 10 --out music.m4a — bills the agent; writes a duration-clamped, loudnorm'd bed.

## Contract
- Paid calls route through the GooseWorks proxies (bills the Ads agent) via the
  bundled `media_proxy.py` — never a provider SDK's default host.
- The template recipe (DB) supplies the model + params; this capability is generic.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
