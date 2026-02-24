# Prompt Anti-Patterns

> The most common mistakes in prompt engineering - and how to fix each one.

## The Anti-Pattern Catalog

### 1. ?? The Vague Commander
**Anti-Pattern**: Giving unclear, ambiguous instructions.

? **Bad**:
```
Help me with my code.
```

? **Fix**:
```
Review the following Python function for bugs. Focus on:
1. Off-by-one errors
2. Null/None handling
3. Type mismatches

For each bug found, show the fix.
```

**Why it fails**: The AI has no idea what kind of help you want, so it guesses - often poorly.

---

### 2. ?? The Kitchen Sink
**Anti-Pattern**: Cramming everything into one prompt.

? **Bad**:
```
Write a full-stack e-commerce app with authentication, payments, 
inventory management, shipping integration, analytics dashboard, 
admin panel, email notifications, and mobile responsiveness.
```

? **Fix**: Break it into focused prompts:
```
Step 1: "Design the database schema for an e-commerce app with 
users, products, orders, and inventory."

Step 2: "Implement the authentication API using the schema from Step 1."

Step 3: "Build the product catalog endpoints..."
```

**Why it fails**: The AI can't hold this many requirements in working memory. Quality drops for every requirement after ~5.

---

### 3. ?? The Lazy Persona
**Anti-Pattern**: Using vague or meaningless role assignments.

? **Bad**:
```
You are an expert. Help me.
```

? **Fix**:
```
You are a senior backend engineer specializing in PostgreSQL 
performance optimization. You have 10+ years of experience 
diagnosing slow queries in high-traffic production systems.
```

**Why it fails**: "Expert" means nothing. The AI needs a *specific* expert with *specific* expertise.

---

### 4. ?? The Invisible Format
**Anti-Pattern**: Not specifying how output should be structured.

? **Bad**:
```
Compare React and Vue.
```

? **Fix**:
```
Compare React and Vue using this table:

| Aspect | React | Vue | Winner |
|--------|-------|-----|--------|
| Learning curve | | | |
| Performance | | | |
| Ecosystem | | | |
| TypeScript support | | | |
| Job market | | | |
```

**Why it fails**: Without a format, every response looks different. You can't build reliable workflows on unpredictable output.

---

### 5. ?? The Hallucination Enabler
**Anti-Pattern**: Asking in ways that encourage the AI to make things up.

? **Bad**:
```
What does the research say about X?
```

? **Fix**:
```
What is known about X? For each claim:
- State your confidence level (high/medium/low)
- If you're unsure, explicitly say so
- Do NOT make up citations or statistics
```

**Why it fails**: The AI wants to be helpful. Without guardrails, it'll confidently present fiction as fact.

---

### 6. ?? The Eternal Context
**Anti-Pattern**: Relying on the AI remembering everything from a long conversation.

? **Bad** (in message 47 of a conversation):
```
Now apply that change to the other file.
```

? **Fix**:
```
Apply the same error handling pattern we used in auth.ts 
(try-catch with custom AppError) to the file api/users.ts, 
specifically in the getUserById function on line 45.
```

**Why it fails**: AI attention degrades for information in the middle of long conversations. Re-state critical context.

---

### 7. ?? The Yes-Man Prompt
**Anti-Pattern**: Not asking the AI to challenge your assumptions.

? **Bad**:
```
My plan is to use MongoDB for this real-time stock trading app. 
Implement it.
```

? **Fix**:
```
My plan is to use MongoDB for a real-time stock trading app. 
Before implementing, critique this choice:
- Is MongoDB the right database for this use case?
- What are the potential issues?
- What alternatives should I consider?
- Give me your honest recommendation, even if it disagrees with my choice.
```

**Why it fails**: The AI defaults to agreement. Without explicit permission to disagree, it won't tell you when you're making a mistake.

---

### 8. ?? The One-Shot Wonder
**Anti-Pattern**: Expecting perfect output on the first try.

? **Bad**: Write prompt ? Get output ? Accept it

? **Fix**: Write prompt ? Get output ? Critique it ? Refine ? Repeat
```
[After receiving initial output]

Good start. Now improve this by:
1. Adding error handling for network failures
2. Making the variable names more descriptive
3. Adding input validation for the email field
```

**Why it fails**: First outputs are drafts. The best results come from iterative refinement - which is the entire philosophy behind SuperRecursive.

---

### 9. ?? The Secret Keeper
**Anti-Pattern**: Not providing necessary context.

? **Bad**:
```
Fix this error: "Cannot read property 'id' of undefined"
```

? **Fix**:
```
Fix this error: "Cannot read property 'id' of undefined"

Context:
- File: src/api/orders.ts, line 42
- This happens when calling GET /orders/:id with a non-existent ID
- Using Express.js + TypeScript + Prisma ORM
- Database: PostgreSQL
- The route handler:
[paste relevant code]
```

**Why it fails**: The AI can't see your codebase, your environment, or your error logs. The more context you provide, the better the fix.

---

### 10. ?? The "Just Do Everything"
**Anti-Pattern**: No constraints or boundaries on AI behavior.

? **Bad**:
```
Build me a website.
```

? **Fix**:
```
Build a landing page with these constraints:
- Tech: HTML + CSS + vanilla JavaScript (no frameworks)
- Sections: hero, features (3 cards), testimonials, CTA
- Style: dark mode, modern, glassmorphism effects
- Must be responsive (mobile + desktop)
- Must load in < 2 seconds (no heavy libraries)
- No placeholder text - use realistic copy for a SaaS product
```

**Why it fails**: Without constraints, the AI has infinite solution space and will pick the most generic option.

## Summary: The Fix Formula

Every good prompt has:

```
1. ROLE    - Who the AI is (specific expertise)
2. TASK    - What to do (clear action verb)
3. CONTEXT - Background information needed
4. FORMAT  - How to structure the output
5. CONSTRAINTS - What NOT to do
6. EXAMPLES - What good output looks like
```

Missing any one of these increases the chance of a bad response significantly.
