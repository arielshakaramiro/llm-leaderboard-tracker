# LLM Leaderboard Tracker

A self-updating record of how large language models rank against each other over time. Every week a GitHub Actions workflow pulls the official [LMArena](https://lmarena.ai) leaderboard dataset, appends any new snapshots to a CSV history, redraws the trend charts, and refreshes the tables below.

Two questions it answers at a glance:

- **Who is winning the frontier race?** The best-rated model from each of the top labs, tracked week by week.
- **How close is open-weight to proprietary?** The best open-weight model against the best proprietary model, and the size of the gap between them.

## Latest standings

<!-- LEADERBOARD_START -->
_Tracked history: Text: 168 snapshots · WebDev: 98 snapshots · Vision: 114 snapshots_

### Text Arena

Leaderboard published 2026-10-15 · change vs 2026-10-08.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | 🆕 | `Gemini 4 Argon (High)` | google | Proprietary | 1532 | 1524–1541 | 4,904 |
| 2 | 🆕 | `Claude Opus 5.5 (High)` | anthropic | Proprietary | 1516 | 1508–1523 | 8,300 |
| 3 | 🆕 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1512 | 1506–1518 | 14,590 |
| 4 | 🆕 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1508 | 1503–1512 | 32,495 |
| 5 | 🆕 | `Claude Opus 5 (High)` | anthropic | Proprietary | 1502 | 1499–1506 | 66,824 |
| 6 | 🆕 | `Claude Opus 4.6 (High)` | anthropic | Proprietary | 1502 | 1498–1505 | 81,394 |
| 7 | 🆕 | `Muse Wonder (Max)` | meta | Proprietary | 1501 | 1490–1512 | 3,247 |
| 8 | 🆕 | `Gemini 3.8 Flash (High)` | google | Proprietary | 1499 | 1494–1504 | 37,454 |
| 9 | 🆕 | `Claude Opus 4.6` | anthropic | Proprietary | 1498 | 1494–1501 | 86,071 |
| 10 | 🆕 | `Claude Fable 5 (High)` | anthropic | Proprietary | 1491 | 1487–1496 | 42,004 |

Best open-weight model: `mimo-v2.6-pro` (xiaomi, MIT) at #11 with 1491.

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-frontier-dark.png"><img alt="Text Arena frontier race chart" src="charts/text-frontier.png"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/text-open-vs-proprietary-dark.png"><img alt="Text Arena open-weight vs proprietary chart" src="charts/text-open-vs-proprietary.png"></picture>

### WebDev Arena

Leaderboard published 2026-10-18 · change vs 2026-10-08.

| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |
|--:|:-:|-------|-----|---------|-------:|:------:|------:|
| 1 | 🆕 | `Claude Opus 5.5 (Max)` | anthropic | Proprietary | 1806 | 1792–1820 | 2,870 |
| 2 | 🆕 | `GPT-6 Astra (Max)` | openai | Proprietary | 1776 | 1766–1786 | 6,172 |
| 3 | 🆕 | `Claude Sonnet 5.5 (xHigh)` | anthropic | Proprietary | 1768 | 1755–1781 | 3,342 |
| 4 | 🆕 | `GPT-6.1 Sol (Max)` | openai | Proprietary | 1754 | 1741–1767 | 3,021 |
| 5 | 🆕 | `Claude Fable 5.1 (Max)` | anthropic | Proprietary | 1742 | 1733–1751 | 7,684 |
| 6 | 🆕 | `Claude Sonnet 5.5 (High)` | anthropic | Proprietary | 1709 | 1699–1719 | 5,105 |
| 7 | 🆕 | `Claude Opus 5 (Max)` | anthropic | Proprietary | 1690 | 1683–1696 | 18,473 |
| 8 | 🆕 | `GPT-6 Sol (Max)` | openai | Proprietary | 1682 | 1672–1693 | 4,552 |
| 9 | 🆕 | `Gemini 4 Argon (High)` | google | Proprietary | 1678 | 1663–1694 | 1,773 |
| 10 | 🆕 | `Qwen3.8-Max (0902)` | alibaba | Proprietary | 1674 | 1667–1681 | 14,199 |

Best open-weight model: `DeepSeek-V4.1-Flash-20261017 (Max)` (deepseek, MIT) at #12 with 1670.

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
