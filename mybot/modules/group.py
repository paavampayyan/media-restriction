import os
import random
from time import time as gg
import time as dl
from pyrogram import Client, emoji, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from mybot import bot

TARGET = ["acd321", "status_group_malayalam"]
admin_group = "status_group_admins"

@bot.on_message(filters.command(['start']) & filters.private)
def start(client, message):
    message.reply_text("Who are you what you want??")


@bot.on_message(filters.command(['help']) & filters.private)
def help(client, message):
    message.reply_text("why should i help you? who the hell are you?")

@bot.on_message(filters.chat(TARGET) & filters.new_chat_members)
def welcome(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    print(chat_id, user_id, user_name)
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    bot.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=True), int(gg() + 172800))
    m = message.reply_text(f"Sorry {rpk} 😕. As a security purposes i restrict you from sending media files to our group  up to next 48 hrs ✋🏻. contact group admin's if you have any queries.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Adminlist", callback_data="admins {}")]
            ]
        ),
        disable_web_page_preview=True,
    )

    bot.send_message(chat_id=admin_group, text=f"i resticted {rpk} media permissions.")
    bot.send_message(chat_id=admin_group, text=f"{user_id} reply to this message to unmute {rpk}")
    


    dl.sleep(120)
    m.delete()


@bot.on_callback_query(filters.regex("admins"))
def en(client, callback_query):
    callback_query.message.edit(
        "**Status Group Adminlist ⚜️**\n\n"
        "⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰ \n\n"
        " ➲ @nousername_psycho\n"
        " ➲ @cyper666 \n"
        " ➲ @Komban_war\n"
        " ➲ @Sathan_Of_Telegram\n"
        " ➲ @voicemagic1\n\n"
        "⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰",

       reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("close", callback_data="close {}")]
            ]
        ),
        disable_web_page_preview=True,
    )


@bot.on_callback_query(filters.regex("close"))
def close(client, callback_query):
    c_group = callback_query.message.chat
    user_close = callback_query.from_user
    closer_status = (c_group.get_member(user_close.id)).status
    message_CQ = callback_query.message.reply_to_message
    closer = message_CQ.from_user
    if user_close.id == closer.id:
        callback_query.message.delete()
    elif closer_status in ("creator", "administrator"):
        callback_query.message.delete()

    else:
        callback_query.answer(f"nee eathaa myre?")
        return

