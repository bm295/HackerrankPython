# Using Architecture Explorer Agent On Any Repository

This guide shows the shortest path for using the agent on any codebase.

## Local repository

```bash
python -m architecture_agent.cli analyze /path/to/repository
```

Windows example:

```bash
python -m architecture_agent.cli analyze D:\Code\my-service
```

## Remote Git repository

```bash
python -m architecture_agent.cli analyze https://github.com/org/project.git
```

The agent clones the repository into a temporary directory, analyzes it there, and does not modify the original target.

## Call it while standing inside another repo

If you are currently inside another repository and want to analyze that repository or a different one, you do not need to leave the folder.

### Option 1: Use `npm --prefix`

From the target repository directory:

```bash
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze .
```

### Option 2: Use the installed console command

```bash
architecture-agent analyze .
```

### Option 3: Install the command once with pip

From the agent repo:

```bash
python -m pip install -e D:\Code\HackerrankPython
```

Then from any other repository:

```bash
architecture-agent analyze .
```

## Use it from Codex as a plugin

This machine now has a local Codex plugin named `architecture-explorer-agent`.

In a new Codex thread, ask for:

- `Analyze the current repository with Architecture Explorer Agent`
- `Run Architecture Explorer Agent on D:\Code\SomeRepo`
- `Analyze https://github.com/org/project.git with Architecture Explorer Agent`

The plugin skill delegates to:

```powershell
python D:\Code\HackerrankPython\architecture_agent\cli.py analyze <target>
```

## Make the run repeatable

```bash
python -m architecture_agent.cli analyze ./repo --seed 42
```

Use the same seed to keep topic selection stable as long as the catalogue does not change.

## Choose a specific topic

```bash
python -m architecture_agent.cli analyze ./repo --topic "Dependency Inversion"
```

This bypasses random topic selection but still keeps repository applicability checks and evidence matching.

## JSON output

```bash
python -m architecture_agent.cli analyze ./repo --json
```

## Save output to a file

```bash
python -m architecture_agent.cli analyze ./repo --output report.md
```

## Ignore extra folders in a target repo

Add a `.architecture-agent.json` file to the repository being analyzed:

```json
{
  "ignoredDirs": ["vendor", "legacy", "tmp"]
}
```

## What to expect

Each run should return:

- repository snapshot
- selected architecture topic
- online research sources
- repository evidence
- one concrete application point
- suggested improvement
- trade-offs
- confidence level

## Limitations

- Git URLs require `git` to be installed.
- Research depends on network access.
- The current implementation uses heuristic evidence matching.
