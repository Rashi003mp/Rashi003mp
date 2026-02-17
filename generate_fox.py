#!/usr/bin/env python3
"""
generate_fox.py
Fetches real GitHub contribution data via GraphQL API,
then generates an animated fox SVG over the contribution grid.
Run by GitHub Actions daily — outputs fox_contribution.svg
"""

import os
import json
import urllib.request
import urllib.error
import random
from datetime import datetime, timedelta

# ── Fetch real contribution data ─────────────────────────
def fetch_contributions(username, token):
    query = """
    query($username: String!) {
      user(login: $username) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
                color
              }
            }
          }
        }
      }
    }
    """
    payload = json.dumps({
        "query": query,
        "variables": {"username": username}
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "fox-contribution-generator"
        }
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())

    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    total = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

    # Build 52w x 7d grid — pad to exactly 52 weeks
    grid = []
    for week in weeks[-52:]:
        days = week["contributionDays"]
        week_data = []
        for day in days:
            count = day["contributionCount"]
            # Map count to 0-4 level
            if count == 0:   level = 0
            elif count <= 2: level = 1
            elif count <= 5: level = 2
            elif count <= 9: level = 3
            else:            level = 4
            week_data.append({"level": level, "count": count, "date": day["date"]})
        # Pad week to 7 days if needed
        while len(week_data) < 7:
            week_data.insert(0, {"level": 0, "count": 0, "date": ""})
        grid.append(week_data)

    # Pad to 52 weeks if fewer
    while len(grid) < 52:
        grid.insert(0, [{"level": 0, "count": 0, "date": ""} for _ in range(7)])

    return grid[:52], total


# ── Generate SVG ─────────────────────────────────────────
def generate_svg(grid, total, username):
    WEEKS   = 52
    DAYS    = 7
    CELL    = 11
    GAP     = 3
    STEP    = CELL + GAP
    PAD_L   = 30
    PAD_T   = 36
    WIDTH   = PAD_L + WEEKS * STEP + 24
    HEIGHT  = PAD_T + DAYS * STEP + 56

    BG           = "#0d1117"
    LABEL_COLOR  = "#8b949e"
    ACCENT       = "#ff6d00"

    # Orange-themed contribution levels
    CELL_COLORS = ["#161b22", "#ff6d0030", "#ff6d0068", "#ff6d00aa", "#ff6d00"]

    # Fox boustrophedon path (row-by-row, alternating direction)
    path_cells = []
    for d in range(DAYS):
        if d % 2 == 0:
            for w in range(WEEKS):
                path_cells.append((w, d))
        else:
            for w in range(WEEKS - 1, -1, -1):
                path_cells.append((w, d))

    TOTAL_CELLS   = len(path_cells)
    ANIM_DURATION = 20  # seconds per loop

    def cx(w): return PAD_L + w * STEP + CELL // 2
    def cy(d): return PAD_T + d * STEP + CELL // 2

    # Motion path for fox
    pts = [f"{cx(w)},{cy(d)}" for w, d in path_cells]
    pts.append(pts[0])  # close loop
    motion_path = "M " + " L ".join(pts)

    # Month labels (approximate week offsets)
    month_starts = []
    seen_months = set()
    for wi, week in enumerate(grid):
        for day in week:
            if day["date"]:
                try:
                    dt = datetime.strptime(day["date"], "%Y-%m-%d")
                    if dt.month not in seen_months:
                        seen_months.add(dt.month)
                        month_starts.append((wi, dt.strftime("%b")))
                    break
                except:
                    pass

    day_labels = ["Mon", "", "Wed", "", "Fri", "", "Sun"]

    lines = []
    lines.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"
     style="background:{BG}; border-radius:12px;">
  <defs>
    <filter id="fg" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <radialGradient id="fb" cx="50%" cy="40%" r="58%">
      <stop offset="0%" stop-color="#ff9500"/>
      <stop offset="100%" stop-color="#d45500"/>
    </radialGradient>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" rx="12" fill="{BG}"/>''')

    # Title + total
    lines.append(f'''
  <text x="{PAD_L}" y="16" font-family="monospace" font-size="10" fill="{LABEL_COLOR}" letter-spacing="1.5">CONTRIBUTION ACTIVITY</text>
  <text x="{WIDTH - 10}" y="16" text-anchor="end" font-family="monospace" font-size="10" fill="{ACCENT}" font-weight="bold">{total} total contributions</text>''')

    # Month labels
    for wi, mname in month_starts:
        mx = PAD_L + wi * STEP
        lines.append(f'  <text x="{mx}" y="{PAD_T - 6}" font-family="monospace" font-size="9" fill="{LABEL_COLOR}">{mname}</text>')

    # Day labels
    for i, label in enumerate(day_labels):
        if label:
            y = PAD_T + i * STEP + CELL - 1
            lines.append(f'  <text x="{PAD_L - 6}" y="{y}" text-anchor="end" font-family="monospace" font-size="9" fill="{LABEL_COLOR}">{label}</text>')

    # Grid cells
    lines.append('\n  <!-- Contribution grid -->')
    for wi, week in enumerate(grid):
        for di, day in enumerate(week):
            x = PAD_L + wi * STEP
            y = PAD_T + di * STEP
            lv = day["level"]
            color = CELL_COLORS[lv]
            cid = f"c{wi}_{di}"
            tip = f"{day['count']} contributions on {day['date']}" if day['date'] else ""
            lines.append(f'  <rect id="{cid}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"><title>{tip}</title></rect>')

    # Eat animations — each cell flashes when fox passes
    lines.append('\n  <!-- Eat flash animations -->')
    for i, (w, d) in enumerate(path_cells):
        t_start = round(i / TOTAL_CELLS * ANIM_DURATION, 3)
        lv = grid[w][d]["level"]
        orig = CELL_COLORS[lv]
        cid = f"c{w}_{d}"
        lines.append(
            f'  <animate xlink:href="#{cid}" attributeName="fill" '
            f'values="{orig};#ffffff;{ACCENT};#161b22" '
            f'keyTimes="0;0.08;0.35;1" '
            f'dur="0.5s" begin="{t_start}s" fill="freeze" repeatCount="indefinite"/>'
        )

    # Fox character with animateMotion
    lines.append(f'''
  <!-- 🦊 Fox animated across grid -->
  <g filter="url(#fg)">
    <!-- Body -->
    <ellipse cx="0" cy="0" rx="7" ry="5" fill="url(#fb)"/>
    <!-- Head -->
    <ellipse cx="7" cy="-1" rx="5" ry="4.5" fill="#ff8800"/>
    <!-- Ears -->
    <polygon points="5,-4.5 3,-9 8,-5"   fill="#e05500"/>
    <polygon points="9,-4.5 11,-9 13,-5" fill="#e05500"/>
    <polygon points="5.5,-5 4,-7.5 7.5,-5.5" fill="#ffb347" opacity="0.8"/>
    <polygon points="9.5,-5 11,-7.5 12,-5.5" fill="#ffb347" opacity="0.8"/>
    <!-- Snout -->
    <ellipse cx="11" cy="1" rx="3" ry="2.3" fill="#f5a46a"/>
    <ellipse cx="13.5" cy="0.5" rx="1.1" ry="0.9" fill="#110500"/>
    <!-- Eye -->
    <ellipse cx="8" cy="-2.5" rx="1.5" ry="1.5" fill="#110500"/>
    <ellipse cx="8.5" cy="-2.9" rx="0.45" ry="0.45" fill="white"/>
    <!-- Tail -->
    <path d="M-7,0 Q-14,-2 -13,-8 Q-9,-13 -5,-7 Q-3,-3 -7,0" fill="#e05500"/>
    <path d="M-11,-8 Q-13,-12 -10,-12 Q-7,-11 -8,-8" fill="white" opacity="0.9"/>
    <!-- Running legs -->
    <line x1="2" y1="4" x2="0" y2="9" stroke="#c04800" stroke-width="2.2" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" values="0 2 4;22 2 4;0 2 4;-22 2 4;0 2 4" dur="0.32s" repeatCount="indefinite"/>
    </line>
    <line x1="-2" y1="4" x2="-4" y2="9" stroke="#c04800" stroke-width="2.2" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" values="0 -2 4;-22 -2 4;0 -2 4;22 -2 4;0 -2 4" dur="0.32s" repeatCount="indefinite"/>
    </line>
    <line x1="4" y1="4" x2="6" y2="9" stroke="#c04800" stroke-width="2.2" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" values="0 4 4;-16 4 4;0 4 4;16 4 4;0 4 4" dur="0.32s" begin="0.16s" repeatCount="indefinite"/>
    </line>
    <line x1="-4" y1="4" x2="-2" y2="9" stroke="#c04800" stroke-width="2.2" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" values="0 -4 4;16 -4 4;0 -4 4;-16 -4 4;0 -4 4" dur="0.32s" begin="0.16s" repeatCount="indefinite"/>
    </line>
    <animateMotion dur="{ANIM_DURATION}s" repeatCount="indefinite" calcMode="linear" rotate="auto">
      <mpath xlink:href="#fp"/>
    </animateMotion>
  </g>
  <path id="fp" d="{motion_path}" fill="none" stroke="none"/>''')

    # Legend
    ly = PAD_T + DAYS * STEP + 16
    lines.append(f'\n  <text x="{PAD_L}" y="{ly + 8}" font-family="monospace" font-size="9" fill="{LABEL_COLOR}">Less</text>')
    for i, color in enumerate(CELL_COLORS):
        lx = PAD_L + 30 + i * (CELL + 3)
        lines.append(f'  <rect x="{lx}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>')
    lx_more = PAD_L + 30 + 5 * (CELL + 3) + 2
    lines.append(f'  <text x="{lx_more}" y="{ly + 8}" font-family="monospace" font-size="9" fill="{LABEL_COLOR}">More</text>')
    lines.append(f'  <text x="{WIDTH - 10}" y="{ly + 8}" text-anchor="end" font-family="monospace" font-size="9" fill="{ACCENT}">🦊 eating your commits</text>')

    lines.append('\n</svg>')
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────
if __name__ == "__main__":
    username = os.environ.get("GH_USERNAME", "Rashi003mp")
    token    = os.environ.get("GH_TOKEN", "")

    if not token:
        print("ERROR: GH_TOKEN environment variable not set")
        exit(1)

    print(f"Fetching contributions for @{username}...")
    grid, total = fetch_contributions(username, token)
    print(f"Got {WEEKS} weeks, {total} total contributions")

    print("Generating SVG...")
    svg = generate_svg(grid, total, username)

    out_path = os.environ.get("OUTPUT_PATH", "fox_contribution.svg")
    with open(out_path, "w") as f:
        f.write(svg)

    print(f"Written to {out_path} ({len(svg):,} chars)")
