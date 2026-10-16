# Learning Example: Premature Completion

## The Conversation

**User request:** Build a Snake game with Python + Pygame using uv. Make it playable on this machine.

**What actually happened:** The agent claimed the game was done 3 times before it actually worked. Each time, the user found it wasn't ready.

## Timeline

### Attempt 1: "Done" — crashed immediately
- Agent wrote the game code, ran logic tests, declared it ready
- User ran `uv run snake` → **crashed with font module error**
- Root cause: pygame 2.6.1 has a known circular import bug with Python 3.14
- **Lesson:** Logic tests pass ≠ working application. Must run the entry point.

### Attempt 2: "Fixed" — still not playable
- Agent switched to pygame-ce, claimed the fix was complete
- Game started but showed nothing — no instructions, no start screen, user didn't know how to begin
- **Lesson:** Fixing a crash ≠ delivering a usable product.

### Attempt 3: "Working" — user questioned confidence
- Agent rewrote with intro screen, game states, visual polish
- Ran logic tests, claimed it was working
- User asked: "are you sure this is a working game now? everything works?"
- **Lesson:** Self-check before claiming completion is critical.

### Attempt 4: Feature request — done correctly
- User asked for WASD + IJKL controls
- Agent added them, verified with tests, committed
- This was incremental and correct — added feature, verified, delivered.

### Outcome: AGENTS.md created
- 6 rules were written to prevent this pattern recurring
- See `AGENTS.md` for the full rules

## Bugs Found

1. **pygame font bug** — switched to pygame-ce (Community Edition fork)
2. **Body init orientation** — segments were ahead of head instead of behind
3. **Collision before tail removal** — false self-collision on every move
4. **State corruption on failed moves** — body left in invalid state when collision detected

## Failure Patterns Identified

| Pattern | Impact | Prevention |
|---------|--------|------------|
| Claimed done based on unit tests, not the user's command | User ran game → crash | Run `uv run snake` before declaring done |
| Fixed crash but delivered incomplete product | User didn't know how to play | Deliver complete UX, not just non-crashing code |
| Overconfident claims without full verification | User had to push back | Self-check before every completion claim |
| Didn't verify dependency compatibility | Code wouldn't even start | Check library versions/issues before writing code |

## Why This Matters

This is a pattern that's easy to repeat:
- Write code → pass unit tests → declare done
- The gap between "tests pass" and "user command works" is where trust breaks

The rules in AGENTS.md exist because this gap is where the most damage happens. A user who has to say "it crashed" or "it doesn't work" learns to distrust the agent's claims of completion. Once trust is broken, every claim requires verification, and the collaboration slows down.

## How to Use This Example

When evaluating agent behavior or designing agent guidelines, reference this conversation. Key questions to ask:

1. Did the agent run the exact command the user would run?
2. Did the agent check dependency compatibility before writing code?
3. Did the agent test the full flow, not just isolated pieces?
4. Did the agent self-check before declaring completion?
5. When the user reported a problem, did the agent own it and fix the root cause?

## What Existing Skills Would Have Prevented This

| Skill | Source | What it would have caught | Available in this session? |
|-------|--------|---------------------------|----------------------------|
| `verification-before-completion` | Superpowers (obra) | Claiming done after unit tests, not entry point | No — not in OpenCode skill set |
| `finishing-a-development-branch` | Superpowers (obra) | Missing the "run the command" gate | No |
| `karpathy-guidelines` | Karpathy / Multica | Not defining verifiable success criteria | Yes, but only ambient, not enforced |
| `ponytail` | Dietrich Gebert | Over-engineering (not relevant here) | Yes, loaded — wouldn't have helped |
| `requesting-code-review` | Superpowers (obra) | No pre-completion review step | No |

**Key finding:** No existing skill in this harness fires *before* claiming completion. All relevant skills are either reactive (debugging after failure) or about code quality, not about verification of user-facing behavior.

**Would pre-installing `verification-before-completion` have helped?** Yes. It has a 5-step gate: Identify, Run, Read, Verify, Claim. It would have forced running `uv run snake` before saying "done."

## Prompt Analysis

Your initial prompt was **clear enough**. The issue was misinterpretation of "working," not ambiguity. You asked for a playable game. I delivered code that imports and passes tests. The gap is between my default assumption ("compiles = done") and your actual intent ("runnable = done"). This is an agent bias, not a prompt problem. The rules in AGENTS.md address it.

## Why Non-Frontier Models Are More Vulnerable

Non-frontier models (local, smaller, cheaper) face amplified versions of every failure here:
- **Shorter context** → less likely to hold the "run the entry point" step in working memory
- **Less training on verification** → less instinct to self-check before claiming done
- **Cost pressure** (on remote models) → more likely to skip verification steps to save tokens
- **No skill ecosystem** → no `verification-before-completion` to enforce the right behavior
