#!/usr/bin/env python3
import requests

BASE_URL = "https://vlrggapi.vercel.app/v2"

def fetch_data(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, params=params, timeout=120)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            return data.get("data", {}).get("segments", [])
        else:
            print(f"Error fetching {endpoint}: status {data.get('status')}")
            return []
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}")
        return []

def generate_rankings_markdown(rankings):
    md = "# 战队排名 (Team Rankings)\n\n"

    # Group by region if possible, otherwise just list top 50
    for rank in rankings[:50]:
        team_name = rank.get("team", "")
        country = rank.get("country", "")
        record = rank.get("record", "")
        earnings = rank.get("earnings", "")
        rank_num = rank.get("rank", "")
        last_played = rank.get("last_played", "")
        last_team = rank.get("last_played_team", "")
        md += f"{rank_num}. **{team_name}** ({country})\n"
        md += f"   - 战绩: {record}\n"
        md += f"   - 奖金: {earnings}\n"
        if last_played:
            md += f"   - 最近比赛: {last_played} {last_team}\n"
        md += "\n"

    return md

def generate_stats_markdown(stats):
    md = "# 选手统计 (Player Stats)\n\n"
    md += "基于最近 60 天比赛数据\n\n"

    # Top 30 players
    for player in stats[:30]:
        name = player.get("player", "")
        org = player.get("org", "")
        rating = player.get("rating", "")
        acs = player.get("average_combat_score", "")
        kd = player.get("kill_deaths", "")
        adr = player.get("average_damage_per_round", "")
        kast = player.get("kill_assists_survived_traded", "")
        kpr = player.get("kills_per_round", "")
        apr = player.get("assists_per_round", "")
        hs = player.get("headshot_percentage", "")
        agents = ", ".join(player.get("agents", []))
        rounds = player.get("rounds_played", "")

        md += f"## {name}"
        if org and org != "N/A":
            md += f" ({org})"
        md += "\n\n"
        md += f"- **Rating**: {rating}\n"
        md += f"- **ACS (平均战斗得分)**: {acs}\n"
        md += f"- **K/D 比**: {kd}\n"
        md += f"- **ADR (每回合平均伤害)**: {adr}\n"
        md += f"- **KAST%**: {kast}\n"
        md += f"- **KPR (每回合击杀)**: {kpr}\n"
        md += f"- **APR (每回合助攻)**: {apr}\n"
        md += f"- **爆头率**: {hs}\n"
        if agents:
            md += f"- **常用特工**: {agents}\n"
        md += f"- **回合数**: {rounds}\n"
        md += "\n"

    return md

def generate_news_markdown(news):
    md = "# 电竞新闻 (News)\n\n"

    for item in news[:30]:
        title = item.get("title", "")
        description = item.get("description", "")
        date = item.get("date", "")
        author = item.get("author", "")
        url = item.get("url_path", "")

        md += f"## {title}\n\n"
        if date:
            md += f"- 日期: {date}\n"
        if author:
            md += f"- 作者: {author}\n"
        if description:
            md += f"\n{description}\n"
        if url:
            md += f"\n[阅读全文]({url})\n"
        md += "\n"

    return md

def generate_events_markdown(events):
    md = "# 赛事列表 (Events)\n\n"

    ongoing = [e for e in events if e.get("status") == "ongoing"]
    upcoming = [e for e in events if e.get("status") == "upcoming"]
    completed = [e for e in events if e.get("status") == "completed"]

    if ongoing:
        md += "## 进行中 🔴\n\n"
        for e in ongoing:
            title = e.get("title", "")
            dates = e.get("dates", "")
            prize = e.get("prize", "")
            region = e.get("region", "")
            url = e.get("url_path", "")
            md += f"### {title}\n\n"
            md += f"- 时间: {dates}\n"
            if prize and prize != "TBD":
                md += f"- 奖池: {prize}\n"
            md += f"- 地区: {region}\n"
            if url:
                md += f"- [VLR 页面]({url})\n"
            md += "\n"

    if upcoming:
        md += "## 即将到来 ⏳\n\n"
        for e in upcoming[:20]:
            title = e.get("title", "")
            dates = e.get("dates", "")
            prize = e.get("prize", "")
            md += f"- **{title}** - {dates}"
            if prize and prize != "TBD":
                md += f" ({prize})"
            md += "\n"
        md += "\n"

    if completed:
        md += "## 已完成 ✅\n\n"
        for e in completed[:50]:
            title = e.get("title", "")
            dates = e.get("dates", "")
            md += f"- {title} - {dates}\n"
        md += "\n"

    return md

def main():
    print("开始获取 vlrggapi 电竞 API 数据...")
    all_data = {}

    # Fetch rankings for all major regions
    print("获取排名数据...")
    all_rankings = []
    for region in ["na", "eu", "ap", "kr", "jp", "br", "cn", "oce", "gc"]:
        print(f"  获取 {region} 地区排名...")
        rankings = fetch_data("/rankings", {"region": region})
        if rankings:
            for r in rankings:
                r["region"] = region
            all_rankings.extend(rankings[:20])
    all_data["rankings"] = all_rankings
    print(f"  共 {len(all_rankings)} 条排名记录")

    # Fetch stats - NA region (most complete data)
    print("获取选手统计数据...")
    stats = fetch_data("/stats", {"timespan": "60", "region": "na"})
    if stats:
        all_data["stats"] = stats
        print(f"  共 {len(stats)} 名选手统计")

    # Fetch events
    print("获取赛事数据...")
    events = fetch_data("/events")
    if events:
        all_data["events"] = events
        print(f"  共 {len(events)} 项赛事")

    # Fetch news - this might timeout, skip if it fails
    print("获取电竞新闻...")
    try:
        news = fetch_data("/news")
        if news:
            all_data["news"] = news
            print(f"  共 {len(news)} 条新闻")
        else:
            print("  新闻获取失败，跳过")
    except:
        print("  新闻获取超时，跳过")

    markdown_parts = []

    markdown_parts.append("# 无畏契约 Valorant 电竞深度分析\n\n")
    markdown_parts.append("本文档由 [vlrggapi.vercel.app](https://vlrggapi.vercel.app) API 自动生成。\n")
    markdown_parts.append("数据来源: [vlr.gg](https://www.vlr.gg)\n\n")

    markdown_parts.append("## 目录\n\n")
    markdown_parts.append("- [赛事列表](#赛事列表-events)\n")
    markdown_parts.append("- [战队排名](#战队排名-team-rankings)\n")
    markdown_parts.append("- [选手统计](#选手统计-player-stats)\n")
    if all_data.get("news"):
        markdown_parts.append("- [电竞新闻](#电竞新闻-news)\n")
    markdown_parts.append("\n")

    if all_data.get("events"):
        markdown_parts.append(generate_events_markdown(all_data["events"]))

    if all_data.get("rankings"):
        markdown_parts.append(generate_rankings_markdown(all_data["rankings"]))

    if all_data.get("stats"):
        markdown_parts.append(generate_stats_markdown(all_data["stats"]))

    if all_data.get("news"):
        markdown_parts.append(generate_news_markdown(all_data["news"]))

    full_md = "".join(markdown_parts)

    output_path = "output/valorant_esports_vlrgg.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_md)

    print(f"\n完成! Markdown 文件已保存到: {output_path}")
    print(f"文件大小: {len(full_md)} 字符")

if __name__ == "__main__":
    main()
