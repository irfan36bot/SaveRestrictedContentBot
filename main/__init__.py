#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=16784506, cast=int)
API_HASH = config("API_HASH", default=562689b74bbd77c6baeceb097204c191)
BOT_TOKEN = config("BOT_TOKEN", default=5810976226:AAHMZDOVu5KBapO__fTBOd5bZ-TknOXJoRU)
SESSION = config("SESSION", default=BQEO_1IAbkm1MUN3BccUYgDelw4oLgYa6w5bLmH5VRWZhRI41UX2BB11gAAuA1wGp3IjPvgAdc_SiC_8lAxG7llQ30xbt-mgCoy2L3KXXWJZz4RR8X-0gDLpNS170t944E6Eub3NFy3y_Vd1iISCGNn36X5_2Qjd-oK6wzYuoLFHcnLSFSWBOGnusPRUgI3YF7tQ7g0M36pzXeHNCf7Cw6NAVNyhDi4yZgKC6Wbd-97xxvbU_YmiqiOAa7Ee6QtBklt2hiNee_TxO5ISPcFgwGCyjhgu61xGiuNNELUtUzjiIUP84DFZyeVJq1CkWwk8iQCKj2dSbOwCLajA5mX7-pRzyYzk9QAAAAE_AG8rAA)
FORCESUB = config("FORCESUB", default=DS_Botz)
AUTH = config("AUTH", default=1125671241, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
