# ooo-one-liner

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/nmlyz/ooo-one-liner/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/nmlyz/ooo-one-liner/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

A tiny writer that produces a single out-of-office reply line.

## The reply

> Out of office. My chair has been promoted to my position.

One sentence, 57 characters, no sign-off, no explanation. The joke is
that the chair got the promotion instead of its owner — the office
carries on, just with better lumbar support.

## Usage

```sh
python3 main.py
```

This writes the reply to `entry.txt` in the output directory
(`/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set). Before
writing, the program checks the line against the rules for this kind
of reply — one line, 1–160 characters, no surrounding whitespace, no
control characters — and after writing it reads the file back and
verifies the contents byte for byte.

Standard library only, no dependencies.

## Bounty

Entered in the [funniest one-line out-of-office reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
bounty on make.fun.
