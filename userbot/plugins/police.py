import html
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot.utils import admin_cmd
from telethon import events
import asyncio
from platform import uname
from userbot import ALIVE_NAME

@borg.on(admin_cmd(pattern=r"police"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    animation_chars = [
        
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",    
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "**🙆🏻‍♂️The Police Is Arrived All Of You With Your Hands Up 🙆🏻‍♂️**"
 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
