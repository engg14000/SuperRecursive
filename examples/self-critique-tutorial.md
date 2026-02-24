---
description: "Tutorial: Transform any prompt from OK to excellent using self-critique"
author: "SuperRecursive"
tags: ["tutorial", "self-critique", "optimization"]
verified: true
version: "1.0"
---

# Optimize Any Prompt with the Self-Critique Loop

## Scenario

You have a prompt that works "OK" but you want it to be excellent. We'll use SuperRecursive's Self-Critique Loop to systematically improve it.

## Starting Prompt (Before)

```
Write a Python function that processes data.
```

This is vague and will produce inconsistent results. Let's improve it.

## Iteration 1: Apply the Critique

### Score the prompt

| Dimension | Score |
|-----------|:---:|
| Clarity | 2/10 - What data? What processing? |
| Specificity | 1/10 - Almost no details |
| Format | 1/10 - No output format specified |
| Constraints | 0/10 - No rules |
| Examples | 0/10 - No examples |

### Improve

```
Write a Python function that reads a CSV file and returns a summary dictionary 
with column names, row count, and data types for each column.
```

## Iteration 2: Score Again

| Dimension | Score |
|-----------|:---:|
| Clarity | 6/10 - Much clearer |
| Specificity | 5/10 - Some details still missing |
| Format | 3/10 - "summary dictionary" is vague |
| Constraints | 2/10 - No error handling mentioned |
| Examples | 0/10 - Still no examples |

### Improve

```
Write a Python function called `analyze_csv` that:

Input: A file path to a CSV file (string)

Processing:
1. Read the CSV file using pandas
2. For each column, determine: name, data type, null count, unique values count
3. Calculate total rows and columns

Output: Return a dictionary with this structure:
{
    "total_rows": int,
    "total_columns": int,
    "columns": [
        {
            "name": str,
            "dtype": str,
            "null_count": int,
            "unique_count": int
        }
    ]
}

Error handling:
- Raise FileNotFoundError if file doesn't exist
- Raise ValueError if file is not valid CSV
- Handle empty files gracefully (return zeros)

Include type hints and a docstring.
```

## Iteration 3: Score Again

| Dimension | Score |
|-----------|:---:|
| Clarity | 9/10 - Very clear |
| Specificity | 9/10 - Detailed requirements |
| Format | 9/10 - Exact output structure |
| Constraints | 8/10 - Error handling specified |
| Examples | 7/10 - Implicit example in output spec |

**All scores = 7** ? Finalized! ?

## Result

| Metric | Before | After | Improvement |
|--------|:---:|:---:|:---:|
| Clarity | 2/10 | 9/10 | +350% |
| Specificity | 1/10 | 9/10 | +800% |
| Format | 1/10 | 9/10 | +800% |
| Constraints | 0/10 | 8/10 | 8 |
| Average | 0.8 | 8.8 | **+1000%** |

## The Pattern

You can use this on ANY prompt:
1. Score it on clarity, specificity, format, constraints, examples
2. Find the lowest-scoring dimension
3. Improve that specific dimension
4. Re-score
5. Repeat until all = 7
