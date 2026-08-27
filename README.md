# Architecture Explorer Agent

Architecture Explorer Agent is a read-only CLI that analyzes a software repository, discovers or selects one architecture topic, researches that topic online, and produces evidence-backed recommendations tied to specific code locations.

For autonomous refactoring, use the Codex skill `architecture-explorer-agent`. That single skill chooses between read-only analysis and a Codex-driven improvement workflow. The `architecture-explorer-agent` CLI remains read-only and is used for analysis reports.

## What it does

- Scans a local repository or clones a Git URL to a temporary read-only workspace
- Builds a staged architecture snapshot
- Discovers relevant topics online from repository languages, frameworks, dependencies, and code signals
- Ranks discovered topics by repository relevance and source quality, with the built-in catalogue as a fallback
- Fetches a small set of authoritative research sources
- Finds concrete evidence in the repository
- Produces a human-readable or JSON report

## Why it exists

The goal is to learn an architecture concept through a real codebase rather than treat architecture as an abstract checklist.

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .
```

## Run

```bash
python -m architecture_explorer_agent.cli analyze ./path/to/repo
```

Analyze a Git repository URL:

```bash
python -m architecture_explorer_agent.cli analyze https://example.com/repository.git
```

## How to use on any repository

### 1. Analyze a local repository

Point the agent at any local codebase you can read:

```bash
python -m architecture_explorer_agent.cli analyze D:\Code\my-app
```

Or from the current directory:

```bash
python -m architecture_explorer_agent.cli analyze .
```

### 2. Analyze a Git repository URL

If you want the agent to inspect a remote repository, pass a Git URL:

```bash
python -m architecture_explorer_agent.cli analyze https://github.com/user/project.git
```

The agent clones the repo into a temporary workspace and keeps the target read-only.

### 3. Call it while standing inside another repo

If you are already inside some other repository, you can still invoke this agent without changing directories.

From the other repo directory:

```bash
python D:\Code\HackerrankPython\architecture_explorer_agent\cli.py analyze .
```

Or use the installed console command:

```bash
architecture-explorer-agent analyze .
```

If you want the command available everywhere, install it once from the agent repo:

```bash
python -m pip install -e D:\Code\HackerrankPython
```

Then from any repository:

```bash
architecture-explorer-agent analyze .
```

### 4. Use it as a Codex skill

This repository includes the project skill `.skills/architecture-explorer-agent`.

After installation, in a new Codex thread you can ask for actions like:

- `Analyze the current repository with Architecture Explorer Agent`
- `Run Architecture Explorer Agent on D:\Code\SomeRepo`
- `Analyze https://github.com/org/project.git with Architecture Explorer Agent`
- `Analyze the current repository with Architecture Explorer Agent and write JSON`
- `Run Architecture Explorer Agent on D:\Code\SomeRepo with the hybrid topic mode`

The `architecture-explorer-agent` skill supports read-only repository analysis and safe,
test-protected architectural refactoring in an arbitrary repository.

When the prompt asks only for analysis or a report, the skill runs the read-only CLI. When the prompt asks for improvement, refactoring, or includes a time budget, the same skill switches to the autonomous improvement workflow. The autonomous workflow is a Codex operating mode; it does not map to a separate CLI command.

The analysis skill runs this local Python CLI:

```powershell
python D:\Code\HackerrankPython\architecture_explorer_agent\cli.py analyze <target>
```

Useful flags for analysis:

- `--topic-mode hybrid` for online discovery with a catalog fallback
- `--topic-mode discover` to require online discovery
- `--topic-mode catalog` to skip search and use the built-in topic catalog
- `--json` for structured output
- `--seed 42` for reproducible topic selection
- `--output report.md` to write the report to a file

You can also combine a seed and a topic when you want reproducible guided selection:

```powershell
python D:\Code\HackerrankPython\architecture_explorer_agent\cli.py analyze <target> --seed 42 --topic "Dependency Inversion"
```

### 5. Make runs reproducible with a seed

Use a seed when you want the same topic selection to be chosen again:

```bash
python -m architecture_explorer_agent.cli analyze ./my-repo --seed 42
```

### 6. Force a topic instead of random selection

The default hybrid behavior searches for a relevant topic and falls back to seeded catalogue selection when search is unavailable.
You can override the topic when you want a specific architecture lens:

```bash
python -m architecture_explorer_agent.cli analyze ./my-repo --topic "Dependency Inversion"
```

The requested topic guides online discovery. If discovery is unavailable in hybrid mode,
the topic must exist in the built-in catalogue or the command reports a clear error.

### Topic discovery modes

```bash
# Online discovery with a catalogue fallback (default)
python -m architecture_explorer_agent.cli analyze ./my-repo --topic-mode hybrid

# Require topics discovered from current online search results
python -m architecture_explorer_agent.cli analyze ./my-repo --topic-mode discover

# Disable search and retain deterministic catalogue selection
python -m architecture_explorer_agent.cli analyze ./my-repo --topic-mode catalog
```

Discovery creates search queries from repository signals and uses DuckDuckGo's HTML
endpoint by default. Configure `SEARCH_ENDPOINT`, `SEARCH_RESULT_COUNT`, and
`SEARCH_TIMEOUT` when a different compatible endpoint or limits are required.

### 7. Emit structured JSON

Use JSON when you want to pipe results into another tool:

```bash
python -m architecture_explorer_agent.cli analyze ./my-repo --json
```

### 8. Write the report to a file

```bash
python -m architecture_explorer_agent.cli analyze ./my-repo --output report.md
```

### Run from another repository

If you are standing inside a different repository, install this read-only analyzer once:

```powershell
cd D:\Code\HackerrankPython
python -m pip install -e .
```

Then you can run analysis from the target repository:

```powershell
cd D:\Code\ElFnB
architecture-explorer-agent analyze . --topic-mode hybrid
```

Or force one topic:

```powershell
cd D:\Code\ElFnB
architecture-explorer-agent analyze . --topic "Dependency Inversion" --topic-mode catalog
```

If you do not want to install the console command, call the CLI directly:

```powershell
cd D:\Code\ElFnB
python D:\Code\HackerrankPython\architecture_explorer_agent\cli.py analyze . --topic-mode hybrid
```

To perform the full autonomous improvement loop, open Codex in the target repository and invoke the skill with only a time range. This repository does not need a local API key because Codex is the executor.

Minimal prompt:

```text
Use the architecture-explorer-agent skill to analyze and refactor this repository for 5-10 minutes.
```

With optional conditions:

```text
Use the architecture-explorer-agent skill to analyze and refactor this repository for 5-10 minutes.
Dieu kien:
- Khong them dependency moi.
- Khong doi public API neu khong can thiet.
- Uu tien src/Application va tests lien quan.
- Validation command: dotnet test
```

That prompt defaults to the autonomous workflow:

- discover one architecture topic automatically;
- inspect the repository and establish a validation baseline;
- add characterization tests before refactoring;
- refactor only a small, evidence-backed target;
- run relevant tests and repair regressions;
- add post-refactoring tests;
- report files changed, tests run, and next topics.

Use the longer form only when you want tighter control:

```text
Use the architecture-explorer-agent skill on this repository.

Goal:
- Inspect the repository.
- Identify architecture weaknesses from source evidence.
- Add characterization tests before risky refactoring.
- Make small architecture improvements.
- Run relevant tests after each meaningful change.
- Repeat with a different architecture topic if time remains.

Conditions:
- Budget: 20-30 minutes.
- Maximum iterations: 2.
- Preferred areas: <folders or modules>.
- Avoid: <dependencies, public API changes, risky areas>.
- Validation command: <known test/build command, if any>.
- Extra constraints: <your project-specific rules>.

Final report:
- What changed.
- Which tests were added or run.
- Architecture before and after.
- Known risks and recommended next topics.
```

If the skill is not available in the current Codex session, point Codex at the skill file explicitly:

```text
Read and follow this skill:
D:\Code\HackerrankPython\architecture-explorer-agent\skills\architecture-explorer-agent\SKILL.md

Run it on the current repository with these conditions:
- Budget: 20-30 minutes.
- Maximum iterations: 2.
- Preferred areas: <folders or modules>.
- Avoid: <dependencies, public API changes, risky areas>.
- Validation command: <known test/build command, if any>.
```

Useful sanity checks before starting the autonomous Codex run:

```powershell
python --version
git status --short
```

If the target repository already has a known validation command, run it once first:

```powershell
python -m unittest discover -s tests -p "test_*.py"
python -m pytest
npm test
dotnet test
go test ./...
cargo test
```

## Useful options

- `--seed 42`
- `--topic "Dependency Inversion"`
- `--topic-mode hybrid`
- `--json true`
- `--output report.md`

## What the agent does during a run

1. Scans the repository in read-only mode.
2. Ignores large or generated directories such as `node_modules`, `dist`, and `build`.
3. Builds a compact architecture snapshot.
4. Builds a repository profile from languages, frameworks, dependencies, and code signals.
5. Searches online for relevant architecture topics and ranks the candidates.
6. Falls back to seeded catalogue selection when hybrid discovery is unavailable.
7. Researches the selected topic online from its discovered sources.
8. Finds concrete evidence in the codebase.
9. Produces a recommendation with benefits, trade-offs, and confidence.

## Optional repo-local configuration

Create a `.architecture-explorer.json` file in the target repository when you want to add extra ignored directories:

```json
{
  "ignoredDirs": ["legacy", "sandbox", "tmp"]
}
```

This is useful when a repository contains old folders that should not influence the analysis.

## Configuration

Environment variables:

- `RESEARCH_PROVIDER`
- `MAX_FILES_ANALYZED`
- `MAX_FILE_SIZE`
- `IGNORED_DIRS`
- `IGNORED_PATTERNS`
- `RESEARCH_SOURCE_COUNT`
- `RANDOM_SEED`
- `LOG_LEVEL`

See `.env.example`.

## Example workflow

```bash
python -m pip install -e .
python -m architecture_explorer_agent.cli analyze ./some-repo --seed 7 --output analysis.md
```

If you want to inspect a different repository later, just point the same CLI at another path or URL.

## Testing

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Architecture

See [docs/architecture.md](docs/architecture.md).

## ADRs

See [docs/adr](docs/adr).
