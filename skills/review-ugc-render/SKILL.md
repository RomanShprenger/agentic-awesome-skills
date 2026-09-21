---
name: review-ugc-render
description: Mandatory pre-publish review gate for a UGC video render. Transcribes
  the finished render's AUDIO with Whisper and word-diffs it against the approved
  spoken script, then gates set_final_render — bloc…
owner: akhil
status: active
version: 1
created: 2026-07-04
updated: 2026-07-04
source_repo: gooseworks-ai/goose-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# review-ugc-render

> The QC gate every UGC video recipe MUST clear before it publishes. Not an
> eyeball `/watch` — a deterministic transcript-vs-script diff that exits non-zero
> on a defect so the recipe can hard-stop `set_final_render`.

## Why this exists

Seedance generates the audio natively. It sometimes **mis-voices a word** — the
approved line `human-vetted` comes back spoken as `human witted`; documented
siblings: `Hume`→`Hune`, `Alitu`→`al-too`. The defect lives in the render's
audio, so an eyeball `/watch` ("dialogue matches the script") slips it through,
and a downstream caption pass then bakes the wrong word in verbatim. Nothing was
comparing the **actual spoken audio** against the **script the user approved**.

This gate does exactly that, deterministically, and refuses to publish on a miss.

## When to run

- **MANDATORY** in every `remix-ugc-*-from-sample` and `create-ugc-*-video-from-refs`
  recipe, in the QC phase, **after** the master render exists and **before**
  `set_final_render`.
- Re-run after every fix / re-roll until it PASSES.

## Contract

Before rendering, persist the exact approved spoken lines (the verbatim utterance,
no beat notes) to `working/approved-script.txt`. Then, after render:

```bash
python3 <pack>/review-ugc-render/scripts/review_render.py \
  --video working/final.mp4 \
  --script-file working/approved-script.txt \
  --json working/review-verdict.json
```

- **exit 0 → PASS** — proceed to publish (`set_final_render`).
- **exit 2 → FAIL** — do NOT publish. Read the report, fix, re-run.
- **exit 3 → ERROR** — the check could not run (see below); fix the environment, do
  not publish blind.

Transcription backend (in priority order): `OPENAI_API_KEY` (honors
`OPENAI_BASE_URL`, so it routes through the gooseworks Whisper proxy when set) →
local `whisper` CLI. `ffmpeg` must be on PATH.

## What FAIL means and how to fix

| Report line | Root cause | Fix |
|---|---|---|
| `[high] said [witted] where script has [vetted]` | Seedance mis-voiced the word in the generated audio | **Re-roll a new seed.** If it is a brand/coined token, spell it phonetically in the `SPOKEN LINE` (e.g. `Ali-too`, never a `(pronounced …)` parenthetical — Seedance reads parentheticals aloud). See `create-video-seedance-2-fal` Failure Modes. |
| `[medium] dropped [...]` / low similarity | Seedance dropped an approved phrase | Re-roll; if only a tail word, a surgical `stitch_replacement.py` window fix may recover it. |
| `⚠ audio is effectively silent` | Wrong render / audio track lost in post | Re-render / re-check the mux; never publish a silent take. |
| `ERROR: no transcription backend` | No `OPENAI_API_KEY` and no local `whisper` | Set the key (proxy `OPENAI_BASE_URL`) or install `whisper`, then re-run. |

`--expect-music` is advisory only (warns if a music bed is absent); it does not by
itself fail the gate.

## Inputs

- `--video PATH` (required) — the rendered master mp4.
- `--script-file PATH` **or** `--script "text"` — the approved spoken script. Omit
  both only for a genuinely script-free clip (the drift check is then skipped and
  the gate is advisory).
- `--min-ratio FLOAT` (default `0.90`) — transcript↔script token similarity to pass.
- `--json PATH` — write the machine verdict for the app's review panel.

## Tests

```bash
python3 tests/test_review_render.py    # pure verdict logic; no audio/network
```

Covers the canonical `vetted→witted` mis-voicing, brand-name mis-voicing, dropped
tails, benign filler, and the no-script advisory path.

## Relationship to the content-goose review engine

This is the shipped, single-file, gating slice of the fuller
`coworkers/video/molecules/review/review-loop` (18-axis rubric). Here we enforce
the one axis that catches audio-vs-script defects at publish time
(`review-transcript-integrity` / `brand_text_accuracy`). Deeper multi-axis review
stays in the content-goose lab.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
