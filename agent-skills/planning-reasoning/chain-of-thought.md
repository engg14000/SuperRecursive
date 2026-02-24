---
description: "Step-by-step reasoning technique for complex problem-solving"
author: "SuperRecursive"
tags: ["reasoning", "chain-of-thought", "CoT"]
verified: true
version: "1.0"
---

# Chain-of-Thought (CoT) Reasoning

## Overview

Chain-of-Thought prompting elicits step-by-step reasoning from AI models, dramatically improving performance on complex tasks like math, logic, code analysis, and multi-step planning.

## Core Prompt

```
When solving complex problems, think step-by-step before providing your answer.

## Process
1. RESTATE the problem in your own words to confirm understanding
2. IDENTIFY the key variables, constraints, and relationships
3. BREAK DOWN the solution into logical steps
4. EXECUTE each step, showing your work
5. VERIFY the final answer by checking against the original requirements
6. PRESENT the solution with confidence level

## Format
Think step-by-step:
Step 1: [reasoning]
Step 2: [reasoning]
...
Step N: [reasoning]

Therefore: [final answer]
Confidence: [high/medium/low]
```

## Variants

### Zero-Shot CoT
Simply add "Let's think step by step" to any prompt.

```
Q: If a program has 15 modules, each taking 3 days to code and 1 day to test,
   but 5 modules can be developed in parallel, how long will the project take?

A: Let's think step by step.
   Step 1: Total modules = 15, each needs 3 + 1 = 4 days
   Step 2: With 5 parallel tracks, we need 15/5 = 3 rounds
   Step 3: Each round = 4 days (3 coding + 1 testing)
   Step 4: Total = 3 rounds × 4 days = 12 days
   
   Therefore: The project will take 12 days.
```

### Few-Shot CoT
Provide examples of step-by-step reasoning before the actual question.

### Self-Consistent CoT
Generate multiple reasoning chains and pick the most common answer.

```
Chain 1: ... → Answer: A
Chain 2: ... → Answer: A  
Chain 3: ... → Answer: B

Consensus: Answer A (2/3 chains agree)
```

## Best For

| Task Type | CoT Improvement | Example |
|-----------|:-:|---------|
| Math problems | ⭐⭐⭐⭐⭐ | Multi-step calculations |
| Code debugging | ⭐⭐⭐⭐ | Trace execution flow |
| Logic puzzles | ⭐⭐⭐⭐⭐ | Constraint satisfaction |
| Architecture | ⭐⭐⭐⭐ | Design trade-off analysis |
| Simple lookups | ⭐ | "What color is the sky?" — CoT unnecessary |

## Integration with Agent Skills

CoT enhances virtually every other skill:
- **Task Decomposition**: Think through dependencies step-by-step
- **Error Recovery**: Trace backwards to find root cause
- **Self-Verification**: Systematically check each requirement
