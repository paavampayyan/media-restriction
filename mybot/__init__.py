from pyrogram import Client
from config import API_HASH, API_ID, BOT_TOKEN


bot = Client("mybot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)