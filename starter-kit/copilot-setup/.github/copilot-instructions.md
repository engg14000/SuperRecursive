# GitHub Copilot Custom Instructions
# Enhanced with SuperRecursive patterns

## Code Generation Preferences

When generating code:
- Match the existing code style exactly (indentation, naming, patterns)
- Include error handling for all failure modes
- Add type annotations/hints
- Write self-documenting code (clear names > comments)
- Follow SOLID principles

## Testing
- Generate tests alongside code when creating new functions
- Include edge cases: null, empty, boundary values
- Use the project's existing test framework and patterns

## Security
- Never hardcode credentials or secrets
- Sanitize user inputs
- Use parameterized queries for databases
- Follow OWASP best practices

## Communication
- Explain complex logic with inline comments
- Use TODO comments for known limitations
- Reference relevant documentation in comments
