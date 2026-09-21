---
name: smart-commit
description: AI-powered git commit message generation. Uses LLM to summarize changes
  and create meaningful commit messages. Triggers when user wants to commit changes,
  amend/squash commits, or needs LLM to summar…
user-invocable: true
source_repo: jackjin1997/clawforge
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Smart Commit

AI-powered git commit message generation using LLM. Creates meaningful commit messages from code changes.

## Capabilities

1. **Amend Last Commit** - Summarize staged/unstaged changes and amend the last commit message
2. **Squash Commits** - Summarize last N commits and create a consolidated commit
3. **Interactive Commit** - Confirm files with user, then summarize and create new commit

## Quick Start

### For New Commit
```bash
# Show changed files and ask user confirmation
git status

# After confirmation, summarize changes with LLM
# Create commit with generated message
```

### For Amending
```bash
# Get diff of changes to amend
git diff --cached  # staged
git diff HEAD~1    # compared to last commit

# LLM summarizes, then
git commit --amend -m "new message"
```

### For Squashing
```bash
# Get last N commit messages and diffs
git log -n N --format="%H %s"

# LLM summarizes, then
git reset --soft HEAD~N
git commit -m "consolidated message"
```

## Workflow Decision Tree

```
User wants git commit help?
├─ "amend" or "修改"? → Amend workflow
├─ "squash" or "合并" + number? → Squash workflow
└─ New commit? → Interactive workflow
```

## Amend Workflow

1. Get changes: `git diff --cached` (staged) or `git diff HEAD~1` (all changes since last commit)
2. Send to LLM with prompt from `references/prompts.md` section "Amend Commit"
3. User reviews suggested message
4. `git commit --amend -m "message"`

## Squash Workflow

1. Get last N commits: `git log -n N --format="%H|%s|%an|%ad"`
2. Get combined diff: `git diff HEAD~N..HEAD`
3. Send to LLM with prompt from `references/prompts.md` section "Squash Commits"
4. User reviews suggested message
5. `git reset --soft HEAD~N && git commit -m "message"`

## Interactive Commit Workflow

1. Show `git status` to user
2. Ask user to confirm which files to include
3. Get diff for confirmed files
4. Send to LLM with prompt from `references/prompts.md` section "New Commit"
5. User reviews suggested message
6. `git add <files> && git commit -m "message"`

## LLM Prompts

See `references/prompts.md` for:
- New commit message generation
- Amend commit message generation
- Squash commit message generation

Each prompt includes:
- Git diff input format
- Output format requirements
- Style guidelines (conventional commits, etc.)

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
