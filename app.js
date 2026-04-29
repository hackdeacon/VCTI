/* ===================================
   VCTI - VALORANT Personality Test
   Application Logic
   =================================== */

// Questions Data
const questions = [
    {
        text: "开局队友说 eco，你会？",
        dimension: 0,
        options: [
            { text: "eco 个屁，强起干拉！死了算球！", value: "D" },
            { text: "听队友的，eco 攒钱，下把起全甲", value: "C" }
        ]
    },
    {
        text: "队友问「A 大有人吗？」，你会？",
        dimension: 1,
        options: [
            { text: "打开摄像头放无人机，精确报点：A 大一个，残血！拿的戍卫！", value: "S" },
            { text: "「我感觉有人...吧？刚才好像有脚步声」", value: "N" }
        ]
    },
    {
        text: "队友说「我没钱了，发把枪」，你会？",
        dimension: 2,
        options: [
            { text: "二话不说 B 键已按，直接发幻影，不够再给甲", value: "T" },
            { text: "「我也没钱，你自己捡枪去」", value: "F" }
        ]
    },
    {
        text: "赛点局队友连续白给输掉，你会？",
        dimension: 3,
        options: [
            { text: "当场红温，开麦指挥：你会不会玩？", value: "J" },
            { text: "笑死，你这波太菜了，下把加油", value: "P" }
        ]
    },
    {
        text: "打排位进点，你更喜欢？",
        dimension: 0,
        options: [
            { text: "永远第一个冲，不拿首杀浑身难受", value: "D" },
            { text: "跟在队友后面补枪，KDA 比什么都重要", value: "C" }
        ]
    },
    {
        text: "1v3 残局，你会？",
        dimension: 1,
        options: [
            { text: "仔细听脚步判位，规划路线逐个击破", value: "S" },
            { text: "直接干拉，凭感觉和枪法硬刚", value: "N" }
        ]
    },
    {
        text: "大招好了，你会？",
        dimension: 2,
        options: [
            { text: "留着打配合，等队友道具一起上", value: "T" },
            { text: "直接放了！我今天就要拿五杀！", value: "F" }
        ]
    },
    {
        text: "排位撞车主播，你会？",
        dimension: 3,
        options: [
            { text: "认真打，赢了能上集锦，输了要被喷", value: "J" },
            { text: "整活走起！节目效果最重要", value: "P" }
        ]
    }
];

// Personality Data
const personalities = {
    "DSTJ": {
        name: "霓虹町战神",
        agent: "捷风 Jett · 雷兹 Raze",
        player: "ZmjjKK 康康",
        badge: "决斗位 · 战场统治者",
        features: [
            "永远第一个干拉进点，不拿 ACE 不罢休",
            "摄像头永远架在最刁钻的角度",
            "自己 eco 也要给队友发戍卫",
            "胜负欲极强，输了当场红温"
        ],
        quote: "你老子是冠军，他是什么？",
        quoteAuthor: "康康",
        rank: "Radiant / 职业赛场",
        weakness: "遇到表哥的广西步直接破防红温"
    },
    "DSTP": {
        name: "康神开播啦",
        agent: "盖可 Gekko · 不死鸟 Phoenix",
        player: "撒娇模式的康康",
        badge: "反差萌 · 贴膜大师",
        features: [
            "冲的时候是世一康，下播立刻变撒娇怪",
            "直播贴膜比打职业还认真专注",
            "「没胖我造！我真比以前瘦了！」",
            "女友在旁边时红温开关自动失效"
        ],
        quote: "不许再说我胖了！再说我真的要急眼了！",
        quoteAuthor: "康康",
        rank: "钻石 Diamond / 超凡 Immortal",
        weakness: "女友的一句话比什么都管用"
    },
    "DSFJ": {
        name: "广西步传人",
        agent: "夜露 Yoru · 霓虹 Neon",
        player: "广西表哥",
        badge: "身法大师 · 绷住王者",
        features: [
            "无规则左右横拉 + 不规则急停 + 预瞄提前枪",
            "魔性广西口音：「你们这些颠公颠婆」",
            "看到康康撒娇也能全程绷住不笑",
            "道歉信写得比假赛记录还干净"
        ],
        quote: "康神开播了？真的假的？我靠真开播了",
        quoteAuthor: "表哥",
        rank: "亚服第一 Rank 1",
        weakness: "世一康的怒火和弹幕节奏"
    },
    "DSFP": {
        name: "ECO 局战神",
        agent: "芮娜 Reyna · 壹决 Iso",
        player: "所有喜欢强起的玩家",
        badge: "强起专业户 · 干拉艺术家",
        features: [
            "没钱？强起！没甲？干拉！就是干！",
            "戍卫手枪也能 1v5，就是这么自信",
            "赢了血赚，输了不亏，大不了下把",
            "永远不相信拳头的经济系统"
        ],
        quote: "eco eco？eco 个屁，强起干他们！",
        quoteAuthor: "瓦洛兰特玩家",
        rank: "白银 Silver / 黄金 Gold",
        weakness: "遇到对面全起奥丁直接集体白给"
    },
    "DNTJ": {
        name: "冷面狙神",
        agent: "尚勃勒 Chamber",
        player: "Smoggy",
        badge: "人形自走挂 · 情绪稳定器",
        features: [
            "全场面无表情，康康红温到爆炸他也不动",
            "大狙架一个角度能架一整局",
            "残局 1v3 拿下赛点连嘴角都不带动一下",
            "情绪波动为 0 的人形自走挂"
        ],
        quote: "（沉默，然后一枪爆头）",
        quoteAuthor: "Smoggy",
        rank: "职业赛场 VCT Masters",
        weakness: "几乎没有，除非网线被拔"
    },
    "DNTP": {
        name: "夜露老六",
        agent: "夜露 Yoru · 幽影 Omen",
        player: "所有喜欢绕后的玩家",
        badge: "绕后专家 · 迷路大师",
        features: [
            "「我去绕后了，你们正面顶住」",
            "然后绕了整整一分钟才出现",
            "队友全死了他才刚到包点",
            "主打一个出其不意，其实是迷路了"
        ],
        quote: "我在路上了，马上到！（还在匪家）",
        quoteAuthor: "每一个夜露玩家",
        rank: "青铜 Bronze / 白银 Silver",
        weakness: "对面也有一个老六在等他"
    },
    "DNFJ": {
        name: "不死鸟莽夫",
        agent: "不死鸟 Phoenix · 霓虹 Neon",
        player: "所有 Rush B 玩家",
        badge: "冲锋敢死队 · 永远向前",
        features: [
            "3 2 1 冲！永远在冲的路上",
            "火墙封自己路也要冲，死了复活接着冲",
            "「怕什么？我有大！怕个球！」",
            "不是在冲，就是在冲的路上"
        ],
        quote: "Rush A！别问，问就是干！",
        quoteAuthor: "不死鸟玩家",
        rank: "黄金 Gold / 铂金 Platinum",
        weakness: "对面炼狱一个大直接蒸发全队"
    },
    "DNFP": {
        name: "炸鱼专家",
        agent: "捷风 Jett · 芮娜 Reyna",
        player: "Radiant 开小号",
        badge: "鱼塘霸主 · 手感玄学",
        features: [
            "「这把随便赢，我 carry，躺好」",
            "然后 1-5 开局，手感冰冷",
            "「没事，看我发力，认真了」",
            "「今天手感不好，明天再来」"
        ],
        quote: "要不是手感不好，这把我早就五杀了",
        quoteAuthor: "Radiant 炸鱼玩家",
        rank: "青铜 - 钻石（通吃）",
        weakness: "遇到对面也是炸鱼的 Radiant"
    },
    "CSTJ": {
        name: "世一烟",
        agent: "星礈 Astra · 幽影 Omen · 海神 Harbor",
        player: "Nobody",
        badge: "控场大师 · 隐形功臣",
        features: [
            "烟位的神，每一个烟都恰到好处",
            "康康的兰花草，有一半是他的烟撑起来的",
            "全场默默付出，数据不起眼但赢比赛的关键",
            "永远在最关键的位置给出最关键的道具"
        ],
        quote: "烟封好了，上吧兄弟们",
        quoteAuthor: "Nobody",
        rank: "高端局 / 职业赛场",
        weakness: "队友干拉根本不看你给的烟"
    },
    "CSTP": {
        name: "摄像头狂魔",
        agent: "零 Cypher · 奇乐 Killjoy · 猎枭 Sova",
        player: "所有信息位玩家",
        badge: "情报专家 · 监控狂魔",
        features: [
            "买摄像头比买枪还积极，道具拉满",
            "一整局都在切摄像头看，比看老婆还认真",
            "「A 大一个，B 小两个，中路三个...哎我怎么死了？」",
            "知道所有人在哪，就是不知道自己怎么死的"
        ],
        quote: "我看到他了！...哎我怎么没了？",
        quoteAuthor: "零玩家",
        rank: "铂金 Platinum / 钻石 Diamond",
        weakness: "看摄像头太入迷被敌人刀了"
    },
    "CSFJ": {
        name: "奶妈贤者",
        agent: "贤者 Sage · 斯凯 Skye · 暮蝶 Clove",
        player: "所有喜欢玩奶的玩家",
        badge: "团队守护者 · 复活天使",
        features: [
            "队友的血比自己的命还重要，奶量拉满",
            "「别死别死！坚持住！我来奶你！」",
            "自己大残也要先救队友，舍己为人",
            "复活技能永远留给最菜的那个队友"
        ],
        quote: "坚持住！我来复活你！马上到！",
        quoteAuthor: "贤者玩家",
        rank: "全段位通吃",
        weakness: "队友刚被复活就又冲出去送了"
    },
    "CSFP": {
        name: "皮蛋玩家",
        agent: "盖可 Gekko",
        player: "所有喜欢整活的玩家",
        badge: "宠物大师 · 整活专家",
        features: [
            "这游戏难道不是召唤宠物的吗？",
            "皮蛋冲！丢丢冲！嗨宝冲！鲨鲨冲！全军出击！",
            "自己死了没关系，宠物必须全部放出去",
            "主打一个宠物比人还厉害"
        ],
        quote: "皮蛋！给我上！干掉他们！",
        quoteAuthor: "盖可玩家",
        rank: "青铜 Bronze / 铂金 Platinum",
        weakness: "宠物全放出去了，自己拿手枪面对五个敌人"
    },
    "CNTJ": {
        name: "铁壁哨卫",
        agent: "奇乐 Killjoy · 钢锁 Deadlock · 维斯 Vyse",
        player: "所有防守狂魔",
        badge: "包点守护者 · 钉子户",
        features: [
            "这个包点我说了算，天王老子来了也不行",
            "炮台、地雷、陷阱、绊线，安排得明明白白",
            "一整局都在守包点，从来没挪过窝",
            "进攻方？那是什么东西？能吃吗？"
        ],
        quote: "有我在，这个包点他们别想碰一下",
        quoteAuthor: "奇乐玩家",
        rank: "钻石 Diamond / 超凡 Immortal",
        weakness: "队友都去打另一个包点了他还在守"
    },
    "CNTP": {
        name: "陷阱大师",
        agent: "零 Cypher · 钢锁 Deadlock · 奇乐 Killjoy",
        player: "所有老六玩家",
        badge: "转角遇到爱 · 陷阱艺术家",
        features: [
            "每一个拐角都有惊喜，转角遇到爱",
            "绊线、摄像头、陷阱，三位一体",
            "「哎？怎么又踩到我的绊线了？真巧」",
            "一整局没杀人，全靠陷阱拿击杀"
        ],
        quote: "我就知道你会走这里，等你很久了",
        quoteAuthor: "老六玩家",
        rank: "黄金 Gold / 铂金 Platinum",
        weakness: "对面根本不走那条路，白放了"
    },
    "CNFJ": {
        name: "炼狱指挥",
        agent: "炼狱 Brimstone · 铁臂 Breach",
        player: "所有指挥型玩家",
        badge: "战场指挥官 · 音量王者",
        features: [
            "「听我指挥！A 大打！给烟给闪给火！」",
            "全场嗓门最大的那个，激情指挥",
            "道具落点精确到厘米，职业级计算",
            "输了全是队友的锅，赢了全是我指挥得好"
        ],
        quote: "都听我的！这把稳赢！不听我的必输！",
        quoteAuthor: "炼狱玩家",
        rank: "铂金 Platinum / 钻石 Diamond",
        weakness: "队友根本不听指挥，各玩各的"
    },
    "CNFP": {
        name: "串子头子",
        agent: "所有特工",
        player: "蛋总 & 瓦圈全体串子",
        badge: "节奏发动机 · 弹幕大师",
        features: [
            "游戏可以输，节奏必须带起来",
            "「兄弟们！康神开播啦！速去！」",
            "霓虹町事变的幕后推手和见证人",
            "主打一个看热闹不嫌事大"
        ],
        quote: "kskblzdjd（康神开播了真的假的）",
        quoteAuthor: "串子",
        rank: "直播间弹幕大神",
        weakness: "被主播禁言 365 天套餐"
    }
};

// Game State
let currentQuestionIndex = 0;
let dimensions = { D: 0, C: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };
let currentType = "";

/* ===================================
   Page Navigation
   =================================== */

function showPage(pageId) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById(pageId).classList.add('active');
    window.scrollTo(0, 0);
}

/* ===================================
   Test Flow
   =================================== */

function startTest() {
    currentQuestionIndex = 0;
    dimensions = { D: 0, C: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 };
    currentType = "";
    showPage('test-page');
    setTimeout(showQuestion, 300);
}

function showQuestion() {
    const q = questions[currentQuestionIndex];
    const qNum = String(currentQuestionIndex + 1).padStart(2, '0');
    document.getElementById('current-num').textContent = qNum;
    document.getElementById('progress-bar-fill').style.width = ((currentQuestionIndex + 1) / questions.length * 100) + '%';

    document.getElementById('question-text').textContent = q.text;

    const container = document.getElementById('options-list');
    container.innerHTML = '';

    q.options.forEach((opt, index) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.innerHTML = `<span class="option-letter">${String.fromCharCode(65 + index)}.</span>${opt.text}`;
        btn.onclick = () => selectOption(opt.value);
        container.appendChild(btn);

        // Stagger animation
        btn.style.opacity = '0';
        btn.style.transform = 'translateX(-10px)';
        setTimeout(() => {
            btn.style.transition = 'all 0.3s ease';
            btn.style.opacity = '1';
            btn.style.transform = 'translateX(0)';
        }, index * 100);
    });

    updateCurrentTypePreview();
}

function selectOption(value) {
    dimensions[value]++;

    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        setTimeout(showQuestion, 400);
    } else {
        setTimeout(showResult, 500);
    }
}

function updateCurrentTypePreview() {
    let type = '';
    type += dimensions.D > dimensions.C ? 'D' : (dimensions.C > dimensions.D ? 'C' : '-');
    type += dimensions.S > dimensions.N ? 'S' : (dimensions.N > dimensions.S ? 'N' : '-');
    type += dimensions.T > dimensions.F ? 'T' : (dimensions.F > dimensions.T ? 'F' : '-');
    type += dimensions.J > dimensions.P ? 'J' : (dimensions.P > dimensions.J ? 'P' : '-');
    document.getElementById('current-type-preview').textContent = type;
}

function calculateType() {
    let type = '';
    type += dimensions.D > dimensions.C ? 'D' : 'C';
    type += dimensions.S > dimensions.N ? 'S' : 'N';
    type += dimensions.T > dimensions.F ? 'T' : 'F';
    type += dimensions.J > dimensions.P ? 'J' : 'P';
    return type;
}

function showResult() {
    const type = calculateType();
    const p = personalities[type];

    showPage('result-page');

    document.getElementById('result-type').textContent = type;
    document.getElementById('result-name').textContent = p.name;
    document.getElementById('result-badge').textContent = p.badge;
    document.getElementById('result-agent').textContent = p.agent;
    document.getElementById('result-player').textContent = p.player;
    document.getElementById('result-quote').textContent = `「${p.quote}」`;
    document.getElementById('result-quote-author').textContent = p.quoteAuthor;
    document.getElementById('result-rank').textContent = p.rank;
    document.getElementById('result-weakness').textContent = p.weakness;

    const featuresList = document.getElementById('result-features-list');
    featuresList.innerHTML = p.features.map(f => `
        <li class="feature-item">
            <span class="feature-bullet"></span>
            ${f}
        </li>
    `).join('');

    // Dimension breakdown
    const breakdownGrid = document.getElementById('breakdown-grid');
    const dimPairs = [
        { left: 'D', right: 'C', leftLabel: '冲锋型', rightLabel: '稳健型', desc: '决定了你在战场上的进攻倾向' },
        { left: 'S', right: 'N', leftLabel: '侦察型', rightLabel: '直觉型', desc: '决定了你获取信息的方式' },
        { left: 'T', right: 'F', leftLabel: '工具型', rightLabel: '核心型', desc: '决定了你在团队中的角色定位' },
        { left: 'J', right: 'P', leftLabel: '竞技型', rightLabel: '娱乐型', desc: '决定了你对待游戏的心态' }
    ];

    breakdownGrid.innerHTML = dimPairs.map(pair => {
        const total = dimensions[pair.left] + dimensions[pair.right];
        const leftPercent = Math.round((dimensions[pair.left] / total) * 100);
        const winner = dimensions[pair.left] > dimensions[pair.right] ? pair.left : pair.right;

        return `
            <div class="breakdown-item">
                <div class="breakdown-labels">
                    <span class="breakdown-label" style="color: ${winner === pair.left ? 'var(--primary)' : 'var(--muted)'}">${pair.left} · ${pair.leftLabel}</span>
                    <span class="breakdown-vs">vs</span>
                    <span class="breakdown-label" style="color: ${winner === pair.right ? 'var(--accent-teal)' : 'var(--muted)'}">${pair.rightLabel} · ${pair.right}</span>
                </div>
                <div class="breakdown-bar">
                    <div class="breakdown-bar-fill" style="width: ${leftPercent}%;"></div>
                </div>
                <div class="breakdown-desc">${pair.desc}</div>
            </div>
        `;
    }).join('');

    // Animate bars after rendering
    setTimeout(() => {
        document.querySelectorAll('.breakdown-bar-fill').forEach(bar => {
            bar.style.transition = 'width 1s cubic-bezier(0.4, 0, 0.2, 1)';
        });
    }, 100);
}

/* ===================================
   Actions
   =================================== */

function shareResult() {
    const type = calculateType();
    const p = personalities[type];
    const text = `🎮 我的 VCTI 无畏契约人格测试结果：${type} - ${p.name}！\n快来测测你的 VALORANT 人格类型！\n${window.location.href}`;

    if (navigator.share) {
        navigator.share({
            title: 'VCTI - VALORANT 人格测试',
            text: text,
            url: window.location.href
        });
    } else {
        navigator.clipboard.writeText(text).then(() => {
            alert('✓ 结果已复制到剪贴板！');
        });
    }
}

function restartTest() {
    showPage('home-page');
}

/* ===================================
   Initialize on Load
   =================================== */

document.addEventListener('DOMContentLoaded', () => {
    // Any initialization code here
});
