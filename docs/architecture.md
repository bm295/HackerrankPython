# Architecture Explorer Agent

## Context
This repository contains a CLI agent that analyzes a target repository in read-only mode, selects one architecture topic, performs web research, and produces evidence-backed recommendations.

## Building Blocks
- CLI
- Config loader
- Repository scanner
- Architecture snapshot builder
- Repository profiler, online topic discovery, catalogue fallback, and selector
- Research provider
- Evidence finder
- Report generator

## Runtime Flow
1. Parse CLI arguments.
2. Scan repository with ignore rules and file limits.
3. Build a repository snapshot.
4. Build search queries from repository signals.
5. Discover and rank topics from online results, or use the catalogue fallback.
6. Research topic sources.
6. Match repository evidence.
7. Render markdown or JSON.

## External Interfaces
- Local repository path
- Git repository URL as a future extension
- Web sources for research

## Important Architectural Decisions
- Read-only analysis by default.
- Staged context construction.
- Deterministic scanning and seeded topic selection.
- Research and LLM-style boundaries are replaceable.
