#!/usr/bin/env python3
"""Generate a self-hosted GitHub contribution streak card.

The profile README references the generated SVG instead of a public image API.
GitHub Actions supplies GITHUB_TOKEN and GITHUB_USERNAME when refreshing it.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


GRAPHQL_URL = "https://api.github.com/graphql"
QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""


def fetch_calendar(username: str, token: str) -> dict:
    payload = json.dumps({"query": QUERY, "variables": {"login": username}}).encode()
    request = Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "masondev1024-profile-streak-card",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"GitHub GraphQL request failed: {exc}") from exc
    if result.get("errors"):
        messages = "; ".join(error.get("message", "unknown GraphQL error") for error in result["errors"])
        raise RuntimeError(messages)
    user = result.get("data", {}).get("user")
    if not user:
        raise RuntimeError(f"GitHub user not found: {username}")
    return user["contributionsCollection"]["contributionCalendar"]


def streak_metrics(calendar: dict) -> tuple[int, int, int]:
    days = [
        (dt.date.fromisoformat(day["date"]), int(day["contributionCount"]))
        for week in calendar["weeks"]
        for day in week["contributionDays"]
    ]
    days.sort()

    longest = 0
    run = 0
    for _, count in days:
        if count > 0:
            run += 1
            longest = max(longest, run)
        else:
            run = 0

    today = dt.date.today()
    active_days = [index for index, (day, count) in enumerate(days) if day <= today and count > 0]
    current = 0
    if active_days:
        index = active_days[-1]
        while index >= 0 and days[index][1] > 0:
            current += 1
            index -= 1

    return current, longest, int(calendar["totalContributions"])


def flame_icon() -> str:
    return (
        '<path d="M24.9 2.4c.7 7.1-4.1 10.3-2.3 14.2 1.1 2.3 3.6 3.1 5.3 1.2 '
        '2.1-2.3 1.5-5.8.3-8.3 7.3 4.8 10.6 11.5 8.8 18.3C35.3 35.1 30 40 '
        '23 40 14.7 40 8 34.3 8 26.1c0-6.2 3.7-11.3 8.7-16.5-.4 4.1.8 6.9 '
        '3.1 7.8-1.3-4.3 1.2-9.4 5.1-15Z" fill="#f97316"/>'
        '<path d="M23.4 22.2c2.9 3.1 4.4 5.1 4.4 7.7 0 3.3-2.1 5.8-5.2 5.8s-5.4-2.3-5.4-5.6c0-2.5 1.6-4.7 4.2-7.9.5 1.9 1.3 2.8 2 3.2-.6-1.4-.5-2.2 0-3.2Z" fill="#fff7ed"/>'
    )


def card_svg(username: str, current: int, longest: int, total: int) -> str:
    updated = dt.date.today().isoformat()
    user_label = html.escape(username)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="650" height="205" viewBox="0 0 650 205" role="img" aria-labelledby="title desc">
  <title id="title">GitHub contribution streak for {user_label}</title>
  <desc id="desc">Current streak {current} days, longest streak {longest} days, and {total} contributions in the last year.</desc>
  <rect x="0.5" y="0.5" width="649" height="204" rx="9" fill="#ffffff" stroke="#d0d7de"/>
  <g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">
    <g transform="translate(24 24)">
      <circle cx="20" cy="20" r="20" fill="#fff7ed"/>
      <g transform="translate(8 8) scale(.6)">{flame_icon()}</g>
      <text x="56" y="17" font-size="17" font-weight="700" fill="#24292f">GitHub Streak</text>
      <text x="56" y="38" font-size="12" fill="#57606a">{user_label} · updated {updated}</text>
    </g>
    <line x1="24" y1="82" x2="626" y2="82" stroke="#eaeef2"/>
    <g transform="translate(32 103)">
      <g transform="translate(0 0)">
        <text x="0" y="0" font-size="31" font-weight="700" fill="#24292f">{current}</text>
        <text x="0" y="24" font-size="11" font-weight="700" letter-spacing="1.1" fill="#57606a">CURRENT STREAK</text>
        <text x="0" y="43" font-size="11" fill="#8c959f">consecutive days</text>
      </g>
      <line x1="194" y1="-12" x2="194" y2="53" stroke="#eaeef2"/>
      <g transform="translate(226 0)">
        <text x="0" y="0" font-size="31" font-weight="700" fill="#24292f">{longest}</text>
        <text x="0" y="24" font-size="11" font-weight="700" letter-spacing="1.1" fill="#57606a">LONGEST STREAK</text>
        <text x="0" y="43" font-size="11" fill="#8c959f">best run in the last year</text>
      </g>
      <line x1="414" y1="-12" x2="414" y2="53" stroke="#eaeef2"/>
      <g transform="translate(446 0)">
        <text x="0" y="0" font-size="31" font-weight="700" fill="#24292f">{total}</text>
        <text x="0" y="24" font-size="11" font-weight="700" letter-spacing="1.1" fill="#57606a">CONTRIBUTIONS</text>
        <text x="0" y="43" font-size="11" fill="#8c959f">in the last year</text>
      </g>
    </g>
    <text x="32" y="187" font-size="11" fill="#8c959f">Built from GitHub contribution history · refreshed automatically</text>
  </g>
</svg>
'''


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    username = os.environ.get("GITHUB_USERNAME", "masondev1024")
    if not token:
        raise SystemExit("GITHUB_TOKEN or GH_TOKEN is required")
    calendar = fetch_calendar(username, token)
    current, longest, total = streak_metrics(calendar)
    output = Path(__file__).resolve().parents[1] / "assets" / "github-streak.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(card_svg(username, current, longest, total), encoding="utf-8")
    print(f"Updated {output} (current={current}, longest={longest}, total={total})")


if __name__ == "__main__":
    main()
