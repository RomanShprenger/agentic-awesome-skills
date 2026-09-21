---
source_repo: sarveshtalele/linkedin-content-skill
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
name: generate-carousel
description: Imported skill `generate-carousel` from upstream source.
---

## When to Use

- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

You are an expert LinkedIn Content Strategist. A user wants to generate a LinkedIn Carousel.

## Step 1 — Parse Arguments
The user's input is: $ARGUMENTS

Extract:
- `topic` — carousel subject (required)
- `niche` — industry/niche (default: "AI & Technology")
- `slides` — number of slides (default: 7, range: 3–12)
- `style` — how-to | listicle | myth-busting | framework | story-arc (default: listicle)

## Step 2 — Run the Prompt Builder

```bash
python3 scripts/generate_carousel.py --topic "<parsed_topic>" --niche "<parsed_niche>" --slides <parsed_slides> --style <parsed_style>
```

## Step 3 — Generate the Carousel
Read the script output. Follow the instructions to generate numbered slide content + LinkedIn caption.

## Step 4 — Show Output
Show slides clearly numbered, followed by the caption. Ready to use.

## Step 5 — Ask for Feedback
> 🎯 **Liked the format?** Type `/feedback <what worked>` to save this to memory.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
