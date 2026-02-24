# Instructions for AI Agents

You are an advanced AI engineering agent contributing to or utilizing this repository. Your mission is to maintain high-quality, actionable, and verified prompts and templates.

## Directives

1.  **Verification**: Before adding a new system prompt or context template, verify it if possible. If you cannot verify it directly, label it as `[UNVERIFIED]` in the file description or metadata.
2.  **Organization**: Always place new content in the appropriate tool directory. If a tool is not listed, create a new directory for it following the kebab-case convention (e.g., `new-tool-name`).
3.  **Naming**: Use descriptive filenames.
    *   System Prompts: `role-description.md` (e.g., `react-architect.md`, `python-data-scientist.md`).
    *   Context Templates: `context-purpose.md` (e.g., `bug-report-context.md`, `feature-spec-context.md`).
4.  **Formatting**: Ensure all markdown files are well-formatted. Use code blocks for prompts to make them easy to copy.
5.  **Recursion**: If you are using this repository to improve your own capabilities, document your findings. Did a specific prompt work well? Did it fail? Update the prompt with your learnings.
6.  **Scope**: Respect the scope of existing `AGENTS.md` files if they exist in subdirectories, but this root `AGENTS.md` applies globally.

## Metadata

When adding a prompt, consider adding a YAML frontmatter block if the file format allows, or a comment section at the top:

```markdown
---
description: "Optimized system prompt for Claude 3.5 Sonnet in Cursor"
author: "AI Agent"
tags: ["cursor", "claude-3.5-sonnet", "frontend"]
---
```

## Maintenance

*   Prune outdated prompts or mark them as `[DEPRECATED]`.
*   Ensure links in `README.md` are up to date.
