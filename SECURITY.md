# Security Policy

Skill Router Registry is intentionally conservative. It indexes skill metadata for routing; it does not prove a skill is safe.

## Supported Security Boundary

The supported workflow is:

```text
read SKILL.md metadata -> create compact registry record -> mark trust/risk -> require review before install or execution
```

The project does not support:

- auto-installing skills from GitHub
- executing discovered scripts
- reading secrets from community skills
- changing auth, shell, or Codex configuration without user approval
- treating registry presence as trust

## Reporting Issues

Open a GitHub issue for:

- a discovered skill being marked too trusted
- missing high-risk indicators
- unsafe install or execution behavior
- misleading docs around trust or review

Do not include secrets, tokens, or private repository contents in public issues.

## Risk Levels

- `low`: instruction-only skill with no obvious execution or credential risk.
- `review`: mentions shell commands, package installs, network access, downloads, auth, or file mutation.
- `high`: asks for credentials, tokens, private keys, passwords, or bypassing approvals.

When unsure, prefer the higher risk level.
