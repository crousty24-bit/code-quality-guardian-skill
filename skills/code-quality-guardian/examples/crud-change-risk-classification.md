# CRUD Change Risk Classification

## User Request

Make this small update/delete behavior change.

## Classification

```text
Intervention class: Level 2 Coordinated or Level 3 Specialized
Decision: coordinate with [test-driven-development] or delegate to [api-and-interface-design, security-and-hardening, deprecation-and-migration] when the material risk exists.
Reason: a small CRUD request can affect persistence, permissions, migrations, idempotency, callers, or public response shape.
Unknowns: affected data state, authorization rules, validation contracts, existing callers, and rollback constraints.
Verification: regression coverage for the changed CRUD behavior, plus affected API or persistence checks.
Stop condition: the requested business behavior changes without widening data contracts or unrelated workflows.
```

## Better Response

Do not classify CRUD work as local by default. First inspect whether the change touches:

- persisted data or migrations;
- authorization or ownership rules;
- validation and error shape;
- idempotency or transaction behavior;
- API responses, events, or external callers.

If these risks are absent and targeted verification exists, stay local. If they are present, keep the business outcome bounded while coordinating or delegating only the relevant specialist discipline.

## Non-Goal

Do not redesign the data model or API unless the requested behavior cannot be made safe within the existing contract.
