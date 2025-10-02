Eagle Scout Bot

A Telegram Bot to force users to join a specific channel before sending messages in a group.

Find it on Telegram as Eagle Scout

Features

Force group members to join a specific channel before sending messages.

Configure different channels for different groups.

/start and /help commands in private chat.

Automatic unmute once a user joins the channel.

Admin-safe: does not mute group admins or creators.

Todo

 Add support for multiple channels per group

 Configure different groups with different channels

 Auto-clean bot messages after unmute

Deployment
1️⃣ Clone the repository
git clone https://github.com/viperadnan-git/eagle-telegram-bot.git
cd eagle-telegram-bot

2️⃣ Install requirements
pip3 install -r requirements.txt

3️⃣ Configure Environment

You can either edit Config.py directly or use environment variables via .env:

Using .env

cp .env.example .env
nano .env


Set the following:

BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here
DATABASE_URL=sqlite:///bot.db  # Optional, defaults to SQLite

4️⃣ Run the bot
python3 bot.py


The bot should start and be ready to manage your groups.

Optional: Deploy on Railway

Create a new project on Railway

Connect GitHub repo

Add environment variables (BOT_TOKEN, API_ID, API_HASH, DATABASE_URL) in Railway project settings

Set start command:

python3 bot.py


Deploy and the bot will run 24/7

Notes

Ensure the bot is admin in both your group and your channel.

Only the group creator can enable or disable force subscribe using /forcesubscribe.
