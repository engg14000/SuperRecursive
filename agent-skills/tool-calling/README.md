# 🔧 Tool Calling Schemas

> Standard JSON schemas for common tool categories. Use these to define tool interfaces for your AI agents.

## Schemas

| Schema | Description | File |
|--------|-------------|------|
| Web & APIs | HTTP requests, GraphQL, search, scraping | [web-apis.json](web-apis.json) |
| File System | Read, write, edit, search, move files | [file-system.json](file-system.json) |
| Code Execution | Shell commands, Python, testing, linting | [code-execution.json](code-execution.json) |
| Database | SQL, NoSQL, vector store operations | [database.json](database.json) |
| DevOps | Docker, Git, CI/CD, cloud deployment | [devops.json](devops.json) |

## How to Use

1. Pick the relevant schema(s) for your agent's needs
2. Include the tool definitions in your agent's system prompt or config
3. The agent will call these tools using the defined parameters
4. Your backend implements the actual tool execution

## Creating Custom Tools

Follow this format:
```json
{
  "name": "tool_name",
  "description": "Clear description of what the tool does",
  "parameters": {
    "type": "object",
    "properties": { ... },
    "required": [...]
  },
  "returns": { ... }
}
```
