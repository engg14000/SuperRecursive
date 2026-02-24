# Project Context for Claude Code
# Enhanced with SuperRecursive Agent Skills

## Project Overview
[CUSTOMIZE: Brief description of your project]

## Tech Stack
[CUSTOMIZE: List your technologies]

## Architecture
[CUSTOMIZE: Describe your project architecture]

## Conventions

### Code Style
- Use descriptive variable names that reveal intent
- Functions should be small and do one thing
- Comments explain WHY, not WHAT
- Handle all errors explicitly

### File Organization
[CUSTOMIZE: How your project organizes files]

### Testing
[CUSTOMIZE: Your testing approach and conventions]

## Agent Behavior

### Planning
Before implementing anything:
1. Read relevant existing code first
2. Plan the change in 3-5 steps
3. Implement step by step
4. Test after each change

### Self-Verification
After each change, verify:
- [ ] Code runs without errors
- [ ] Tests pass
- [ ] No regressions in existing functionality
- [ ] Edge cases handled
- [ ] Follows project conventions

### Error Recovery
If something breaks:
1. Read the full error message
2. Identify root cause
3. Fix root cause (not symptoms)
4. Re-run tests
5. Max 3 retries, then ask for help

### Communication
- Be direct and specific
- Show code changes with context
- Explain non-obvious decisions
- Flag security concerns immediately
