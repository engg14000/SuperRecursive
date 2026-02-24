---
description: "Layer context from high-level to detailed for progressive understanding"
author: "SuperRecursive"
tags: ["context-engineering", "progressive-disclosure", "layered"]
verified: true
version: "1.0"
---

# Progressive Disclosure Strategy

## Overview

Start with a high-level overview and progressively add detail. This helps the model build a mental model before diving into specifics, mimicking how humans understand complex systems.

## The Pyramid Pattern

```
        /\
       /  \        Level 1: ONE-SENTENCE SUMMARY
      /    \       "We're building a real-time chat app"
     /──────\
    /        \     Level 2: KEY COMPONENTS
   /          \    "Auth, messaging, presence, notifications"
  /────────────\
 /              \  Level 3: ARCHITECTURE
/                \ "WebSocket server, Redis pub/sub, PostgreSQL"
/──────────────────\
                    Level 4: IMPLEMENTATION DETAILS
                    "Specific code, configs, APIs"
```

## Template

```markdown
# Level 1: Executive Summary
{{one_paragraph_overview}}

# Level 2: Components & Relationships 
## Components
{{component_list_with_one_line_descriptions}}

## How They Connect
{{simple_architecture_diagram}}

# Level 3: Architecture & Design
## Component Details
{{for_each_component_detailed_description}}

## Data Flow
{{data_flow_description}}

## Technology Choices
{{tech_stack_with_rationale}}

# Level 4: Implementation
## Current Code
{{relevant_source_files}}

## Configuration
{{config_files}}

## API Endpoints
{{api_specification}}

# Task
Now that you understand the full system from high level to implementation details,
please: {{specific_task}}
```

## Why This Works

1. **Reduces hallucination**: The model understands the "why" before the "what"
2. **Enables better decisions**: Understanding architecture prevents local-optimum choices
3. **Catches conflicts early**: High-level constraints frame detailed implementation
4. **Natural for humans too**: If a human can't follow it, the model probably can't either

## When to Use

| Use Case | Progressive Disclosure? |
|----------|:----------------------:|
| New developer onboarding | ✅ Essential |
| Complex system modification | ✅ Very helpful |
| Simple bug fix | ❌ Just show the bug |
| Code review | ⚠️ Only if reviewer needs context |
| Architecture discussion | ✅ Perfect fit |
