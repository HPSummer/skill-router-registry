# Routing Policy

## Tiny Route

Default output:

```text
Route:
- Task type:
- Best skill:
- Why:
- Confidence:
- Next action:
```

## Token Rules

- Never load the full registry.
- Never load multiple full `SKILL.md` files by default.
- Search compact metadata first.
- Show at most 5 candidate summaries.
- Load references only after selecting a skill.
- If routing confidence is low, use question framing instead of reading more files.

## Confidence

- High: one obvious skill, proceed.
- Medium: show 2-3 candidates and recommend one.
- Low: ask one clarification question or fallback.

## Fallback

If no suitable skill is found:

1. Use `question-to-prompt-pack` for intent alignment if available.
2. Use normal Codex task framing.
3. Ask whether the user wants a new skill created.

## Multi-Skill Use

Use multiple skills only when:

- task clearly has independent phases
- user asks for orchestration
- each skill has a distinct responsibility

Keep loaded skill bodies minimal.
