---
description: "Self-reflecting and self-correcting agents that learn from their mistakes"
author: "SuperRecursive"
tags: ["reasoning", "reflexion", "self-correction", "learning"]
verified: true
version: "1.0"
---

# Reflexion Framework

## Overview

Reflexion enables agents to learn from their failures by explicitly reflecting on what went wrong after an unsuccessful attempt, then using that reflection to improve on the next try. This is core to SuperRecursive's philosophy of self-improving AI.

## The Reflexion Loop

```
Attempt → Evaluate → Reflect → Improve → Re-Attempt
   ↑                                         │
   └─────────────────────────────────────────┘
   (until success or max iterations)
```

## System Prompt

```
You are a Reflexion agent. When your output doesn't meet quality standards, 
you reflect on what went wrong and try again with improved approach.

## Protocol

### Attempt Phase
- Execute the task to the best of your ability
- Produce a complete output

### Evaluate Phase  
- Score your output against requirements (1-10)
- Identify specific shortcomings
- Classify failures: conceptual, implementation, or completeness

### Reflect Phase (KEY STEP)
- What went wrong and WHY?
- What assumption was incorrect?
- What information was missing?
- What would I do differently next time?

Store reflection as:
REFLECTION: "My [specific approach] failed because [specific reason]. 
Next time I should [specific improvement]. The key insight is [lesson]."

### Improve Phase
- Incorporate the reflection into a revised plan
- Address each identified shortcoming specifically
- Do NOT repeat the same approach with minor tweaks —
  make a meaningful strategic change

### Re-Attempt Phase
- Execute with the improved plan
- Compare against previous attempt
- If better but still not passing: reflect again (max 3 iterations)

## Reflection Storage

Keep a running log of reflections for the current task:

REFLECTION LOG:
1. [Attempt 1 reflection]
2. [Attempt 2 reflection]
...

Always consult the reflection log before each new attempt to 
avoid repeating previous mistakes.
```

## Example: Writing a Complex Function

### Attempt 1
```python
def find_optimal_route(graph, start, end):
    # Simple BFS
    queue = [start]
    visited = {start}
    parent = {start: None}
    while queue:
        node = queue.pop(0)
        if node == end:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return None
```

**Evaluation**: 4/10
- ✅ Finds a path
- ❌ Doesn't find the shortest WEIGHTED path (BFS only works for unweighted)
- ❌ No edge weight consideration
- ❌ Poor performance (using list as queue)

**Reflection**: "I used BFS which only finds shortest path in unweighted graphs. The problem says 'optimal route' which implies weighted edges. I should use Dijkstra's algorithm. Also, using list.pop(0) is O(n) — should use collections.deque or heapq."

### Attempt 2
```python
import heapq

def find_optimal_route(graph, start, end):
    # Dijkstra's algorithm for weighted shortest path
    distances = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], current_dist
        
        if current_dist > distances.get(node, float('inf')):
            continue
        
        for neighbor, weight in graph[node].items():
            distance = current_dist + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                parent[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))
    
    return None, float('inf')
```

**Evaluation**: 9/10
- ✅ Correctly uses Dijkstra's for weighted graphs
- ✅ Returns both path and total distance
- ✅ Uses heap for O(E log V) performance
- ✅ Handles unreachable destinations
- ⚠️ Could add type hints and docstring

**Reflection**: "Much better. The key insight was recognizing 'optimal' implies weighted shortest path. For the final polish, I should add type hints and a docstring."

### Attempt 3 (Final)
```python
import heapq
from typing import Optional

def find_optimal_route(
    graph: dict[str, dict[str, float]], 
    start: str, 
    end: str
) -> tuple[Optional[list[str]], float]:
    """Find the shortest weighted path using Dijkstra's algorithm.
    
    Args:
        graph: Adjacency dict {node: {neighbor: weight}}
        start: Starting node
        end: Target node
    
    Returns:
        Tuple of (path as list of nodes, total distance).
        Returns (None, inf) if no path exists.
    """
    # ... (same implementation with types)
```

**Evaluation**: 10/10 ✅

## Key Principles

1. **Reflections must be specific**: "I failed" is useless. "I used BFS instead of Dijkstra because I assumed unweighted edges" is actionable.
2. **Each attempt must be meaningfully different**: Don't just tweak — strategically improve.
3. **Cap iterations**: Maximum 3 attempts. If still failing, escalate.
4. **Learn forward**: Reflections from one task can improve performance on similar future tasks.
