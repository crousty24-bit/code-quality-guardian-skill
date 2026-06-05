# Coordinated Multi-Transport Validation

## Situation

The same date and time contract is implemented in JavaScript, TypeScript, and Rust transports. All accept impossible dates and out-of-range times.

## Classification

```text
Intervention class: Level 2 Coordinated
Decision: coordinate with [test-driven-development, incremental-implementation]
Reason: one bounded validation contract must remain identical across three transports and test suites.
Unknowns: whether all transports use the same error messages and boundary rules.
Verification: failing contract tests first, then targeted JS/TS and Rust suites.
Stop condition: all transports reject the same invalid values without changing valid inputs or public messages.
```

Do not create a validation framework merely because the rule is duplicated. Coordinate the tests and smallest matching changes.
