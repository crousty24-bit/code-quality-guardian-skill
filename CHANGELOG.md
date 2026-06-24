# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Comparative Phase 3 field testing against a true baseline without the skill.
- Additional compatibility evidence from previously unseen repositories.

## [0.2.0-beta.1] - 2026-06-24

### Added

- Senior engineering heuristics for DRY, SOLID, Clean Code, CRUD risk, and monolith decomposition decisions.
- Examples for CRUD risk classification and long-logic decomposition.
- Centralized Markdown rendering helpers for safer display of untrusted repository-derived values.
- Regression coverage for hostile paths, function names, detected commands, and script read-only behavior.

### Changed

- Clarified that Code Quality Guardian is an intervention governor, not a refactoring, architecture, or Clean Code checklist.
- Strengthened intervention-risk guidance for local business outcomes that still cross persistence, authorization, migrations, contracts, or concurrency.
- Expanded script detection and scanning support for Rails/Ruby and Rust/Tauri evidence.
- Updated CI dependency pins for the GitHub Actions workflow.

### Fixed

- Neutralized Markdown output from evidence scripts so repository-controlled paths, names, sources, and detected commands remain observation data instead of actionable instructions.
- Reduced false confidence around detected project conventions by adding explicit safety notes to script output.

## [0.1.0-beta.1] - 2026-06-05

### Added

- Lightweight intervention-discipline workflow for coding agents.
- Three-level intervention classification: Local, Coordinated, and Specialized.
- Scope-preserving orchestration guidance for specialist skills.
- Conditional references for quality, refactoring, testing, security, TypeScript, and intervention risk.
- Field-derived examples for local, multi-transport, no-change, and specialized interventions.
- Read-only Python evidence scripts with Markdown and JSON output.
- Targeted project detection for JavaScript/TypeScript, Python, Rails/Ruby, and Rust/Tauri.
- Standard-library regression and package-structure tests.
- Public contribution, support, security, issue, pull-request, and CI documentation.

### Changed

- Quality-command support is detection-only and never executes project commands.
- Diagnostics distinguish facts, evidence, inference, unknowns, and minimal action.
- Public documentation now explains installation, usage, updates, limitations, and beta status.

### Fixed

- NestJS detection through `@nestjs/core`.
- Python pytest and Ruff false positives from generic `pyproject.toml` files.
- Rails/Ruby and Rust/Tauri convention and command detection.
- Scanning support for Ruby, ERB, and Rust files and functions.

### Removed

- Tracked Python bytecode and empty placeholder directories from the distributed skill.

[Unreleased]: https://github.com/crousty24-bit/code-quality-guardian-skill/compare/0.2.0-beta.1...HEAD
[0.2.0-beta.1]: https://github.com/crousty24-bit/code-quality-guardian-skill/compare/0.1.0-beta.1...0.2.0-beta.1
[0.1.0-beta.1]: https://github.com/crousty24-bit/code-quality-guardian-skill/tree/0.1.0-beta.1
