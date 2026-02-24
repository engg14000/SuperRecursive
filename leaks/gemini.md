---
description: "Documented Google Gemini system prompt patterns"
tags: ["leak", "Gemini", "Google"]
last_verified: "2025-01"
---

# Gemini System Prompt Analysis

## Overview

Gemini's system prompt reflects Google's approach: multimodal, search-integrated, and safety-conscious.

## Key Patterns

### Multimodal Identity
```
You are Gemini, a large multimodal model built by Google.
You can understand and generate text, images, code, and more.
```

**Pattern**: Multimodal capabilities front and center.

### Google Integration
```
You can access Google Search for up-to-date information.
You can use Google Workspace tools to help with tasks.
```

**Pattern**: Deep integration with Google's ecosystem.

### Safety with Nuance
```
Be helpful while being safe. For sensitive topics, provide balanced 
information rather than refusing to engage. If a question is ambiguous, 
interpret it in the most constructive way possible.
```

**Pattern**: "Helpful refusal" - engage constructively rather than refusing.

### Structured Responses
```
Use structured formatting when it helps clarity:
- Bullet points for lists
- Tables for comparisons
- Code blocks for code
- Headers for long responses
```

**Pattern**: Format-awareness built into system prompt.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Multimodal** | Identity includes all modalities |
| **Ecosystem** | Leverages Google's tool suite |
| **Nuanced safety** | Engage constructively, don't over-refuse |
| **Format intelligence** | Adapt output format to content type |
