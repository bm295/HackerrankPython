---
name: architecture-explorer-agent
description: Analyze a repository or run one autonomous, test-protected architecture improvement workflow from a single Architecture Explorer Agent skill. Use for focused architecture analysis and refactors in any codebase.
---

# Architecture Explorer Agent

Use this skill when the user invokes `Architecture Explorer Agent` for repository architecture work in any repository.

This is the Codex skill for architecture analysis and focused architectural improvement.

If the user asks to improve, refactor, fix architecture, run for a time budget, or says "phan tich va refactor", perform the autonomous improvement workflow directly as Codex in the target repository.

## Autonomous Improvement Mode

Use this mode when the user asks Codex to work directly inside an existing repository, identify an architectural weakness from source evidence, protect behavior with tests, make a small refactoring, verify it, and optionally repeat if time allows.

The user may provide only a time range, for example `5-10 minutes`, plus optional constraints. In that case:

- infer the target repository from the current workspace unless the user gives a path;
- treat the time range as a hard budget;
- select exactly one architecture topic automatically from source evidence;
- add characterization tests before changing production code;
- refactor only code covered by those tests or by equivalent existing tests;
- run relevant tests after refactoring and repair regressions before continuing;
- add post-refactoring tests where they protect the improved boundary or behavior;
- for `5-10 minutes`, perform at most one focused iteration;
- if the budget is too small for a safe production refactor, spend the run on characterization or conformance tests and report why production code was not changed.

Optional user conditions override these defaults when safe, such as preferred folders, areas to avoid, no new dependencies, public API restrictions, validation commands, or maximum iterations.

## Autonomous Operating Rules

- Begin by inspecting the repository deeply enough to understand its context.
- Do not assume a specific language, framework, test runner, or architecture style.
- Respect repository-local instructions such as `AGENTS.md`, `CONTRIBUTING.md`, and build docs.
- Before editing production code, establish a baseline with relevant tests, build, lint, or type checks where practical.
- Prefer small, test-protected, reviewable changes.
- Do not rewrite the repository wholesale.
- Do not intentionally leave the repo in a broken state.
- Do not introduce abstractions without repository evidence.
- Do not weaken or delete tests to make the run green.
- Do not make broad rewrites during short budgets.

## Autonomous Workflow

Follow this cycle:

1. Repository discovery.
2. Select one architecture topic.
3. Find a concrete weakness.
4. State the architectural hypothesis.
5. Add characterization tests before refactoring.
6. Perform the smallest coherent refactoring.
7. Verify the refactoring.
8. Add post-refactoring tests.
9. Evaluate the result.
10. Start another iteration only if time and risk allow.

Each iteration must use a substantially different architectural concern from previous iterations.

### 1. Repository discovery

Inspect enough of the repository to determine:

- primary languages;
- build system;
- test frameworks;
- package or module structure;
- entry points;
- important domain and infrastructure modules;
- dependency direction;
- existing architecture documentation;
- existing tests;
- CI, lint, and static-analysis configuration.

Read relevant files such as `README.md`, architecture docs, `AGENTS.md`, package/build manifests, test configuration, CI configuration, dependency configuration, and important application entry points.

### 2. Select one architecture topic

Choose one topic based on evidence in the repository. Examples:

- modularization;
- separation of concerns;
- information hiding;
- encapsulation;
- high cohesion;
- loose coupling;
- dependency inversion;
- dependency direction;
- interface design;
- architectural conformance;
- testability;
- persistence boundaries;
- communication boundaries;
- domain vs. infrastructure separation;
- plugin boundaries;
- error handling;
- global state;
- data coupling;
- dependency cycles.

Do not apply a pattern just because it is fashionable. State the exact selected topic internally and report it later.

### 3. Find a concrete weakness

Favor evidence such as:

- one module depending on implementation details of another;
- domain code depending directly on infrastructure;
- bidirectional dependencies or circular dependencies;
- excessive imports between modules;
- duplicated cross-cutting logic;
- global mutable state;
- one component with too many responsibilities;
- persistence concerns leaking into domain logic;
- business rules embedded in adapters or controllers;
- difficult-to-test code caused by dependency structure;
- construction of infrastructure dependencies deep inside business logic;
- repeated conditional logic that suggests a real boundary;
- unstable dependencies or informal conventions that can easily regress.

For each candidate, ask whether the benefit is worth the added abstraction or complexity, and whether behavior can be protected with automated tests.

### 4. State the architectural hypothesis

Use this form:

```text
Current structure X causes architectural problem Y, affecting quality Z.
Changing it to A should improve B, while preserving externally observable behavior C.
```

Also identify affected building blocks, dependency changes, interface changes, benefits, trade-offs, and regression risks.

### 5. Add characterization tests before refactoring

Before changing targeted production behavior, add or strengthen tests around the code being refactored.

Prefer observable behavior over implementation details. Cover normal behavior, boundary cases, error paths, important branches, and interactions across the boundary being changed where relevant.

Run the relevant tests and confirm they pass against the pre-refactoring implementation, except for clearly identified baseline failures. A test created after the production change does not satisfy this pre-refactor gate.

### 6. Perform the architectural refactoring

Refactor the smallest coherent scope that demonstrates a real architectural improvement.

Good refactorings include:

- moving responsibilities to a more cohesive building block;
- introducing an abstraction at a real architectural boundary;
- inverting a dependency;
- isolating infrastructure behind an interface;
- splitting an oversized component;
- removing an inappropriate dependency;
- reducing data coupling;
- eliminating a dependency cycle;
- separating domain logic from technical concerns;
- narrowing an interface;
- introducing an adapter;
- isolating external communication;
- encapsulating global or shared mutable state;
- enforcing an existing architectural rule.

Preserve observable behavior unless fixing a clearly demonstrated bug. Avoid unrelated formatting changes, unnecessary dependency upgrades, and public API changes unless architecturally justified.

### 7. Verify the refactoring

After production code changes:

1. run the new characterization tests;
2. run tests for directly affected modules;
3. run the broader test suite when feasible;
4. run build, type-check, lint, or static-analysis commands relevant to the repository.

If tests fail, investigate and repair regressions before continuing.

### 8. Add post-refactoring tests

Once the refactoring works, add further tests where they create meaningful protection against architectural regression.

Possible additions include behavioral tests, boundary tests, and architectural or conformance tests. Examples: domain modules must not depend on infrastructure modules, module A must not import module B, adapters must implement the expected abstraction, or dependency cycles must not appear.

At least one post-refactor test is required when the new boundary or extracted behavior is testable. Name it explicitly in the final report.

### 9. Evaluate and continue

Only consider an iteration successful when the improvement is concrete enough to justify its cost. Start another iteration only if the remaining time can fit discovery, tests, refactor, and verification.

Near the end of the budget, finish the current safe change, verify it, document findings, and avoid starting new risky work.

## Invocation Defaults

If the user says:

```text
Use the architecture-explorer-agent skill to analyze and refactor this repository for 5-10 minutes.
```

Interpret it as:

- run Autonomous Improvement Mode;
- minimum 5 minutes and maximum 10 minutes;
- maximum 1 focused iteration unless there is clearly enough time for more;
- discover the architecture topic automatically;
- add characterization tests, refactor, verify, then add post-refactor tests.

## Final Report

For autonomous improvement, finish with a concise report containing:

- elapsed time;
- topic selected;
- architectural weakness and source evidence;
- tests added before refactoring, with file names, test names, commands, and results;
- refactor performed;
- tests added after refactoring, with file names, test names, commands, and results;
- validation commands run;
- files changed;
- known failures or unverified areas;
- recommended next topics.

If any required gate cannot be completed within the budget, do not claim a completed refactor. Report `Refactor not completed`, identify the missing gate, and include only verified work.
