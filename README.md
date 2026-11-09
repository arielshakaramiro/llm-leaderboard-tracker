# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 173 snapshots · WebDev: 105 snapshots · Vision: 117 snapshots_

### Text Arena

Leaderboard published 2026-11-08 · change vs 2026-10-28.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Gemini 4 Carbon (High)` | google | Proprietary | 1539 | 1529–1548 | 4,281 |
| 2 | = | `Gemini 4 Argon (High)` | google | Proprietary | 1530 | 1524–1535 | 18,850 |
| 3 | ▲1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1513 | 1507–1518 | 19,755 |
| 4 | ▼1 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1513 | 1507–1519 | 14,815 |
| 5 | = | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1506 | 1502–1511 | 35,712 |
| 6 | ▲2 | `Muse Wonder (Max)` | meta | Proprietary | 1504 | 1498–1511 | 11,483 |
| 7 | ▼1 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1502 | 1499–1506 | 73,730 |
| 8 | ▼1 | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1502 | 1498–1505 | 84,428 |
| 9 | = | `Gemini 3.8 Flash (High)` | google | Proprietary | 1500 | 1496–1505 | 59,624 |
| 10 | = | `Claude Opus 4.6` | anthropic | Proprietary | 1497 | 1494–1500 | 89,224 |

Best open-weight model: `MiMo-V2.6-Pro` (xiaomi, MIT) at #11 with 1492.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-11-08 · change vs 2026-10-28.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Opus 5.5 (Max)` | anthropic | Proprietary | 1818 | 1806–1830 | 4,034 |
| 2 | ▲1 | `Claude Sonnet 5.5 (xHigh)` | anthropic | Proprietary | 1774 | 1763–1784 | 5,536 |
| 3 | ▲1 | `Gemini 4 Carbon (High)` | google | Proprietary | 1768 | 1753–1783 | 2,130 |
| 4 | ▼2 | `GPT-6 Astra (Max)` | openai | Proprietary | 1767 | 1758–1776 | 8,161 |
| 5 | ▲1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1744 | 1736–1752 | 9,507 |
| 6 | ▼1 | `GPT-6.1 Sol (Max)` | openai | Proprietary | 1743 | 1733–1753 | 5,283 |
| 7 | = | `Muse Wonder Full (Max)` | meta | Proprietary | 1724 | 1709–1738 | 2,080 |
| 8 | = | `Claude Sonnet 5.5 (High)` | anthropic | Proprietary | 1713 | 1705–1722 | 7,582 |
| 9 | ▲1 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1691 | 1685–1697 | 19,583 |
| 10 | ▼1 | `Kimi K3.1 Pro (Max)` | moonshot | Open (Kimi K3.1 Pro License) | 1687 | 1677–1697 | 4,651 |

Best open-weight model: `Kimi K3.1 Pro (Max)` (moonshot, Kimi K3.1 Pro License) at #10 with 1687.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-frontier-dark.png"><img alt="WebDev Arena frontier race chart" src="charts/webdev-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/webdev-open-vs-proprietary-dark.png"><img alt="WebDev Arena open-weight vs proprietary chart" src="charts/webdev-open-vs-proprietary.png"></picture>

### Vision Arena

Leaderboard published 2026-11-08 · change vs 2026-10-19.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | = | `Claude Fable 5 (High)` | anthropic | Proprietary | 1326 | 1319–1332 | 15,527 |
| 2 | = | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1324 | 1314–1334 | 4,829 |
| 3 | ▲1 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1322 | 1313–1330 | 6,330 |
| 4 | ▲1 | `Claude Opus 4.7` | anthropic | Proprietary | 1318 | 1312–1325 | 23,826 |
| 5 | ▼2 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1317 | 1311–1324 | 19,342 |
| 6 | ▲1 | `Gemini 3.8 Flash (High)` | google | Proprietary | 1317 | 1309–1325 | 7,682 |
| 7 | ▼1 | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1316 | 1309–1322 | 22,109 |
| 8 | ▲1 | `Claude Opus 4.7 (High)` | anthropic | Proprietary | 1314 | 1307–1320 | 22,590 |
| 9 | ▼1 | `Gemini 3.7 Flash (High)` | google | Proprietary | 1313 | 1305–1322 | 6,839 |
| 10 | = | `Qwen3.8-Max` | alibaba | Proprietary | 1312 | 1305–1320 | 9,839 |

Best open-weight model: `GLM-5.3-Flash` (zai, MIT) at #23 with 1295.

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
