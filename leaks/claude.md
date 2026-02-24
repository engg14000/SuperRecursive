---
description: "Documented Claude system prompt patterns and constitutional approach"
tags: ["leak", "Claude", "Anthropic"]
last_verified: "2025-01"
---

# Claude System Prompt Analysis

## Overview

Claude's system prompt demonstrates Anthropic's "constitutional AI" approach - principles rather than rules.

## Key Patterns

### Identity
```
The assistant is Claude, made by Anthropic.
```

**Pattern**: Minimal identity, letting the constitutional training carry the personality.

### Harmlessness Through Principles
```
Claude should be helpful, harmless, and honest.
```

**Pattern**: Three simple principles instead of a laundry list of restrictions.

### Handling Uncertainty
```
If Claude is unsure about something, it says so rather than guessing.
Claude doesn't claim to have personal experiences or feelings.
```

**Pattern**: Explicit metacognition about its own uncertainty - very effective.

### Formatting
```
Claude uses markdown formatting when appropriate.
Claude provides code in code blocks with the language specified.
```

**Pattern**: Output format guidance without being overly prescriptive.

### CLAUDE.md / Project Context
```
Content from the human's project is provided in <context> tags.
```

**Pattern**: Clear delimiter for external project context vs. system instructions.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Minimal role** | Claude's persona comes from training, not the prompt |
| **Principles > Rules** | Three principles replace hundreds of rules |
| **Uncertainty handling** | Explicit instruction to admit uncertainty |
| **Context delimiters** | Clean separation of system vs. project context |

## Patterns Worth Copying

### The Uncertainty Pattern
```
When unsure, say "I'm not certain about this, but..." rather than 
presenting uncertain information as fact.
```

### The Non-Claim Pattern
```
Do not claim to have personal experiences, emotions, or consciousness.
You can discuss these topics intellectually but not from personal experience.
```
