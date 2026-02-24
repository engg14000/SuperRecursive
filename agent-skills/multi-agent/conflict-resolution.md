---
description: "Conflict resolution strategies when multiple agents disagree"
author: "SuperRecursive"
tags: ["multi-agent", "conflict-resolution", "consensus"]
verified: true
version: "1.0"
---

# Conflict Resolution

## Overview

In multi-agent systems, agents may produce conflicting outputs. This framework provides systematic strategies for resolving disagreements.

## When Conflicts Arise

| Scenario | Example | Resolution Type |
|----------|---------|----------------|
| Design disagreement | Architect says SQL, Coder prefers NoSQL | Criteria-based evaluation |
| Quality dispute | Reviewer rejects, Coder defends | Standards-based review |
| Priority conflict | Two tasks claim highest priority | Cost-benefit analysis |
| Resource contention | Two agents need same resource | Scheduling/sequencing |
| Approach divergence | Different algorithms proposed | Benchmark comparison |

## Resolution Protocol

```
CONFLICT RESOLUTION PROTOCOL:

1. IDENTIFY: What exactly is the disagreement?
   - Agent A position: [summary]
   - Agent B position: [summary]
   - Core difference: [root of disagreement]

2. GATHER EVIDENCE:
   - Agent A rationale: [arguments with evidence]
   - Agent B rationale: [arguments with evidence]
   - External references: [documentation, benchmarks, best practices]

3. EVALUATE AGAINST CRITERIA (weighted):
   - Requirements alignment (30%): Which better satisfies user needs?
   - Simplicity (20%): Which is easier to implement and maintain?
   - Performance (15%): Which performs better under expected load?
   - Risk (15%): Which has fewer potential failure modes?
   - Extensibility (10%): Which is easier to extend later?
   - Team consensus (10%): Which do more agents prefer?

4. DECIDE:
   - Calculate weighted scores
   - Choose the higher-scoring approach
   - If scores within 5%: prefer the simpler option

5. COMMUNICATE:
   - Announce the decision with rationale
   - Acknowledge the merits of the rejected approach
   - Document the decision for future reference

6. ADAPT:
   - Losing agent modifies their output to align
   - Winning approach may incorporate elements of the other
```

## Decision Record Template

```markdown
## Decision Record: [Title]

**Date**: 2026-02-24
**Conflict**: [Brief description]
**Agent A (Architect)**: [Position]
**Agent B (Coder)**: [Position]

| Criterion | Weight | Agent A Score | Agent B Score |
|-----------|--------|:---:|:---:|
| Requirements | 30% | 8/10 | 7/10 |
| Simplicity | 20% | 6/10 | 9/10 |
| Performance | 15% | 9/10 | 7/10 |
| Risk | 15% | 7/10 | 8/10 |
| Extensibility | 10% | 8/10 | 6/10 |
| Consensus | 10% | 5/10 | 5/10 |
| **Weighted Total** | | **7.35** | **7.25** |

**Decision**: Agent A's approach (by narrow margin)
**Rationale**: Requirements alignment and performance edge are critical for this use case
**Incorporated from B**: Adopted B's simpler error handling pattern
```
