import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾 import LOGGER, app, userbot
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.core.call import ONEPAC
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.misc import sudo
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.plugins import ALL_MODULES
from 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        pass
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.plugins" + all_module)
    LOGGER("𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await 1PAC.start()
    try
        await 1PAC.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n 1pac 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        pass
    except:
        pass
    await 1pac.decorators()
    LOGGER("𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 ONEPAC☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾").info("𝗦𝗧𝗢𝗣 𝘿𝙊𝙍𝘼𝙀𝙈𝙊𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
