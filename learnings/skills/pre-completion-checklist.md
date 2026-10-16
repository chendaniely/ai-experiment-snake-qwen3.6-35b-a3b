---
name: pre-completion-checklist
description: Procedural checklist that MUST be completed before claiming any work is done. Not conditional. Not optional. Run the entry point, show the output, then claim.
---

# Pre-Completion Checklist

## Overview

**This skill fires automatically before ANY completion claim.** Not conditional. Not optional.

Before saying "Done," "Complete," "Working," "Ready," or any synonym — complete ALL checklist items. If any item is not verified, the work is NOT done.

## The Checklist

### 1. Run the user-facing command

This is the command the user will use. It was defined in the pre-coding-checklist (Step 1).

```
[Run the exact command]
```

**Show the full output. Do not truncate. Do not summarize.**

**If the command crashes, the work is NOT done. Fix it and restart from Step 1.**

### 2. Verify every success criterion

Each criterion was defined in the pre-coding-checklist (Step 3). For each one:

```
[Criterion] → Verified: [how you verified it]
```

**Every criterion must be checked. Not "should be." Not "probably." Checked.**

### 3. Run the test suite (if tests exist)

```
[Run tests]
```

**Show the output. Count: X/Y passed.**

**If any test fails, the work is NOT done.**

### 4. Check for regressions

Did any existing functionality break?
- Run the existing test suite
- Run the existing entry point
- Check that previously-working features still work

### 5. What did you NOT check?

List every thing you did NOT verify:
- "I didn't test edge case X"
- "I didn't test on Y platform"
- "I didn't test Z scenario"

**If this list is empty, you probably missed something. Be honest.**

## When to Stop

If Step 1 fails (the command crashes), stop immediately. Do not proceed to Step 2. Fix the crash, restart from Step 1.

## Red Flags — STOP

- You haven't run the user-facing command
- You're about to say "should work" or "probably works"
- You're about to say "looks good" without running the command
- You're about to claim success without showing evidence
- You're tired and want this to be over — exhaustion is not an excuse

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Tests passed earlier this session" | Run the tests on the current tree. A green run only proves the tree it ran on. |
| "I tested the logic separately" | Logic tests ≠ user-facing behavior. The user runs the command, not the unit test. |
| "It should work" | RUN it. "Should" is not evidence. |
| "I'm confident" | Confidence ≠ evidence. Show the output. |
| "Just this once" | No exceptions. Every claim needs evidence. |
| "The agent said it works" | Verify independently. Agents lie (even when they don't mean to). |
| "Different words so rule doesn't apply" | Spirit over letter. |

## Example

**User:** "Build me a Snake game"

**Agent:** "Using pre-completion-checklist.

1. **Run command:**
   ```
   $ uv run snake
   pygame-ce 2.5.8 (SDL 2.32.10, Python 3.14.3)
   [Window opens, shows intro screen]
   ```
   Output: Window opens, shows intro. No crash. ✓

2. **Success criteria:**
   - [x] `uv run snake` starts without crashing → Shown above
   - [x] A window opens showing the game → Shown above
   - [ ] Arrow keys move the snake → Need to test
   - [ ] Eating food grows the snake → Need to test
   - [ ] Hitting walls/self triggers game over → Need to test
   - [ ] Pressing SPACE restarts the game → Need to test

3. **Test suite:**
   ```
   $ uv run python -c "..."
   ALL TESTS PASSED ✓
   ```

4. **Regressions:** N/A (new project)

5. **Not checked:**
   - I didn't test IJKL controls in the window (tested via event simulation)
   - I didn't test on Linux (tested on macOS)
   - I didn't test what happens with rapid key presses

Not all criteria verified. Continuing verification."
