# Context Engineering Patterns

> A pattern catalog for structuring AI context - from simple to advanced.

## Pattern Hierarchy

```
Level 1: Basic          ? Simple role + task
Level 2: Structured     ? Role + guidelines + format  
Level 3: Contextual     ? + relevant documents/code
Level 4: Engineered     ? + attention management + memory
Level 5: SuperRecursive ? + self-improvement loops
```

## Level 1: Basic Patterns

### Direct Instruction
```
Translate this text to Spanish: [text]
```
**Use when**: Simple, well-defined tasks.

### Role Assignment
```
You are a [specific role]. [task].
```
**Use when**: You need domain expertise.

---

## Level 2: Structured Patterns

### The CRAFT Framework
```
Context: [Background information]
Role: [Who the AI should be]
Action: [What to do]
Format: [How to structure output]
Target: [Who the output is for]
```

### Guidelines Block
```
## Role
You are [role].

## Guidelines
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]

## Output Format
[Specify structure]
```

---

## Level 3: Contextual Patterns

### Document Injection
```
## Reference Material
<documents>
[paste relevant docs/code here]
</documents>

## Task
Using the reference material above, [task].
```

### Code Context
```
## Codebase Context
Project: [name] ([language] + [framework])
Architecture: [pattern]
Current file: [filename]

## Relevant Code
```[language]
[paste code]
```

## Task
[What to do with this code]
```

---

## Level 4: Engineered Patterns

### Attention Anchoring
Place critical instructions at the **start** AND **end** of your context (the U-shaped attention pattern):
```
CRITICAL: [Most important rule]

[... middle content ...]

REMINDER: [Repeat the most important rule]
```

### Progressive Disclosure
```
## Overview (Always read)
[High-level summary]

## Details (Read when relevant)
[Detailed specifications]

## Reference (Look up as needed)
[API docs, schemas, examples]
```

### Zone-Based Architecture
```
=== ZONE 1: IDENTITY (Always Active) ===
[Role and core behavior]

=== ZONE 2: CURRENT TASK (This Session) ===
[What we're working on right now]

=== ZONE 3: PROJECT CONTEXT (Reference) ===
[Codebase, docs, conventions]

=== ZONE 4: EXAMPLES (As Needed) ===
[Input/output examples]
```

### Token Budget Allocation
```
Total context: 200K tokens

Allocation:
+-- System prompt:     5K (2.5%)   - Role + rules
+-- Task description:  2K (1%)     - Current objective
+-- Critical context: 20K (10%)    - Most relevant code/docs
+-- Supporting docs:  50K (25%)    - Related reference material
+-- Examples:         10K (5%)     - Input/output pairs
+-- Response space:  113K (56.5%)  - Room for the AI to think
```

---

## Level 5: SuperRecursive Patterns

### Self-Critique Loop
```
1. Generate initial response
2. Critique your response on [dimensions]
3. Score each dimension (1-10)
4. If any score < 7, improve that dimension
5. Repeat until all scores = 7
```
? See [Self-Critique Loop](../context-engineering/recursive/self-critique-loop.md)

### Quality Ratchet
```
After each output, verify quality has NOT decreased:
- Compare to previous version
- Score on [metrics]
- If score decreased, revert and try different approach
- Quality can only go UP, never down
```
? See [Quality Ratchet](../context-engineering/recursive/quality-ratchet.md)

### Prompt Evolution
```
1. Start with multiple prompt variants
2. Test each against evaluation criteria
3. Keep the best, mutate to create new variants
4. Repeat for N generations
5. Best prompt wins
```
? See [Prompt Evolution](../context-engineering/recursive/prompt-evolution.md)

## Pattern Selection Guide

| Your Situation | Recommended Pattern | Level |
|:---|---|:---:|
| Simple question | Direct Instruction | 1 |
| Need expertise | Role Assignment | 1 |
| Complex task, specific format | CRAFT Framework | 2 |
| Working with existing code | Code Context | 3 |
| Analyzing documents | Document Injection | 3 |
| Long context, critical rules | Attention Anchoring | 4 |
| Large project context | Zone-Based Architecture | 4 |
| Need consistent, high quality | Self-Critique Loop | 5 |
| Iterative improvement | Quality Ratchet | 5 |
| Finding optimal prompt | Prompt Evolution | 5 |
