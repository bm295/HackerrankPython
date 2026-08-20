# Architecture Explorer Agent

Architecture Explorer Agent is a read-only CLI that analyzes a software repository, selects one architecture topic with controlled randomness, researches that topic online, and produces evidence-backed recommendations tied to specific code locations.

## What it does

- Scans a local repository or clones a Git URL to a temporary read-only workspace
- Builds a staged architecture snapshot
- Selects one topic from an extensible catalogue
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
python -m architecture_agent.cli analyze ./path/to/repo
```

Analyze a Git repository URL:

```bash
python -m architecture_agent.cli analyze https://example.com/repository.git
```

## How to use on any repository

### 1. Analyze a local repository

Point the agent at any local codebase you can read:

```bash
python -m architecture_agent.cli analyze D:\Code\my-app
```

Or from the current directory:

```bash
python -m architecture_agent.cli analyze .
```

### 2. Analyze a Git repository URL

If you want the agent to inspect a remote repository, pass a Git URL:

```bash
python -m architecture_agent.cli analyze https://github.com/user/project.git
```

The agent clones the repo into a temporary workspace and keeps the target read-only.

### 3. Call it while standing inside another repo

If you are already inside some other repository, you can still invoke this agent without changing directories.

From the other repo directory:

```bash
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze .
```

Or use the installed console command:

```bash
architecture-agent analyze .
```

If you want the command available everywhere, install it once from the agent repo:

```bash
python -m pip install -e D:\Code\HackerrankPython
```

Then from any repository:

```bash
architecture-agent analyze .
```

### 4. Use it through a Codex plugin

This repository has also been wrapped as a local Codex plugin named `architecture-explorer-agent`.

After installation, in a new Codex thread you can ask for actions like:

- `Analyze the current repository with Architecture Explorer Agent`
- `Run Architecture Explorer Agent on D:\Code\SomeRepo`
- `Analyze https://github.com/org/project.git with Architecture Explorer Agent`

The plugin skill runs this local Python CLI:

```powershell
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target>
```

### 5. Make runs reproducible with a seed

Use a seed when you want the same topic selection to be chosen again:

```bash
python -m architecture_agent.cli analyze ./my-repo --seed 42
```

### 6. Force a topic instead of random selection

The default behavior is random topic selection with repository applicability checks.
You can override the topic when you want a specific architecture lens:

```bash
python -m architecture_agent.cli analyze ./my-repo --topic "Dependency Inversion"
```

### 7. Emit structured JSON

Use JSON when you want to pipe results into another tool:

```bash
python -m architecture_agent.cli analyze ./my-repo --json
```

### 8. Write the report to a file

```bash
python -m architecture_agent.cli analyze ./my-repo --output report.md
```

## Useful options

- `--seed 42`
- `--topic "Dependency Inversion"`
- `--json true`
- `--output report.md`

## What the agent does during a run

1. Scans the repository in read-only mode.
2. Ignores large or generated directories such as `node_modules`, `dist`, and `build`.
3. Builds a compact architecture snapshot.
4. Selects one architecture topic with controlled randomness.
5. Researches the topic online from authoritative sources.
6. Finds concrete evidence in the codebase.
7. Produces a recommendation with benefits, trade-offs, and confidence.

## Optional repo-local configuration

Create a `.architecture-agent.json` file in the target repository when you want to add extra ignored directories:

```json
{
  "ignoredDirs": ["legacy", "sandbox", "tmp"]
}
```

This is useful when a repository contains old folders that should not influence the analysis.

## Configuration

Environment variables:

- `LLM_PROVIDER`
- `LLM_MODEL`
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
python -m architecture_agent.cli analyze ./some-repo --seed 7 --output analysis.md
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
