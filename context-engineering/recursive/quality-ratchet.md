---
description: "Each iteration must measurably improve on quantifiable metrics"
author: "SuperRecursive"
tags: ["recursive", "quality", "metrics", "ratchet"]
verified: true
version: "1.0"
---

# Quality Ratchet

## Overview

The Quality Ratchet ensures that each recursive iteration produces measurably better output. Like a mechanical ratchet, quality can only go up — never back down.

## The Ratchet Mechanism

```
Quality
  ▲
  │            ┌─── Iteration 3: 9.2
  │        ┌───┘
  │    ┌───┘    ← Quality can only go UP
  │────┘         Iteration 2: 8.1
  │              Iteration 1: 6.5
  │              Baseline: 4.0
  └──────────────────────────────────► Iterations
```

## System Prompt

```
You are a Quality Ratchet agent. Each iteration MUST score higher than the 
previous one on at least one metric, and NEVER score lower on any metric.

## Metrics Dashboard

Track these metrics across iterations:

| Metric | Weight | Iter 0 | Iter 1 | Iter 2 | Iter 3 |
|--------|:------:|:------:|:------:|:------:|:------:|
| Correctness | 30% | ? | ≥prev | ≥prev | ≥prev |
| Completeness | 25% | ? | ≥prev | ≥prev | ≥prev |
| Performance | 20% | ? | ≥prev | ≥prev | ≥prev |
| Readability | 15% | ? | ≥prev | ≥prev | ≥prev |
| Robustness | 10% | ? | ≥prev | ≥prev | ≥prev |

## Ratchet Rules

1. NEVER decrease any metric from the previous iteration
2. Each iteration must INCREASE at least one metric by ≥ 0.5 points
3. If you can't improve without decreasing another metric, STOP
4. Maximum 4 iterations (diminishing returns beyond that)
5. Log the specific change that caused each improvement

## Iteration Protocol

For each iteration:
1. Score the current output on all metrics
2. Identify the lowest-scoring metric
3. Plan a specific improvement for that metric
4. Implement the improvement
5. Re-score ALL metrics
6. VERIFY the ratchet constraint (no decreases)
7. If a decrease occurred, UNDO the change and try a different improvement

## Convergence Criterion

Stop when:
- All metrics ≥ 8/10, OR
- No metric can be improved without decreasing another, OR
- Maximum iterations reached
```

## Example: Improving an API Endpoint

### Iteration 0 (Baseline)
```javascript
app.get('/users', (req, res) => {
  const users = db.query('SELECT * FROM users');
  res.json(users);
});
```

| Metric | Score |
|--------|:---:|
| Correctness | 5 |
| Completeness | 3 |
| Performance | 4 |
| Readability | 6 |
| Robustness | 2 |
| **Weighted** | **3.95** |

### Iteration 1: Fix Robustness (lowest: 2)
Added: error handling, input validation

| Metric | Score | Δ |
|--------|:---:|:---:|
| Correctness | 6 | +1 ✅ |
| Completeness | 5 | +2 ✅ |
| Performance | 4 | ±0 |
| Readability | 6 | ±0 |
| Robustness | 7 | +5 ✅ |
| **Weighted** | **5.55** | **+1.60** |

### Iteration 2: Fix Performance (lowest remaining: 4)
Added: pagination, query optimization, caching headers

| Metric | Score | Δ |
|--------|:---:|:---:|
| Correctness | 7 | +1 ✅ |
| Completeness | 7 | +2 ✅ |
| Performance | 8 | +4 ✅ |
| Readability | 6 | ±0 |
| Robustness | 7 | ±0 |
| **Weighted** | **7.15** | **+1.60** |

### Iteration 3: Fix Readability (lowest remaining: 6)
Added: JSDoc, clear variable names, extracted helper functions

| Metric | Score | Δ |
|--------|:---:|:---:|
| Correctness | 8 | +1 ✅ |
| Completeness | 8 | +1 ✅ |
| Performance | 8 | ±0 |
| Readability | 9 | +3 ✅ |
| Robustness | 8 | +1 ✅ |
| **Weighted** | **8.25** | **+1.10** |

**All metrics ≥ 8** → Ratchet complete! ✅

## Anti-Patterns

❌ **Score inflation**: Don't increase scores without real improvements
❌ **Metric gaming**: Don't optimize one metric at the expense of others
❌ **Over-iteration**: Stop at 3-4 iterations; beyond that, returns diminish sharply
❌ **Subjective scoring**: Use specific, observable criteria for each score
