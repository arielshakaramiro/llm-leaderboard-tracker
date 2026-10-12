# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 166 snapshots · WebDev: 95 snapshots · Vision: 114 snapshots_

### Text Arena

Leaderboard published 2026-10-08 · change vs 2026-09-30.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `gemini-4-argon-high` | google | Proprietary | 1534 | 1525–1543 | 4,892 |
| 2 | = | `claude-opus-5.5-high` | anthropic | Proprietary | 1515 | 1507–1523 | 6,272 |
| 3 | = | `claude-fable-5.1-max` | anthropic | Proprietary | 1510 | 1504–1516 | 13,063 |
| 4 | = | `claude-opus-5-max` | anthropic | Proprietary | 1507 | 1502–1512 | 30,569 |
| 5 | = | `claude-opus-4-6-high` | anthropic | Proprietary | 1503 | 1500–1506 | 79,415 |
| 6 | = | `claude-opus-5-high` | anthropic | Proprietary | 1503 | 1499–1506 | 62,934 |
| 7 | ▲1 | `gemini-3.8-flash-high` | google | Proprietary | 1499 | 1494–1504 | 31,437 |
| 8 | ▼1 | `claude-opus-4-6` | anthropic | Proprietary | 1498 | 1495–1501 | 84,095 |
| 9 | ▲1 | `mimo-v2.6-pro` | xiaomi | Open (MIT) | 1492 | 1482–1501 | 4,069 |
| 10 | ▼1 | `claude-fable-5-high` | anthropic | Proprietary | 1491 | 1487–1496 | 40,026 |

Best open-weight model: `mimo-v2.6-pro` (xiaomi, MIT) at #9 with 1492.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-10-08 · change vs 2026-10-01.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `claude-opus-5.5-max` | anthropic | Proprietary | 1813 | 1798–1828 | 2,294 |
| 2 | = | `gpt-6-astra-max` | openai | Proprietary | 1786 | 1775–1797 | 5,189 |
| 3 | = | `claude-sonnet-5.5-xhigh` | anthropic | Proprietary | 1774 | 1759–1789 | 2,323 |
| 4 | = | `gpt-6.1-sol-max` | openai | Proprietary | 1755 | 1740–1770 | 2,102 |
| 5 | = | `claude-fable-5.1-max` | anthropic | Proprietary | 1744 | 1734–1753 | 6,663 |
| 6 | = | `claude-sonnet-5.5-high` | anthropic | Proprietary | 1715 | 1704–1726 | 3,984 |
| 7 | = | `claude-opus-5-max` | anthropic | Proprietary | 1691 | 1685–1698 | 17,320 |
| 8 | = | `gpt-6-sol-max` | openai | Proprietary | 1688 | 1676–1700 | 3,407 |
| 9 | = | `gemini-4-argon-high` | google | Proprietary | 1678 | 1662–1693 | 1,771 |
| 10 | ▲1 | `qwen3.8-max-0902` | alibaba | Proprietary | 1674 | 1666–1681 | 11,182 |

Best open-weight model: `kimi-k3-max` (moonshot, Kimi K3 license) at #14 with 1654.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-frontier-dark.png"><img alt="WebDev Arena frontier race chart" src="charts/webdev-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-open-vs-proprietary-dark.png"><img alt="WebDev Arena open-weight vs proprietary chart" src="charts/webdev-open-vs-proprietary.png"></picture>

### Vision Arena

Leaderboard published 2026-10-09 · change vs 2026-10-02.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `claude-fable-5-high` | anthropic | Proprietary | 1324 | 1317–1331 | 14,175 |
| 2 | 🆕 | `claude-opus-5.5-high` | anthropic | Proprietary | 1320 | 1308–1333 | 2,508 |
| 3 | ▼1 | `claude-opus-5-high` | anthropic | Proprietary | 1319 | 1312–1326 | 16,665 |
| 4 | ▼1 | `claude-fable-5.1-max` | anthropic | Proprietary | 1318 | 1309–1328 | 4,648 |
| 5 | ▼1 | `claude-opus-4-7` | anthropic | Proprietary | 1316 | 1310–1323 | 23,165 |
| 6 | ▲1 | `gemini-3.7-flash-high` | google | Proprietary | 1316 | 1306–1326 | 4,524 |
| 7 | ▼1 | `claude-opus-4-6-high` | anthropic | Proprietary | 1316 | 1309–1322 | 22,304 |
| 8 | ▼3 | `gemini-3.8-flash-high` | google | Proprietary | 1314 | 1304–1325 | 3,792 |
| 9 | ▼1 | `qwen3.8-max` | alibaba | Proprietary | 1314 | 1306–1321 | 10,017 |
| 10 | ▼1 | `claude-opus-4-6` | anthropic | Proprietary | 1313 | 1307–1319 | 26,853 |

Best open-weight model: `glm-5.3-flash` (zai, MIT) at #23 with 1296.

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
