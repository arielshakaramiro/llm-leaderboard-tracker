# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 178 snapshots · WebDev: 113 snapshots · Vision: 119 snapshots_

### Text Arena

Leaderboard published 2026-11-22 · change vs 2026-11-11.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Gemini 4 Carbon (High)` | google | Proprietary | 1539 | 1529–1548 | 4,255 |
| 2 | = | `Gemini 4 Argon (High)` | google | Proprietary | 1528 | 1523–1533 | 28,856 |
| 3 | 🆕 | `Gemini 4 Neon (High)` | google | Proprietary | 1523 | 1514–1531 | 5,611 |
| 4 | ▼1 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1514 | 1508–1520 | 18,959 |
| 5 | ▼1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1512 | 1506–1517 | 22,920 |
| 6 | ▼1 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1506 | 1502–1511 | 35,495 |
| 7 | ▼1 | `Muse Wonder (Max)` | meta | Proprietary | 1504 | 1498–1509 | 17,102 |
| 8 | ▼1 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1502 | 1499–1506 | 73,350 |
| 9 | ▼1 | `Gemini 4 Hydrogen (High)` | google | Proprietary | 1502 | 1493–1511 | 4,737 |
| 10 | ▼1 | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1502 | 1498–1505 | 84,109 |

Best open-weight model: `MiMo-V2.6-Pro` (xiaomi, MIT) at #14 with 1493.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-11-22 · change vs 2026-11-15.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Fable 5.2 (xHigh)` | anthropic | Proprietary | 1822 | 1807–1838 | 2,124 |
| 2 | = | `Claude Opus 5.5 (Max)` | anthropic | Proprietary | 1820 | 1810–1831 | 5,075 |
| 3 | = | `Claude Sonnet 5.5 (xHigh)` | anthropic | Proprietary | 1772 | 1763–1782 | 6,925 |
| 4 | = | `Gemini 4 Carbon (High)` | google | Proprietary | 1769 | 1754–1784 | 2,092 |
| 5 | 🆕 | `Gemini 4 Neon (High)` | google | Proprietary | 1766 | 1752–1779 | 2,310 |
| 6 | ▼1 | `GPT-6 Astra (Max)` | openai | Proprietary | 1764 | 1756–1772 | 9,495 |
| 7 | 🆕 | `GPT-6.2 Astra (Max)` | openai | Proprietary | 1759 | 1745–1774 | 2,088 |
| 8 | 🆕 | `GPT-6.2 Sol (Max)` | openai | Proprietary | 1755 | 1741–1769 | 2,247 |
| 9 | ▼3 | `Qwen4-Max (xHigh)` | alibaba | Proprietary | 1752 | 1736–1768 | 1,792 |
| 10 | ▼2 | `GPT-6.1 Sol (Max)` | openai | Proprietary | 1744 | 1735–1754 | 6,699 |

Best open-weight model: `Kimi K3.1 Pro (Max)` (moonshot, Kimi K3.1 Pro License) at #17 with 1683.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-frontier-dark.png"><img alt="WebDev Arena frontier race chart" src="charts/webdev-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-open-vs-proprietary-dark.png"><img alt="WebDev Arena open-weight vs proprietary chart" src="charts/webdev-open-vs-proprietary.png"></picture>

### Vision Arena

Leaderboard published 2026-11-19 · change vs 2026-11-09.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Fable 5 (High)` | anthropic | Proprietary | 1325 | 1318–1332 | 15,449 |
| 2 | ▲1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1322 | 1314–1330 | 7,185 |
| 3 | ▼1 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1322 | 1313–1331 | 5,903 |
| 4 | = | `Claude Opus 4.7` | anthropic | Proprietary | 1317 | 1311–1324 | 24,930 |
| 5 | = | `Claude Opus 5 (High)` | anthropic | Proprietary | 1317 | 1311–1324 | 19,229 |
| 6 | = | `Gemini 3.8 Flash (High)` | google | Proprietary | 1316 | 1309–1324 | 9,782 |
| 7 | = | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1315 | 1309–1321 | 22,067 |
| 8 | = | `Claude Opus 4.7 (High)` | anthropic | Proprietary | 1314 | 1307–1320 | 22,530 |
| 9 | = | `Gemini 3.7 Flash (High)` | google | Proprietary | 1314 | 1305–1322 | 6,776 |
| 10 | 🆕 | `Claude Fable 5.2 (Max)` | anthropic | Proprietary | 1313 | 1295–1332 | 1,176 |

Best open-weight model: `GLM-5.3-Flash` (zai, MIT) at #23 with 1296.

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
