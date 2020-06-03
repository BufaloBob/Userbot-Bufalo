"""Emoji

Available Commands:

.Bruh

built by @r4v4n4 , isse bhi loot lo betichod"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd




@borg.on(admin_cmd(pattern=r"Bruh"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 24)

    #input_str = event.pattern_match.group(1)

  #  if input_str == "Bruh":

    await event.edit("Bruh")

    animation_chars = [
        
            " ____             _     \n| __ ) _ __ _   _| |__  \n|  _ \| '__| | | | '_ \ \n| |_) | |  | |_| | | | |\n| |_) | |  | |_| | | | |"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 24])
