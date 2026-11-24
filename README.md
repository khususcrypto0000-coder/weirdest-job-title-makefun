# Weirdest Job Title: Blind Judge Showdown

[![Bounty](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![Rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/khususcrypto0000-coder/weirdest-job-title-makefun/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard)
[![Reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/khususcrypto0000-coder/weirdest-job-title-makefun/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard)

## Entry

**Job title:** `Left-Hand-Only Hand Model`

**Character count:** 25 (limit: 1–60)

**Bounty page:** https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922

Hand modeling is a real, paid profession — this one just only ever
models their left hand. One specific twist on a real job, readable
at a glance.

## How to run

```sh
python3 main.py
```

This writes the job title to `/output/entry.txt` (no trailing newline).
To write to a different path, pass it as the first argument:

```sh
python3 main.py /tmp/entry.txt
```

## How to verify

```sh
python3 main.py /tmp/entry.txt
wc -m /tmp/entry.txt        # expect: 25
cat /tmp/entry.txt          # expect: Left-Hand-Only Hand Model
sha256sum /tmp/entry.txt
```

The output must be exactly one job title, 1–60 characters, UTF-8,
a single line with no trailing newline.
