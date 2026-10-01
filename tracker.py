#!/usr/bin/env python3
"""
LLM Leaderboard Tracker
-----------------------
Pulls the official LMArena leaderboard dataset from Hugging Face, keeps a
weekly-growing CSV history per arena, renders trend charts, and rewrites the
"latest" section of README.md.

  data/<arena>.csv                  overall-category history (top N per snapshot)
  charts/<arena>-frontier[-dark].png       best rating per lab over time
  charts/<arena>-open-vs-proprietary[-dark].png   best open-weight vs best proprietary

Every run merges the dataset's full history into the CSVs, so a missed week
fills itself in. If nothing new was published, no file changes and the
workflow makes no commit.

Usage:
  python tracker.py                    # fetch + charts + README
  python tracker.py --source-dir DIR   # read <arena>.parquet files from DIR (offline/testing)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import timedelta
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
DATA_DIR = ROOT / "data"
CHART_DIR = ROOT / "charts"
README = ROOT / "README.md"
README_START = "<!-- LEADERBOARD_START -->"
README_END = "<!-- LEADERBOARD_END -->"

HF = "https://huggingface.co"
USER_AGENT = "llm-leaderboard-tracker/1.0 (+https://github.com/arielshakaramiro/llm-leaderboard-tracker)"

COLUMNS = ["date", "model", "organization", "license", "rating",
           "rating_lower", "rating_upper", "votes", "rank"]
# Different arenas name the same fields differently.
RENAME = {
    "leaderboard_publish_date": "date",
    "model_name": "model",
    "score": "rating",
    "score_ci_lower": "rating_lower",
    "score_ci_upper": "rating_upper",
    "observation_count": "votes",
    "vote_count": "votes",
}


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #
def http_get(url: str, timeout: int = 120, retries: int = 3) -> bytes:
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500 and e.code != 429:
                raise RuntimeError(f"HTTP {e.code} for {url}") from e
            last = e
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
        time.sleep(5 * attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last}")


def parquet_url(arena: str, split: str = "full") -> str:
    """Find the parquet file for an arena split via the Hub tree API."""
    api = f"{HF}/api/datasets/{CONFIG['dataset']}/tree/main/{arena}"
    files = [f["path"] for f in json.loads(http_get(api, timeout=60))
             if f.get("type") == "file" and f["path"].endswith(".parquet")]
    matches = sorted(p for p in files if Path(p).name.startswith(f"{split}-"))
    if not matches:
        raise RuntimeError(f"No '{split}' parquet found for arena '{arena}': {files}")
    return f"{HF}/datasets/{CONFIG['dataset']}/resolve/main/{matches[0]}"


def load_arena(arena: str, source_dir: Path | None) -> pd.DataFrame:
    if source_dir:
        path = source_dir / f"{arena}.parquet"
    else:
        url = parquet_url(arena)
        print(f"  downloading {url}")
        path = DATA_DIR / f".{arena}.parquet"
        path.write_bytes(http_get(url, timeout=300))
    try:
        import pyarrow.parquet as pq
        has_category = "category" in pq.read_schema(path).names
        # filter while reading: the text arena's full history is tens of MB
        filters = [("category", "==", CONFIG["category"])] if has_category else None
        df = pd.read_parquet(path, filters=filters)
    finally:
        if not source_dir:
            path.unlink(missing_ok=True)
    return normalize(df)


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=RENAME)
    missing = [c for c in COLUMNS if c not in df.columns and c != "votes"]
    if missing:
        raise RuntimeError(f"Dataset schema changed, missing columns: {missing}")
    if "votes" not in df.columns:
        df["votes"] = pd.NA
    if "category" in df.columns:
        df = df[df["category"] == CONFIG["category"]]
    df = df[df["date"] >= CONFIG["history_start"]]
    df = df[df["rank"] <= CONFIG["keep_top_n"]]
    df = df[COLUMNS].dropna(subset=["date", "model", "rating", "rank"]).copy()
    df["date"] = df["date"].astype(str).str[:10]
    df["license"] = df["license"].fillna("Unknown")
    df["organization"] = df["organization"].fillna("unknown")
    df["rating"] = df["rating"].round(1)
    df["rating_lower"] = df["rating_lower"].round(1)
    df["rating_upper"] = df["rating_upper"].round(1)
    df["votes"] = pd.to_numeric(df["votes"], errors="coerce").round().astype("Int64")
    df["rank"] = df["rank"].round().astype(int)
    return df


def merge_history(arena: str, fresh: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    csv_path = DATA_DIR / f"{arena}.csv"
    if csv_path.exists():
        old = pd.read_csv(csv_path, dtype={"date": str})
        old["votes"] = old["votes"].astype("Int64")
        known = set(old["date"])
        new_dates = sorted(set(fresh["date"]) - known)
        merged = pd.concat([old, fresh[fresh["date"].isin(new_dates)]], ignore_index=True)
    else:
        new_dates = sorted(set(fresh["date"]))
        merged = fresh
    merged = merged.sort_values(["date", "rank", "model"]).reset_index(drop=True)
    if new_dates:
        merged.to_csv(csv_path, index=False)
    return merged, len(new_dates)


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #
def is_open(license_name: str) -> bool:
    return str(license_name).strip().lower() != "proprietary"


def latest_and_previous(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame | None, str, str | None]:
    dates = sorted(df["date"].unique())
    latest = dates[-1]
    cutoff = (pd.Timestamp(latest) - timedelta(days=7)).strftime("%Y-%m-%d")
    earlier = [d for d in dates if d <= cutoff]
    prev = earlier[-1] if earlier else None
    return (df[df["date"] == latest], df[df["date"] == prev] if prev else None, latest, prev)


def frontier(df: pd.DataFrame, orgs: list[str]) -> pd.DataFrame:
    sub = df[df["organization"].isin(orgs)]
    return sub.groupby(["date", "organization"])["rating"].max().unstack("organization")


def open_vs_proprietary(df: pd.DataFrame) -> pd.DataFrame:
    tmp = df.assign(kind=df["license"].map(lambda x: "Open-weight" if is_open(x) else "Proprietary"))
    return tmp.groupby(["date", "kind"])["rating"].max().unstack("kind")


# --------------------------------------------------------------------------- #
# Charts
# --------------------------------------------------------------------------- #
THEMES = {
    "light": {
        "surface": "#fcfcfb", "text": "#0b0b0b", "text2": "#52514e", "muted": "#898781",
        "grid": "#e1e0d9", "axis": "#c3c2b7", "band": "#f0efec",
        "series": ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
                   "#e87ba4", "#008300", "#4a3aa7", "#e34948"],
    },
    "dark": {
        "surface": "#1a1a19", "text": "#ffffff", "text2": "#c3c2b7", "muted": "#898781",
        "grid": "#2c2c2a", "axis": "#383835", "band": "#2c2c2a",
        "series": ["#3987e5", "#d95926", "#199e70", "#c98500",
                   "#d55181", "#008300", "#9085e9", "#e66767"],
    },
}


def org_slots(orgs: list[str]) -> dict[str, int]:
    """Stable color slot per lab: configured labs keep their slot; others take
    the free slots in alphabetical order so the mapping never depends on rank."""
    fixed = {o: s - 1 for o, s in CONFIG["org_colors"].items()}
    slots = {o: fixed[o] for o in orgs if o in fixed}
    free = [s for s in range(8) if s not in slots.values()]
    for o in sorted(o for o in orgs if o not in fixed):
        slots[o] = free.pop(0) if free else 7
    return slots


def spread_labels(ys: list[float], min_gap: float) -> list[float]:
    """Nudge end-of-line labels apart so they never overlap."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    placed = [0.0] * len(ys)
    last = None
    for i in order:
        y = ys[i] if last is None else max(ys[i], last + min_gap)
        placed[i] = last = y
    # shift the whole stack down if it drifted above the highest real value
    overshoot = placed[order[-1]] - max(ys)
    if overshoot > 0:
        placed = [p - overshoot / 2 for p in placed]
    return placed


def style_axes(ax, t: dict) -> None:
    ax.set_facecolor(t["surface"])
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(t["axis"])
    ax.grid(axis="y", color=t["grid"], linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(colors=t["muted"], labelsize=9, length=0)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))


def line_chart(series: pd.DataFrame, colors: dict[str, int], title: str, subtitle: str,
               path_stub: Path, fill_between: tuple[str, str] | None = None) -> None:
    series = series.copy()
    series.index = pd.to_datetime(series.index)
    for mode, t in THEMES.items():
        fig, ax = plt.subplots(figsize=(10, 5.2), dpi=150)
        fig.patch.set_facecolor(t["surface"])
        style_axes(ax, t)

        if fill_between and all(c in series for c in fill_between):
            a, b = fill_between
            both = series[[a, b]].dropna()
            ax.fill_between(both.index, both[a], both[b], color=t["band"], linewidth=0, zorder=1)

        ends = []
        for name in series.columns:
            s = series[name].dropna()
            if s.empty:
                continue
            color = t["series"][colors[name]]
            ax.plot(s.index, s.values, color=color, linewidth=2, solid_capstyle="round",
                    label=name, zorder=3)
            ax.plot(s.index[-1], s.values[-1], "o", markersize=6, color=color,
                    markeredgecolor=t["surface"], markeredgewidth=1.5, zorder=4)
            ends.append((name, s.index[-1], s.values[-1], color))

        x_max = max(e[1] for e in ends)
        ax.set_xlim(right=x_max + timedelta(days=5))
        lo, hi = ax.get_ylim()
        placed = spread_labels([e[2] for e in ends], (hi - lo) * 0.05)
        # labels live in the right margin: x in axes fraction, y in data units
        for (name, x, y, color), py in zip(ends, placed):
            ax.annotate(f"{name}  {y:.0f}", xy=(x, y), xytext=(1.02, py),
                        textcoords=ax.get_yaxis_transform(), annotation_clip=False,
                        color=t["text"], fontsize=9, va="center",
                        arrowprops=dict(arrowstyle="-", color=color, linewidth=1, shrinkA=2, shrinkB=4))

        fig.text(0.06, 0.95, title, color=t["text"], fontsize=13, fontweight="bold")
        fig.text(0.06, 0.905, subtitle, color=t["text2"], fontsize=9.5)
        ax.set_ylabel("Arena rating (Elo-style)", color=t["text2"], fontsize=9)
        leg = ax.legend(loc="upper left", ncol=min(len(ends), 6), borderaxespad=0, frameon=False, fontsize=9,
                        bbox_to_anchor=(-0.01, 1.07), handlelength=1.6)
        for text in leg.get_texts():
            text.set_color(t["text2"])
        fig.text(0.06, 0.015, "Source: LMArena leaderboard dataset (CC BY 4.0)",
                 color=t["muted"], fontsize=8)
        fig.subplots_adjust(left=0.08, right=0.82, top=0.83, bottom=0.10)
        suffix = "" if mode == "light" else "-dark"
        fig.savefig(path_stub.with_name(path_stub.name + suffix + ".png"), facecolor=t["surface"])
        plt.close(fig)


def render_charts(arena: str, label: str, df: pd.DataFrame) -> None:
    start = (pd.Timestamp(df["date"].max()) - timedelta(days=CONFIG["chart_days"])).strftime("%Y-%m-%d")
    window = df[df["date"] >= start]
    latest = df[df["date"] == df["date"].max()]

    best_by_org = latest.groupby("organization")["rating"].max().sort_values(ascending=False)
    orgs = list(best_by_org.index[: CONFIG["frontier_orgs"]])
    front = frontier(window, orgs)[orgs]  # column order = current standing
    line_chart(front, org_slots(orgs),
               f"{label} Arena: the frontier race",
               f"Best-rated model per lab, top {len(orgs)} labs today, last {CONFIG['chart_days']} days",
               CHART_DIR / f"{arena}-frontier")

    ovp = open_vs_proprietary(window)
    cols = [c for c in ("Proprietary", "Open-weight") if c in ovp]
    if len(cols) == 2:
        gap = ovp.dropna().iloc[-1]
        sub = (f"Best proprietary vs best open-weight model · gap today: "
               f"{gap['Proprietary'] - gap['Open-weight']:.0f} rating points")
    else:
        sub = "Best proprietary vs best open-weight model"
    line_chart(ovp[cols], {"Proprietary": 0, "Open-weight": 1},
               f"{label} Arena: open-weight vs proprietary", sub,
               CHART_DIR / f"{arena}-open-vs-proprietary", fill_between=("Proprietary", "Open-weight"))


# --------------------------------------------------------------------------- #
# README
# --------------------------------------------------------------------------- #
def picture(stub: str, alt: str) -> str:
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="charts/{stub}-dark.png">'
            f'<img alt="{alt}" src="charts/{stub}.png"></picture>')


def rank_change(model: str, rank: int, prev: pd.DataFrame | None) -> str:
    if prev is None:
        return "–"
    row = prev[prev["model"] == model]
    if row.empty:
        return "🆕"
    diff = int(row["rank"].iloc[0]) - rank
    return f"▲{diff}" if diff > 0 else f"▼{-diff}" if diff < 0 else "="


def arena_section(arena: str, label: str, df: pd.DataFrame) -> list[str]:
    latest, prev, date, prev_date = latest_and_previous(df)
    top = latest.sort_values(["rank", "rating"], ascending=[True, False]).head(CONFIG["table_size"])
    vs = f" · change vs {prev_date}" if prev_date else ""
    lines = [
        f"### {label} Arena",
        "",
        f"Leaderboard published {date}{vs}.",
        "",
        "| # | Δ | Model | Lab | License | Rating | 95% CI | Votes |",
        "|--:|:-:|-------|-----|---------|-------:|:------:|------:|",
    ]
    for r in top.itertuples():
        votes = f"{int(r.votes):,}" if pd.notna(r.votes) else "–"
        lic = "Proprietary" if not is_open(r.license) else f"Open ({r.license})"
        lines.append(f"| {r.rank} | {rank_change(r.model, r.rank, prev)} | `{r.model}` | {r.organization} "
                     f"| {lic} | {r.rating:.0f} | {r.rating_lower:.0f}–{r.rating_upper:.0f} | {votes} |")

    open_best = latest[latest["license"].map(is_open)].sort_values("rating", ascending=False).head(1)
    if not open_best.empty:
        o = open_best.iloc[0]
        lines += ["", f"Best open-weight model: `{o['model']}` ({o['organization']}, {o['license']}) "
                      f"at #{o['rank']} with {o['rating']:.0f}."]
    lines += [
        "",
        picture(f"{arena}-frontier", f"{label} Arena frontier race chart"),
        "",
        picture(f"{arena}-open-vs-proprietary", f"{label} Arena open-weight vs proprietary chart"),
        "",
    ]
    return lines


def update_readme(sections: list[str], snapshots: dict[str, int]) -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    if README_START not in text or README_END not in text:
        return
    stats = " · ".join(f"{label}: {n} snapshots" for label, n in snapshots.items())
    block = [README_START, f"_Tracked history: {stats}_", "", *sections, README_END]
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    README.write_text(pattern.sub(lambda _: "\n".join(block), text), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, help="read <arena>.parquet from here instead of the Hub")
    parser.add_argument("--force-render", action="store_true", help="redraw charts even without new data")
    args = parser.parse_args()

    DATA_DIR.mkdir(exist_ok=True)
    CHART_DIR.mkdir(exist_ok=True)

    histories: dict[str, pd.DataFrame] = {}
    total_new = 0
    for arena, label in CONFIG["arenas"].items():
        print(f"[{label}]")
        try:
            fresh = load_arena(arena, args.source_dir)
        except Exception as e:  # noqa: BLE001 - one broken arena must not stop the others
            print(f"  ! skipped: {e}", file=sys.stderr)
            csv_path = DATA_DIR / f"{arena}.csv"
            if csv_path.exists():
                histories[arena] = pd.read_csv(csv_path, dtype={"date": str})
            continue
        merged, n_new = merge_history(arena, fresh)
        total_new += n_new
        histories[arena] = merged
        print(f"  {n_new} new snapshot(s), {merged['date'].nunique()} total, latest {merged['date'].max()}")

    if not histories:
        print("No data available.", file=sys.stderr)
        return 1
    if total_new == 0 and not args.force_render:
        print("No new leaderboard snapshots. Nothing to commit.")
        return 0

    sections, snapshots = [], {}
    for arena, df in histories.items():
        label = CONFIG["arenas"][arena]
        render_charts(arena, label, df)
        sections += arena_section(arena, label, df)
        snapshots[label] = df["date"].nunique()
    update_readme(sections, snapshots)
    print("Charts and README updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
