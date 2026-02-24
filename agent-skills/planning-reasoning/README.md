# 🧩 Planning & Reasoning

> Advanced reasoning frameworks for AI agents — from step-by-step thinking to self-correcting loops.

## Frameworks

| Framework | Approach | Best For | File |
|-----------|----------|----------|------|
| Chain-of-Thought (CoT) | Step-by-step reasoning | Math, logic, debugging | [chain-of-thought.md](chain-of-thought.md) |
| Tree-of-Thought (ToT) | Multi-path exploration | Design decisions, architecture | [tree-of-thought.md](tree-of-thought.md) |
| ReAct | Reasoning + Acting | Investigation, research, tool use | [react.md](react.md) |
| Reflexion | Learn from failures | Self-improving code, iterative tasks | [reflexion.md](reflexion.md) |
| Structured Output | Consistent format | Agent pipelines, machine-readable | [structured-output.md](structured-output.md) |

## Quick Decision Guide

```
What kind of task?
├── Clear, step-by-step problem → Chain-of-Thought
├── Multiple valid solutions → Tree-of-Thought
├── Investigation/research → ReAct
├── Iterative improvement → Reflexion
└── Pipeline/automation → Structured Output
```

## Combining Frameworks

The most powerful approach is combining frameworks:
- **ReAct + CoT**: Investigate with structured reasoning
- **ToT + Reflexion**: Explore options, learn from failed branches
- **CoT + Structured Output**: Reason step-by-step, output in parsed format
