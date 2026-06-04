# Code Quality Guardian

Status: `Unreleased` MVP draft.

`code-quality-guardian` is an agent skill for pragmatic code-quality work. It keeps coding agents from overproducing code: inspect first, make small justified changes, preserve behavior, follow project conventions, and verify honestly.

This is not a general clean-code handbook or a complete review framework. It is a lightweight intervention-discipline orchestrator for audits, reviews, targeted refactors, readability improvements, complexity reduction, testing guidance, and maintainability work.

See `AGENTS.md` for the project vision, MVP boundaries, and evolution rules.

## Installation

Once published on GitHub, install or inspect it with:

```bash
npx skills add owner/repo --list
npx skills add owner/repo --skill code-quality-guardian
```

For local validation before publication:

```bash
npx skills add ./code-quality-guardian --list
```

Replace `owner/repo` with the final GitHub repository.

## Structure

```text
skills/
  code-quality-guardian/
    SKILL.md
    agents/
      openai.yaml
    references/
      quality-principles.md
      refactoring-checklist.md
      testing-guidelines.md
      typescript-guidelines.md
      security-checklist.md
    scripts/
      project_conventions_probe.py
      scan_file_lengths.py
      scan_function_lengths.py
      run_quality_checks.py
      risk_summary.py
    examples/
      bad-agent-overproduction.md
      good-limited-intervention.md
      refactor-scope-reduction.md
    templates/
      .gitkeep
```

## Usage

Use the skill when asking an agent to:

- audit code quality;
- review a file or pull request;
- perform a targeted refactor;
- improve readability or reduce complexity;
- strengthen tests or TypeScript contracts;
- identify obvious security risks during code changes.

The skill should not push an agent toward broad rewrites, new dependencies, framework-specific rules, or architecture changes without evidence.

## Evidence Scripts

The bundled scripts are read-only helpers. They use Python 3 standard library only, do not access the network, and do not rewrite files.

They produce evidence for the agent to interpret:

- `project_conventions_probe.py` detects package manager, scripts, configs, and likely frameworks.
- `scan_file_lengths.py` finds long files for inspection.
- `scan_function_lengths.py` finds long functions with simple heuristics.
- `run_quality_checks.py` lists or runs detected quality commands; default mode only lists.
- `risk_summary.py` aggregates read-only signals into an inspection summary.

Script output can be Markdown or JSON.

## Current Scope

- `SKILL.md` contains the core operating procedure.
- `references/` contains short conditional guides.
- `examples/` contains short behavior examples.
- `scripts/` contains read-only evidence helpers.
- The skill delegates deep concerns to specialized skills instead of duplicating them.

## Not Doing Yet

- No new skills in this repository until field validation proves a separate workflow is needed.
- No stable release claim before real project validation.
- No auto-fix, no code rewriting, no formatter execution, and no network-dependent scripts.

## Validation

Validate the skill with:

```bash
/mnt/c/Users/allen/.codex/skills/.system/skill-creator/scripts/quick_validate.py /home/allen/mes_projets/code-quality-guardian/skills/code-quality-guardian
```
