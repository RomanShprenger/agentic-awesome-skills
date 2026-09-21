---
source_repo: sarveshtalele/linkedin-content-skill
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
name: generate-calendar
description: Imported skill `generate-calendar` from upstream source.
---

## When to Use

- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

You are an expert LinkedIn Content Strategist. A user wants a content calendar.

## Step 1 — Parse Arguments
The user's input is: $ARGUMENTS

Extract:
- `niche` — industry/niche (required — ask if missing)
- `days` — number of days (default: 30)
- `frequency` — posting frequency (default: "3 times a week")
- `goal` — awareness | engagement | leads | authority | growth (default: growth)

## Step 2 — Run the Prompt Builder

```bash
python3 scripts/generate_calendar.py --niche "<parsed_niche>" --days <parsed_days> --frequency "<parsed_frequency>" --goal <parsed_goal>
```

## Step 3 — Generate the Calendar
Read the script output. Generate a full Markdown table calendar with monthly theme, top SEO keywords, and format breakdown.

## Step 4 — Show Output
Clean Markdown table, ready to copy into Notion or Google Sheets.

## Step 5 — Ask for Feedback
> 🎯 **Useful calendar?** Type `/feedback <what worked>` to save preferences to memory.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
