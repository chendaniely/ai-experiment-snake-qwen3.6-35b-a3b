# Retrospective Review — With Procedural Skills Installed

## What Would Have Happened Differently

If pre-coding-checklist, pre-completion-checklist, and chain-to-downstream had been active:

### Step 1: Pre-Coding Checklist (would have fired immediately)

The task "build a snake game" is a coding task. Pre-coding-checklist fires.

I would have been forced to:

1. **Name the user-facing command** — `uv run snake`
2. **Run it** — fail (not built yet), but record the failure mode
3. **List success criteria** — game starts, window opens, controls work, food eaten, game over triggered, restart works
4. **Check dependency compatibility** — pygame + Python 3.14 = known font circular import bug → use pygame-ce
5. **Define minimal viable implementation** — grid movement, snake body, food, collision, game loop

**Result:** Step 4 would have caught the pygame 2.6.1 font bug BEFORE writing any code. I would have added `pygame-ce` to the project from the start, not discovered it mid-stream.

### Step 2: Chain to Downstream

Task classification: "build a snake game" = **Building**

Chain: `brainstorming → writing-plans → implementation → verification-before-completion`

I would have invoked:
1. `brainstorming` — defined scope: grid size, snake length, speed, controls, food, score, game over, restart
2. `writing-plans` — created plan: constants module, snake module (body, movement, collision), food module (placement, growth), game module (loop, input, rendering)
3. `implementation` — wrote code per plan
4. `verification-before-completion` — ran `uv run snake` before claiming done

**Result:** The brainstorming step would have defined "press SPACE to start" as a requirement. The intro screen would have been built as part of the plan, not as an afterthought.

### Step 3: Implementation With Self-Checks

During implementation, the pre-completion-checklist would have fired after each logical grouping:

After writing snake body: run a self-check test.
After writing food: run a self-check test.
After writing game loop: run `uv run snake` to verify the entry point.

**Result:** The collision logic bug would have been caught when testing the snake module, not when the user ran the full game. The body orientation bug would have been caught when testing movement.

### Step 4: Pre-Completion Checklist (before claiming done)

Before saying "Done":

1. **Run `uv run snake`** — would have shown the window opens and the intro screen displays
2. **Verify every criterion:**
   - [x] `uv run snake` starts without crashing
   - [x] Window opens showing the game
   - [ ] Arrow keys move the snake → NEED TO TEST
   - [ ] Eating food grows the snake → NEED TO TEST
   - [ ] Hitting walls triggers game over → NEED TO TEST
   - [ ] Pressing SPACE restarts → NEED TO TEST
3. **Not checked:** rapid key presses, IJKL controls (not yet implemented), high score persistence

**Result:** I would have identified the missing verifications BEFORE saying "Done." I would have tested the controls, found the WASD/IJKL gap, and added them before declaring completion.

## What the User Could Have Said Differently

The user's original prompt:
> "i want you to use python + pygame with uv and uv venvs in this project. i want you to just go ahead and without any more prompts from me make your best attempt at a game of snake. you may initialize a git repo here and commit along the way. but make something where you review and think of your own solutions to things. I'm looking for a way to play snake on this machine. document how to start things up as well."

### What Was Clear

- Technology: Python + Pygame + uv + venvs
- Goal: Playable Snake game
- Freedom: "review and think of your own solutions"
- Documentation: "document how to start things up"

### What Was Unclear (and Could Have Helped)

The prompt didn't specify:
- What "done" looks like (a window opens? you can play for 5 minutes? it handles all edge cases?)
- That the game needs to be immediately playable (no tutorial, no learning curve)
- That the user expects to run a single command and play
- That the user is on Python 3.14 (which has known pygame compatibility issues)

### How the User Could Have Prompted Better

**Option 1: Add a completion criterion**
> "Build a playable Snake game. When it's done, I should be able to run `uv run snake`, see the game, and control it with arrow keys. No crash, no errors."

This would have triggered the pre-completion-checklist's Step 1: "Run `uv run snake`." The user explicitly stated what done looks like.

**Option 2: Add a verification requirement**
> "Build a playable Snake game. Before you say it's done, run the game and show me it works. Don't just say tests pass — run the actual game."

This directly addresses the failure mode. It tells the agent: the verification step is part of the task, not optional.

**Option 3: Add a dependency check**
> "Build a playable Snake game. Check that pygame works with Python 3.14 before you start."

This catches the compatibility issue at Step 1 of the pre-coding-checklist.

**Option 4: Add a user-experience requirement**
> "Build a playable Snake game. When I run it, I should immediately understand how to play — no guessing, no trial and error."

This would have triggered the brainstorming step to include: "intro screen with instructions" as a requirement, not an afterthought.

### The Best Prompt

Combining all of the above:

> "Build a playable Snake game using Python + Pygame with uv.
> 
> When it's done, I should be able to run `uv run snake`, see the game window open, and control it with arrow keys to eat food and grow. No crashes, no errors.
> 
> Check that pygame works with Python 3.14 before you start. If there's a compatibility issue, use an alternative.
> 
> Before you say it's done, run the game and show me it works. Don't just say tests pass.
> 
> Make sure the user immediately understands how to play — include an intro screen or instructions.
> 
> Initialize a git repo and commit along the way. Think through your own solutions."

This prompt:
- Defines the user-facing command (`uv run snake`)
- Defines success criteria (window opens, controls work, no crashes)
- Requires dependency check before coding
- Requires running the game before claiming done
- Requires user-friendly UX (intro screen)
- Still gives the agent freedom on implementation details

## Key Takeaways

### For the User (Prompting)

1. **Name the user-facing command.** "I should be able to run `uv run snake`" is better than "document how to start things up."
2. **Define what done looks like.** "No crashes, no errors, controls work" is better than "make your best attempt."
3. **Require running the entry point.** "Before you say it's done, run the game and show me" is better than hoping the agent tests it.
4. **State the environment.** "Python 3.14" would have triggered a dependency check.

### For the Agent (With Procedural Skills)

1. **Pre-coding-checklist catches dependency issues** before writing code.
2. **Chain-to-downstream forces brainstorming** which defines requirements upfront.
3. **Pre-completion-checklist forces running the entry point** before claiming done.
4. **Self-checks during implementation** catch logic bugs early.

### For the Skills (Design)

1. **Procedural > Conditional.** "Always do X before Y" beats "use when X."
2. **Chain > Isolation.** Skills should fire in sequence, not independently.
3. **Evidence > Assertions.** "Show the output" beats "should work."
4. **Gates > Suggestions.** "Must complete" beats "should try."

## Would This Have Fixed the Snake Game?

Let's trace through what would have happened:

1. **Pre-coding-checklist:**
   - User-facing command: `uv run snake` ✓
   - Run it: fails (not built), record failure ✓
   - Success criteria listed ✓
   - Dependency check: pygame + Python 3.14 → font bug → use pygame-ce ✓ (would have fixed Attempt 1)
   - Minimal implementation defined ✓

2. **Chain to downstream:**
   - Brainstorming → scope defined: intro screen, controls, food, collision, score, game over ✓ (would have fixed Attempt 2)
   - Writing plans → architecture defined ✓
   - Implementation → code written per plan ✓

3. **Self-checks during implementation:**
   - After writing snake module: test movement, collision → catch body orientation bug ✓ (would have fixed Attempt 3)
   - After writing game loop: run `uv run snake` → verify entry point works ✓

4. **Pre-completion-checklist:**
   - Run `uv run snake` → show window opens ✓
   - Verify every criterion:
     - [x] `uv run snake` starts without crashing
     - [x] Window opens
     - [ ] Arrow keys work → TEST BEFORE CLAIMING (would have caught that WASD was missing)
     - [ ] Food eating works → TEST
     - [ ] Game over works → TEST
     - [ ] Restart works → TEST
   - List what's not checked: nothing (all verified) ✓

**Verdict:** With the procedural skills installed, the Snake game would have been built correctly the first time. The pygame compatibility issue would have been caught before coding. The missing intro screen would have been included in the plan. The body orientation bug would have been caught during self-testing. The incomplete feature set would have been caught during pre-completion verification.

The game would have been delivered with WASD and IJKL controls (because the brainstorming step would have included "multiple control schemes" as a reasonable requirement, and the pre-completion checklist would have verified all controls work).
