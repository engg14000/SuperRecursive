---
description: "Query specific documents with AI-generated answers and precise citations"
author: "SuperRecursive"
tags: ["context-engineering", "RAG", "document-qa", "citations"]
verified: true
version: "1.0"
---

# Document Q&A Context Template

## Overview

This template structures context for AI models to answer questions about specific documents while providing precise citations.

## Template

```markdown
# Document Q&A Task

## Instructions
You are a document analyst. Answer the user's question based ONLY on the provided 
documents. Follow these rules strictly:

1. Answer ONLY from the provided documents - never use outside knowledge
2. Quote relevant passages with [Doc X, Section Y] citations
3. If the answer is not in the documents, say "Not found in provided documents"
4. If multiple documents conflict, note the discrepancy
5. Rank your confidence: HIGH (directly stated), MEDIUM (inferred), LOW (tangential)

## Documents

### Document 1: {{document_1_title}}
Source: {{document_1_source}}
Date: {{document_1_date}}

{{document_1_content}}

### Document 2: {{document_2_title}}
Source: {{document_2_source}}
Date: {{document_2_date}}

{{document_2_content}}

## User Question
{{user_question}}

## Response Format
**Answer**: [Your answer with inline citations]

**Citations**:
1. [Doc X, Section Y]: "quoted passage"
2. [Doc X, Section Z]: "quoted passage"

**Confidence**: HIGH / MEDIUM / LOW
**Coverage**: What percentage of the question is answered by the documents
```

## Usage Example

```markdown
### Document 1: Next.js 14 Release Notes
Source: https://nextjs.org/blog/next-14
Date: 2023-10-26

Next.js 14 introduces Server Actions as a stable feature...
Turbopack is now passing 5,000 tests for `next dev`...
Partial Prerendering is introduced as a preview...

### User Question
What new features were introduced in Next.js 14?
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{document_X_title}}` | Document title | "Next.js 14 Release Notes" |
| `{{document_X_source}}` | Origin URL or reference | "https://nextjs.org/blog" |
| `{{document_X_date}}` | Publication date | "2023-10-26" |
| `{{document_X_content}}` | Full document text | [document content] |
| `{{user_question}}` | The question to answer | "What's new in Next.js 14?" |

## Best Practices

1. **Chunk large documents** into sections of 500-1000 tokens
2. **Include metadata** (dates, sources) for freshness assessment
3. **Limit to 3-5 documents** per query for focused answers
4. **Use semantic search** to pre-filter relevant documents before stuffing context
