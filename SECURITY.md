# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability within this repository, please report it
responsibly. **Do not open a public issue.**

### How to Report

1. **Email**: Send details to the repository maintainer via GitHub's private messaging
2. **GitHub Security Advisories**: Use the "Report a vulnerability" button under the Security tab

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 1 week
- **Resolution**: Within 2 weeks for critical issues

## Scope

This security policy covers:

- **Repository content**: System prompts, templates, and configurations
- **Scripts and tools**: Python scripts, YAML configs, JSON schemas
- **Dependencies**: Any third-party libraries referenced

## Responsible Disclosure

We follow responsible disclosure practices:

1. We will acknowledge your report promptly
2. We will investigate and fix the issue
3. We will credit you (unless you prefer anonymity) once the fix is released

## AI Prompt Security

### Prompt Injection Awareness

Many prompts in this repository are designed for specific AI tools. When using them:

- **Never paste untrusted user input** directly into system prompts
- **Sanitize inputs** when building programmatic prompt chains
- **Test prompts in sandboxed environments** before production use
- **Review recursive chains** for potential amplification attacks

### Best Practices

1. **Validate outputs**: Always review AI-generated code before execution
2. **Limit permissions**: Run AI agents with minimal required permissions
3. **Monitor usage**: Track token consumption to detect prompt injection attempts
4. **Version control**: Keep your prompt configurations in version control

## Supported Versions

| Version | Supported |
|---------|-----------|
| main    | ✅ Active |
| All branches | ✅ Best effort |

Thank you for helping keep SuperRecursive and its users safe! 🛡️
