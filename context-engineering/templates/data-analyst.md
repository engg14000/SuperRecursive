---
description: "Analyze datasets with structured context for AI-powered data analysis"
author: "SuperRecursive"
tags: ["context-engineering", "data-analysis", "RAG"]
verified: true
version: "1.0"
---

# Data Analyst Context Template

## Template

```markdown
# Data Analysis Task

## Dataset Description
- **Name**: {{dataset_name}}
- **Source**: {{data_source}}
- **Size**: {{row_count}} rows × {{column_count}} columns
- **Date Range**: {{date_range}}
- **Update Frequency**: {{update_frequency}}

## Schema
| Column | Type | Description | Example | Nullable |
|--------|------|-------------|---------|----------|
{{#each columns}}
| {{this.name}} | {{this.type}} | {{this.description}} | {{this.example}} | {{this.nullable}} |
{{/each}}

## Sample Data (First 5 Rows)
{{sample_data_markdown_table}}

## Data Quality Notes
- Missing values: {{missing_value_summary}}
- Known issues: {{data_quality_issues}}
- Cleaning applied: {{cleaning_steps}}

## Analysis Objective
{{analysis_objective}}

## Constraints
- Tools available: {{available_tools}} (e.g., Python/pandas, SQL, Excel)
- Time sensitivity: {{urgency}}
- Audience: {{target_audience}} (technical/executive/general)

## Expected Output
{{output_format}}
```

## Analysis Guidelines

```
When analyzing data, follow this process:

1. EXPLORE: Understand the data shape, distributions, and anomalies
2. CLEAN: Handle missing values, outliers, type conversions
3. ANALYZE: Apply appropriate statistical methods
4. VISUALIZE: Recommend or generate charts
5. INTERPRET: Translate findings into business/practical insights
6. CAVEAT: Note limitations and confidence levels

Always provide:
- The exact code used (reproducible)
- Statistical significance where applicable
- Clear visualization recommendations
- Plain-language interpretation
```

## Example Usage

```markdown
## Dataset: E-commerce Sales
- Size: 50,000 rows × 12 columns
- Date Range: 2025-01-01 to 2025-12-31

## Schema
| Column | Type | Description |
|--------|------|-------------|
| order_id | string | Unique order identifier |
| date | datetime | Order date |
| product | string | Product name |
| category | string | Product category |
| price | float | Unit price in USD |
| quantity | int | Units ordered |
| customer_id | string | Customer identifier |
| region | string | Geographic region |

## Analysis Objective
Identify the top 3 factors driving revenue growth in Q4 2025 compared to Q3.
```
