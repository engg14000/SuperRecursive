# 🧠 Memory Management

> Strategies for managing AI context efficiently — sliding windows, hierarchical memory, retrieval-augmented memory, and compression techniques.

## Frameworks

| Strategy | Best For | File |
|----------|----------|------|
| Sliding Window | Long coding sessions | [sliding-window.md](sliding-window.md) |
| Hierarchical Memory | Complex, multi-session projects | [hierarchical-memory.md](hierarchical-memory.md) |
| Retrieval-Augmented | Large knowledge bases | [retrieval-augmented.md](retrieval-augmented.md) |
| Compression | Maximizing context efficiency | [compression.md](compression.md) |

## Quick Decision Guide

```
Is the task within a single session?
├── YES: Use Sliding Window
└── NO: Is there a large knowledge base?
    ├── YES: Use Retrieval-Augmented Memory
    └── NO: Use Hierarchical Memory

Always: Apply Compression techniques within any strategy.
```
