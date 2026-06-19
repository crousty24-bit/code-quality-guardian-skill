# Monolithic Logic Decomposition

## User Request

Split this long function into smaller functions.

## Classification

```text
Intervention class: Level 1 Local or Level 2 Coordinated
Decision: stay local if the extraction is contained; coordinate with [code-simplification] if callers, contracts, or tests span files.
Reason: a long function is an inspection signal, not proof that decomposition is safer.
Unknowns: whether the function has stable sub-responsibilities, independent test value, or hidden caller contracts.
Verification: existing targeted tests, or the smallest regression check covering the preserved behavior.
Stop condition: extract only the named responsibility that improves comprehension or reduces change risk.
```

## Better Response

Inspect the function before splitting it. Identify whether it contains:

- a stable named responsibility;
- a repeated business rule;
- a separately testable contract;
- state that would become harder to follow if moved.

Extract only the part with a clear name and verified benefit. Keep sequential logic together when splitting would only create parameter plumbing or hide the control flow.

## Non-Goal

Do not create a file, class, or helper layer just because the function is long. Size is a reason to inspect, not a reason to fragment.
