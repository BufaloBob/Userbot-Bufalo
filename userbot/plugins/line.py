from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from datetime import datetime

timeset = 0

@command(pattern=r"^.(offline|standby (.*)|online)")
async def name(event):
    style = event.pattern_match.group(1)
    standby = event.pattern_match.group(2)
    if style == "offline":
        await client(UpdateProfileRequest(last_name="🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸"))
        await event.edit("🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸 right now.")
        timeset = datetime.now().time()
    elif style == "online":
        await client(UpdateProfileRequest(last_name="✅ 𝑂𝑁𝐿𝐼𝑁𝐸"))
        await event.edit("✅ 𝑂𝑁𝐿𝐼𝑁𝐸 right now.")
    elif style == "standby":
        await client(UpdateProfileRequest(last_name=standby))
        await event.edit(f"{standby} right now.")

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    me = await bot.get_me()
    now = datetime.now().time()
    time = str(now - timeset)[:-6]
    if me.last_name == "🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸":
        await event.reply(f"""⚠️ AT THE MOMENT I'M OFFLINE.
SO PLEASE DON'T SPAM IN MY CHAT, THANKS 🔥 
I'LL ANSWER AS SOON AS POSIBLE! 
☀️ AFK FOR ~ {time}""")