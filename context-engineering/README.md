# ?? Context Engineering

> The art and science of feeding AI models the right information at the right time. Templates, strategies, and recursive frameworks for maximizing AI output quality.

## ?? Contents

- [Templates](templates/) - RAG, long-context, structured context formats
- [Recursive](recursive/) - Self-improving prompt chains (SuperRecursive signature)
- [Meta-Prompting](meta-prompting/) - Prompts that generate and optimize prompts
- [Benchmarks](benchmarks/) - Evaluation frameworks for context quality

## ?? What is Context Engineering?

Context engineering is the discipline of **crafting the information environment** around an AI model to maximize output quality. It goes beyond prompt engineering by considering:

1. **What** information to include (relevance)
2. **How** to structure it (format)
3. **Where** to place it (position within context window)
4. **When** to update it (freshness)
5. **How much** to include (density vs. noise)

## ?? Core Principles

| Principle | Description |
|-----------|-------------|
| **Relevance** | Only include information the model needs for the current task |
| **Structure** | Use clear sections, headers, and delimiters |
| **Position** | Place critical info at the start and end (attention peaks) |
| **Density** | Compress low-value info, expand high-value info |
| **Freshness** | Update dynamic context, keep static context stable |
| **Consistency** | Use the same format across similar contexts |

## ?? Related Sections

- [Agent Skills](../agent-skills/) - Memory management directly supports context engineering
- [Vibe Coding](../vibe-coding/) - Mood-based context adaptation
- [System Prompts](../) - Tool-specific context optimization
