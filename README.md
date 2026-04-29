# VCTI - VALORANT 玩家人格测试

> 前有MBTI，后有SBTI，CSGO有CSTI，无畏契约有VCTI

基于 VALORANT 游戏习惯、团队角色、心态偏好的 16 型人格测试。

## ✨ 特性

- 🎮 **16 种独特玩家人格** - 从霓虹町战神到串子头子
- 📝 **8 道深度问题** - 基于真实游戏场景设计
- 🎨 **Claude 设计系统** - 温暖奶油色 + 优雅衬线字体
- 📊 **完整维度分析** - 4 个维度详细解析
- 📱 **完全响应式** - 支持手机、平板、桌面
- 🔗 **一键分享** - 支持 Web Share API

## 🧠 四个维度

| 维度 | 倾向 A | 倾向 B | 说明 |
|------|--------|--------|------|
| **D/C** | 冲锋型 D | 稳健型 C | 决定你在战场上的进攻倾向 |
| **S/N** | 侦察型 S | 直觉型 N | 决定你获取信息的方式 |
| **T/F** | 工具型 T | 核心型 F | 决定你在团队中的角色定位 |
| **J/P** | 竞技型 J | 娱乐型 P | 决定你对待游戏的心态 |

## 🎭 16 型人格速览

| 类型 | 名称 | 代表玩家 |
|------|------|---------|
| **DSTJ** | 霓虹町战神 | 康康 ZmjjKK |
| **DSTP** | 康神开播啦 | 撒娇模式的康康 |
| **DSFJ** | 广西步传人 | 广西表哥 |
| **DSFP** | ECO 局战神 | 所有喜欢强起的玩家 |
| **DNTJ** | 冷面狙神 | Smoggy |
| **DNTP** | 夜露老六 | 所有喜欢绕后的玩家 |
| **DNFJ** | 不死鸟莽夫 | 所有 Rush B 玩家 |
| **DNFP** | 炸鱼专家 | Radiant 开小号 |
| **CSTJ** | 世一烟 | Nobody |
| **CSTP** | 摄像头狂魔 | 所有信息位玩家 |
| **CSFJ** | 奶妈贤者 | 所有喜欢玩奶的玩家 |
| **CSFP** | 皮蛋玩家 | 所有喜欢整活的玩家 |
| **CNTJ** | 铁壁哨卫 | 所有防守狂魔 |
| **CNTP** | 陷阱大师 | 所有老六玩家 |
| **CNFJ** | 炼狱指挥 | 所有指挥型玩家 |
| **CNFP** | 串子头子 | 蛋总 & 瓦圈全体串子 |

## 🚀 快速开始

### 本地运行

直接在浏览器中打开 `index.html` 即可：

```bash
# macOS
open index.html

# 或者使用任意本地服务器
python -m http.server 8080
# 访问 http://localhost:8080
```

### 在线部署

支持部署到任何静态网站托管平台：

- Vercel / Netlify
- GitHub Pages
- Cloudflare Pages
- 或者任何支持静态文件的服务器

## 📁 项目结构

```
VCTI/
├── index.html          # 主页面
├── styles.css          # 样式文件 (Claude Design System)
├── app.js              # 应用逻辑
├── data/               # VALORANT 数据资料
│   ├── valorant_full_guide_zh-CN.md
│   ├── valorant_full_guide.md
│   ├── valorant_esports_vlr.md
│   ├── valorant_esports_vlrgg.md
│   ├── 梗.md
│   └── 术语.md
├── scripts/            # 数据导出脚本
│   ├── export_valorant.py
│   ├── export_vlr.py
│   └── export_vlrgg.py
├── docs/               # 文档
│   ├── DESIGN.md       # Claude 设计系统
│   └── VCTI_16型人格测试.md
└── README.md
```

## 🎨 设计系统

项目采用 **Claude Design System** 设计语言：

- **温暖奶油色画布** (#faf9f5) - 替代冰冷的纯白
- **珊瑚色主色调** (#cc785c) - 用于按钮、强调元素
- **深色海军蓝卡片** (#181715) - 用于展示详情内容
- **Cormorant Garamond** - 优雅的衬线字体（替代 Copernicus）
- **Inter** - 人文主义无衬线字体用于正文

详细设计规范请参考 [DESIGN.md](docs/DESIGN.md)。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📝 致谢

- 感谢 VALORANT 中国电竞社区提供的各种名梗和名场面
- 感谢康康、表哥、Smoggy 等选手带来的精彩比赛
- 感谢 Claude Design System 设计规范

## 📄 许可证

[MIT License](LICENSE)

---

> 🎮 东京盛夏开了花，仁川雨夜结了果
