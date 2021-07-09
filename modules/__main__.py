import requests
from pyrogram import Client as Bot

from env.config import API_HASH
from env.config import API_ID
from env.config import BG_IMAGE
from env.config import BOT_TOKEN
from env.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=".modules"),
)

bot.start()
run()
