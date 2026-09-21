---
name: create-video-fal
description: Image-to-video (or text-to-video) via any FAL video model (Kling, Seedance,
  Veo), ROUTED THROUGH THE GooseWorks fal-proxy so the call bills the Ads agent. The
  template recipe names the model + params…
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

# create-video-fal

Image-to-video (or text-to-video) via any FAL video model (Kling, Seedance, Veo), ROUTED THROUGH THE GooseWorks fal-proxy so the call bills the Ads agent. The template recipe names the model + params; image_url inputs must be public URLs (the orchestrator hosts local frames via MCP get_upload_url -> get_download_url). Returns the result video URL and downloads it. Use for the generative base clip of any video-ad format.

## Run
gen_video.py --model fal-ai/kling-video/v2.1/standard/image-to-video --payload '{...}' --out clip.mp4 — bills the agent; host-swaps the FAL queue URLs; downloads the result.

## Contract
- Paid calls route through the GooseWorks proxies (bills the Ads agent) via the
  bundled `media_proxy.py` — never a provider SDK's default host.
- The template recipe (DB) supplies the model + params; this capability is generic.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
