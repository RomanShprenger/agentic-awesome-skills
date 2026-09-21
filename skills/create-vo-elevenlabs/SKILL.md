---
name: create-vo-elevenlabs
description: Generate a voiceover (VO) clip via ElevenLabs text-to-speech, ROUTED
  THROUGH THE elevenlabs-proxy so it bills the Ads agent. Voice id + script text come
  from the template recipe. Use for the spoken n…
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

# create-vo-elevenlabs

VO via the elevenlabs-proxy (bills the Ads agent). `gen_vo.py --text "..." --voice <id> --out vo.mp3`.
The template recipe supplies the voice + text; paid call routes through media_proxy.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
