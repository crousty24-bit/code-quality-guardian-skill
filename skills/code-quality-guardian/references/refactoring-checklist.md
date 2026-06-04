# Refactoring Checklist

Use this before non-trivial refactors.

## Before Changing

- Identify the behavior that must stay the same.
- Find callers, tests, and adjacent code.
- Check whether the requested improvement is local or cross-cutting.
- Determine whether missing tests make the refactor risky.
- State the smallest safe refactor.
- Ask whether this is real simplification or agent churn.

## During The Refactor

- Keep one refactor intention at a time.
- Preserve names and boundaries that are already clear.
- Prefer simplifying branches, extracting obvious concepts, or deleting duplication over introducing a framework.
- Avoid moving files unless location is part of the problem.
- Avoid broad renames unless they materially improve comprehension.

## After Changing

- Run targeted tests or the nearest available verification.
- Run typecheck, lint, or build when the change touches contracts or compilation boundaries.
- Inspect the diff for accidental formatting churn.
- Summarize remaining debt instead of solving unrelated problems.

## Stop Conditions

Stop and reassess when:

- The diff grows beyond the original issue.
- A new abstraction needs extensive explanation.
- You need to change many callers for a cosmetic improvement.
- Verification is unavailable and behavior risk is high.
- The refactor mainly makes the agent's preferred style replace the project's style.
