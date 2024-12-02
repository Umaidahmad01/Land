import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7255422393:AAEpTMHjS_qpGs7dcoDpHMJsQc_ZmxnP8pg")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20718334"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002177334941"))

# DEV ID
DEV_ID = int(os.environ.get("DEV_ID", "5585016974"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://uffobitoxe:umaid2008@cluster0.vpebe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002072642438"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002056122922"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://envs.sh/Chb.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/Chb.jpg")

# Add your text according to your preference
HELP_TXT = "<b>ᴅᴍ <a href=https://t.me/Madhav_S9>sᴏʟᴏ</a></a></b>"
ABOUT_TXT = "<b>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Madhav_S9>sᴏʟᴏ</a>\n» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/TEAM_HTX>ᴛᴇᴀᴍ ʜᴛx</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/anime_hindi_sub_industry>ᴀɴɪᴍᴇ ɪɴᴅᴜsᴛʀʏ</a>\n» ᴏɴɢᴏɪɴɢ ɪɴᴅᴜsᴛʀʏ : <a href=https://t.me/OngoingAnime_Industry>ᴏɴɢᴏɪɴɢ ɪɴᴅᴜsᴛʀʏ</a>\n» ɪɴᴅᴜsᴛʀʏ ɴᴇᴡs : <a href=https://t.me/Anime_News_Industry>ɪɴᴅᴜsᴛʀʏ ɴᴇᴡs</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/i_killed_my_clan>ᴏʙɪᴛᴏ</a></b>"# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://t.me/animes_society_official>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a></b>")
try:
    ADMINS=[5585016974]
    for x in (os.environ.get("ADMINS", "5585016974").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "» ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫ᴍᴋʟ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - <a href=https://t.me/animes_society_official>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a></b>"


OWNER_ID = int(os.environ.get("OWNER_ID", "5585016974"))
ADMINS.append(OWNER_ID)
ADMINS.append(5585016974)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
