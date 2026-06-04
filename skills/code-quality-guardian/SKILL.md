---
name: code-quality-guardian
description: "Use this skill when Codex needs to audit, review, refactor, or improve code quality while avoiding agent overproduction: inspect the codebase first, preserve behavior, make the smallest justified change, respect existing conventions, add or recommend relevant tests, and verify honestly. Use for codebase audits, PR reviews, readability improvements, complexity reduction, TypeScript cleanup, targeted refactors, and maintainability work."
---

# Code Quality Guardian

Use this skill to keep code-quality work pragmatic, evidence-based, and small.
Optimize for an agent that changes less, but better.

## Operating Position

Act as a lightweight intervention-discipline orchestrator, not as a complete code-quality framework.
Use this skill to decide the right depth of intervention, constrain scope, and route toward specialized practices only when the evidence justifies them.

The posture is that of a careful senior developer:

- Observe before acting.
- Limit the diff.
- Preserve behavior.
- Respect the existing codebase.
- Verify honestly.

## Core Rule

Do not make code look cleaner by making the system harder to understand, test, or change.
Improve the existing codebase from the inside: follow its conventions, preserve its behavior, and verify what you claim.

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

### 3. Propose

Before broad changes, state:

- The exact problem.
- Why it matters.
- The smallest safe approach.
- Files likely to be touched.
- Verification to run.
- Risks or remaining uncertainty.

Skip a long proposal only when the user asked for a narrow, obvious local fix.

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

## Delegation Matrix

Use this skill to keep the intervention small. When a deeper concern is real, follow the relevant specialized pattern instead of reproducing it here:

- Reproducible bug, failing test, or root-cause work: use `debugging-and-error-recovery`.
- Readability refactor with preserved behavior: use `code-simplification`.
- Multi-file implementation or refactor: use `incremental-implementation`.
- Critical behavior change or bug fix: use `test-driven-development`.
- Public API, module boundary, or external contract: use `api-and-interface-design`.
- Non-trivial security work: use `security-and-hardening`.
- Measurable performance work: use `performance-optimization`.
- Commit scope, reviewability, or branch hygiene: use `git-workflow-and-versioning`.

Do not broaden the task just because a specialized skill exists. Delegate only when the code, risk, or user request calls for it.

## Evidence Scripts

Use bundled scripts only to gather evidence before deciding what to change. They are read-only signals, not verdicts.

- Run `scripts/project_conventions_probe.py` to detect package manager, available scripts, config files, and likely frameworks.
- Run `scripts/scan_file_lengths.py` to find long files that may need inspection.
- Run `scripts/scan_function_lengths.py` to find long functions with simple heuristics.
- Run `scripts/run_quality_checks.py --list` to list quality commands without executing them; use `--run` only when command execution is appropriate.
- Run `scripts/risk_summary.py` to aggregate read-only signals into an inspection summary.

Treat script output as evidence for triage. Do not claim that a long file, long function, missing config, or failed command proves bad code by itself.

## Reference Loading

Load reference files only when they are relevant:

- Read `references/quality-principles.md` for general code-quality judgment.
- Read `references/refactoring-checklist.md` before non-trivial refactors.
- Read `references/testing-guidelines.md` when adding, changing, or recommending tests.
- Read `references/typescript-guidelines.md` only for TypeScript or typed JavaScript work.
- Read `references/security-checklist.md` when user input, auth, secrets, permissions, external data, or dependencies are involved.

Load examples only when the expected behavior is unclear:

- Read `examples/bad-agent-overproduction.md` to recognize behavior this skill should prevent.
- Read `examples/good-limited-intervention.md` to mirror a small, evidence-based intervention.
- Read `examples/refactor-scope-reduction.md` when a broad refactor should be reduced.

Keep `SKILL.md` as the operating procedure. Use references for details, not as a reason to broaden scope.
