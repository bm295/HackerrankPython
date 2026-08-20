# ADR-002 - Separate deterministic analysis from research

## Context
Repository traversal, filtering, and topic sampling should be reproducible.

## Decision
Filesystem scanning and topic selection are deterministic. Web research is isolated behind a provider function.

## Consequences
- Easier testing
- Repeatable runs with a seed
- Research can fail independently of local analysis
