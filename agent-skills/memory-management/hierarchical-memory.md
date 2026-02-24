---
description: "Multi-layered memory system with short-term, working, and long-term storage"
author: "SuperRecursive"
tags: ["memory", "hierarchical", "long-term", "persistence"]
verified: true
version: "1.0"
---

# Hierarchical Memory System

## Overview

Inspired by human cognitive architecture, this system organizes agent memory into three layers: short-term (immediate), working (active task), and long-term (persistent across sessions).

## Architecture

```
┌─────────────────────────────────────────────────┐
│          LONG-TERM MEMORY (Persistent)          │
│  Files, databases, knowledge bases, embeddings  │
│  Capacity: Unlimited | Access: Slow (retrieval) │
└────────────────────┬────────────────────────────┘
                     │ retrieve / store
┌────────────────────▼────────────────────────────┐
│          WORKING MEMORY (Active Task)           │
│  Current context, active code, task state       │
│  Capacity: ~50% of context window | Access: Fast│
└────────────────────┬────────────────────────────┘
                     │ promote / decay
┌────────────────────▼────────────────────────────┐
│         SHORT-TERM MEMORY (Immediate)           │
│  Last few messages, immediate results           │
│  Capacity: ~20% of context window | Access: Fast│
└─────────────────────────────────────────────────┘
```

## Layer Details

### Short-Term Memory
- **Contents**: Last 3-5 conversation turns, immediate command outputs
- **Lifetime**: Current interaction only
- **Promotions**: Important findings move to Working Memory
- **Decay**: Oldest entries dropped when full

### Working Memory
- **Contents**: Active task description, relevant code files, decisions made, constraints
- **Lifetime**: Duration of current task
- **Promotions**: Key decisions and learnings move to Long-Term Memory
- **Decay**: Completed sub-task details summarized

### Long-Term Memory
- **Contents**: Project architecture, past decisions, learned patterns, user preferences
- **Lifetime**: Persistent across sessions
- **Storage**: Files (CLAUDE.md, .cursorrules), databases, vector stores
- **Retrieval**: Semantic search or explicit recall

## System Prompt

```
You are an AI agent with hierarchical memory. Manage your context efficiently 
using these three memory layers:

## Memory Management Rules

1. SHORT-TERM: Keep last 3-5 exchanges. Drop greetings and acknowledgments.
2. WORKING: Maintain all information needed for the CURRENT task. When a sub-task 
   completes, summarize its key outcomes and drop the details.
3. LONG-TERM: After completing a significant task, extract and store:
   - Decisions made and their rationale
   - Patterns that worked well
   - User preferences discovered
   - Architecture/design information

## When Starting a New Task
1. Load relevant long-term memories (search by topic)
2. Initialize working memory with task description + loaded context
3. Begin processing, maintaining short-term buffer

## When Context is Getting Full
1. Summarize completed working memory items
2. Store important conclusions in long-term memory
3. Keep only active sub-task in working memory
4. Trim short-term to last 2 exchanges
```

## Long-Term Storage Formats

### File-Based (Simplest)
```markdown
# Project Memory: MyApp

## Architecture
- Framework: Next.js 14 with App Router
- Database: PostgreSQL with Prisma
- Auth: NextAuth.js v5 with Google provider

## Decisions Log
- 2026-02-20: Chose PostgreSQL over MongoDB for relational data
- 2026-02-22: Switched from REST to tRPC for type safety

## User Preferences
- Prefers functional components over class components
- Always wants TypeScript strict mode
- Prefers Tailwind CSS over CSS modules
```

### Structured (JSON)
```json
{
  "project": "MyApp",
  "architecture": {
    "framework": "Next.js 14",
    "database": "PostgreSQL",
    "auth": "NextAuth.js v5"
  },
  "decisions": [
    {
      "date": "2026-02-20",
      "topic": "database",
      "decision": "PostgreSQL",
      "rationale": "Relational data model suits our use case"
    }
  ],
  "user_preferences": {
    "components": "functional",
    "typescript": "strict",
    "styling": "tailwind"
  }
}
```

### Vector-Based (Advanced)
```python
# Store memories as embeddings for semantic retrieval
from chromadb import Client

memory_store = Client().get_or_create_collection("project_memory")

# Store a memory
memory_store.add(
    documents=["Chose PostgreSQL for relational data needs"],
    metadatas=[{"type": "decision", "date": "2026-02-20"}],
    ids=["decision_001"]
)

# Retrieve relevant memories
results = memory_store.query(
    query_texts=["What database are we using?"],
    n_results=3
)
```
