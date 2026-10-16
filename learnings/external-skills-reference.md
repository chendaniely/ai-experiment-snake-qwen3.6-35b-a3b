# External Skills Reference — Skills That Would Have Helped

This documents every external skill and resource found during research that could have prevented the Snake game failure chain.

## Skills That Would Have Prevented This

### 1. verification-before-completion

| Field | Value |
|-------|-------|
| **Source** | Superpowers (obra) |
| **Repository** | https://github.com/obra/superpowers |
| **GitHub Stars** | 196.7K |
| **Claude Code Plugin** | `claude-plugins-official/superpowers` v7.0.0 |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | **Critical** |

**What it does:** 5-step gate before any completion claim: Identify, Run, Read, Verify, Claim. "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE."

**How it would have prevented the failure:** The agent would have been forced to run `uv run snake` before claiming done. The first "Done." statement would have been blocked.

**Why it wasn't invoked:** The skill was loaded but never invoked. Its trigger ("about to claim work is complete") was not recognized as having fired because the skill wasn't part of the workflow.

**Install command:**
```bash
npx skills add obra/superpowers --skill=verification-before-completion
```

---

### 2. finishing-a-development-branch

| Field | Value |
|-------|-------|
| **Source** | Superpowers (obra) |
| **Repository** | https://github.com/obra/superpowers |
| **Claude Code Plugin** | `claude-plugins-official/superpowers` v7.0.0 |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | Yes |

**What it does:** Verifies tests pass, presents merge/PR/keep options, cleans up worktree. "Test gate is not optional and cannot be skipped."

**How it would have helped:** Would have enforced a completion gate. The agent couldn't declare the branch "finished" without passing tests AND running the entry point.

**Why it wasn't invoked:** The agent never reached the "finishing" phase because it claimed done prematurely. The skill fires at the end of a development cycle, but the agent never got there.

**Install command:**
```bash
npx skills add obra/superpowers --skill=finishing-a-development-branch
```

---

### 3. requesting-code-review

| Field | Value |
|-------|-------|
| **Source** | Superpowers (obra) |
| **Repository** | https://github.com/obra/superpowers |
| **Claude Code Plugin** | `claude-plugins-official/superpowers` v7.0.0 |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | Yes |

**What it does:** Dispatches a code reviewer subagent to catch issues before they cascade. "Review early, review often."

**How it would have helped:** Would have forced a self-review before claiming done. The agent would have had to review its own work against the plan and standards.

**Why it wasn't invoked:** The agent self-reviewed inline (informally) instead of invoking the skill.

**Install command:**
```bash
npx skills add obra/superpowers --skill=requesting-code-review
```

---

### 4. brainstorming

| Field | Value |
|-------|-------|
| **Source** | Superpowers (obra) |
| **Repository** | https://github.com/obra/superpowers |
| **Claude Code Plugin** | `claude-plugins-official/superpowers` v7.0.0 |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | Yes |

**What it does:** Structured brainstorming to define scope, requirements, and edge cases before building.

**How it would have helped:** Would have defined "press SPACE to start" as a requirement. The intro screen would have been built as part of the plan, not as an afterthought.

**Why it wasn't invoked:** `using-superpowers` says "build X → brainstorming first" but the agent didn't follow this chain.

**Install command:**
```bash
npx skills add obra/superpowers --skill=brainstorming
```

---

### 5. karpathy-guidelines

| Field | Value |
|-------|-------|
| **Source** | Andrej Karpathy / Multica |
| **Repository** | https://github.com/multica-ai/andrej-karpathy-skills |
| **GitHub Stars** | 60K+ |
| **Claude Code Plugin** | `claude-plugins-official` (available) |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | Yes |

**What it does:** 4 principles for AI coding: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. "Don't tell it what to do, give it success criteria and watch it go."

**How it would have helped:** Would have forced the agent to define success criteria (run `uv run snake`) before writing any code.

**Why it wasn't invoked:** Loaded as "ambient every response" but not followed. Ambient skills are suggestions, not gates.

**Install command:**
```bash
npx skills add multica-ai/andrej-karpathy-skills --skill=karpathy-guidelines
```

---

### 6. ponytail

| Field | Value |
|-------|-------|
| **Source** | Dietrich Gebert |
| **Repository** | https://github.com/DietrichGebert/ponytail |
| **GitHub Stars** | 106.8K |
| **Claude Code Plugin** | `claude-plugins-official/frontend-design` (frontend-design variant) |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | No (different failure mode) |

**What it does:** Lazy senior dev mode. "The best code is the code never written." Constrains code volume, not verification.

**Why it wouldn't have helped:** Ponytail constrains HOW MUCH code you write, not WHETHER YOU VERIFY it works. Different failure mode.

---

### 7. Matt Pocock code-review

| Field | Value |
|-------|-------|
| **Source** | Matt Pocock |
| **Repository** | https://github.com/mattpocock/skills |
| **Claude Code Plugin** | `claude-plugins-official/mattpocock-skills` v1.3.1 |
| **OpenCode Availability** | Installed in `~/.agents/skills/` as `matt-pocock-code-review` |
| **Would Have Helped** | Yes (post-hoc) |

**What it does:** Two-axis review (Standards + Spec) via parallel sub-agents. "Review the changes since a fixed point."

**How it would have helped:** Would have caught spec mismatches (intro screen missing, no start instructions) after the fact. Not preventive, but would have caught issues before the user saw them.

**Install command:**
```bash
npx skills add mattpocock/skills --skill=code-review
```

---

### 8. Matt Pocock diagnosing-bugs

| Field | Value |
|-------|-------|
| **Source** | Matt Pocock |
| **Repository** | https://github.com/mattpocock/skills |
| **Claude Code Plugin** | `claude-plugins-official/mattpocock-skills` v1.3.1 |
| **OpenCode Availability** | Installed in `~/.agents/skills/` as `matt-pocock-diagnosing-bugs` |
| **Would Have Helped** | Post-hoc only |

**What it does:** 6-phase diagnosis loop with feedback loops. "Build the right feedback loop, and the bug is 90% fixed."

**How it would have helped:** Would have caught the root cause faster after the crash was reported. Not preventive.

**Install command:**
```bash
npx skills add mattpocock/skills --skill=diagnosing-bugs
```

---

### 9. test-driven-development

| Field | Value |
|-------|-------|
| **Source** | Superpowers (obra) |
| **Repository** | https://github.com/obra/superpowers |
| **Claude Code Plugin** | `claude-plugins-official/superpowers` v7.0.0 |
| **OpenCode Availability** | Loaded (in system prompt) |
| **Would Have Helped** | Partially |

**What it does:** Red-green-refactor cycle. "Write failing test, watch it fail, write minimal code, watch it pass."

**How it would have helped:** Would have written a test that runs `uv run snake` before the game code existed. The test would have failed, then the agent would have fixed it.

**Why it wasn't fully effective:** The agent wrote logic tests but not end-to-end tests. TDD without entry-point tests is incomplete.

**Install command:**
```bash
npx skills add obra/superpowers --skill=test-driven-development
```

---

## Research Resources

### AI Coding Agent Verification Practices

| Resource | URL | Key Insight |
|----------|-----|-------------|
| Zima Store: Best AI Agent Skills for Code Quality | https://shop.zimaspace.com/blogs/tech-ai-hub/best-10-ai-agent-skills-for-code-quality-review-2026 | "If your bigger problem is AI-generated code that looks correct but has not been properly verified, codex-grade-coding is the stronger companion" |
| Firecrawl: Best Codex Skills | https://www.firecrawl.dev/blog/best-codex-skills | Karpathy Guidelines encodes 4 behavioral rules; 144K stars |
| SkillsLLM: agents-best-practices | https://skillsllm.com/skill/agents-best-practices | 2.4K stars, provider-neutral agent skill |
| GitHub: iliaal/ai-skills | https://github.com/iliaal/ai-skills | "AI coding agents skip planning, claim 'done' without verifying" |
| Vonage: Beyond Vibe Coding | https://developer.vonage.com/en/blog/beyond-vibe-coding-best-practices-2026 | "A Stop hook can block the agent from prematurely declaring victory" |
| Red Hat: Building Skills | https://next.redhat.com/2026/07/28/building-skills-for-ai-agents-pitfalls-and-best-practices | Skills are modular plugins with SKILL.md format |
| Substack: All You Need to Know About SKILL.md | https://aishwaryasrinivasan.substack.com/p/all-you-need-to-know-about-skillmd | Open standard at agentskills.io, 280K+ skills indexed by Feb 2026 |
| Medium: My LLM Coding Workflow | https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e | Addy Osmani's workflow: brainstorm → spec → plan → code → review |
| AddyOsmani: Good Spec for AI Agents | https://addyosmani.com/blog/good-spec | "Encourage self-verification: have the agent verify its work against the spec automatically" |
| LinkedIn: 8 Rules to Improve AI Coding Agent | https://www.linkedin.com/posts/svpino_8-rules-to-improve-your-ai-coding-agent-activity-7387144776581705728-DKtK | "Dependency checks — prevent your agent from suggesting insecure libraries based on outdated training data" |
| Codacy: Govern AI Coding Agents | https://blog.codacy.com/how-to-govern-ai-coding-agents-across-development-teams | "Treat MCP servers and agent tool access as dependencies with an approval process" |
| SRI: AI-Generated Code Is Not Reproducible | https://www.csl.sri.com/users/gehani/papers/RAI-2026.Dependencies.pdf | "31.7% failure rate and 13.5x dependency gap" in LLM-generated code |
| Minitap: AI Coding Agents Who's Testing | https://www.minitap.ai/magazine/ai-coding-agents-automated-testing | "Agent that only sees the file open in front of it will miss how a change ripples through the rest of the app" |
| Augment Code: 80% Problem | https://www.augmentcode.com/guides/the-80-percent-problem-ai-agents-technical-debt | "API misuse at 20.41% of annotated hallucination instances" |
| Sourcegraph: Automated Code Review | https://sourcegraph.com/blog/automated-code-review-tools | AI reviewers catch context-dependent issues simple lint rules miss |
| Vellum: Top 12 AI Developer Tools | https://www.vellum.ai/blog/best-ai-agents-for-coding-2026 | Overview of coding agents in 2026 |

### Ponytail-Specific Resources

| Resource | URL | Key Insight |
|----------|-----|-------------|
| ToKnow.ai: Ponytail | https://toknow.ai/posts/ponytail-lazy-senior-dev-skill-ai-agents-less-code | "Cut new code by about 54%, up to 94%" |
| Flavio Copes: Deep Dive into Ponytail | https://flaviocopes.com/ponytail | "Lazy does not mean careless here" |
| SkillsLLM: Ponytail | https://skillsllm.com/skill/ponytail | 157K stars |
| YouTube: Ponytail | https://www.youtube.com/watch?v=2xuFcmUAQUc | Demo of Ponytail vs default Claude Code |
| Hacker News: Ponytail | https://news.ycombinator.com/item?id=48527946 | Community discussion on Ponytail |
| JetBrains: Ponytail Tested | https://blog.jetbrains.com/ai/2026/07/ponytail-skill-claude-tested | Independent benchmark of Ponytail |

### Superpowers-Specific Resources

| Resource | URL | Key Insight |
|----------|-----|-------------|
| GitHub: obra/superpowers | https://github.com/obra/superpowers | 196.7K stars, most complete multi-agent development framework |
| Heyuan110: Superpowers Deep Dive | https://www.heyuan110.com/posts/ai/2026-02-01-superpowers-deep-dive | "The skills system: the heart of Superpowers" |
| Verdent: What Is Superpowers | https://www.verdent.ai/guides/what-is-superpowers-ai-coding-framework | "Each feature development session gets its own git worktree" |
| DEV Community: Most Popular AI Coding Skills | https://dev.to/aws/the-most-popular-ai-coding-skills-right-now | "Best skills are becoming workflow contracts rather than just prompt snippets" |

### Karpathy-Specific Resources

| Resource | URL | Key Insight |
|----------|-----|-------------|
| GitHub: multica-ai/andrej-karpathy-skills | https://github.com/multica-ai/andrej-karpathy-skills | 60K stars, 4 principles |
| Skillselion: Karpathy Guidelines | https://skillselion.com/guides/karpathy-guidelines-skill-claude-code | "Most-searched Claude Code skill in the catalog" |
| Nic's Notes: Karpathy Skills | https://notes.nicolasdeville.com/github/karpathy-skills | Installation guide, 4 principles explained |
| YouTube: Karpathy Skill Fixed Claude Code | https://www.youtube.com/watch?v=EsgUfrwsV5A | "Just fixed Claude Code's Biggest Problem" |
| Developer Digest: Karpathy Skills | https://www.developersdigest.tech/blog/github-trending-andrej-karpathy-skills-2026-04-21 | "60,000 developers bookmarked" |
| Medium: Karpathy × Superpowers | https://watchsound.medium.com/andrej-karpathy-superpowers-skills-6c1808cdaa58 | "Reinforcement across existing skills" |
| Level Up Coding: 4 Lines Every CLAUDE.md | https://levelup.gitconnected.com/the-4-lines-every-claude-md-needs-2717a46866f6 | "One GitHub repo. 60,000 stars. No dependencies, no API, no build step." |

### Matt Pocock-Specific Resources

| Resource | URL | Key Insight |
|----------|-----|-------------|
| GitHub: mattpocock/skills | https://github.com/mattpocock/skills | Official skills repository |
| AIHero: The /code-review Skill | https://www.aihero.dev/skills-code-review | Matt's two-axis review skill |
| SkillsLLM: code-review | https://skillsllm.com/skill/code-review | 2.1K installs |

### AI Coding Agent Research Papers

| Resource | URL | Key Insight |
|----------|-----|-------------|
| SRI: AI-Generated Code Is Not Reproducible | https://www.csl.sri.com/users/gehani/papers/RAI-2026.Dependencies.pdf | "31.7% failure rate" in LLM-generated code reproduction |
| ISSTA 2025: LLM Code Hallucinations | https://arxiv.org/abs/* | "API knowledge conflicts, parameter errors, deprecated API usage at 20.41%" |
| Journal of Systems and Software: Non-functional Quality | N/A | "Instability of optimizing NFQCs through prompts in practical settings" |

### OpenCode / Agent Skills Ecosystem

| Resource | URL | Key Insight |
|----------|-----|-------------|
| Agent Skills Standard | https://agentskills.io | Open standard, published Dec 2025 |
| skills.sh | https://skills.sh | 283K+ skills indexed by Feb 2026 |
| Anthropic Academy: Verification Skills | https://academy.claude.com/courses/claude-code-in-action/verification-skills | "A verification skill removes that dependency" |
