# Sunday 22 November 2026 — The World in One Picture

Entry for the [make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122).

## What it is

`main.py` copies the bundled newspaper front page (`assets/entry.png`,
1024×1024 PNG, 556 KB) to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`). No network, no randomness — every run writes identical bytes.

## The day's news it sums up

Researched from live news coverage of Sunday 22 November 2026:

1. **COP31 COLLAPSES — NO CLIMATE DEAL** — The UN climate summit in
   Antalya, Turkey ended with no agreement, two days past its deadline,
   after the EU and others rejected a final draft that did not mention
   fossil fuels.
2. **IRAN STRIKES BAHRAIN** — Iranian projectiles hit a civilian
   industrial site in Sitra, Bahrain, injuring two people; Gulf states
   condemned the attack, amid wider strikes on tankers near the Strait
   of Hormuz.
3. **KYIV FLAT HIT — 14 MISSING** — A Russian drone struck a
   five-storey apartment building in Dymer, near Kyiv; two people were
   killed and at least 14 were missing under the rubble. A Russian
   missile also hit Kryvyi Rih, killing two, including a 7-year-old boy.
4. **MEXICO CAPTURES EL CHAPO ISIDRO** — Mexican special forces captured
   cartel boss Fausto Isidro Meza Flores ("El Chapo Isidro") in Sinaloa;
   11 people were killed in the raid, including four soldiers.
5. **ICJ: MYANMAR GUILTY OF ROHINGYA GENOCIDE** — The International
   Court of Justice ruled Myanmar committed genocide against the
   Rohingya in 2017 — the first time the court has found a state
   responsible for genocide.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see `LICENSE`.
