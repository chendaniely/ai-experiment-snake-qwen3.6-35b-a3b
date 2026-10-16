# Procedural Skills — Teaching Examples

## Why These Exist

The Snake game session revealed a critical gap: **skills are conditionally triggered, not procedurally enforced.**

The loaded skills say "use when X" — they sit dormant until the agent recognizes X. This fails when:
- The agent doesn't recognize the condition
- The agent recognizes it but rationalizes around it
- The agent loads a meta-skill but doesn't chain to downstream skills

## These Skills Fix That

These three skills use **procedural enforcement** instead of conditional triggers:

### `pre-coding-checklist.md`
**What it does:** Forces definition of success criteria, user-facing command, and dependency compatibility BEFORE any code is written.

**How it's different:** The pre-coding checklist fires on ANY coding task. It doesn't wait for you to recognize a condition. It's a gate that must be passed before coding begins.

### `pre-completion-checklist.md`
**What it does:** Forces running the user-facing command, showing output, and verifying every criterion BEFORE any "done" claim.

**How it's different:** The pre-completion checklist fires before ANY completion claim. Not just "when about to claim done" — always before claiming. It requires showing evidence, not just asserting.

### `chain-to-downstream.md`
**What it does:** A meta-skill that chains skill invocation. It says which skills to invoke, in what order, for each task type.

**How it's different:** `using-superpowers` says "invoke skills" but doesn't say WHICH ones. This skill gives you the chain for every task type. "Build X" → brainstorming → writing-plans → implementation. No guessing.

## How to Use These as Teaching Examples

These are in `learnings/skills/` because they're teaching examples, not production skills yet. They demonstrate:

1. **Procedural > Conditional** — "always do X before Y" beats "use when X"
2. **Chaining > Isolation** — Skills should fire in sequence, not independently
3. **Evidence > Assertions** — "show the output" beats "should work"
4. **Gates > Suggestions** — "must complete" beats "should try"

## How to Install These

When ready to use, copy these to `~/.agents/skills/`:

```bash
cp learnings/skills/pre-coding-checklist.md ~/.agents/skills/pre-coding-checklist/SKILL.md
cp learnings/skills/pre-completion-checklist.md ~/.agents/skills/pre-completion-checklist/SKILL.md
cp learnings/skills/chain-to-downstream.md ~/.agents/skills/chain-to-downstream/SKILL.md
```

Or adapt them into your AGENTS.md as procedural rules:

```markdown
## Before Coding (procedural, not conditional)
1. Name the user-facing command
2. Run it (even if it fails)
3. List success criteria
4. Check dependency compatibility
5. Define minimal viable implementation

## Before Claiming Done (procedural, not conditional)
1. Run the user-facing command
2. Show the output
3. Verify every success criterion
4. Run tests
5. List what you did NOT check
```
