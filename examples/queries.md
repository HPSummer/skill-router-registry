# Example Queries

Use these to sanity-check routing behavior. The executable benchmark lives in `benchmarks/routes.jsonl`.

| Query | Expected task type | Expected route style |
|---|---:|---|
| make an explainer video with subtitles | video | video generation skill |
| turn my rough question into a better prompt | planning | question framing skill |
| review this MATLAB optimal control code | coding | MATLAB review/testing skill |
| build a React dashboard for my research planner | coding | frontend app builder |
| find recent papers about low-thrust trajectory optimization | research | literature or paper lookup skill |
| polish this manuscript for Nature style | writing | Nature polishing/writing skill |
| scan this repo for security issues | coding | security scan skill |
| make a weekly reminder to check new GitHub skills | automation | automation workflow |
| extract tables from this PDF | data | PDF/document skill |
| create an Obsidian literature note from this paper | research | research or citation skill |

## Low-Confidence Cases

These should not force a skill too early:

| Query | Better behavior |
|---|---|
| help me with this | ask one clarification question |
| make it better | ask what artifact/task is being improved |
| deal with the file | ask file type and desired outcome |
| optimize my project | ask whether this means speed, quality, UX, or research direction |
