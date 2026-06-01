# Registry Schema

The registry is a compact routing index. It is not an install list and not a security guarantee.

## Record

```json
{
  "id": "question-to-prompt-pack",
  "name": "question-to-prompt-pack",
  "description": "Short trigger description from SKILL.md",
  "source": "local | github",
  "path_or_url": "local path or GitHub URL",
  "domains": ["planning", "writing"],
  "task_types": ["planning"],
  "trigger_phrases": [],
  "tools_required": [],
  "risk_level": "low | review | high",
  "trust_level": "trusted | review | unknown",
  "summary": "sub-500 character routing summary",
  "last_seen": "ISO timestamp"
}
```

## Trust Levels

- `trusted`: local installed skill, official source, or user-approved repo
- `review`: known community source or changed skill needing inspection
- `unknown`: discovered but not reviewed

## Risk Levels

- `low`: pure instruction skill, no risky operations
- `review`: mentions shell commands, installs, network, auth, or file mutations
- `high`: asks for secrets, credentials, API keys, auth/access tokens, private keys, passwords, or bypasses approvals

Do not mark normal context-budget terms such as "token budget" or "save tokens" as high risk unless they refer to authentication tokens.

## Routing Rule

Use registry records only for candidate selection. Load full `SKILL.md` only after selecting a candidate.
