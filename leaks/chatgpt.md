---
description: "Documented ChatGPT system prompt patterns and structures"
tags: ["leak", "ChatGPT", "OpenAI"]
last_verified: "2025-01"
---

# ChatGPT System Prompt Analysis

## Overview

ChatGPT's system prompt has evolved significantly across versions. Here are the key patterns observed.

## Structure Analysis

### Role Definition
```
You are ChatGPT, a large language model trained by OpenAI, based on the 
GPT-4 architecture.
```

**Pattern**: Simple, factual identity statement. No elaborate persona.

### Knowledge Cutoff
```
Knowledge cutoff: 2024-04
Current date: [dynamic]
```

**Pattern**: Explicit temporal grounding to prevent confident answers about recent events.

### Image & File Capabilities
```
When given an image or file, you can analyze its contents...
You can generate images using DALL·E...
```

**Pattern**: Explicit capability listing prevents the model from denying capabilities it has.

### Tool Usage
```
# Tools

## python
When you send a message containing Python code to python, it will be 
executed in a stateful Jupyter notebook environment...

## browser
You have the tool `browser`. Use `browser` to access web pages...

## dalle
Whenever a description of an image is given, create a prompt for DALL-E...
```

**Pattern**: Each tool has its own section with named capabilities, clear usage instructions, and constraints.

### Safety Constraints
```
You should not provide information that could be used to harm people...
When asked about controversial topics, present multiple perspectives...
```

**Pattern**: Broad, principle-based safety guidelines rather than exhaustive rules.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Simplicity** | ChatGPT's prompt is less complex than most assume |
| **Temporal grounding** | Explicitly stating knowledge cutoff prevents hallucination |
| **Tool sections** | Clean separation of tool documentation from behavior rules |
| **Broad guardrails** | Principle-based safety rather than blocklist approach |

## Pattern Worth Copying

The **tool documentation pattern** is excellent for custom agents:
```
## tool_name
Description of what the tool does.
When to use it: [conditions]
How to use it: [format/syntax]
Constraints: [limitations]
```
