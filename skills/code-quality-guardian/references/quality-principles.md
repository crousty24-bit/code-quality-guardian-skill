# Quality Principles

Use these principles as heuristics, not dogma. Prefer the principle that best reduces risk in the current codebase.

## Orchestration Before Specialization

- Start by deciding how much intervention the task actually needs.
- Separate local business scope from implementation risk.
- Classify the intervention as Level 1 Local, Level 2 Coordinated, or Level 3 Specialized.
- Keep this skill as the scope and judgment layer.
- Use specialized skills for deep review, simplification, testing, security, performance, or API design only when the evidence requires that depth.
- Coordinate specialist disciplines without transferring or broadening the requested scope.
- Do not copy specialized checklists into a general quality response.
- If a specialized concern is only adjacent, mention it as follow-up instead of expanding the current change.

## Simplicity

- Apply KISS: choose the simplest solution that solves the current problem.
- Apply YAGNI: do not build abstractions, options, or extension points for hypothetical future needs.
- Prefer boring, obvious code over clever code.
- Avoid decorative patterns that make the code look engineered without reducing real complexity.

## Readability

- Choose names that reveal intent.
- Keep functions focused, but do not split code into tiny fragments that obscure flow.
- Prefer explicit control flow when implicit behavior would force readers to guess.
- Add comments only for non-obvious why, constraints, tradeoffs, or external requirements.
- Match surrounding style before applying general preferences.

## Maintainability

- Keep responsibilities clear.
- Reduce coupling when it directly makes future changes safer.
- Remove duplication only when it is truly the same concept, not merely similar syntax.
- Prefer local improvements over global rewrites.
- Make dependencies visible and understandable.

## Minimal Diff

- Touch only files needed for the task.
- Keep unrelated cleanup out of the change.
- Separate behavior changes from refactors when possible.
- Preserve public contracts unless the user explicitly asks to change them.

## Project Conventions

- Inspect existing structure before adding files or modules.
- Reuse established helpers, test patterns, error handling, naming, and formatting.
- Treat consistency with the codebase as a quality requirement.
- Do not impose an architecture that the project does not already support.
