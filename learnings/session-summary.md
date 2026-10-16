# Session Summary — Learning Goals Achieved

## This Session's Purpose

Document a complete failure chain: agent claimed a Snake game was done when it crashed. Build rules, skills, and reference materials to prevent recurrence. Use as a teaching example for non-frontier model development.

## What We Built

### 1. The Game (snake/)
- Python + Pygame + uv Snake game
- WASD + IJKL controls
- Intro screen, game states, high score
- 5 git commits showing the evolution

### 2. The Rules (AGENTS.md)
6 rules to prevent premature completion claims:
1. Don't declare done until the user-facing command works
2. Verify dependencies before building
3. Test the full flow, not just pieces
4. Self-check before claiming completion
5. Verify no-crash initialization when you can't test output
6. If you make a mistake, own it immediately

### 3. The Learning Library (learnings/)
- `transcript.json` — Structured conversation data
- `analysis.md` — Narrative analysis + research
- `skills-inventory.md` — OpenCode vs Claude Code comparison
- `skill-invocation-failure.md` — Why loaded skills weren't invoked
- `retrospective-review.md` — What would have happened differently
- `external-skills-reference.md` — All external skills with links
- `claude-vs-opencode-skills.md` — Detailed skills comparison
- `skills/` — Procedural skill implementations

### 4. Procedural Skills (learnings/skills/)
- `pre-coding-checklist.md` — Must complete before any code
- `pre-completion-checklist.md` — Must complete before any "done" claim
- `chain-to-downstream.md` — Chains skill invocation by task type

### 5. Installed Skills (OpenCode)
- Matt Pocock code-review
- Matt Pocock diagnosing-bugs
- Matt Pocock domain-modeling
- Matt Pocock research

## Key Insights

1. **All prevention skills were loaded.** The failure was invocation discipline, not skill availability.
2. **Skills are conditionally triggered.** "use when X" sits dormant. "always do Y before Z" fires.
3. **Status bar shows idle during tool execution.** UX gap that compounds the problem.
4. **Better prompting helps, but procedural enforcement is better.** A well-crafted prompt is still only as good as the agent following through.
5. **Non-frontier models are more vulnerable.** Less context, less training on skill invocation, no skill ecosystem.

## Lessons Learned

### From the Agent's Perspective
- Loading a skill ≠ using it. Invocation discipline matters.
- "Should work" ≠ verified. Evidence before assertions.
- Ambient skills are suggestions, not gates.
- Logic tests ≠ user-facing behavior.

### From the User's Perspective
- Name the user-facing command in your prompt.
- Define what done looks like.
- Require running the entry point before claiming done.
- State the environment (Python version, platform, etc.).

### From a Skills Design Perspective
- Procedural > Conditional. "always do X before Y" beats "use when X."
- Chain > Isolation. Skills should fire in sequence.
- Evidence > Assertions. "show the output" beats "should work."
- Gates > Suggestions. "must complete" beats "should try."

## Files in This Repo

```
learnings/
├── README.md                    ← You are here
├── transcript.json              ← Structured conversation data
├── analysis.md                  ← Narrative analysis
├── skills-inventory.md          ← Skills comparison (OpenCode vs Claude Code)
├── skill-invocation-failure.md  ← Why loaded skills weren't invoked
├── retrospective-review.md      ← What would have happened with fixes
├── external-skills-reference.md ← All external skills with links
├── claude-vs-opencode-skills.md ← Detailed skills comparison
├── skills/
│   ├── README.md                ← How to use/install procedural skills
│   ├── pre-coding-checklist.md  ← Before any code
│   ├── pre-completion-checklist.md ← Before any "done" claim
│   └── chain-to-downstream.md   ← Chains skill invocation
```

## Git History

```
d7cdd7c feat: build Snake game with Python + Pygame
a883b00 fix: use pygame-ce for Python 3.14 font support
4084abd fix: complete snake game with intro screen, proper movement, and game states
3bae3a2 feat: add WASD and IJKL control schemes
46316ed docs: add AGENTS.md — rules to prevent premature completion claims
86cc7e3 docs: add learning library entry with dependency research
a2e1d48 docs: skills inventory and Matt Pocock skill installation
266c256 analysis: why loaded skills were not invoked
142aa68 docs: build procedural skills as teaching examples
de4fb1b docs: retrospective review — what would have happened with procedural skills installed
```

## Next Steps (If Any)

- Install procedural skills into `~/.agents/skills/` (currently in `learnings/skills/`)
- Adapt procedural skills into AGENTS.md as procedural rules
- Report OpenCode status bar UX issue (shows idle during tool execution)
- Add more learning examples to the library
