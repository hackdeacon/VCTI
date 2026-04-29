#!/usr/bin/env python3
import requests
import time

BASE_URL = "https://vlr.orlandomm.net/api/v1"

def fetch_data(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "OK":
            return data
        else:
            print(f"Error fetching {endpoint}: status {data.get('status')}")
            return None
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}")
        return None

def generate_players_markdown(players):
    md = "# 职业选手 (Players)\n\n"
    md += f"共计 {len(players)} 名职业选手\n\n"

    # Group by country
    by_country = {}
    for p in players:
        country = p.get("country", "unknown")
        if country not in by_country:
            by_country[country] = []
        by_country[country].append(p)

    for country, country_players in sorted(by_country.items()):
        md += f"## {country.upper()}\n\n"
        for p in sorted(country_players, key=lambda x: x.get("name", "")):
            name = p.get("name", "")
            team = p.get("teamTag", "")
            pid = p.get("id", "")
            url = p.get("url", "")
            team_str = f" [{team}]" if team else ""
            md += f"- **{name}**{team_str} - [VLR Profile]({url})\n"
        md += "\n"
    return md

def generate_teams_markdown(teams):
    md = "# 职业战队 (Teams)\n\n"
    md += f"共计 {len(teams)} 支职业战队\n\n"

    for team in sorted(teams, key=lambda x: x.get("name", "")):
        name = team.get("name", "")
        country = team.get("country", "")
        tid = team.get("id", "")
        url = team.get("url", "")
        img = team.get("img", "")
        md += f"## {name}\n\n"
        md += f"- 地区: {country}\n"
        md += f"- VLR Profile: [{url}]({url})\n\n"
    return md

def generate_matches_markdown(matches):
    md = "# 近期比赛 (Matches)\n\n"

    live_matches = [m for m in matches if m.get("status") == "LIVE"]
    upcoming_matches = [m for m in matches if m.get("status") == "Upcoming"]
    completed_matches = [m for m in matches if m.get("status") not in ["LIVE", "Upcoming"]]

    if live_matches:
        md += "## 正在进行 🔴\n\n"
        for m in live_matches[:20]:
            teams = m.get("teams", [])
            if len(teams) >= 2:
                t1_name = teams[0].get("name", "TBD")
                t1_score = teams[0].get("score", 0)
                t2_name = teams[1].get("name", "TBD")
                t2_score = teams[1].get("score", 0)
                tournament = m.get("tournament", "")
                md += f"- **{t1_name}** {t1_score} - {t2_score} **{t2_name}**\n"
                md += f"  _{tournament}_\n\n"

    if upcoming_matches:
        md += "## 即将开始 ⏳\n\n"
        for m in upcoming_matches[:30]:
            teams = m.get("teams", [])
            if len(teams) >= 2:
                t1_name = teams[0].get("name", "TBD")
                t2_name = teams[1].get("name", "TBD")
                tournament = m.get("tournament", "")
                in_time = m.get("in", "")
                md += f"- **{t1_name}** vs **{t2_name}**"
                if in_time:
                    md += f" ({in_time})"
                md += f"\n  _{tournament}_\n"
        md += "\n"

    if completed_matches:
        md += "## 已完成 ✅\n\n"
        for m in completed_matches[:30]:
            teams = m.get("teams", [])
            if len(teams) >= 2:
                t1_name = teams[0].get("name", "TBD")
                t1_score = teams[0].get("score", 0)
                t2_name = teams[1].get("name", "TBD")
                t2_score = teams[1].get("score", 0)
                tournament = m.get("tournament", "")
                md += f"- **{t1_name}** {t1_score} - {t2_score} **{t2_name}**\n"
                md += f"  _{tournament}_\n"
        md += "\n"

    return md

def generate_events_markdown(events):
    md = "# 赛事 (Events)\n\n"

    ongoing = [e for e in events if e.get("status") == "ongoing"]
    completed = [e for e in events if e.get("status") == "completed"]
    upcoming = [e for e in events if e.get("status") == "upcoming"]

    if ongoing:
        md += "## 进行中 🔴\n\n"
        for e in sorted(ongoing, key=lambda x: x.get("name", "")):
            name = e.get("name", "")
            dates = e.get("dates", "")
            country = e.get("country", "")
            prizepool = e.get("prizepool", "")
            md += f"### {name}\n\n"
            md += f"- 时间: {dates}\n"
            md += f"- 地区: {country}\n"
            if prizepool and prizepool != "0":
                md += f"- 奖池: ${prizepool}\n"
            md += "\n"

    if upcoming:
        md += "## 即将到来 ⏳\n\n"
        for e in sorted(upcoming, key=lambda x: x.get("name", ""))[:20]:
            name = e.get("name", "")
            dates = e.get("dates", "")
            country = e.get("country", "")
            md += f"- **{name}** - {dates} ({country})\n"
        md += "\n"

    if completed:
        md += "## 已完成 ✅\n\n"
        for e in sorted(completed, key=lambda x: x.get("name", ""))[:50]:
            name = e.get("name", "")
            dates = e.get("dates", "")
            md += f"- {name} - {dates}\n"
        md += "\n"

    return md

def generate_results_markdown(results):
    md = "# 近期赛果 (Results)\n\n"

    for r in results[:50]:
        teams = r.get("teams", [])
        if len(teams) >= 2:
            t1_name = teams[0].get("name", "TBD")
            t1_score = teams[0].get("score", 0)
            t2_name = teams[1].get("name", "TBD")
            t2_score = teams[1].get("score", 0)
            tournament = r.get("tournament", "")
            md += f"- **{t1_name}** {t1_score} - {t2_score} **{t2_name}**\n"
            md += f"  _{tournament}_\n"
    md += "\n"
    return md

def main():
    print("开始获取 vlr.gg 电竞 API 数据...")
    all_data = {}

    # Fetch players - first page only (50 players for demo)
    print("获取选手数据...")
    players_data = fetch_data("/players", {"limit": 100})
    if players_data:
        all_data["players"] = players_data.get("data", [])
        print(f"  找到 {len(all_data['players'])} 名选手")

    # Fetch teams - first page (50 teams)
    print("获取战队数据...")
    teams_data = fetch_data("/teams", {"limit": 130})
    if teams_data:
        all_data["teams"] = teams_data.get("data", [])
        print(f"  找到 {len(all_data['teams'])} 支战队")

    # Fetch matches
    print("获取比赛数据...")
    matches_data = fetch_data("/matches", {"limit": 100})
    if matches_data:
        all_data["matches"] = matches_data.get("data", [])
        print(f"  找到 {len(all_data['matches'])} 场比赛")

    # Fetch events
    print("获取赛事数据...")
    events_data = fetch_data("/events", {"limit": 200})
    if events_data:
        all_data["events"] = events_data.get("data", [])
        print(f"  找到 {len(all_data['events'])} 项赛事")

    # Fetch results
    print("获取赛果数据...")
    results_data = fetch_data("/results", {"limit": 50})
    if results_data:
        all_data["results"] = results_data.get("data", [])
        print(f"  找到 {len(all_data['results'])} 条赛果")

    markdown_parts = []

    markdown_parts.append("# 无畏契约 Valorant 电竞资料大全\n\n")
    markdown_parts.append("本文档由 [vlr.orlandomm.net](https://vlr.orlandomm.net) API 自动生成。\n")
    markdown_parts.append("数据来源: [vlr.gg](https://www.vlr.gg)\n\n")

    markdown_parts.append("## 目录\n\n")
    markdown_parts.append("- [职业战队](#职业战队-teams)\n")
    markdown_parts.append("- [职业选手](#职业选手-players)\n")
    markdown_parts.append("- [赛事](#赛事-events)\n")
    markdown_parts.append("- [近期比赛](#近期比赛-matches)\n")
    markdown_parts.append("- [近期赛果](#近期赛果-results)\n\n")

    if all_data.get("teams"):
        markdown_parts.append(generate_teams_markdown(all_data["teams"]))

    if all_data.get("players"):
        markdown_parts.append(generate_players_markdown(all_data["players"]))

    if all_data.get("events"):
        markdown_parts.append(generate_events_markdown(all_data["events"]))

    if all_data.get("matches"):
        markdown_parts.append(generate_matches_markdown(all_data["matches"]))

    if all_data.get("results"):
        markdown_parts.append(generate_results_markdown(all_data["results"]))

    full_md = "".join(markdown_parts)

    output_path = "output/valorant_esports_vlr.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_md)

    print(f"\n完成! Markdown 文件已保存到: {output_path}")
    print(f"文件大小: {len(full_md)} 字符")

if __name__ == "__main__":
    main()
