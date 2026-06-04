# TypeScript Guidelines

Use this only for TypeScript or typed JavaScript projects.

## Type Contracts

- Strengthen types at boundaries: API inputs, external data, component props, public functions, and persistence layers.
- Avoid `any` unless there is a clear compatibility reason.
- Prefer precise, readable types over generic-heavy abstractions.
- Use existing project validation libraries and schema patterns before introducing new ones.

## Readability

- Let TypeScript infer obvious local variables.
- Name types after domain concepts, not implementation mechanics.
- Avoid duplicating types that can be derived from an existing source of truth.
- Do not introduce advanced type programming unless it removes real risk and remains understandable.

## Refactors

- Preserve exported types and public interfaces unless changing them is part of the task.
- Check call sites before tightening a type.
- Run the project typecheck when available.
- Treat type errors as evidence, not as something to silence with assertions.

## Avoid

- Blanket `as` assertions.
- `// @ts-ignore` without a documented reason.
- Overly generic helpers for one or two call sites.
- Runtime validation gaps at external input boundaries.

