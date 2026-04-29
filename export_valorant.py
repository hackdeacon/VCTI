#!/usr/bin/env python3
import requests
import json
import os

BASE_URL = "https://valorant-api.com/v1"

ENDPOINTS = {
    "agents": "/agents",
    "buddies": "/buddies",
    "buddy_levels": "/buddies/levels",
    "bundles": "/bundles",
    "ceremonies": "/ceremonies",
    "competitive_tiers": "/competitivetiers",
    "content_tiers": "/contenttiers",
    "contracts": "/contracts",
    "currencies": "/currencies",
    "events": "/events",
    "gamemodes": "/gamemodes",
    "gamemode_equippables": "/gamemodes/equippables",
    "gears": "/gear",
    "level_borders": "/levelborders",
    "maps": "/maps",
    "player_cards": "/playercards",
    "player_titles": "/playertitles",
    "seasons": "/seasons",
    "seasons_competitive": "/seasons/competitive",
    "sprays": "/sprays",
    "spray_levels": "/sprays/levels",
    "themes": "/themes",
    "weapons": "/weapons",
    "weapon_skins": "/weapons/skins",
    "weapon_skin_chromas": "/weapons/skinchromas",
    "weapon_skin_levels": "/weapons/skinlevels",
}

def fetch_data(endpoint_name, endpoint_path, language="zh-CN"):
    url = f"{BASE_URL}{endpoint_path}?language={language}"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == 200:
            return data.get("data", [])
        else:
            print(f"Error fetching {endpoint_name}: status {data.get('status')}")
            return []
    except Exception as e:
        print(f"Error fetching {endpoint_name}: {e}")
        return []

def generate_agents_markdown(agents):
    md = "# 特工\n\n"
    roles = {}
    for agent in agents:
        if agent.get("isPlayableCharacter", False):
            role = agent.get("role", {}).get("displayName", "Unknown")
            if role not in roles:
                roles[role] = []
            roles[role].append(agent)

    for role, role_agents in roles.items():
        md += f"## {role}\n\n"
        for agent in sorted(role_agents, key=lambda x: x.get("displayName", "")):
            name = agent.get("displayName", "Unknown")
            desc = agent.get("description", "")
            md += f"### {name}\n\n"
            md += f"{desc}\n\n"

            abilities = agent.get("abilities", [])
            if abilities:
                md += "**技能:**\n\n"
                for ab in abilities:
                    ab_name = ab.get("displayName", "")
                    ab_desc = ab.get("description", "")
                    slot = ab.get("slot", "")
                    if ab_name and ab_name != "null":
                        slot_label = ""
                        if slot == "Ability1":
                            slot_label = " (C)"
                        elif slot == "Ability2":
                            slot_label = " (Q)"
                        elif slot == "Grenade":
                            slot_label = " (E)"
                        elif slot == "Ultimate":
                            slot_label = " (X)"
                        md += f"- **{ab_name}{slot_label}**: {ab_desc}\n"
                md += "\n"
    return md

def generate_weapons_markdown(weapons):
    md = "# 武器\n\n"
    categories = {}
    for weapon in weapons:
        cat = weapon.get("category", "Unknown").split("::")[-1]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(weapon)

    for cat, cat_weapons in categories.items():
        md += f"## {cat}\n\n"
        for weapon in sorted(cat_weapons, key=lambda x: x.get("displayName", "")):
            name = weapon.get("displayName", "Unknown")
            md += f"### {name}\n\n"

            stats = weapon.get("weaponStats", {})
            if stats:
                md += "- 开火模式: "
                fire_modes = stats.get("fireRate", "")
                md += f"{fire_modes} RPM\n"
                md += f"- 弹匣容量: {stats.get('magazineSize', 'N/A')}\n"
                md += f"- 装弹时间: {stats.get('reloadTimeSeconds', 'N/A')} 秒\n"
                damage = stats.get("damageRanges", [])
                if damage:
                    md += "- 伤害:\n"
                    for dmg in damage[:2]:
                        md += f"  - {dmg.get('rangeStartMeters', 0)}-{dmg.get('rangeEndMeters', 0)}米: 头{dmg.get('headDamage', 0)} 身{dmg.get('bodyDamage', 0)} 腿{dmg.get('legDamage', 0)}\n"
            md += "\n"
    return md

def generate_maps_markdown(maps):
    md = "# 地图\n\n"
    for map_item in sorted(maps, key=lambda x: x.get("displayName", "")):
        name = map_item.get("displayName", "Unknown")
        coords = map_item.get("coordinates", "")
        md += f"## {name}\n\n"
        if coords:
            md += f"- 坐标: {coords}\n"
        callouts = map_item.get('callouts') or []
        md += f"- 点位数量: {len(callouts)}\n\n"
    return md

def generate_gamemodes_markdown(gamemodes):
    md = "# 游戏模式\n\n"
    for mode in sorted(gamemodes, key=lambda x: x.get("displayName", "")):
        if mode.get("isPlayable", False):
            name = mode.get("displayName", "Unknown")
            desc = mode.get("description", "")
            md += f"## {name}\n\n"
            if desc:
                md += f"{desc}\n\n"
    return md

def generate_simple_list_markdown(items, title, name_field="displayName", desc_field="description"):
    md = f"# {title}\n\n"
    for item in sorted(items, key=lambda x: x.get(name_field, "")):
        name = item.get(name_field, "Unknown")
        desc = item.get(desc_field, "")
        md += f"## {name}\n\n"
        if desc:
            md += f"{desc}\n\n"
    return md

def main():
    print("开始获取 Valorant API 数据...")
    all_data = {}

    for name, path in ENDPOINTS.items():
        print(f"获取 {name}...")
        data = fetch_data(name, path)
        all_data[name] = data
        print(f"  找到 {len(data) if isinstance(data, list) else 1} 条记录")

    os.makedirs("output", exist_ok=True)

    markdown_parts = []

    markdown_parts.append("# 无畏契约 Valorant 游戏资料大全\n\n")
    markdown_parts.append("本文档由 [valorant-api.com](https://valorant-api.com) API 自动生成 (语言: zh-CN)。\n\n")
    markdown_parts.append("## 目录\n\n")
    markdown_parts.append("- [特工](#特工)\n")
    markdown_parts.append("- [武器](#武器)\n")
    markdown_parts.append("- [地图](#地图)\n")
    markdown_parts.append("- [游戏模式](#游戏模式)\n")
    markdown_parts.append("- [段位](#段位)\n")
    markdown_parts.append("- [赛季](#赛季)\n")
    markdown_parts.append("- [喷漆](#喷漆)\n")
    markdown_parts.append("- [挂饰](#挂饰)\n")
    markdown_parts.append("- [玩家卡片](#玩家卡片)\n")
    markdown_parts.append("- [玩家称号](#玩家称号)\n")
    markdown_parts.append("- [货币](#货币)\n")
    markdown_parts.append("- [皮肤主题](#皮肤主题)\n\n")

    if all_data.get("agents"):
        markdown_parts.append(generate_agents_markdown(all_data["agents"]))

    if all_data.get("weapons"):
        markdown_parts.append(generate_weapons_markdown(all_data["weapons"]))

    if all_data.get("maps"):
        markdown_parts.append(generate_maps_markdown(all_data["maps"]))

    if all_data.get("gamemodes"):
        markdown_parts.append(generate_gamemodes_markdown(all_data["gamemodes"]))

    if all_data.get("competitive_tiers"):
        tiers_md = "# 段位\n\n"
        for tier_data in all_data["competitive_tiers"]:
            tiers = tier_data.get("tiers", [])
            for tier in tiers:
                if tier.get("rank", 0) > 0:
                    tiers_md += f"- {tier.get('tierName', '')}\n"
            break
        markdown_parts.append(tiers_md + "\n")

    if all_data.get("seasons"):
        seasons_md = "# 赛季\n\n"
        for season in sorted(all_data["seasons"], key=lambda x: x.get("startTime", "")):
            name = season.get("displayName", "")
            if name:
                seasons_md += f"- {name}\n"
        markdown_parts.append(seasons_md + "\n")

    if all_data.get("sprays"):
        markdown_parts.append(generate_simple_list_markdown(all_data["sprays"], "喷漆 (Sprays)"))

    if all_data.get("buddies"):
        markdown_parts.append(generate_simple_list_markdown(all_data["buddies"], "挂饰 (Buddies)"))

    if all_data.get("player_cards"):
        markdown_parts.append(generate_simple_list_markdown(all_data["player_cards"], "玩家卡片 (Player Cards)"))

    if all_data.get("player_titles"):
        titles_md = "# 玩家称号 (Player Titles)\n\n"
        valid_titles = [t for t in all_data["player_titles"] if t.get("displayName")]
        for title in sorted(valid_titles, key=lambda x: x.get("displayName", "")):
            name = title.get("displayName", "")
            if name and name != "":
                titles_md += f"- {name}\n"
        markdown_parts.append(titles_md + "\n")

    if all_data.get("currencies"):
        markdown_parts.append(generate_simple_list_markdown(all_data["currencies"], "货币 (Currencies)"))

    if all_data.get("themes"):
        markdown_parts.append(generate_simple_list_markdown(all_data["themes"], "皮肤主题 (Themes)"))

    full_md = "".join(markdown_parts)

    output_path = "output/valorant_full_guide_zh-CN.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_md)

    print(f"\n完成! Markdown 文件已保存到: {output_path}")
    print(f"文件大小: {len(full_md)} 字符")

if __name__ == "__main__":
    main()
