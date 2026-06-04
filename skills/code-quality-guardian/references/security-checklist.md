# Security Checklist

Use this when code touches user input, authentication, authorization, secrets, external data, dependencies, file access, or logging.

## Basic Risks

- Secrets committed in source, config, logs, tests, or fixtures.
- Missing input validation at trust boundaries.
- Injection risks in SQL, shell commands, templates, paths, or URLs.
- Authorization checks that rely only on frontend state.
- Sensitive data exposed in logs or error messages.
- Overly broad permissions or tokens.

## Review Questions

- What data is untrusted?
- Where is it validated or sanitized?
- Who is allowed to perform this action?
- Could the change leak secrets or personal data?
- Does an added dependency increase attack surface without strong reason?

## Change Discipline

- Do not broaden permissions as a convenience fix.
- Do not log raw credentials, tokens, cookies, or personal data.
- Prefer existing project security helpers and middleware.
- State unresolved security uncertainty clearly.
- Recommend a dedicated security pass when the issue is larger than the current scope.

