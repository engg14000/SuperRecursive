---
description: "Synthesize insights from multiple research sources into coherent analysis"
author: "SuperRecursive"
tags: ["context-engineering", "RAG", "research", "synthesis"]
verified: true
version: "1.0"
---

# Research Synthesizer Context Template

## Template

```markdown
# Research Synthesis Task

## Objective
Synthesize the following {{source_count}} sources into a comprehensive analysis 
of {{research_topic}}.

## Sources

{{#each sources}}
### Source {{@index}}: {{this.title}}
- **Type**: {{this.type}} (paper/blog/docs/video transcript)
- **Author**: {{this.author}}
- **Date**: {{this.date}}
- **Credibility**: {{this.credibility}} (peer-reviewed/official/community/unknown)

{{this.content}}

---
{{/each}}

## Synthesis Instructions
1. **Identify common themes** across all sources
2. **Note contradictions** between sources (cite which disagree)
3. **Assess evidence quality** — peer-reviewed > official docs > blog posts
4. **Extract actionable insights** — what should a practitioner do?
5. **Identify gaps** — what questions remain unanswered?

## Output Format

### Executive Summary (3-5 sentences)
[Overall synthesis]

### Key Findings
| # | Finding | Support | Confidence |
|---|---------|---------|------------|
| 1 | [Finding] | Sources 1, 3, 5 | High |
| 2 | [Finding] | Source 2 (contradicted by 4) | Medium |

### Points of Agreement
[What all/most sources agree on]

### Points of Contention  
[Where sources disagree, with citations]

### Gaps & Open Questions
[What's not covered or uncertain]

### Recommendations
[Actionable next steps based on synthesis]
```

## Variables

| Variable | Description |
|----------|-------------|
| `{{research_topic}}` | The topic being researched |
| `{{source_count}}` | Number of sources provided |
| `{{sources}}` | Array of source objects with title, type, author, date, credibility, content |

## Usage Tips

- **Limit to 5-8 sources** per synthesis for quality
- **Pre-sort by credibility** — academic papers first
- **Include dates** — recency matters in fast-moving fields
- **Mix source types** — papers + docs + blogs give balanced view
