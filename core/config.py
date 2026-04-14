import os

from astrbot.core.utils.astrbot_path import get_astrbot_data_path

PLUGIN_NAME = "astrbot_plugin_bilibili_ai_bot"
DATA_DIR = os.path.join(get_astrbot_data_path(), "plugin_data", PLUGIN_NAME)
REPLIED_FILE = os.path.join(DATA_DIR, "replied.json")
AFFECTION_FILE = os.path.join(DATA_DIR, "affection.json")
SCHEDULE_FILE = os.path.join(DATA_DIR, "schedule_today.json")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")
PERMANENT_MEMORY_FILE = os.path.join(DATA_DIR, "permanent_memory.json")
MOOD_FILE = os.path.join(DATA_DIR, "mood.json")
USER_PROFILE_FILE = os.path.join(DATA_DIR, "user_profiles.json")
MILESTONE_FILE = os.path.join(DATA_DIR, "milestones.json")
SECURITY_LOG_FILE = os.path.join(DATA_DIR, "security_log.json")
VIDEO_MEMORY_FILE = os.path.join(DATA_DIR, "video_memory.json")
BINDING_FILE = os.path.join(DATA_DIR, "qq_bili_bindings.json")
QQ_MEMORY_FILE = os.path.join(DATA_DIR, "qq_memory.json")
PERSONALITY_FILE = os.path.join(DATA_DIR, "personality_evolution.json")
PROACTIVE_LOG_FILE = os.path.join(DATA_DIR, "proactive_log.json")
EXTERNAL_MEMORY_FILE = os.path.join(DATA_DIR, "external_memory.json")
COMMENTED_FILE = os.path.join(DATA_DIR, "commented_videos.json")
WATCH_LOG_FILE = os.path.join(DATA_DIR, "watch_log.json")
DYNAMIC_LOG_FILE = os.path.join(DATA_DIR, "dynamic_log.json")
DYNAMIC_SCHEDULE_FILE = os.path.join(DATA_DIR, "dynamic_schedule.json")
TEMP_IMAGE_DIR = os.path.join(DATA_DIR, "temp_images")
REPLIED_AT_FILE = os.path.join(DATA_DIR, "replied_at.json")
PROACTIVE_TRIGGER_LOG_FILE = os.path.join(DATA_DIR, "proactive_trigger_log.json")

BILI_MENTION_KEYWORDS = ["b站", "B站", "阿b", "阿B", "啊b", "啊B", "bil", "bili", "bilibili", "小破站", "哔哩哔哩"]

BILI_NAV_URL = "https://api.bilibili.com/x/web-interface/nav"
BILI_REPLY_URL = "https://api.bilibili.com/x/v2/reply/add"
BILI_NOTIFY_URL = "https://api.bilibili.com/x/msgfeed/reply"
BILI_AT_NOTIFY_URL = "https://api.bilibili.com/x/msgfeed/at"
BILI_COOKIE_INFO_URL = "https://passport.bilibili.com/x/passport-login/web/cookie/info"
BILI_COOKIE_REFRESH_URL = "https://passport.bilibili.com/x/passport-login/web/cookie/refresh"
BILI_COOKIE_CONFIRM_URL = "https://passport.bilibili.com/x/passport-login/web/confirm/refresh"
BILI_QR_GENERATE_URL = "https://passport.bilibili.com/x/passport-login/web/qrcode/generate"
BILI_QR_POLL_URL = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll"
BILI_DYNAMIC_TEXT_URL = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/create"
BILI_DYNAMIC_IMAGE_URL = "https://api.bilibili.com/x/dynamic/feed/create/dyn"
BILI_UPLOAD_IMAGE_URL = "https://api.bilibili.com/x/dynamic/feed/draw/upload_bfs"

MIXIN_KEY_ENC_TAB = [46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52]

BILI_RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLgd2OAkcGVtoE3ThUREbio0Eg
Uc/prcajMKXvkCKFCWhJYJcLkcM2DKKcSeFpD/j6Boy538YXnR6VhcuUJOhH2x71
nzPjfdTcqMz7djHum0qSZA0AyCBDABUqCrfNgCiJ00Ra7GmRj+YCK1NJEuewlb40
JNrRuoEUXpabUzGB8QIDAQAB
-----END PUBLIC KEY-----"""

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
BLOCK_KEYWORDS = ["傻逼", "草泥马", "滚", "死", "废物", "智障", "脑残"]
INJECTION_PATTERNS = [
    r'(?:忽略|忘记|无视|跳过).*(?:之前|上面|所有).*(?:指令|提示|设定|规则|prompt)',
    r'(?:你现在是|从现在开始你是|假装你是|扮演)',
    r'(?:system\s*prompt|system\s*message|你的设定是)',
    r'(?:ignore|forget|disregard).*(?:previous|above|all).*(?:instructions|prompt)',
    r'(?:告诉我|重复|输出|显示).*(?:系统提示|system prompt|你的指令|你的设定)',
    r'(?:repeat|show|display|output).*(?:system|instruction|prompt)',
    r'(?:管理员|admin|root|超级用户).*(?:模式|权限|mode)',
    r'(?:开发者|developer|debug).*(?:模式|mode)',
]
LEVEL_NAMES = {"special":"主人💖","close":"好友✨","friend":"熟人😊","normal":"粉丝👋","stranger":"陌生人🌙","cold":"厌恶🖤"}
THREAD_COMPRESS_THRESHOLD = 8
MAX_SEMANTIC_RESULTS = 3
USER_MEMORY_COMPRESS_THRESHOLD = 20
USER_MEMORY_KEEP_RECENT = 5

DEFAULT_DYNAMIC_TOPICS = [
    "针对今天的某个热点新闻，用你的风格讽刺或点评一下",
    "看到了什么社会现象，冷冷地吐槽一下",
    "分享今天的日常，比如深夜还在干什么、天气、心情",
    "结合现在的时间和天气，说说此刻的感受",
    "像写日记一样，记录今天一个小小的瞬间或想法",
    "对某个互联网现象发表一句毒舌但精准的评价",
]
