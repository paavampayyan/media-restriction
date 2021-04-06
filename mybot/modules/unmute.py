import os
import random
from time import time as gg
import time as dl
from pyrogram import Client, emoji, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from mybot import bot

chat_id = "-1001266612390" 
unmute_rejex = r"unmute|Unmute"
ban_rejex = r"ban|Ban"

@bot.on_message(filters.chat("status_group_admins") & filters.regex(unmute_rejex))
def unmute(client,message):
    user_id = message.reply_to_message.text.split()[0]
    user_name = message.reply_to_message.text.split()[7]
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    bot.unban_chat_member(chat_id, user_id)
    bot.send_chat_action(chat_id=chat_id, action="typing")
    bot.send_message(chat_id=chat_id, text=f"hello {rpk} we allowed you to send media here.")
    dl.sleep(1)
    message.reply_text("♣️ user unmuted.")
    

@bot.on_message(filters.command(['copy']) & filters.chat("status_group_admins"))
def copy(client,message):
    cc = message.reply_to_message
    bot.send_chat_action(chat_id=chat_id, action="typing")
    cc.copy(chat_id)
    dl.sleep(1)
    message.reply_text("😁 done")

@bot.on_message(filters.chat("status_group_admins") & filters.regex(ban_rejex))
def unmute(client,message):
    user_id = message.reply_to_message.text.split()[0]
    user_name = message.reply_to_message.text.split()[7]
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    bot.kick_chat_member(chat_id, user_id)
    bot.send_chat_action(chat_id=chat_id, action="typing")
    bot.send_message(chat_id=chat_id, text=f"Banned {rpk}.")
    dl.sleep(1)
    message.reply_text("♣️ user Banned.")
    
