from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.core.bot import 1PAC
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.core.dir import dirr
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.core.git import git
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.core.userbot import Userbot
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ONEPAC()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
