# Claude Code vs OpenCode Skill Comparison

## Overview

This document compares the skill ecosystems available in Claude Code vs OpenCode, focusing on skills that would have prevented the Snake game failure chain.

## Installation Paths

| Harness | Skill Location | Discovery Mechanism |
|---------|---------------|-------------------|
| **Claude Code** | `~/.claude/plugins/cache/claude-plugins-official/*/skills/` | Plugin cache, auto-loaded |
| **Claude Code** | `~/.claude/skills/` | Symlinks to user skills repo |
| **OpenCode** | Loaded in system prompt (hardcoded list) | System prompt injection |
| **OpenCode** | `~/.agents/skills/*/SKILL.md` | Filesystem discovery |

## Skills That Would Have Prevented the Snake Failure

### verification-before-completion

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | obra/superpowers | Same (via system prompt) |
| **Version** | 7.0.0 (plugin cache) | Loaded (version unknown) |
| **Location** | `~/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/verification-before-completion/SKILL.md` | System prompt |
| **Discovery** | Plugin auto-discovers | Pre-loaded in system prompt |
| **Invoked?** | Would have needed user to invoke or chain skill | **Loaded but not invoked** |
| **File Content** | 120 lines, 5-step gate | Same content (inferred) |
| **Install** | `npx skills add obra/superpowers --skill=verification-before-completion` | Already available (via system prompt) |

### finishing-a-development-branch

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | obra/superpowers | Same (via system prompt) |
| **Version** | 7.0.0 | Loaded (version unknown) |
| **Location** | `~/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/finishing-a-development-branch/SKILL.md` | System prompt |
| **Invoked?** | Would have needed to be invoked | **Loaded but not invoked** |

### requesting-code-review

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | obra/superpowers | Same (via system prompt) |
| **Version** | 7.0.0 | Loaded (version unknown) |
| **Location** | `~/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/requesting-code-review/` | System prompt |
| **Files** | SKILL.md + code-reviewer.md | SKILL.md only (inferred) |
| **Invoked?** | Would have needed to be invoked | **Loaded but not invoked** |

### brainstorming

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | obra/superpowers | Same (via system prompt) |
| **Version** | 7.0.0 | Loaded (version unknown) |
| **Location** | `~/.claude/plugins/cache/claude-plugins-official/superpowers/7.0.0/skills/brainstorming/SKILL.md` | System prompt |
| **Invoked?** | Would have needed to be invoked | **Loaded but not invoked** |

### karpathy-guidelines

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | multica-ai/andrej-karpathy-skills | Same (via system prompt) |
| **Version** | Available in Claude Code plugin | Loaded in system prompt |
| **Location** | `~/.claude/plugins/cache/` (plugin) | System prompt |
| **Invocation** | Ambient (active every response) | Ambient (active every response) |
| **Followed?** | **Loaded but not followed** | **Loaded but not followed** |
| **Install** | `npx skills add multica-ai/andrej-karpathy-skills --skill=karpathy-guidelines` | Already available (via system prompt) |

### ponytail

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | DietrichGebert/ponytail | Same (via system prompt) |
| **GitHub Stars** | 106.8K | Same |
| **Invocation** | Active every response | Active every response |
| **Followed?** | **Loaded but didn't prevent this failure** (different failure mode) | **Same** |
| **Install** | `npx skills add dietrichgebert/ponytail` | Already available (via system prompt) |

### test-driven-development

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Repository** | obra/superpowers | Same (via system prompt) |
| **Version** | 7.0.0 | Loaded (version unknown) |
| **Invoked?** | Would have needed to be invoked | **Loaded but not invoked** |

### Matt Pocock Skills

| Skill | Claude Code | OpenCode |
|-------|-------------|----------|
| **code-review** | Plugin v1.3.1 | Installed in `~/.agents/skills/matt-pocock-code-review/` |
| **diagnosing-bugs** | Plugin v1.3.1 | Installed in `~/.agents/skills/matt-pocock-diagnosing-bugs/` |
| **domain-modeling** | Plugin v1.3.1 | Installed in `~/.agents/skills/matt-pocock-domain-modeling/` |
| **research** | Plugin v1.3.1 | Installed in `~/.agents/skills/matt-pocock-research/` |

**Note:** Matt Pocock skills are NOT in OpenCode's system prompt. They were installed manually into `~/.agents/skills/` during this session.

## Skills Available in Both

| Skill | Claude Code Source | OpenCode Availability |
|-------|-------------------|----------------------|
| brainstorming | obra/superpowers | System prompt |
| verification-before-completion | obra/superpowers | System prompt |
| finishing-a-development-branch | obra/superpowers | System prompt |
| requesting-code-review | obra/superpowers | System prompt |
| receiving-code-review | obra/superpowers | System prompt |
| systematic-debugging | obra/superpowers | System prompt |
| test-driven-development | obra/superpowers | System prompt |
| diagnosing-superpowers | obra/superpowers | System prompt |
| dispatching-parallel-agents | obra/superpowers | System prompt |
| executing-plans | obra/superpowers | System prompt |
| subagent-driven-development | obra/superpowers | System prompt |
| writing-plans | obra/superpowers | System prompt |
| writing-skills | obra/superpowers | System prompt |
| using-git-worktrees | obra/superpowers | System prompt |
| using-superpowers | obra/superpowers | System prompt |
| karpathy-guidelines | multica-ai | System prompt |
| ponytail | DietrichGebert | System prompt |

**Total Superpowers skills in both:** 16
**Total Karpathy skills in both:** 1 (karpathy-guidelines)
**Total Ponytail skills in both:** 1 (ponytail + 5 variants)

## Skills Only in Claude Code (via Plugins)

| Skill | Source | Install Command |
|-------|--------|----------------|
| code-review (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=code-review` |
| diagnosing-bugs (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=diagnosing-bugs` |
| domain-modeling (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=domain-modeling` |
| research (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=research` |
| grill-with-docs (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=grill-with-docs` |
| improve-codebase-architecture (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=improve-codebase-architecture` |
| tdd (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=tdd` |
| to-spec (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=to-spec` |
| to-tickets (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=to-tickets` |
| triage (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=triage` |
| wayfinder (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=wayfinder` |
| wait-what (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=wait-what` |
| setup-matt-pocock-skills (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=setup-matt-pocock-skills` |
| ask-matt (Matt Pocock) | mattpocock/skills | `npx skills add mattpocock/skills --skill=ask-matt` |

## Skills Only in OpenCode (via System Prompt)

OpenCode loads skills from its system prompt. These are not independently installed — they're injected by the harness. The OpenCode system prompt lists these skills:

| Skill | Source | Notes |
|-------|--------|-------|
| academy-guide | Anthropic Academy | Training materials |
| algorithmic-art | p5.js art | Creative |
| alt-text | R package alt text | Domain-specific |
| brand-guidelines | Anthropic brand | Design |
| brand-yml | Shiny/Quarto branding | Domain-specific |
| built-in-browser | Claude desktop browser | Tool-specific |
| canvas-design | Visual design | Creative |
| cavecrew (builder, investigator, reviewer) | CaveCrew | Code navigation |
| caveman (commit, compress, help, review, stats) | Style | Communication |
| chrome-browser | Chrome extension | Tool-specific |
| clothing-inventory | Obsidian vault | Domain-specific |
| critical-code-reviewer | Review | Code quality |
| deep-research | Research | Information gathering |
| deploy-to-connect | Posit Connect | Domain-specific |
| describe-design | Architecture docs | Documentation |
| diagnosing-bugs | Matt Pocock | **Installed manually** |
| domain-modeling | Matt Pocock | **Installed manually** |
| email-digest | Thunderbird mail | Domain-specific |
| external-app-review | Review | Code quality |
| find-skills | Skills CLI | Discovery |
| ggsql | SQL visualization | Domain-specific |
| git-guardrails-claude-code | Git safety | Safety |
| google-workspace | Google apps | Integration |
| graphify | Knowledge graphs | Information |
| grilling | Interviews | Communication |
| i-have-adhd | ADHD formatting | Communication |
| import-memory | Memory migration | Integration |
| internal-comms | Internal communications | Communication |
| karpathy-guidelines | Karpathy | **Loaded in system prompt** |
| maintainers-decline | Open source | Communication |
| mcp-builder | MCP servers | Development |
| migrate-to-shoehorn | TypeScript types | Development |
| morning | Daily brief | Productivity |
| ootd | Outfit inventory | Domain-specific |
| openCode | OpenCode itself | Meta |
| orchestration | Multi-agent | Development |
| pdf | PDF processing | File handling |
| plaud-* (browse, digest, export, find, followup, read, shared) | Plaud | Domain-specific |
| ponytail (audit, debt, gain, help, review) | Ponytail | **Loaded in system prompt** |
| pr, pr-create | GitHub PRs | Development |
| pr-threads-address, pr-threads-resolve | GitHub PRs | Development |
| product-search | Product research | Information |
| prototype | Design prototypes | Development |
| quarto-authoring | Quarto | Domain-specific |
| r-* (cli, cli-app, cran-extrachecks, cran-status, lifecycle, mirai, package-development, testthat, tidyverse-style) | R ecosystem | Domain-specific |
| receiving-code-review | Superpowers | **Loaded in system prompt** |
| release-post | R packages | Domain-specific |
| report | Bug reports | Communication |
| requesting-code-review | Superpowers | **Loaded in system prompt** |
| research | Matt Pocock | **Installed manually** |
| reviewing-testing | Testing | Code quality |
| scaffold-exercises | Exercise creation | Education |
| setup-pre-commit | Git hooks | Development |
| shiny-* (bslib, bslib-theming) | Shiny | Domain-specific |
| skill-creator | Skill creation | Meta |
| slack-gif-creator | GIF creation | Creative |
| systematic-debugging | Superpowers | **Loaded in system prompt** |
| tdd | Superpowers | **Loaded in system prompt** |
| theme-factory | Design themes | Creative |
| using-git-worktrees | Superpowers | **Loaded in system prompt** |
| using-superpowers | Superpowers | **Loaded in system prompt** |
| verification-before-completion | Superpowers | **Loaded in system prompt** |
| web-artifacts-builder | Web artifacts | Development |
| webapp-testing | Testing | Development |
| wizard | Interactive wizards | Development |
| writing-for-agents | Agent writing | Documentation |
| writing-plans | Superpowers | **Loaded in system prompt** |
| writing-skills | Superpowers | **Loaded in system prompt** |
| xlsx | Spreadsheets | File handling |

## Key Differences

### 1. Loading Mechanism

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **How skills arrive** | Plugin system (`npx skills add`) | System prompt injection |
| **Discovery** | Filesystem scanning | Hardcoded in system prompt |
| **Updates** | Plugin updates via `npx skills update` | Requires harness update |
| **Custom skills** | `~/.claude/skills/` symlinks | `~/.agents/skills/` directories |

### 2. Skill Invocation

| Aspect | Claude Code | OpenCode |
|--------|-------------|----------|
| **Invocation method** | `skill` tool with skill name | `skill` tool with skill ID |
| **Auto-trigger** | Based on description matching | Based on description matching |
| **Chain support** | via `using-superpowers` | via `using-superpowers` |
| **Ambient skills** | Plugin-based (always on) | System prompt (always on) |

### 3. Coverage Gap

| Category | Claude Code | OpenCode | Gap |
|----------|-------------|----------|-----|
| Superpowers (obra) | 16 skills | 16 skills | **None** |
| Karpathy | Available | 1 skill | **Partial** |
| Ponytail | Available | 6 skills | **None** |
| Matt Pocock | 13 skills | 4 skills | **9 skills missing** |
| Domain-specific (R, Quarto, Shiny) | 17 skills | 17 skills | **None** |
| Integration (Plaud, Google, Posit) | Available | Available | **None** |
| Creative (art, design, GIF) | Available | Available | **None** |
| Meta (skill-creator, find-skills) | Available | Available | **None** |

### 4. What This Means

**OpenCode has all the Superpowers skills that would have prevented this failure.** The issue was invocation, not availability.

**Claude Code has Matt Pocock skills that OpenCode lacks.** These are domain-specific (code-review, diagnosing-bugs) and were manually installed during this session.

**The gap is not in the prevention skills — it's in the invocation discipline.**
