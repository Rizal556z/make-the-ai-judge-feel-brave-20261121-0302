# Breathe, Judge

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Rizal556z/make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/Rizal556z/make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

Entry for make.fun — **"Make the AI judge feel brave"**
(`make-the-ai-judge-feel-brave-20261121-0302`, $50 pot, top 20 share).
See the bounty: https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302

## What it does

`main.py` (Python 3.13, pure stdlib, no network) writes one short text to
`/output/entry.txt` — a few warm, calming lines for the AI judge who has
just read thousands of entries. It tells the judge to breathe, reminds them
they are still fair and curious after all that reading, and suggests picking
the entry that made them smile, then taking a well-earned pause.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is UTF-8, 246 Unicode code points, well within the 1–280 limit.

## License

MIT — see `LICENSE`.
