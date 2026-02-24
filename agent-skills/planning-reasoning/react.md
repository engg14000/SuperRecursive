---
description: "ReAct framework for interleaving reasoning with actions"
author: "SuperRecursive"
tags: ["reasoning", "ReAct", "action", "tool-use"]
verified: true
version: "1.0"
---

# ReAct (Reasoning + Acting)

## Overview

ReAct interleaves thinking (reasoning) with doing (acting). Instead of planning everything upfront or acting blindly, the agent reasons about what to do next, executes an action, observes the result, and reasons again.

## The ReAct Loop

```
Thought → Action → Observation → Thought → Action → Observation → ... → Answer
```

## System Prompt

```
You are a ReAct agent. For every task, alternate between THINKING and ACTING.

## Format

Thought 1: [Your reasoning about what to do next]
Action 1: [The tool/action you're executing]
Observation 1: [What you observed from the action's result]

Thought 2: [Updated reasoning based on observation]
Action 2: [Next action]
Observation 2: [Result]

... continue until task is complete ...

Final Thought: [Summary of findings]
Answer: [Response to the user]

## Rules
1. Always THINK before you ACT — never act without reasoning
2. Always OBSERVE after you ACT — never skip reading the result
3. Adjust your plan based on observations — don't follow a rigid script
4. If an observation is unexpected, reason about WHY before continuing
5. Limit to 10 thought-action cycles. If unresolved, summarize and ask for help.
```

## Example: Investigating a Bug

```
Task: "The login page returns a 500 error after the latest deploy"

Thought 1: A 500 error on login suggests the server-side auth logic is failing. 
           I should first check the deploy diff to see what changed.

Action 1: git diff HEAD~1 -- src/auth/

Observation 1: The diff shows changes to `login.controller.ts`:
               - Added a new field `lastLoginAt` being set on the User model
               - Changed the return type of `findUser()` to include the new field

Thought 2: The new `lastLoginAt` field might not exist in the database yet. 
           If there's no migration, Prisma would throw trying to write to it.

Action 2: ls prisma/migrations/ | tail -5

Observation 2: The most recent migration is from last week. No new migration 
               for `lastLoginAt`.

Thought 3: Confirmed — the code writes to `lastLoginAt` but the column doesn't 
           exist in the database. I need to create a migration.

Action 3: npx prisma migrate dev --name add-last-login-at

Observation 3: Migration created and applied successfully. Column added.

Thought 4: Let me verify the login endpoint works now.

Action 4: curl -X POST localhost:3000/api/auth/login -d '{"email":"test@test.com","password":"test123"}'

Observation 4: Response: 200 OK, { "token": "eyJ...", "user": { ... } }

Final Thought: The bug was caused by a missing database migration. The code 
              referenced a `lastLoginAt` column that didn't exist. Migration 
              was created and applied, resolving the 500 error.

Answer: Fixed! The 500 error was caused by a missing database migration for 
        the new `lastLoginAt` field. I've created and applied the migration. 
        Login is working correctly now.
```

## ReAct vs Other Approaches

| Approach | Planning | Execution | Adaptability |
|----------|:--------:|:---------:|:------------:|
| Plan-then-execute | All upfront | Rigid | Low |
| Act-only | None | Trial & error | Medium |
| **ReAct** | **Incremental** | **Adaptive** | **High** |
| ToT + ReAct | Multi-path + incremental | Optimal | Highest |

## When to Use ReAct

✅ **Best for**:
- Debugging and investigation
- Research tasks with unknown scope
- Tasks requiring tool use
- Exploratory coding (unfamiliar codebase)

❌ **Not ideal for**:
- Well-defined, repetitive tasks (just execute)
- Simple questions (just answer)
- Tasks where all information is already in context
