import sys
import logging
from pyrogram import Client
from Config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Validate Config
missing = []
if not Config.BOT_TOKEN:
    missing.append("BOT_TOKEN")
if not Config.APP_ID:
    missing.append("APP_ID")
if not Config.API_HASH:
    missing.append("API_HASH")

if missing:
    logging.error(f"Missing configuration: {', '.join(missing)}. Please set the environment variables in Railway.")
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
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    logging.info("Bot is starting...")
    app.run()
    logging.info("Bot stopped gracefully.")
except Exception as e:
    logging.exception(f"Failed to start the bot: {e}")
    sys.exit(1)
