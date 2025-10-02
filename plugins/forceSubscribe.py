from pyrogram import Client, filters, ChatPermissions
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram.errors
import sql_helpers.forceSubscribe_sql as sql

# Button callback
@Client.on_callback_query(filters.regex("onButtonPress"))
def onButtonPress(client, cb):
    user_id = cb.from_user.id
    chat_id = cb.message.chat.id
    cws = sql.fs_settings(chat_id)
    if not cws:
        return
    channel = cws.channel
    try:
        client.get_chat_member(channel, user_id)
        client.unban_chat_member(chat_id, user_id)
    except pyrogram.errors.UserNotParticipant:
        client.answer_callback_query(cb.id, text="Join the channel and press the button again.")

# Force subscribe on text messages
@Client.on_message(filters.text & ~filters.private)
def check_subscription(client, message):
    cws = sql.fs_settings(message.chat.id)
    if not cws:
        return

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    channel = cws.channel

    try:
        client.get_chat_member(channel, user_id)
        return
    except pyrogram.errors.UserNotParticipant:
        status = client.get_chat_member(message.chat.id, user_id).status
        if status in ("administrator", "creator"):
            return
        message.reply_text(
            f"[{first_name}](tg://user?id={user_id}), you are **not subscribed** to my [channel](https://t.me/{channel}) yet. Please [join](https://t.me/{channel}) and **press the button below** to unmute yourself.",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("UnMute Me", callback_data="onButtonPress")]]
            ),
            parse_mode="MarkdownV2"
        )
        client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=False))
    except (pyrogram.errors.ChatAdminRequired, ValueError):
        client.send_message(message.chat.id, text=f"I am not an admin in @{channel}")

# /forcesubscribe command
@Client.on_message(filters.command(["forcesubscribe"]) & ~filters.private)
def configure(client, message):
    user = client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status == "creator":
        chat_id = message.chat.id
        try:
            input_str = message.command[1].replace("@", "")
        except IndexError:
            if sql.fs_settings(chat_id):
                message.reply_text(f"Force Subscribe is **enabled** in this chat.\nChannel - @{sql.fs_settings(chat_id).channel}")
                return
            else:
                message.reply_text("Force Subscribe is **disabled** in this chat.")
                return

        if input_str.lower() in ("off", "no", "disable"):
            sql.disapprove(chat_id)
            message.reply_text("Force Subscribe is **Disabled**")
        elif input_str:
            try:
                client.get_chat_member(input_str, "me")
                sql.add_channel(chat_id, input_str)
                message.reply_text(f"Force Subscribe is **enabled** for this chat\nChannel - @{input_str}")
            except pyrogram.errors.UserNotParticipant:
                message.reply_text(f"I am not an admin in @{input_str}\nAdd me on your channel as admin and send the command again.")
            except pyrogram.errors.UsernameNotOccupied:
                message.reply_text(f"Invalid Channel Username")
            except ValueError:
                message.reply_text(f"@{input_str} didn't belongs to a channel.")
        else:
            message.reply_text("Something went wrong")
    else:
        message.reply_text("You have to be the **Group Creator** to do that.")
