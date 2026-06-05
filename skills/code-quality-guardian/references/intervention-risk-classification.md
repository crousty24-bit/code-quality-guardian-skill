# Intervention Risk Classification

Use this reference when the correct intervention level or specialist selection is not obvious.

## Level 1 Local

Choose Level 1 when the change is contained to one layer, preserves public and persistent contracts, introduces no migration or material concurrency/security risk, and has targeted verification.

Decision: `stay local`.

Examples include renaming an unclear local variable, simplifying one function, or fixing a validation branch in one implementation.

## Level 2 Coordinated

Choose Level 2 when one bounded outcome crosses files, layers, transports, or test suites. Coordinate the minimum disciplines needed to keep the shared contract aligned.

Decision: `coordinate with [...]`.

Typical coordination:

| Signal | Coordinate with |
|---|---|
| Multiple implementation steps or files | `incremental-implementation` |
| Bug fix or behavior-sensitive contract | `test-driven-development` |
| Readability refactor across related code | `code-simplification` |

Unknowns are required. State contract differences, missing coverage, or environment limits before editing.

## Level 3 Specialized

Choose Level 3 when a material specialist risk exists, even if the requested outcome sounds local.

Decision: `delegate to [...]`.

| Material risk | Delegate to |
|---|---|
| Security, authentication, authorization | `security-and-hardening` |
| Public API, module boundary, external contract | `api-and-interface-design` |
| Migration or compatibility transition | `deprecation-and-migration` |
| Reproducible failure or complex root cause | `debugging-and-error-recovery` |
| Measurable performance concern | `performance-optimization` |
| Multi-step delivery | `incremental-implementation` |
| Critical behavior or regression protection | `test-driven-development` |

For transaction or concurrency work, use project-native database and framework patterns, coordinate TDD, and add security or API guidance when trust boundaries or contracts are involved.

Unknowns are required. Identify data state, rollback constraints, concurrency assumptions, affected callers, and verification limits as applicable.

## Escalation Rules

- Escalate from Level 1 when inspection reveals another layer, contract, or material risk.
- Escalate from Level 2 when migration, security, concurrency, public API, or complex diagnosis becomes material.
- Do not downgrade solely because the diff is small.
- Do not upgrade solely because many files are generated or mechanically changed.
- Keep the business outcome fixed while adding specialist discipline.

## Suspend Before Editing

Pause implementation when:

- product intent could change whether behavior is defective;
- affected callers or data contracts are unknown;
- a migration lacks a safe treatment for existing data;
- concurrency assumptions are unverified;
- required regression coverage cannot be identified;
- an unknown could change the intervention level.
