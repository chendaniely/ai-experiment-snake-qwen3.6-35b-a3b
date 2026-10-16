---
name: pre-coding-checklist
description: Procedural checklist that MUST be completed before writing any code. Not conditional — fires on any coding task. Defines what success looks like before implementation begins.
---

# Pre-Coding Checklist

## Overview

**This skill fires automatically on any coding task.** Not conditional. Not optional.

Before writing a single line of code, complete ALL checklist items. If any item is unanswered, stop and answer it.

## The Checklist

### 1. What is the user-facing command?

Every project has one command the user will run to use it:
- Python: `python main.py` or `uv run app`
- JavaScript: `npm start` or `node index.js`
- Rust: `cargo run`
- Go: `go run .`
- Any: the entry point that starts the application

**If you cannot name this command, you cannot claim the project works.**

### 2. Does the command exist?

- If yes: run it. Show the output.
- If no: create it. Verify it runs (even if it fails). Show the output.

**Record the command and its output. You will need this for the completion checklist.**

### 3. What are the success criteria?

List every way the user will judge success:
- Does the program start without crashing?
- Does the UI render?
- Does the API respond?
- Does the game start and can you play it?
- Does the import work?
- Does the command run?

**Each criterion must be verifiable by running the command or a test.**

### 4. What dependencies are needed?

- List every external dependency
- Check compatibility: does the dependency version work with the Python/Node/Rust version?
- Search for known issues: does the dependency have a bug on this version?
- If a known bug exists, use the working alternative NOW — not after writing code

### 5. What is the minimal viable implementation?

- What is the smallest thing that could possibly work?
- What can be deleted, not added?
- What can use existing code, not new code?
- What can use the standard library, not a dependency?

**Write this down. Every line of code you write that is NOT in this list is a bug waiting to happen.**

## When to Skip

There is NO skipping this checklist. Even if the task seems trivial. Especially if the task seems trivial.

## Red Flags — STOP

- You're about to write code without naming the user-facing command
- You're about to write code without running the command at least once
- You're about to write code without checking dependency compatibility
- You're about to write code without defining success criteria
- You feel "confident" — confidence is not evidence

## Example

**User:** "Build me a Snake game"

**Agent:** "Using pre-coding-checklist. Before I write any code:

1. **User-facing command:** `uv run snake` (defined in pyproject.toml entry point)
2. **Command exists:** Not yet. I'll create it and verify.
3. **Success criteria:**
   - [ ] `uv run snake` starts without crashing
   - [ ] A window opens showing the game
   - [ ] Arrow keys move the snake
   - [ ] Eating food grows the snake
   - [ ] Hitting walls/self triggers game over
   - [ ] Pressing SPACE restarts the game
4. **Dependencies:** pygame + Python 3.14. Known issue: pygame 2.6.1 font circular import on 3.14. Use pygame-ce instead.
5. **Minimal implementation:** Grid-based movement, snake body, food, collision detection, game loop.

Starting implementation."
