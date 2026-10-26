# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 170 snapshots · WebDev: 101 snapshots · Vision: 115 snapshots_

### Text Arena

Leaderboard published 2026-10-22 · change vs 2026-10-15.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Gemini 4 Argon (High)` | google | Proprietary | 1526 | 1519–1532 | 10,083 |
| 2 | = | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1516 | 1509–1523 | 10,322 |
| 3 | = | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1512 | 1507–1518 | 16,343 |
| 4 | = | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1508 | 1504–1513 | 34,526 |
| 5 | = | `Claude Opus 5 (High)` | anthropic | Proprietary | 1503 | 1500–1507 | 71,020 |
| 6 | = | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1502 | 1498–1505 | 83,454 |
| 7 | = | `Muse Wonder (Max)` | meta | Proprietary | 1500 | 1492–1509 | 6,001 |
| 8 | = | `Gemini 3.8 Flash (High)` | google | Proprietary | 1498 | 1494–1503 | 43,997 |
| 9 | = | `Claude Opus 4.6` | anthropic | Proprietary | 1497 | 1494–1500 | 88,206 |
| 10 | ▲2 | `Muse Spark 1.3 (Max)` | meta | Proprietary | 1491 | 1486–1496 | 20,506 |

Best open-weight model: `MiMo-V2.6-Pro` (xiaomi, MIT) at #11 with 1491.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-10-23 · change vs 2026-10-16.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Opus 5.5 (Max)` | anthropic | Proprietary | 1807 | 1794–1820 | 3,140 |
| 2 | = | `GPT-6 Astra (Max)` | openai | Proprietary | 1774 | 1764–1784 | 6,579 |
| 3 | = | `Claude Sonnet 5.5 (xHigh)` | anthropic | Proprietary | 1769 | 1757–1781 | 3,822 |
| 4 | = | `GPT-6.1 Sol (Max)` | openai | Proprietary | 1749 | 1737–1762 | 3,469 |
| 5 | = | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1742 | 1734–1751 | 8,098 |
| 6 | 🆕 | `Muse Wonder Full (Max)` | meta | Proprietary | 1726 | 1712–1740 | 2,253 |
| 7 | ▼1 | `Claude Sonnet 5.5 (High)` | anthropic | Proprietary | 1709 | 1700–1719 | 5,632 |
| 8 | 🆕 | `Kimi K3.1 Pro (Max)` | moonshot | Proprietary | 1692 | 1678–1705 | 2,451 |
| 9 | ▼2 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1691 | 1684–1697 | 18,995 |
| 10 | ▼2 | `GPT-6 Sol (Max)` | openai | Proprietary | 1681 | 1671–1691 | 5,008 |

Best open-weight model: `DeepSeek-V4.1-Flash-20261017 (Max)` (deepseek, MIT) at #14 with 1665.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-frontier-dark.png"><img alt="WebDev Arena frontier race chart" src="charts/webdev-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-open-vs-proprietary-dark.png"><img alt="WebDev Arena open-weight vs proprietary chart" src="charts/webdev-open-vs-proprietary.png"></picture>

### Vision Arena

Leaderboard published 2026-10-19 · change vs 2026-10-09.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | 🆕 | `Claude Fable 5 (High)` | anthropic | Proprietary | 1325 | 1318–1332 | 14,714 |
| 2 | 🆕 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1321 | 1309–1332 | 3,035 |
| 3 | 🆕 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1320 | 1313–1326 | 17,743 |
| 4 | 🆕 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1320 | 1310–1329 | 5,026 |
| 5 | 🆕 | `Claude Opus 4.7` | anthropic | Proprietary | 1317 | 1310–1324 | 23,139 |
| 6 | 🆕 | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1316 | 1309–1322 | 22,286 |
| 7 | 🆕 | `Gemini 3.8 Flash (High)` | google | Proprietary | 1315 | 1306–1325 | 4,645 |
| 8 | 🆕 | `Gemini 3.7 Flash (High)` | google | Proprietary | 1314 | 1305–1323 | 5,369 |
| 9 | 🆕 | `Claude Opus 4.7 (High)` | anthropic | Proprietary | 1313 | 1307–1320 | 22,731 |
| 10 | 🆕 | `Qwen3.8-Max` | alibaba | Proprietary | 1313 | 1306–1320 | 9,957 |

Best open-weight model: `GLM-5.3-Flash` (zai, MIT) at #24 with 1294.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/vision-frontier-dark.png"><img alt="Vision Arena frontier race chart" src="charts/vision-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/vision-open-vs-proprietary-dark.png"><img alt="Vision Arena open-weight vs proprietary chart" src="charts/vision-open-vs-proprietary.png"></picture>

<!-- LEADERBOARD_END -->

## How it works

```
LMArena dataset (Hugging Face) ──► normalize + filter ──► data/<arena>.csv ──► charts/*.png + README
```

1. **Fetch.** Downloads the `full` split of [`lmarena-ai/leaderboard-dataset`](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset) for each tracked arena (Text, WebDev, Vision).
2. **Normalize.** Keeps the `overall` category and the top 150 models of each snapshot, and maps the slightly different column names used by different arenas onto one schema.
3. **Merge.** Adds only snapshots that are not in the CSV yet. Because the whole history is checked every run, a missed week fills itself in.
4. **Render.** Draws two charts per arena, each in a light and a dark version (GitHub shows the one matching your theme).
5. **Publish.** Rewrites the section above. If LMArena published nothing new, no file changes and no commit is made.

## Data

| File | Contents |
|------|----------|
| `data/text.csv`, `data/webdev.csv`, `data/vision.csv` | `date, model, organization, license, rating, rating_lower, rating_upper, votes, rank` |
| `charts/<arena>-frontier.png` | Best rating per lab over the last 12 months |
| `charts/<arena>-open-vs-proprietary.png` | Best open-weight vs best proprietary model |

**Open-weight** means any license other than `Proprietary` in the dataset (Apache 2.0, MIT, Llama, Modified MIT, and similar). **Rating** is LMArena's Elo-style score from human preference votes, with a 95% confidence interval. Models whose intervals overlap are statistically tied.

The CSVs are plain files, so you can load them straight into pandas:

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/arielshakaramiro/llm-leaderboard-tracker/main/data/text.csv")
```

### Why not the Hugging Face Open LLM Leaderboard?

It was retired by Hugging Face in 2025 and its results are archived, so there is no new data to track. LMArena is the actively maintained leaderboard with an official, versioned dataset.

## Run it yourself

```bash
pip install -r requirements.txt
python tracker.py
```

Requires Python 3.10+. No API keys needed, the dataset is public.

## Customize

Edit `config.json`:

- `arenas`: which arenas to track. Other available ones include `search`, `document`, `text_to_image`, `image_edit`, `text_to_video`, and `agent`.
- `history_start`: how far back the CSV history goes.
- `chart_days`: the time window shown in the charts.
- `frontier_orgs`: how many labs appear in the frontier chart.
- `org_colors`: a fixed color slot (1–8) per lab, so a lab keeps the same color across every chart and every week.

## License

Code: MIT. Leaderboard data: © LMArena, distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) via the [Arena leaderboard dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset).
