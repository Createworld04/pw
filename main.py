import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import logging
from pyrogram import Client, filters
from subprocess import getstatusoutput
import re
from pyrogram.types import User, Message
import os

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

logger = logging.getLogger()
thumb = os.environ.get("THUMB")
if thumb.startswith("http://") or thumb.startswith("https://"):
    getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
    thumb = "thumb.jpg"


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **physics Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/login** to continue..\n\n")

@bot.on_message(filters.command(["login"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Number or email** in this manner otherwise bot will not respond.\n\nSend like this:-  **mobile no.*"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

        
        
        





        
                
        














bot.run()
