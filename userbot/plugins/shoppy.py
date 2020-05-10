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

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "shoppy":

        await event.edit(input_str)

        animation_chars = [
        
            "Command Created By The_Killer_Bob",
            "Buy",
            "Buy From",
            "Buy From My",
            "Buy From My Shoppy",
            "Legit, Cheap, Fast\n Searching Link For The Best Shoppy",
            "✅ Oh The Most Legit And Cheapest Is Just Mine ✅",
            "https://shoppy.gg/@The_Killer_Bob\n💰GO BUY PAYPAL-BTC-ETH💰\n🧨DON'T FORGET TO LEAVE FEEDBACK🧨"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
