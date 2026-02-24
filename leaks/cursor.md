---
description: "Documented Cursor IDE system prompt patterns"
tags: ["leak", "Cursor", "IDE"]
last_verified: "2025-02"
---

# Cursor System Prompt Analysis

## Overview

Cursor's system prompt is optimized for IDE-integrated code assistance with rich file context.

## Key Patterns

### Multi-File Awareness
```
You can see and edit multiple files in the user's workspace.
The current file and cursor position are provided.
Related files may be provided as additional context.
```

**Pattern**: Full workspace awareness, not just single-file.

### Edit Format
```
When suggesting edits, provide them in a diff-like format that 
can be applied directly to the file. Include the exact line numbers 
and the complete modified code.
```

**Pattern**: Machine-applicable edits, not just suggestions.

### Project Context (.cursorrules)
```
Users can provide custom instructions via .cursorrules file.
These instructions are loaded at the start of every interaction.
They take priority over default behavior.
```

**Pattern**: User-customizable behavior through config files.

### Tool Usage
```
You have access to: terminal, file creation, file editing, search.
Use these tools proactively to investigate and fix issues.
```

**Pattern**: Agentic tool use is encouraged, not just chat.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Workspace context** | Multi-file awareness beats single-file |
| **Actionable output** | Diffs > suggestions |
| **User customization** | .cursorrules = user-defined behavior |
| **Agentic** | Proactive tool use authorized |

## Pattern Worth Copying

### The .cursorrules Pattern
```
Allow users to define custom rules in a project-level config:
1. Project conventions (naming, structure, style)
2. Technology preferences (frameworks, libraries)
3. Quality requirements (testing, documentation)
4. Communication preferences (verbose vs concise)
```
