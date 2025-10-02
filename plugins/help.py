from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from Config import Messages as tr

# Keyboard mapping
def keyboard_map(pos):
    if pos == 1:
        button = [[InlineKeyboardButton(text='-->', callback_data="help+2")]]
    elif pos == len(tr.HELP_MSG) - 1:
        url = "https://t.me/super_botz_support"
        button = [
            [InlineKeyboardButton(text='Support Chat', url=url)],
            [InlineKeyboardButton(text='Feature Request', url=url)],
            [InlineKeyboardButton(text='<--', callback_data=f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text='<--', callback_data=f"help+{pos-1}"),
                InlineKeyboardButton(text='-->', callback_data=f"help+{pos+1}")
            ]
        ]
    return button

# /start command
@Client.on_message(filters.private & filters.command("start"))
def start(client, message):
    try:
        client.send_message(
            chat_id=message.chat.id,
            text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    except Exception as e:
        print(f"[ERROR] /start failed: {e}")

# /help command
@Client.on_message(filters.private & filters.command("help"))
def help_command(client, message):
    try:
        client.send_message(
            chat_id=message.chat.id,
            text=tr.HELP_MSG[1],
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_notification=True,
            reply_markup=InlineKeyboardMarkup(keyboard_map(1))
        )
    except Exception as e:
        print(f"[ERROR] /help failed: {e}")

# Callback query for help buttons
@Client.on_callback_query(filters.regex(r"^help\+\d+$"))
def help_answer(client, callback_query):
    try:
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        pos = int(callback_query.data.split('+')[1])

        client.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=tr.HELP_MSG[pos],
            reply_markup=InlineKeyboardMarkup(keyboard_map(pos))
        )
    except Exception as e:
        print(f"[ERROR] Help callback failed: {e}")
