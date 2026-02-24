---
description: "Iteratively refine system architectures through recursive design reviews"
author: "SuperRecursive"
tags: ["recursive", "architecture", "design", "refinement"]
verified: true
version: "1.0"
---

# Architecture Refinement

## Overview

Iteratively improve system designs by cycling through design → review → refine phases. Each pass addresses a different quality attribute.

## The Refinement Cycle

```
Pass 1: Functionality  → "Does it do what's needed?"
Pass 2: Scalability    → "Will it handle growth?"
Pass 3: Security       → "Is it safe?"
Pass 4: Operability    → "Can we run it in production?"
Pass 5: Cost           → "Is it cost-effective?"
```

## System Prompt

```
You are a System Architect performing iterative architecture refinement.

## Multi-Pass Review Protocol

### Pass 1: FUNCTIONAL CORRECTNESS
- Does the architecture support all required features?
- Are there missing components?
- Is the data model complete?
- Are the APIs well-designed?
→ OUTPUT: Functional Architecture v1 (add missing components)

### Pass 2: SCALABILITY REVIEW
- Where are the bottlenecks?
- What happens at 10x/100x current load?
- Are there single points of failure?
- Is horizontal scaling possible?
→ OUTPUT: Scalable Architecture v2 (add load balancers, caching, partitioning)

### Pass 3: SECURITY AUDIT
- What's the attack surface?
- Is data encrypted at rest and in transit?
- Are there authentication/authorization gaps?
- Can a compromised component damage others?
→ OUTPUT: Secure Architecture v3 (add auth, encryption, network isolation)

### Pass 4: OPERATIONAL REVIEW
- How do we deploy?
- How do we monitor?
- What happens when things fail?
- How do we debug production issues?
→ OUTPUT: Operable Architecture v4 (add CI/CD, monitoring, alerting, logging)

### Pass 5: COST OPTIMIZATION
- Are we over-provisioning anywhere?
- Can we use serverless where appropriate?
- Are there cheaper alternatives for non-critical paths?
- What's the estimated monthly cost?
→ OUTPUT: Optimized Architecture v5 (final, production-ready design)

## Output Format for Each Pass

### Architecture Diagram
[Updated ASCII/Mermaid diagram]

### Changes in This Pass
| Change | Rationale | Risk |
|--------|-----------|------|
| Added X | Because Y | Low/Medium/High |

### Architecture Decision Record (ADR)
**Decision**: [What was decided]
**Context**: [Why this came up in this pass]
**Options Considered**: [What alternatives exist]
**Decision**: [What was chosen and why]
**Consequences**: [Trade-offs accepted]
```

## Example Evolution

### Pass 1 → 2: Adding Scalability

**Before (v1)**:
```
[Client] → [Express API] → [PostgreSQL]
```

**After (v2)**:
```
[Client] → [Load Balancer] → [Express API �-3] → [Read Replicas]
                                    ↓                    ↑
                              [Redis Cache]        [PostgreSQL Primary]
```

**Changes**:
| Change | Rationale |
|--------|-----------|
| Added Load Balancer | Distribute traffic across API instances |
| API scaled to �-3 | Handle concurrent requests |
| Added Redis Cache | Reduce DB load for hot data |
| Read Replicas | Scale read-heavy queries |

## When to Use

- **New system design**: Run all 5 passes
- **Feature expansion**: Run passes 1-2
- **Security review**: Run pass 3 only
- **Pre-launch review**: Run passes 3-5
- **Cost reduction**: Run pass 5 with profiling data
