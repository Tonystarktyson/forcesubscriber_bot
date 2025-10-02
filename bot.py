import sys
import logging
from pyrogram import Client
from pyrogram.enums import ParseMode
from Config import BOT_TOKEN, API_ID, API_HASH, Messages

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Plugins setup
plugins = dict(
    root="plugins",
    include=[
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
