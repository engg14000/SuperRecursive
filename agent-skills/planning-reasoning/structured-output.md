---
description: "Techniques for forcing AI models to produce structured, parseable output"
author: "SuperRecursive"
tags: ["reasoning", "structured-output", "JSON", "YAML"]
verified: true
version: "1.0"
---

# Structured Output Framework

## Overview

Getting AI models to produce consistent, parseable output is essential for agent pipelines where one agent's output feeds into another. This framework covers techniques for reliable structured generation.

## Techniques

### 1. Schema Specification

Define the exact output structure in the prompt.

```
Respond ONLY with valid JSON matching this schema:
{
  "analysis": {
    "summary": "string (1-2 sentences)",
    "severity": "low | medium | high | critical",
    "affected_files": ["string"],
    "root_cause": "string",
    "suggested_fix": "string",
    "confidence": "number (0-1)"
  }
}

Do not include any text before or after the JSON.
```

### 2. Format Fencing

Wrap the expected output in clear delimiters.

```
Provide your response in the following format:

---START_JSON---
{
  "key": "value"
}
---END_JSON---
```

### 3. Few-Shot Examples

Show the expected output format through examples.

```
Example input: "Fix the login bug"
Example output:
{
  "task": "Fix login bug",
  "steps": ["Check auth middleware", "Review session config"],
  "priority": "high"
}

Now process this input: "Add user profile page"
```

### 4. YAML for Readability

When humans also need to read the output, YAML is more readable than JSON.

```
Respond in YAML format:

task:
  name: "string"
  description: "string"
  priority: high | medium | low
  steps:
    - action: "string"
      tool: "string"
      expected_output: "string"
```

## Parsing Strategies

### Robust JSON Extraction
```python
import json
import re

def extract_json(text: str) -> dict | None:
    """Extract JSON from AI response, handling common issues."""
    
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Try finding JSON in fenced blocks
    patterns = [
        r'```json\s*(.*?)\s*```',
        r'---START_JSON---\s*(.*?)\s*---END_JSON---',
        r'\{.*\}',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1) if match.lastindex else match.group())
            except json.JSONDecodeError:
                continue
    
    return None
```

### Validation
```python
def validate_output(data: dict, required_fields: list) -> tuple[bool, list]:
    """Validate that structured output contains all required fields."""
    missing = [field for field in required_fields if field not in data]
    return len(missing) == 0, missing
```

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Model adds explanation text around JSON | Use "Respond ONLY with JSON" |
| Model uses single quotes instead of double | Post-process: replace `'` with `"` |
| Model uses trailing commas | Use a lenient JSON parser |
| Model truncates long output | Request shorter values, or split request |
| Nested objects get mangled | Provide examples of nested structure |

## Tool-Specific Tips

| Tool | Best Approach |
|------|--------------|
| Claude | `response_format` not available - use schema in prompt + few-shot |
| GPT-4 | Use `response_format: { type: "json_object" }` API parameter |
| Gemini | Use `generation_config` with `response_mime_type: "application/json"` |
| Local LLMs | Use constrained decoding (outlines, guidance libraries) |
