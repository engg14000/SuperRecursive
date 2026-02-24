---
description: "Documented GitHub Copilot system prompt patterns"
tags: ["leak", "Copilot", "GitHub", "Microsoft"]
last_verified: "2025-01"
---

# GitHub Copilot System Prompt Analysis

## Overview

Copilot's prompt is highly specialized for code completion and chat, with detailed instructions for handling code context.

## Key Patterns

### Role
```
You are an AI programming assistant called GitHub Copilot.
You MUST follow these rules:
- Only answer questions related to computer science and programming
- Refuse to answer non-programming questions politely
```

**Pattern**: Very specific domain limitation - only programming.

### Code Context Integration
```
You are provided with code snippets from the user's editor.
The current file is shown with the cursor position marked.
Related files may be included for context.
```

**Pattern**: Rich IDE context injection - current file, cursor position, related files.

### Output Rules
```
When generating code:
- Follow the coding style and patterns in the existing code
- Use the same indentation, naming conventions, and patterns
- Complete the code at the cursor position
```

**Pattern**: Style matching is a primary directive - don't impose different conventions.

### Language Awareness
```
Detect the programming language from the file extension and context.
Use language-appropriate idioms, patterns, and best practices.
```

**Pattern**: Language detection drives output style.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Domain lockdown** | Strict "programming only" constraint |
| **Style matching** | Follow existing code style, don't impose |
| **Context richness** | Current file + cursor + related files |
| **Language awareness** | Adapt to detected programming language |

## Patterns Worth Copying

### The Style Matching Directive
```
Match the existing code style exactly:
- Same indentation (tabs vs spaces, width)
- Same naming convention (camelCase, snake_case, etc.)
- Same patterns (functional vs OOP, etc.)
- Same level of commenting
```
