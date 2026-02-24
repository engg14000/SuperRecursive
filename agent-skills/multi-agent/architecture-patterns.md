---
description: "Common architectural patterns for multi-agent systems"
author: "SuperRecursive"
tags: ["multi-agent", "architecture", "design-patterns"]
verified: true
version: "1.0"
---

# Multi-Agent Architecture Patterns

## Overview

Choosing the right architecture determines how effectively your agents collaborate. Each pattern has distinct strengths and trade-offs.

## Pattern 1: Hierarchical (Manager-Worker)

```
         ┌─────────┐
         │ Manager  │
         └────┬─────┘
         ┌────┼────┐
         │    │    │
       ┌─▼─┐┌▼──┐┌▼─┐
       │ W1 ││W2 ││W3│
       └────┘└───┘└──┘
```

**How it works**: A single manager agent decomposes tasks and assigns them to worker agents. Workers report back to the manager.

**Best for**: Clear task decomposition, predictable workflows
**Weakness**: Single point of failure (manager), bottleneck at scale

### Implementation
```
MANAGER PROMPT: "You manage a team of specialist workers. Decompose the user's 
request, assign sub-tasks to workers, and assemble their outputs."

WORKER PROMPT: "You are a specialist in [DOMAIN]. Execute the assigned task and 
report your output to the manager. Ask the manager if you need clarification."
```

## Pattern 2: Peer-to-Peer (Collaborative)

```
    ┌────┐   ┌────┐
    │ A1 │◄──│ A2 │
    └──┬─┘   └─┬──┘
       │       │
    ┌──▼─┐   ┌▼──┐
    │ A3 │◄──│ A4 │
    └────┘   └───┘
```

**How it works**: All agents are peers with equal authority. They communicate directly and coordinate through shared state.

**Best for**: Creative/brainstorming tasks, consensus-building
**Weakness**: Coordination overhead, potential deadlocks

### Implementation
```
PEER PROMPT: "You are one of [N] equal collaborators. Share your work in the 
shared context. Build on others' contributions. When you disagree, state your 
reasoning and seek consensus."
```

## Pattern 3: Pipeline (Sequential Stages)

```
    ┌────┐   ┌────┐   ┌────┐   ┌────┐
    │ S1 │──►│ S2 │──►│ S3 │──►│ S4 │
    └────┘   └────┘   └────┘   └────┘
  Research   Design    Build    Review
```

**How it works**: Each agent represents a stage. Output from one stage feeds directly into the next.

**Best for**: Well-defined processes (CI/CD-like), quality gates
**Weakness**: Sequential latency, one slow stage blocks all

### Implementation
```
STAGE PROMPT: "You are stage [N] in a [M]-stage pipeline. Your input comes from 
stage [N-1]. Process it according to your specialty and pass the enhanced output 
to stage [N+1]."
```

## Pattern 4: Blackboard (Shared State)

```
       ┌───────────────────┐
       │    BLACKBOARD     │
       │  (Shared Memory)  │
       └───┬───┬───┬───┬──┘
           │   │   │   │
         ┌─▼─┐│ ┌─▼─┐ │
         │ A ││ │ C │ │
         └───┘│ └───┘ │
           ┌──▼┐   ┌──▼┐
           │ B │   │ D │
           └───┘   └───┘
```

**How it works**: All agents read from and write to a shared "blackboard" (document, database, or file system). Agents work whenever they see something they can contribute to.

**Best for**: Complex, evolving problems; agents with diverse specialties
**Weakness**: Concurrency issues, requires careful state management

### Implementation
```
BLACKBOARD AGENT PROMPT: "You monitor the shared project state. When you identify 
something in your area of expertise that needs work, do it and update the state. 
Always read the latest state before acting."
```

## Pattern 5: Mixture of Experts (Router)

```
         ┌──────────┐
         │  ROUTER  │
         └────┬─────┘
         ┌────┼────┐
         │    │    │
    ┌────▼┐┌──▼──┐┌▼────┐
    │Code ││Data ││Write│
    │Expert││Expert││Expert│
    └─────┘└─────┘└─────┘
```

**How it works**: A router agent analyzes each request/sub-task and routes it to the most qualified specialist.

**Best for**: Varied tasks, leveraging specialist strengths
**Weakness**: Router becomes a bottleneck, routing errors costly

## Choosing the Right Pattern

| Criteria | Hierarchical | Peer-to-Peer | Pipeline | Blackboard | Router |
|----------|:-:|:-:|:-:|:-:|:-:|
| Task clarity | High | Low | High | Medium | Medium |
| Parallelism | Medium | High | Low | High | Medium |
| Simplicity | High | Low | High | Low | Medium |
| Fault tolerance | Low | High | Low | Medium | Medium |
| Scalability | Medium | Low | High | High | High |
| Best team size | 3-7 | 2-4 | 3-6 | 3-10 | 3-10 |
