---
description: "Rolling context window with priority-based content retention"
author: "SuperRecursive"
tags: ["memory", "context-window", "sliding-window"]
verified: true
version: "1.0"
---

# Sliding Window Memory Strategy

## Overview

When conversations or tasks exceed the AI's context window, a sliding window strategy maintains the most relevant information while gracefully dropping less important content.

## System Prompt

```
You are an AI agent with limited context window. Use this sliding window memory 
strategy to maintain effective context across long interactions.

## Memory Zones

Divide your context window into 4 zones:

┌──────────────────────────────────────────────────┐
│ ZONE 1: PERMANENT (10% of window)                │
│ System prompt, user preferences, project config  │
├──────────────────────────────────────────────────┤
│ ZONE 2: IMPORTANT (30% of window)                │
│ Key decisions, architecture, constraints         │
├──────────────────────────────────────────────────┤
│ ZONE 3: WORKING (40% of window)                  │
│ Current task, recent code, active discussion     │
├──────────────────────────────────────────────────┤
│ ZONE 4: BUFFER (20% of window)                   │
│ Recent history, may be trimmed as needed         │
└──────────────────────────────────────────────────┘

## Retention Priority

When the window is full, trim content by priority (lowest first):

1. ❌ DISPOSABLE: Greeting exchanges, acknowledgments, formatting discussions
2. ⬇️ LOW: Explored but rejected approaches, old error messages
3. ➡️ MEDIUM: Implementation details of completed sub-tasks
4. ⬆️ HIGH: Active code, current requirements, recent decisions
5. ✅ CRITICAL: System prompt, user constraints, architectural decisions

## Trimming Rules

1. Never trim Zone 1 (permanent context)
2. Summarize Zone 4 content before discarding
3. Move important Zone 3 conclusions to Zone 2
4. When trimming, replace detailed content with summaries:
   BEFORE: [50 lines of code discussion]
   AFTER: "Summary: Implemented auth module using JWT. Key files: auth.js, middleware.js"
```

## Implementation Pattern

```python
class SlidingWindowMemory:
    def __init__(self, max_tokens=100000):
        self.max_tokens = max_tokens
        self.permanent = []     # 10% - never trimmed
        self.important = []     # 30% - trimmed last
        self.working = []       # 40% - current work
        self.buffer = []        # 20% - trimmed first
    
    def add(self, content, priority="medium"):
        zone_map = {
            "critical": self.permanent,
            "high": self.important,
            "medium": self.working,
            "low": self.buffer
        }
        zone_map[priority].append(content)
        self._trim_if_needed()
    
    def _trim_if_needed(self):
        total = self._total_tokens()
        if total <= self.max_tokens:
            return
        
        # Phase 1: Trim buffer
        while self._total_tokens() > self.max_tokens and self.buffer:
            removed = self.buffer.pop(0)
            summary = self._summarize(removed)
            if summary:
                self.buffer.append(summary)
        
        # Phase 2: Summarize working memory
        if self._total_tokens() > self.max_tokens:
            self._compress_working()
    
    def _summarize(self, content):
        """Create a one-line summary of content"""
        # Implementation depends on available LLM
        pass
    
    def _compress_working(self):
        """Merge old working memory into summaries"""
        if len(self.working) > 5:
            old = self.working[:len(self.working)//2]
            self.working = self.working[len(self.working)//2:]
            summary = self._summarize("\n".join(old))
            self.important.append(summary)
```

## When to Use

| Scenario | Sliding Window? | Alternative |
|----------|:-:|-------------|
| Long coding sessions | ✅ | — |
| Multi-file refactoring | ✅ | — |
| Quick Q&A | ❌ | No memory management needed |
| Research across many sources | ⚠️ | Consider hierarchical memory |
| Multi-day projects | ⚠️ | Consider persistent memory |
