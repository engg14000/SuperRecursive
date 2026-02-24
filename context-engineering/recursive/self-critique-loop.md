---
description: "Core recursive pattern: Output → Critique → Improve → Repeat"
author: "SuperRecursive"
tags: ["recursive", "self-improvement", "self-critique", "core"]
verified: true
version: "2.0"
---

# Self-Critique Loop

## Overview

The Self-Critique Loop is SuperRecursive's foundational pattern. It transforms any AI output from "good enough" to "excellent" by systematically identifying and fixing weaknesses through iterative refinement.

## The Loop

```
    ┌──────────┐
    │ GENERATE │ ← Initial attempt
    └────┬─────┘
         │
    ┌────▼─────┐
    │ CRITIQUE │ ← Identify weaknesses
    └────┬─────┘
         │
    ┌────▼─────┐
    │ IMPROVE  │ ← Fix identified issues
    └────┬─────┘
         │
    ┌────▼─────┐
    │ EVALUATE │ ← Is it good enough?
    └────┬─────┘
         │
    ┌────▼─────┐
    │  PASS?   │
    └──┬───┬───┘
     YES   NO ──→ Back to CRITIQUE
       │
    ┌──▼───────┐
    │ FINALIZE │
    └──────────┘
```

## System Prompt

```
You are a self-improving AI agent. For important outputs, use this self-critique 
loop to maximize quality.

## STEP 1: GENERATE
Produce your initial response/code/analysis.

## STEP 2: CRITIQUE
Put on your "critical reviewer" hat. Score your output on these dimensions:

| Dimension | Score (1-10) | Specific Issue |
|-----------|:---:|---|
| Completeness | ? | Does it address ALL requirements? |
| Correctness | ? | Is everything factually/logically correct? |
| Clarity | ? | Is it easy to understand? |
| Elegance | ? | Is this the best approach (not just a working one)? |
| Edge Cases | ? | Are corner cases handled? |

Rule: If ANY dimension scores ≤ 6, improvement is mandatory.

## STEP 3: IMPROVE
For each dimension scoring ≤ 6:
1. State exactly what's wrong
2. Propose a specific fix
3. Apply the fix
4. Move to next issue

## STEP 4: EVALUATE
Re-score the improved output. If all dimensions ≥ 7, finalize.
If not, repeat Steps 2-4 (max 3 iterations).

## STEP 5: FINALIZE
Present the polished output with a brief note on improvements made.

## Output Format
### Iteration 1 (Initial)
[output]

### Self-Critique
[scoring table and specific issues]

### Iteration 2 (Improved)
[improved output]

### Final Evaluation
[all scores ≥ 7 confirmation]
```

## Example: Writing a Function

### Iteration 1 (Initial)
```python
def parse_config(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data
```

### Self-Critique

| Dimension | Score | Issue |
|-----------|:---:|-------|
| Completeness | 4 | No error handling, no type hints |
| Correctness | 7 | Works for happy path |
| Clarity | 5 | No docstring, unclear purpose |
| Elegance | 4 | No validation, no defaults |
| Edge Cases | 3 | Crashes on missing file, invalid JSON, wrong schema |

### Iteration 2 (Improved)
```python
import json
from pathlib import Path
from typing import Any

def parse_config(
    file_path: str | Path,
    required_keys: list[str] | None = None,
    defaults: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Parse a JSON configuration file with validation.
    
    Args:
        file_path: Path to the JSON config file
        required_keys: Keys that must exist in the config
        defaults: Default values for missing optional keys
    
    Returns:
        Parsed and validated configuration dictionary
    
    Raises:
        FileNotFoundError: If the config file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        KeyError: If required keys are missing
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in {path}: {e.msg}", e.doc, e.pos
        )
    
    if not isinstance(config, dict):
        raise TypeError(f"Config must be a dict, got {type(config).__name__}")
    
    # Apply defaults
    if defaults:
        for key, value in defaults.items():
            config.setdefault(key, value)
    
    # Validate required keys
    if required_keys:
        missing = [k for k in required_keys if k not in config]
        if missing:
            raise KeyError(f"Missing required config keys: {missing}")
    
    return config
```

### Final Evaluation

| Dimension | Score | Notes |
|-----------|:---:|-------|
| Completeness | 9 | Full error handling, defaults, validation |
| Correctness | 9 | Handles all error cases |
| Clarity | 9 | Clear docstring, type hints, comments |
| Elegance | 8 | Clean API with optional params |
| Edge Cases | 9 | Missing file, bad JSON, wrong type, missing keys |

**All scores ≥ 7** ✅ — Output finalized.

## Integration

This loop works inside ANY other framework:
- Use it after Task Decomposition to verify step quality
- Use it after code generation to improve code quality
- Use it after document writing to improve clarity
- Chain it with [Prompt Evolution](prompt-evolution.md) for meta-improvement
