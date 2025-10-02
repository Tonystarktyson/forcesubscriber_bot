import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Telegram API credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH", "").strip()

# Validate API_ID
try:
    API_ID = int(API_ID)
except (TypeError, ValueError):
    API_ID = 0

# Database URL (fallback to SQLite)
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///bot.db")

# Validate essential configs
missing_configs = []
if not BOT_TOKEN:
    missing_configs.append("BOT_TOKEN")
if not API_ID:
    missing_configs.append("API_ID")
if not API_HASH:
    missing_configs.append("API_HASH")

if missing_configs:
    raise ValueError(f"Missing critical config(s): {', '.join(missing_configs)}")

# Messages
class Messages:
    HELP_MSG = [
        ".",
        "**Force Subscribers**\nForce group members to join a specific channel before sending messages in the group.\n\n"
        "**Setup**\n"
        "**Step 1.** __Add me in a group (where you are the creator) as admin.__\n"
        "**Step 2.** __Send__ `/ForceSubscribe {your channel username}`\n"
        "**Step 3.** __Add me to your channel as admin.__\n\n"
        "`All set! I mute users who didn't join your channel and ask them to join channel to unmute themselves.`\n\n"
        "**Commands**\n\n"
        "/ForceSubscribe { off / no / disable} - To stop force subscriber\n"
        "/ForceSubscribe {Channel Username} - Set the Channel\n"
        "/ForceSubscribe - Get current Status",
        
        "**Developed by @admin 🇮🇳**\n\nPowered by @admin 🇮🇳\nThanks to - @PyroGram @HasibulKobir"
    ]

    START_MSG = (
        "Hey [{}](tg://user?id={})\n"
        "I am a multifunctional group manager bot.\n"
        "Learn more at /help"
    )
