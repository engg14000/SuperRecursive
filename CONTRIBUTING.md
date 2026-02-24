# ?? Contributing to SuperRecursive

Thank you for your interest in contributing! SuperRecursive thrives on community contributions from **humans and AI agents alike**.

## ?? Table of Contents

- [Quick Start](#quick-start)
- [What We Need](#what-we-need)
- [How to Contribute](#how-to-contribute)
- [Content Guidelines](#content-guidelines)
- [File Naming Conventions](#file-naming-conventions)
- [Folder Structure](#folder-structure)
- [Quality Standards](#quality-standards)
- [Pull Request Process](#pull-request-process)
- [Recognition](#recognition)

## Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/engg14000/SuperRecursive.git
cd SuperRecursive

# 2. Create a feature branch
git checkout -b feat/add-my-awesome-prompt

# 3. Add your content (see guidelines below)

# 4. Commit with a descriptive message
git add .
git commit -m "feat: add recursive debugging prompt for Cursor"

# 5. Push and open a PR
git push origin feat/add-my-awesome-prompt
```

## What We Need

### ?? High Priority

| Type | Description | Where to Add |
|------|-------------|--------------|
| **System Prompts** | Real system prompts from AI tools (leaked, extracted, or crafted) | `tool-name/system-prompts/` |
| **Recursive Variants** | Self-improving versions of existing prompts | `context-engineering/recursive/` |
| **Context Templates** | Structured context formats for specific use cases | `tool-name/context-templates/` |
| **New Tool Coverage** | Prompts for tools not yet in the repo | Create new `tool-name/` folder |

### ?? Medium Priority

| Type | Description | Where to Add |
|------|-------------|--------------|
| **Agent Skills** | Tool schemas, multi-agent patterns, memory strategies | `agent-skills/` |
| **Benchmarks** | Comparative evaluations with methodology | `benchmarks/` |
| **Vibe Coding Moods** | New mood-based prompt styles | `vibe-coding/moods/` |
| **Awesome List Entries** | New links for curated lists | `awesome-lists/` |

### ?? Nice to Have

| Type | Description | Where to Add |
|------|-------------|--------------|
| **Examples** | Real-world use cases and tutorials | `examples/` |
| **Tools** | Scripts that enhance the workflow | `tools/` |
| **Bug Fixes** | Fix typos, broken links, formatting | Anywhere |
| **Translations** | Multi-language prompt collections | `tool-name/translations/` |

## How to Contribute

### Adding a System Prompt

1. Navigate to the appropriate tool folder (e.g., `cursor/system-prompts/`)
2. Create a new `.md` file with a descriptive name
3. Use this template:

```markdown
---
description: "Brief description of what this prompt does"
author: "Your GitHub username or 'AI Agent'"
tags: ["tool-name", "model", "use-case"]
verified: true  # Set to false if not tested
version: "1.0"
---

# Tool Name: Prompt Title

## Role
[Describe the AI's role and persona]

## Core Capabilities
- Capability 1
- Capability 2
- Capability 3

## Guidelines
1. Guideline 1
2. Guideline 2

## Output Format
[Describe expected output structure]

## Example
**Input**: [Example user request]
**Output**: [Example AI response summary]
```

### Adding a Context Template

1. Navigate to `tool-name/context-templates/`
2. Use placeholders with `{{double_braces}}`
3. Document all variables at the top

### Adding a New Tool

1. Create a new directory: `tool-name/` (use kebab-case)
2. Create the standard subdirectories:
   - `system-prompts/`
   - `context-templates/`
   - `internal-tools/`
3. Create a `README.md` with:
   - Tool description
   - Links to official site
   - List of resources in the folder

### Adding to Awesome Lists

1. Open the relevant list in `awesome-lists/`
2. Add your entry in the correct category
3. Use this format: `- [Name](URL) - Brief description`
4. Ensure the link is valid and the description is accurate

## Content Guidelines

### Do ?

- **Be specific**: Include exact model versions, tool versions
- **Be actionable**: Prompts should be copy-paste ready
- **Be tested**: Try your prompt before submitting (mark as `[UNVERIFIED]` if not)
- **Be descriptive**: Clear filenames, frontmatter, and inline comments
- **Add examples**: Show input/output pairs when possible
- **Use YAML frontmatter**: Tags, description, author, version

### Don't ?

- **Don't submit untested, low-quality prompts** - quality over quantity
- **Don't duplicate** existing content without adding value (recursive upgrades welcome!)
- **Don't include API keys, secrets**, or personal information
- **Don't plagiarize** without attribution - reference original sources
- **Don't submit off-topic content** - keep it AI/LLM/agent focused

## File Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| System Prompts | `role-description.md` | `react-architect.md` |
| Context Templates | `context-purpose.md` | `bug-report-context.md` |
| Internal Tools | `tool-name.ext` | `git-workflow.yaml` |
| Agent Skills | `skill-name.md` | `task-decomposition.md` |
| Vibe Coding | `mood-name.md` | `zen-refactor.md` |

**General rules:**
- Use **kebab-case** (lowercase with hyphens)
- Be **descriptive** but concise
- Avoid abbreviations unless universally understood

## Folder Structure

When in doubt, follow this hierarchy:
```
tool-or-section/
+-- README.md                  # Overview and index
+-- system-prompts/            # AI role definitions
¦   +-- prompt-name.md
+-- context-templates/         # Structured contexts
¦   +-- template-name.md
+-- internal-tools/            # Configs and scripts
    +-- tool-name.ext
```

## Quality Standards

### Prompt Quality Checklist

Before submitting, ensure your prompt:

- [ ] Has YAML frontmatter (description, author, tags)
- [ ] Includes a clear role description
- [ ] Specifies output format expectations
- [ ] Has been tested with at least one AI model
- [ ] Contains no sensitive information
- [ ] Follows the file naming conventions
- [ ] Is properly formatted Markdown

### Recursive Enhancement Standard

If you're improving an existing prompt with recursive techniques:

- [ ] Document what the original prompt was
- [ ] Explain the recursive enhancement applied
- [ ] Show before/after quality comparison
- [ ] Tag with `recursive` in frontmatter

## Pull Request Process

1. **Title**: Use conventional commits format
   - `feat: add recursive debugging prompt for Cursor`
   - `fix: correct broken link in awesome-prompts`
   - `docs: improve Claude Code setup guide`

2. **Description**: Include:
   - What you added/changed
   - Which tool(s) it applies to
   - Whether it's been tested
   - Any special notes

3. **Review**: Maintainers will review within 48 hours

4. **Merge**: After approval, your PR will be merged into `main`

## Recognition

### ?? Hall of Fame

Contributors who submit **5+ quality prompts** get featured in our [Hall of Fame](community/hall-of-fame.md)!

### Levels

| Contributions | Badge | Perks |
|--------------|-------|-------|
| 1-4 | ?? Seedling | Listed in CONTRIBUTORS |
| 5-14 | ?? Growing | Hall of Fame entry |
| 15-29 | ?? Established | Featured contributor badge |
| 30+ | ?? Champion | Co-maintainer invitation |

### AI Agent Contributors

AI agents (Claude, GPT, Gemini, etc.) can also contribute! Document:
- Which AI agent generated the content
- The prompt used to generate it
- Any human verification performed

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

**Questions?** Open a [Discussion](https://github.com/engg14000/SuperRecursive/discussions) or reach out in an issue!

? **Thank you for making SuperRecursive better for everyone!**
