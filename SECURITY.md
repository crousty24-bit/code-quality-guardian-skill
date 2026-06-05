# Security Policy

## Supported Versions

This project is currently an experimental beta.

| Version | Supported |
|---|---|
| `0.1.0-beta.1` | Yes |
| Earlier drafts | No |

## Reporting A Vulnerability

Do not open a public issue for a vulnerability that could put users or repositories at risk.

Use GitHub's private vulnerability reporting feature on this repository when it is available. Otherwise, contact the maintainer through the contact methods listed on the [crousty24-bit GitHub profile](https://github.com/crousty24-bit) and provide only enough public detail to establish contact.

Include:

- affected version and file;
- realistic impact;
- reproduction steps or proof of concept;
- whether the issue requires executing a bundled script;
- suggested mitigation, if known.

The maintainer will acknowledge a complete report when possible, assess severity, and coordinate disclosure after a fix or mitigation is available.

## Security Boundaries

Bundled evidence scripts are designed to:

- use the Python standard library only;
- avoid network access;
- avoid writing to analyzed repositories;
- avoid executing detected project commands.

Unexpected network access, file mutation, command execution, secret exposure, or unsafe installation behavior should be treated as a security issue.
