# Strategy workbook

## Discovery
Capture: business outcome and owner; user workflow; target date; current baseline; repository evidence; data permissions and freshness; integration constraints; workload distribution; quality and latency targets; budget and team capacity; operations and decision authority.
Keep unknown fields explicit. Ask only questions that materially affect a decision.

## Portfolio
| Use case | Owner | Baseline | Outcome metric | Data readiness | Error impact | Effort range | Dependencies | Pilot/hold/stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Separate enabling platform work from direct business benefits to avoid double-counting value.

## Evidence and scenarios
| Claim | Fact/assumption/forecast/recommendation | Evidence and date | Confidence | Limitation | Decision affected |
| --- | --- | --- | --- | --- | --- |

For baseline, accelerated, and constrained scenarios, state the changing assumption, consequences, common investments, optional investments, leading indicators and pivot trigger. No numerical probability without a defensible basis.

## Alternatives
First list pass/fail/unknown for mandatory requirements. Keep options with unresolved mandatory constraints provisional.
Then score feasible options on business fit, quality, latency, TCO, operability, security, integration and reversibility as applicable.
Use a proposed 1–5 scale with explicit anchors and weights totaling 100%; compute weighted score as sum(weight × score)/100. Mark missing scores unknown rather than inventing neutral scores. Test whether plausible changes in key weights or estimates change the winner. Explain the decisive trade-off in prose.

## Architecture decision record
- Decision ID, title, date, owner role and proposed/accepted/superseded status.
- Context, quality scenario and constraints.
- Options, evidence and why alternatives were rejected.
- Decision, assumptions and consequences.
- Verification plan, dependencies and migration sequence.
- Reversibility, exit cost and reconsideration trigger.

Never mark an ADR accepted without an actual authorized decision.

## Quality scenario and release gate
| Stimulus and environment | Affected boundary | Expected response | Metric and proposed threshold | Measurement dataset/load | Owner | Failure response |
| --- | --- | --- | --- | --- | --- | --- |

Keep offline quality separate from business benefit. Prevent evaluation leakage and preserve dataset provenance. Segment by tenant, workflow and difficult cases when appropriate. Use sample size and uncertainty to qualify conclusions. Averages must not hide tail latency or severe failures.

## Economics
- Define accounting period and currency.
- Inference cost = input tokens / pricing unit × input rate + output tokens / pricing unit × output rate, plus applicable modality, caching and hosting charges.
- Monthly TCO = variable runtime + fixed infrastructure + amortized engineering/migration + operations/security/evaluation + human review/support.
- Cost per successful task = attributable total cost / successfully completed business tasks; include retries, failures and fallback costs in the numerator.
- Net benefit = measured incremental benefit minus incremental TCO; avoid counting time saved as cash savings without a credible realization mechanism.
- Break-even volume = incremental fixed cost / positive per-task contribution, only when the linear assumptions hold.
- Show low/base/high workload and price assumptions, peak capacity, currency/price date, and sensitivity. Do not use token price alone to justify a platform choice.

## Roadmap 2027
| ID | Period | 2028 outcome or decision | Owner role | Prerequisites | Deliverable | Completion gate | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Group by quarter and use monthly windows where useful. Schedule prerequisites before their dependents. Record phase-level staffing/effort and cost assumptions, plus stop, pivot or rollback conditions. Include pilot, production hardening, scaling and optimization only if time permits. Allocate the first 90 days from the actual current date and shorten to the deadline if needed.

## Source register and revision history
| Source ID | Title and link/path | Published/version | Inspected | Claim and limitation | Decisions/tasks affected |
| --- | --- | --- | --- | --- | --- |

| Revision date | Source IDs | Decisions/tasks changed | Rationale and follow-up |
| --- | --- | --- | --- |

## Review prompts
- What evidence would make the recommendation wrong?
- Does the simplest non-AI baseline satisfy the outcome?
- Can the model read or act beyond the user's permissions?
- What happens after an ambiguous timeout on a write?
- Can tenant-restricted content leak through retrieval, caches, logs or evaluation data?
- Can users complete the workflow during model/provider failure?
- Can a model change pass quality gates and still worsen business outcomes?
- Which decision is expensive to reverse, and what experiment reduces that uncertainty?
- What observable threshold triggers scaling, pausing, migration or retirement?

## Context architecture decision worksheet
Use [context-architecture.md](context-architecture.md) for RAG and agent strategies.
- Identify authoritative records, curated knowledge, session/durable memory and active inference context.
- Complete the information contract: source, permissions, version/event time, freshness, retention/deletion, conflict rule and unavailable-source behavior.
- Record context assembly boundaries, input/output token allocation, compression risks and cache invalidation.
- Compare bounded retrieval against proposed context lifecycle changes on identical held-out tasks and workload.
- Include stale/conflicting facts, cross-tenant access, revoked permissions, deletion propagation, poisoned memory and compression-loss cases in quality gates.
- Capture quality, latency and cost trade-offs in the ADR; set an owner and a measurable stop/pivot trigger.
- Label the context engineering trend as a forecast; record supporting and contrary evidence, uncertainty and the decision it would change.
