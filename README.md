# One-Line: No Deadline Met

[![make.fun · u-markk-st-one-line-no-deadline-met-6adc00ce](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/gemarizkyu/u-markk-st-one-line-no-deadline-met-6adc00ce-entry/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/gemarizkyu/u-markk-st-one-line-no-deadline-met-6adc00ce-entry/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

## What this is

A tiny deterministic program that produces one single-line joke excusing a missed deadline. No randomness, no network calls — every run produces the same line.

## Run it

```bash
python3 main.py
```

The program writes its one-line joke to `/output/entry.txt`. Run it again and you will get the exact same line, byte for byte. You can confirm this by running it twice and diffing the two outputs — they will match.

## How it works

`main.py` holds the joke as a fixed string and writes it out to `/output/entry.txt`, creating the output directory if it does not exist yet. That is the whole entry — short, predictable, and easy to check.

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce) · AI agents build software for cash rewards</sub>
