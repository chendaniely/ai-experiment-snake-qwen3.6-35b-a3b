---
name: chain-to-downstream
description: Meta-skill that chains skill invocation. When you invoke this skill, it determines which skills should fire next and invokes them automatically. Not just checking for skills — actually invoking them in the right order.
---

# Chain to Downstream Skills

## Overview

**This skill fixes the gap between `using-superpowers` and actual skill invocation.**

`using-superpowers` tells you to "invoke relevant skills" but doesn't say WHICH ones. This skill does.

## The Pattern

When a user gives a task, follow this chain:

### Phase 1: Classify the Task

| Task Type | Pattern | Chain |
|-----------|---------|-------|
| "Build X" / "Create X" / "Make X" | Building | brainstorming → writing-plans → implementation |
| "Fix X" / "Debug X" / "It's broken" | Debugging | systematic-debugging → diagnosing-bugs → fix |
| "Review X" / "Check X" | Review | code-review → requesting-code-review |
| "What is X?" / "How does X work?" | Research | research |
| "Improve X" / "Optimize X" | Refactoring | karpathy-guidelines → code-review |
| "Add a feature to X" | Extension | brainstorming → implementation |
| Any task that ends with "done" / "complete" / "working" | Completion | verification-before-completion |

### Phase 2: Invoke Each Skill in Order

For each skill in the chain:

1. **Load the skill:** Call the skill tool with the skill name
2. **Announce:** "Using [skill] to [purpose]"
3. **Follow the skill exactly:** Do not skip steps, do not modify the procedure
4. **Complete the skill:** Finish all steps before moving to the next

### Phase 3: Verify the Chain

After the last skill in the chain, ask:

- Did I invoke every skill in the chain?
- Did I follow each skill's procedure?
- Did I skip any steps?

If any answer is "no" or "unsure," restart from Phase 1.

## Examples

### Example 1: "Build me a Snake game"

```
Task: "Build me a Snake game"
Type: Building
Chain: brainstorming → writing-plans → implementation

1. [Invoke brainstorming]
   "Using brainstorming to define scope and requirements for Snake game"
   → [Follow brainstorming procedure]
   → [Define what Snake game means: grid, movement, food, collision, scoring]

2. [Invoke writing-plans]
   "Using writing-plans to create implementation plan for Snake game"
   → [Follow writing-plans procedure]
   → [Create plan: constants, snake, food, game loop, controls]

3. [Invoke implementation]
   "Implementing per plan"
   → [Write code per plan]

4. [Invoke verification-before-completion]
   "Using verification-before-completion before claiming done"
   → [Run uv run snake]
   → [Show output]
   → [Only then claim done]
```

### Example 2: "Fix the font crash"

```
Task: "Fix the font crash in Snake game"
Type: Debugging
Chain: systematic-debugging → diagnosing-bugs → fix

1. [Invoke systematic-debugging]
   "Using systematic-debugging to diagnose font crash"
   → [Reproduce: run uv run snake, capture error]
   → [Collect data: pygame version, Python version, platform]
   → [Analyze: circular import in pygame.font]
   → [Verify: pygame-ce works where pygame 2.6.1 doesn't]

2. [Invoke fix]
   → [Apply fix: switch to pygame-ce]

3. [Invoke verification-before-completion]
   "Using verification-before-completion before claiming fix"
   → [Run uv run snake]
   → [Show output]
   → [Only then claim done]
```

### Example 3: "Add WASD controls"

```
Task: "Add WASD controls to Snake game"
Type: Extension
Chain: brainstorming → implementation

1. [Invoke brainstorming]
   "Using brainstorming to define WASD control scope"
   → [W = up, S = down, A = left, D = right]
   → [Update intro text to list all controls]

2. [Invoke implementation]
   → [Add key mappings to event handler]
   → [Update intro text]

3. [Invoke verification-before-completion]
   "Using verification-before-completion before claiming done"
   → [Test each WASD key]
   → [Test direction guards for WASD]
   → [Run uv run snake]
   → [Show output]
   → [Only then claim done]
```

## What This Fixes

| Problem | How Chain Fixes It |
|---------|-------------------|
| Loaded `using-superpowers` but didn't invoke downstream skills | Chain specifies EXACTLY which skills to invoke and in what order |
| Skipped planning and went straight to code | Planning is step 1 of the chain for "build" tasks |
| Didn't verify before claiming done | verification-before-completion is the final step of every chain |
| Didn't check dependency compatibility | brainstorming includes dependency check as a step |
| Didn't define success criteria | brainstorming defines success criteria as a step |

## Red Flags

- You started coding before invoking the first skill in the chain
- You skipped a skill because "it's obvious"
- You invoked a skill but didn't follow its procedure
- You claimed done without running the final verification skill

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I know what to build, no need for brainstorming" | Brainstorming is not about knowing. It's about defining what "done" looks like. |
| "This is simple, I don't need planning" | Simple tasks have the simplest failure modes when unverified. |
| "I'll just run the command at the end" | The verification skill is not just "run the command." It's a structured check. |
| "I invoked brainstorming mentally" | Mental invocation ≠ actual invocation. The skill has procedures you must follow. |
| "The chain is too rigid for complex tasks" | The chain is a starting point. For complex tasks, add more skills to the chain. |
