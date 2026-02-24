---
description: "External memory augmentation with semantic search for context-limited agents"
author: "SuperRecursive"
tags: ["memory", "RAG", "retrieval", "semantic-search"]
verified: true
version: "1.0"
---

# Retrieval-Augmented Memory

## Overview

When an agent's internal context window is insufficient, retrieval-augmented memory extends its knowledge by fetching relevant information from external sources on-demand.

## How It Works

```
User Query → Extract Key Topics → Search External Memory → 
Inject Retrieved Context → Generate Response
```

## System Prompt

```
You have access to an external memory system. When you need information beyond 
your current context, use retrieval to fetch relevant memories.

## When to Retrieve
- You're asked about something not in your current context
- You need to reference a past decision or discussion
- You're working on a module and need to understand related modules
- You're unsure about a project convention or preference

## Retrieval Strategy
1. Formulate a specific search query (not the user's raw question)
2. Retrieve top 3-5 most relevant results
3. Evaluate relevance of each result (discard noise)
4. Integrate relevant information into your response
5. Cite the source of retrieved information

## Example
User: "How should I handle authentication in the new microservice?"
Your search queries:
  - "authentication architecture decision"
  - "microservice auth pattern"
  - "JWT vs session current project"
```

## Implementation Patterns

### Pattern 1: File-Based Retrieval

Best for smaller projects. Search through project documentation.

```python
import os
import re

def retrieve_from_files(query, docs_dir="./docs"):
    """Simple file-based retrieval using keyword matching."""
    results = []
    keywords = query.lower().split()
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(('.md', '.txt')):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    score = sum(1 for kw in keywords if kw in content.lower())
                    if score > 0:
                        results.append((score, path, content[:500]))
    
    return sorted(results, reverse=True)[:5]
```

### Pattern 2: Vector Store Retrieval

Best for large knowledge bases. Uses semantic similarity.

```python
from sentence_transformers import SentenceTransformer
import chromadb

# Initialize
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.get_or_create_collection("agent_memory")

# Store memories
def store_memory(text, metadata=None):
    embedding = model.encode(text).tolist()
    collection.add(
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}],
        ids=[f"mem_{collection.count()}"]
    )

# Retrieve memories
def retrieve_memories(query, top_k=5):
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0]
```

### Pattern 3: Conversation Log Retrieval

Search through past conversation logs.

```python
def retrieve_from_conversations(query, logs_dir="./logs"):
    """Search conversation logs for relevant past discussions."""
    results = []
    
    for log_file in sorted(os.listdir(logs_dir), reverse=True):
        with open(os.path.join(logs_dir, log_file)) as f:
            conversations = f.read().split("---")  # Delimiter between turns
            for i, turn in enumerate(conversations):
                if any(kw in turn.lower() for kw in query.lower().split()):
                    results.append({
                        'file': log_file,
                        'turn': i,
                        'content': turn[:300],
                        'date': log_file[:10]  # Assumes date-prefixed filenames
                    })
    
    return results[:5]
```

## Best Practices

| Practice | Why |
|----------|-----|
| Query reformulation | Raw user questions make poor search queries |
| Result re-ranking | Retrieval results aren't always in best order |
| Freshness bias | Prefer recent memories over old ones |
| Source citation | Always note where retrieved info came from |
| Fallback gracefully | If retrieval returns nothing, say so |
