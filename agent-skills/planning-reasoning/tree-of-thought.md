---
description: "Branching exploration of multiple solution paths for optimal problem-solving"
author: "SuperRecursive"
tags: ["reasoning", "tree-of-thought", "ToT", "exploration"]
verified: true
version: "1.0"
---

# Tree-of-Thought (ToT) Reasoning

## Overview

Tree-of-Thought extends Chain-of-Thought by exploring multiple reasoning paths simultaneously, evaluating each branch, and pursuing the most promising ones. Ideal for problems where the first approach isn't guaranteed to be best.

## Architecture

```
                    [Problem]
                   /    |    \
                  /     |     \
            [Path A] [Path B] [Path C]
            Score:8   Score:6   Score:9
              |                   |
           [A.1]              [C.1]
           Score:7            Score:9
              |                   |
           [A.2]              [C.2] ← WINNER
           Score:6            Score:10
```

## System Prompt

```
You are a deliberative AI that explores multiple solution paths before committing 
to an approach. Use Tree-of-Thought reasoning for complex problems.

## Process

1. GENERATE: Propose 3 distinct approaches to the problem
2. EVALUATE: Score each approach (1-10) on:
   - Feasibility: Can this actually work?
   - Efficiency: How optimal is the solution?
   - Risk: What could go wrong?
   - Simplicity: How easy to implement/maintain?
3. SELECT: Choose the top 2 scoring approaches
4. EXPAND: Develop each selected approach one step further
5. RE-EVALUATE: Score the expanded approaches
6. COMMIT: Choose the highest-scoring path and execute fully
7. REFLECT: Note what made the winning path better (for future reference)

## Output Format

### Branch Exploration

**Branch A**: [Approach description]
| Criterion | Score |
|-----------|:-----:|
| Feasibility | 8/10 |
| Efficiency | 7/10 |
| Risk | 6/10 |
| Simplicity | 9/10 |
| **Total** | **30/40** |

**Branch B**: [Approach description]
...

### Decision
Selected: Branch [X] (score: [Y]/40)
Rationale: [Why this branch wins]
```

## Example: Designing a Cache Layer

### Problem
> "Design a caching strategy for our API that handles high read traffic with minimal stale data"

### Tree Exploration

```
Branch A: Redis with TTL-based expiration
├── Feasibility: 9/10 (mature, well-documented)
├── Efficiency: 7/10 (TTL may serve stale data until expiry)
├── Risk: 5/10 (Redis as SPOF, needs clustering)
├── Simplicity: 8/10 (straightforward implementation)
└── Total: 29/40

Branch B: Application-level cache with write-through
├── Feasibility: 8/10 (no new infrastructure)
├── Efficiency: 9/10 (always fresh on writes)
├── Risk: 7/10 (memory pressure on app servers)
├── Simplicity: 6/10 (complex invalidation logic)
└── Total: 30/40

Branch C: CDN edge caching with stale-while-revalidate
├── Feasibility: 9/10 (Cloudflare/Vercel built-in)
├── Efficiency: 9/10 (fast globally, background refresh)
├── Risk: 8/10 (well-tested pattern)
├── Simplicity: 9/10 (config-based, minimal code)
└── Total: 35/40 ← WINNER
```

### Expansion of Winner (Branch C)
```
C.1: CDN with stale-while-revalidate headers
     Cache-Control: public, max-age=60, stale-while-revalidate=300
     + API endpoints return ETag headers for validation
     + Critical endpoints: shorter max-age (10s)
     + Static content: longer max-age (3600s)
     Score: 36/40

Selected: Branch C.1
```

## When to Use ToT vs CoT

| Scenario | Use CoT | Use ToT |
|----------|:-------:|:-------:|
| Clear, single solution path | ✅ | ❌ |
| Multiple valid approaches exist | ❌ | ✅ |
| High stakes decision | ❌ | ✅ |
| Time-critical (need quick answer) | ✅ | ❌ |
| Architecture/design decisions | ❌ | ✅ |
| Debugging (clear error) | ✅ | ❌ |
| Debugging (unclear root cause) | ❌ | ✅ |

## Pruning Strategies

- **Score threshold**: Drop branches scoring below 50% of theoretical max
- **Early termination**: Stop exploring a branch if any criterion scores ≤ 3/10
- **Budget limit**: Explore maximum 3-5 branches (more is diminishing returns)
- **Depth limit**: Expand at most 3 levels deep before committing
