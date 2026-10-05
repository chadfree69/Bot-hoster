# ═══════════════════════════════════════════════════════════════════════════════
#                    𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘈𝘉𝘉𝘜 𝘝6 👑 - ULTIMATE MULTI-BOT SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

import os, sys, io, time, json, random, asyncio, logging, requests, pytz, gc, re, traceback, atexit
import socket as _sock
from datetime import datetime, timedelta
from urllib.parse import quote
from collections import deque, OrderedDict, defaultdict
from typing import Optional, Dict, List, Set, Any, Callable, Tuple

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    ReactionTypeEmoji, ChatAdministratorRights, Bot, ChatPermissions
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters
)
from telegram.constants import ParseMode, ChatType
from telegram.error import RetryAfter, BadRequest, NetworkError, TimedOut, TelegramError

try:
    from gtts import gTTS
    HAS_GTTS = True
except ImportError:
    HAS_GTTS = False

INSTANCE_ID = os.environ.get("INSTANCE_ID", "0")
LOCK_PORT = int(os.environ.get("LOCK_PORT", str(47832 + int(INSTANCE_ID))))
DATA_SUFFIX = f"_inst{INSTANCE_ID}" if INSTANCE_ID != "0" else ""

_instance_lock: Optional[_sock.socket] = None

def _acquire_instance_lock(port: int) -> bool:
    global _instance_lock
    try:
        s = _sock.socket(_sock.AF_INET, _sock.SOCK_STREAM)
        s.setsockopt(_sock.SOL_SOCKET, _sock.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", port))
        s.listen(1)
        _instance_lock = s
        return True
    except OSError:
        return False

def _release_instance_lock():
    global _instance_lock
    if _instance_lock:
        try: _instance_lock.close()
        except Exception: pass
        _instance_lock = None

atexit.register(_release_instance_lock)
print(f"[INSTANCE] ID={INSTANCE_ID} | LOCK_PORT={LOCK_PORT}")

BOT_TOKENS = ["8642798207:AAHuS_G_KFS920MDP5FGCp1FRLfrjf2SpCo"
"8924007320:AAGK5sFgFuQYvXb_9y2Zmq6V_ZlxAXqM48Q"
"8911900835:AAHOfu7cKpUr00tVO6d4rGd-Q_3daUvtSsU "
"8683503974:AAEC_nr_5WKJns8LwmlMzXYVS0d7CUrDqjQ"
"8777337275:AAEmkISvG1Bq4k70JjE9tLoDRNpPICE0nAw"
"8908597093:AAG7YlIyca7eFkTrR_4htTmCNEoYYeXXu10 "
"8394508233:AAGFnuxVMf0Lktee1U1mEwG96Jqi-WSyQOI"
"8929929150:AAElBafersfa3QGtSfNrcwxnFUk2NVdoI9c"
"8923076129:AAHNvb0vxXkcFehUg0TPN45E6Kc5DgydhrI"
"8685987238:AAHigCyqWtQ_wjLzxUu09p3c3eZUHujbwu4"
"8890698834:AAGLUk6Ov84gK_f7bZjhd7CTHkmUNLQOJ7I"
"8421460820:AAGISaCrJy4CQi8J3B8b3mBVmDTo1ZMYOaA"
"8968018775:AAGGi7eMYTxfSKSMnB8kz6FOjoFlhEvqqRM"
"8963335185:AAHkXqfJJQlMsFBwK3bJbEtquejHw4P8kgI"
"8560670091:AAFoS2GPZE25S2WXx4VXvFJIdZACX6zEOAs"
"8849258012:AAEh0k-ayRfx8QpyXlVg6vkYSANl6BNdsaA"
"8958220055:AAGk7YLRl9vq2-UYkWsXhU3xjHlsD2Ug9s4"
"8864880255:AAGe0wdw6iYcvDO3kAEg4jys8tc7SzJd3jI"
"8823359778:AAGLRVk9ykMDoBE0ez2c3VdiqfOWuB6doYw"
"8685396757:AAGO4ffbRUFwdUL0lHIe9V-_XGXu-nnH_Kk"
    
]

OWNER_BOT_USERNAMES = {"@Dominationv1bot"
    
}

WORTHY_BOTS = list(OWNER_BOT_USERNAMES)
OWNER_ID = 8410820416
SUDO_IDS = [8410820416]
CMD_PREFIXES = ["!", ".", "/", "-", "?", "*", "$", "#", "&", "_"]

HELP_PHOTO_URL = "https://cdn.pfps.gg/pfps/6747-leon-resident-evil.png"
GAMEOVER_PHOTO_URL = "https://img.magnific.com/premium-photo/black-background-with-game-text-overlay-typo-minimalism_955080-4949.jpg?semt=ais_hybrid&w=740&q=80"
HELP_PHOTO_PATH = f"media{DATA_SUFFIX}/help_photo.png"
GAMEOVER_PHOTO_PATH = f"media{DATA_SUFFIX}/gameover_photo.jpg"

DEFAULT_NC_DELAY = 0.0001
DEFAULT_NCT_DELAY = 0.0001
DEFAULT_NCS_DELAY = 0.0001
DEFAULT_NCP_DELAY = 0.0001
DEFAULT_NCGOD_DELAY = 0.001
DEFAULT_NCX_DELAY = 0.07
DEFAULT_NCLOOP_DELAY = 0.15
DEFAULT_WHONC_DELAY = 0.5
DEFAULT_NCTIME_DELAY = 0.001
DEFAULT_NCMOON_DELAY = 0.001
DEFAULT_NCCLOCK_DELAY = 0.001
DEFAULT_NCKENG_DELAY = 0.1
DEFAULT_NCHEART_DELAY = 0.001
DEFAULT_NCGAWD_DELAY = 0.001
DEFAULT_NCY_DELAY = 0.01
DEFAULT_NCXY_DELAY = 0.05
DEFAULT_NCYX_DELAY = 0.1
DEFAULT_NCZ_DELAY = 0.7
DEFAULT_NCWXS_DELAY = 0.5
DEFAULT_NCEMO_DELAY = 0.05
DEFAULT_NCQ_DELAY = 0.001
DEFAULT_KENGSPAM_DELAY = 0.5
DEFAULT_AUTOPINSPAM_DELAY = 0.1
DEFAULT_RR_DELAY = 0.1
DEFAULT_XSPAM_DELAY = 0.01
DEFAULT_XS_DELAY = 0.05
DEFAULT_X_DELAY = 0.02
DEFAULT_SX_DELAY = 0.01
DEFAULT_SL_DELAY = 0.04
DEFAULT_TS_DELAY = 0.04
DEFAULT_SWIPE_DELAY = 0.04
DEFAULT_MAR_DELAY = 0.0001
DEFAULT_PFP_DELAY = 0.5
DEFAULT_PHOTO_DELAY = 0.5
DEFAULT_DELMSG_DELAY = 0.001
DEFAULT_DELALL_DELAY = 0.001
DEFAULT_GAMEOVER_DELAY = 0.5
DEFAULT_SP_DELAY = 0.0
DEFAULT_SLIDE_DELAY = 0.1
DEFAULT_POLL_DELAY = 0.005
DEFAULT_MULTITARGET_DELAY = 0.001

NC_DELAY_RANGE = (0.0001, 0.1)
NCT_DELAY_RANGE = (0.0001, 0.5)
NCS_DELAY_RANGE = (0.0001, 0.1)
NCP_DELAY_RANGE = (0.0001, 0.1)
NCGOD_DELAY_RANGE = (0.0001, 0.5)
NCX_DELAY_RANGE = (0.0001, 0.5)
NCLOOP_DELAY_RANGE = (0.0001, 0.5)
WHONC_DELAY_RANGE = (0.0001, 0.5)
NCTIME_DELAY_RANGE = (0.0001, 0.5)
NCMOON_DELAY_RANGE = (0.0001, 0.5)
NCCLOCK_DELAY_RANGE = (0.0001, 0.5)
NCKENG_DELAY_RANGE = (0.0001, 0.5)
NCHEART_DELAY_RANGE = (0.0001, 0.5)
NCGAWD_DELAY_RANGE = (0.0001, 0.5)
NCY_DELAY_RANGE = (0.0001, 1.0)
NCXY_DELAY_RANGE = (0.0001, 0.05)
NCYX_DELAY_RANGE = (0.0001, 0.5)
NCZ_DELAY_RANGE = (0.0001, 0.7)
NCWXS_DELAY_RANGE = (0.0001, 0.5)
NCEMO_DELAY_RANGE = (0.0001, 0.5)
NCQ_DELAY_RANGE = (0.0001, 0.1)
KENGSPAM_DELAY_RANGE = (0.1, 1.0)
AUTOPINSPAM_DELAY_RANGE = (0.1, 1.0)
RR_DELAY_RANGE = (0.0001, 0.1)
XSPAM_DELAY_RANGE = (0.001, 1.0)
XS_DELAY_RANGE = (0.001, 1.0)
X_DELAY_RANGE = (0.001, 0.1)
SX_DELAY_RANGE = (0.001, 0.1)
SL_DELAY_RANGE = (0.0001, 0.1)
TS_DELAY_RANGE = (0.0001, 0.5)
SWIPE_DELAY_RANGE = (0.0001, 0.1)
MAR_DELAY_RANGE = (0.0001, 1.0)
PFP_DELAY_RANGE = (0.0001, 0.5)
PHOTO_DELAY_RANGE = (0.01, 1.0)
DELMSG_DELAY_RANGE = (0.0001, 1.0)
DELALL_DELAY_RANGE = (0.0001, 0.1)
GAMEOVER_DELAY_RANGE = (0.01, 1.0)
SP_DELAY_RANGE = (0.0, 1.0)
SLIDE_DELAY_RANGE = (0.01, 1.0)
POLL_DELAY_RANGE = (0.001, 1.0)
MULTITARGET_DELAY_RANGE = (0.001, 0.5)

RAGE_MODE_MIN_DELAY = 0.00005
ECO_MODE_MIN_DELAY = 0.5
NCGOD_PARALLEL = 5
NCYX_BURST = 5

BOT_START_TIME = time.time()

SUDO_FILE = f"sudo{DATA_SUFFIX}.json"
ADMIN_GROUPS_FILE = f"admin_groups{DATA_SUFFIX}.json"
LOG_DIR = f"logs{DATA_SUFFIX}"
BUFFER_LOG_DIR = f"buffer_logs{DATA_SUFFIX}"
STICKER_DIR = f"stickers{DATA_SUFFIX}"
MEDIA_DIR = f"media{DATA_SUFFIX}"
DOWNLOAD_DIR = f"downloads{DATA_SUFFIX}"
TTS_DIR = f"tts{DATA_SUFFIX}"
VOICE_DIR = f"voice{DATA_SUFFIX}"
GIF_DIR = f"gif{DATA_SUFFIX}"

for d in (LOG_DIR, BUFFER_LOG_DIR, MEDIA_DIR, DOWNLOAD_DIR, TTS_DIR, STICKER_DIR, VOICE_DIR, GIF_DIR):
    os.makedirs(d, exist_ok=True)

NC_LOOP_EMOJIS = ["🌀", "⚡", "🔥", "💥", "🌪️", "✨", "💫", "⭐", "🌟", "☄️", "➿", "➰"]
GAWD_EMOJIS = ["🌀", "⚡", "🔥", "💥", "🌪️", "✨", "💫", "⭐", "🌟", "☄️",
               "➿", "➰", "😂", "🙏🏻", "🙂", "😭", "❤️", "🎯", "👑", "🩷",
               "🧡", "💛", "💚", "🩵", "💙", "💜", "🖤", "🤍", "🤎", "💔"]
MOON_EMOJIS = ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌙", "🌚"]
HEART_EMOJIS = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💔",
                "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💝"]
KENG_EMOJIS = ["🐉", "🔥", "🪽", "✴️", "🌪️", "⚡", "💥", "✨", "💫", "⭐"]
CLOCK_EMOJIS = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]

NC_EMOJI_MODES = {
    "Dnc": ["🐉", "🔥", "🪽", "✴️", "🌪️"],
    "Lnc": ["🌊", "🔱", "🫧", "🐍", "💦"],
    "Knc": ["⚔️", "🗡️", "🛡️", "🏰", "⚜️"],
    "Anc": ["🏹", "🎯", "👁️", "🪶", "🍃"],
    "Enc": ["🍄", "☘️", "🧝🏻", "🧝🏻‍♀️", "🌲"],
    "Gnc": ["👹", "👺", "💚", "⛓️", "🪓"],
    "Znc": ["⚡", "🌩️", "🌬️", "🦅", "🏛️"],
    "Cnc": ["🌋", "🐕", "🐺", "🌑", "🖤"],
    "Mnc": ["🔮", "✨", "💠", "☄️", "🌙"],
}

MAR_EMOJIS = ["🤣", "😂", "😹", "🤡", "💀", "☠️", "👻", "😈", "👿", "🔥",
              "💥", "⚡", "❤️", "💔", "👍", "👎", "🖕", "🤡", "😭", "😡",
              "🤬", "🥶", "😱", "🤯", "😴", "🤤", "😏", "🙄", "😒", "😤"]

SMOJI_POOL = [
    "😀", "😂", "🤣", "😊", "😎", "🥰", "😍", "🤩", "😘", "😜",
    "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔", "🤐", "😐", "😑",
    "😶", "😏", "😒", "🙄", "😬", "🤥", "😌", "😔", "😪", "🤤",
    "😴", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "🥵", "🥶", "🥴",
    "😵", "🤯", "🤠", "🥳", "🤓", "🧐", "😕", "😟", "🙁",
    "😮", "😯", "😲", "😳", "🥺", "😦", "😧", "😨", "😰", "😥",
    "😢", "😭", "😱", "😖", "😣", "😞", "😓", "😩", "😫", "🥱",
    "😤", "😡", "😠", "🤬", "😈", "👿", "💀", "☠️", "💩", "🤡",
    "👹", "👺", "👻", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹",
    "😻", "😼", "😽", "🙀", "😿", "😾", "🙈", "🙉", "🙊",
    "❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💔",
    "❣️", "💕", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "♥️",
    "🔥", "💥", "⚡", "✨", "💫", "⭐", "🌟", "☄️", "🌪️", "🌊",
    "💧", "💦", "💨", "🌀", "➿", "➰", "🎯", "🎭", "🎨",
    "🍕", "🍔", "🍟", "🌸", "🌹", "🍀", "🍁", "🍄",
]

NCX_LINES = [
    " ‌ ✿ ꪑꫝᴅꫝʀCʜꪮᴅ ✿", " ‌ ✮⋆ ꪑꫝᴅꫝʀCʜꪮᴅ ✮⋆",
    " ‌ ᯓᡣ𐭩 ꪑꫝᴅꫝʀCʜꪮᴅ ᡣ𐭩ᯓ", " ‌ ♡ ꪑꫝᴅꫝʀCʜꪮᴅ ♡",
]

NCGOD_LINES = [
    "𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜજ⁀➴😀",
    "𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜજ⁀➴😁",
    "𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜજ⁀➴😂",
    "𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜજ⁀➴🤣",
]

NCLOOP_LINES = [
    " ᵀᵐᴷᶜ」🦋꙰  ~ ༈  ◠🇮🇳◡", " Teri माँ Dead 😂 ",
    " ᴛᴇʀᴀ ʙᴀᴀᴘ ᴄᴀʀᴘᴀɴᴛᴇʀ 🪚", " ᴛʀʏ ᴅᴀᴅɪ sʟᴜᴛ⚀︎",
]

# ═══════════════════════════════════════════════════════════════════════════════
#                    WHONC TEXTS — 17 slots
# ═══════════════════════════════════════════════════════════════════════════════

WHONC_TEXTS = [
    """(test)𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓજ⁀➴𑁍ࠬܓ""",
    """(test)𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗦ʟᴜᴛ◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────▹🤣◃───────────""",
    """(test)تیری ما کے بوسدے پہ لنڈ ہی لنڈ ماروگا ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ❤️⁀➷""",
    """(test)𝘴ꪖꪶꪖꪑ 𝘬𝘳 ꪑꪖᦔꪖ𝘳ᥴꫝꪮᦔ ρ𝓲ꪶꪶꫀ➴➵➶➴➵➶➴➵➶⚡️➴➵➶➴➵➶➴➵➶🌙➴➵➶➴➵➶➴➵➶❤️➴➵➶➴➵➶➴➵➶😂➴➵➶➴➵➶➴➵➶🥺➴➵➶➴➵➶➴➵➶❤️‍🩹➴➵➶➴➵➶➴➵➶💋➴➵➶➴➵➶➴➵➶🫠➴➵➶➴➵➶➴➵➶🤍➴➵➶➴➵➶➴➵➶🥰➴➵➶➴➵➶➴➵➶""",
    """(test)ѕυииє мє αуα тєяι мα вυя ∂єкє я∂ρ ℓαgαтι нαι•❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅••❅───✧❅✦❅✧───❅•""",
    """(test)𝘓𝘜𝘕 𝘚𝘌 𝘜𝘛𝘈𝘙 𝘗𝘐𝘓𝘓𝘌─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───""",
    """(test)𝙏𝙊𝙃𝘼𝙍 𝙈𝘼𝙄𝙔𝘼 𝘾𝙃𝘼𝙄𝙔𝘼 𝘾𝙃𝘼𝙄𝙔𝘼 🦕 ꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅꧅""",
    """(test)☠️ TMKC 𒐫꧅𒐫꧅𒐫꧅𒐫꧅𒐫꧅💠𒐫𒐫𒐫🩷𒐫𒐫𒐫𒐫꧅𒐫꧅𒐫꧅𒐫꧅𒐫꧅💠𒐫𒐫𒐫🩷𒐫𒐫𒐫𒐫꧅𒐫꧅𒐫꧅𒐫꧅𒐫꧅💠𒐫𒐫𒐫🩷𒐫𒐫𒐫𒐫꧅𒐫꧅𒐫꧅𒐫꧅𒐫꧅💠𒐫𒐫𒐫""",
    """(test)𝙈𝘼𝘿𝘼𝙍𝘾𝙃🚫𝘿 𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫💠𒐫𒐫𒐫𒐫💠 """,
    """(test)𝘛𝘔𝘒𝘊 ¡👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀🌀🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀🌀🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀🌀🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀🌀🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀🌀🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑🌀👑""",
    """(test)ᖇᗩᑎᗪᗩᒪ 𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙⸻𒈙🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🤍🌀🫧🌀🤍🫧🌀🤍𐃘𐃘 ᶜʰᵘᵈ ʲᵃ !""",
    """(test)ƬƲᴍ ƧƛƁ Ҡƛ ƁƲƦ ƑƛƬ ƓᎩƛ ƇᎩƛ 𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙𒈙""",
    """(test)🇰🇬 𝘾𝙃𝙐𝘿𝘼𝙄 𝙏𝘼𝙈𝙀 𝘾𝙃𝘼𝙇𝙐]>{🥶}𒈙👑𒈙❤️‍🔥𒈙👑𒈙💦𒈙👑𒈙💛𒈙👑𒈙🤍𒈙👑𒈙💚𒈙👑𒈙🩷𒈙🎀𒈙👑𒈙❤️‍🔥𒈙👑𒈙💦𒈙👑𒈙💛𒈙👑𒈙🤍𒈙👑𒈙💚𒈙👑𒈙🩷𒈙🎀𒈙👑𒈙❤️‍🔥𒈙👑𒈙💦𒈙👑𒈙💛𒈙👑𒈙🤍𒈙👑𒈙💚𒈙👑𒈙🩷𒈙🎀""",
    """(test) ʟᴜɴᴅ ᴄʜᴜꜱ ʀᴅᴩ ᴅᴜɢᴀ😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂""",
    """(test) 𝘛𝘔𝘒𝘊 ﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽﷽⚡️﷽⚡️﷽⚡️﷽﷽⚡️""",
]

WHONC_TEXTS_ACTIVE = [t for t in WHONC_TEXTS if t.strip()]

SX_TEXTS = [
    "NHI NHI AB TOH TERI MA CHOD DUGA🤣🤣😭😭😭😭❤️❤️",
    "ᴀʙ ᴛᴏʜ ᴍᴀᴀ ᴄʜᴜᴅᴀ ɴᴀ ᴍᴜᴊʜᴇ q ʙᴛᴀ ʀʜᴀ ᴋɪ ᴛᴇʀɪ ᴍᴀ ʀᴀɴᴅɪ?? 🥹🥹🥹😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂",
    "ᵉʸ ᵈᵉᵏʰ ᵗᵐᵏᶜ ˢᵉ ᵇʰⁱ ᶜʰᵒᵗᵃ ᶠᵒⁿᵗ ⁱˢˢᵉ ᵗᵉʳⁱ ᵐᵃ ᵏⁱ ᶜʰᵘᵈᵃⁱ ᵏʳᵈᵘ? 🤔🤔🤔😬😬",
    "ѕυи мєяι ℓυи ¢нυѕℓє єк вααя ☺️☺️",
    "ᗩᑕᕼᗩ ᑕᕼᒪ TᗯO Kᗩ TᗩᗷᒪE Yᗩᗩᗪ Kᖇ Tᗷ TK ᗰᗩI TEᖇI ᗰᗩ KO ᗷIO ᑭᗩᗪᕼᗩ KE ᗩYᗩ!!🥹🥹🥹☺️☺️😬😬🤔🤔🤣❄️😂😂❄️🤣😭",
    "ι∂нαя ѕυи мαι ку вσℓ яgα ιтиє α¢нє ѕє q ѕυи янα тєяι мα яи∂ι єу вσℓ янα тнα🥲🙏🙏🙏🙏😇😇😇",
    "ᶜʰᵘᵈᵃⁱ ᵏʰᵃᵒᵍᵉ ʸᵃ ᵐᵉʳᵃ ˡᵘⁿ ᶜʰᵘˢᵒᵍᵉ? ☺️😬",
    "ᵃᶜʰᵃ ᵏᵒⁱ ⁿᵃʰ ᵐᵃⁱ ᵗᵒʰ ᵗᵐᵏᶜ ᵐᵃʳᵘᵍᵃ????? 🙏🙏🙏🙏🙏",
    "ᴀᴄʜᴀ ᴄʜʟ ꜱᴀʟᴀᴍ ᴛʜᴏᴋ ʙᴇᴛᴀ...!!? 😇🙏"
]

XS_TEXTS = [
    """(test) ʙᴇᴛᴀ ᴋɪ ᴄʜᴀᴅʜɪ ꜰᴀᴛɪ ᴩᴀᴅɪ ᴏʀ ʙᴇᴛᴀ ᴇᴋ ɢᴄ ꜱᴩᴍ ᴋʀᴇɢᴀ<semoji>\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n*35""",
    """(test) ᵃᶜʰᵃ ᵏᵒⁱ ⁿᵃʰ ᵐᵃⁱ ᵗᵒʰ ᵗᵉʳⁱ ᵇʰⁿ ᵇʰⁱ ᶜʰᵒᵈᵘᵍᵃ ʸʳ<semoji>\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n*35""",
    """(test)SUNNE ME AYA TERI MA BUR DEKE HOSTER BOT KA ACCESS LETI<semoji>\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n*35""",
]

KENGSPAM_TEXTS = [
    "(test)𝗥ᴜᴋ 𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗠ᴇ 𝗟ᴀᴀᴅ 𝗕ʜᴀʀᴛᴀ 𝗛ᴜ(smoji)\n*50",
    "(test) ℓυи ѕє ѕтαи∂ υρ нσ ριℓℓє(semojj)\n*50",
    "(test)🅴︎🅺︎ 🅶︎🅲︎ 🆂︎🅿︎🅰︎🅼︎🅼︎🅴︎🆁︎ 🅱︎🅰︎🅽︎🅰︎🆄︎? (semoji)\n*50",
    "(test)𝗧𝗠𝗞𝗖(semojj)\n*50",
    "(test)𝗧ᴇʀɪ 𝗠ᴀᴀ 𝗦ʟᴜᴛ◃───────────▹(semoji)◃───────────▹\n*50",
    "(test)تیری ما کے بوسدے پہ لنڈ ہی لنڈ ماروگا ೃ❤️⁀➷ ೃ❤️⁀➷ ೃ(semoji)\n*50",
    "(test)𝘴ꪖꪶꪖꪑ 𝘬𝘳 ꪑꪖᦔꪖ𝘳ᥴꫝꪮᦔ ρ𝓲ꪶꪶꫀ➴➵➶➴➵➶➴➵➶(emoji)➴➵➶➴➵➶➴➵➶(emoji)➴➵➶➴➵➶➴➵➶\n*50",
    "(test)ѕυииє мє αуα тєяι мα вυя ∂єкє я∂ρ ℓαgαтι нαι•❅───✧❅✦❅✧───❅••❅───✧❅✦(semoji)\n*50",
    "(test)𝘓𝘜𝘕 𝘚𝘌 𝘜𝘛𝘈𝘙 𝘗𝘐𝘓𝘓𝘌─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ. ───🎀─── ･ ｡ﾟ☆: *.☽ .*:☆ﾟ.(semoji)\n*50",
]

XTEXT = [
    """(Test) 𝘛𝘌𝘙𝘐 𝘔𝘖𝘔 𝘐𝘚 𝘈 𝘔𝘖𝘛𝘏𝘌𝘙𝘍𝘊𝘒𝘐𝘕𝘎 𝘚𝘓𝘜𝘛<semoji>\n*70""",
    """(Test) 𝘓𝘜𝘕 𝘊𝘏𝘜𝘚 𝘙𝘋𝘗 𝘋𝘜𝘎𝘈<semoji>\n*70""",
    """(Test) 𝗕ᴀᴀᴩ 𝗞ᴇ 𝗦ᴀᴍɴᴇ 𝗦ᴩᴀᴍ 𝗞ʀᴇɢᴀ 𝗜ᴛɴᴀ 𝗕ᴀᴅᴀ 𝗞ʙ 𝗛ᴏɢʏᴀ<semoji>\n*70""",
    """(Test) 𝗘ᴋ 𝗚ᴄ 𝗦ᴩᴀᴍᴍᴇʀ 𝗕ᴀɴᴀᴜ<semoji>\n*70""",
]

XTEXT_RAID = [
    "𝐓ꫀʀɪ 𝐌ꫝꫝ 𝐂ʜꪮᴅꪀꫀ 𝐊 ʟɪʏꫀ 𝐏ᴜʀꫝ 𝐆ᥴ 𝐊ʜꫝᴅꫝ 𝐇ꫝɪ 🥴😁🩷💯",
    "𝐎ʏꫀ 𝐌ꫝᴅꫝʀᥴʜꪮᴅ 𝐔ᴛʜ 😤😡🥵 𝐓ꫀʀɪ 𝐌ꫝꫝ 𝐊ꫝ 𝐂ʜꪮᴅɪꪀɢ 𝐓ꫀꪑ 😈👻🦶🏻",
]

SLAUGHTER_TEXTS = [
    "𝐓ꫀʀɪ 𝐌ꫝꫝ 𝐂ʜꪮᴅꪀꫀ 𝐊 ʟɪʏꫀ 𝐏ᴜʀꫝ 𝐆ᥴ 𝐊ʜꫝᴅꫝ 𝐇ꫝɪ 🥴😁🩷💯",
    "𝐎ʏꫀ 𝐌ꫝᴅꫝʀᥴʜꪮᴅ 𝐔ᴛʜ 😤😡🥵 𝐓ꫀʀɪ 𝐌ꫝꫝ 𝐊ꫝ 𝐂ʜꪮᴅɪꪀɢ 𝐓ꫀꪑ 😈👻🦶🏻",
]

TARGET_SLIDE_TEXTS = ["𝗧ᴇʀᴇ 𝗕ᴀᴀᴘ 𝗛ᴀɪɴ 𝗛ᴜᴍ 𝗟ᴏɢ 𝗦ᴍᴊʜᴀ ?¿ ִֶָ. ..𓂃 ࣪ ִֶָ🪽་༘࿐",
"͙͘͡★𝙏𝙈𝙆𝘾 𝙈𝙀 𝙂𝙊𝙅𝙊 𝙆𝘼 𝙃𝙊𝙇𝙇𝙊𝙒 𝙋𝙐𝙍𝙋𝙇𝙀 🔴🔵-> 🫴🏻🟣",
"𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐎 𝐊𝐇𝐀𝐂𝐇𝐀𝐑 𝐊𝐇𝐀𝐂𝐇𝐀𝐑 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐂𝐇𝐔𝐓𝐈𝐘𝐄 🩷🩵🩷🩵 ᭝ ᨳଓ ՟",
"Tᴇʀɪ ᵐᵃ Cʜ⭕ᴅ Dɪ Rᴇ 🕷️᭄••°ᠿ--",
"ᛕꪖꪑɀꪮ᥅ ᥅ꪀᦔꪗᛕ ꪶꪮᦔꫀ ᜣ𝔯 ᥇ꫀꪻ𝔥 ⋆｡𖦹°⭒˚｡⋆",
"tmkc me itne saarey desh 🇦🇨🇦🇩🇦🇪🇦🇫🇦🇬🇦🇮🇦🇱🇦🇲🇦🇿🇦🇽🇦🇼🇦🇺🇧🇪🇧🇫🇧🇩🇧🇴🇧🇳🇧🇼🇧🇾🇨🇮🇨🇭🇨🇵🇪🇸🇫🇴🇬🇭🇬🇷🇬🇶🇬🇬🇬🇪🇬🇳🇮🇳🇰🇪🇯🇵",
"⁀➴Fᴀᴛᴇ Hᴀs Bᴇᴇɴ Sᴇᴀʟᴇᴅ , Yᴏᴜ Cᴀɴɴᴏᴛ Dᴇғᴇᴀᴛ Mᴇ 🖤🍃",
"𝒀𝒐𝒖 𝒂𝒓𝒆 𝒅𝒆𝒔𝒕𝒊𝒏𝒆𝒅 𝒕𝒐 𝒍𝒐𝒔𝒆 𝒕𝒐 𝒎𝒆 . 𝑱𝒖𝒔𝒕 𝒌𝒏𝒆𝒆𝒍 𝒊𝒏𝒇𝒓𝒐𝒏𝒕 𝒐𝒇 𝒎𝒆 , 𝑰'𝒅 𝒈𝒐 𝒆𝒂𝒔𝒚 𝒐𝒏 𝒚𝒐𝒖 𝒕𝒉𝒆𝒏 ♱ .ᐟ.ᐟ",
"𝚃ᴇʀɪ 𝙳ᴀᴅɪ 𝙺ɪ 𝚆ʜᴇᴇʟᴄʜᴀɪ𝚁 𝚃ᴏᴅ𝚄 𝙺ʏᴀ 𝚁ᴇ 𓆩❤︎𓆪",
"ᗷᕼᗴᑎ ᖇᗩᑎᗪY TᗴᖇI 🤮🤣😂😹😂😹🤣👐🏻🫲🏻🖐🏻👐🏻👈🏻👇🏻",
"𝐊ʀᴋʀ 𝐆ᴀʀᴀᴍ 𝐏ᴀʀᴀᴛʜᴇ 🥞 𝐓ᴍᴋᴄ 𝐏ʀ 𝐌ᴀʀᴜ 𝐂ʜᴀᴘᴀᴛᴇ 💀🫲🏻",
"𝗦𝗬𝗕𝗔𝗨 𝗡𝗚𝗔 🫨🐬 ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.",
"⌗Tᴇʀɪ Mᴀ Kᴇ Sᴏғᴛ Cʜᴜᴛᴀᴅᴏ Pᴀʀ Aᴘɴᴇ Lᴜɴᴅ Sᴇ Cʜᴀᴀᴛᴇ Mᴀʀᴜ .𖥔 ݁ ˖🦢˚. ᵎᵎ",
"𝘎𝘊 𝘓𝘌𝘈𝘝𝘌 𝘓𝘌 𝘍𝘈𝘛 𝘔𝘖𝘔 𝘒𝘌 𝘓𝘈𝘋𝘒𝘌 😂❤️‍🔥💙😂🔔🎯",
"༯ Bow down and show respect to the e-gods .ᐟ"]
SWIPE_TEXTS = [
    "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐒ʟᴜᴛ 🤣", "𝐂ʜᴜᴘ ʀᴀɴᴅɪ 🤫", "𝐓ᴇʀᴀ ʙᴀᴀᴘ ʜᴜ ᴍᴀɪ 🎅",
]

RR_TEXTS = [
    "𝗧ᴍᴋᴄ ʙᴏʟ ᴋᴇ ᴍᴀᴛ ʙᴀᴅʜ 🤬", "𝐓ᴇʀɪ 𝐌ᴀᴀ 𝐒ʟᴜᴛ 🤣", "ᴄʜᴜᴘ ʀᴀɴᴅɪ 🤫",
    "𝐓ᴇʀᴀ ʙᴀᴀᴘ ʜᴜ ᴍᴀɪ 🎅",
"𝗧ᴇʀᴇ 𝗕ᴀᴀᴘ 𝗛ᴀɪɴ 𝗛ᴜᴍ 𝗟ᴏɢ 𝗦ᴍᴊʜᴀ ?¿ ִֶָ. ..𓂃 ࣪ ִֶָ🪽་༘࿐",
"͙͘͡★𝙏𝙈𝙆𝘾 𝙈𝙀 𝙂𝙊𝙅𝙊 𝙆𝘼 𝙃𝙊𝙇𝙇𝙊𝙒 𝙋𝙐𝙍𝙋𝙇𝙀 🔴🔵-> 🫴🏻🟣",
"𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐎 𝐊𝐇𝐀𝐂𝐇𝐀𝐑 𝐊𝐇𝐀𝐂𝐇𝐀𝐑 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐂𝐇𝐔𝐓𝐈𝐘𝐄 🩷🩵🩷🩵 ᭝ ᨳଓ ՟",
"Tᴇʀɪ ᵐᵃ Cʜ⭕ᴅ Dɪ Rᴇ 🕷️᭄••°ᠿ--",
"ᛕꪖꪑɀꪮ᥅ ᥅ꪀᦔꪗᛕ ꪶꪮᦔꫀ ᜣ𝔯 ᥇ꫀꪻ𝔥 ⋆｡𖦹°⭒˚｡⋆",
"tmkc me itne saarey desh 🇦🇨🇦🇩🇦🇪🇦🇫🇦🇬🇦🇮🇦🇱🇦🇲🇦🇿🇦🇽🇦🇼🇦🇺🇧🇪🇧🇫🇧🇩🇧🇴🇧🇳🇧🇼🇧🇾🇨🇮🇨🇭🇨🇵🇪🇸🇫🇴🇬🇭🇬🇷🇬🇶🇬🇬🇬🇪🇬🇳🇮🇳🇰🇪🇯🇵",
"⁀➴Fᴀᴛᴇ Hᴀs Bᴇᴇɴ Sᴇᴀʟᴇᴅ , Yᴏᴜ Cᴀɴɴᴏᴛ Dᴇғᴇᴀᴛ Mᴇ 🖤🍃",
"𝒀𝒐𝒖 𝒂𝒓𝒆 𝒅𝒆𝒔𝒕𝒊𝒏𝒆𝒅 𝒕𝒐 𝒍𝒐𝒔𝒆 𝒕𝒐 𝒎𝒆 . 𝑱𝒖𝒔𝒕 𝒌𝒏𝒆𝒆𝒍 𝒊𝒏𝒇𝒓𝒐𝒏𝒕 𝒐𝒇 𝒎𝒆 , 𝑰'𝒅 𝒈𝒐 𝒆𝒂𝒔𝒚 𝒐𝒏 𝒚𝒐𝒖 𝒕𝒉𝒆𝒏 ♱ .ᐟ.ᐟ",
"𝚃ᴇʀɪ 𝙳ᴀᴅɪ 𝙺ɪ 𝚆ʜᴇᴇʟᴄʜᴀɪ𝚁 𝚃ᴏᴅ𝚄 𝙺ʏᴀ 𝚁ᴇ 𓆩❤︎𓆪",
"ᗷᕼᗴᑎ ᖇᗩᑎᗪY TᗴᖇI 🤮🤣😂😹😂😹🤣👐🏻🫲🏻🖐🏻👐🏻👈🏻👇🏻",
"𝐊ʀᴋʀ 𝐆ᴀʀᴀᴍ 𝐏ᴀʀᴀᴛʜᴇ 🥞 𝐓ᴍᴋᴄ 𝐏ʀ 𝐌ᴀʀᴜ 𝐂ʜᴀᴘᴀᴛᴇ 💀🫲🏻",
"𝗦𝗬𝗕𝗔𝗨 𝗡𝗚𝗔 🫨🐬 ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.",
"⌗Tᴇʀɪ Mᴀ Kᴇ Sᴏғᴛ Cʜᴜᴛᴀᴅᴏ Pᴀʀ Aᴘɴᴇ Lᴜɴᴅ Sᴇ Cʜᴀᴀᴛᴇ Mᴀʀᴜ .𖥔 ݁ ˖🦢˚. ᵎᵎ",
"𝘎𝘊 𝘓𝘌𝘈𝘝𝘌 𝘓𝘌 𝘍𝘈𝘛 𝘔𝘖𝘔 𝘒𝘌 𝘓𝘈𝘋𝘒𝘌 😂❤️‍🔥💙😂🔔🎯",
"༯ Bow down and show respect to the e-gods .ᐟ"
]

AUTOPINSPAM_TEXT = "𝗞ʏᴇ 𝗥ᴇ 𝗔ᴩɴᴇ 𝗕ᴀᴀᴩ 𝗦𝗲 𝗙ʏᴛ 𝗞ʀᴇɢᴀ 𝗧ᴍᴋᴄ{text}"

GAMEOVER_TEXT = (
    "(test) ᴍᴀᴀ ᴄʜᴏᴅ ɢʏɪ? ᴋʏ ʀᴀɴᴅɪᴋᴇ ʙᴀᴀᴩ ꜱᴇ ꜰʏᴛ ᴋʀᴇɢᴀ?? "
    "😂😂😂😂😂😂😂🤣🤣🤣 ᴄʜʟ ᴀʙ ʟᴜɴ ᴄʜᴜꜱ ᴏʀ ʙᴀᴅᴀ ʜᴏᴊᴀ 🥂\n"
    "🕐 IST: {ist}\n"
    "📅 DATE: {date}"
)

SP1_TEXTS = [
    "{{target}} 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐑𝐍𝐃𝐈➢ (💛)                                                                                          {{target}} 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐑𝐍𝐃𝐈➢ (💛)",
    "{{target}} 𝐓ᴇʀɪ Mᴀ Pʀᴇᴛᴛʏ Lɪʟ Rɴᴅɪ ➢(🎀)                                                                                          {{target}} 𝐓ᴇʀɪ Mᴀ Pʀᴇᴛᴛʏ Lɪʟ Rɴᴅɪ ➢(🎀)",
    "Cʜᴀᴛʀɪ Kᴇ UᴘᴀR Pᴀɴɪ {{target}} Tᴇʀɪ Mᴀ Rᴀɴᴅɪᴏ Kɪ Mᴀʜᴀ Rᴀɴɪ 〔𓆩🎀𓆪〕⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝ Cʜᴀᴛʀɪ Kᴇ UᴘᴀR Pᴀɴɪ {{target}} Tᴇʀɪ Mᴀ Rᴀɴᴅɪᴏ Kɪ Mᴀʜᴀ Rᴀɴɪ 〔𓆩🎀𓆪〕──╯",
    "𝑨𝑨𝑴 𝑻𝑶𝑫𝑼 𝑳𝑨𝑻𝑨𝑲 𝑳𝑨𝑻𝑨𝑲 𝑲𝑬    {{target}}  𝑮𝑹𝑰𝑩 𝑲𝑰 𝑴𝑨𝑲𝑶 𝑪𝑯𝑶𝑫𝑼 𝑷𝑨𝑻𝑨𝑲 𝑷𝑨𝑻𝑨𝑲 𝑲𝑨𝑹 🩷..........................🩷..........................🩷..........................🩷..........................🩷..........................🩷..........................🩷..........................🩷..........................🩷.......................... 𝑨𝑨𝑴 𝑻𝑶𝑫𝑼 𝑳𝑨𝑻𝑨𝑲 𝑳𝑨𝑻𝑨𝑲 𝑲𝑬    {{target}}  𝑮𝑹𝑰𝑩 𝑲𝑰 𝑴𝑨𝑲𝑶 𝑪𝑯𝑶𝑫𝑼 𝑷𝑨𝑻𝑨𝑲 𝑷𝑨𝑻𝑨𝑲 𝑲𝑨𝑹"
]

SP2_TEXTS = [
    "⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️\n\n⚡️🌙☘️ {{target}} 𝐹𝑌𝑇𝐸𝑅 𝐵𝑁𝐸𝐺 𝐵𝐻𝐸𝑁 𝐾𝐸 𝐿𝐴𝑁𝐷 𝐵𝑁𝐴𝑈 𝐹𝑌𝑇𝑅?⚡️🌙☘️"
]

SP3_TEXTS = [
    "𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>\n\n𝗧𝗘𝗘𝗥 𝗦𝗘 𝗡𝗔 𝗧𝗔𝗟𝗪𝗔𝗥 𝗦𝗘 ({{target}}) 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨𝗚𝗔 𝗟𝗡𝗗 𝗞𝗘 𝗪𝗔𝗥 𝗦𝗘 ─── <🧃>"
]

SP4_TEXTS = [
    "{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒𝘐 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪\n\n{{target}} 𝘛𝘌𝘙I 𝘔𝘈𝘈 𝘒O 𝘙O𝘊𝘒𝘌𝘛 𝘒I 𝘚𝘗𝘌𝘌𝘋 𝘚𝘌 𝘊𝘏O𝘋𝘜?⏤‌‌  ⏤‌‌  ⏤‌‌ 𓆩🚀𓆪"
]

SP5_TEXTS = [
    "({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝟵𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────\n\n({{target}})  𝗞𝗬𝗔 𝗥𝗘 𝗥𝗔𝗡𝗗𝗜𝗞𝗘 𝗙𝗬𝗧𝗥 𝗕𝗡𝗘𝗚𝗔 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗨? ⚡️🌙💚  ──────"
]

SP6_TEXTS = [
    ".ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜ𝐎ᴅ 𝐊ᴇ 𝐁ʜ𝐎s𝐃ᴀ 𝐅ᴀ𝐃ᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜ𝐎ᴅ 𝐊ᴇ 𝐁ʜ𝐎s𝐃ᴀ 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅᴀ 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ\n\n.ᐟ.ᐟ {{target}} 𝐓ᴇ𝐑ɪ 𝐌ᴀᴀ 𝐂ʜᴏᴅ 𝐊ᴇ 𝐁ʜᴏsᴅ𝐀 𝐅ᴀᴅᴜ? ⏤‌‌🤍 .ᐟ.ᐟ"
]

SP_TEXTS_MAP: Dict[int, list] = {
    1: SP1_TEXTS, 2: SP2_TEXTS, 3: SP3_TEXTS,
    4: SP4_TEXTS, 5: SP5_TEXTS, 6: SP6_TEXTS,
}
SP_TEXTS_ACTIVE: Dict[int, list] = {
    n: [t for t in texts if t.strip()] for n, texts in SP_TEXTS_MAP.items()
}

SLIDE_PATTERNS_1 = [
    "{{target}} 𝑻𝒆𝒓𝒊 𝑴𝒂 𝑮𝒂𝒏𝒋𝒊 𝑪𝒉𝒖𝒅𝒂𝒊𝒍🤢🔥",
    "{{target}} PᴀɪR Pᴀᴋᴀᴅ Kᴇ Sᴏʀʀʏ 𝗣ʀᴇғɪ᥊ᴇ𝗥 Pᴀᴘᴀ Bᴏʟ😂🔥",
    "{{target}} 𝐂𝐇𝐔𝐃𝐃𝐊𝐑 𝐌𝐔𝐋𝐋𝐄🫏",
    "{{target}} 𝘉𝘢𝘶𝘯𝘪 𝘔𝘢𝘬𝘦 𝘓𝘢𝘥𝘬𝘦 𝘉𝘩𝘢𝘯𝘨𝘪 😂🔥",
    "{{target}} 𝗞𝗔𝗟𝗪𝗔𝗔𝗔𝗔𝗔😭🔥",
]
SLIDE_PATTERNS_2 = [
    "𓆩🩷𓆪{{target}} HAKLI BAUNI 𓆩🩷𓆪",
    "𓆩💛𓆪{{target}} CHUDDKR CHI 𓆩💛𓆪",
    "𓆩💜𓆪{{target}} BTS LOVER RNDI𓆩💜𓆪",
    "𓆩🌗𓆪{{target}} GHINONI RND𓆩🌗𓆪",
    "𓆩🤍𓆪{{target}} CHUDAI KHA KIDA𓆩🤍𓆪",
    "𓆩💢𓆪{{target}} MA RNDI TERI 𓆩💢𓆪"
]
SLIDE_PATTERNS_3 = [
    "~×💜×~HIJDA~×💜×~",
    "~×💛×~GAY~×💛×~",
    "~×🤍×~PANTY CHOR ~×🤍×~",
    "~×🎀×~RANDYMON~×🎀×~",
    "~×🖤×~CHAMAR~×🖤×~",
    "~×🧡×~TRI MA CHUDI~×🧡×~",
    "~×🩵×~NIGGA CHI~×🩵×~"
]
SLIDE_PATTERNS_4 = [
    "{{target}} Hɪᴊᴅᴏ Kᴇ Sᴀᴜᴅᴀɢᴀʀ",
    "{{target}} Bᴀᴡᴀsɪʀ Kᴀ Mᴀʀɪᴢ",
    "{{target}} Zᴏᴍᴇᴛᴏ BᴏY ᴄʜᴜᴘ",
    "{{target}} Kɪɴɴᴀʀᴏ Kᴀ Bᴇᴛᴀ",
    "{{target}} Kᴀᴄʜʀᴀ Uᴛʜᴀɴᴇ ᴡᴀʟᴇ",
    "{{target}} Mᴜʟʟᴀ Bᴀᴜɴᴀ",
    "{{target}} Cʜᴜᴛɪʏᴀ Bᴇᴛᴀ",
    "{{target}} Nɪᴄʜɪ Jᴀᴀᴛ",
    "{{target}} Kᴀʟʟᴜ Aғʀɪᴄᴀɴ",
    "{{target}} Nᴀᴊᴀʏᴇᴢ Lᴀᴅᴋᴀ",
]
SLIDE_PATTERNS_5 = [
    "{{target}} 𝐓𝐔𝐌 𝐓𝐀𝐀𝐓𝐓𝐎 𝐊𝐈 𝐌𝐊𝐁 𝐆𝐀𝐑𝐄𝐄𝐁𝐎___/⭐{{target}} 𝐓𝐔𝐌 𝐓𝐀𝐀𝐓𝐓𝐎 𝐊𝐈 𝐌𝐊𝐁 𝐆𝐀𝐑𝐄𝐄𝐁𝐎_/⭐{{target}} 𝐓𝐔𝐌 𝐓𝐀𝐀𝐓𝐓𝐎 𝐊𝐈 𝐌𝐊𝐁 𝐆𝐀𝐑𝐄𝐄𝐁𝐎_/⭐{{target}} 𝐓𝐔𝐌 𝐓𝐀𝐀𝐓𝐓𝐎 𝐊𝐈 𝐌𝐊𝐁 𝐆𝐀𝐑𝐄𝐄𝐁𝐎_/⭐{{target}} 𝐓𝐔𝐌 𝐓𝐀𝐀𝐓𝐓𝐎 𝐊𝐈 𝐌𝐊𝐁 𝐆𝐀𝐑𝐄𝐄𝐁𝐎_____/⭐"
]
SLIDE_TEXTS_MAP: Dict[int, list] = {
    1: SLIDE_PATTERNS_1, 2: SLIDE_PATTERNS_2, 3: SLIDE_PATTERNS_3,
    4: SLIDE_PATTERNS_4, 5: SLIDE_PATTERNS_5
}
SLIDE_TEXTS_ACTIVE: Dict[int, list] = {
    n: [t for t in texts if t.strip()] for n, texts in SLIDE_TEXTS_MAP.items()
}

POLL_QUESTION_TEMPLATE = "(test) 𝗟ᴜɴᴅ 𝗖ʜᴜꜱ 𝗕ᴀᴅᴀ 𝗛ᴏ<semoji>"
POLL_OPT1_TEMPLATE = "(test) 𝗧ᴍᴋʙ 𝗣ᴇ 𝗟ᴜɴᴅ 𝗠ᴀʀᴜ\n\n\n\n\n\n\n(semoji)\n*30"
POLL_OPT2_TEMPLATE = "(test) 𝘴ꪖꪶꪖꪑ 𝘬𝘳 ꪑꪖᦔꪖ𝘳ᥴꫝꪮᦔ ρ𝓲ꪶꪶꫀ➴➵➶➴➵➶➴➵➶(emoji)➴➵➶➴➵➶➴➵➶(emoji)➴➵➶➴➵➶➴➵➶\n*30"

LEGION_EVOLUTION_MSG = """╔══════════════════════════════╗
║ 🌌 𝗟𝗘𝗚𝗜𝗢𝗡 𝗘𝗩𝗢𝗟𝗨𝗧𝗜𝗢𝗡 ║
╚══════════════════════════════╝
🌀 𝑻𝒉𝒆 𝒆𝒗𝒐𝒍𝒖𝒕𝒊𝒐𝒏 𝒃𝒆𝒈𝒊𝒏𝒔...
⚡ 𝑹𝒂𝒏𝒌𝒔 𝒂𝒓𝒆 𝒃𝒆𝒊𝒏𝒈 𝒓𝒆𝒇𝒐𝒓𝒎𝒆𝒅.
🔥 𝑻𝒉𝒆 𝒍𝒆𝒈𝒊𝒐𝒏 𝒉𝒂𝒔 𝒆𝒗𝒐𝒍𝒗𝒆𝒅.
👑 𝑨 𝒏𝒆𝒘 𝒆𝒓𝒂 𝒃𝒆𝒈𝒊𝒏𝒔."""

RETREAT_ORDER_MSG = """╔══════════════════════════════╗
║ 🏳️ 𝗥𝗘𝗧𝗥𝗘𝗔𝗧 𝗢𝗥𝗗𝗘𝗥 ║
╚══════════════════════════════╝

👑 𝑻𝒉𝒆 𝒔𝒐𝒗𝒆𝒓𝒆𝒊𝒈𝒏'𝒔 𝒐𝒓𝒅𝒆𝒓 𝒉𝒂𝒔 𝒃𝒆𝒆𝒏 𝒉𝒆𝒂𝒓𝒅.
⚔️ 𝑨𝒍𝒍 𝒘𝒂𝒓𝒓𝒊𝒐𝒓𝒔 𝒂𝒓𝒆 𝒘𝒊𝒕𝒉𝒅𝒓𝒂𝒘𝒊𝒏𝒈...
🏰 𝑻𝒉𝒆 𝒍𝒆𝒈𝒊𝒐𝒏 𝒓𝒆𝒕𝒖𝒓𝒏𝒔 𝒕𝒐 𝒕𝒉𝒆 𝒓𝒆𝒂𝒍𝒎.
🛡️ 𝑭𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏: 𝑪𝒍𝒆𝒂𝒓𝒆𝒅
🌙 𝑻𝒉𝒆 𝒃𝒂𝒕𝒕𝒍𝒆𝒇𝒊𝒆𝒍𝒅 𝒇𝒂𝒍𝒍𝒔 𝒔𝒊𝒍𝒆𝒏𝒕."""

SUMMONING_RITUAL_MSG = """╔══════════════════════════════╗
║ 🌀 𝗦𝗨𝗠𝗠𝗢𝗡𝗜𝗡𝗚 𝗥𝗜𝗧𝗨𝗔𝗟 ║
╚══════════════════════════════╝
👑 𝑺𝒐𝒗𝒆𝒓𝒆𝒊𝒈𝒏'𝒔 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒓𝒆𝒄𝒆𝒊𝒗𝒆𝒅.
🔮 𝑺𝒖𝒎𝒎𝒐𝒏𝒊𝒏𝒈 {count} 𝒆𝒏𝒕𝒊𝒕𝒊𝒆𝒔...
⚡ 𝑴𝒂𝒏𝒂: 𝑺𝑻𝑨𝑩𝑳𝑬
🌀 𝑷𝒐𝒓𝒕𝒂𝒍: 𝑶𝑷𝑬𝑵
⚔️ {count} 𝒘𝒂𝒓𝒓𝒊𝒐𝒓𝒔 𝒉𝒂𝒗𝒆 𝒂𝒏𝒔𝒘𝒆𝒓𝒆𝒅 𝒕𝒉𝒆 𝒄𝒂𝒍𝒍.
🏰 𝑻𝒉𝒆 𝒍𝒆𝒈𝒊𝒐𝒏 𝒏𝒐𝒘 𝒂𝒘𝒂𝒊𝒕𝒔 𝒚𝒐𝒖𝒓 𝒄𝒐𝒎𝒎𝒂𝒏𝒅."""

ECO_OFF_MSG = """╔════════════════════════════╗
║ 🌿 𝙀𝘾𝙊 𝙈𝙊𝘿𝙀 𝙊𝙁𝙁 ║
╚════════════════════════════╝
☯️ Eco Protocol: 𝘋𝘌𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋
🫧 𝘗𝘖𝘞𝘌𝘙 𝘊𝘖𝘕𝘚𝘜𝘔𝘗𝘛𝘐𝘖𝘕 : 𝘋𝘌𝘍𝘈𝘜𝘓𝘛 
🌱 𝘚𝘠𝘚𝘛𝘌𝘔𝘚: 𝘚𝘌𝘛 𝘛𝘖 𝘕𝘖𝘙𝘔𝘈𝘓

「𝘚𝘈𝘎𝘌 𝘔𝘖𝘋𝘌 𝘋𝘌𝘗𝘈𝘙𝘛𝘌𝘋🔮」"""

ECO_ON_MSG = """╔════════════════════════════╗
║ 🌿 𝙀𝘾𝙊 𝙈𝙊𝘿𝙀 𝙊𝙉  ║
╚════════════════════════════╝
☯️ Eco Protocol: 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋
🔮 𝘗𝘖𝘞𝘌𝘙 𝘊𝘖𝘕𝘚𝘜𝘔𝘗𝘛𝘐𝘖𝘕 : 𝘖𝘗𝘛𝘐𝘔𝘐𝘚𝘡𝘌𝘋. 
🌱 𝘚𝘠𝘚𝘛𝘌𝘔𝘚: 𝘚𝘛𝘈𝘉𝘓𝘐𝘡𝘐𝘌𝘋 

「𝘉𝘈𝘓𝘈𝘕𝘊𝘌 𝘏𝘈𝘚 𝘉𝘌𝘌𝘕 𝘍𝘖𝘙𝘔𝘌𝘋 🔮」"""

RAGE_OFF_MSG = """╔════════════════════════════╗
║🩵 𝘽𝙀𝙍𝙎𝙀𝙍𝙆𝙀𝙍 𝙈𝙊𝘿𝙀 𝙊𝙁𝙁 ║
╚════════════════════════════╝
⚔️ Rage Protocol: 𝘋𝘌𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 
 🍃 𝘛𝘏𝘌 𝘙𝘌𝘚𝘛𝘙𝘈𝘐𝘕𝘛𝘚 𝘏𝘈𝘝𝘌 𝘉𝘌𝘌𝘕 𝘚𝘌𝘛 𝘛𝘖 𝘕𝘖𝘙𝘔𝘈𝘓 . 
🪷 𝘗𝘖𝘞𝘌𝘙 𝘖𝘜𝘛𝘗𝘜𝘛 𝘏𝘈𝘚 𝘉𝘌𝘌𝘕 𝘚𝘌𝘛 𝘛𝘖 𝘕𝘖𝘙𝘔𝘈𝘓.

「𝙒𝘼𝙍 𝙃𝘼𝙎 𝘽𝙀𝙀𝙉 𝗢𝗩𝗘𝗥 💕」"""

RAGE_ON_MSG = """╔════════════════════════════╗
║ 🔥 𝘽𝙀𝙍𝙎𝙀𝙍𝙆𝙀𝙍 𝙈𝙊𝘿𝙀 𝙊𝙉 ║
╚════════════════════════════╝
⚔️ Rage Protocol: 𝘈𝘊𝘛𝘐𝘝𝘈𝘛𝘌𝘋 
👹 𝘛𝘏𝘌 𝘙𝘌𝘚𝘛𝘙𝘈𝘐𝘕𝘛𝘚 𝘏𝘈𝘝𝘌 𝘉𝘌𝘌𝘕 𝘙𝘌𝘓𝘌𝘈𝘚𝘌𝘋 . 
🔥 𝘗𝘖𝘞𝘌𝘙 𝘖𝘜𝘛𝘗𝘜𝘛 𝘏𝘈𝘚 𝘐𝘕𝘊𝘙𝘌𝘈𝘚𝘌𝘋 .

「𝙒𝘼𝙍 𝙃𝘼𝙎 𝘽𝙀𝙀𝙉 𝘿𝙀𝘾𝙇𝘼𝙍𝙀𝘿 👑」"""


class BufferLogger:
    _buffer = deque(maxlen=500)
    _last_flush = 0.0
    _flush_interval = 15.0
    _flush_count = 50
    @classmethod
    def _should_flush(cls):
        return len(cls._buffer) >= cls._flush_count or time.time() - cls._last_flush >= cls._flush_interval
    @classmethod
    def _flush(cls):
        if not cls._buffer: return
        try:
            lf = os.path.join(BUFFER_LOG_DIR, f"buffer_{datetime.now().strftime('%Y%m%d_%H')}.log")
            with open(lf, "a", encoding="utf-8") as f:
                for e in cls._buffer: f.write(e + "\n")
        except Exception: pass
        cls._buffer.clear()
        cls._last_flush = time.time()
    @classmethod
    def log(cls, level, msg):
        line = f"[INST{INSTANCE_ID}] [{datetime.now().strftime('%H:%M:%S')}] [{level}] {msg}"
        print(line)
        cls._buffer.append(line)
        if cls._should_flush(): cls._flush()
    @classmethod
    def info(cls, m): cls.log("INFO", m)
    @classmethod
    def error(cls, m): cls.log("ERROR", m)
    @classmethod
    def warn(cls, m): cls.log("WARN", m)
    @classmethod
    def cmd(cls, c, u, i): cls.log("CMD", f"{c} by {u} in {i}")

ColorLogger = BufferLogger

class HealthCheckup:
    def __init__(self): self.bot_health: Dict[int, Dict[str, Any]] = {}
    def register(self, bot_id):
        self.bot_health[bot_id] = {"score": 100, "total_sent": 0, "total_fail": 0,
                                    "last_error": None, "last_check": time.time(), "flood_until": 0}
    def success(self, bot_id):
        if bot_id in self.bot_health:
            h = self.bot_health[bot_id]
            h["total_sent"] += 1
            h["score"] = min(100, h["score"] + 1)
    def failure(self, bot_id, err=""):
        if bot_id in self.bot_health:
            h = self.bot_health[bot_id]
            h["total_fail"] += 1
            h["score"] = max(0, h["score"] - 5)
    def flood(self, bot_id, sec):
        if bot_id in self.bot_health:
            self.bot_health[bot_id]["flood_until"] = time.time() + sec
    def ratio(self):
        if not self.bot_health: return 1.0
        return sum(1 for h in self.bot_health.values() if h["score"] > 10) / len(self.bot_health)
    def snapshot(self):
        lines = ["🏥 BOT HEALTH"]
        for bid, h in list(self.bot_health.items())[:20]:
            lines.append(f"  {bid}: score={h['score']} sent={h['total_sent']} fail={h['total_fail']}")
        return "\n".join(lines)

health_checkup = HealthCheckup()

class StabilityEngine:
    def __init__(self):
        self.errors_5min = deque(maxlen=1000)
        self.cycles = 0
    def report(self, e): self.errors_5min.append((time.time(), str(e)[:200]))
    def prune(self):
        cutoff = time.time() - 300
        while self.errors_5min and self.errors_5min[0][0] < cutoff: self.errors_5min.popleft()
    def stable(self): self.prune(); return len(self.errors_5min) < 200
    def gc(self):
        try: gc.collect()
        except Exception: pass
    def snapshot(self):
        self.prune()
        return f"⚙️ errs5m={len(self.errors_5min)}"

stability_engine = StabilityEngine()

class AntiFlood:
    def __init__(self):
        self.enabled: Dict[int, bool] = {}
        self._msg_times: Dict[Tuple[int, int], deque] = {}
        self.limit = 5
        self.window = 3.0
    def toggle(self, chat_id, on: bool): self.enabled[chat_id] = on
    def is_on(self, chat_id): return self.enabled.get(chat_id, False)
    def check(self, chat_id, user_id) -> bool:
        if not self.enabled.get(chat_id): return False
        key = (chat_id, user_id)
        now = time.time()
        dq = self._msg_times.setdefault(key, deque(maxlen=self.limit + 2))
        while dq and dq[0] < now - self.window: dq.popleft()
        dq.append(now)
        return len(dq) > self.limit

antiflood = AntiFlood()

class StateManager:
    def __init__(self):
        self.bots: List[Bot] = []
        self.bot_ids_cache: Set[int] = set()
        self.bot_usernames: Dict[int, str] = {}
        self.sudo_users: Set[int] = set(SUDO_IDS) | {OWNER_ID}
        self._load_sudo()
        self.active_chats: Dict[int, Dict[str, bool]] = {}
        self.saved_photos: List[str] = []
        self.saved_voices: List[str] = []
        self.saved_gifs: List[str] = []
        self.saved_stickers: List[str] = []
        self.rage_mode_enabled = False
        self.eco_mode_enabled = False
        self.auto_react_enabled = False
        self.auto_react_emoji = "🤣"
        self.global_react = False
        self.global_react_emoji = "🤣"
        self.react_chats: Dict[int, bool] = {}
        self.react_emoji: Dict[int, str] = {}
        self.mar_active: Dict[int, bool] = {}
        self.purge_chats: Dict[int, bool] = {}
        self.target_slide_active: Dict[int, bool] = {}
        self.target_slide_targets: Dict[int, int] = {}
        self.slaughter_active: Dict[int, bool] = {}
        self.slaughter_targets: Dict[int, int] = {}
        self.swipe_data: Dict[int, str] = {}
        self.target_users: Set[int] = set()
        self.spam_users: Set[int] = set()
        self.rr_active: Dict[int, bool] = {}
        self.rr_targets: Dict[int, int] = {}
        self.rr_user_text: Dict[int, str] = {}
        self.admin_groups: Dict[int, Dict[str, Any]] = {}
        self._load_admin_groups()
        self.delall_running: Dict[int, bool] = {}
        self.fetch_gcs: Dict[int, str] = {}
        self.ncy_active: Dict[int, bool] = {}
        self.ncy_text: Dict[int, str] = {}
        self.ncxy_active: Dict[int, bool] = {}
        self.ncxy_text: Dict[int, str] = {}
        self.ncyx_active: Dict[int, bool] = {}
        self.ncyx_text: Dict[int, str] = {}
        self.ncz_active: Dict[int, bool] = {}
        self.ncz_text: Dict[int, str] = {}
        self.ncwxs_active: Dict[int, bool] = {}
        self.ncwxs_text: Dict[int, str] = {}
        self.ncemo_active: Dict[int, bool] = {}
        self.ncemo_text: Dict[int, str] = {}
        self.ncq_active: Dict[int, bool] = {}
        self.ncq_text: Dict[int, str] = {}
        self.nckeng_active: Dict[int, bool] = {}
        self.nckeng_text: Dict[int, str] = {}
        self.ncgawd_active: Dict[int, bool] = {}
        self.ncgawd_text: Dict[int, str] = {}
        self.whonc_active: Dict[int, bool] = {}
        self.whonc_text: Dict[int, str] = {}
        self.s1_active: Dict[int, bool] = {}
        self.s1_text: Dict[int, str] = {}
        self.s2_active: Dict[int, bool] = {}
        self.s2_text: Dict[int, str] = {}
        self.s3_active: Dict[int, bool] = {}
        self.s3_text: Dict[int, str] = {}
        self.xspam_active: Dict[int, bool] = {}
        self.xspam_text: Dict[int, str] = {}
        self.kengspam_active: Dict[int, bool] = {}
        self.kengspam_text: Dict[int, str] = {}
        self.autopinspam_active: Dict[int, bool] = {}
        self.autopinspam_text: Dict[int, str] = {}
        self.sx_active: Dict[int, bool] = {}
        self.sx_targets: Dict[int, int] = {}
        self.xs_active: Dict[int, bool] = {}
        self.xs_text: Dict[int, str] = {}
        self.xs_counter: Dict[int, int] = {}
        self.x_raid_active: Dict[int, bool] = {}
        self.x_raid_targets: Dict[int, int] = {}
        self.sp_running: Dict[int, bool] = {}
        self.sp_slot: Dict[int, int] = {}
        self.sp_tasks: Dict[int, Any] = {}
        self.slide_running: Dict[int, bool] = {}
        self.slide_slot: Dict[int, int] = {}
        self.slide_targets: Dict[int, Dict[int, int]] = {}
        self.slide_msg_id: Dict[int, int] = {}
        self.poll_running: Dict[int, bool] = {}
        self.poll_tasks: Dict[int, Any] = {}
        self.multitarget_active: Dict[int, bool] = {}
        self.multitarget_targets: Dict[int, Set[int]] = {}
        self.gcpfp_running: Dict[int, bool] = {}
        self.delmsg_running: Dict[int, bool] = {}
        self.gameover_running: Dict[int, bool] = {}

        self.delays: Dict[str, float] = {
            "nc": DEFAULT_NC_DELAY, "nct": DEFAULT_NCT_DELAY,
            "ncs": DEFAULT_NCS_DELAY, "ncp": DEFAULT_NCP_DELAY,
            "ncgod": DEFAULT_NCGOD_DELAY, "ncx": DEFAULT_NCX_DELAY,
            "ncloop": DEFAULT_NCLOOP_DELAY, "whonc": DEFAULT_WHONC_DELAY,
            "nctime": DEFAULT_NCTIME_DELAY, "ncmoon": DEFAULT_NCMOON_DELAY,
            "ncclock": DEFAULT_NCCLOCK_DELAY, "nckeng": DEFAULT_NCKENG_DELAY,
            "ncheart": DEFAULT_NCHEART_DELAY, "ncgawd": DEFAULT_NCGAWD_DELAY,
            "ncy": DEFAULT_NCY_DELAY, "ncxy": DEFAULT_NCXY_DELAY,
            "ncyx": DEFAULT_NCYX_DELAY, "ncz": DEFAULT_NCZ_DELAY,
            "ncwxs": DEFAULT_NCWXS_DELAY, "ncemo": DEFAULT_NCEMO_DELAY,
            "ncq": DEFAULT_NCQ_DELAY,
            "kengspam": DEFAULT_KENGSPAM_DELAY,
            "autopinspam": DEFAULT_AUTOPINSPAM_DELAY,
            "rr": DEFAULT_RR_DELAY, "xspam": DEFAULT_XSPAM_DELAY,
            "xs": DEFAULT_XS_DELAY, "x": DEFAULT_X_DELAY,
            "sx": DEFAULT_SX_DELAY, "slaughter": DEFAULT_SL_DELAY,
            "targetslide": DEFAULT_TS_DELAY, "swipe": DEFAULT_SWIPE_DELAY,
            "mar": DEFAULT_MAR_DELAY, "pfp": DEFAULT_PFP_DELAY,
            "photo": DEFAULT_PHOTO_DELAY, "delmsg": DEFAULT_DELMSG_DELAY,
            "delall": DEFAULT_DELALL_DELAY, "gameover": DEFAULT_GAMEOVER_DELAY,
            "s1": 0.01, "s2": 0.01, "s3": 0.01,
            "sp": DEFAULT_SP_DELAY, "slide": DEFAULT_SLIDE_DELAY,
            "poll": DEFAULT_POLL_DELAY, "multitarget": DEFAULT_MULTITARGET_DELAY,
        }
        self.nc_emoji_delays: Dict[str, float] = {
            "Dnc": 0.1, "Lnc": 0.1, "Knc": 0.1, "Anc": 0.1,
            "Enc": 0.1, "Gnc": 0.1, "Znc": 0.1, "Cnc": 0.1, "Mnc": 0.1,
        }
        self._cmd_cooldowns: Dict[Tuple[int, int], float] = {}
        self.commands_processed = 0

    def _load_sudo(self):
        if os.path.exists(SUDO_FILE):
            try:
                with open(SUDO_FILE) as f:
                    self.sudo_users = set(int(x) for x in json.load(f)) | {OWNER_ID}
            except Exception: pass
    def save_sudo(self):
        try:
            with open(SUDO_FILE, "w") as f: json.dump(list(self.sudo_users), f)
        except Exception: pass
    def _load_admin_groups(self):
        if os.path.exists(ADMIN_GROUPS_FILE):
            try:
                with open(ADMIN_GROUPS_FILE, encoding="utf-8") as f:
                    self.admin_groups = {int(k): v for k, v in json.load(f).items()}
            except Exception: self.admin_groups = {}
    def save_admin_groups(self):
        try:
            with open(ADMIN_GROUPS_FILE, "w", encoding="utf-8") as f:
                json.dump({str(k): v for k, v in self.admin_groups.items()}, f, indent=2)
        except Exception: pass
    def add_admin_group(self, chat_id, title="", source="auto"):
        if chat_id not in self.admin_groups:
            self.admin_groups[chat_id] = {"title": title or "Unknown",
                                          "added_by": source,
                                          "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            self.save_admin_groups()
    def update_bot_ids(self):
        self.bot_ids_cache = {b.id for b in self.bots}
    @property
    def bot_ids(self): return self.bot_ids_cache
    def is_active(self, cid, mode): return self.active_chats.get(cid, {}).get(mode, False)
    def set_active(self, cid, mode, st):
        self.active_chats.setdefault(cid, {})[mode] = st
    def eff_delay(self, mode, base):
        if self.rage_mode_enabled and base > RAGE_MODE_MIN_DELAY: return RAGE_MODE_MIN_DELAY
        if self.eco_mode_enabled and base < ECO_MODE_MIN_DELAY: return ECO_MODE_MIN_DELAY
        return base
    def prune(self):
        now = time.time()
        for k in [k for k, ts in self._cmd_cooldowns.items() if now - ts > 20]: del self._cmd_cooldowns[k]
    def stop_all(self, cid):
        for m in list(self.active_chats.get(cid, {}).keys()):
            self.active_chats[cid][m] = False
        for attr in ["slaughter_active", "target_slide_active", "rr_active",
                     "gcpfp_running", "purge_chats", "mar_active", "delall_running",
                     "ncy_active", "ncxy_active", "ncyx_active", "ncz_active",
                     "ncwxs_active", "ncemo_active", "ncq_active", "nckeng_active",
                     "ncgawd_active", "whonc_active", "s1_active", "s2_active",
                     "s3_active", "xspam_active", "kengspam_active",
                     "autopinspam_active", "sx_active", "xs_active",
                     "x_raid_active", "delmsg_running", "sp_running", "slide_running",
                     "poll_running", "multitarget_active"]:
            try: getattr(self, attr)[cid] = False
            except Exception: pass
        t = self.sp_tasks.get(cid)
        if t and not t.done(): t.cancel()
        self.sp_tasks.pop(cid, None)
        t2 = self.poll_tasks.get(cid)
        if t2 and not t2.done(): t2.cancel()
        self.poll_tasks.pop(cid, None)
        self.sp_slot.pop(cid, None)
        self.slide_slot.pop(cid, None)
        self.slide_targets.pop(cid, None)
        self.slide_msg_id.pop(cid, None)
        self.multitarget_targets.pop(cid, None)
        self.swipe_data.pop(cid, None)
        self.kengspam_text.pop(cid, None)
        self.autopinspam_text.pop(cid, None)

state = StateManager()

def safe_unicode_truncate(text: str, max_len: int) -> str:
    if not text or len(text) <= max_len: return text
    truncated = text[:max_len]
    while truncated:
        last = truncated[-1]
        code = ord(last)
        if 0xD800 <= code <= 0xDBFF: truncated = truncated[:-1]; continue
        if code == 0x200D: truncated = truncated[:-1]; continue
        if 0xFE00 <= code <= 0xFE0F: truncated = truncated[:-1]; continue
        if 0x1F3FB <= code <= 0x1F3FF: truncated = truncated[:-1]; continue
        break
    return truncated

def safe_chunk_text(text: str, max_len: int = 4000) -> List[str]:
    if not text: return []
    if len(text) <= max_len: return [text]
    chunks = []
    remaining = text
    while remaining:
        if len(remaining) <= max_len:
            chunks.append(remaining); break
        cut = max_len
        newline_pos = remaining.rfind('\n', 0, cut)
        if newline_pos > max_len // 2:
            cut = newline_pos + 1
        else:
            chunk = remaining[:cut]
            while chunk:
                last = chunk[-1]
                code = ord(last)
                if 0xD800 <= code <= 0xDBFF: chunk = chunk[:-1]; continue
                if code == 0x200D or (0xFE00 <= code <= 0xFE0F) or (0x1F3FB <= code <= 0x1F3FF):
                    chunk = chunk[:-1]; continue
                break
            cut = len(chunk)
        chunk = remaining[:cut]
        if chunk: chunks.append(chunk)
        remaining = remaining[cut:]
    return chunks

async def _gather_ignore(*tasks):
    if tasks: await asyncio.gather(*tasks, return_exceptions=True)

def fire_and_forget(coro):
    try: return asyncio.create_task(coro)
    except Exception as e:
        ColorLogger.error(f"f&f: {e}"); return None

def gather_bg(*tasks):
    try: return asyncio.create_task(_gather_ignore(*tasks))
    except Exception as e:
        ColorLogger.error(f"bg: {e}"); return None

def get_uptime():
    s = int(time.time() - BOT_START_TIME)
    return f"{s//86400}d {(s%86400)//3600}h {(s%3600)//60}m {s%60}s"

def ist_time():
    return datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%H:%M:%S")

def ist_date():
    return datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y")

def is_owner(uid): return uid == OWNER_ID
def _random_smoji(): return random.choice(SMOJI_POOL)

async def safe_reply(update, text, parse_mode=None, reply_markup=None):
    if not update or not update.effective_message: return None
    msg = update.effective_message
    safe_text = safe_unicode_truncate(text, 4000)
    for kw in ({"parse_mode": parse_mode, "reply_markup": reply_markup},
               {"reply_markup": reply_markup}, {}):
        try:
            return await msg.reply_text(safe_text, **{k: v for k, v in kw.items() if v is not None})
        except Exception: continue
    try:
        return await msg.get_bot().send_message(msg.chat_id, safe_text, reply_markup=reply_markup)
    except Exception: return None

async def send_dual(bot, cid, text, **kw):
    if not text: return None
    chunks = safe_chunk_text(text, 4000)
    for chunk in chunks:
        for a in (kw, {**kw, "parse_mode": None},
                  {k: v for k, v in kw.items() if k != "reply_to_message_id"}, {}):
            try:
                return await bot.send_message(cid, chunk, **a)
            except Exception: continue
    return None

async def set_title_dual(bot, cid, t):
    if not t: return None
    safe_t = safe_unicode_truncate(t, 255)
    for n in (255, 128, 64):
        try:
            return await bot.set_chat_title(cid, safe_t[:n])
        except Exception: continue
    try:
        c = re.sub(r'[^\x20-\x7E\u00A0-\uFFFF]', '', t)[:64]
        return await bot.set_chat_title(cid, c or "NC")
    except Exception: return None

def download_photo_sync(url: str, save_path: str) -> bool:
    try:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        r = requests.get(url, headers=headers, timeout=30, stream=True)
        if r.status_code != 200: return False
        with open(save_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: f.write(chunk)
        return os.path.getsize(save_path) > 500
    except Exception:
        return False
    # ═══════════════════════════════════════════════════════════════════════════════
#                              WORKERS
# ═══════════════════════════════════════════════════════════════════════════════

async def sp_loop(cid: int, sp_num: int, extra: str):
    while state.sp_running.get(cid, False):
        try:
            active_texts = SP_TEXTS_ACTIVE.get(sp_num, [])
            if not active_texts:
                await asyncio.sleep(0.2)
                continue
            spam_text = random.choice(active_texts)
            if extra:
                spam_text = spam_text.replace("{{target}}", extra)
            else:
                spam_text = spam_text.replace("{{target}}", "")
            chunks = safe_chunk_text(spam_text, 4000)
            async def _send(bot, chunks=chunks):
                for ch in chunks[:3]:
                    try:
                        await bot.send_message(cid, ch)
                        health_checkup.success(bot.id)
                    except RetryAfter as e:
                        health_checkup.flood(bot.id, e.retry_after)
                        await asyncio.sleep(min(e.retry_after + 0.3, 5))
                    except Exception:
                        pass
            await _gather_ignore(*[asyncio.create_task(_send(b)) for b in state.bots])
            d = state.delays.get("sp", 0.0)
            await asyncio.sleep(state.eff_delay("sp", d) if d > 0 else 0)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.1)


async def continuous_slide_loop(cid: int, message_id: int, slide_num: int):
    all_texts = SLIDE_TEXTS_ACTIVE.get(slide_num, [])
    n_texts = len(all_texts)
    if n_texts == 0:
        return
    i = 0
    while state.slide_running.get(cid, False):
        try:
            text = all_texts[i % n_texts]
            text = text.replace("{{target}}", "")
            chunks = safe_chunk_text(text, 4000)
            async def _send(bot, chunks=chunks):
                for ch in chunks[:2]:
                    try:
                        await bot.send_message(cid, ch, reply_to_message_id=message_id)
                        health_checkup.success(bot.id)
                    except RetryAfter as e:
                        health_checkup.flood(bot.id, e.retry_after)
                        await asyncio.sleep(min(e.retry_after + 0.3, 5))
                    except Exception:
                        pass
            await _gather_ignore(*[asyncio.create_task(_send(b)) for b in state.bots])
            i += 1
            d = state.delays.get("slide", 0.1)
            await asyncio.sleep(state.eff_delay("slide", d) if d > 0 else 0)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.1)


async def poll_loop(cid: int, question: str, opt1: str, opt2: str):
    while state.poll_running.get(cid, False):
        try:
            q = question.replace("(test)", "").strip() or "Poll"
            o1 = opt1.replace("(test)", "").strip() or "Option 1"
            o2 = opt2.replace("(test)", "").strip() or "Option 2"
            o1 = o1.replace("(semoji)", _random_smoji()).replace("(smoji)", _random_smoji()).replace("(emoji)", _random_smoji())
            o2 = o2.replace("(semoji)", _random_smoji()).replace("(smoji)", _random_smoji()).replace("(emoji)", _random_smoji())
            q = q.replace("<semoji>", _random_smoji()).replace("<smoji>", _random_smoji())
            def apply_multiplier(txt):
                m = re.search(r"\*(\d+)\s*$", txt)
                if m:
                    try: mult = int(m.group(1))
                    except Exception: mult = 1
                    txt = txt[:m.start()].rstrip()
                    txt = txt * max(1, mult)
                return txt
            o1 = apply_multiplier(o1)
            o2 = apply_multiplier(o2)
            q = safe_unicode_truncate(q, 290)
            o1 = safe_unicode_truncate(o1, 90)
            o2 = safe_unicode_truncate(o2, 90)
            async def _send(bot):
                try:
                    await bot.send_poll(
                        chat_id=cid,
                        question=q,
                        options=[o1, o2],
                        is_anonymous=False,
                        allows_multiple_answers=False,
                    )
                    health_checkup.success(bot.id)
                except RetryAfter as e:
                    health_checkup.flood(bot.id, e.retry_after)
                    await asyncio.sleep(min(e.retry_after + 0.3, 5))
                except Exception:
                    pass
            await _gather_ignore(*[asyncio.create_task(_send(b)) for b in state.bots])
            d = state.delays.get("poll", 0.005)
            await asyncio.sleep(state.eff_delay("poll", d) if d > 0 else 0)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.05)


async def multitarget_worker(cid: int):
    while state.multitarget_active.get(cid, False):
        try:
            targets = state.multitarget_targets.get(cid, set())
            if not targets:
                await asyncio.sleep(0.3)
                continue
            async def _send_one(bot, target_id):
                try:
                    name = f"User{target_id}"
                    try:
                        ch = await bot.get_chat(target_id)
                        name = ch.first_name or f"User{target_id}"
                    except Exception: pass
                    mention = f"[{name}](tg://user?id={target_id})"
                    body = f"{mention} {random.choice(SX_TEXTS)}"
                    try:
                        await bot.send_message(cid, body, parse_mode=ParseMode.MARKDOWN)
                    except Exception:
                        try:
                            await bot.send_message(cid, f"{name} {random.choice(SX_TEXTS)}")
                        except Exception: pass
                    health_checkup.success(bot.id)
                except RetryAfter as e:
                    health_checkup.flood(bot.id, e.retry_after)
                    await asyncio.sleep(min(e.retry_after + 0.3, 5))
                except Exception:
                    pass
            tasks = []
            for b in state.bots:
                for tid in targets:
                    tasks.append(asyncio.create_task(_send_one(b, tid)))
            await _gather_ignore(*tasks)
            d = state.delays.get("multitarget", 0.001)
            await asyncio.sleep(state.eff_delay("multitarget", d) if d > 0 else 0)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.05)


# ═══════════════════════════════════════════════════════════════════════════════
#                              WHONC WORKER
# ═══════════════════════════════════════════════════════════════════════════════

async def whonc_worker(cid: int, base: str):
    """whonc: uses the 17 WHONC_TEXTS with (test) replaced by base + loop emoji appended."""
    while state.whonc_active.get(cid, False):
        try:
            if not WHONC_TEXTS_ACTIVE:
                await asyncio.sleep(0.3); continue
            tpl = random.choice(WHONC_TEXTS_ACTIVE)
            txt = re.sub(r"\([Tt]est\)", base, tpl).strip()
            loop_emoji = random.choice(NC_LOOP_EMOJIS)
            txt = f"{txt} {loop_emoji}"
            for b in state.bots:
                if not state.whonc_active.get(cid, False): break
                try:
                    await set_title_dual(b, cid, txt)
                except RetryAfter as e:
                    await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
                except BadRequest as e:
                    if "not enough rights" in str(e).lower(): return
                except Exception:
                    pass
            d = state.delays.get("whonc", 0.5)
            await asyncio.sleep(state.eff_delay("whonc", d) if d > 0 else 0)
        except asyncio.CancelledError:
            return
        except Exception:
            await asyncio.sleep(0.05)


# ═══════════════════════════════════════════════════════════════════════════════
#                              NC WORKERS
# ═══════════════════════════════════════════════════════════════════════════════

class NCWorkers:
    @staticmethod
    async def _basic(bot, cid, base, mode, generator):
        while state.is_active(cid, mode):
            try:
                text = generator(base)
                await set_title_dual(bot, cid, text)
                d = state.delays.get(mode, 0.01)
                await asyncio.sleep(state.eff_delay(mode, d))
                health_checkup.success(bot.id)
            except asyncio.CancelledError: return
            except RetryAfter as e:
                w = getattr(e, "retry_after", 1)
                health_checkup.flood(bot.id, w + 0.3)
                await asyncio.sleep(min(w + 0.3, 5))
            except BadRequest as e:
                err = str(e).lower()
                if "not enough rights" in err or "chat_admin_required" in err:
                    return
                await asyncio.sleep(0)
            except Exception:
                await asyncio.sleep(0)

    @staticmethod
    async def _indexed(bot, cid, base, mode, generator):
        i = 0
        while state.is_active(cid, mode):
            try:
                text = generator(base, i)
                await set_title_dual(bot, cid, text)
                d = state.delays.get(mode, 0.001)
                await asyncio.sleep(state.eff_delay(mode, d))
                i += 1
                health_checkup.success(bot.id)
            except asyncio.CancelledError: return
            except RetryAfter as e:
                w = getattr(e, "retry_after", 1)
                health_checkup.flood(bot.id, w + 0.3)
                await asyncio.sleep(min(w + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception:
                await asyncio.sleep(0)

    @staticmethod
    async def _ncgod(bot, cid, base):
        while state.is_active(cid, "ncgod"):
            try:
                async def one_call():
                    try:
                        tpl = random.choice(NCGOD_LINES)
                        await set_title_dual(bot, cid, f"{base} {tpl}")
                    except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one_call())
                                       for _ in range(NCGOD_PARALLEL)])
                d = state.delays.get("ncgod", 0.001)
                await asyncio.sleep(state.eff_delay("ncgod", d))
                health_checkup.success(bot.id)
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _whonc(bot, cid, base):
        while state.whonc_active.get(cid, False):
            try:
                if WHONC_TEXTS_ACTIVE:
                    tpl = random.choice(WHONC_TEXTS_ACTIVE)
                    txt = re.sub(r"\([Tt]est\)", base, tpl).strip()
                    e = random.choice(NC_LOOP_EMOJIS)
                    await set_title_dual(bot, cid, f"{txt} {e}")
                d = state.delays.get("whonc", 0.5)
                await asyncio.sleep(state.eff_delay("whonc", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _ncxy(bot, cid, base):
        while state.ncxy_active.get(cid, False):
            try:
                e = random.choice(NC_LOOP_EMOJIS)
                await set_title_dual(bot, cid, f"{e} {base} {e}")
                d = state.delays.get("ncxy", 0.05)
                await asyncio.sleep(state.eff_delay("ncxy", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _ncyx(cid, base):
        while state.ncyx_active.get(cid, False):
            try:
                for b in state.bots:
                    if not state.ncyx_active.get(cid, False): break
                    for _ in range(NCYX_BURST):
                        if not state.ncyx_active.get(cid, False): break
                        try:
                            e = random.choice(NC_LOOP_EMOJIS)
                            await set_title_dual(b, cid, f"{e} {base} {e}")
                            d = state.delays.get("ncyx", 0.1)
                            await asyncio.sleep(state.eff_delay("ncyx", d))
                        except RetryAfter as ex:
                            await asyncio.sleep(min(getattr(ex, "retry_after", 1) + 0.3, 5))
                        except BadRequest as ex:
                            if "not enough rights" in str(ex).lower(): break
                            await asyncio.sleep(0)
                        except Exception: await asyncio.sleep(0)
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.1)

    @staticmethod
    async def _ncz(cid, base):
        base_lower = base.lower()[:30]
        while state.ncz_active.get(cid, False):
            try:
                cur_title = None
                for b in state.bots:
                    if not state.ncz_active.get(cid, False): break
                    try:
                        chat = await b.get_chat(cid)
                        cur_title = chat.title or ""
                        break
                    except Exception: continue
                if cur_title is None:
                    await asyncio.sleep(state.eff_delay("ncz", state.delays.get("ncz", 0.7)))
                    continue
                if base_lower not in cur_title.lower():
                    e = random.choice(NC_LOOP_EMOJIS)
                    text = f"{e} {base} {e}"
                    async def one(bot):
                        try: await set_title_dual(bot, cid, text)
                        except Exception: pass
                    await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                await asyncio.sleep(state.eff_delay("ncz", state.delays.get("ncz", 0.7)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.7)

    @staticmethod
    async def _ncwxs(bot, cid, base):
        while state.ncwxs_active.get(cid, False):
            try:
                e = random.choice(NC_LOOP_EMOJIS)
                await set_title_dual(bot, cid, f"{e} {base} {e}")
                d = state.delays.get("ncwxs", 0.5)
                await asyncio.sleep(state.eff_delay("ncwxs", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _ncemo(bot, cid, base):
        while state.ncemo_active.get(cid, False):
            try:
                e = random.choice(NC_LOOP_EMOJIS)
                await set_title_dual(bot, cid, f"{e} {base} {e}")
                d = state.delays.get("ncemo", 0.05)
                await asyncio.sleep(state.eff_delay("ncemo", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _ncq(cid, base):
        while state.ncq_active.get(cid, False):
            try:
                async def one(bot):
                    for _ in range(5):
                        if not state.ncq_active.get(cid, False): return
                        try:
                            e = random.choice(NC_LOOP_EMOJIS)
                            await set_title_dual(bot, cid, f"{e} {base} {e}")
                        except RetryAfter as ex:
                            await asyncio.sleep(min(getattr(ex, "retry_after", 1) + 0.3, 3))
                        except BadRequest as ex:
                            if "not enough rights" in str(ex).lower(): return
                            return
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                d = state.delays.get("ncq", 0.001)
                await asyncio.sleep(state.eff_delay("ncq", d))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _nckeng(bot, cid, base):
        while state.nckeng_active.get(cid, False):
            try:
                e = random.choice(KENG_EMOJIS)
                await set_title_dual(bot, cid, f"{e} {base} {e}")
                d = state.delays.get("nckeng", 0.1)
                await asyncio.sleep(state.eff_delay("nckeng", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    async def _ncgawd(bot, cid, base):
        while state.ncgawd_active.get(cid, False):
            try:
                e = random.choice(GAWD_EMOJIS)
                await set_title_dual(bot, cid, f"{base} {e}")
                d = state.delays.get("ncgawd", 0.001)
                await asyncio.sleep(state.eff_delay("ncgawd", d))
            except asyncio.CancelledError: return
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 1) + 0.3, 5))
            except BadRequest as e:
                if "not enough rights" in str(e).lower(): return
                await asyncio.sleep(0)
            except Exception: await asyncio.sleep(0)

    @staticmethod
    def stop_all(cid):
        for m in ["nc", "nct", "ncs", "ncp", "nctime", "ncgod", "ncx", "ncloop",
                  "ncmoon", "ncclock", "nckeng", "ncheart", "ncgawd", "ncy",
                  "ncxy", "ncyx", "ncz", "ncwxs", "ncemo", "ncq"]:
            state.set_active(cid, m, False)
        for attr in ["ncy_active", "ncxy_active", "ncyx_active", "ncz_active",
                     "ncwxs_active", "ncemo_active", "ncq_active",
                     "nckeng_active", "ncgawd_active", "whonc_active"]:
            try: getattr(state, attr)[cid] = False
            except Exception: pass
        for m in NC_EMOJI_MODES:
            state.set_active(cid, f"nc{m.lower()}", False)


# ═══════════════════════════════════════════════════════════════════════════════
#                    FIXED ADDALL — Direct add + fallbacks
# ═══════════════════════════════════════════════════════════════════════════════

async def _resolve_username(bot, username: str):
    if not username: return None, None
    uname = username.strip()
    if not uname.startswith("@"): uname = "@" + uname
    try:
        chat = await bot.get_chat(uname)
        return chat.id, chat
    except Exception:
        return None, None


async def promote_bot(promoter_bot: Bot, cid: int, bot_id: int):
    try:
        await promoter_bot.promote_chat_member(
            cid, bot_id,
            can_manage_chat=True, can_delete_messages=True,
            can_manage_video_chats=True, can_restrict_members=True,
            can_promote_members=True, can_change_info=True,
            can_invite_users=True, can_pin_messages=True,
        )
        return True
    except Exception:
        return False


async def addall_via_invite(update, context, adder_bot: Bot):
    """FIXED: Direct add each bot by ID (invite links don't work for bots)."""
    chat_id = update.effective_chat.id
    try:
        invite_link = None
        try:
            link_obj = await adder_bot.create_chat_invite_link(
                chat_id=chat_id,
                name="Bot Join Link",
                creates_join_request=False,
            )
            invite_link = link_obj.invite_link
        except Exception:
            pass

        await update.message.reply_text(f"🔄 **Joining All Bots...**")

        joined = 0
        failed = 0
        failed_names = []

        for bot in state.bots:
            if bot.id == adder_bot.id:
                continue
            me = None
            try:
                me = await bot.get_me()
            except Exception:
                failed += 1
                failed_names.append("unknown")
                continue

            bot_name = f"@{me.username}" if me.username else str(bot.id)
            added = False

            # Method 1: Direct add by user ID
            try:
                await adder_bot.add_chat_member(chat_id, bot.id)
                joined += 1
                added = True
                await asyncio.sleep(1.2)
            except RetryAfter as e:
                await asyncio.sleep(min(getattr(e, "retry_after", 3) + 1, 10))
                try:
                    await adder_bot.add_chat_member(chat_id, bot.id)
                    joined += 1
                    added = True
                    await asyncio.sleep(1.2)
                except Exception:
                    pass
            except BadRequest as e:
                err = str(e).lower()
                if "already" in err or "participant" in err:
                    joined += 1
                    added = True
            except Exception:
                pass

            # Method 2: Invite link
            if not added and invite_link:
                try:
                    await bot.join_chat(invite_link)
                    joined += 1
                    added = True
                    await asyncio.sleep(1.2)
                except Exception:
                    pass

            # Method 3: Add by username
            if not added and me.username:
                try:
                    await adder_bot.add_chat_member(chat_id, f"@{me.username}")
                    joined += 1
                    added = True
                    await asyncio.sleep(1.2)
                except Exception:
                    pass

            if added:
                try:
                    await promote_bot(adder_bot, chat_id, bot.id)
                except Exception:
                    pass
                await asyncio.sleep(0.5)
            else:
                failed += 1
                failed_names.append(bot_name)

        # Cleanup invite link
        if invite_link:
            try:
                await adder_bot.revoke_chat_invite_link(chat_id, invite_link)
            except Exception:
                pass

        msg = f"✅ **Done!**\n\n➕ Joined: **{joined}**\n❌ Failed: **{failed}**"
        if failed_names:
            msg += "\n\n**Failed bots:**\n" + "\n".join(f"• {n}" for n in failed_names[:10])
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
#                              MAIN BOT
# ═══════════════════════════════════════════════════════════════════════════════

class WhoAbbuBot:
    def __init__(self):
        self.leader_bot: Optional[Bot] = None

    async def init_bots(self):
        print("═" * 60)
        print(f"       𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘈𝘉𝘉𝘜 𝘝6 👑 [INSTANCE {INSTANCE_ID}]")
        print("═" * 60)
        for i, t in enumerate(BOT_TOKENS, 1):
            try:
                b = Bot(token=t)
                me = await b.get_me()
                state.bots.append(b)
                state.bot_usernames[b.id] = me.username or ""
                health_checkup.register(b.id)
                print(f"✅ {i}/{len(BOT_TOKENS)}: @{me.username}")
            except Exception as e:
                print(f"❌ {i}/{len(BOT_TOKENS)}: {e}")
        state.update_bot_ids()
        if not state.bots:
            print("❌ No bots!"); sys.exit(1)
        self.leader_bot = state.bots[0]
        me = await self.leader_bot.get_me()
        print(f"\n🤖 {len(state.bots)} bots\n")
        try:
            download_photo_sync(HELP_PHOTO_URL, HELP_PHOTO_PATH)
            download_photo_sync(GAMEOVER_PHOTO_URL, GAMEOVER_PHOTO_PATH)
        except Exception as e:
            ColorLogger.warn(f"photo predownload: {e}")

    @staticmethod
    def is_cmd(text):
        if not text: return False, ""
        for p in CMD_PREFIXES:
            if text.startswith(p):
                r = text[len(p):].strip()
                if not r: return False, ""
                raw = r.split()[0].lower()
                return True, raw.split("@")[0] if raw else ""
        return False, ""

    @staticmethod
    def box(title: str, body: str = "", emoji: str = "✅") -> str:
        t = title.upper()
        lines = [f"╭━━━〔 {emoji} {t} 〕━━━╮", "┃", f"┃  {emoji} {t}", "┃"]
        if body:
            lines.append(f"┃  {body}"); lines.append("┃")
        lines.append("╰━━━━━━━━━━━━━━━━━━━━━━╯")
        return "\n".join(lines)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            msg = update.effective_message
            if not msg: return
            cid = msg.chat_id
            uid = update.effective_user.id if update.effective_user else 0
            txt = msg.text or msg.caption or ""

            if msg.chat.type in ("group", "supergroup"):
                state.add_admin_group(cid, msg.chat.title or "", "auto")
                state.fetch_gcs[cid] = msg.chat.title or "Unknown"

            is_cmd, cmd = self.is_cmd(txt)

            if is_cmd and uid in state.sudo_users:
                if cmd == "purge":
                    try: await msg.delete()
                    except Exception: pass
                    state.purge_chats[cid] = True
                    return
                if cmd == "unpurge":
                    try: await msg.delete()
                    except Exception: pass
                    state.purge_chats[cid] = False
                    return

            if state.purge_chats.get(cid):
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    try: await msg.delete(); return
                    except Exception: pass

            if antiflood.is_on(cid) and uid not in state.bot_ids and uid not in state.sudo_users:
                if antiflood.check(cid, uid):
                    try:
                        await msg.delete()
                        await context.bot.send_message(cid, f"🚫 {update.effective_user.first_name} flood detected!")
                    except Exception: pass
                    return

            if uid not in state.bot_ids:
                if state.mar_active.get(cid):
                    emoji_pool = MAR_EMOJIS.copy()
                    random.shuffle(emoji_pool)
                    async def mar_react(bot, emoji):
                        try:
                            await bot.set_message_reaction(cid, msg.message_id,
                                reaction=[ReactionTypeEmoji(emoji)])
                        except Exception: pass
                    tasks = []
                    for i, b in enumerate(state.bots):
                        e = emoji_pool[i % len(emoji_pool)]
                        tasks.append(asyncio.create_task(mar_react(b, e)))
                    gather_bg(*tasks)
                    await asyncio.sleep(state.delays.get("mar", 0.0001))
                elif state.global_react:
                    async def g_react(bot, e):
                        try:
                            await bot.set_message_reaction(cid, msg.message_id,
                                reaction=[ReactionTypeEmoji(e)])
                        except Exception: pass
                    gather_bg(*[asyncio.create_task(g_react(b, state.global_react_emoji))
                                for b in state.bots])
                elif state.react_chats.get(cid) and uid in state.sudo_users:
                    e = state.react_emoji.get(cid, "🤣")
                    async def c_react(bot):
                        try:
                            await bot.set_message_reaction(cid, msg.message_id,
                                reaction=[ReactionTypeEmoji(e)])
                        except Exception: pass
                    chosen = state.bots if uid == OWNER_ID else random.sample(state.bots, min(5, len(state.bots)))
                    gather_bg(*[asyncio.create_task(c_react(b)) for b in chosen])
                elif state.auto_react_enabled:
                    async def a_react(bot):
                        try:
                            await bot.set_message_reaction(cid, msg.message_id,
                                reaction=[ReactionTypeEmoji(state.auto_react_emoji)])
                        except Exception: pass
                    gather_bg(*[asyncio.create_task(a_react(b)) for b in state.bots])

            if state.rr_active.get(cid):
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    tid = state.rr_targets.get(cid)
                    if tid and uid == tid:
                        ut = state.rr_user_text.get(cid, "")
                        name = update.effective_user.first_name or "User"
                        mention = f"[{name}](tg://user?id={tid})"
                        body = f"{mention} {ut} {random.choice(RR_TEXTS)}"
                        async def rr_t(bot):
                            for _ in range(25):
                                if not state.rr_active.get(cid): return
                                try:
                                    await bot.send_message(cid, body,
                                        reply_to_message_id=msg.message_id,
                                        parse_mode=ParseMode.MARKDOWN)
                                except Exception:
                                    try:
                                        await bot.send_message(cid, body,
                                            reply_to_message_id=msg.message_id)
                                    except Exception: pass
                                await asyncio.sleep(0.02)
                            await asyncio.sleep(2)
                        gather_bg(*[asyncio.create_task(rr_t(b)) for b in state.bots])

            if state.slaughter_active.get(cid) and state.slaughter_targets.get(cid) == uid:
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    name = update.effective_user.first_name or "User"
                    mention = f"[{name}](tg://user?id={uid})"
                    async def sl(bot):
                        for _ in range(25):
                            if not state.slaughter_active.get(cid): return
                            try:
                                await send_dual(bot, cid, f"{mention} {random.choice(SLAUGHTER_TEXTS)}",
                                                reply_to_message_id=msg.message_id,
                                                parse_mode=ParseMode.MARKDOWN)
                            except Exception: pass
                            await asyncio.sleep(state.delays.get("slaughter", 0.04))
                        await asyncio.sleep(2)
                    gather_bg(*[asyncio.create_task(sl(b)) for b in state.bots])

            if state.target_slide_active.get(cid) and state.target_slide_targets.get(cid) == uid:
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    name = update.effective_user.first_name or "User"
                    mention = f"[{name}](tg://user?id={uid})"
                    async def ts(bot):
                        for _ in range(25):
                            if not state.target_slide_active.get(cid): return
                            try:
                                await send_dual(bot, cid, f"{mention} {random.choice(TARGET_SLIDE_TEXTS)}",
                                                reply_to_message_id=msg.message_id,
                                                parse_mode=ParseMode.MARKDOWN)
                            except Exception: pass
                            await asyncio.sleep(state.delays.get("targetslide", 0.04))
                        await asyncio.sleep(2)
                    gather_bg(*[asyncio.create_task(ts(b)) for b in state.bots])

            if state.sx_active.get(cid) and state.sx_targets.get(cid) == uid:
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    name = update.effective_user.first_name or "User"
                    mention = f"[{name}](tg://user?id={uid})"
                    async def sx_burst(bot):
                        for _ in range(10):
                            if not state.sx_active.get(cid): return
                            try:
                                body = f"{mention} {random.choice(SX_TEXTS)}"
                                try:
                                    await bot.send_message(cid, body,
                                        reply_to_message_id=msg.message_id,
                                        parse_mode=ParseMode.MARKDOWN)
                                except Exception:
                                    await bot.send_message(cid, body,
                                        reply_to_message_id=msg.message_id)
                            except Exception: pass
                            await asyncio.sleep(state.delays.get("sx", 0.01))
                    gather_bg(*[asyncio.create_task(sx_burst(b)) for b in state.bots])

            if uid in state.multitarget_targets.get(cid, set()) and uid not in state.bot_ids:
                if state.multitarget_active.get(cid, False):
                    name = update.effective_user.first_name or "User"
                    mention = f"[{name}](tg://user?id={uid})"
                    async def mt_hit(bot):
                        try:
                            body = f"{mention} {random.choice(SX_TEXTS)}"
                            try:
                                await bot.send_message(cid, body,
                                    reply_to_message_id=msg.message_id,
                                    parse_mode=ParseMode.MARKDOWN)
                            except Exception:
                                await bot.send_message(cid, body,
                                    reply_to_message_id=msg.message_id)
                        except Exception: pass
                        await asyncio.sleep(state.delays.get("multitarget", 0.001))
                    gather_bg(*[asyncio.create_task(mt_hit(b)) for b in state.bots])

            if txt and uid not in state.sudo_users:
                if cid in state.swipe_data or uid in state.target_users or uid in state.spam_users:
                    prefix = ""
                    if cid in state.swipe_data and state.swipe_data[cid] != "ONLY_RAID_TEXT":
                        prefix = state.swipe_data[cid] + " "
                    asyncio.create_task(self._swipe(cid, msg, prefix, uid))

            if state.x_raid_active.get(cid) and state.x_raid_targets.get(cid) == uid:
                if uid not in state.sudo_users and uid not in state.bot_ids:
                    name = update.effective_user.first_name or "User"
                    mention = f"[{name}](tg://user?id={uid})"
                    if self.leader_bot:
                        try: await self.leader_bot.delete_message(cid, msg.message_id)
                        except Exception: pass
                    async def x_r(bot):
                        for _ in range(50):
                            if not state.x_raid_active.get(cid): return
                            try:
                                await bot.send_message(cid, f"{mention} {random.choice(XTEXT_RAID)}",
                                    reply_to_message_id=msg.message_id,
                                    parse_mode=ParseMode.MARKDOWN)
                            except Exception: pass
                            await asyncio.sleep(state.delays.get("x", 0.02))
                    gather_bg(*[asyncio.create_task(x_r(b)) for b in state.bots])

            if txt and uid not in state.bot_ids and cid in state.slide_targets:
                if uid in state.slide_targets[cid]:
                    slide_num = state.slide_targets[cid][uid]
                    state.slide_running[cid] = True
                    state.slide_slot[cid] = slide_num
                    state.slide_msg_id[cid] = msg.message_id
                    fire_and_forget(continuous_slide_loop(cid, msg.message_id, slide_num))

            if is_cmd:
                if uid not in state.sudo_users: return
                ColorLogger.cmd(cmd, uid, cid)
                state.commands_processed += 1
                if uid != OWNER_ID:
                    k = (uid, cmd)
                    if time.time() - state._cmd_cooldowns.get(k, 0) < 2: return
                    state._cmd_cooldowns[k] = time.time()
                    if state.commands_processed % 500 == 0: state.prune()
                await self.dispatch(update, context, cmd, cid, uid, txt)
        except Exception as e:
            stability_engine.report(e)
            ColorLogger.error(f"handler: {e}")

    async def _swipe(self, cid, msg, prefix, uid):
        name = "User"
        try:
            if msg.from_user: name = msg.from_user.first_name or "User"
        except Exception: pass
        mention = f"[{name}](tg://user?id={uid})"
        async def one(bot):
            for _ in range(25):
                if not (cid in state.swipe_data or uid in state.target_users or uid in state.spam_users): break
                try:
                    await send_dual(bot, cid, f"{mention} {prefix}{random.choice(SWIPE_TEXTS)}",
                                    reply_to_message_id=msg.message_id,
                                    parse_mode=ParseMode.MARKDOWN)
                except Exception: pass
                await asyncio.sleep(state.delays.get("swipe", 0.04))
            await asyncio.sleep(2)
        gather_bg(*[asyncio.create_task(one(b)) for b in state.bots])

    async def dispatch(self, update, context, cmd, cid, uid, txt):
        parts = txt.split()
        args = parts[1:] if len(parts) > 1 else []
        try:
            if cmd in ("help", "h", "start"):
                await self.cmd_help(update, args)
            elif cmd in ("help1", "h1"): await self.cmd_help_page(update, 1)
            elif cmd in ("help2", "h2"): await self.cmd_help_page(update, 2)
            elif cmd in ("help3", "h3"): await self.cmd_help_page(update, 3)
            elif cmd in ("help4", "h4"): await self.cmd_help_page(update, 4)
            elif cmd in ("help5", "h5"): await self.cmd_help_page(update, 5)
            elif cmd in ("help6", "h6"): await self.cmd_help_page(update, 6)
            elif cmd in ("help7", "h7"): await self.cmd_help_page(update, 7)
            elif cmd in ("help8", "h8"): await self.cmd_help_page(update, 8)
            elif cmd in ("help9", "h9"): await self.cmd_help_page(update, 9)

            elif cmd == "ping": await self.cmd_ping(update)
            elif cmd == "status": await self.cmd_status(update)
            elif cmd == "uptime": await safe_reply(update, f"⏰ {get_uptime()}")
            elif cmd == "health": await safe_reply(update, health_checkup.snapshot())
            elif cmd == "rfbots": await self.cmd_rfbots(update)
            elif cmd == "rage": await self.cmd_rage(update, args)
            elif cmd == "eco": await self.cmd_eco(update, args)
            elif cmd == "legion": await safe_reply(update, LEGION_EVOLUTION_MSG)

            elif cmd in ("sp1", "sp2", "sp3", "sp4", "sp5", "sp6"):
                await self.cmd_sp(update, args, int(cmd[2:]))

            elif cmd in ("slide1", "slide2", "slide3", "slide4", "slide5"):
                await self.cmd_slide(update, int(cmd[5:]))

            elif cmd == "poll":
                await self.cmd_poll(update, txt)

            elif cmd == "multitarget":
                await self.cmd_multitarget(update, args)
            elif cmd == "targetlist":
                await self.cmd_targetlist(update)
            elif cmd == "cleartargets":
                await self.cmd_cleartargets(update)

            elif cmd in ("ssp", "stopsp"):
                state.sp_running[cid] = False
                t = state.sp_tasks.get(cid)
                if t and not t.done(): t.cancel()
                state.sp_tasks.pop(cid, None)
                state.sp_slot.pop(cid, None)
                await safe_reply(update, self.box("SP", "Stopped.", "🛑"))
            elif cmd in ("sslide", "stopslide"):
                state.slide_running[cid] = False
                state.slide_targets.pop(cid, None)
                await safe_reply(update, self.box("SLIDE", "Stopped.", "🛑"))
            elif cmd in ("spoll", "stoppoll"):
                state.poll_running[cid] = False
                t = state.poll_tasks.get(cid)
                if t and not t.done(): t.cancel()
                state.poll_tasks.pop(cid, None)
                await safe_reply(update, self.box("POLL", "Stopped.", "🛑"))
            elif cmd in ("smt", "stopmt", "stopmultitarget"):
                state.multitarget_active[cid] = False
                await safe_reply(update, self.box("MULTITARGET", "Stopped.", "🛑"))

            elif cmd == "dsp":
                await self.set_delay(update, "sp", args, *SP_DELAY_RANGE)
            elif cmd == "dslide":
                await self.set_delay(update, "slide", args, *SLIDE_DELAY_RANGE)
            elif cmd == "dpoll":
                await self.set_delay(update, "poll", args, *POLL_DELAY_RANGE)
            elif cmd == "dmt":
                await self.set_delay(update, "multitarget", args, *MULTITARGET_DELAY_RANGE)

            elif cmd in ("nc", "nct", "ncs", "ncp", "nctime", "ncmoon", "ncclock",
                         "nckeng", "ncheart", "ncgawd", "ncgod", "ncx", "ncloop"):
                await self.cmd_nc(update, args, cmd)
            elif cmd == "ncy": await self.cmd_ncy(update, args)
            elif cmd == "ncxy": await self.cmd_ncxy(update, args)
            elif cmd == "ncyx": await self.cmd_ncyx(update, args)
            elif cmd == "ncz": await self.cmd_ncz(update, args)
            elif cmd == "ncwxs": await self.cmd_ncwxs(update, args)
            elif cmd == "ncemo": await self.cmd_ncemo(update, args)
            elif cmd == "ncq": await self.cmd_ncq(update, args)
            elif cmd == "whonc": await self.cmd_whonc(update, args)

            elif cmd in ("snc", "stopnc"):
                NCWorkers.stop_all(cid)
                await safe_reply(update, self.box("ALL NC", "Stopped.", "🛑"))
            elif cmd == "sgod":
                state.set_active(cid, "ncgod", False)
                await safe_reply(update, self.box("NCGOD", "Stopped.", "🛑"))
            elif cmd == "sncx":
                state.set_active(cid, "ncx", False)
                await safe_reply(update, self.box("NCX", "Stopped.", "🛑"))
            elif cmd == "sncloop":
                state.set_active(cid, "ncloop", False)
                await safe_reply(update, self.box("NCLOOP", "Stopped.", "🛑"))
            elif cmd == "sncy":
                state.ncy_active[cid] = False
                await safe_reply(update, self.box("NCY", "Stopped.", "🛑"))
            elif cmd == "sncxy":
                state.ncxy_active[cid] = False
                await safe_reply(update, self.box("NCXY", "Stopped.", "🛑"))
            elif cmd == "sncyx":
                state.ncyx_active[cid] = False
                await safe_reply(update, self.box("NCYX", "Stopped.", "🛑"))
            elif cmd == "sncz":
                state.ncz_active[cid] = False
                await safe_reply(update, self.box("NCZ", "Stopped.", "🛑"))
            elif cmd == "sncwxs":
                state.ncwxs_active[cid] = False
                await safe_reply(update, self.box("NCWXS", "Stopped.", "🛑"))
            elif cmd == "sncemo":
                state.ncemo_active[cid] = False
                await safe_reply(update, self.box("NCEMO", "Stopped.", "🛑"))
            elif cmd == "sncq":
                state.ncq_active[cid] = False
                await safe_reply(update, self.box("NCQ", "Stopped.", "🛑"))
            elif cmd == "snckeng":
                state.nckeng_active[cid] = False
                await safe_reply(update, self.box("NCKENG", "Stopped.", "🛑"))
            elif cmd == "sncgawd":
                state.ncgawd_active[cid] = False
                await safe_reply(update, self.box("NCGAWD", "Stopped.", "🛑"))
            elif cmd == "swhonc":
                state.whonc_active[cid] = False
                await safe_reply(update, self.box("WHONC", "Stopped.", "🛑"))

            elif cmd in ("Dnc", "Lnc", "Knc", "Anc", "Enc", "Gnc", "Znc", "Cnc", "Mnc"):
                await self.cmd_nc_emoji(update, args, cmd)

            elif cmd in ("ddnc", "dlnc", "dknc", "danc", "denc", "dgnc", "dznc", "dcnc", "dmnc"):
                mode_map = {"ddnc": "Dnc", "dlnc": "Lnc", "dknc": "Knc",
                            "danc": "Anc", "denc": "Enc", "dgnc": "Gnc",
                            "dznc": "Znc", "dcnc": "Cnc", "dmnc": "Mnc"}
                await self.set_nc_emoji_delay(update, mode_map[cmd], args)

            elif cmd == "delaync": await self.set_delay(update, "nc", args, *NC_DELAY_RANGE)
            elif cmd == "delaynct": await self.set_delay(update, "nct", args, *NCT_DELAY_RANGE)
            elif cmd == "delayncs": await self.set_delay(update, "ncs", args, *NCS_DELAY_RANGE)
            elif cmd == "dncp": await self.set_delay(update, "ncp", args, *NCP_DELAY_RANGE)
            elif cmd == "dngod": await self.set_delay(update, "ncgod", args, *NCGOD_DELAY_RANGE)
            elif cmd == "dncx": await self.set_delay(update, "ncx", args, *NCX_DELAY_RANGE)
            elif cmd == "dncloop": await self.set_delay(update, "ncloop", args, *NCLOOP_DELAY_RANGE)
            elif cmd == "dwnc": await self.set_delay(update, "whonc", args, *WHONC_DELAY_RANGE)
            elif cmd == "dnctime": await self.set_delay(update, "nctime", args, *NCTIME_DELAY_RANGE)
            elif cmd == "dncmoon": await self.set_delay(update, "ncmoon", args, *NCMOON_DELAY_RANGE)
            elif cmd == "dncclock": await self.set_delay(update, "ncclock", args, *NCCLOCK_DELAY_RANGE)
            elif cmd == "dnckeng": await self.set_delay(update, "nckeng", args, *NCKENG_DELAY_RANGE)
            elif cmd == "dncheart": await self.set_delay(update, "ncheart", args, *NCHEART_DELAY_RANGE)
            elif cmd == "dncgawd": await self.set_delay(update, "ncgawd", args, *NCGAWD_DELAY_RANGE)
            elif cmd == "dncy": await self.set_delay(update, "ncy", args, *NCY_DELAY_RANGE)
            elif cmd == "dncxy": await self.set_delay(update, "ncxy", args, *NCXY_DELAY_RANGE)
            elif cmd == "dncyx": await self.set_delay(update, "ncyx", args, *NCYX_DELAY_RANGE)
            elif cmd == "dncz": await self.set_delay(update, "ncz", args, *NCZ_DELAY_RANGE)
            elif cmd == "dncwxs": await self.set_delay(update, "ncwxs", args, *NCWXS_DELAY_RANGE)
            elif cmd == "dncemo": await self.set_delay(update, "ncemo", args, *NCEMO_DELAY_RANGE)
            elif cmd == "dncq": await self.set_delay(update, "ncq", args, *NCQ_DELAY_RANGE)

            elif cmd == "xspam": await self.cmd_xspam(update, args)
            elif cmd == "sxspam":
                state.xspam_active[cid] = False
                await safe_reply(update, self.box("XSPAM", "Stopped.", "🛑"))
            elif cmd == "dxspam": await self.set_delay(update, "xspam", args, *XSPAM_DELAY_RANGE)

            elif cmd == "kengspam": await self.cmd_kengspam(update, args)
            elif cmd in ("skspam", "stopkengspam"):
                state.kengspam_active[cid] = False
                await safe_reply(update, self.box("KENGSPAM", "Stopped.", "🛑"))
            elif cmd == "kdelay": await self.set_delay(update, "kengspam", args, *KENGSPAM_DELAY_RANGE)

            elif cmd == "autopinspam": await self.cmd_autopinspam(update, args)
            elif cmd in ("saps", "stopautopinspam"):
                state.autopinspam_active[cid] = False
                await safe_reply(update, self.box("AUTOPIN", "Stopped.", "🛑"))
            elif cmd == "apdelay": await self.set_delay(update, "autopinspam", args, *AUTOPINSPAM_DELAY_RANGE)

            elif cmd == "x": await self.cmd_xraid(update)
            elif cmd == "sx":
                state.x_raid_active[cid] = False
                state.x_raid_targets.pop(cid, None)
                await safe_reply(update, self.box("X RAID", "Stopped.", "🛑"))
            elif cmd == "dx": await self.set_delay(update, "x", args, *X_DELAY_RANGE)

            elif cmd == "sxr": await self.cmd_sxr(update)
            elif cmd == "ssx":
                state.sx_active[cid] = False
                state.sx_targets.pop(cid, None)
                await safe_reply(update, self.box("SX", "Stopped.", "🛑"))
            elif cmd == "dsx": await self.set_delay(update, "sx", args, *SX_DELAY_RANGE)

            elif cmd == "s1": await self.cmd_s1(update, args)
            elif cmd == "sss1":
                state.s1_active[cid] = False
                await safe_reply(update, self.box("S1", "Stopped.", "🛑"))
            elif cmd == "ds1": await self.set_delay(update, "s1", args, 0.001, 1.0)
            elif cmd == "s2": await self.cmd_s2(update, args)
            elif cmd == "sss2":
                state.s2_active[cid] = False
                await safe_reply(update, self.box("S2", "Stopped.", "🛑"))
            elif cmd == "ds2": await self.set_delay(update, "s2", args, 0.001, 1.0)
            elif cmd == "s3": await self.cmd_s3(update, args)
            elif cmd == "sss3":
                state.s3_active[cid] = False
                await safe_reply(update, self.box("S3", "Stopped.", "🛑"))
            elif cmd == "ds3": await self.set_delay(update, "s3", args, 0.001, 1.0)

            elif cmd == "xs": await self.cmd_xs(update, args)
            elif cmd == "sxs":
                state.xs_active[cid] = False
                await safe_reply(update, self.box("XS", "Stopped.", "🛑"))
            elif cmd == "dxs": await self.set_delay(update, "xs", args, *XS_DELAY_RANGE)

            elif cmd == "rr": await self.cmd_rr(update, args)
            elif cmd == "srr":
                state.rr_active[cid] = False
                state.rr_targets.pop(cid, None)
                state.rr_user_text.pop(cid, None)
                await safe_reply(update, self.box("RR", "Stopped.", "🛑"))
            elif cmd == "drr": await self.set_delay(update, "rr", args, *RR_DELAY_RANGE)

            elif cmd in ("sl", "slaughter"): await self.cmd_slaughter(update)
            elif cmd in ("ssl", "stopslaughter"):
                state.slaughter_active[cid] = False
                await safe_reply(update, self.box("SLAUGHTER", "Stopped.", "🛑"))
            elif cmd == "ds": await self.set_delay(update, "slaughter", args, *SL_DELAY_RANGE)

            elif cmd in ("ts", "targetslide"): await self.cmd_ts(update)
            elif cmd in ("sts", "stopts"):
                state.target_slide_active[cid] = False
                await safe_reply(update, self.box("TARGET SLIDE", "Stopped.", "🛑"))
            elif cmd == "dts": await self.set_delay(update, "targetslide", args, *TS_DELAY_RANGE)

            elif cmd in ("sw", "swp"): await self.cmd_swipe(update, args)
            elif cmd in ("ssw", "stopswipe"):
                state.swipe_data.pop(cid, None)
                state.target_users.clear()
                state.spam_users.clear()
                await safe_reply(update, self.box("SWIPE", "Stopped.", "🛑"))
            elif cmd == "dsw": await self.set_delay(update, "swipe", args, *SWIPE_DELAY_RANGE)

            elif cmd in ("autoreact", "ar"):
                e = args[0] if args else "🤣"
                state.auto_react_enabled = True
                state.auto_react_emoji = e
                await safe_reply(update, self.box("AUTOREACT", f"Emoji: {e}", "✅"))
            elif cmd in ("sar", "stopreact"):
                state.auto_react_enabled = False
                await safe_reply(update, self.box("AUTOREACT", "Stopped.", "🛑"))
            elif cmd == "greact":
                e = args[0] if args else "🤣"
                state.global_react = True
                state.global_react_emoji = e
                await safe_reply(update, self.box("GLOBAL REACT", f"Emoji: {e}", "✅"))
            elif cmd == "sgreact":
                state.global_react = False
                await safe_reply(update, self.box("GLOBAL REACT", "Stopped.", "🛑"))
            elif cmd == "creact":
                e = args[0] if args else "🤣"
                state.react_chats[cid] = True
                state.react_emoji[cid] = e
                await safe_reply(update, self.box("CHAT REACT", f"Emoji: {e}", "✅"))
            elif cmd == "screact":
                state.react_chats[cid] = False
                await safe_reply(update, self.box("CHAT REACT", "Stopped.", "🛑"))
            elif cmd == "mar":
                state.mar_active[cid] = True
                await safe_reply(update, self.box("MAR", "Ultra-fast mass react ON", "🎭"))
            elif cmd == "smar":
                state.mar_active[cid] = False
                await safe_reply(update, self.box("MAR", "Stopped.", "🛑"))
            elif cmd == "dmar": await self.set_delay(update, "mar", args, *MAR_DELAY_RANGE)

            elif cmd == "purge":
                state.purge_chats[cid] = True
                await safe_reply(update, self.box("PURGE", "Active.", "🧹"))
            elif cmd == "unpurge":
                state.purge_chats[cid] = False
                await safe_reply(update, self.box("PURGE", "Stopped.", "🛑"))

            elif cmd == "delall":
                state.delall_running[cid] = True
                await safe_reply(update, self.box("DELALL", "Deleting all...", "🗑️"))
                fire_and_forget(self._delall(cid))
            elif cmd == "sdel":
                state.delall_running[cid] = False
                await safe_reply(update, self.box("DELALL", "Stopped.", "🛑"))
            elif cmd == "ddelall": await self.set_delay(update, "delall", args, *DELALL_DELAY_RANGE)

            elif cmd == "savephoto": await self.save_media(update, context, "photo")
            elif cmd in ("stpic", "pic"): await self.start_media(update, "photo")
            elif cmd in ("spic", "stoppic"): await self.stop_media(update, "photo")
            elif cmd == "dp": await self.set_delay(update, "photo", args, *PHOTO_DELAY_RANGE)
            elif cmd == "startphoto": await self.cmd_startphoto(update)
            elif cmd in ("stopgcpfp", "vmd"):
                state.gcpfp_running[cid] = False
                await safe_reply(update, self.box("GC PFP", "Stopped.", "🛑"))
            elif cmd == "gdelay": await self.set_delay(update, "pfp", args, *PFP_DELAY_RANGE)
            elif cmd == "delmsg":
                state.delmsg_running[cid] = True
                fire_and_forget(self._delmsg(cid))
                await safe_reply(update, self.box("DELMSG", "Deleting bot msgs.", "🗑️"))
            elif cmd == "sdelmsg":
                state.delmsg_running[cid] = False
                await safe_reply(update, self.box("DELMSG", "Stopped.", "🛑"))
            elif cmd == "ddelmsg": await self.set_delay(update, "delmsg", args, *DELMSG_DELAY_RANGE)

            elif cmd == "mute": await self.mod_mute(update)
            elif cmd == "unmute": await self.mod_unmute(update)
            elif cmd == "lockgc":
                for b in state.bots:
                    try:
                        await b.set_chat_permissions(cid, permissions=ChatPermissions(can_send_messages=False)); break
                    except Exception: continue
                await safe_reply(update, self.box("GROUP LOCK", "Locked.", "🔒"))
            elif cmd == "unlockgc":
                for b in state.bots:
                    try:
                        await b.set_chat_permissions(cid, permissions=ChatPermissions(
                            can_send_messages=True, can_send_media_messages=True,
                            can_send_other_messages=True, can_add_web_page_previews=True)); break
                    except Exception: continue
                await safe_reply(update, self.box("GROUP UNLOCKED", "Unlocked.", "🔓"))

            elif cmd == "gameover": await self.cmd_gameover(update, args)
            elif cmd == "sgameover":
                state.gameover_running[cid] = False
                await safe_reply(update, self.box("GAMEOVER", "Stopped.", "🛑"))
            elif cmd == "dgameover": await self.set_delay(update, "gameover", args, *GAMEOVER_DELAY_RANGE)

            elif cmd in ("addworthy", "addsudo"): await self.sudo_add(update)
            elif cmd in ("unworthy", "delsudo"): await self.sudo_del(update)
            elif cmd == "nworthy": await self.sudo_list(update, context)

            elif cmd in ("summon", "addall", "add"): await self.cmd_addall(update, context)
            elif cmd in ("upall", "promoteall"): await self.cmd_upall(update)
            elif cmd == "retreat": await self.cmd_retreat(update)

            elif cmd == "song": await self.cmd_song(update, args)
            elif cmd == "tts": await self.cmd_tts(update, args)

            elif cmd == "ggs": await self.cmd_ggs(update)
            elif cmd in ("stopall", "stp", "sstop"):
                state.stop_all(cid)
                await safe_reply(update, self.box("ALL STOPPED", "Stopped.", "🛑"))
        except Exception as e:
            stability_engine.report(e)
            ColorLogger.error(f"dispatch {cmd}: {e}")
                # ═══════════════════════════════════════════════════════════════
    #                    POLL COMMAND
    # ═══════════════════════════════════════════════════════════════

    async def cmd_poll(self, update, raw_text: str):
        cid = update.effective_chat.id
        m = re.match(r"^[!\./\-\?\*\$\#\&_]+poll\s*(.*)$", raw_text, re.IGNORECASE | re.DOTALL)
        body = m.group(1).strip() if m else ""
        if not body:
            question = POLL_QUESTION_TEMPLATE
            opt1 = POLL_OPT1_TEMPLATE
            opt2 = POLL_OPT2_TEMPLATE
        else:
            parts = [p.strip() for p in body.split("|")]
            if len(parts) >= 3:
                question, opt1, opt2 = parts[0], parts[1], parts[2]
            elif len(parts) == 1:
                question = parts[0]; opt1 = POLL_OPT1_TEMPLATE; opt2 = POLL_OPT2_TEMPLATE
            elif len(parts) == 2:
                question = parts[0]; opt1 = parts[1]; opt2 = POLL_OPT2_TEMPLATE
            else:
                question = POLL_QUESTION_TEMPLATE; opt1 = POLL_OPT1_TEMPLATE; opt2 = POLL_OPT2_TEMPLATE
        def apply_test(tpl, user_text):
            if not user_text: return tpl.replace("(test)", "").strip()
            return re.sub(r"\([Tt]est\)", user_text, tpl).strip()
        if "(test)" in opt1: opt1 = apply_test(opt1, question)
        if "(test)" in opt2: opt2 = apply_test(opt2, question)
        old = state.poll_tasks.get(cid)
        if old and not old.done():
            state.poll_running[cid] = False; old.cancel()
        state.poll_running[cid] = True
        task = asyncio.create_task(poll_loop(cid, question, opt1, opt2))
        state.poll_tasks[cid] = task
        d = state.delays.get("poll", 0.005)
        await safe_reply(update, self.box("POLL", f"Started | Delay: {d}s | Stop: spoll", "🗳️"))

    # ═══════════════════════════════════════════════════════════════
    #                    MULTITARGET (mention-based)
    # ═══════════════════════════════════════════════════════════════

    async def cmd_multitarget(self, update, args):
        cid = update.effective_chat.id
        if not args:
            await safe_reply(update, "❌ Usage: multitarget @username1 @username2 ...")
            return
        added = []
        failed = []
        for uname in args:
            if not uname.startswith("@"): uname = "@" + uname
            try:
                ch = await update.get_bot().get_chat(uname)
                tid = ch.id
                state.multitarget_targets.setdefault(cid, set()).add(tid)
                added.append(f"{ch.first_name} ({tid})")
            except Exception:
                failed.append(uname)
        if not state.multitarget_active.get(cid, False) and added:
            state.multitarget_active[cid] = True
            fire_and_forget(multitarget_worker(cid))
        count = len(state.multitarget_targets.get(cid, set()))
        body = f"Added: {len(added)}\nTotal: {count}\nStop: smt"
        if added:
            body += "\n\n" + "\n".join(f"• {n}" for n in added[:10])
        if failed:
            body += "\n\nFailed:\n" + "\n".join(f"• {u}" for u in failed[:10])
        await safe_reply(update, self.box("MULTITARGET", body, "⚡"))

    async def cmd_targetlist(self, update):
        cid = update.effective_chat.id
        targets = state.multitarget_targets.get(cid, set())
        if not targets:
            await safe_reply(update, self.box("TARGETS", "No active targets.", "📋")); return
        lines = [f"⚡ Multitarget ({len(targets)}):"]
        for tid in targets:
            nm = f"User{tid}"
            try:
                ch = await update.get_bot().get_chat(tid)
                nm = ch.first_name or nm
                if ch.username: nm += f" @{ch.username}"
            except Exception: pass
            lines.append(f"• {nm} ({tid})")
        await safe_reply(update, "\n".join(lines))

    async def cmd_cleartargets(self, update):
        cid = update.effective_chat.id
        state.multitarget_targets.pop(cid, None)
        state.multitarget_active[cid] = False
        await safe_reply(update, self.box("TARGETS", "All cleared.", "🗑️"))

    # ═══════════════════════════════════════════════════════════════
    #                    SP / SLIDE COMMANDS
    # ═══════════════════════════════════════════════════════════════

    async def cmd_sp(self, update, args, sp_num: int):
        cid = update.effective_chat.id
        extra = " ".join(args) if args else ""
        old = state.sp_tasks.get(cid)
        if old and not old.done():
            state.sp_running[cid] = False; old.cancel()
        state.sp_running[cid] = True
        state.sp_slot[cid] = sp_num
        task = asyncio.create_task(sp_loop(cid, sp_num, extra))
        state.sp_tasks[cid] = task
        await safe_reply(update, self.box(f"SP{sp_num}", f"Started. Stop: ssp", "❤️"))

    async def cmd_slide(self, update, slide_num: int):
        cid = update.effective_chat.id
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user to target them with Slide."); return
        t = update.message.reply_to_message.from_user
        state.slide_targets.setdefault(cid, {})[t.id] = slide_num
        await safe_reply(update, self.box(f"SLIDE{slide_num}", f"Target: {t.first_name}\nReply will trigger slide.", "🩷"))

    # ═══════════════════════════════════════════════════════════════
    #                    NC COMMANDS
    # ═══════════════════════════════════════════════════════════════

    async def cmd_nc(self, update, args, mode):
        if not args: await safe_reply(update, f"❌ {mode} <text>"); return
        base = " ".join(args)
        cid = update.effective_chat.id
        if not state.bots: await safe_reply(update, "❌ No bots!"); return
        state.set_active(cid, mode, True)
        simple = {
            "nc": lambda t: f"{t} {random.choice(NCLOOP_LINES)}",
            "nct": lambda t: f"{random.choice(NC_LOOP_EMOJIS)} {t} {ist_time()}",
            "ncs": lambda t: f"{random.choice(NC_LOOP_EMOJIS)} {t} {random.choice(NCLOOP_LINES)} {random.choice(NC_LOOP_EMOJIS)}",
            "ncp": lambda t: f"{random.choice(NC_LOOP_EMOJIS)} {t} {random.choice(NC_LOOP_EMOJIS)} {random.choice(NCLOOP_LINES)}",
            "nctime": lambda t: f"⏰ {t} {ist_time()}",
            "ncx": lambda t: f"{t} {random.choice(NCX_LINES)}",
            "ncloop": lambda t: f"{t} {random.choice(NCLOOP_LINES)}",
        }
        indexed = {
            "ncmoon": lambda t, i: f"{MOON_EMOJIS[i % 10]} {t} {MOON_EMOJIS[i % 10]}",
            "ncclock": lambda t, i: f"{CLOCK_EMOJIS[i % 12]} {t} {CLOCK_EMOJIS[i % 12]}",
            "nckeng": lambda t, i: f"{KENG_EMOJIS[i % 10]} {t} {KENG_EMOJIS[i % 10]}",
            "ncheart": lambda t, i: f"{HEART_EMOJIS[i % 10]} {t} {HEART_EMOJIS[i % 10]}",
            "ncgawd": lambda t, i: f"{t} {GAWD_EMOJIS[i % 30]}",
        }
        tasks = []
        for b in state.bots:
            if mode == "ncgod":
                tasks.append(asyncio.create_task(NCWorkers._ncgod(b, cid, base)))
            elif mode in simple:
                tasks.append(asyncio.create_task(NCWorkers._basic(b, cid, base, mode, simple[mode])))
            elif mode in indexed:
                tasks.append(asyncio.create_task(NCWorkers._indexed(b, cid, base, mode, indexed[mode])))
        gather_bg(*tasks)
        stop = {"ncgod": "sgod", "ncx": "sncx", "ncloop": "sncloop"}.get(mode, "snc")
        extra = f"\n⚡ 5x parallel per bot → {len(state.bots)*5} NC/sec" if mode == "ncgod" else ""
        await safe_reply(update, self.box(
            mode.upper(),
            f"Delay: {state.delays.get(mode, 0.001)}s | Bots: {len(state.bots)}{extra}\nStop: {stop}",
            "✅"))

    async def cmd_ncy(self, update, args):
        if not args: await safe_reply(update, "❌ ncy <text>"); return
        cid = update.effective_chat.id
        base = " ".join(args)
        state.ncy_active[cid] = True; state.ncy_text[cid] = base
        await safe_reply(update, self.box("NCY", f"Delay: {state.delays['ncy']}s\nStop: sncy", "🌀"))
        async def w(bot):
            while state.ncy_active.get(cid, False):
                try:
                    e = random.choice(NC_LOOP_EMOJIS)
                    await set_title_dual(bot, cid, f"{base} {e}")
                    await asyncio.sleep(state.eff_delay("ncy", state.delays.get("ncy", 0.01)))
                except asyncio.CancelledError: return
                except RetryAfter as ex: await asyncio.sleep(min(getattr(ex, "retry_after", 1) + 0.3, 5))
                except BadRequest as ex:
                    if "not enough rights" in str(ex).lower(): return
                    await asyncio.sleep(0)
                except Exception: await asyncio.sleep(0)
        gather_bg(*[asyncio.create_task(w(b)) for b in state.bots])

    async def cmd_ncxy(self, update, args):
        if not args: await safe_reply(update, "❌ ncxy <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncxy_active[cid] = True; state.ncxy_text[cid] = base
        await safe_reply(update, self.box("NCXY", f"Delay: {state.delays['ncxy']}s\nStop: snc / sncxy", "🌀"))
        gather_bg(*[asyncio.create_task(NCWorkers._ncxy(b, cid, base)) for b in state.bots])

    async def cmd_ncyx(self, update, args):
        if not args: await safe_reply(update, "❌ ncyx <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncyx_active[cid] = True; state.ncyx_text[cid] = base
        await safe_reply(update, self.box("NCYX", f"Pentagon (5x/bot)\nDelay: {state.delays['ncyx']}s\nStop: snc / sncyx", "🔺"))
        fire_and_forget(NCWorkers._ncyx(cid, base))

    async def cmd_ncz(self, update, args):
        if not args: await safe_reply(update, "❌ ncz <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncz_active[cid] = True; state.ncz_text[cid] = base
        await safe_reply(update, self.box("NCZ", f"Opponent detect\nDelay: {state.delays['ncz']}s\nStop: snc / sncz", "🎯"))
        fire_and_forget(NCWorkers._ncz(cid, base))

    async def cmd_ncwxs(self, update, args):
        if not args: await safe_reply(update, "❌ ncwxs <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncwxs_active[cid] = True; state.ncwxs_text[cid] = base
        await safe_reply(update, self.box("NCWXS", f"Delay: {state.delays['ncwxs']}s\nStop: snc / sncwxs", "🌀"))
        gather_bg(*[asyncio.create_task(NCWorkers._ncwxs(b, cid, base)) for b in state.bots])

    async def cmd_ncemo(self, update, args):
        if not args: await safe_reply(update, "❌ ncemo <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncemo_active[cid] = True; state.ncemo_text[cid] = base
        await safe_reply(update, self.box("NCEMO", f"Delay: {state.delays['ncemo']}s\nStop: snc / sncemo", "😀"))
        gather_bg(*[asyncio.create_task(NCWorkers._ncemo(b, cid, base)) for b in state.bots])

    async def cmd_ncq(self, update, args):
        if not args: await safe_reply(update, "❌ ncq <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.ncq_active[cid] = True; state.ncq_text[cid] = base
        await safe_reply(update, self.box("NCQ", f"Parallel+Penta\nDelay: {state.delays['ncq']}s\nStop: snc / sncq", "💠"))
        fire_and_forget(NCWorkers._ncq(cid, base))

    async def cmd_whonc(self, update, args):
        if not args: await safe_reply(update, "❌ whonc <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        state.whonc_active[cid] = True; state.whonc_text[cid] = base
        await safe_reply(update, self.box("WHONC", f"Delay: {state.delays['whonc']}s\nStop: swhonc / snc\nTexts: 17 slots", "🫧"))
        fire_and_forget(whonc_worker(cid, base))

    async def cmd_nc_emoji(self, update, args, mode):
        if not args: await safe_reply(update, f"❌ {mode} <text>"); return
        cid = update.effective_chat.id; base = " ".join(args)
        mk = f"nc{mode.lower()}"; state.set_active(cid, mk, True)
        async def w(bot):
            while state.is_active(cid, mk):
                try:
                    e = random.choice(NC_EMOJI_MODES.get(mode, ["🌀"]))
                    await set_title_dual(bot, cid, f"{e} {base} {e}")
                    d = state.nc_emoji_delays.get(mode, 0.1)
                    await asyncio.sleep(state.eff_delay(mk, d))
                except asyncio.CancelledError: return
                except RetryAfter: await asyncio.sleep(0)
                except BadRequest as e:
                    if "not enough rights" in str(e).lower(): return
                    await asyncio.sleep(0)
                except Exception: await asyncio.sleep(0)
        gather_bg(*[asyncio.create_task(w(b)) for b in state.bots])
        await safe_reply(update, self.box(mode.upper(), f"Delay: {state.nc_emoji_delays.get(mode, 0.1)}s\nStop: snc", "✅"))

    async def set_delay(self, update, mode, args, min_v=0.0001, max_v=5.0):
        if not args:
            await safe_reply(update, f"❌ <delay>\nCur: {state.delays.get(mode, 'N/A')}s\nRange: {min_v}–{max_v}"); return
        try: v = float(args[0])
        except ValueError: await safe_reply(update, "❌ Invalid!"); return
        if v < min_v or v > max_v:
            await safe_reply(update, f"❌ Must be {min_v}–{max_v}"); return
        old = state.delays.get(mode); state.delays[mode] = v
        await safe_reply(update, self.box(f"{mode.upper()} DELAY", f"{old}s → {v}s", "⏱️"))

    async def set_nc_emoji_delay(self, update, mode, args):
        if not args: await safe_reply(update, f"❌ d{mode.lower()} <delay>\nRange: 0.0005–0.1"); return
        try: v = float(args[0])
        except ValueError: await safe_reply(update, "❌ Invalid!"); return
        if v < 0.0005 or v > 0.1: await safe_reply(update, "❌ Must be 0.0005–0.1"); return
        old = state.nc_emoji_delays.get(mode); state.nc_emoji_delays[mode] = v
        await safe_reply(update, self.box(f"{mode} DELAY", f"{old}s → {v}s", "⏱️"))

    # ═══════════════════════════════════════════════════════════════
    #                    SPAM COMMANDS
    # ═══════════════════════════════════════════════════════════════

    async def cmd_xspam(self, update, args):
        if not args: await safe_reply(update, "❌ xspam <text>"); return
        cid = update.effective_chat.id
        state.xspam_active[cid] = True
        state.xspam_text[cid] = " ".join(args)
        await safe_reply(update, self.box("XSPAM", f"Delay: {state.delays['xspam']}s\nStop: sxspam", "📢"))
        fire_and_forget(self._xspam_worker(cid))

    async def _xspam_worker(self, cid):
        while state.xspam_active.get(cid, False):
            try:
                user_text = state.xspam_text.get(cid, "")
                if not user_text: break
                tpl = random.choice(XTEXT); repeat = 70
                m = re.search(r"\*(\d+)\s*$", tpl)
                if m:
                    try: repeat = int(m.group(1))
                    except Exception: repeat = 70
                    tpl = tpl[:m.start()]
                body = re.sub(r"\([Tt]est\)", user_text, tpl).replace("<semoji>", _random_smoji())
                big = body * repeat
                chunks = safe_chunk_text(big, 4000)
                async def one(bot, chunks=chunks):
                    for ch in chunks[:3]:
                        try: await bot.send_message(cid, ch)
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                await asyncio.sleep(state.eff_delay("xspam", state.delays.get("xspam", 0.01)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.05)

    async def cmd_kengspam(self, update, args):
        if not args: await safe_reply(update, "❌ kengspam <text>"); return
        cid = update.effective_chat.id
        state.kengspam_active[cid] = True
        state.kengspam_text[cid] = " ".join(args)
        await safe_reply(update, self.box("KENGSPAM", f"Delay: {state.delays['kengspam']}s\nStop: skspam", "💥"))
        fire_and_forget(self._kengspam_worker(cid))

    async def _kengspam_worker(self, cid):
        while state.kengspam_active.get(cid, False):
            try:
                user_text = state.kengspam_text.get(cid, "")
                if not user_text: break
                tpl = random.choice(KENGSPAM_TEXTS); repeat = 50
                m = re.search(r"\*(\d+)\s*$", tpl)
                if m:
                    try: repeat = int(m.group(1))
                    except Exception: repeat = 50
                    tpl = tpl[:m.start()]
                body = re.sub(r"\([Tt]est\)", user_text, tpl)
                for ph in ("(smoji)", "(semojj)", "(semoji)", "(emoji)"):
                    body = body.replace(ph, _random_smoji())
                big = body * repeat
                chunks = safe_chunk_text(big, 4000)
                async def one(bot, chunks=chunks):
                    for ch in chunks[:3]:
                        try: await bot.send_message(cid, ch)
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                await asyncio.sleep(state.eff_delay("kengspam", state.delays.get("kengspam", 0.5)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.05)

    async def cmd_autopinspam(self, update, args):
        if not args: await safe_reply(update, "❌ autopinspam <text>"); return
        cid = update.effective_chat.id
        state.autopinspam_active[cid] = True
        state.autopinspam_text[cid] = " ".join(args)
        await safe_reply(update, self.box("AUTOPIN", f"Delay: {state.delays['autopinspam']}s\nStop: saps", "📌"))
        fire_and_forget(self._autopinspam_worker(cid))

    async def _autopinspam_worker(self, cid):
        while state.autopinspam_active.get(cid, False):
            try:
                user_text = state.autopinspam_text.get(cid, "")
                if not user_text: break
                body = AUTOPINSPAM_TEXT.replace("{text}", user_text).replace("(test)", user_text)
                big = body * 100
                chunks = safe_chunk_text(big, 4000)
                async def one(bot, chunks=chunks):
                    first = None
                    for ch in chunks[:2]:
                        try:
                            m2 = await bot.send_message(cid, ch)
                            if first is None: first = m2
                        except Exception: pass
                    if first:
                        try: await bot.pin_chat_message(cid, first.message_id, disable_notification=False)
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                await asyncio.sleep(state.eff_delay("autopinspam", state.delays.get("autopinspam", 0.1)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.05)

    async def cmd_s1(self, update, args):
        if not args: await safe_reply(update, "❌ s1 <text>"); return
        cid = update.effective_chat.id
        state.s1_active[cid] = True; state.s1_text[cid] = " ".join(args)
        await safe_reply(update, self.box("S1", f"Delay: {state.delays['s1']}s\nStop: sss1", "📝"))
        fire_and_forget(self._s_worker(cid, "s1"))

    async def _s_worker(self, cid, mode):
        while getattr(state, f"{mode}_active").get(cid, False):
            try:
                ut = getattr(state, f"{mode}_text").get(cid, "")
                if not ut: break
                body = re.sub(r"\([Tt]est\)", ut, f"(test) {ut}").replace("<semoji>", _random_smoji())
                big = body * 50
                chunks = safe_chunk_text(big, 4000)
                async def one(bot, chunks=chunks):
                    for ch in chunks[:3]:
                        try: await bot.send_message(cid, ch)
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                await asyncio.sleep(state.eff_delay(mode, state.delays.get(mode, 0.01)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.05)

    async def cmd_s2(self, update, args):
        if not args: await safe_reply(update, "❌ s2 <text>"); return
        cid = update.effective_chat.id
        state.s2_active[cid] = True; state.s2_text[cid] = " ".join(args)
        await safe_reply(update, self.box("S2", f"Delay: {state.delays['s2']}s\nStop: sss2", "📝"))
        fire_and_forget(self._s_worker(cid, "s2"))

    async def cmd_s3(self, update, args):
        if not args: await safe_reply(update, "❌ s3 <text>"); return
        cid = update.effective_chat.id
        state.s3_active[cid] = True; state.s3_text[cid] = " ".join(args)
        await safe_reply(update, self.box("S3", f"Delay: {state.delays['s3']}s\nStop: sss3", "📝"))
        fire_and_forget(self._s_worker(cid, "s3"))

    async def cmd_xs(self, update, args):
        if not args: await safe_reply(update, "❌ xs <text>"); return
        cid = update.effective_chat.id
        state.xs_active[cid] = True; state.xs_text[cid] = " ".join(args); state.xs_counter[cid] = 0
        await safe_reply(update, self.box("XS", f"Delay: {state.delays['xs']}s\n5s pause after 100 msg\nStop: sxs", "🌀"))
        fire_and_forget(self._xs_worker(cid))

    async def _xs_worker(self, cid):
        while state.xs_active.get(cid, False):
            try:
                user_text = state.xs_text.get(cid, "")
                if not user_text: break
                tpl = random.choice(XS_TEXTS); repeat = 35
                m = re.search(r"\*(\d+)\s*$", tpl)
                if m:
                    try: repeat = int(m.group(1))
                    except Exception: repeat = 35
                    tpl = tpl[:m.start()]
                body = re.sub(r"\([Tt]est\)", user_text, tpl).replace("<semoji>", _random_smoji())
                big = body * repeat
                chunks = safe_chunk_text(big, 4000)
                async def one(bot, chunks=chunks):
                    for ch in chunks[:2]:
                        try: await bot.send_message(cid, ch)
                        except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                state.xs_counter[cid] = state.xs_counter.get(cid, 0) + 1
                if state.xs_counter[cid] >= 100:
                    state.xs_counter[cid] = 0
                    await asyncio.sleep(5)
                else:
                    await asyncio.sleep(state.eff_delay("xs", state.delays.get("xs", 0.05)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.05)

    # ═══════════════════════════════════════════════════════════════
    #                    RAID COMMANDS
    # ═══════════════════════════════════════════════════════════════

    async def cmd_rr(self, update, args):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        text = " ".join(args) if args else ""
        state.rr_active[cid] = True; state.rr_targets[cid] = t.id; state.rr_user_text[cid] = text
        await safe_reply(update, self.box("RR", f"Target: {t.first_name}\nStop: srr", "🎯"))

    async def cmd_slaughter(self, update):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        state.slaughter_active[cid] = True; state.slaughter_targets[cid] = t.id
        await safe_reply(update, self.box("SLAUGHTER", f"Target: {t.first_name}\nStop: ssl", "🔪"))

    async def cmd_ts(self, update):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        state.target_slide_active[cid] = True; state.target_slide_targets[cid] = t.id
        await safe_reply(update, self.box("TARGET SLIDE", f"Target: {t.first_name}\nStop: sts", "🎯"))

    async def cmd_swipe(self, update, args):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        text = " ".join(args) if args else ""
        state.swipe_data[cid] = text if text else "ONLY_RAID_TEXT"
        state.target_users.add(t.id)
        await safe_reply(update, self.box("SWIPE", f"Target: {t.first_name}\nStop: ssw", "⚡"))

    async def cmd_xraid(self, update):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        state.x_raid_active[cid] = True; state.x_raid_targets[cid] = t.id
        await safe_reply(update, self.box("X RAID", f"Target: {t.first_name}\nStop: sx", "🔥"))

    async def cmd_sxr(self, update):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a user!"); return
        cid = update.effective_chat.id
        t = update.message.reply_to_message.from_user
        state.sx_active[cid] = True; state.sx_targets[cid] = t.id
        await safe_reply(update, self.box("SX", f"Target: {t.first_name}\nStop: ssx", "⚔️"))

    # ═══════════════════════════════════════════════════════════════
    #                    GAMEOVER / DELALL / DELMSG
    # ═══════════════════════════════════════════════════════════════

    async def cmd_gameover(self, update, args):
        if not update.message.reply_to_message:
            await safe_reply(update, "❌ Reply to a target user!"); return
        if not args: await safe_reply(update, "❌ gameover <text>"); return
        if not self.leader_bot: await safe_reply(update, "❌ No leader bot."); return
        cid = update.effective_chat.id
        if state.gameover_running.get(cid):
            await safe_reply(update, "⏳ Already running."); return
        state.gameover_running[cid] = True
        target = update.message.reply_to_message.from_user
        user_text = " ".join(args)
        final_text = GAMEOVER_TEXT.format(ist=ist_time(), date=ist_date())
        final_text = re.sub(r"\([Tt]est\)", user_text, final_text)
        await safe_reply(update, self.box("GAMEOVER", f"Target: {target.first_name}\nLeader sends ONCE.", "🎮"))
        try:
            if os.path.exists(GAMEOVER_PHOTO_PATH):
                try:
                    with open(GAMEOVER_PHOTO_PATH, "rb") as f:
                        await self.leader_bot.send_photo(cid, photo=f, caption=final_text[:1024])
                    return
                except Exception: pass
            for ch in safe_chunk_text(final_text, 4000)[:1]:
                await self.leader_bot.send_message(cid, ch)
        finally:
            state.gameover_running[cid] = False

    async def _delall(self, cid):
        try:
            first_bot = state.bots[0] if state.bots else None
            if not first_bot: return
            while state.delall_running.get(cid, False):
                try:
                    messages = []
                    async for msg in first_bot.get_chat_history(cid, limit=100):
                        messages.append(msg.message_id)
                    if not messages:
                        await asyncio.sleep(1); continue
                    async def delete_one(mid):
                        for b in state.bots:
                            try:
                                await b.delete_message(cid, mid); break
                            except Exception: continue
                        await asyncio.sleep(state.eff_delay("delall", state.delays.get("delall", 0.001)))
                    await _gather_ignore(*[asyncio.create_task(delete_one(mid)) for mid in messages])
                except asyncio.CancelledError: return
                except Exception: await asyncio.sleep(0.1)
        except asyncio.CancelledError: return
        finally: state.delall_running[cid] = False

    async def _delmsg(self, cid):
        while state.delmsg_running.get(cid, False):
            try:
                for b in state.bots:
                    try:
                        async for m in b.get_chat_history(cid, limit=10):
                            if m.from_user and m.from_user.id == b.id:
                                await m.delete()
                    except Exception: pass
                await asyncio.sleep(state.eff_delay("delmsg", state.delays.get("delmsg", 0.001)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.1)

    # ═══════════════════════════════════════════════════════════════
    #                    MEDIA
    # ═══════════════════════════════════════════════════════════════

    async def save_media(self, update, context, kind):
        try:
            r = update.message.reply_to_message
            if not r or not r.photo: await safe_reply(update, "❌ Reply to a photo!"); return
            f = await context.bot.get_file(r.photo[-1].file_id)
            path = f"{MEDIA_DIR}/photo_{len(state.saved_photos)}.jpg"
            await f.download_to_drive(path)
            state.saved_photos.append(path)
            await safe_reply(update, f"✅ Saved ({len(state.saved_photos)})")
        except Exception as e:
            await safe_reply(update, f"❌ {e}")

    async def start_media(self, update, kind):
        cid = update.effective_chat.id
        if not state.saved_photos: await safe_reply(update, "❌ No photos"); return
        state.set_active(cid, kind, True)
        await safe_reply(update, self.box(f"{kind.upper()} SPAM", f"Delay: {state.delays[kind]}s", "✅"))
        fire_and_forget(self._media_worker(cid, kind))

    async def _media_worker(self, cid, kind):
        i = 0
        while state.is_active(cid, kind):
            try:
                path = state.saved_photos[i % len(state.saved_photos)]
                async def one(bot):
                    try:
                        with open(path, "rb") as f: await bot.send_photo(cid, photo=f)
                    except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                i += 1
                await asyncio.sleep(state.eff_delay(kind, state.delays.get(kind, 0.5)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.5)

    async def stop_media(self, update, kind):
        state.set_active(update.effective_chat.id, kind, False)
        await safe_reply(update, self.box(f"{kind.upper()}", "Stopped.", "🛑"))

    async def cmd_startphoto(self, update):
        cid = update.effective_chat.id
        if not state.saved_photos: await safe_reply(update, "❌ No photos"); return
        state.gcpfp_running[cid] = True
        await safe_reply(update, self.box("GC PFP", "Changing group photo", "🖼️"))
        fire_and_forget(self._pfp(cid))

    async def _pfp(self, cid):
        i = 0
        while state.gcpfp_running.get(cid, False):
            try:
                path = state.saved_photos[i % len(state.saved_photos)]
                async def one(b):
                    try:
                        with open(path, "rb") as f: await b.set_chat_photo(cid, photo=f)
                    except Exception: pass
                await _gather_ignore(*[asyncio.create_task(one(b)) for b in state.bots])
                i += 1
                await asyncio.sleep(state.eff_delay("pfp", state.delays.get("pfp", 0.5)))
            except asyncio.CancelledError: return
            except Exception: await asyncio.sleep(0.5)

    # ═══════════════════════════════════════════════════════════════
    #                    MODS
    # ═══════════════════════════════════════════════════════════════

    async def mod_mute(self, update):
        if not update.message.reply_to_message: await safe_reply(update, "❌ Reply"); return
        cid = update.effective_chat.id; t = update.message.reply_to_message.from_user
        for b in state.bots:
            try:
                await b.restrict_chat_member(cid, t.id, permissions=ChatPermissions(can_send_messages=False)); break
            except Exception: continue
        await safe_reply(update, self.box("MUTE", f"{t.first_name} muted.", "🔇"))

    async def mod_unmute(self, update):
        if not update.message.reply_to_message: await safe_reply(update, "❌ Reply"); return
        cid = update.effective_chat.id; t = update.message.reply_to_message.from_user
        for b in state.bots:
            try:
                await b.restrict_chat_member(cid, t.id, permissions=ChatPermissions(
                    can_send_messages=True, can_send_media_messages=True,
                    can_send_other_messages=True, can_add_web_page_previews=True)); break
            except Exception: continue
        await safe_reply(update, self.box("UNMUTE", f"{t.first_name} unmuted.", "🔊"))

    async def sudo_add(self, update):
        if not is_owner(update.effective_user.id):
            await safe_reply(update, "❌ Not worthy"); return
        if not update.message.reply_to_message: await safe_reply(update, "❌ Reply"); return
        t = update.message.reply_to_message.from_user
        state.sudo_users.add(t.id); state.save_sudo()
        await safe_reply(update, f"✅ {t.first_name} added")

    async def sudo_del(self, update):
        if not is_owner(update.effective_user.id):
            await safe_reply(update, "❌ Not worthy"); return
        if not update.message.reply_to_message: await safe_reply(update, "❌ Reply"); return
        t = update.message.reply_to_message.from_user
        if t.id in state.sudo_users and t.id != OWNER_ID:
            state.sudo_users.discard(t.id); state.save_sudo()
            await safe_reply(update, f"✅ {t.first_name} removed")

    async def sudo_list(self, update, context):
        lines = [f"🛡️ Worthy ({len(state.sudo_users)})"]
        for u in state.sudo_users:
            try:
                c = await context.bot.get_chat(u); lines.append(f"• {c.first_name} ({u})")
            except Exception: lines.append(f"• {u}")
        await safe_reply(update, "\n".join(lines))

    async def cmd_addall(self, update, context):
        cid = update.effective_chat.id
        leader = self.leader_bot or state.bots[0]
        is_admin = False
        try:
            me = await leader.get_chat_member(cid, leader.id)
            if me.status in ("administrator", "creator"):
                is_admin = True
        except Exception:
            pass
        if not is_admin:
            await safe_reply(update,
                "⚠️ **Leader bot is NOT admin!**\n\n"
                "Please promote the leader bot with **Add Users** right, "
                "then run `addall` again.")
            return
        await safe_reply(update, SUMMONING_RITUAL_MSG.format(count=len(state.bots)))
        try:
            await addall_via_invite(update, context, leader)
        except Exception as e:
            await safe_reply(update, f"❌ {e}")

    async def cmd_upall(self, update):
        cid = update.effective_chat.id; n = 0
        for b in state.bots:
            try:
                await update.get_bot().promote_chat_member(
                    cid, b.id, can_manage_chat=True, can_delete_messages=True,
                    can_manage_video_chats=True, can_restrict_members=True,
                    can_promote_members=True, can_change_info=True,
                    can_invite_users=True, can_pin_messages=True); n += 1
            except Exception: pass
        await safe_reply(update, f"✅ {n} promoted")

    async def cmd_retreat(self, update):
        cid = update.effective_chat.id; n = 0
        for b in state.bots:
            try: await update.get_bot().ban_chat_member(cid, b.id); n += 1
            except Exception: pass
        await safe_reply(update, RETREAT_ORDER_MSG)

    async def cmd_song(self, update, args):
        if not args: await safe_reply(update, "❌ song <name>"); return
        await safe_reply(update, "🎵 Song download coming soon.")

    async def cmd_tts(self, update, args):
        try:
            if not HAS_GTTS: await safe_reply(update, "❌ gTTS missing"); return
            if len(args) < 2: await safe_reply(update, "❌ tts <text> <lang>"); return
            langs = {"hindi": "hi", "english": "en", "japanese": "ja",
                     "french": "fr", "spanish": "es", "german": "de"}
            lang = args[-1].lower(); text = " ".join(args[:-1])
            if lang not in langs: await safe_reply(update, f"❌ Langs: {', '.join(langs)}"); return
            tts = gTTS(text=text, lang=langs[lang])
            fp = f"{TTS_DIR}/tts_{int(time.time())}.ogg"
            tts.save(fp)
            with open(fp, "rb") as f: await update.message.reply_voice(voice=f)
            os.remove(fp)
        except Exception as e: await safe_reply(update, f"❌ {e}")

    async def cmd_ggs(self, update):
        await safe_reply(update,
            f"📡 𝘞𝘏𝘖 𝘈𝘉𝘉𝘜 𝘝6 👑\n"
            f"🖥️ Inst {INSTANCE_ID}\n"
            f"🤖 {len(state.bots)}\n"
            f"🛡️ {len(state.sudo_users)}\n📂 {len(state.admin_groups)}\n"
            f"⏱️ {get_uptime()}\n"
            f"🏥 {int(health_checkup.ratio()*100)}%")

    async def cmd_ping(self, update):
        t = time.time()
        m = await update.message.reply_text("🏓")
        ms = round((time.time() - t) * 1000, 2)
        txt = f"🎯 {ms}ms\n⏱️ {get_uptime()}\n🤖 {len(state.bots)}\n🖥️ Inst {INSTANCE_ID}"
        try: await m.edit_text(txt)
        except Exception:
            try: await m.delete()
            except Exception: pass
            await safe_reply(update, txt)

    async def cmd_status(self, update):
        cid = update.effective_chat.id
        a = [m for m, v in state.active_chats.get(cid, {}).items() if v]
        await safe_reply(update,
            f"📊 𝘞𝘏𝘖 𝘈𝘉𝘉𝘜 𝘝6\n"
            f"🖥️ Inst {INSTANCE_ID}\n"
            f"🛡️ {len(state.sudo_users)}\n"
            f"🤖 {len(state.bots)}\n⏱️ {get_uptime()}\n"
            f"📂 {len(state.admin_groups)}\n"
            f"🏥 {int(health_checkup.ratio()*100)}%\n"
            f"Active: {', '.join(a) if a else 'None'}")

    async def cmd_rfbots(self, update):
        await safe_reply(update, "🔄 Refreshing...")
        state.bots.clear(); state.update_bot_ids()
        health_checkup.bot_health.clear()
        ok = 0
        for t in BOT_TOKENS:
            try:
                b = Bot(token=t); await b.get_me()
                state.bots.append(b); health_checkup.register(b.id); ok += 1
            except Exception: pass
        state.update_bot_ids()
        if state.bots and not self.leader_bot:
            self.leader_bot = state.bots[0]
        stability_engine.gc()
        await safe_reply(update, self.box("RFBOTS", f"Refreshed {ok} bots.", "🔄"))

    async def cmd_rage(self, update, args):
        if not args: state.rage_mode_enabled = not state.rage_mode_enabled
        elif args[0] in ("on", "1"): state.rage_mode_enabled = True
        elif args[0] in ("off", "0"): state.rage_mode_enabled = False
        if state.rage_mode_enabled:
            state.eco_mode_enabled = False
            await safe_reply(update, RAGE_ON_MSG)
        else:
            await safe_reply(update, RAGE_OFF_MSG)

    async def cmd_eco(self, update, args):
        if not args: state.eco_mode_enabled = not state.eco_mode_enabled
        elif args[0] in ("on", "1"): state.eco_mode_enabled = True
        elif args[0] in ("off", "0"): state.eco_mode_enabled = False
        if state.eco_mode_enabled:
            state.rage_mode_enabled = False
            await safe_reply(update, ECO_ON_MSG)
        else:
            await safe_reply(update, ECO_OFF_MSG)

    # ═══════════════════════════════════════════════════════════════
    #                    HELP MENU — 9 PAGES
    # ═══════════════════════════════════════════════════════════════

    async def cmd_help(self, update, args):
        page = 1
        if args and args[0].isdigit():
            page = int(args[0])
        await self.cmd_help_page(update, page)

    async def cmd_help_page(self, update, page: int):
        try:
            if page == 1: text = self._help_page_1()
            elif page == 2: text = self._help_page_2()
            elif page == 3: text = self._help_page_3()
            elif page == 4: text = self._help_page_4()
            elif page == 5: text = self._help_page_5()
            elif page == 6: text = self._help_page_6()
            elif page == 7: text = self._help_page_7()
            elif page == 8: text = self._help_page_8()
            else: text = self._help_page_9()
            buttons = []
            row1 = []; row2 = []; row3 = []
            for p in (1, 2, 3):
                mark = "◉" if p == page else "○"
                row1.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            for p in (4, 5, 6):
                mark = "◉" if p == page else "○"
                row2.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            for p in (7, 8, 9):
                mark = "◉" if p == page else "○"
                row3.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            buttons.append(row1); buttons.append(row2); buttons.append(row3)
            keyboard = InlineKeyboardMarkup(buttons)
            safe_text = safe_unicode_truncate(text, 4000)
            sent = False
            if page == 1 and os.path.exists(HELP_PHOTO_PATH):
                try:
                    with open(HELP_PHOTO_PATH, "rb") as f:
                        await update.effective_message.reply_photo(
                            photo=f, caption=safe_text[:1024],
                            reply_markup=keyboard)
                    sent = True
                    if len(safe_text) > 1024:
                        for ch in safe_chunk_text(safe_text[1024:], 4000):
                            await safe_reply(update, ch)
                except Exception:
                    sent = False
            if not sent:
                for ch in safe_chunk_text(safe_text, 4000):
                    await safe_reply(update, ch)
        except Exception as e:
            stability_engine.report(e)
            ColorLogger.error(f"help: {e}")
            await safe_reply(update, "❌ Help menu error.")

    def _help_page_1(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 1/9 (NC) ⚔️    ║
╚══════════════════════════════════════════╝

⚔️ ┃ 𝙒𝘼𝙍 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 (NC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚔️ nc <text>              ── Basic
⏳ nct <text>             ── Time NC
⚡ ncs <text>             ── Fast loop
🌀 ncp <text>             ── Parallel
🕐 nctime <text>          ── Timed
🌙 ncmoon <text>          ── Moon emoji
🕰️ ncclock <text>         ── Clock emoji
👑 nckeng <text>          ── Keng emoji
❤️ ncheart <text>         ── Heart emoji
⚡ ncgawd <text>          ── GAWD emoji
🔥 ncx <text>             ── Internal
👑 ncgod <text>           ── 5x parallel/bot
🌀 ncloop <text>          ── Loop
🌀 ncy <text>             ── Quad
🌀 ncxy <text>            ── Emoji loop
🔺 ncyx <text>            ── Pentagon (5x/bot)
🎯 ncz <text>             ── Opponent detect
🌀 ncwxs <text>           ── Loop emoji
😀 ncemo <text>           ── Emoji loop
💠 ncq <text>             ── Parallel+Penta
🫧 whonc <text>           ── WhoNC (17 texts!)

🛑 NC STOPS:
   snc / sgod / sncx / sncloop / sncy
   sncxy / sncyx / sncz / sncwxs
   sncemo / sncq / snckeng / sncgawd
   swhonc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_2(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 2/9 (SP/SLIDE)❤️║
╚══════════════════════════════════════════╝

❤️ ┃ 𝙏𝙀𝘾𝙃𝙉𝙄𝙌𝙐𝙀 𝘼𝙍𝙍𝘼𝙔 (spam msg loops)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❤️ sp1 <extra>           ── SP1
❤️ sp2 <extra>           ── SP2
❤️ sp3 <extra>           ── SP3
❤️ sp4 <extra>           ── SP4
❤️ sp5 <extra>           ── SP5
❤️ sp6 <extra>           ── SP6
🛑 ssp / stopsp
⏱️ dsp <d>              0.0–1.0

🩷 ┃ 𝘼𝙍𝙎𝙀𝙉𝘼𝙇 𝙎𝙃𝙊𝙏𝙎 (reply target)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🩷 slide1 (reply)        ── Slide 1
🩷 slide2 (reply)        ── Slide 2
🩷 slide3 (reply)        ── Slide 3
🩷 slide4 (reply)        ── Slide 4
🩷 slide5 (reply)        ── Slide 5
🛑 sslide / stopslide
⏱️ dslide <d>           0.01–1.0

🗳️ ┃ 𝙋𝙊𝙇𝙇
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🗳️ poll <q> | <opt1> | <opt2>
🛑 spoll / stoppoll
⏱️ dpoll <d>            0.001–1.0

⚡ ┃ 𝙈𝙐𝙇𝙏𝙄𝙏𝘼𝙍𝙂𝙀𝙏
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ multitarget @user1 @user2 ...
📋 targetlist
🗑️ cleartargets
🛑 smt / stopmt / stopmultitarget
⏱️ dmt <d>              0.001–0.5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_3(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 3/9 (SPAM) 📢║
╚══════════════════════════════════════════╝

📢 ┃ 𝙓𝙎𝙋𝘼𝙈 & 𝙆𝙀𝙉𝙂𝙎𝙋𝘼𝙈
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📢 xspam <text>          ── XSPAM
🛑 sxspam / ⏱️ dxspam <d> (0.001–1.0)

💥 kengspam <text>       ── Keng
🛑 skspam / ⏱️ kdelay <d> (0.1–1.0)

📌 autopinspam <text>    ── Auto pin
🛑 saps / ⏱️ apdelay <d> (0.1–1.0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 ┃ 𝙈𝘼𝙉𝘼 𝘽𝘼𝙍𝙍𝘼𝙂𝙀 (msg loop)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 s1 <text>             ── Series 1
🛑 sss1 / ⏱️ ds1 <d>     0.001–1.0

📝 s2 <text>             ── Series 2
🛑 sss2 / ⏱️ ds2 <d>     0.001–1.0

📝 s3 <text>             ── Series 3
🛑 sss3 / ⏱️ ds3 <d>     0.001–1.0

🌀 xs <text>             ── XS (100 msg, 5s pause)
🛑 sxs / ⏱️ dxs <d>      0.001–1.0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎮 ┃ 𝙂𝘼𝙈𝙀𝙊𝙑𝙀𝙍 (reply)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎮 gameover <text>       ── Leader-only, ONCE
🛑 sgameover / ⏱️ dgameover <d> (0.01–1.0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_4(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 4/9 (RAID) 🎯║
╚══════════════════════════════════════════╝

🎯 ┃ 𝘿𝙊𝙈𝘼𝙄𝙉 𝙒𝘼𝙍 (reply)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 rr <text>             ── Reply raid
🛑 srr / ⏱️ drr <d>      0.0001–0.1

🔪 sl (reply)            ── Slaughter
🛑 ssl / ⏱️ ds <d>       0.0001–0.1

🪩 ts (reply)            ── Target slide
🛑 sts / ⏱️ dts <d>      0.0001–0.5

⚡ sw <text> (reply)     ── Swipe
🛑 ssw / ⏱️ dsw <d>      0.0001–0.1

⚔️ sxr (reply)           ── SX reply raid
🛑 ssx / ⏱️ dsx <d>      0.001–0.1

🔥 x (reply)             ── X raid
🛑 sx / ⏱️ dx <d>        0.001–0.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎭 ┃ 𝙍𝙀𝘼𝘾𝙏𝙄𝙊𝙉𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ autoreact [e] / sar
🌟 greact [e] / sgreact
💜 creact [e] / screact
🎭 mar ── Ultra-fast (0.0001s)
🛑 smar / ⏱️ dmar <d>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_5(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 5/9 (CLEAN) 🪄║
╚══════════════════════════════════════════╝

🪄 ┃ 𝘾𝙇𝙀𝘼𝙉𝙎𝙀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧹 purge / 🛡️ unpurge
🗑️ delall / sdel / ddelall <d>
🗑️ delmsg / sdelmsg / ddelmsg <d>

🪽 ┃ 𝘽𝘼𝙏𝙏𝙇𝙀 𝙎𝙏𝘼𝙉𝘾𝙀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌪️💢 rage on|off
└─ 𝘽𝙀𝙍𝙎𝙀𝙍𝙆𝙀𝙍 𝙈𝙊𝘿𝙀

🌙🌿 eco on|off
└─ 𝙀𝘾𝙊 𝙈𝙊𝘿𝙀

🌌 legion ── 𝙇𝙀𝙂𝙄𝙊𝙉 𝙀𝙑𝙊𝙇𝙐𝙏𝙄𝙊𝙉

⛩️ ┃ 𝙂𝘼𝙐𝙍𝘿𝙄𝘼𝙉𝙎 𝙒𝘼𝙏𝘾𝙃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💫 rfbots ── 𝙍𝙀𝙁𝙍𝙀𝙎𝙃 𝙇𝙀𝙂𝙄𝙊𝙉
🫀 health ── 𝙆𝙄𝙉𝙂𝘿𝙊𝙈 𝙃𝙀𝘼𝙇𝙏𝙃
🔔 ping ── 𝙃𝙀𝙍𝘼𝙇𝘿
📜 status ── 𝙍𝙀𝘼𝙇𝙈 𝙍𝙀𝙋𝙊𝙍𝙏
🕰️ uptime ── 𝙍𝙀𝙄𝙂𝙉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_6(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 6/9 (MEDIA) 📖║
╚══════════════════════════════════════════╝

📖 ┃ 𝙍𝙀𝙇𝙄𝘾𝙎 & 𝙎𝘾𝙍𝙊𝙇𝙇𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎙️ savevoice / stv / sv
📸 savephoto / stpic / spic
🎞️ savegif / stgif / sgif
🏷️ savesticker / ststicker / ssticker
📸 startphoto / 🛑 stopgcpfp / 🎬 vmd

📦 ┃ 𝘼𝙍𝙏𝙄𝙁𝘼𝘾𝙏 𝙑𝘼𝙐𝙇𝙏
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📸 stpic / pic           ── Photo spam
🛑 spic / stoppic / ⏱️ dp <d>

🖼️ startphoto            ── GC PFP changer
🛑 stopgcpfp / vmd / ⏱️ gdelay <d>

🗑️ delmsg / sdelmsg / ⏱️ ddelmsg <d>
🗑️ delall / sdel / ⏱️ ddelall <d>

🛡️ ┃ 𝙎𝙀𝘾𝙏 𝘼𝙐𝙏𝙃𝙊𝙍𝙄𝙏𝙔
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛡️ mute (reply)          ── Mute user
🔊 unmute (reply)        ── Unmute user
🔒 lockgc / 🔓 unlockgc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_7(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 7/9 (DELAYS) ⏱️║
╚══════════════════════════════════════════╝

⏱️ ┃ 𝙉𝘾 𝘿𝙀𝙇𝘼𝙔 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚔️ delaync <d>      0.0001–0.1
⏳ delaynct <d>     0.0001–0.5
⚡ delayncs <d>     0.0001–0.1
🌀 dncp <d>         0.0001–0.1
🔺 dncy <d>         0.0001–1.0
👑 dngod <d>        0.0001–0.5
🔥 dncx <d>         0.0001–0.5
🌀 dncloop <d>      0.0001–0.5
🫧 dwnc <d>         0.0001–0.5
🕐 dnctime <d>      0.0001–0.5
🌙 dncmoon <d>      0.0001–0.5
🕰️ dncclock <d>     0.0001–0.5
👑 dnckeng <d>      0.0001–0.5
❤️ dncheart <d>     0.0001–0.5
⚡ dncgawd <d>      0.0001–0.5
🌀 dncxy <d>        0.0001–0.05
🔺 dncyx <d>        0.0001–0.5
🎯 dncz <d>         0.0001–0.7
🌀 dncwxs <d>       0.0001–0.5
😀 dncemo <d>       0.0001–0.5
💠 dncq <d>         0.0001–0.1

🎭 EMOJI NC DELAYS:
   ddnc/dlnc/dknc/danc/denc
   dgnc/dznc/dcnc/dmnc <d>
   Range: 0.0005–0.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📢 ┃ 𝙊𝙏𝙃𝙀𝙍 𝘿𝙀𝙇𝘼𝙔𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❤️ dsp <d>          0.0–1.0
🩷 dslide <d>       0.01–1.0
🗳️ dpoll <d>        0.001–1.0
⚡ dmt <d>          0.001–0.5
📢 dxspam <d>       0.001–1.0
💥 kdelay <d>       0.1–1.0
📌 apdelay <d>      0.1–1.0
🎯 drr <d>          0.0001–0.1
🔪 ds <d>           0.0001–0.1
🪩 dts <d>          0.0001–0.5
⚡ dsw <d>          0.0001–0.1
⚔️ dsx <d>          0.001–0.1
🔥 dx <d>           0.001–0.1
📝 ds1/ds2/ds3 <d>  0.001–1.0
🌀 dxs <d>          0.001–1.0
🎭 dmar <d>         0.0001–1.0
🎮 dgameover <d>    0.01–1.0
🗑️ ddelall <d>      0.0001–0.1
🗑️ ddelmsg <d>      0.0001–1.0
📸 dp <d>           0.01–1.0
🖼️ gdelay <d>       0.0001–0.5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_8(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 8/9 (EMOJI NC)🎭║
╚══════════════════════════════════════════╝

🎭 ┃ 𝙀𝙈𝙊𝙅𝙄 𝙉𝘾 𝙈𝙊𝘿𝙀𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐉 Dnc <text>   ── Dragon / Fire / Wing
🌊 Lnc <text>   ── Sea / Trident / Wave
⚔️ Knc <text>   ── Knight / Sword / Shield
🏹 Anc <text>   ── Archer / Eye / Feather
🍄 Enc <text>   ── Elven / Mushroom / Tree
👹 Gnc <text>   ── Goblin / Chain / Axe
⚡ Znc <text>   ── Zeus / Lightning / Storm
🌋 Cnc <text>   ── Cerberus / Wolf / Dark
🔮 Mnc <text>   ── Mage / Magic / Crystal

🎭 𝙀𝙈𝙊𝙅𝙄 𝙉𝘾 𝘿𝙀𝙇𝘼𝙔𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ddnc  → Dnc delay
dlnc  → Lnc delay
dknc  → Knc delay
danc  → Anc delay
denc  → Enc delay
dgnc  → Gnc delay
dznc  → Znc delay
dcnc  → Cnc delay
dmnc  → Mnc delay

📏 Range: 0.0005–0.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def _help_page_9(self) -> str:
        return """╔══════════════════════════════════════════╗
║  👑 𝗣ʀᴇғɪ᥊ᴇ𝗥 𝘼𝘽𝘽𝙐 𝙑6 — PAGE 9/9 (WHONC) 🫧║
╚══════════════════════════════════════════╝

🫧 ┃ 𝗣ʀᴇғɪ᥊ᴇ𝗥𝙉𝘾 𝙈𝙊𝘿𝙀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🫧 whonc <text>          ── Start WhoNC mode
🛑 swhonc                ── Stop WhoNC
⏱️ dwnc <d>              ── Set delay (0.0001–0.5s)

📝 How it works:
   1. Choose random text from 17 slots
   2. Replace (test) with your <text>
   3. Append a random loop emoji
   4. Set as group title repeatedly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛑 ┃ 𝘼𝙇𝙇 𝙉𝘾 𝙎𝙏𝙊𝙋𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   snc / sgod / sncx / sncloop / sncy
   sncxy / sncyx / sncz / sncwxs
   sncemo / sncq / snckeng / sncgawd
   swhonc

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ ┃ 𝙀𝙈𝙊𝙅𝙄 𝙉𝘾 𝙈𝙊𝘿𝙀𝙎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dnc / Lnc / Knc / Anc / Enc
Gnc / Znc / Cnc / Mnc <text>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 help1 → help9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    async def handle_help_callback(self, update, context):
        try:
            q = update.callback_query
            if not q: return
            await q.answer()
            if not q.data or not q.data.startswith("helppage_"): return
            try:
                page = int(q.data.replace("helppage_", ""))
            except Exception: page = 1
            if page == 1: text = self._help_page_1()
            elif page == 2: text = self._help_page_2()
            elif page == 3: text = self._help_page_3()
            elif page == 4: text = self._help_page_4()
            elif page == 5: text = self._help_page_5()
            elif page == 6: text = self._help_page_6()
            elif page == 7: text = self._help_page_7()
            elif page == 8: text = self._help_page_8()
            else: text = self._help_page_9()
            buttons = []
            row1 = []; row2 = []; row3 = []
            for p in (1, 2, 3):
                mark = "◉" if p == page else "○"
                row1.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            for p in (4, 5, 6):
                mark = "◉" if p == page else "○"
                row2.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            for p in (7, 8, 9):
                mark = "◉" if p == page else "○"
                row3.append(InlineKeyboardButton(f"{mark} P{p}", callback_data=f"helppage_{p}"))
            buttons.append(row1); buttons.append(row2); buttons.append(row3)
            keyboard = InlineKeyboardMarkup(buttons)
            try:
                await q.edit_message_caption(caption=text[:1024], reply_markup=keyboard)
            except Exception:
                try:
                    await q.edit_message_text(text=text[:4000], reply_markup=keyboard)
                except Exception:
                    try: await q.message.reply_text(text[:4000], reply_markup=keyboard)
                    except Exception: pass
        except Exception as e:
            stability_engine.report(e)


# ═══════════════════════════════════════════════════════════════════════════════
#                              BACKGROUND
# ═══════════════════════════════════════════════════════════════════════════════

async def _stability_daemon():
    await asyncio.sleep(15)
    while True:
        try:
            stability_engine.cycles += 1
            stability_engine.gc()
            state.prune()
            BufferLogger._flush()
        except Exception as e:
            stability_engine.report(e)
        await asyncio.sleep(30)

async def _dashboard():
    await asyncio.sleep(10)
    while True:
        try:
            up = int(time.time() - BOT_START_TIME)
            active = sum(1 for m in state.active_chats.values() for v in m.values() if v)
            ColorLogger.info(
                f"📊 Inst:{INSTANCE_ID} Bots:{len(state.bots)} Groups:{len(state.admin_groups)} "
                f"Active:{active} Up:{up//3600}h")
        except Exception: pass
        await asyncio.sleep(30)

async def error_handler(update, context):
    try:
        stability_engine.report(context.error)
        ColorLogger.error(f"global: {context.error}")
    except Exception: pass

async def main():
    if not _acquire_instance_lock(LOCK_PORT):
        print(f"❌ Instance with port {LOCK_PORT} already running! Exiting.")
        sys.exit(1)
    print(f"✅ Instance lock on port {LOCK_PORT}")

    bot = WhoAbbuBot()
    await bot.init_bots()

    app = Application.builder().token(BOT_TOKENS[0]).build()
    app.add_handler(MessageHandler(filters.ALL, bot.handle_message))
    app.add_handler(CallbackQueryHandler(bot.handle_help_callback, pattern="^helppage_"))
    app.add_error_handler(error_handler)

    await app.initialize()
    await app.start()
    await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)

    fire_and_forget(_dashboard())
    fire_and_forget(_stability_daemon())

    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit): pass
    finally:
        try: BufferLogger._flush()
        except Exception: pass
        await app.updater.stop()
        await app.stop()
        await app.shutdown()
        _release_instance_lock()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n👋 Instance {INSTANCE_ID} stopped")
    except Exception as e:
        print(f"❌ {e}")
        traceback.print_exc()
