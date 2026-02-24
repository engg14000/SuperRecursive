---
description: "Inter-agent messaging protocols and communication patterns"
author: "SuperRecursive"
tags: ["multi-agent", "communication", "protocols"]
verified: true
version: "1.0"
---

# Agent Communication Protocols

## Overview

Effective multi-agent systems require structured communication. This document defines message formats, handoff patterns, and state sharing protocols.

## Message Format

### Standard Message

```json
{
  "message_id": "msg_001",
  "timestamp": "2026-02-24T14:00:00Z",
  "from": "agent_architect",
  "to": "agent_coder",
  "type": "TASK_ASSIGNMENT",
  "priority": "HIGH",
  "payload": {
    "task": "Implement user authentication module",
    "context": "Express.js API, MongoDB, JWT tokens",
    "constraints": ["Must support Google OAuth", "Session timeout: 24h"],
    "expected_output": "Source files in /src/auth/",
    "deadline": "2026-02-24T15:00:00Z"
  },
  "references": ["msg_000"]
}
```

### Message Types

| Type | Direction | Purpose |
|------|-----------|---------|
| `TASK_ASSIGNMENT` | Coordinator → Agent | Assign work |
| `STATUS_UPDATE` | Agent → Coordinator | Report progress |
| `TASK_COMPLETE` | Agent → Coordinator | Deliver results |
| `QUERY` | Agent → Agent | Ask for information |
| `RESPONSE` | Agent → Agent | Answer a query |
| `CONFLICT` | Agent → Coordinator | Report disagreement |
| `ESCALATION` | Agent → Coordinator | Request human help |
| `HANDOFF` | Agent → Agent | Transfer task ownership |

## Handoff Patterns

### Sequential Handoff
```
Agent A completes → passes full context → Agent B starts
```
**Use when**: Tasks are strictly sequential (design → implement)

### Parallel Fan-Out
```
Coordinator → broadcasts task parts → Agents work in parallel → results merge
```
**Use when**: Tasks are independent (test different modules)

### Pipeline
```
Agent A → partial result → Agent B → enriched result → Agent C → final
```
**Use when**: Each agent adds a layer (generate → review → document)

### Callback
```
Agent A starts → needs info → queries Agent B → Agent B responds → Agent A continues
```
**Use when**: An agent discovers a dependency mid-task

## Context Sharing

### Shared Context Document
```markdown
# Shared Project Context
Last Updated: 2026-02-24T14:30:00Z

## Architecture Decisions
- Framework: Express.js (decided by ARCHITECT, Task 1)
- Database: MongoDB with Mongoose (decided by ARCHITECT, Task 1)
- Auth: passport.js + JWT (decided by RESEARCHER, Task 2)

## Active Constraints
- Node.js 18+ required
- Must pass all existing tests
- No new runtime dependencies without REVIEWER approval

## Current State
- [ ] Auth module (CODER - in progress)
- [x] Architecture spec (ARCHITECT - complete)
- [x] Library research (RESEARCHER - complete)
```

### State Machine

Agent states and valid transitions:

```
IDLE → ASSIGNED → WORKING → BLOCKED → WORKING → COMPLETE
                     │                              │
                     └──── ERROR ── RECOVERING ─────┘
```

## Conflict Resolution Protocol

When two agents produce conflicting outputs:

1. **Coordinator identifies the conflict**
2. **Both agents provide rationale** (structured arguments)
3. **Evaluation criteria applied**:
   - Which approach better satisfies requirements?
   - Which is simpler/more maintainable?
   - Which has fewer risks?
4. **Decision recorded** with rationale
5. **Losing agent adapts** their output to align
