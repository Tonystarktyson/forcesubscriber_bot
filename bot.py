import sys
import logging
from pyrogram import Client
from Config import BOT_TOKEN, API_ID, API_HASH, Messages

# Debug: print variables to make sure Railway injected them
print("BOT_TOKEN:", BOT_TOKEN)
print("API_ID:", API_ID)
print("API_HASH:", API_HASH)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Validate Config
missing = []
if not BOT_TOKEN:
    missing.append("BOT_TOKEN")
if not API_ID:
    missing.append("API_ID")
if not API_HASH:
    missing.append("API_HASH")

if missing:
    logging.error(f"Missing configuration: {', '.join(missing)}. Please update Service Variables in Railway.")
    sys.exit(1)

# Plugins setup
plugins = dict(
    root="plugins",
    include=[
        "start",
        "help",
        "forceSubscribe"
    ]
)

# Initialize and run bot
try:
    app = Client(
        "eagle_eye",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    logging.info("Bot is starting...")
    app.run()
    logging.info("Bot stopped gracefully.")
except Exception as e:
    logging.exception(f"Failed to start the bot: {e}")
    sys.exit(1)
