from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from datetime import datetime

timeset = datetime.now()

@command(pattern=r"^.online")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="✅ 𝑂𝑁𝐿𝐼𝑁𝐸"))
        await event.edit("Now You Are ✅ 𝑂𝑁𝐿𝐼𝑁𝐸.")

@command(pattern=r"^.offline")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸"))
        await event.edit("Now You Are 🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸.")
        timeset = datetime.now()
        
@command(pattern=r"^.Studying")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="📚Studying📖"))
        await event.edit("Now You Are 📚Studying📖.")
        timeset = datetime.now()

@command(pattern=r"^.standby ?(.*)")
async def name(event):
    style = "online"
    standby = event.pattern_match.group(1)
    if style == "online":
        await bot(UpdateProfileRequest(last_name=standby))
        await event.edit("Now You Are" + standby)

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    if not event.is_private:
        if not event.mentioned:
            return
    me = await bot.get_me()
    if me.last_name == "🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸":
        now = datetime.now()
        time = str((now - timeset))[:-6]
        await event.reply(f"""⚠️ AT THE MOMENT I'M OFFLINE.
SO PLEASE DON'T SPAM IN MY CHAT, THANKS 🔥 
I'LL ANSWER AS SOON AS POSIBLE! 
☀️ AFK FOR ~ {time}""")

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    if not event.is_private:
        if not event.mentioned:
            return
    me = await bot.get_me()
    if me.last_name == "📚Studying📖":
        now = datetime.now()
        time = str((now - timeset))[:-6]
        await event.reply(f"""⚠️ AT THE MOMENT I'M STUDYING.
SO PLEASE DON'T SPAM IN MY CHAT, THANKS 🔥 
I'LL ANSWER AS SOON AS POSIBLE!}""")
