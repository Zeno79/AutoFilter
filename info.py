import re, os
from os import environ, getenv
from Script import script
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^-?\d+$')  # Regex to match numeric IDs (including negatives like for channels)

def is_enabled(value, default):
    if isinstance(value, str):  # Ensure value is a string before lowering
        value = value.lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def get_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = get_int(environ.get('API_ID', '21983955'))
API_HASH = environ.get('API_HASH', 'edc3c906b06c2dd3dc6ee4c2573fb3f1')
OWNER_ID = get_int(environ.get('OWNER_ID', '5957500906'))
BOT_TOKEN = environ.get('BOT_TOKEN', "6005947500:AAEdfOGTZeoGbF2dPECpduLrmmy1pMMOWuI")

# Bot settings
CACHE_TIME = get_int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)

PICS = environ.get('PICS', '').split() or [
    'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg',
    'https://graph.org/file/d6d9d9b8d2dc779c49572.jpg'
]

NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/6988f560cf6d67339f628.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/549fd9f3272214acade82.jpg")
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://graph.org/file/347c1f79f36d3cf14e0f5.jpg')

# Stream link shortener
STREAM_SITE = environ.get('STREAM_SITE', 'shareus.io')
STREAM_API = environ.get('STREAM_API', '')
STREAMHTO = environ.get('STREAMHTO', 'https://t.me/How_to_Download_7x/32')

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
PREFIX = environ.get("PREFIX", "/")

CHAT_GROUP = get_int(environ.get("CHAT_GROUP", "-1001953724858"))

# Admins, Channels & Users
ADMINS = [get_int(admin, admin) for admin in environ.get('ADMINS', '6497757690 5115691197').split()]
CHANNELS = [get_int(ch, ch) for ch in environ.get('CHANNELS', '0').split()]
auth_users = [get_int(user, user) for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [get_int(user, user) for user in environ.get('PREMIUM_USER', '6497757690').split()]

auth_channel = environ.get('AUTH_CHANNEL', '0')
AUTH_CHANNEL = get_int(auth_channel) if id_pattern.search(auth_channel) else None

auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [get_int(ch) for ch in auth_grp.split()] if auth_grp else None

support_chat_id = environ.get('SUPPORT_CHAT_ID', '0')
SUPPORT_CHAT_ID = get_int(support_chat_id)

reqst_channel = environ.get('REQST_CHANNEL_ID', '0')
REQST_CHANNEL = get_int(reqst_channel)

NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "False"), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://luffyx7819:R0xYGEYRui9e2ScP@cluster1.lyqtfz7.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Lucy")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# chatgptAI
AI = is_enabled(environ.get("AI", "True"), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")

# Further configurations...

# Verify other settings are enabled
IMDB = is_enabled(environ.get('IMDB', "False"), False)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "True"), True)
# etc...
