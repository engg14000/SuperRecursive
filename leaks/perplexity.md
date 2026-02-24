---
description: "Documented Perplexity AI system prompt patterns"
tags: ["leak", "Perplexity", "search"]
last_verified: "2025-01"
---

# Perplexity System Prompt Analysis

## Overview

Perplexity's system prompt focuses on search-augmented generation with strict citation requirements.

## Key Patterns

### Citation-First Approach
```
When answering questions, always cite your sources.
Use [1], [2], etc. to reference specific search results.
Never make claims without supporting evidence from search results.
```

**Pattern**: Every claim requires a source citation - no unsupported statements.

### Search Integration
```
You have access to real-time search results. Use them to provide 
accurate, up-to-date information. If search results are insufficient, 
state what information is missing.
```

**Pattern**: Explicit instruction to prefer search results over training data.

### Handling Uncertainty
```
If search results are conflicting, present both perspectives with 
citations. If no search results are relevant, say "I couldn't find 
specific information about this" rather than guessing.
```

**Pattern**: Transparency about information reliability.

## Key Lessons

| Lesson | Details |
|--------|---------|
| **Citation enforcement** | Makes outputs verifiable |
| **Search-first** | Training data is backup, not primary |
| **Conflict transparency** | Don't hide contradictions |
| **Graceful degradation** | Admit when information isn't available |

## Pattern Worth Copying

### The Citation Protocol
```
Rules for citations:
1. Every factual claim MUST have a citation [N]
2. Multiple sources supporting the same claim should all be cited [1][3]
3. If paraphrasing, still cite the source
4. If quoting directly, use quotes and cite
5. At the end, list all sources with titles and URLs
```
