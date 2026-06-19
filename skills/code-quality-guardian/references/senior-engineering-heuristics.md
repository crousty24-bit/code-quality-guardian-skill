# Senior Engineering Heuristics

Use these heuristics as judgment tools, not doctrine. Guardian should arbitrate between principles instead of applying them mechanically.

## DRY

Apply DRY when repeated code expresses the same concept, business rule, validation rule, or contract.

Avoid DRY when code merely looks similar, when callers are likely to diverge, or when extraction would hide important local context behind a vague helper.

## SOLID

Use SOLID principles when they reduce verified coupling, protect a real contract, or make the current change safer.

Avoid introducing interfaces, layers, factories, or dependency boundaries only to satisfy a principle. A simple project convention is often safer than an imported architecture.

## Clean Code

Improve comprehension locally through clearer names, explicit control flow, cohesive functions, and comments for non-obvious constraints.

Avoid style churn when the existing code is understandable, conventional for the project, and not part of the verified risk.

## CRUD Discipline

Escalate CRUD work when create, read, update, or delete behavior touches persistence, authorization, validation, migrations, idempotency, data backfills, transactions, or public response shape.

Stay local only when the change preserves data contracts, has no material permission or migration risk, and has targeted verification.

## Monolith vs Decomposition

Decompose when the extracted part has a stable name, coherent responsibility, reused behavior, independent test value, or reduces a verified change risk.

Keep logic together when the flow is linear and clearer in one place, when extraction spreads local state across files, when parameter plumbing grows, or when the split is motivated only by size.

## Guardian Decision

Prefer the principle that reduces the current verified risk with the smallest behavioral surface. If a principle would widen the diff, introduce new contracts, or require broad caller changes, classify the intervention higher or reject the change.
