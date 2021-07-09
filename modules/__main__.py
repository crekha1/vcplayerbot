import requests
from pyrogram import Client as Bot

from utils.config import API_HASH
from utils.config import API_ID
from utils.config import BG_IMAGE
from utils.config import BOT_TOKEN
from utils.services.callsmusic import run

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
