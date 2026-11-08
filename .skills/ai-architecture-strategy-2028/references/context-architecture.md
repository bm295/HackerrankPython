# Context, memory and knowledge architecture

## Source and interpretation
- Source: Adi Polak, “Systemic Approach to Memory, Knowledge, and Context in Agentic AI Architectures”, InfoQ, published 2026-11-02.
- URL: https://www.infoq.com/articles/agentic-ai-context-memory-knowledge/
- Inspected: 2026-11-08.
- Treat this author-written architecture article as a design perspective, not a benchmark or proof of a 2028 forecast.

The article distinguishes active context, persistent memory and curated knowledge. It proposes selecting information, arranging it for inference, compressing it, and expiring or refreshing it. It also discusses tiered memory, combining historical and live information, and controlling token use. Its warnings include excessive context, stale information, generic retrieval and uncontrolled memory growth.

## Engineering recommendations for applying the perspective
The following are this skill's design and validation recommendations; do not attribute them as measured results from the article.

### Define boundaries and authority
- Define context as the bounded input assembled for an inference step; memory as persisted interaction or task state; knowledge as curated domain reference material with provenance.
- Identify the authoritative system for each business fact. Memory and generated summaries must not silently replace transactional records.
- Choose working, session and durable storage only where the workflow needs them. Do not require vector storage, graphs, a separate service or multiple agents.
- Keep policy enforcement and transaction authorization outside probabilistic reasoning, even when policy descriptions appear in context.

### Specify the information contract
For every relevant information class, record:
| Information class | Authority/source | Tenant/access scope | Event time/version | Freshness limit | Retention/deletion | Conflict rule | Failure behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |

- Preserve provenance through summaries and derived stores. Distinguish observation time from ingestion time.
- Make current explicit instructions take precedence over inferred preferences unless mandatory policy prevents it.
- Define what happens when sources disagree, refresh fails or the authoritative service is unavailable. Revalidate volatile facts before consequential actions.
- Propagate permission revocation and deletion to derived memories, summaries and caches. Prevent untrusted tool content from becoming durable instructions.

### Design context assembly
- Compare a simple bounded retrieval baseline with more elaborate context assembly before adding components.
- Document candidate retrieval, authorization filtering, relevance/freshness ranking, deduplication, structured placement and budget enforcement.
- Reserve space for instructions, tool results and output. State what is dropped when the budget is exceeded.
- If compression is used, preserve identifiers, constraints, negation and unresolved uncertainty; retain a way to retrieve original evidence.
- Define cache keys and invalidation using tenant, permissions, source version and task needs. Bound asynchronous update lag explicitly.
- Specify expiration by data class and business requirements; never invent universal TTL values.

### Validate with workload-specific evidence
Compare alternatives on the same held-out tasks and load:
- Task success and groundedness, alongside context tokens, p50/p95 latency and cost per successful task.
- Changed facts, conflicting sources, missing evidence and failures of refresh.
- Cross-tenant retrieval, revoked permissions, deletion propagation and poisoned memory/tool outputs.
- Loss of critical details during compression and conflicts between historical preferences and current requests.
- Cache misses, delayed updates and concurrent changes.

Propose thresholds until stakeholders agree or measurements establish them. A smaller context is not automatically better; compression may lose essential evidence. Context management cannot guarantee factual correctness or eliminate model error. Perplexity or distribution similarity alone does not establish semantic fidelity or safe business behavior.

## Use as a 2028 signal
Record “greater investment in context lifecycle engineering” as a forecast hypothesis, not an observed future. Explain how it changes architecture decisions under baseline, accelerated and constrained scenarios. Seek independent evidence and counterexamples; a single article does not establish industry adoption. Reconsider investment if controlled experiments show no material quality, cost or latency benefit over the simpler baseline.
