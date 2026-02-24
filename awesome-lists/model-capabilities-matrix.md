# AI Model Capabilities Matrix

> Quick reference for choosing the right AI model for the right task.

## Context Window Comparison (2025)

| Model | Context Window | Best At | Speed | Cost |
|-------|:---:|---------|:---:|:---:|
| **GPT-4o** | 128K | General tasks, coding, analysis | ⚡⚡⚡ | 💰💰 |
| **GPT-4o mini** | 128K | Fast, cheap general tasks | ⚡⚡⚡⚡ | 💰 |
| **Claude 3.5 Sonnet** | 200K | Coding, long documents, analysis | ⚡⚡⚡ | 💰💰 |
| **Claude 3.5 Haiku** | 200K | Fast coding, simple tasks | ⚡⚡⚡⚡ | 💰 |
| **Claude 3 Opus** | 200K | Complex reasoning, research | ⚡⚡ | 💰💰💰 |
| **Gemini 2.0 Flash** | 1M | Massive documents, multimodal | ⚡⚡⚡⚡ | 💰 |
| **Gemini 2.0 Pro** | 1M+ | Long-form analysis, multimodal | ⚡⚡⚡ | 💰💰 |
| **DeepSeek V3** | 128K | Coding, math, reasoning | ⚡⚡⚡ | 💰 |
| **Llama 3.3 70B** | 128K | Open-source, self-hosted | ⚡⚡ | Free |
| **Mistral Large** | 128K | European data compliance, coding | ⚡⚡⚡ | 💰💰 |
| **Grok 2** | 128K | Real-time data, social context | ⚡⚡⚡ | 💰💰 |

## Task Suitability

### 💻 Code Generation & Review
| Task | Top Pick | Runner Up | Why |
|------|----------|-----------|-----|
| Complex codebase changes | Claude 3.5 Sonnet | GPT-4o | Long context + code quality |
| Quick code snippets | GPT-4o mini | Claude Haiku | Speed + cost |
| Code review | Claude 3.5 Sonnet | GPT-4o | Catches subtle bugs |
| Debugging | Claude 3.5 Sonnet | GPT-4o | Methodical reasoning |
| Algorithm design | DeepSeek V3 | Claude Opus | Strong at logic/math |

### 📝 Writing & Content
| Task | Top Pick | Runner Up | Why |
|------|----------|-----------|-----|
| Technical documentation | Claude 3.5 Sonnet | GPT-4o | Clear, structured writing |
| Creative writing | Claude Opus | GPT-4o | Nuanced, literary quality |
| Summarization | Gemini Flash | GPT-4o mini | Speed + large context |
| Translation | GPT-4o | Gemini Pro | Broad language support |

### 🔍 Analysis & Research
| Task | Top Pick | Runner Up | Why |
|------|----------|-----------|-----|
| Long document analysis | Gemini Pro | Claude Sonnet | 1M+ context window |
| Data analysis | GPT-4o (Code Interpreter) | Claude Sonnet | Built-in execution |
| Scientific research | Claude Opus | GPT-4o | Deep reasoning |
| Legal/compliance review | Claude Sonnet | GPT-4o | Careful, thorough |

### 🤖 Agent & Automation
| Task | Top Pick | Runner Up | Why |
|------|----------|-----------|-----|
| Autonomous coding | Claude Sonnet | GPT-4o | Best tool-use + reasoning |
| Multi-step workflows | GPT-4o | Claude Sonnet | Consistent function calling |
| Data pipelines | GPT-4o mini | Gemini Flash | Speed + cost at scale |

## Model Selection Flowchart

```
What's your priority?
├── 💰 Cost → GPT-4o mini / Gemini Flash / DeepSeek
├── 🧠 Quality → Claude Opus / GPT-4o
├── ⚡ Speed → GPT-4o mini / Gemini Flash
├── 📏 Context Length → Gemini (1M+) / Claude (200K)
├── 🔒 Privacy → Llama (self-hosted) / Mistral (EU)
└── 💻 Code → Claude Sonnet / DeepSeek V3
```

## Prompting Style by Model

| Model Family | Prefers | Avoid |
|:---|---|---|
| **GPT-4** | System/user message split, function calling JSON | Overly long system prompts |
| **Claude** | XML tags, clear sections, thinking out loud | Jailbreak-style instructions |
| **Gemini** | Natural language, multimodal inputs | Overly rigid formatting |
| **DeepSeek** | Technical, direct instructions | Vague creative tasks |
| **Llama** | Short, direct prompts | Very long contexts (quality drops) |

## Cost Optimization Tips

1. **Start with the cheapest model** that works, then upgrade only if quality is insufficient
2. **Use fast/cheap models for filtering**, then expensive models for processing
3. **Cache responses** for repeated similar queries
4. **Batch requests** to reduce API overhead
5. **Use streaming** for user-facing applications (perceived speed)
