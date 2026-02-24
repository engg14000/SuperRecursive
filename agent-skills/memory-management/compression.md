---
description: "Context compression and summarization techniques for efficient memory usage"
author: "SuperRecursive"
tags: ["memory", "compression", "summarization"]
verified: true
version: "1.0"
---

# Context Compression Techniques

## Overview

When context windows fill up, compression techniques reduce content size while preserving essential information. These techniques work alongside sliding window and hierarchical memory strategies.

## Compression Methods

### 1. Summarization (Most Common)

Replace detailed content with concise summaries.

```
BEFORE (500 tokens):
  "We discussed three database options: PostgreSQL, MongoDB, and DynamoDB.
   PostgreSQL pros: ACID compliance, mature ecosystem, great with Prisma.
   PostgreSQL cons: Vertical scaling limits.
   MongoDB pros: Flexible schema, horizontal scaling.
   MongoDB cons: No joins, eventual consistency by default.
   DynamoDB pros: Serverless, auto-scaling.
   DynamoDB cons: Complex query patterns, vendor lock-in.
   After evaluating all options against our relational data model 
   requirements, we decided on PostgreSQL with Prisma ORM."

AFTER (50 tokens):
  "Decision: PostgreSQL with Prisma ORM. Chosen for ACID compliance 
   and relational data model fit. Rejected MongoDB (no joins) and 
   DynamoDB (vendor lock-in)."
```

### 2. Key-Value Extraction

Extract only the decisions and facts, drop the discussion.

```
BEFORE: [Long discussion about API design]

AFTER:
- API_STYLE: REST with OpenAPI spec
- AUTH: JWT bearer tokens
- RATE_LIMIT: 100 req/min per user
- VERSIONING: URL path (/v1/)
- FORMAT: JSON only
```

### 3. Code Compression

Keep function signatures and key logic, drop boilerplate.

```
BEFORE (full implementation):
  [50 lines of complete function code]

AFTER (compressed):
  auth.js: validateToken(token) → returns {userId, role} or throws AuthError
  auth.js: hashPassword(plain) → returns bcrypt hash (10 rounds)
  auth.js: generateToken(user) → returns JWT (24h expiry, HS256)
```

### 4. Conversation Compression

Keep the conclusions, drop the back-and-forth.

```
BEFORE:
  User: "Should we use Redux or Zustand?"
  AI: "Let me compare them..."
  [200 tokens of comparison]
  User: "I think Zustand is simpler"
  AI: "Agreed, Zustand is better for this project because..."
  [150 tokens of reasoning]

AFTER:
  Decision: Zustand over Redux. Reason: Simpler API, sufficient for project scope.
```

## System Prompt for Self-Compression

```
When your context is getting full, compress older content using these rules:

1. DECISIONS: Keep the decision and brief rationale. Drop the discussion.
2. CODE: Keep signatures and key logic. Drop imports, boilerplate, comments.
3. ERRORS: Keep the root cause and fix. Drop the stack traces.
4. CONVERSATIONS: Keep conclusions. Drop the negotiation.
5. FILES: Keep the file list and purpose. Drop the content details.

Compression format:
  📋 [Topic] → [Key conclusion] (originally discussed in [context])

Always preserve:
- User's stated preferences
- Architecture decisions
- Known constraints
- Active task requirements

Never compress:
- Current task instructions
- Code being actively edited
- Unresolved questions
```

## Compression Ratios

| Content Type | Typical Input | Compressed | Ratio |
|-------------|:---:|:---:|:---:|
| Discussion | 500 tokens | 50 tokens | 10:1 |
| Code file | 200 tokens | 40 tokens | 5:1 |
| Error trace | 300 tokens | 30 tokens | 10:1 |
| Decision log | 400 tokens | 80 tokens | 5:1 |
| Conversation | 1000 tokens | 100 tokens | 10:1 |

## When to Compress

```
IF context_usage > 70%:
    Compress Zone 4 (buffer) content
IF context_usage > 85%:
    Compress older Zone 3 (working) content  
IF context_usage > 95%:
    Emergency compression of all non-critical content
    Alert: "Context running low, consider starting fresh sub-task"
```
