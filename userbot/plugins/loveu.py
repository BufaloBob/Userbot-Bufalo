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

    if input_str == "loveu":

        await event.edit(input_str)

        animation_chars = [
        

            "COMMAND CREATED BY @THE_KILLER_BOB",
            "𝒀𝒐𝒖",
            "𝒀𝒐𝒖 𝒂𝒓𝒆",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫 𝒂𝒏𝒅",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫 𝒂𝒏𝒅 𝑩𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫 𝒂𝒏𝒅 𝑩𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍 𝒂𝒔",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫 𝒂𝒏𝒅 𝑩𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍 𝒂𝒔 𝒂",
            "𝒀𝒐𝒖 𝒂𝒓𝒆 𝑺𝒘𝒆𝒆𝒕 𝒂𝒔 𝒂 𝑪𝒉𝒐𝒄𝒐𝒍𝒂𝒕𝒆🍫 𝒂𝒏𝒅 𝑩𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍 𝒂𝒔 𝒂 𝑹𝒐𝒔𝒆🌹",
            "❤️𝑰❤️ ❤️𝑳𝑶𝑽𝑬❤️ ❤️𝒀𝑶𝑼❤️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])
