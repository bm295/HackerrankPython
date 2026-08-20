# ADR-001 - Read-only repository analysis

## Context
The agent must inspect arbitrary repositories without modifying them.

## Decision
Repository inputs are treated as read-only data. The analyzer never writes to the target repository.

## Consequences
- Safer analysis
- Better trust boundaries
- Refactoring must be applied separately when requested
