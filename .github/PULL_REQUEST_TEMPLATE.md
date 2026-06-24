## Problem

Describe the observed problem and the evidence supporting it.

## Change

Describe the smallest chosen change and its intervention classification.

## Verification

List exact commands and results.

```text
python3 -m unittest discover -s tests -v
skills-ref validate skills/code-quality-guardian
npx skills add . --list --yes
```

## Scope

- [ ] The change addresses one concern.
- [ ] No unrelated cleanup is included.
- [ ] No runtime dependency, network access, or mutating script behavior was added.
- [ ] New references or examples are linked from `SKILL.md`.
- [ ] Documentation and changelog are updated when user-visible behavior changes.
- [ ] Release metadata is updated when the supported public version changes.

## Remaining Uncertainty

State unverified assumptions, compatibility limits, or follow-up work.
