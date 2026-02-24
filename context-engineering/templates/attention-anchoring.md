---
description: "Place critical information at attention-peak positions in context"
author: "SuperRecursive"
tags: ["context-engineering", "attention", "optimization"]
verified: true
version: "1.0"
---

# Attention Anchoring Strategy

## Overview

Research shows that LLMs have a "U-shaped" attention pattern — they attend most strongly to the **beginning** and **end** of the context window, with a trough in the middle. This strategy exploits that pattern.

## The Attention Curve

```
Attention
Level
  ▲
  █ █                                         █ █
  █ █ █                                     █ █ █
  █ █ █ █                                 █ █ █ █
  █ █ █ █ █                             █ █ █ █ █
  █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █
  ──────────────────────────────────────────────►
  Start              Middle                   End
  (HIGH)             (LOW)                 (HIGH)
```

## Placement Strategy

```
POSITION 1 (Start): CRITICAL INSTRUCTIONS
├── Role definition
├── Core constraints
├── Task objective
└── Output format requirements

POSITION 2 (Early): HIGH-PRIORITY CONTEXT
├── Key code files being modified
├── Architecture decisions
└── Current error messages

POSITION 3 (Middle): REFERENCE MATERIAL ← Lowest attention
├── Background documentation
├── Extended code examples
├── Historical context
└── Supporting evidence

POSITION 4 (Late): IMPORTANT DETAILS
├── Specific requirements
├── Edge cases to handle
└── Quality criteria

POSITION 5 (End): CRITICAL REMINDERS
├── Restate the core task
├── Key constraints reminder
├── Output format reminder
└── "Remember: [most important rule]"
```

## Practical Template

```markdown
# [CRITICAL: Read first] Your Role and Task
You are {{role}}. Your task is {{task}}.

CRITICAL RULES (must follow):
1. {{most_important_rule}}
2. {{second_most_important_rule}}

# Context: Active Code
{{current_file_contents}}

# Context: Error Details  
{{error_messages}}

# Reference: Documentation
{{background_docs — OK if slightly less attended to}}

# Reference: Related Code
{{supporting_code_examples}}

# Requirements: Specific Details
{{edge_cases_and_requirements}}

# [REMINDER] Output Format
Your output MUST follow this format:
{{output_format}}

Remember: {{most_important_rule_restated}}
```

## Evidence

This strategy is supported by:
- "Lost in the Middle" (Liu et al., 2023) — documents in the middle of context are used less
- Anthropic's prompt engineering guidelines — "put important info first"
- OpenAI's best practices — "repeat key instructions at the end"

## Quick Rules

1. ✅ **Start** with the most important instruction
2. ✅ **End** with a reminder of the key constraint
3. ✅ Put **reference material** in the middle (it's OK there)
4. ❌ Don't bury critical instructions in the middle
5. ❌ Don't front-load low-priority background info
