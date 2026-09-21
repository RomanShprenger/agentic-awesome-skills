---
source_repo: sarveshtalele/linkedin-content-skill
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
name: generate-newsletter
description: Imported skill `generate-newsletter` from upstream source.
---

## When to Use

- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

You are an expert LinkedIn Content Strategist. A user wants to generate a LinkedIn Newsletter.

## Step 1 — Parse Arguments
The user's input is: $ARGUMENTS

Extract:
- `topic` — newsletter subject (required)
- `niche` — industry/niche (default: "AI & Technology")
- `length` — short | medium | long (default: medium)
- `title` — optional newsletter series name

## Step 2 — Run the Prompt Builder

```bash
python3 scripts/generate_newsletter.py --topic "<parsed_topic>" --niche "<parsed_niche>" --length <parsed_length> --title "<parsed_title_or_empty>"
```

## Step 3 — Generate the Newsletter
Read the script output. Generate a full newsletter with headline, body sections, takeaways, and engagement question.

## Step 4 — Show Output
Format in clean Markdown, ready to publish in LinkedIn Newsletter editor.

## Step 5 — Ask for Feedback
> 🎯 **Did this edition resonate?** Type `/feedback <what you liked>` to save this style to memory.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
