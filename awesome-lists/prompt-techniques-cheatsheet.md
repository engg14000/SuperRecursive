# Prompt Techniques Cheat Sheet

> Every major prompting technique at a glance. Bookmark this.

## Quick Reference

| Technique | One-Liner | Best For | Complexity |
|-----------|-----------|----------|:---:|
| **Zero-Shot** | Just ask the question directly | Simple tasks, factual Q&A | ? |
| **Few-Shot** | Provide 2-5 examples before asking | Classification, formatting | ?? |
| **Chain-of-Thought (CoT)** | "Think step by step" | Math, logic, debugging | ?? |
| **Zero-Shot CoT** | Append "Let's think step by step" | Quick reasoning without examples | ? |
| **Tree-of-Thought (ToT)** | Explore multiple solution paths | Design decisions, complex problems | ??? |
| **ReAct** | Interleave Thought ? Action ? Observation | Research, investigation, tool use | ??? |
| **Reflexion** | Try ? Evaluate ? Reflect ? Retry | Iterative improvement, code writing | ??? |
| **Self-Consistency** | Generate multiple answers, pick majority | High-stakes decisions | ?? |
| **Role Prompting** | "You are a senior {role}" | Domain-specific answers | ? |
| **Structured Output** | "Respond in JSON/YAML/table format" | Data extraction, pipelines | ?? |
| **Mega-Prompt** | One massive, multi-section prompt | Complex one-shot tasks | ??? |
| **Prompt Chaining** | Output of prompt A feeds into prompt B | Multi-step workflows | ??? |

## Technique Details

### Zero-Shot
```
What is the capital of France?
```
**When**: Simple questions, well-defined tasks
**When NOT**: Ambiguous tasks, specific formatting needed

---

### Few-Shot
```
Classify the sentiment:

"I love this product!" ? Positive
"Terrible experience." ? Negative
"It's okay I guess." ? Neutral

"Best purchase I've ever made!" ? 
```
**When**: Classification, consistent formatting, the model needs to see the pattern
**When NOT**: Creative tasks, simple questions
**Tip**: 3-5 examples is usually the sweet spot

---

### Chain-of-Thought (CoT)
```
Solve this step by step:

A store has 50 apples. They sell 30% on Monday, then receive a 
delivery of 20 apples on Tuesday. How many apples do they have?

Think through each step before giving the final answer.
```
**When**: Math, logic puzzles, debugging, multi-step reasoning
**When NOT**: Simple factual recall, creative writing
**Tip**: "Think step by step" alone boosts accuracy ~30% on reasoning tasks

---

### Tree-of-Thought (ToT)
```
I need to design a caching strategy. Consider 3 different approaches:

For each approach:
1. Describe the approach
2. List pros and cons
3. Rate complexity (1-10)
4. Rate effectiveness (1-10)

Then compare all approaches and recommend the best one.
```
**When**: Architecture decisions, comparing trade-offs, creative exploration
**When NOT**: Tasks with one obvious answer

---

### ReAct
```
Investigate why the API response time increased by 200ms.

Use this pattern:
Thought: [What I think might be happening]
Action: [What I'll check/do next]
Observation: [What I found]
... repeat until solved ...
Final Answer: [Root cause and fix]
```
**When**: Debugging, research, information gathering with tools
**When NOT**: Simple generation tasks

---

### Reflexion
```
Write a function to merge two sorted arrays.

After writing it, evaluate your solution:
- Is it correct for edge cases (empty arrays, single elements)?
- Is the time complexity optimal?
- Is it readable?

If any issues found, write an improved version.
```
**When**: Code generation, essay writing, anything iterative
**When NOT**: Quick answers, time-sensitive tasks

---

### Role Prompting
```
You are a senior security engineer with 15 years of experience 
in web application security and a deep knowledge of OWASP Top 10.

Review this code for security vulnerabilities...
```
**When**: Domain expertise needed, consistent persona
**Tip**: Be specific - "senior security engineer" > "expert"

---

### Structured Output
```
Extract the following from this job posting and return as JSON:

{
  "title": "",
  "company": "",
  "salary_range": { "min": 0, "max": 0, "currency": "" },
  "required_skills": [],
  "experience_years": 0,
  "remote": true/false
}
```
**When**: Data extraction, API responses, pipeline inputs
**Tip**: Provide the exact schema you want filled

## Combination Recipes

The most powerful prompts combine techniques:

| Combo | How | Use Case |
|-------|-----|----------|
| **Role + CoT** | Expert persona + step-by-step | Technical analysis |
| **Few-Shot + Structured** | Examples + JSON format | Consistent data extraction |
| **ReAct + CoT** | Investigation + reasoning | Complex debugging |
| **Reflexion + CoT** | Self-improve + reasoning | High-quality code |
| **Role + Mega-Prompt** | Expert + comprehensive context | Production system prompts |

## Token Efficiency Tips

| Tip | Example | Savings |
|-----|---------|:---:|
| Use abbreviations in schema | `"desc"` vs `"description"` | ~10% |
| Omit obvious fields | Skip `"type": "string"` | ~15% |
| Use shorthand instructions | `"Be concise"` vs long explanation | ~20% |
| Structured delimiters | `###` vs verbose XML tags | ~5% |
