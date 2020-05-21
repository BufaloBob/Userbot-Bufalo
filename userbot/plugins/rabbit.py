"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.50

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "rabbit":

        await event.edit(input_str)

        animation_chars = [
        

            "Command Created By The_Killer_Bob",
            "(\(\\n(  -.-)\n°_(")(")",
            "(\(\\n(  -.-)\n°_(")(")",
            "💞💖💝❤️YHEA THIS RABBIT LOVE YOU💖💝❤️💗"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
