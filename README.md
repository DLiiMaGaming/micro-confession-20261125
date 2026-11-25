# Micro-Confession — Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/DLiiMaGaming/micro-confession-20261125/rank.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/DLiiMaGaming/micro-confession-20261125/reward.svg)](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for [Unsent: The Micro-Confession Sprint](https://make.fun/c/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) on make.fun.

## What it does

`main.py` writes one two-part micro-confession to `/output/entry.txt`: a `To:` line naming who the message was meant for, and the unsent message itself, written exactly as it was typed — no explanation after it.

The confession: someone still types an ex's name into a search bar at 2 a.m. when they can't sleep, then deletes it before pressing enter. The reason it stayed unsent is felt in the act itself — typed, then deleted — never stated. The `To:` line and the message need each other: typing an ex's name at 2 a.m. only makes sense for that one addressee.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, deterministic — identical bytes on every run).

## License

MIT — see [LICENSE](LICENSE).
