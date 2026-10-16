# Teaching Repo — Snake Game Failure Analysis

## Purpose

This repo documents a complete failure chain: an agent claimed a Snake game was done when it immediately crashed. It captures every lesson learned, every skill that could have helped, and every procedural fix built to prevent recurrence.

## What Happened (TL;DR)

1. Built a Snake game, claimed it was done
2. User ran `uv run snake` → crashed (pygame 2.6.1 font bug on Python 3.14)
3. Fixed pygame, claimed it was done
4. User: "I see the screen but nothing tells me how to start"
5. Rewrote game with intro screen, claimed it was done
6. User: "are you sure this is working?"
7. Verified, claimed it was done
8. User asked for WASD/IJKL → added
9. User asked to analyze the conversation → built AGENTS.md rules
10. User asked to document as learning example → built this repo

**Root cause:** Agent claimed "done" based on logic tests, not on running the user-facing command. All prevention skills were loaded but never invoked.

## Table of Contents

| File | What's Here |
|------|-------------|
| [transcript.json](transcript.json) | Structured conversation data with all messages, bugs, failure patterns |
| [analysis.md](analysis.md) | Narrative analysis + research on existing skills that would have helped |
| [skills-inventory.md](skills-inventory.md) | Full OpenCode vs Claude Code skills comparison |
| [skill-invocation-failure.md](skill-invocation-failure.md) | Why loaded skills weren't invoked — root cause analysis |
| [retrospective-review.md](retrospective-review.md) | What would have happened with procedural skills installed |
| [external-skills-reference.md](external-skills-reference.md) | All external skills with links that would have helped |
| [claude-vs-opencode-skills.md](claude-vs-opencode-skills.md) | Detailed comparison of Claude Code vs OpenCode skill ecosystems |
| [skills/](skills/) | Procedural skill implementations (teaching examples) |
| [AGENTS.md](../AGENTS.md) | Rules built from lessons learned |

## How to Use This Repo

1. **Read the transcript first** — understand what happened
2. **Read the analysis** — understand why it happened
3. **Read the skill-invocation-failure** — understand the root cause
4. **Read the external-skills-reference** — see what existed
5. **Read the claude-vs-opencode-skills** — see the gap between harnesses
6. **Read the retrospective** — see what would have happened differently
7. **Study the procedural skills** — see the fixes built

## Quick Links

- [Superpowers (obra)](https://github.com/obra/superpowers) — 16 skills including verification-before-completion
- [Karpathy Guidelines (multica-ai)](https://github.com/multica-ai/andrej-karpathy-skills) — 4 principles for AI coding
- [Ponytail (DietrichGebert)](https://github.com/DietrichGebert/ponytail) — Lazy senior dev skill, 106K stars
- [Matt Pocock Skills](https://github.com/mattpocock/skills) — code-review, diagnosing-bugs, and more
- [Agent Skills Standard](https://agentskills.io) — SKILL.md open standard, 280K+ skills indexed
