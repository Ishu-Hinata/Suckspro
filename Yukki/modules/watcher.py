import re
import time
import asyncio
import random 

from pyrogram import filters
from pyrogram.types import Message

from Yukki import app, botid, botname, botusername
from Yukki.database import add_served_chat
from Yukki.helpers import get_readable_time, put_cleanmode

chat_watcher_group = 1
welcome_group = 2

MEDIA = [
    "https://telegra.ph/file/32493eb609fa847b43b8c.mp4",
    "https://telegra.ph/file/547add5141d7f5c2b00c7.mp4",
    "https://telegra.ph/file/344f4bec8e26def7e723a.mp4",
]

TEXT = [
    "hiii",
    "yooo",
    "Test",
]



@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    media = random.choice(MEDIA)
    notes = random.choice(TEXT)
    await message.reply_video(video=MEDIA, caption=TEXT)





@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id == botid:
                send =  await message.reply_text(
                    f"Thanks for having me in {message.chat.title}\n\n{botname} is alive."
                )
                await put_cleanmode(message.chat.id, send.message_id)
        except:
            return

