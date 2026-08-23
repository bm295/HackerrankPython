---
name: architecture-explorer-agent
description: Analyze a repository or run an autonomous, test-protected architecture refactoring loop when the user asks to improve, refactor, or gives a time budget.
---

# Architecture Explorer Agent

Use this skill when the user invokes `Architecture Explorer Agent` for repository architecture work.

Choose the mode from the request:

- If the user asks only to analyze, inspect, report, or output JSON/Markdown, run the local read-only analyzer.
- If the user asks to improve, refactor, fix architecture, run for a time budget, or says "phan tich va refactor", perform the autonomous improvement workflow directly as Codex in the target repository.

## Read-Only Analysis Mode

Use this mode only when the user wants a report and does not ask for code changes.

The local Python CLI is:

```powershell
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target>
```

Common commands:

```powershell
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze .
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze D:\Path\To\Repository
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target> --topic-mode hybrid
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target> --topic "Dependency Inversion" --topic-mode catalog
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target> --json
```

## Autonomous Improvement Mode

Use this mode by default when the user includes a time range such as `5-10 minutes` or asks to refactor. The user should only need to provide minimum and maximum minutes plus any optional constraints.

Default behavior:

- Infer the target repository from the current workspace unless the user gives a path.
- Treat the supplied minutes as a hard budget, for example `5-10 minutes` means minimum 5 and maximum 10 minutes.
- Automatically discover a relevant architecture topic from the repository; do not ask the user to choose one.
- Inspect repository instructions, manifests, tests, entry points, architecture docs, and relevant source files before editing.
- Establish a baseline by running practical existing validation commands.
- Find one concrete architectural weakness supported by source evidence.
- Add or strengthen characterization tests around the behavior that will be refactored before changing production code.
- Run the characterization tests and confirm they pass against the current behavior, except for clearly identified baseline failures.
- Perform the smallest coherent architecture refactor that improves the identified weakness.
- Run relevant tests after the refactor and repair regressions before continuing.
- Add post-refactoring tests where they meaningfully protect the new boundary or behavior.
- Repeat only if the remaining time can fit a complete safe iteration.
- Stop before the maximum time and leave the repository coherent.

For short budgets:

- `5-10 minutes`: perform at most one focused iteration.
- `10-20 minutes`: perform one iteration and consider a second only if the first finishes cleanly.
- If time is too short for a safe refactor, add characterization or conformance tests and report why production code was not changed.

Optional user conditions may override defaults when safe, for example:

- preferred folders or modules;
- areas to avoid;
- no new dependencies;
- do not change public APIs;
- validation command;
- maximum iterations.

Do not require the user to spell out the full workflow. If they say:

```text
[@Architecture Explorer Agent](plugin://architecture-explorer-agent@personal) phan tich kien truc va refactor trong 5-10 phut
```

Interpret it as:

- run Autonomous Improvement Mode;
- min minutes: 5;
- max minutes: 10;
- maximum iterations: 1 unless there is clearly enough time for more;
- discover the architecture topic automatically;
- add characterization tests, refactor, verify, then add post-refactor tests.

## Final Report

For autonomous improvement, finish with a concise report:

- elapsed time;
- topic selected;
- problem and evidence;
- tests added before refactoring;
- refactor performed;
- tests added after refactoring;
- validation commands run;
- files changed;
- known failures or unverified areas;
- recommended next topics.

## Constraints

- The Python CLI is read-only; do not expect it to refactor code.
- Autonomous improvement is performed by Codex editing the repository directly.
- Do not introduce abstractions without repository evidence.
- Do not weaken or delete tests to make the run green.
- Do not make broad rewrites during short budgets.
