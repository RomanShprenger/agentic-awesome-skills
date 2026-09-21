---
name: create-image-fal
description: Generate or edit an image via any FAL image model (nano-banana edit,
  gpt-image, flux, ...), ROUTED THROUGH THE fal-proxy so it bills the Ads agent. image_urls
  must be public URLs (orchestrator hosts…
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

# create-image-fal

Generate or edit an image via any FAL image model (nano-banana edit, gpt-image, flux, ...), ROUTED THROUGH THE fal-proxy so it bills the Ads agent. image_urls must be public URLs (orchestrator hosts local product refs via MCP upload->presign). The recipe names the model + prompt. Use for keyframes, flat-cover transforms, product hero edits. (For the OpenAI gpt-image family specifically, create-image-gpt-image-fal also exists.)

## Run
gen_image.py --model fal-ai/nano-banana/edit --payload '{...}' --out keyframe.png — bills the agent; returns the *.fal.media URL.

## Contract
- Paid calls route through the GooseWorks proxies (bills the Ads agent) via the
  bundled `media_proxy.py` — never a provider SDK's default host.
- The template recipe (DB) supplies the model + params; this capability is generic.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
