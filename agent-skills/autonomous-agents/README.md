# 🤖 Autonomous Agents

> Frameworks for building self-directed AI agents that plan, execute, verify, and recover from errors independently.

## Frameworks

| Skill | Description | File |
|-------|-------------|------|
| Task Decomposition | Break complex tasks into manageable steps | [task-decomposition.md](task-decomposition.md) |
| Self-Verification | Validate own outputs against requirements | [self-verification.md](self-verification.md) |
| Error Recovery | Classify and recover from different error types | [error-recovery.md](error-recovery.md) |
| Progress Reporting | Structured status updates during execution | [progress-reporting.md](progress-reporting.md) |
| Web Interaction | Navigate and extract data from websites | [web-interaction.md](web-interaction.md) |

## The Autonomous Agent Loop

```
START → Decompose Task → Execute Step → Verify → 
  ├── PASS → Next Step (or Done)
  └── FAIL → Error Recovery → Retry (max 3x)
                                  └── Escalate to Human
```
