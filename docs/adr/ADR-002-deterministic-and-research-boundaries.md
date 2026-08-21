# ADR-002 - Separate deterministic analysis from research

## Context
Repository traversal, filtering, and topic sampling should be reproducible.

## Decision
Filesystem scanning and catalogue topic selection are deterministic. Online topic discovery and web research are isolated behind provider interfaces. Hybrid mode falls back to the deterministic catalogue when discovery is unavailable.

## Consequences
- Easier testing
- Repeatable runs with a seed
- Research can fail independently of local analysis
- Search providers can be mocked for repeatable tests
