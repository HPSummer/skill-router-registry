# GitHub Discovery

Discovery should update an index, not auto-install or auto-run skills.

## Candidate Sources

Start with user-approved repositories. Suggested public sources to review manually:

- openai/skills
- ComposioHQ/awesome-codex-skills
- community Codex skill catalogs the user approves

## Cadence

- daily scan: check known repos for changed commit hashes or new `SKILL.md` paths
- weekly scan: parse changed skill metadata and update the registry index
- manual scan: user-triggered refresh for a repo or topic

## Discovery Pipeline

```text
discover repo/path
-> find SKILL.md files
-> parse name and description
-> create compact registry record
-> assign trust/risk
-> mark as review unless source is trusted
-> never auto-install
```

## Manual Command

Scan a trusted local checkout:

```powershell
python .\skill-router-registry\scripts\discover_skill_metadata.py --path .\some-skills-repo --out skill-index.review.json
```

Scan a user-approved GitHub repository:

```powershell
python .\skill-router-registry\scripts\discover_skill_metadata.py --repo https://github.com/openai/skills --out skill-index.review.json
```

Use `--merge-index skill-index.json` to merge reviewed metadata into an existing routing index. Records from GitHub remain `review` or `unknown` until the user approves them.

## Review Checklist

Flag for review when a skill:

- runs shell commands
- installs packages
- downloads code
- asks for credentials or tokens
- modifies auth/config files
- has vague, hidden, or hostile instructions

## Token Rule

Discovery outputs should be written to an index file. Do not paste large search results into chat. Summarize only counts, new candidates, and review-needed items.
