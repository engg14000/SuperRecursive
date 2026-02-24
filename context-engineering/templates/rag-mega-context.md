---
description: "Maximum context utilization pattern for complex, multi-faceted AI tasks"
author: "SuperRecursive"
tags: ["context-engineering", "RAG", "mega-context", "advanced"]
verified: true
version: "2.0"
---

# RAG Mega-Context Builder

## Overview

The RAG Mega-Context pattern maximizes the value extracted from every token in the context window. Use this for complex tasks that need comprehensive background information.

## The Mega-Context Architecture

```
┌─────────────────────────────────────────────────┐
│ ZONE 1: SYSTEM IDENTITY (5%)                    │
│ Role, personality, core rules                   │
├─────────────────────────────────────────────────┤
│ ZONE 2: TASK SPECIFICATION (10%)                │
│ What to do, success criteria, constraints       │
├─────────────────────────────────────────────────┤
│ ZONE 3: DOMAIN KNOWLEDGE (25%)                  │
│ Retrieved documents, reference material         │
├─────────────────────────────────────────────────┤
│ ZONE 4: PROJECT CONTEXT (25%)                   │
│ Codebase, architecture, conventions             │
├─────────────────────────────────────────────────┤
│ ZONE 5: CURRENT WORK (25%)                      │
│ Active files, recent changes, error logs        │
├─────────────────────────────────────────────────┤
│ ZONE 6: OUTPUT SPECIFICATION (10%)              │
│ Format, structure, examples of desired output   │
└─────────────────────────────────────────────────┘
```

## Template

```markdown
# ═══════════════════════════════════════════════
# ZONE 1: SYSTEM IDENTITY
# ═══════════════════════════════════════════════

You are {{role_description}}.

Core Rules:
{{core_rules}}

# ═══════════════════════════════════════════════
# ZONE 2: TASK SPECIFICATION
# ═══════════════════════════════════════════════

## Objective
{{task_objective}}

## Success Criteria
{{success_criteria}}

## Constraints
{{constraints}}

## Non-Goals (explicitly out of scope)
{{non_goals}}

# ═══════════════════════════════════════════════
# ZONE 3: DOMAIN KNOWLEDGE
# ═══════════════════════════════════════════════

## Reference Material
{{retrieved_documents}}

## Best Practices for This Domain
{{domain_best_practices}}

## Common Pitfalls
{{common_pitfalls}}

# ═══════════════════════════════════════════════
# ZONE 4: PROJECT CONTEXT
# ═══════════════════════════════════════════════

## Architecture
{{architecture_overview}}

## Key Files
{{key_files_with_content}}

## Conventions
{{project_conventions}}

## Dependencies
{{dependency_list}}

# ═══════════════════════════════════════════════
# ZONE 5: CURRENT WORK
# ═══════════════════════════════════════════════

## Files Being Modified
{{current_file_contents}}

## Recent Changes
{{git_diff_or_change_log}}

## Error Log (if applicable)
{{error_messages}}

## Previous Attempts (if applicable)
{{previous_attempts_and_why_they_failed}}

# ═══════════════════════════════════════════════
# ZONE 6: OUTPUT SPECIFICATION
# ═══════════════════════════════════════════════

## Expected Output Format
{{output_format_spec}}

## Example of Good Output
{{example_output}}

## Quality Checklist
{{quality_checklist}}
```

## Optimization Techniques

### 1. Token Budget Allocation

For a 128k token window:

| Zone | Budget | Tokens | Priority |
|------|:------:|:------:|:--------:|
| System Identity | 5% | ~6,400 | Fixed |
| Task Spec | 10% | ~12,800 | Fixed |
| Domain Knowledge | 25% | ~32,000 | Dynamic |
| Project Context | 25% | ~32,000 | Dynamic |
| Current Work | 25% | ~32,000 | Dynamic |
| Output Spec | 10% | ~12,800 | Fixed |

### 2. Attention Optimization

Place the most critical information at:
- **Start of context** (high attention)
- **End of context** (high attention)
- **Avoid** burying critical info in the middle (attention trough)

### 3. Progressive Loading

```
Level 1: System + Task + Output Spec (always loaded)
Level 2: + Key project files (if task involves code)
Level 3: + Domain knowledge (if task requires reference)
Level 4: + Full current file contents (if editing)
Level 5: + Related files and error logs (if debugging)
```

Only load deeper levels as needed to stay within budget.

## When to Use

| Scenario | Use Mega-Context? | Why |
|----------|:-:|-----|
| Complex multi-file refactor | ✅ | Needs full project understanding |
| Simple bug fix | ❌ | Too much context adds noise |
| Architecture design | ✅ | Needs domain + project knowledge |
| Quick question | ❌ | Overkill |
| Production debugging | ✅ | Needs logs + code + context |
