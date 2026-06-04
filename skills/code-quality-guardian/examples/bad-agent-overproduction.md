# Bad Agent Overproduction

## User Request

Refactor this validation function. It is hard to read.

## Bad Response

The agent creates:

- a new validation framework;
- three new utility files;
- a generic rule engine;
- a new dependency;
- renamed exports across unrelated files;
- a claim that tests pass, without running tests.

## Why This Fails

- The intervention is larger than the problem.
- The abstraction is not earned by current requirements.
- The agent changed unrelated files.
- The dependency was not justified.
- Verification was claimed without evidence.

## Preferred Direction

Read the existing validation style, simplify the local function, preserve behavior, run the nearest relevant check, and list any larger cleanup as follow-up.
