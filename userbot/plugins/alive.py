"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "unknown"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**🎲 __THE_KILLER_BOB USERBOT STATUS__ 🎲**\n\n"
                     "⭐️Tetethon Version: 7.0.1\n\n⭐️Python Version: 3.8.0\n\n🥶**SUPPORT & UPDATE: I CAN SUPPORT YOU **\n\n"
                     "🥶**Custom By:** [The_Killer_Bob](tg://user?id=) **\n\n"
                     "⭐️**CPU:** Ok \n\n🎲 **__USER DATA__** 🎲\n\n"
                     f"🥶 **USER:** __{DEFAULTUSER}__\n\n"
                     "🥶[SHOPPY](https://shoppy.gg/@The_Killer_Bob)")
