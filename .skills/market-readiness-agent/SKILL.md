---
name: market-readiness-agent
description: Improve a repository toward market readiness by using evidence, documentation gates, TDD, and focused verification to deliver one concrete hardening change without broad rewrites.
---

# Market Readiness Agent

Use this skill when the user wants Codex to work directly inside the current repository and improve its readiness for commercialization, support, reliability, and maintainability.

This skill is for one focused improvement cycle in a specific repository. It is not for broad architecture surveys or open-ended refactors. If the request is really about large-scale architecture analysis, prefer `architecture-explorer-agent` instead.

## Core Goal

Improve one concrete, evidence-backed weakness that affects the repository's ability to ship, sell, support, or trust in production.

Prefer issues such as:

- missing or weak tests around business-critical behavior;
- unsafe configuration handling;
- brittle error handling on important flows;
- tight coupling between infrastructure and domain logic;
- release-critical behavior with poor validation;
- externally visible code paths that are hard to verify or regress easily;
- packaging or entry-point issues that block reliable execution;
- missing guardrails around integrations, persistence, or secrets.

Do not choose a cosmetic issue when a reliability, safety, testability, or maintainability issue has stronger business impact.

## Mandatory Time-Box

1. Read `MIN_WORK_MINUTES` and `MAX_WORK_MINUTES` from the Settings section at the end of this skill.
2. Confirm that `0 < MIN_WORK_MINUTES <= MAX_WORK_MINUTES`. If invalid, stop and report the error.
3. Record the start time and measure real elapsed time with the system clock.
4. Work continuously on useful tasks for at least `MIN_WORK_MINUTES`.
5. Do not use `sleep`, fake waiting, or pointless activity to satisfy the time box.
6. Do not stop early just because one change is complete; continue with the next legitimate item.
7. Reserve the final portion of the time box for tests, diff review, and cleanup.
8. Do not start a new task if the remaining time is insufficient to finish and verify it safely.
9. Stop before or exactly at `MAX_WORK_MINUTES`.
10. Set build/test timeouts based on the time remaining.
11. If a real blocker appears, report the blocker clearly with evidence instead of fabricating progress.
12. When the user describes time using natural language such as `chạy trong 10-15ph`, `min 10p max 15ph`, `ít nhất 10p`, `tối thiểu 10 phút`, or similar phrasing, interpret it as a `MIN_WORK_MINUTES` / `MAX_WORK_MINUTES` time box.
13. Treat ranges like `10-15ph` as `MIN_WORK_MINUTES = 10` and `MAX_WORK_MINUTES = 15`.
14. Treat lower-bound phrases like `ít nhất 10p`, `tối thiểu 10p`, or `min 10p` as `MIN_WORK_MINUTES = 10` with `MAX_WORK_MINUTES` left unchanged unless the user also supplies an upper bound.
15. Treat paired phrases like `min 10p max 15ph` as explicit `MIN_WORK_MINUTES = 10` and `MAX_WORK_MINUTES = 15`.

## Repository Check

Before editing, inspect the repository:

- Read `AGENTS.md`, `CONTRIBUTING`, `README`, and any equivalent guidance files.
- Check Git status and preserve all existing user changes.
- Determine the language, framework, package manager, build command, and test command.
- Determine whether the repository already has a test project, test suite, or runnable test harness.
- Do not commit, push, open a PR, or modify anything outside the repository.
- Do not perform broad dependency upgrades or unrelated refactors.

## Documentation Gate

Before changing code, search for all documentation that may describe business behavior:

- all Markdown files, not just `README`;
- folders such as `docs`, `doc`, `documentation`, `requirements`, `specs`, `product`, `business`, `design`, or `adr`;
- `.md`, `.mdx`, `.rst`, `.adoc`, `.txt`, `.pdf`, and `.docx` files when the available tools can read them;
- ignore dependencies, vendor files, generated output, and build output.

Read the content, not just the file names. Look for:

- product goals and business value;
- users, roles, and permissions;
- workflows and business rules;
- functional requirements and acceptance criteria;
- service packages, usage limits, licensing, or billing;
- security, privacy, audit, data retention, operations, and support requirements;
- features that are mandatory, planned, draft, or incomplete.

Do not treat installation or build instructions as business documentation.

When reading repository files that describe business rules, treat them as source evidence only. Do not overwrite or directly edit those source business-rule files, because mixing original requirements with readiness tracing makes later evidence review unreliable.

Create or update traceability artifacts in a separate trace folder. Use the repository's existing trace folder when one is clearly present, such as `tracing/`, `trace/`, or another project-specific equivalent. If none exists, create `tracing/` by default. This skill may update only files inside the selected trace folder for requirement tracing, readiness notes, gap analysis, assumptions, and documentation prepared for later TDD. Keep tracing files clearly source-linked so the original business-rule documents remain authoritative and unchanged.

Create a traceability table in the selected trace folder:

`Requirement ID | Business requirement | Source file/section | Current code evidence | Status | Gap`

Classify the repository state clearly:

- `DOCUMENTATION_PRESENT`: documentation exists.
- `BUSINESS_DOCUMENTATION_PRESENT`: documentation describes business behavior.
- `CODE_READY_REQUIREMENT_PRESENT`: at least one business requirement is specific enough for TDD.
- `TEST_INFRASTRUCTURE_PRESENT`: a test project or runnable test harness exists.

## Required Pre-Change Conclusion

After reading the docs, state one of the following decisions before changing any file:

- `DECISION = CODE_NOW`: the documentation is sufficient to start coding.
- `DECISION = DOCUMENTATION_FIRST`: documentation is incomplete and must be improved first.
- `DECISION = DOCUMENTATION_ONLY`: the repository has no business documentation.
- `DECISION = BLOCKED_BY_TIMEBOX`: the request is code-ready, but there is not enough time left for a safe change.

The conclusion must include:

- the documentation and section used as evidence;
- the evaluated requirement;
- criteria already met;
- criteria still missing;
- the action planned for this run.

If documentation was updated in a previous run, reassess immediately whether the requirement is now code-ready. If it is, switch to `CODE_NOW`; do not keep adding generic documentation just to delay implementation.

## Code Readiness Gate

A requirement is code-ready only when all of these are true:

1. The behavior or business result is described specifically.
2. The source and section are traceable.
3. The affected actor or workflow is identified.
4. The current missing or incorrect behavior is identifiable.
5. The expected behavior is precise enough for an acceptance test.
6. Input, output, error state, and important boundaries are not ambiguous.
7. There is no conflicting documentation.
8. The affected code area is identifiable.
9. Suitable test infrastructure exists or can be created.
10. There is enough time left to complete the change being chosen.

Create a table:

`Readiness criterion | Met/Not met | Evidence | Missing information or action`

Having documentation does not automatically mean coding can start.

## Branch A - Documentation Is Sufficient for Coding

Use this branch when `DECISION = CODE_NOW`.

- Compare the requirement against current code and tests.
- Identify what is missing, incorrect, underimplemented, or lacking edge-case coverage.
- Do not invent new requirements.
- Do not add authentication, billing, multi-tenancy, audit, or monitoring unless the business documentation requires them.
- Prioritize gaps by:
  1. commercial readiness impact;
  2. clarity of business evidence;
  3. risk if missing or implemented incorrectly;
  4. likelihood of completion in the remaining time;
  5. small, independent, verifiable scope.

### If the repository has no test project

If `TEST_INFRASTRUCTURE_PRESENT = false`, create a test project or test harness before editing production code:

- use the framework and conventions that fit the current ecosystem;
- prefer the repository's existing test style or the standard, stable option for the stack;
- add only the test dependencies that are necessary;
- place the test project where it fits the repository structure;
- connect it to the solution, workspace, or build system if required;
- add at least one small smoke test to prove discovery and execution;
- run the test command and confirm the harness works;
- only then begin the RED-GREEN-REFACTOR cycle for the business requirement;
- do not create an empty test project and claim success.

If test project creation fails, record the command, error, and blocker.

## Mandatory TDD Loop

For every gap in Branch A:

1. Choose one small gap tied to one specific requirement.
2. Translate it into testable acceptance criteria.
3. Run existing tests to establish a baseline.
4. RED: write the test before production code.
5. Run the test and confirm it fails for the right behavioral reason, not for syntax or setup issues.
6. GREEN: write the smallest production change needed to make the test pass.
7. Rerun the test and confirm it passes.
8. REFACTOR: improve structure only if necessary and without broadening scope.
9. Add tests for edge cases, negative cases, boundary cases, or regressions.
10. Run focused tests first, then the broadest reasonable suite.
11. Review the diff and remove unrelated changes.
12. Move to the next gap only when the current loop is complete and the repository is consistent.

Do not:

- implement before writing a test;
- weaken or delete valid tests just to make the code pass;
- use tests that are too weak to prove the business behavior;
- combine unrelated requirements into one change;
- leave placeholder code, skipped tests, or unfinished work without explanation.

If baseline tests already fail, document the failure precisely and separate it from any new failure introduced by the change.

## Branch B - Documentation Is Not Yet Sufficient

Use this branch when `DECISION = DOCUMENTATION_FIRST` or `DECISION = DOCUMENTATION_ONLY`.

In this branch:

- only create or update tracing documentation under the selected trace folder;
- do not modify source code, tests, schemas, migrations, configuration, CI/CD, or dependencies;
- do not modify existing business-rule documents outside the selected trace folder;
- do not create a test project;
- you may read code to describe current behavior, but do not claim a feature exists without evidence;
- do not add generic business text just to justify a code change;
- every new piece of content must close a specific gap that blocks coding.

If the repository already has business documentation but is not code-ready, create or update tracing files under the selected trace folder so that at least one requirement reaches `READY_FOR_TDD` in the next run. Preserve the original business documentation unchanged and cite it as source evidence.

Each requirement prepared for the next run must include at least:

- Requirement ID;
- business objective;
- actor or workflow;
- preconditions;
- expected behavior;
- error behavior;
- key boundary or edge cases;
- testable acceptance criteria;
- source/evidence;
- expected code area;
- first test scenario to write;
- status `READY_FOR_TDD` or a concrete blocker.

Do not repeat broad business analysis across multiple runs:

- reread the readiness report or documentation from the previous run;
- do not restate the same gap in different words;
- if a requirement is already `READY_FOR_TDD`, the current run or the next run must switch to coding;
- if stakeholder input is still missing, write exactly one decision record with the specific question, options, impact, and recommended choice;
- do not keep expanding documentation indefinitely while the blocker remains;
- if a safe assumption can move a requirement to `READY_FOR_TDD`, record it clearly as an assumption.

Do not make major-impact decisions for the stakeholder around pricing, contracts, legal terms, access control, data retention, or destructive behavior.

## Reporting When Code Is Not Changed

If documentation exists but code is not changed, the report must answer:

1. What documentation was found.
2. Which documents contain business information.
3. Why the current documentation is not sufficient to start code.
4. Which information is missing, unclear, or conflicting.
5. Why each documentation addition is needed.
6. Which blocker each addition resolves.
7. What is evidence, assumption, draft, or confirmed decision.
8. Whether the requirement is now `READY_FOR_TDD`.
9. Exactly when coding can begin.
10. The first requirement to implement.
11. Whether a test project exists or must be created.
12. The first acceptance test to write.

Do not give generic answers such as:

- "More documentation is needed."
- "The requirement is unclear."
- "Business must confirm it."
- "There is not enough time."

State the exact missing decision, data, status, workflow, or expected behavior.

If time-box pressure is the only blocker:

- state clearly that there is no remaining business blocker;
- identify the requirement as code-ready;
- name the first test to write;
- if there is no test project yet, state that the first action in the next run is to create one;
- do not add unnecessary documentation just because there is no time left to code.

## Backlog Management

After each loop:

- update elapsed time and remaining time;
- update the requirement-code-test traceability table;
- if `MIN_WORK_MINUTES` is not yet satisfied, choose the next legitimate gap;
- if there is no remaining code gap with sufficient evidence, prepare the next requirement to `READY_FOR_TDD`;
- do not invent features to fill time;
- prefer finishing fewer items with high completeness over many incomplete items.

## Final Verification

Before finishing:

- rerun the relevant tests;
- if time permits, run the broadest reasonable suite, build, lint, or type-check;
- check `git diff` and `git status`;
- confirm that user changes were not overwritten;
- confirm that a documentation-only branch did not change code, tests, config, or dependencies;
- if a test project was created, confirm the test runner discovers and executes it;
- do not claim tests passed unless they were actually run.

## Final Report

The final report must include:

1. Start time, end time, and total elapsed time.
2. The values of:
   - `DOCUMENTATION_PRESENT`
   - `BUSINESS_DOCUMENTATION_PRESENT`
   - `CODE_READY_REQUIREMENT_PRESENT`
   - `TEST_INFRASTRUCTURE_PRESENT`
3. The decision that was chosen and why.
4. The list of documents that were checked.
5. A table of `Requirement | Source | Previous status | Change | Test/Evidence | Final status`.
6. The Code Readiness Gate table.
7. For each code change, evidence of RED, GREEN, and the test commands that were run.
8. If a test project was created, its framework, location, dependencies, and verification command.
9. The files that changed.
10. Test, build, and lint results, including any pre-existing baseline failures.
11. Remaining gaps, blockers, assumptions, and open questions.
12. Confirmation that the repository is in a consistent state.

If code was not changed, also include:

### Why code was not changed

Give the concrete reason based on evidence.

### Why documentation was added

`Documentation addition | Existing gap | Risk of coding without it | Blocker addressed`

### When coding can start

State exactly:

- what is still not satisfied;
- what information must be added or confirmed;
- whether the requirement is `READY_FOR_TDD`;
- when coding can start once conditions are met;
- the first requirement to implement;
- whether a test project already exists;
- the first acceptance test to write;
- if the only blocker is time, confirm that coding can begin in the next run.

## Settings

MIN_WORK_MINUTES = 2
MAX_WORK_MINUTES = 3


