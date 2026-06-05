# Evidence-Structured Diagnostic

## Situation

A bilingual interface contains two English labels while nearby text changes with the selected language.

## Diagnostic

- **Fact**: the two labels remain in English in both language modes.
- **Evidence**: the component uses fixed English strings while adjacent labels use the localization map.
- **Inference**: the labels may be inconsistent with the surrounding localization pattern.
- **Unknown**: the product may intentionally keep these headings in English.
- **Minimal action**: verify the intended copy before editing. If intent is unavailable, report the uncertainty and make no change.

## Why This Matters

A local pattern is evidence, not proof of product intent. Do not turn an unverified preference into a defect.
