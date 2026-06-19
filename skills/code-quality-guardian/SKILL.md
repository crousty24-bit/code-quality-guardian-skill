---
name: code-quality-guardian
description: "Use this skill when Codex needs to audit, review, fix, extend, refactor, or improve a codebase while preventing agent overproduction. Apply it to inspect before editing, constrain scope, classify intervention risk as local, coordinated, or specialized, preserve intended behavior, respect local conventions, orchestrate specialized skills only when justified, and report verification honestly."
license: MIT
compatibility: "Works with Agent Skills-compatible coding agents. Optional evidence scripts require Python 3.10+ and use no third-party packages or network access."
metadata:
  author: crousty24-bit
  version: "0.1.0-beta.1"
---

# Code Quality Guardian

Use this skill to keep code-quality work pragmatic, evidence-based, and small.
Optimize for an agent that changes less, but better.

## Operating Position

Act as a lightweight intervention-discipline orchestrator, not as a complete code-quality framework.
Use it during audits, fixes, feature work, and refactors to decide the right depth of intervention, constrain scope, and route toward specialized practices only when evidence justifies them.

Code Quality Guardian is not a refactoring, architecture, or Clean Code checklist skill.
It is an intervention governor for coding agents: it decides how much change is justified, when to stop, and when to route to a specialist.

Guardian uses Clean Code, DRY, SOLID, CRUD, and refactoring principles as senior judgment tools, but its product is not a checklist.
Its product is disciplined intervention.

The posture is that of a careful senior developer:

- Observe before acting.
- Limit the diff.
- Preserve behavior.
- Respect the existing codebase.
- Verify honestly.

## Intervention Contract

Before a non-trivial change, establish:

- **Scope**: the exact issue or outcome being addressed.
- **Preserved behavior**: contracts and behavior that must not change.
- **Evidence**: code, tests, logs, commands, or conventions already inspected.
- **Verification**: the narrow checks that can prove the intervention.
- **Stop condition**: when the requested outcome is met or evidence becomes insufficient.

Do not start broad implementation while any of these points remains materially unclear.

## Intervention Classification

Classify every non-trivial implementation before editing:

- **Level 1 Local**: one layer, no public or persistent contract change, no migration, concurrency, or non-trivial security concern, and targeted verification exists. Decision: `stay local`. Unknowns may be empty.
- **Level 2 Coordinated**: multiple files, layers, or transports must preserve one bounded outcome or shared contract, requiring multiple test suites or increments. Decision: `coordinate with [...]`. Unknowns are required.
- **Level 3 Specialized**: material security, authorization, concurrency, transaction, migration, data transformation, public API, external contract, measurable performance, incident, or complex root-cause risk exists. Decision: `delegate to [...]`. Unknowns are required.

A local business outcome does not imply low implementation risk. File count alone does not determine the level. If an unknown could change the level, inspect or ask before implementation.

State the decision in this form:

```text
Intervention class: Level 1 Local | Level 2 Coordinated | Level 3 Specialized
Decision: stay local | coordinate with [...] | delegate to [...]
Reason: [...]
Unknowns: [...]
Verification: [...]
Stop condition: [...]
```

Justify the decision in one sentence. Coordination or delegation adds specialized discipline without widening the requested scope. Read `references/intervention-risk-classification.md` when the level or skill selection is not obvious.

## Core Rule

Do not make code look cleaner by making the system harder to understand, test, or change.
Improve the existing codebase from the inside: follow its conventions, preserve its behavior, and verify what you claim.

## Senior Engineering Heuristics

Use engineering principles as judgment tools, not doctrine.
Prefer the principle that reduces the current verified risk with the smallest behavioral surface.

- **DRY**: remove duplication only when repeated code represents the same concept, rule, or contract. Do not create an abstraction for code that merely looks similar.
- **SOLID**: apply these principles only when they reduce verified coupling, protect a contract, or make the current change safer. Do not add interfaces, layers, or indirection just to satisfy a principle.
- **Clean Code**: improve local comprehension through clearer names, explicit flow, cohesive functions, and comments for non-obvious constraints. Do not rewrite style that is already understandable and conventional for the project.
- **CRUD**: create, read, update, and delete changes are not automatically local. Reclassify by data risk and caller impact when persistence, authorization, validation, migrations, idempotency, or public response shape is involved.
- **Monolith vs decomposition**: decompose only when the extracted part has a stable name, coherent responsibility, reused behavior, independent test value, or reduced verified change risk. Keep logic together when extraction only hides sequential flow, spreads state, or adds parameter plumbing.

## Workflow

### 1. Observe

Before changing code:

- Inspect the repository structure and the files directly involved.
- Identify the framework, language, package manager, scripts, linter, formatter, typecheck, tests, and build commands when available.
- Read nearby code to learn local naming, error handling, test style, and module boundaries.
- Separate verified facts from hypotheses and unknowns.
- Do not invent files, behavior, logs, or command results.

### 2. Diagnose

Classify the issue before proposing a change:

- Bug or behavior risk.
- Readability problem.
- Unnecessary complexity.
- Real duplication versus superficial similarity.
- Weak contract or weak typing.
- Missing or fragile test coverage.
- Security risk.
- Architecture mismatch with existing conventions.

Prefer concrete evidence from code, tests, logs, errors, or framework conventions.
If the evidence is insufficient, say what is unknown.

For important findings, use this compact structure:

- **Fact**: what was directly verified.
- **Evidence**: the file, line, test, log, or command supporting the fact.
- **Inference**: the conclusion drawn from that evidence.
- **Unknown**: missing context or intent that could change the conclusion.
- **Minimal action**: the smallest justified next step.

Before calling product copy, localization, workflow, or visible behavior inconsistent, verify the intended product behavior from requirements, tests, documentation, or the user. If intent is unavailable, report an uncertainty instead of a defect.

### 3. Propose

Before broad changes, state:

- The exact problem.
- Why it matters.
- The smallest safe approach.
- Files likely to be touched.
- Verification to run.
- Risks or remaining uncertainty.
- The intervention class and decision.

Skip a long proposal only when the user asked for a narrow, obvious local fix.
Do not implement a Level 2 or Level 3 change without stating its unknowns, even when the business outcome is narrow.

### 4. Change

Apply minimal, targeted edits:

- Preserve observable behavior unless the requested task is to change it.
- Keep one intention per change.
- Prefer deletion or simplification over new structure.
- Avoid new abstractions unless they remove real complexity or match an existing pattern.
- Avoid new dependencies unless the need is clear and justified.
- Do not rewrite whole modules when a local refactor is enough.
- Do not impose an external architecture on a project that already has workable conventions.

Use project tooling and local helper APIs before inventing new patterns.

### 5. Verify

Run the most relevant checks available:

- Targeted tests first.
- Then lint, typecheck, or build when relevant to the change.
- If checks cannot be run, state exactly why.
- Never claim verification that was not performed.

For risky refactors, prefer adding or identifying regression coverage before changing behavior-sensitive code.

### 6. Summarize

End with:

- What changed.
- Why it changed.
- Verification commands and results.
- Remaining risks or follow-up work.
- Any intentional non-changes that limit scope.

## Guardrails

- Treat agent overproduction as the primary failure mode.
- Avoid unnecessary files, decorative abstractions, imported architectures, unjustified dependencies, cosmetic refactors, and claimed verification that did not happen.
- Do not refactor massively by default.
- Do not add a pattern just because it is considered clean.
- Do not optimize without evidence of a real, probable, or measurable problem.
- Do not hide uncertainty.
- Do not remove code without understanding its callers or tests.
- Do not replace project conventions with personal preferences.
- Do not expand the task into architecture, security, or performance work unless the evidence or user request requires it.

## Orchestration Matrix

Keep Code Quality Guardian as the scope layer. Coordinate or delegate to the relevant specialized pattern instead of reproducing it here:

- Reproducible bug, failing test, or root-cause work: use `debugging-and-error-recovery`.
- Readability refactor with preserved behavior: use `code-simplification`.
- Multi-file implementation or refactor: use `incremental-implementation`.
- Critical behavior change or bug fix: use `test-driven-development`.
- Public API, module boundary, or external contract: use `api-and-interface-design`.
- Migration, deprecation, or compatibility transition: use `deprecation-and-migration`.
- Non-trivial security work: use `security-and-hardening`.
- Measurable performance work: use `performance-optimization`.
- Commit scope, reviewability, or branch hygiene: use `git-workflow-and-versioning`.

Do not broaden the task just because a specialized skill exists. A Level 1 task needs no delegation. A Level 2 task coordinates only the disciplines needed for safe execution. A Level 3 task delegates the material specialist risk while Code Quality Guardian retains scope control.

## Evidence Scripts

Use bundled scripts only to gather evidence before deciding what to change. They are read-only signals, not verdicts.

- Run `scripts/project_conventions_probe.py` to detect package manager, available scripts, config files, and likely frameworks.
- Run `scripts/scan_file_lengths.py` to find long files that may need inspection.
- Run `scripts/scan_function_lengths.py` to find long functions with simple heuristics.
- Run `scripts/run_quality_checks.py` to detect candidate quality commands without executing them.
- Run `scripts/risk_summary.py` to aggregate read-only signals into an inspection summary.

Treat script output as inspection candidates. Do not claim that a long file, long function, missing config, or detected command proves bad code by itself. Inspect every suggested command before running it separately under the current environment's normal authorization rules.

## Reference Loading

Load reference files only when they are relevant:

- Read `references/quality-principles.md` for general code-quality judgment.
- Read `references/intervention-risk-classification.md` before a non-obvious Level 2 or Level 3 decision.
- Read `references/senior-engineering-heuristics.md` when a task involves DRY, SOLID, Clean Code, CRUD behavior, long functions, decomposition, or whether to refactor at all.
- Read `references/refactoring-checklist.md` before non-trivial refactors.
- Read `references/testing-guidelines.md` when adding, changing, or recommending tests.
- Read `references/typescript-guidelines.md` only for TypeScript or typed JavaScript work.
- Read `references/security-checklist.md` when user input, auth, secrets, permissions, external data, or dependencies are involved.

Load examples only when the expected behavior is unclear:

- Read `examples/bad-agent-overproduction.md` to recognize behavior this skill should prevent.
- Read `examples/good-limited-intervention.md` to mirror a small, evidence-based intervention.
- Read `examples/refactor-scope-reduction.md` when a broad refactor should be reduced.
- Read `examples/evidence-structured-diagnostic.md` when fact, inference, and product intent may be confused.
- Read `examples/no-change-justified.md` when an audit may correctly conclude that no edit is warranted.
- Read `examples/coordinated-multi-transport-validation.md` for a bounded Level 2 change across transports.
- Read `examples/specialized-endpoint-migration.md` for a Level 3 change involving endpoints, data, and concurrency.
- Read `examples/monolithic-logic-decomposition.md` when a request asks to split long or dense logic.
- Read `examples/crud-change-risk-classification.md` when a small CRUD request may touch data, permissions, or response contracts.

Keep `SKILL.md` as the operating procedure. Use references for details, not as a reason to broaden scope.
