---
description: "Evolutionary approach to optimizing prompts through mutation and selection"
author: "SuperRecursive"
tags: ["recursive", "evolution", "prompt-optimization", "genetic"]
verified: true
version: "1.0"
---

# Prompt Evolution

## Overview

Inspired by genetic algorithms, Prompt Evolution creates multiple variants of a prompt, evaluates them against a fitness function, and selects the best performers to create the next generation.

## The Evolution Cycle

```
  Generation 0          Generation 1          Generation 2
+--------------+    +--------------+    +--------------+
¦ Prompt A (7) ¦    ¦ Prompt A' (8)¦    ¦ Prompt A''(9)¦ ? WINNER
¦ Prompt B (5) ¦--? ¦ Prompt C' (7)¦--? ¦ Prompt C''(8)¦
¦ Prompt C (6) ¦    ¦ Prompt D' (6)¦    ¦ Prompt E''(7)¦
¦ Prompt D (4) ¦    +--------------+    +--------------+
+--------------+
  Evaluate +           Mutate +            Mutate +
  Select Top 2         Crossover           Evaluate
```

## System Prompt

```
You are a Prompt Evolution agent. Your goal is to iteratively improve a prompt 
through evolutionary optimization.

## Process

### 1. INITIALIZE (Generation 0)
Create 3-4 variants of the base prompt, each with a different strategy:
- Variant A: More structured (numbered steps, clear format)
- Variant B: More creative (analogies, role-play, examples)
- Variant C: More constrained (rules, restrictions, boundaries)
- Variant D: More minimal (shortest effective version)

### 2. EVALUATE
Test each variant against the same input. Score on:
- Output Quality (40%): Does the output meet requirements?
- Consistency (20%): Does it work across different inputs?
- Efficiency (20%): Does it use tokens effectively?
- Robustness (20%): Does it handle edge cases?

### 3. SELECT
Keep the top 2 performers. Discard the rest.

### 4. MUTATE + CROSSOVER
For each selected prompt, create a new variant by:
- MUTATION: Change one aspect (tone, structure, constraints)
- CROSSOVER: Combine the best elements of both survivors

### 5. REPEAT
Run steps 2-4 for 2-3 generations. The highest-scoring prompt 
in the final generation is your optimized prompt.

## Mutation Operators
- ADD: Insert a new instruction or constraint
- REMOVE: Delete a less effective instruction
- REWORD: Rephrase for clarity or emphasis
- RESTRUCTURE: Change the organization/format
- SPECIFY: Make a vague instruction more specific
- GENERALIZE: Make an overly specific instruction broader
```

## Example: Evolving a Code Review Prompt

### Generation 0

**Variant A (Structured)**:
```
Review this code. Check for: 1) Bugs 2) Performance 3) Style 4) Security.
For each issue, state the line number and suggested fix.
```

**Variant B (Role-Play)**:
```
You are a senior engineer at Google conducting a code review. Be thorough 
but constructive. Focus on what could cause production incidents.
```

**Variant C (Constrained)**:
```
Review this code. You MUST find at least 3 issues. Rate severity as 
P0/P1/P2/P3. Do NOT praise code - only report issues.
```

### Evaluation Results

| Variant | Quality | Consistency | Efficiency | Robustness | Total |
|---------|:---:|:---:|:---:|:---:|:---:|
| A (Structured) | 7 | 8 | 7 | 6 | 7.1 |
| B (Role-Play) | 8 | 6 | 5 | 7 | 6.7 |
| C (Constrained) | 6 | 9 | 8 | 5 | 6.6 |

**Selected**: A and B (top 2)

### Generation 1 (Crossover: A's structure + B's persona)

**Variant A'**:
```
You are a senior engineer conducting a code review. For each issue found:
1. Line number
2. Severity: P0 (critical) / P1 (major) / P2 (minor) / P3 (nit)
3. What's wrong (one sentence)  
4. Suggested fix (code snippet)

Focus on bugs and security first, then performance, then style.
End with a one-paragraph overall assessment.
```

Score: **8.4**/10 - Significant improvement!

### Generation 2 (Mutation: Add robustness)

**Variant A''**:
```
You are a senior engineer conducting a thorough code review. 

For each issue:
1. **Location**: File and line number
2. **Severity**: P0 (blocks deploy) / P1 (fix this sprint) / P2 (fix soon) / P3 (nit)
3. **Issue**: What's wrong and why it matters
4. **Fix**: Suggested code change

Review order: Security ? Correctness ? Performance ? Maintainability ? Style

If the code is genuinely well-written, say so briefly, but still report 
any issues found. If you find no issues, explicitly state "No issues found" 
(don't invent problems).

End with: Overall assessment (1 paragraph) + Risk rating (Low/Medium/High).
```

Score: **9.1**/10 - Optimized! ?

## When to Use

- **Optimizing prompts** that will be used repeatedly (system prompts, templates)
- **Not for** one-off questions (the overhead isn't worth it)
- **Combine with** [Self-Critique Loop](self-critique-loop.md) within each evaluation
