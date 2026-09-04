---
name: code-review
description: Review uncommitted or proposed code changes for correctness, regressions, maintainability, and separation of concerns. Use when the user asks for a code review or review of a diff; do not broaden the review into unrelated unchanged code unless the diff requires it.
metadata:
  short-description: Review code changes and separation of concerns
---

# Code Review Diff

Review the current change set and report actionable findings. Do not modify files unless the user explicitly asks for fixes.

## Scope and evidence

- Identify the exact change set first using `git diff`, `git diff --staged`, and `git status`; include untracked files when they are part of the requested change.
- Review changed lines and immediate callers, callees, tests, configuration, and data contracts when needed to establish impact. Avoid auditing unrelated legacy code.
- If there is no diff, state that clearly and review only a supplied patch or explicitly named target.
- Run focused, relevant tests or static checks when available. Distinguish existing failures from regressions caused by the change.

## Review priorities

Look for functional defects, edge cases, security or data-loss risks, regressions, missing tests, and separation-of-concerns violations. Check whether one module, function, class, or handler mixes business rules, I/O, persistence, transport/UI concerns, validation, formatting, and orchestration. Recommend boundaries that preserve behavior and avoid speculative abstractions; small local coupling is acceptable when splitting adds complexity without meaningful benefit.

## Findings standard

Each finding must point to a specific changed file and line, explain the concrete failure mode or maintenance consequence, give an implementable recommendation, and use a priority: `P0` release/blocking, `P1` high impact, `P2` normal, or `P3` low/non-blocking.

Do not report style preferences, unsupported hypotheticals, or issues already prevented by surrounding code. If no actionable findings remain, say so and mention verification performed.

## Output format

Start with the highest-priority findings using:

`[P1] path/to/file.ext:42 — Short title`

Then provide the explanation and recommendation. Finish with a brief verification summary and remaining uncertainty.
