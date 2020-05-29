"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""

import asyncio

from telethon import events

from telethon.tl.types import ChannelParticipantsAdmins

from platform import uname

from userbot import ALIVE_NAME

from userbot.utils import admin_cmd





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"



#@command(outgoing=True, pattern="^.alive$")

@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(alive):

    """ For .alive command, check if the bot is running.  """

    await alive.edit("░█─░█ █▀▀ █── █── █▀▀█ \n░█▀▀█ █▀▀ █── █── █──█ \n░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ \n\nYEEEE FINALLY ! I'm Alive\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n"

                     f"My BOSS`: {DEFAULTUSER}\n"

                     "⭐️Tetethon Version: 7.0.1\n\n⭐️Python Version: 3.8.0\n\n🥶**MORE INFO**\n"
					 
					 "⭐️**CPU:** Ok \n"

                     "Database Status: Databases functioning normally!\n\nAlways with you, my Boss!\n"

                     "[Contact My Boss Now](https://t.me/The_Killer_Bob)")
