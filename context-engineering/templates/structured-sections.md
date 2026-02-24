---
description: "Organize context into labeled sections for long-context windows"
author: "SuperRecursive"
tags: ["context-engineering", "long-context", "structure"]
verified: true
version: "1.0"
---

# Structured Sections Strategy

## Overview

When working with 100k+ token context windows, organizing content into clearly labeled, delimited sections prevents the model from confusing information sources.

## Template

```markdown
# +--------------------------------------+
# ¦ SECTION 1: INSTRUCTIONS             ¦
# +--------------------------------------+

[Your instructions here]

# +--------------------------------------+
# ¦ SECTION 2: REFERENCE MATERIAL       ¦
# +--------------------------------------+

[Reference documents here]

# +--------------------------------------+
# ¦ SECTION 3: CURRENT WORK             ¦
# +--------------------------------------+

[Active task content here]

# +--------------------------------------+
# ¦ SECTION 4: OUTPUT REQUIREMENTS      ¦
# +--------------------------------------+

[What you want back here]
```

## Delimiter Options (Ranked by Effectiveness)

| Style | Example | Best For |
|-------|---------|----------|
| XML tags | `<instructions>...</instructions>` | Programmatic contexts |
| Box drawing | `+---+ ... +---+` | Visual clarity |
| Markdown headers | `## Section Name` | General use |
| Separator lines | `---` or `===` | Simple separation |
| Numbered labels | `[SECTION 1/4]` | Sequential processing |

## Key Principles

1. **Name sections descriptively** - not "Section 1" but "INSTRUCTIONS" or "CODEBASE"
2. **Use consistent delimiters** - don't mix styles within one context
3. **Reference sections explicitly** - "As described in SECTION 2..."
4. **Keep critical info at boundaries** - start and end of each section get more attention
5. **Number sections** when order matters for processing
