# Sample Routes

## Video

Input:

```text
make an explainer video with subtitles
```

Output:

```text
Route:
- Task type: video
- Best skill: seedance-2-pro-video
- Why: matched video, subtitle; trust=trusted; risk=review
- Confidence: high
- Next action: load only seedance-2-pro-video and execute the task
```

## Prompt Framing

Input:

```text
把我的大白话问题转成一个更清晰的提示词
```

Output:

```text
Route:
- Task type: planning
- Best skill: question-to-prompt-pack
- Why: matched prompt framing and task alignment; trust=trusted; risk=low
- Confidence: high
- Next action: load only question-to-prompt-pack and execute the task
```

## Research

Input:

```text
find recent papers about low-thrust trajectory optimization
```

Output:

```text
Route:
- Task type: research
- Best skill: literature-review
- Why: matched paper, literature, research; trust=trusted; risk=review
- Confidence: medium
- Next action: show the top candidates, recommend one, then load only the selected skill
- Alternatives: paper-lookup, nature-academic-search
```

## Ambiguous

Input:

```text
帮我优化一下
```

Output:

```text
Route:
- Task type: general
- Best skill: none
- Why: no indexed skill matched the task metadata
- Confidence: low
- Next action: use question-to-prompt-pack or ask one clarification question
```
