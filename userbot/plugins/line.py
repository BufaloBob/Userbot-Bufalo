from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from datetime import datetime

timeset = datetime.now().time()

@command(pattern=r"^.online")
async def name(event):
    style = "online"
    if style == "online":
        await client(UpdateProfileRequest(last_name="✅ 𝑂𝑁𝐿𝐼𝑁𝐸"))
        await event.edit("✅ 𝑂𝑁𝐿𝐼𝑁𝐸 right now.")

@command(pattern=r"^.online")
async def name(event):
    style = "online"
    if style == "online":
        await client(UpdateProfileRequest(last_name="🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸"))
        await event.edit("🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸 right now.")

@command(pattern=r"^.standby ?(.*)")
async def name(event):
    style = "online"
    standby = event.pattern_match.group(1)
    if style == "online":
        await client(UpdateProfileRequest(last_name=standby))
        await event.edit(standby + " right now.")

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    me = await bot.get_me()
    if me.last_name == "🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸":
        now = datetime.now().time()
        time = str(now - timeset)[:-6]
        await event.reply(f"""⚠️ AT THE MOMENT I'M OFFLINE.
SO PLEASE DON'T SPAM IN MY CHAT, THANKS 🔥 
I'LL ANSWER AS SOON AS POSIBLE! 
☀️ AFK FOR ~ {time}""")