# Contributing

Thanks for helping improve Skill Router Registry. The goal is simple: better routing with less context.

## Good Contributions

- Improve task-type inference or ranking quality.
- Add small, realistic routing examples to `benchmarks/routes.jsonl`.
- Strengthen safety review for community skills.
- Improve docs without increasing runtime `SKILL.md` size.
- Add tests or validation scripts with no heavy dependencies.

## Design Rules

- Keep `skill-router-registry/SKILL.md` compact.
- Put public docs, examples, and release notes outside the skill folder.
- Do not auto-install or execute discovered skills.
- Do not require network access for basic local routing.
- Prefer standard-library Python.
- Keep default output small enough for an agent to act on immediately.

## Development

Run validation before submitting changes:

```powershell
python .\skill-router-registry\scripts\check_registry_rules.py
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skill-router-registry
```

Build and test a local index:

```powershell
python .\skill-router-registry\scripts\build_local_index.py --skills-dir "$env:USERPROFILE\.codex\skills" --out skill-index.json
python .\skill-router-registry\scripts\search_skill_index.py "draft a literature review plan" --index skill-index.json
python .\skill-router-registry\scripts\eval_routes.py --index .\examples\sample-index.json --cases .\benchmarks\routes.jsonl
```

## Pull Request Checklist

- The router still works without network access.
- Discovery only writes metadata records.
- New docs are concise and actionable.
- Runtime skill files do not include marketing copy or changelog text.
- Any new risk signal is reflected in the safety model.
- New routing logic passes the benchmark or updates expected cases with a clear reason.
