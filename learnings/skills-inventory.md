# Skills Inventory — OpenCode vs Claude Code

## Summary

All the key prevention skills that would have caught the Snake game mistakes are **already loaded in OpenCode**. The failure was **not** a missing skill — it was a failure to invoke them.

## What's Loaded in OpenCode (from system prompt)

### Superpowers 7.0.0 — All 16 skills ✓

| Skill | Would Have Helped? | Why It Failed |
|-------|-------------------|---------------|
| `using-superpowers` | Yes (meta-skill) | Loaded, but didn't trigger downstream skills |
| `brainstorming` | Yes | Loaded, but skipped — went straight to code |
| `verification-before-completion` | **Critical** | Loaded, but not invoked before claiming done |
| `finishing-a-development-branch` | Yes | Loaded, but not used at completion |
| `requesting-code-review` | Yes | Loaded, but self-review happened inline instead of via skill |
| `test-driven-development` | Partially | Logic tests were written but not as TDD red-green cycle |
| `systematic-debugging` | Post-mortem only | Used after user reported crash |
| `diagnosing-superpowers` | Post-mortem only | Would identify this pattern retroactively |
| `dispatching-parallel-agents` | No (not applicable) | — |
| `executing-plans` | Partially | No plan was written before coding |
| `subagent-driven-development` | Partially | Not used for self-verification |
| `writing-plans` | Yes | No implementation plan was written |
| `writing-skills` | No (meta-skill) | — |
| `using-git-worktrees` | No (not applicable) | — |
| `receiving-code-review` | No (self-review) | — |

### Karpathy Guidelines ✓
| Skill | Would Have Helped? | Why It Failed |
|-------|-------------------|---------------|
| `karpathy-guidelines` | **Yes** | Loaded, but not applied — didn't define verifiable success criteria before coding |

### Ponytail ✓
| Skill | Would Have Helped? | Why It Failed |
|-------|-------------------|---------------|
| `ponytail` | No | Constrains code volume, not verification behavior. Different failure mode. |

### Other Loaded Skills

| Skill | Notes |
|-------|-------|
| `diagnosing-bugs` (Matt Pocock) | Would have helped after the crash was reported |
| `code-review` (OpenCode built-in) | Not invoked — self-review was informal |
| `critical-code-reviewer` | Not invoked |
| `tdd` (OpenCode built-in) | Not invoked as formal TDD |
| `systematic-debugging` (built-in) | Loaded, used after crash |

## What's in Claude Code but NOT in OpenCode

### Matt Pocock Skills (from `claude-plugins-official/mattpocock-skills/1.3.1`)

These are available in Claude Code but could be added to OpenCode:

| Skill | Description | Value |
|-------|-------------|-------|
| `code-review` | Two-axis review (Standards + Spec) via parallel sub-agents | Strong — would catch spec mismatches |
| `diagnosing-bugs` | 6-phase diagnosis loop with feedback loops | Strong — would catch root causes faster |
| `domain-modeling` | Build project domain model | Moderate |
| `research` | Investigate questions across sources | Moderate |
| `wizard` | Generate interactive bash wizards for user tasks | Moderate |
| `setup-pre-commit` | Husky pre-commit hooks | Weak for this case |
| `migrate-to-shoehorn` | TypeScript type assertion migration | Niche |
| `scaffold-exercises` | Exercise directory structures | Niche |
| `git-guardrails-claude-code` | Block dangerous git commands | Weak for this case |

### What's NOT in Either Harness

| Skill | Source | Description |
|-------|--------|-------------|
| `karpathy-guidelines` | Karpathy / Multica | In OpenCode loaded from system prompt. In Claude Code, available via `multica-ai/andrej-karpathy-skills` plugin. |
| `ponytail` | Dietrich Gebert | In OpenCode loaded from system prompt. In Claude Code, available via `dietrichgebert/ponytail` plugin. |

## The Real Problem

**Skills were available. Invocation discipline was not.**

The `verification-before-completion` skill was loaded and its SKILL.md content was available in context. It defines:

> "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"
> "If you haven't run the verification command in this message, you cannot claim it passes."

Yet it was not invoked before saying "Done." This is a **process failure**, not a **skills gap**.

## What This Means for Non-Frontier Models

Non-frontier models (local, smaller, cheaper) are more vulnerable because:

1. **Shorter context** — skill content may get truncated or not fully loaded
2. **Less training on skill invocation** — fewer examples of using skills before acting
3. **No skill ecosystem** — may not have any verification skills at all
4. **No enforcement** — skills are suggestions, not gates. A smaller model is more likely to skip them

**For non-frontier models, skills need to be:**
- Shorter (less context pressure)
- More imperative (less room for interpretation)
- Enforced via harness hooks, not just instructions
- Paired with explicit checklists that must be completed

## Recommended Actions

### For OpenCode (current harness)
1. **No new skills needed** — the prevention skills are already loaded
2. **Fix the invocation discipline** — the AGENTS.md rules address this
3. **Consider Matt Pocock's code-review** for stronger spec-matching reviews

### For Non-Frontier Model Setup
1. **Install a minimal verification skill** — shorter, more imperative than the full Superpowers one
2. **Add a pre-completion checklist** that must be checked before any "done" claim
3. **Use harness hooks** (if available) to enforce the verification gate
4. **Document the skill invocation pattern** explicitly in AGENTS.md
