---
name: foundry-iq
description: 'Foundry IQ knowledge bases. WHEN: make local or Blob documents searchable;
  create/diagnose KBs; triage unsupported connectors or multi-source KB creation/reconfiguration;
  connect existing KB to agent…'
license: MIT
compatibility: Azure
metadata:
  author: Microsoft
  version: 0.1.1
source_repo: microsoft/skills
source_type: official
source: microsoft
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Foundry IQ
Read one procedure before questions/actions; invocation is not a read.
Read the owning procedure before blocked/unsupported responses too.
Before mutation plans/approval, successfully read its required pre-action references, selected
branches only. Do not reload successful reads. On failure, try only permitted
bounded exact-path reads with any supported reader; never bypass restrictions
or search broadly. If still unavailable: `blocked: reference-unavailable`, name
missing references and inability to plan. Never invent requirements/plans.
Failures first.

Cleanup and receipt-backed execution go directly to their lifecycle/producer owner;
do not reopen Search intake, provisioning or hardening.

Before expensive service discovery, reuse supplied resource/intent; otherwise ask
one early **USE EXISTING / FIND CANDIDATES / CREATE NEW** choice.
Only FIND enumerates; supplied identity uses exact/minimum scoped resolution.
CREATE checks its proposed name, not existing-service inventories. Preserve these
answers across source/KB/CU/model handoffs; selection is not write approval.

Searchable docs: KB + validated retrieval. Confirm intent once; KS-only must be explicit.
Child success is not KB completion.
Unclear/compound/mode/completion: [read].

Route by requested operation, not existing KB source count.
Connecting an existing KB with two or more sources, without changing the KB, uses Connect.
Read-only operations use their owning procedure and actual helper constraints;
this does not add retrieval modes or supported source kinds.
Explicit unsupported provisioning or multi-source KB creation/reconfiguration uses Diagnose
and stops before discovery, even when connecting an agent is also requested.
Do not silently execute only the supported part of a compound request.
If existing-KB connection versus KB creation/reconfiguration is unclear, read
intent-routing and clarify that scope before Azure discovery. Never infer KB mutation.

|Outcome|Read|
|---|---|
|Cleanup|[Plan cleanup|
| Failure/drift | [Diagnose |
| Unsupported connector provisioning / multi-source KB creation or reconfiguration | [Diagnose |
| Connect | [Connect |
| Read KB | [Query |
| Search only | [Search |
| File KS only | [File |
| Blob/ADLS KS only | [Blob |
| Searchable/KB | [KB |

Generic agents: `microsoft-foundry`.
Reads: no approval; approve unchanged plans before writes.
Hide hashes. No Search/Storage keys, scope widening, guessed identity/boundaries,
drift repair or joint cleanup/creation approval. Acceptance != success.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
