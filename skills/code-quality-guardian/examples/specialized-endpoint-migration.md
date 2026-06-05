# Specialized Endpoint And Migration Change

## Situation

Public mutation endpoints bypass domain rules. Fixing them requires removing routes, adding a unique database constraint, handling existing duplicates, and serializing concurrent reward updates.

## Classification

```text
Intervention class: Level 3 Specialized
Decision: delegate to [security-and-hardening, api-and-interface-design, deprecation-and-migration, test-driven-development]
Reason: the bounded outcome crosses authorization, public contracts, persistent data, and concurrency.
Unknowns: existing duplicate rows, callers relying on removed routes, rollback behavior, and untested concurrent requests.
Verification: route tests, migration tests on duplicate fixtures, constraint tests, regression tests, and project security checks.
Stop condition: bypass routes are unavailable, existing data migrates safely, uniqueness is enforced, and reward updates cannot lose writes.
```

Code Quality Guardian retains scope control. Specialist guidance must not turn the change into a broader security or architecture rewrite.
