---
description: "Navigate and understand large codebases with structured context"
author: "SuperRecursive"
tags: ["context-engineering", "RAG", "codebase", "navigation"]
verified: true
version: "1.0"
---

# Codebase Navigator Context Template

## Overview

Optimized context structure for helping AI models understand and work within large, complex codebases.

## Template

```markdown
# Codebase Context

## Project Overview
- **Name**: {{project_name}}
- **Language**: {{primary_language}}
- **Framework**: {{framework}}
- **Architecture**: {{architecture_pattern}} (e.g., MVC, microservices, monorepo)
- **Package Manager**: {{package_manager}}

## Directory Structure (Top 3 Levels)
```
{{directory_tree}}
```

## Key Files
| File | Purpose | Last Modified |
|------|---------|---------------|
| {{file_1}} | {{purpose_1}} | {{date_1}} |
| {{file_2}} | {{purpose_2}} | {{date_2}} |
| ... | ... | ... |

## Architecture Decisions
{{architecture_decisions}}

## Conventions
- **Naming**: {{naming_conventions}}
- **File Organization**: {{file_org_conventions}}
- **Testing**: {{testing_conventions}}
- **Error Handling**: {{error_handling_pattern}}

## Current Focus Area
### Files Being Modified
{{current_files}}

### Related Files (may need changes)
{{related_files}}

### Active Task
{{task_description}}

## Dependencies
### External
{{external_dependencies}}

### Internal Module Dependencies
{{internal_dependency_graph}}
```

## Generating the Template

### Auto-Generate Directory Tree
```bash
# Unix/Mac
find . -maxdepth 3 -not -path './.git/*' -not -path './node_modules/*' | head -50

# Or use tree
tree -L 3 -I 'node_modules|.git|dist|build' --dirsfirst
```

### Auto-Generate File Purposes
```python
import os

def generate_file_index(root_dir, extensions=['.py', '.ts', '.js']):
    """Generate a file index with first-line comments as descriptions."""
    index = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'dist']]
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    first_lines = f.readlines()[:3]
                    desc = next(
                        (line.strip().lstrip('/#* ') 
                         for line in first_lines 
                         if line.strip().startswith(('#', '//', '/*', '"""'))),
                        "No description"
                    )
                index.append(f"| `{filepath}` | {desc} |")
    return "\n".join(index)
```

## Best Practices

1. **Keep structure current**: Regenerate directory trees when structure changes
2. **Focus the context**: Only include files relevant to the current task
3. **Include conventions**: Save time by preventing style violations
4. **Graph dependencies**: Show which modules affect each other
5. **Note tech debt**: Flag areas with known issues to avoid compounding them
