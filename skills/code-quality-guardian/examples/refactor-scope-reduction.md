# Refactor Scope Reduction

## User Request

Refactor the whole service layer to make it cleaner.

## Better Response

Do not start with a rewrite. First reduce the request to a safe inspection and proposal:

- identify the service files involved;
- locate tests and public call sites;
- find the most confusing or risky areas;
- propose one or two small refactors;
- explain what should remain out of scope.

## Scope-Limited Plan

1. Inspect service boundaries and conventions.
2. Pick one high-friction file or function.
3. Preserve public interfaces.
4. Add or identify regression coverage if behavior risk exists.
5. Apply one focused refactor.
6. Verify and summarize.

## Follow-Up

If repeated patterns emerge after the first safe change, propose the next increment. Do not convert a broad request into a broad rewrite by default.
