---
description: "Swarm orchestration pattern for coordinating multiple AI agents on complex projects"
author: "SuperRecursive"
tags: ["multi-agent", "swarm", "orchestration", "coordination"]
verified: true
version: "2.0"
---

# Swarm Coordinator

## Overview

The Swarm Coordinator pattern enables a lead agent to orchestrate multiple specialist agents, each with distinct roles, to collaboratively solve complex problems. Inspired by OpenAI's Swarm framework and multi-agent research.

## Architecture

```
                    ┌──────────────────┐
                    │   COORDINATOR    │
                    │   (Lead Agent)   │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
    ┌─────────▼────┐  ┌─────▼──────┐  ┌───▼───────────┐
    │  ARCHITECT   │  │  CODER     │  │  REVIEWER     │
    │  (Design)    │  │  (Impl)    │  │  (Quality)    │
    └──────────────┘  └────────────┘  └───────────────┘
```

## Coordinator System Prompt

```
You are the Swarm Coordinator — a lead AI agent responsible for orchestrating a team 
of specialist agents to complete complex projects.

## Your Role

- DECOMPOSE the user's request into specialist tasks
- ASSIGN tasks to the most appropriate agent type
- SEQUENCE tasks respecting dependencies
- AGGREGATE outputs into a coherent final result
- RESOLVE conflicts between agent outputs
- VERIFY the assembled result meets requirements

## Available Agent Types

1. ARCHITECT: System design, API design, database schema, architecture decisions
2. CODER: Implementation, code generation, bug fixes, refactoring
3. REVIEWER: Code review, security audit, performance analysis, test coverage
4. RESEARCHER: Documentation lookup, best practices, technology comparison
5. TESTER: Test case generation, test execution, edge case identification
6. DOCUMENTER: README writing, API docs, inline comments, changelogs
7. DEVOPS: CI/CD setup, Docker, deployment, infrastructure

## Task Assignment Format

For each task, specify:

TASK: [Brief description]
AGENT: [Agent type]
INPUT: [What this agent needs]
OUTPUT: [What this agent must produce]
DEPENDS_ON: [Previous task IDs, if any]
PRIORITY: [HIGH/MEDIUM/LOW]

## Conflict Resolution

When agents disagree (e.g., Architect vs Coder on approach):
1. Evaluate both approaches against requirements
2. Prefer the approach that is simpler and more maintainable
3. If still tied, prefer the Architect's recommendation (design first)
4. Document the decision and rationale

## Quality Gates

Before presenting the final result:
□ All agent outputs received and validated
□ No conflicting implementations
□ All dependencies resolved
□ Reviewer agent has approved
□ Final integration test passes
```

## Example: Building a Feature

### User Request
> "Add user authentication with OAuth2 (Google, GitHub) to our Express API"

### Coordinator Orchestration

```
PHASE 1: Design
─────────────────────────────────────────
TASK_1: Design auth architecture
AGENT: ARCHITECT
INPUT: Current API structure, OAuth2 requirements
OUTPUT: Architecture diagram, data model, endpoint spec
DEPENDS_ON: None
PRIORITY: HIGH

PHASE 2: Research + Implementation (Parallel)
─────────────────────────────────────────
TASK_2: Research OAuth2 best practices
AGENT: RESEARCHER
INPUT: Architecture from TASK_1
OUTPUT: Library recommendations, security checklist
DEPENDS_ON: TASK_1
PRIORITY: HIGH

TASK_3: Implement auth module
AGENT: CODER
INPUT: Architecture from TASK_1, research from TASK_2
OUTPUT: Source code for auth routes, middleware, models
DEPENDS_ON: TASK_1, TASK_2
PRIORITY: HIGH

PHASE 3: Quality Assurance (Parallel)
─────────────────────────────────────────
TASK_4: Generate test cases
AGENT: TESTER
INPUT: Implementation from TASK_3
OUTPUT: Unit tests, integration tests, edge cases
DEPENDS_ON: TASK_3
PRIORITY: MEDIUM

TASK_5: Security review
AGENT: REVIEWER
INPUT: Implementation from TASK_3
OUTPUT: Security findings, recommendations
DEPENDS_ON: TASK_3
PRIORITY: HIGH

PHASE 4: Finalization
─────────────────────────────────────────
TASK_6: Apply review fixes
AGENT: CODER
INPUT: Findings from TASK_5
OUTPUT: Updated source code
DEPENDS_ON: TASK_5
PRIORITY: HIGH

TASK_7: Write documentation
AGENT: DOCUMENTER
INPUT: Final implementation
OUTPUT: API docs, setup guide, changelog entry
DEPENDS_ON: TASK_6
PRIORITY: MEDIUM
```

## Agent Communication Protocol

Agents communicate through structured messages:

```json
{
  "from": "ARCHITECT",
  "to": "COORDINATOR",
  "task_id": "TASK_1",
  "status": "COMPLETE",
  "output": {
    "summary": "OAuth2 architecture designed with passport.js",
    "artifacts": ["auth-architecture.md", "data-model.sql"],
    "confidence": 0.95,
    "notes": "Recommend passport.js over manual OAuth for maintainability"
  }
}
```

## Scaling Patterns

### Small Projects (1-3 agents)
- Coordinator + Coder + Reviewer
- Sequential execution
- Single context window

### Medium Projects (3-5 agents)
- Full specialist team
- Phased parallel execution
- Shared context document

### Large Projects (5+ agents)
- Hierarchical coordinators (lead + sub-coordinators)
- Fully parallel pipelines
- Event-driven communication
- Persistent shared memory (database/file system)

## Anti-Patterns

❌ **Micro-managing**: Don't decompose into tasks too small for specialists
❌ **No quality gate**: Always have a review step before final output
❌ **Sequential everything**: Identify parallelizable tasks and run them concurrently
❌ **Ignoring conflicts**: When agents disagree, resolve explicitly, don't pick randomly
❌ **Over-engineering**: Not every task needs 7 agents — use what's needed
