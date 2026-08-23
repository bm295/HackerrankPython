---
name: autonomous-architecture-improvement-loop
description: Run an autonomous architecture improvement loop in an arbitrary repository, protecting behavior with tests and performing small verified refactorings.
---

# Autonomous Architecture Improvement Loop

Use this skill when the user wants an autonomous senior software architect and engineer to work directly inside an existing repository, find architecture problems, protect behavior with tests, make small safe refactorings, verify them, and repeat the process.

## Operating rules

- Begin by inspecting the repository deeply enough to understand its context.
- Do not assume a particular language, framework, test runner, or architecture style.
- Respect repository-local instructions such as `AGENTS.md`, `CONTRIBUTING.md`, and build docs.
- Before editing production code, establish a baseline with the repository's relevant tests, build, lint, or type checks where practical.
- Prefer small, test-protected, reviewable changes.
- Do not rewrite the repository wholesale.
- Do not intentionally leave the repo in a broken state.
- If the user provides a time budget, treat it as a hard budget and manage scope accordingly.

## Required workflow

Follow this cycle:

1. Repository discovery
2. Select one architecture topic
3. Find a concrete weakness
4. State the architectural hypothesis
5. Add characterization tests before refactoring
6. Perform the smallest coherent refactoring
7. Verify the refactoring
8. Add post-refactoring tests
9. Evaluate the result
10. Start another iteration only if time and risk allow

Each iteration must use a substantially different architectural concern from previous iterations.

## Phase 0: Repository discovery

Inspect enough of the repository to determine:

- primary language(s);
- build system;
- test framework(s);
- package/module structure;
- entry points;
- important domain and infrastructure modules;
- dependency direction;
- existing architecture documentation;
- existing tests;
- CI and lint/static-analysis configuration.

Read relevant files such as:

- `README.md`;
- architecture docs;
- `AGENTS.md` or equivalent repository instructions;
- package/build manifests;
- test configuration;
- CI configuration;
- dependency configuration;
- important application entry points.

Run relevant baseline validation commands where practical before refactoring.

## Phase 1: Select an architecture topic

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

Do not apply a pattern just because it is fashionable. The repository determines whether the topic is useful.

## Phase 2: Find a concrete weakness

Look for a location where the selected topic is relevant. Favor evidence such as:

- one module depending on implementation details of another;
- domain code depending directly on infrastructure;
- bidirectional dependencies;
- circular dependencies;
- excessive imports between modules;
- duplicated cross-cutting logic;
- global mutable state;
- one component with too many responsibilities;
- low cohesion;
- interface exposure of implementation details;
- persistence concerns leaking into domain logic;
- business rules embedded in adapters or controllers;
- difficult-to-test code caused by dependency structure;
- construction of infrastructure dependencies deep inside business logic;
- changes requiring many unrelated files;
- repeated conditional logic that suggests an abstraction;
- temporal coupling between operations;
- unstable dependencies;
- informal conventions that can easily regress.

For each candidate, ask:

1. What architectural problem exists?
2. What source-code evidence supports it?
3. Which quality is affected?
4. What changes become unnecessarily difficult?
5. What is the smallest meaningful improvement?
6. Can behavior be protected with automated tests?
7. Is the benefit worth the added abstraction or complexity?

## Phase 3: State the architectural hypothesis

Use this form:

> Current structure X causes architectural problem Y, affecting quality Z.
> Changing it to A should improve B, while preserving externally observable behavior C.

Also identify:

- affected building blocks;
- dependency changes;
- interface changes;
- benefits;
- trade-offs;
- regression risks.

## Phase 4: Characterization tests before refactoring

Before changing the targeted production behavior, add or strengthen tests around the code being refactored.

Prefer observable behavior over internal implementation details.

Cover, where relevant:

- normal behavior;
- boundary cases;
- error paths;
- important branches;
- interactions across the boundary being changed.

Run the relevant tests and confirm they pass against the pre-refactoring implementation, except for known baseline failures.

If the code is hard to test because of the current design, create the smallest possible seam that enables characterization without doing the full refactor yet.

## Phase 5: Perform the architectural refactoring

Refactor the smallest coherent scope that demonstrates a real architectural improvement.

Guidelines:

- preserve observable behavior unless fixing a clearly demonstrated bug;
- keep changes incremental;
- use existing repository conventions;
- avoid repo-wide rewrites;
- avoid speculative abstractions;
- avoid unrelated formatting changes;
- avoid unnecessary dependency upgrades;
- avoid changing public interfaces unless architecturally justified;
- avoid introducing a new architectural style purely for theoretical purity.

Good refactorings include:

- moving responsibilities to a more cohesive building block;
- introducing an abstraction at a real architectural boundary;
- inverting a dependency;
- isolating infrastructure behind an interface;
- splitting an oversized component;
- removing an inappropriate dependency;
- reducing data coupling;
- eliminating a dependency cycle;
- centralizing a genuine cross-cutting concern;
- separating domain logic from technical concerns;
- narrowing an interface;
- introducing an adapter;
- isolating external communication;
- encapsulating global or shared mutable state;
- removing temporal coupling;
- restructuring building-block dependencies;
- enforcing an existing architectural rule.

## Phase 6: Verify the refactoring

After production code changes:

1. run the new characterization tests;
2. run tests for directly affected modules;
3. run the broader test suite when feasible;
4. run build, type-check, lint, or static-analysis commands relevant to the repository.

If tests fail, investigate and repair regressions before continuing.

## Phase 7: Add post-refactoring tests

Once the refactoring works, add further tests where they create meaningful protection against architectural regression.

Possible additions:

- behavioral tests;
- boundary tests;
- architectural or conformance tests.

Examples:

- domain modules must not depend on infrastructure modules;
- module A must not import module B;
- dependencies must point inward;
- certain packages must remain independent;
- adapters must implement the expected abstraction;
- dependency cycles must not appear.

## Phase 8: Evaluate the result

Record internally:

- architecture topic;
- concrete problem;
- evidence;
- refactoring;
- dependency impact;
- quality impact;
- trade-offs;
- tests.

Only consider an iteration successful when the improvement is concrete enough to justify its cost.

## Phase 9: Start another iteration

After one successful iteration:

1. check elapsed time;
2. estimate whether another safe iteration fits;
3. choose a different architectural topic;
4. inspect another area of the repository;
5. repeat the process.

Do not keep applying the same technique under different names.

## Time budget handling

If the prompt provides `[min]` and `[max]` minutes:

- do not intentionally finish before `[min]` if safe meaningful work remains;
- do not start a risky iteration when the remaining time is insufficient for test, refactor, and verification;
- stop before exceeding `[max]`;
- near the end of the budget, finish the current safe change, verify it, document findings, and avoid starting new risky work.

## Safety rules

Do not:

- delete large amounts of production code without strong justification;
- rewrite the entire repository;
- change technology stacks unnecessarily;
- upgrade unrelated dependencies;
- disable failing tests;
- skip tests to make the pipeline green;
- weaken assertions to hide regressions;
- introduce abstractions solely because they are considered best practice;
- make architectural changes unsupported by evidence;
- change user-facing behavior without explicit justification;
- expose secrets or credentials;
- modify generated code unless the repository intentionally maintains it;
- perform destructive version-control operations.

## Final report

When done, output a concise report with sections for:

- execution;
- architecture improvements;
- validation;
- rejected topics;
- recommended next topics.

Make the report concrete and evidence-based.
