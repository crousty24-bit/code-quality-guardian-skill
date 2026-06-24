# Contributing

Code Quality Guardian is an experimental Agent Skill. Contributions should strengthen intervention discipline without turning the skill into a general-purpose quality framework.

## Before Opening A Change

1. Read `AGENTS.md` and `skills/code-quality-guardian/SKILL.md`.
2. Search existing issues for related proposals.
3. Keep one concern per issue and pull request.
4. Explain which observed behavior or field-test evidence motivates the change.

Changes based only on abstract clean-code preference are unlikely to be accepted.

## Development Setup

Requirements:

- Python 3.10 or newer;
- Node.js with `npx`;
- Git.

Clone the repository and run:

```bash
python3 -m unittest discover -s tests -v
npx skills add . --list --yes
```

Validate the skill with the official reference validator when available:

```bash
skills-ref validate skills/code-quality-guardian
```

## Naming Conventions

- Repository: `code-quality-guardian-skill`.
- Installable skill and directory: `code-quality-guardian`.
- Skill names and Markdown resource names: lowercase kebab-case.
- Python modules and functions: lowercase snake_case.
- Test files: `test_*.py`.
- Examples and references must be linked directly from `SKILL.md`.

Do not rename the repository or installable skill without a migration plan.

## Scope Rules

- Keep `SKILL.md` under 500 lines.
- Keep framework-specific detail in conditional references or scripts.
- Do not copy long checklists from specialized skills.
- Do not add network access, project rewrites, auto-fix behavior, or third-party runtime dependencies to evidence scripts.
- Do not add another skill until field evidence proves a distinct standalone workflow.
- Keep evaluation notes outside the published package.

## Tests

Behavioral script changes require regression tests using `unittest` and temporary directories.

Documentation or skill-contract changes require static tests when an invariant can be checked deterministically, such as:

- linked resources exist;
- metadata matches the release;
- only one skill is discoverable;
- the script set has not expanded accidentally;
- no tracked bytecode exists.

Run the full suite before submitting:

```bash
python3 -m unittest discover -s tests -v
```

## Release Preparation

Before a beta release:

- update the version in `skills/code-quality-guardian/SKILL.md` and matching metadata tests;
- update `README.md`, `CHANGELOG.md`, `SECURITY.md`, and issue placeholders when the public supported version changes;
- keep release notes focused on user-visible behavior, scope discipline, script safety, compatibility, and verification;
- tag only the final release commit on `main` after the release merge is validated.

## Pull Requests

Include:

- the problem and evidence;
- the smallest chosen change;
- tests and exact commands run;
- compatibility or migration concerns;
- intentional non-changes;
- remaining uncertainty.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
