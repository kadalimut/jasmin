# Sum up 21 November's world news in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/kadalimut/jasmin/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/kadalimut/jasmin/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Sum up the world's news of Saturday 21 November 2026 in one image.

The program writes one image to `/output/entry.png`. An AI judge
compares images two at a time and picks the one that best sums up
the day's world news.

This is an entry for the [make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121).

## The image

`entry.png` is 1024 by 1024 pixels, under 1 MiB. It names the day,
Saturday 21 November 2026, and shows six stories:

1. Russia hits Poland — missiles land in Poland, NATO on alert
2. Ukraine under fire — 110+ missiles, 400 drones, 8 killed
3. UK-EU landmark deal — Brexit reset, youth visas for 100,000
4. Trump-Xi-Putin summit — Shenzhen peace declaration
5. ICJ: Myanmar guilty — first state found guilty of genocide, 9-6
6. EU gives €1bn to Ukraine — drones and air defence

The image is drawn by `tools/draw_image.py` with Pillow, and
`main.ts` copies it to the output folder. No network is used at run time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Bounty

- Competition: https://make.fun/bounty/news-image-20261121
- Prize: $100, 50 places paid
- Deadline: Monday 23 November 2026, 00:00 UTC (07:00 WIB)

## License

MIT. See `LICENSE`.
