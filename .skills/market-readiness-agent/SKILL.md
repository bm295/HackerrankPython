---
name: market-readiness-agent
description: Improve any repository toward market readiness by finding one evidence-backed weakness, adding tests, refactoring safely, and verifying the result.
---

# Market Readiness Agent

Use this skill when the user wants Codex to work inside any repository and make one concrete improvement that materially increases readiness for commercialization.

This skill is for autonomous repository work by Codex. It is not tied to one language, framework, or test runner.

## Outcome

Complete one focused improvement cycle:

1. Inspect the repository.
2. Choose one issue that blocks or weakens market readiness.
3. Add tests covering the area to be changed before editing production code.
4. Refactor or fix the code.
5. Run verification and ensure tests pass.
6. Add at least one more test that increases protection or coverage after the fix.

The result must leave the repository in a coherent state with verified tests.

## What counts as market readiness

Favor issues that affect the repository's ability to be shipped, sold, supported, or trusted in production. Common examples:

- missing or weak tests around business-critical behavior;
- unsafe configuration handling;
- brittle error handling on important flows;
- infrastructure and domain logic tightly coupled in a way that blocks maintenance;
- release-critical behavior with poor validation;
- code paths that are hard to verify or regress easily;
- critical duplication or oversized components that make change risky;
- missing guardrails for externally visible behavior;
- packaging or entry-point issues that prevent reliable execution;
- weak boundaries around integrations, persistence, or secrets.

Do not choose a cosmetic issue when a reliability, safety, testability, or maintainability issue has stronger business impact.

## Operating rules

- Work on any repository in the current workspace unless the user gives a different target path.
- Do not assume a specific language, framework, architecture style, or test tool.
- Read repository instructions and constraints first, including `AGENTS.md`, `README.md`, build files, CI files, and test configuration where relevant.
- Base the chosen improvement on concrete source evidence, not generic best practices.
- Prefer the smallest change that creates a real commercial-readiness gain.
- Do not broaden scope into a repo-wide rewrite.
- Do not change unrelated behavior.
- Do not claim success without running relevant tests.

## Required workflow

### 1. Discover repository context

Inspect enough of the repository to determine:

- primary language and package structure;
- build and test commands;
- entry points and important modules;
- existing test coverage in the target area;
- obvious release, reliability, security, or maintenance risks.

Run a practical baseline command when feasible before editing.

### 2. Select one improvement target

Choose exactly one issue and state:

- why it matters for market readiness;
- what source evidence supports it;
- what quality attribute is at risk;
- why the chosen scope is the highest-value safe change.

Good targets are concrete and verifiable. Examples:

- a service constructs dependencies internally and is effectively untestable;
- an API handler swallows important failures and returns misleading results;
- critical input validation is inconsistent across code paths;
- release behavior depends on global mutable state;
- configuration parsing accepts invalid values without protection;
- business logic is mixed with infrastructure concerns and changes are risky.

### 3. Add tests before changing production code

Before production edits, add or strengthen tests around the behavior being changed.

The pre-change tests should:

- cover normal behavior;
- cover at least one boundary, failure, or regression-prone case;
- protect the behavior that the refactor must preserve or intentionally fix.

Run those tests on the current code and record the result. If there are baseline failures, identify them precisely.

### 4. Refactor or fix the code

Make the smallest coherent code change that improves market readiness in the selected area.

Acceptable improvements include:

- introducing a seam that makes critical behavior testable;
- separating infrastructure concerns from business logic;
- hardening error handling on a release-critical path;
- tightening configuration validation;
- removing a risky dependency coupling;
- extracting a responsibility from an oversized unit;
- enforcing a boundary that reduces regression risk.

Avoid speculative abstractions or broad style rewrites.

### 5. Verify the change

After editing:

1. run the new or strengthened pre-change tests;
2. run relevant existing tests for affected modules;
3. run broader validation when feasible for the repo.

A completed run requires passing verification for the changed area.

### 6. Add post-change tests

After the code is stable, add at least one additional test that increases confidence or coverage beyond the minimum characterization tests.

Prefer tests that lock in:

- the new boundary;
- a previously uncovered edge case;
- an integration contract;
- a regression-prone error path;
- a commercially important invariant.

### 7. Final report

Report:

- selected issue and why it matters for market readiness;
- source evidence;
- tests added before the change;
- code change made;
- tests added after the change;
- commands run and pass/fail status;
- any remaining important risks not addressed.

## Safety rules

Do not:

- rewrite the entire repository;
- disable or weaken tests to force a green run;
- change technology stacks unnecessarily;
- introduce new dependencies unless clearly justified;
- modify generated files unless the repository intentionally maintains them;
- claim the repo is fully market-ready after one improvement;
- skip validation of the touched area.

If the repository state prevents safe completion, stop with a precise explanation of the blocker instead of pretending the improvement was completed.
