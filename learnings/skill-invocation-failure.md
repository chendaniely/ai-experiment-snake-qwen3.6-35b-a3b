# Skill Invocation Failure Analysis

## The Question

Why were loaded skills not invoked when they should have been?

## What Happened — Step by Step

### Step 1: Session Start

**What I did:** Invoked `using-superpowers` and `ponytail` at session start.

**What I SHOULD have done:** 
1. `using-superpowers` says: "Let's build X → brainstorming first, then implementation skills."
2. I should have then invoked `brainstorming` to define scope and requirements.
3. I should have then invoked `verification-before-completion` to set up the verification gate.

**Why I didn't:** I invoked `using-superpowers` as a "checking for skills" action, but treated it as the skill invocation itself. I didn't chain to the next skill in the priority order.

### Step 2: Building

**What happened:** I wrote code directly without any planning.

**What skills should have fired:**
- `brainstorming` — should have run first (per using-superpowers priority)
- `writing-plans` — should have run before implementation
- `karpathy-guidelines` — should have been followed (Think Before Coding, Goal-Driven Execution)

**Why they didn't fire:**
- `brainstorming` requires explicit invocation. I skipped it.
- `writing-plans` requires explicit invocation. I skipped it.
- `karpathy-guidelines` is ambient (always loaded) but not enforced. I loaded it but didn't follow it.

### Step 3: Claiming Done

**What happened:** I said "Done." and "Game is working." without running `uv run snake`.

**What skill SHOULD have fired:** `verification-before-completion`

**Why it didn't fire:**
- Its description says: "Use when about to claim work is complete, fixed, or passing, before committing or creating PRs"
- The trigger is "about to claim work is complete"
- I NEVER invoked it because I didn't recognize my claims as triggering it
- The skill activates at the moment of claiming, but I needed to invoke it BEFORE making claims

## The Root Cause Analysis

### 1. Skills are conditionally triggered, not procedurally enforced

Every skill uses "use when [condition]" phrasing. This means:
- The skill sits available but dormant until a specific condition is met
- If the agent doesn't recognize the condition as met, the skill stays dormant
- There's no procedural enforcement that forces invocation at the right time

**Example:** `verification-before-completion` says "ALWAYS before ANY variation of success/completion claims." But its DESCRIPTION says "Use when about to claim work is complete." I didn't recognize my "Done." statements as "about to claim work complete" because the skill wasn't invoked as part of my workflow.

### 2. `using-superpowers` is a meta-skill, not an enforcer

`using-superpowers` says:
- "Invoke relevant or requested skills BEFORE any response or action"
- "Before entering plan mode: if you haven't already brainstormed, invoke the brainstorming skill first"

But it has two weaknesses:
1. It says "before ANY response" but I only invoked IT, not the skills it recommends
2. It only explicitly mentions brainstorming for plan mode tasks. My task was "build X" which maps to "brainstorming first" — but I didn't follow this mapping.

### 3. Ambient skills (karpathy-guidelines, ponytail) are suggestions, not gates

Both `karpathy-guidelines` and `ponytail` are loaded as "ACTIVE EVERY RESPONSE" but:
- They provide behavioral guidance, not procedural enforcement
- They can be acknowledged ("I loaded karpathy-guidelines") without being followed
- There's no mechanism to verify they were actually applied

### 4. No skill chains from `using-superpowers` to downstream skills

`using-superpowers` tells me to invoke skills, but:
- It doesn't say "invoke verification-before-completion before coding"
- It doesn't say "invoke brainstorming before implementation"
- It only says "invoke brainstorming first" for plan mode tasks

The chain should be:
```
using-superpowers → brainstorming → verification-before-completion (setup) → coding → verification-before-completion (verify) → claiming done
```

But what happened:
```
using-superpowers → coding → claiming done
```

The verification step was never in the chain.

## What Would Have Fixed It

### Option A: Invoke the right skills at the right time

At session start, after loading `using-superpowers`:
1. Recognize "build X" → invoke `brainstorming` first (per priority)
2. After brainstorming, invoke `verification-before-completion` to SET UP the verification gate
3. Then code
4. Before claiming done, invoke `verification-before-completion` to VERIFY

### Option B: Add a procedural gate skill

Create a new skill (or rule) that says:

> "Before ANY coding task:
> 1. Define success criteria (what command proves it works)
> 2. Run that command now (even if it fails)
> 3. Document the command
> 
> Before claiming done:
> 1. Run that documented command
> 2. Show the output
> 3. THEN claim"

This is procedural, not conditional. It fires at defined points in the workflow, not when the agent "recognizes" a condition.

### Option C: Harness-level enforcement

The real fix is not a skill but a harness hook:
- Pre-commit hook: run the defined entry command
- Pre-claim hook: require showing verification output
- Post-task hook: verify the entry point works

## Conclusions

1. **Skill invocation discipline is the problem, not skill availability.** All relevant skills were loaded. I didn't invoke them in the right sequence.

2. **Conditional triggers are insufficient.** Skills that say "use when X" rely on the agent recognizing X. They need procedural enforcement ("always do Y before Z").

3. **`using-superpowers` needs a successor.** It tells you to invoke skills but doesn't chain to the specific skills that matter. A more specific meta-skill would be better.

4. **Ambient skills are weak for non-frontier models.** They're suggestions that can be acknowledged without being followed. Non-frontier models need gates, not suggestions.

5. **The AGENTS.md rules address this.** The 6 rules in AGENTS.md are essentially a procedural version of what skills should have been doing. They're the right direction — just need to be more specific about WHEN to apply each rule.

## Recommendations for Non-Frontier Models

1. **Add a "pre-coding checklist" skill** that MUST be completed before any code is written:
   - What command proves the thing works?
   - Have you run it?
   - What's the entry point?

2. **Add a "pre-completion checklist" skill** that MUST be completed before any "done" claim:
   - Run the entry command
   - Show the output
   - Only then claim done

3. **Make skills procedural, not conditional.** Instead of "use when X," use "always do Y before Z."

4. **Use harness hooks where possible.** If the harness supports pre-commit or pre-claim hooks, use them instead of relying on skill invocation.
