# Testing Guidelines

Use tests to protect behavior, not to decorate a change.

## Choose Relevant Checks

- Run the narrowest test that covers the changed behavior.
- Add or update regression tests when fixing a bug.
- Use integration tests when confidence depends on module interaction.
- Use unit tests when logic is isolated and behavior is easy to express.
- Avoid tests that mirror implementation details without protecting user-visible or contract behavior.

## Before Refactoring

- Look for existing tests around the target code.
- If coverage is missing and the refactor is risky, add or recommend a characterization test first.
- If tests cannot be added within scope, state the risk explicitly.

## Verification Honesty

- Report exact commands run.
- Report failures and partial verification.
- Do not say "tests pass" unless tests were executed and passed.
- If no project test command exists, say so and describe the nearest manual or static check performed.
- Do not rerun unchanged checks just to sound safer; run checks after relevant changes and report what they prove.
- Distinguish proof, signal, and unverified assumption.

## Practical Order

1. Targeted tests for changed behavior.
2. Typecheck or compile checks when contracts changed.
3. Lint when style or static quality may be affected.
4. Build when packaging, bundling, or integration may be affected.
