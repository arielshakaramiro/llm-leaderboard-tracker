# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 171 snapshots · WebDev: 103 snapshots · Vision: 115 snapshots_

### Text Arena

Leaderboard published 2026-10-28 · change vs 2026-10-20.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | 🆕 | `Gemini 4 Carbon (High)` | google | Proprietary | 1540 | 1531–1549 | 4,403 |
| 2 | ▼1 | `Gemini 4 Argon (High)` | google | Proprietary | 1529 | 1522–1535 | 11,889 |
| 3 | ▼1 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1516 | 1509–1522 | 11,415 |
| 4 | ▼1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1514 | 1508–1520 | 17,178 |
| 5 | ▼1 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1508 | 1503–1513 | 35,531 |
| 6 | ▼1 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1504 | 1500–1508 | 73,167 |
| 7 | = | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1502 | 1498–1505 | 84,512 |
| 8 | ▼2 | `Muse Wonder (Max)` | meta | Proprietary | 1499 | 1492–1506 | 7,749 |
| 9 | ▼1 | `Gemini 3.8 Flash (High)` | google | Proprietary | 1498 | 1494–1503 | 47,803 |
| 10 | ▼1 | `Claude Opus 4.6` | anthropic | Proprietary | 1496 | 1493–1499 | 89,324 |

Best open-weight model: `MiMo-V2.6-Pro` (xiaomi, MIT) at #12 with 1491.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-10-28 · change vs 2026-10-19.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Opus 5.5 (Max)` | anthropic | Proprietary | 1810 | 1797–1823 | 3,473 |
| 2 | = | `GPT-6 Astra (Max)` | openai | Proprietary | 1773 | 1764–1783 | 7,210 |
| 3 | = | `Claude Sonnet 5.5 (xHigh)` | anthropic | Proprietary | 1770 | 1758–1781 | 4,469 |
| 4 | 🆕 | `Gemini 4 Carbon (High)` | google | Proprietary | 1768 | 1753–1783 | 2,230 |
| 5 | ▼1 | `GPT-6.1 Sol (Max)` | openai | Proprietary | 1751 | 1739–1762 | 4,092 |
| 6 | ▼1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1746 | 1737–1754 | 8,614 |
| 7 | ▼1 | `Muse Wonder Full (Max)` | meta | Proprietary | 1725 | 1712–1739 | 2,248 |
| 8 | ▼1 | `Claude Sonnet 5.5 (High)` | anthropic | Proprietary | 1711 | 1701–1720 | 6,371 |
| 9 | 🆕 | `Kimi K3.1 Pro (Max)` | moonshot | Proprietary | 1695 | 1682–1708 | 2,671 |
| 10 | ▼2 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1690 | 1684–1697 | 19,641 |

Best open-weight model: `DeepSeek-V4.1-Flash-20261017 (Max)` (deepseek, MIT) at #16 with 1665.

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
