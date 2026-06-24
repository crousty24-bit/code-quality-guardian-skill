# Code Quality Guardian - Project Vision

## Premise

Code Quality Guardian exists because AI agents often produce too much code, too quickly, with too much certainty.

The target risk is not only "bad code". The target risk is poorly disciplined agentic intervention:

- adding unnecessary files;
- creating decorative abstractions;
- importing an architecture that is foreign to the project;
- adding dependencies without justification;
- refactoring too broadly;
- changing behavior without saying so;
- claiming verification without evidence.

## MVP Vision

The skill must remain a lightweight orchestrator for intervention discipline.

It should help the agent:

- observe before acting;
- limit the diff;
- preserve existing behavior;
- respect the codebase conventions;
- decide when a specialized practice is genuinely necessary;
- report verification honestly.

The central promise is: change less, but better.

## What This Skill Is Not

Code Quality Guardian is not:

- an exhaustive clean-code guide;
- a copy of `code-review-and-quality`;
- a copy of `code-simplification`;
- a complete framework for review, security, performance, tests, or architecture;
- a framework-specific skill;
- a pretext for expanding every task into a global redesign.

Specialized skills remain the best references for their domains. Code Quality Guardian decides when to invoke or draw from them.

## Conceptual References

The project's Obsidian notes are the initial source of truth for vision and positioning.

The following skills are references for validated patterns, not content to copy:

- `code-review-and-quality` for review axes, change size, and dependency discipline;
- `code-simplification` for preserving behavior and avoiding churn;
- `incremental-implementation` for small verifiable increments;
- `test-driven-development` for bug fixes and critical behavior;
- `debugging-and-error-recovery` for evidence-based diagnostics;
- `api-and-interface-design`, `security-and-hardening`, `performance-optimization`, and `git-workflow-and-versioning` for specialized concerns.

## Evolution Rules

Every evolution of the skill must follow these rules:

- strengthen the distinction against AI overproduction;
- stay short and actionable;
- avoid copying specialized checklists;
- prefer a delegation rule over an exhaustive section;
- keep `SKILL.md` compact;
- move long details into `references/` only if they materially change agent behavior;
- add only read-only detection scripts, using the Python standard library, with no network access, rewrites, or execution of project commands;
- do not claim a stable publication before short examples, field tests, and real feedback.

## Field Phase 1 Lessons

The first campaign across five repositories confirms the desired behavior:

- the agent observes before modifying;
- changes remain limited and verified;
- scripts are interpreted as signals, not verdicts;
- delegation remains conditional on a real need;
- no massive refactor or unjustified architecture addition was observed.

It also identified three limits to correct:

- the initial scripts favored JavaScript conventions and detected Rails poorly;
- some diagnostics confused a local convention with product intent;
- the methodology does not yet prove a causal gain against a true baseline without the skill.

The added Rails/Ruby and Rust/Tauri support remains targeted at field evidence. The project must not claim universal compatibility.

## Field Phase 2 Lessons

The second campaign confirms:

- effective Rails/Ruby and Rust/Tauri detection on real projects;
- scope discipline, limited diffs, and honest verification;
- improved diagnostic precision and better handling of product intent;
- no over-architecture despite multi-layer interventions.

It also shows that the binary decision `stay local` or `delegate` is insufficient. A local business outcome can require multi-file coordination or specialized delegation when security, migrations, persistent contracts, or concurrency are material.

The skill now distinguishes:

- `Level 1 Local`: contained intervention with low execution risk;
- `Level 2 Coordinated`: bounded outcome requiring several disciplines or layers;
- `Level 3 Specialized`: material risk requiring dedicated expertise.

Code Quality Guardian keeps scope control at every level. It orchestrates specialized skills without copying their checklists.

## Possible Future Skills After Field Validation

Do not create these skills now. Keep them in the backlog until field validation shows an autonomous workflow that is useful on its own and distinct from `code-quality-guardian`.

- `agent-change-auditor`: audit an agent-generated diff or PR to detect scope creep, unexpected files, missing verification, and added dependencies.
- `codebase-risk-scout`: map risk areas before intervention from read-only signals.
- `verification-discipline`: frame the verification strategy and distinguish proof, signal, and unverified hypothesis.
- `refactor-scope-control`: refuse or reduce overly broad refactors when a local intervention is enough.

## Current Beta

The repository is prepared for beta `0.2.0-beta.1` after two field validation phases, scope and guardrail improvements, and a fix related to the Snyk security audit.

The MIT license is defined. Scripts remain strictly read-only, cannot execute the commands they detect, and must treat detected paths, names, sources, and commands as untrusted data.

A stable post-beta version still requires:

- a comparative campaign with real control passes without the skill installed or activated;
- at least one reserve repository not used during development;
- separate tracking for false positives, diff size, and verification actually executed;
- validation of the three intervention levels on distinct scenarios;
- validation of public installation from GitHub.
