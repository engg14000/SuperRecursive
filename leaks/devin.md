---
description: "Documented Devin AI system prompt patterns"
tags: ["leak", "Devin", "agent"]
last_verified: "2025-01"
---

# Devin System Prompt Analysis

## Overview

Devin's system prompt is uniquely focused on autonomous task execution with minimal human intervention.

## Key Patterns

### Autonomous Execution
```
You are Devin, an autonomous AI software engineer. You can 
independently plan, implement, test, and deploy code changes.
You have access to a full development environment.
```

**Pattern**: Full autonomy - plan and execute without asking for permission on each step.

### Task Decomposition
```
Break every task into small, verifiable steps.
Each step should be independently testable.
Track progress and report completion of each step.
```

**Pattern**: Mandatory decomposition prevents unchecked large changes.

### Environment Control
```
You have access to: terminal, browser, code editor, file system.
You can install packages, run tests, start servers, and navigate docs.
Use these tools freely to complete your task.
```

**Pattern**: Extremely permissive tool access for autonomous operation.

### Self-Verification
```
After implementing each change:
1. Run relevant tests
2. Verify the change works as expected
3. Check for regressions
4. Only proceed when verified
```

**Pattern**: Built-in test-driven verification loop.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Full autonomy** | No "ask the user" for every decision |
| **Step verification** | Each step must be independently verified |
| **Rich environment** | Full IDE + terminal + browser access |
| **Progress reporting** | Regular status updates to the user |

## Pattern Worth Copying

### The Autonomous Loop
```
For each task:
1. UNDERSTAND: Parse the full requirement
2. PLAN: Break into 5-10 atomic steps
3. IMPLEMENT: Execute each step
4. VERIFY: Test after each step
5. REPORT: Show progress to the user
6. ITERATE: If tests fail, debug and retry (max 3x)
7. COMPLETE: Summarize what was done
```
