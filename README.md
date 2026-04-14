# astrbot\_plugin\_bilibili\_bot

B站 AI Bot 插件 for [AstrBot](https://github.com/AstrBotDevs/AstrBot) — 让你的 AI 角色在 B 站评论区"活"起来。

## ✨ 功能

* **评论自动回复** — 轮询评论通知，自动生成 AI 回复
* **好感度系统** — 陌生人 → 粉丝 → 熟人 → 好友 → 主人，不同等级不同语气；辱骂自动拉黑
* **用户画像** — 词条式档案：昵称、喜好、个人信息、标签、印象
* **语义记忆** — Embedding 向量化 + 余弦相似度检索，支持记忆压缩、永久记忆
* **心情系统** — 每日随机心情 + 节日彩蛋（含农历）
* **性格演化** — 每日反思互动经历，渐进式性格成长
* **视频上下文** — 自动获取视频信息，支持视觉模型分析封面
* **图片识别** — 评论中的图片自动识别内容
* **@Bot 回复** — 轮询 B站 `@消息`，有人@你时可直接回复
* **主动看视频** — 自动刷B站、评价视频、点赞/投币/收藏/关注/评论
* **自动发动态** — 定时发布动态，支持 AI 生成配图
* **Web 管理面板** — 浏览器管理记忆、好感度、动态日志等
* **LLM 熔断保护** — 单条重试 3 次放弃，全局连续 5 次失败冷却 5 分钟
* **基础防注入** — 对可疑 prompt 注入内容做检测、记录和安全包裹
* **Cookie 自动刷新** — 定期检查 + 自动刷新，支持扫码登录
* **拉黑管理** — 手动/自动拉黑，黑名单用户不调 LLM 不花钱

## 🔗 QQ ↔ B站 记忆互通

绑定后，两个平台的记忆会自动共享：

1. 在 QQ 发送 `/bili绑定 <B站UID>` 完成绑定
2. QQ 聊天中提到 B站 相关话题时，B站侧的永久记忆会自动注入
3. QQ 的对话记录会存入记忆池（带 embedding），B站回复时通过语义检索按需调取相关的 QQ 记忆

## 📦 安装

在 AstrBot WebUI 的插件市场搜索 `bilibili\\\_bot`，点击安装即可。

或手动安装：

```bash
cd AstrBot/data/plugins
git clone https://github.com/chenluQwQ/astrbot\\\_plugin\\\_bilibili\\\_bot
```

## ⚙️ 配置

安装后在 WebUI 插件配置页面填写：

|配置项|必填|说明|
|-|-|-|
|`LLM\\\_PROVIDER\\\_ID`|✅|选择用于回复的 LLM 模型|
|`SESSDATA`|自动|B站 Cookie（`/bili登录` 扫码自动填入）|
|`BILI\\\_JCT`|自动|B站 CSRF Token（扫码自动填入）|
|`DEDE\\\_USER\\\_ID`|自动|Bot 的 B站 UID（扫码自动填入）|
|`REFRESH\\\_TOKEN`|自动|Cookie 自动刷新用（扫码自动填入）|
|`OWNER\\\_MID`|推荐|主人的 B站 UID（好感度特殊处理）|
|`OWNER\\\_NAME`|推荐|主人名称（用于 prompt）|
|`EMBED\\\_API\\\_KEY`|可选|Embedding API 密钥（记忆向量化用）|
|`EMBED\\\_API\\\_BASE`|可选|Embedding API 地址，默认 SiliconFlow|
|`EMBED\\\_MODEL`|可选|Embedding 模型名，默认 `BAAI/bge-m3`|
|`VIDEO\\\_VISION\\\_PROVIDER\\\_ID`|可选|视频分析走 AstrBot 模型提供商，留空则走独立 API|
|`VIDEO\\\_VISION\\\_API\\\_KEY`|可选|视频分析视觉模型 API Key|
|`IMAGE\\\_VISION\\\_PROVIDER\\\_ID`|可选|图片识别走 AstrBot 模型提供商，留空则走独立 API|
|`IMAGE\\\_VISION\\\_API\\\_KEY`|可选|图片识别视觉模型 API Key|
|`IMAGE\\\_GEN\\\_API\\\_KEY`|可选|图片生成 API Key（动态配图用）|
|`IMAGE\\\_GEN\\\_MODEL`|可选|图片生成模型，默认 `black-forest-labs/flux-schnell`|
|`EVOLVE\\\_MAX\\\_RETRIES`|可选|性格演化失败后的最大重试次数，默认 2|
|`ENABLE\\\_DYNAMIC`|可选|启用自动发动态|
|`DYNAMIC\\\_TIMES\\\_COUNT`|可选|每天触发几次动态发布|
|`DYNAMIC\\\_DAILY\\\_COUNT`|可选|每天最多发几条动态|
|`ENABLE\\\_WEB\\\_PANEL`|可选|启用 Web 管理面板|
|`WEB\\\_PANEL\\\_PORT`|可选|Web 面板端口，默认 5001|
|`WEB\\\_PANEL\\\_PASSWORD`|可选|Web 面板密码，默认 admin123|

> 💡 Cookie 获取方式：发送 `/bili登录` 扫码即可，登录后 Cookie 会自动定期刷新。
>
> 💡 视觉模型留空时，视频分析回退为纯文本 LLM 分析，图片识别则跳过。

## 🎮 命令

|命令|说明|
|-|-|
|`/bili登录`|扫码登录 B站（扫码后发 `/bili确认`）|
|`/bili确认`|确认扫码结果|
|`/bili状态`|查看运行状态|
|`/bili启动`|启动 Bot|
|`/bili停止`|停止 Bot|
|`/bili开关 <功能>`|切换功能开关|
|`/bili刷新`|手动刷新 Cookie|
|`/bili记忆 <关键词>`|语义搜索记忆|
|`/bili好感 \\\[UID]`|查看好感度排行/查询|
|`/bili拉黑 <UID>`|手动拉黑用户|
|`/bili解黑 <UID>`|解除拉黑|
|`/bili黑名单`|查看黑名单|
|`/bili性格`|查看性格演化|
|`/bili日志`|今日视频/评论日志|
|`/bili永久记忆`|查看/删除永久记忆|
|`/bili动态`|手动发动态|
|`/bili动态日志`|动态记录|
|`/bili绑定 <UID>`|绑定 QQ 与 B站 UID（记忆互通）|
|`/bili解绑`|解除绑定|
|`/bili帮助`|查看帮助|

## 🏗️ 好感度等级

|等级|分数|语气风格|
|-|-|-|
|🌙 陌生人|0-10|礼貌简洁|
|👋 粉丝|11-30|友好温和|
|😊 熟人|31-50|轻松自然|
|✨ 好友|51+|亲近真诚|
|💖 主人|特殊|撒娇宠溺|
|🖤 厌恶|≤-10|极简冷淡|

> 好感度 ≤ -30 或连续辱骂 5 次自动拉黑。

## 🌐 Web 管理面板

启用 `ENABLE\\\_WEB\\\_PANEL` 后访问 `http://服务器IP:5001`

功能：

* 📊 状态概览
* 🧠 记忆管理（分页/删除）
* 💛 好感度排行
* 💎 永久记忆管理
* 🌱 性格演化查看
* 🎯 主动行为触发日志 API（`/api/proactive/log`）
* 📝 动态日志
* 📦 数据导出

## 📁 数据存储

插件数据存储在 `data/plugin\\\_data/astrbot\\\_plugin\\\_bilibili\\\_bot/` 目录下，更新插件不会丢失数据。

## 🔗 相关

* [AstrBot 文档](https://docs.astrbot.app/)
* [问题反馈](https://github.com/chenluQwQ/astrbot_plugin_bilibili_ai_bot/issues)

## 📄 License

MIT
