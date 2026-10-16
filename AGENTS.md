# Agent Rules — Never Claim Done Before It Is

## 1. Don't declare "done" until the user-facing command works

The user cares about one thing: does the thing work for them. Imports pass ≠ done. Logic tests pass ≠ done. The entry point must run without crashing.

**Rule:** Before saying anything is "ready" or "working", run the exact command the user would run. If it crashes, it's not done.

```
User says: "build me a snake game"
Wrong: "All logic tests pass ✓"
Right: "uv run snake" → opens a window, shows intro screen
```

## 2. Verify dependencies before building

If the project depends on external libraries, check compatibility first. Don't write 200 lines of code then discover the library has a known bug on your Python version.

**Rule:** On first project setup, before writing any logic:
- Check library versions against your Python version
- Search for known critical bugs (font module, display init, etc.)
- If a known issue exists, use the working alternative immediately

## 3. Test the full flow, not just pieces

Unit tests on isolated logic are fine. But the real test is the entry point — the thing the user runs. If you can't run it in this environment, verify init + event loop + update + render work together without crashing.

**Rule:** At minimum, verify:
1. `import main_module` works
2. The entry function/class initializes without crashing
3. The main loop runs at least one iteration without crashing

## 4. Self-check before claiming completion

Before telling the user something is ready, ask:

- Did I run the exact command the user will run?
- Did I verify the thing starts without errors?
- Did I check for known compatibility issues with my dependencies?
- Would I be embarrassed if the user ran it right now and it crashed?

If any answer is "no" or "yes (embarrassed)", keep working.

## 5. When you can't test display/output, verify no-crash initialization

If you can't show the user the result (no display, no server, no output), at least verify the thing starts cleanly. A game that crashes on init, a web app that crashes on startup, a script that crashes on load — all are "not done".

## 6. If you make a mistake, own it immediately

When the user points out a crash or error:
- Acknowledge the mistake directly
- Fix the root cause, not just the symptom
- Verify the fix with the real command
- Don't say "I tested it" unless you actually tested the thing the user would run
