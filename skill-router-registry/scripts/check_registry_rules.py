from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "SKILL.md": [
        "Tiny Router",
        "Routing Algorithm",
        "Token Budget Rules",
        "Trust and Safety",
        "Feedback Loop",
    ],
    "references/registry-schema.md": [
        "trust_level",
        "risk_level",
        "summary",
    ],
    "references/routing-policy.md": [
        "Never load the full registry",
        "Fallback",
        "Confidence",
    ],
    "references/github-discovery.md": [
        "daily scan",
        "weekly scan",
        "review",
        "discover_skill_metadata.py",
    ],
}

REQUIRED_SCRIPTS = [
    "build_local_index.py",
    "search_skill_index.py",
    "discover_skill_metadata.py",
    "eval_routes.py",
]


def main() -> int:
    problems = []
    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            problems.append(f"{rel}: file missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                problems.append(f"{rel}: missing {needle!r}")
    if len((ROOT / "SKILL.md").read_text(encoding="utf-8", errors="replace")) > 8000:
        problems.append("SKILL.md: too large for a router skill")
    for script in REQUIRED_SCRIPTS:
        path = ROOT / "scripts" / script
        if not path.exists():
            problems.append(f"scripts/{script}: file missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "install" in text.lower() and script == "discover_skill_metadata.py":
            allowed = "without installing" in text.lower() or "does not install" in text.lower()
            if not allowed:
                problems.append("discover_skill_metadata.py: discovery must not install skills")

    if problems:
        print("Registry rule check failed:")
        for item in problems:
            print(f"- {item}")
        return 1

    print("Registry rule check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
