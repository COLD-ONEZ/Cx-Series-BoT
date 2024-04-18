import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/bbd1d86d41da4f6541286.jpg https://telegra.ph/file/251425550021d48bf71a6.jpg https://telegra.ph/file/02d9ac2f1f55d1ac6b55b.jpg https://telegra.ph/file/77cfaae36401a4de24703.jpg https://telegra.ph/file/48ada7dbc0eb818c279a8.jpg https://telegra.ph/file/2ff10857cf66ef34465e3.jpg https://telegra.ph/file/f2302ac2a2c4221a55d41.jpg https://telegra.ph/file/16166fd1c8cce77260559.jpg https://telegra.ph/file/858f0211db7e37d623f6e.jpg https://telegra.ph/file/8b1c885aed32d7a6c47cc.jpg https://telegra.ph/file/24d3aaf47bceff497b224.jpg https://telegra.ph/file/b40a39a2e9cbf0e595286.jpg https://telegra.ph/file/6e9503d3646f123437e42.jpg https://telegra.ph/file/054db06463aa981f60125.jpg https://telegra.ph/file/f7c8ece5a79fbfdbaf5a5.jpg https://telegra.ph/file/546ad993fe55e0168a4c2.jpg https://telegra.ph/file/37a1a25ecb9de57f321c8.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/2c21b0d0e9348df316318.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/e55bc695a38ce8b977f82.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

CLOSE_IMG = (environ.get('CLOSE_IMG', 'https://telegra.ph/file/6e9dd701bac49632cf79a.jpg https://telegra.ph/file/998d2b84e1411ed5189e3.jpg https://telegra.ph/file/c199babd469011d07f139.jpg https://telegra.ph/file/31b6d3d2c70bbe52b5300.jpg https://telegra.ph/file/77744524fbb6305298d45.jpg https://telegra.ph/file/9d79d990674166a2a2364.jpg')).split()


BOT_START_TIME = 'time'

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# Request To Join
REQ_CHANNEL = environ.get('REQ_CHANNEL', "")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get('DATABASE_URI')
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), True)

# Auto Delete Information
AUTO_DELETE = int(environ.get('AUTO_DELETE', "10")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get('AUTO_DELETE_TIME', "600")) # Time in Seconds

#COLD REQEST_LINK
COLDREQLINK = environ.get('COLDREQLINK', "")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001977832240').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/Verifying5754/3")
VERIFY2_URL = environ.get('VERIFY2_URL', "linkshortify.com")
VERIFY2_API = environ.get('VERIFY2_API', "4b285124282f3253426e9020826d1b5f2528a641")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'linkshortify.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '4b285124282f3253426e9020826d1b5f2528a641')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'True')),True)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/TEAM_COLD_BOT')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TEAM_COLD')
MSG_ALRT = environ.get('MSG_ALRT', 'Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ Ꮯᴏʟᴅ_Ꮻɴᴇᴢ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/TEAM_COLD_BOT')
S_GROUP = environ.get('S_GROUP',"https://t.me/TEAM_COLD_BOT")
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
