from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from datetime import datetime

timeset = datetime.now()

@command(pattern=r"^.online")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="✅ 𝑂𝑁𝐿𝐼𝑁𝐸"))
        await event.edit("Now You Are ✅ 𝑂𝑁𝐿𝐼𝑁𝐸. Created By @The_Killer_Bob")

@command(pattern=r"^.offline")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸"))
        await event.edit("Now You Are 🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸. Created By @The_Killer_Bob")
        timeset = datetime.now()
        
@command(pattern=r"^.Studying")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="📚Studying📖"))
        await event.edit("Now You Are 📚Studying📖. Created By @The_Killer_Bob")
        timeset = datetime.now()

@command(pattern=r"^.standby ?(.*)")
async def name(event):
    style = "online"
    standby = event.pattern_match.group(1)
    if style == "online":
        await bot(UpdateProfileRequest(last_name=standby))
        await event.edit("Created By @The_Killer_Bob Now You Are " + standby)

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    if not event.is_private:
        if not event.mentioned:
            return
    me = await bot.get_me()
    if me.last_name == "🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸":
        now = datetime.now()
        time = str((now - timeset))[:-6]
        await event.reply(f"""⚠️ 𝑨𝑻 𝑻𝑯𝑬 𝑴𝑶𝑴𝑬𝑵𝑻 𝑰'𝑴 𝑶𝑭𝑭𝑳𝑰𝑵𝑬.
𝑺𝑶 𝑷𝑳𝑬𝑨𝑺𝑬 𝑫𝑶𝑵'𝑻 𝑺𝑷𝑨𝑴 𝑰𝑵 𝑴𝒀 𝑪𝑯𝑨𝑻, 𝑻𝑯𝑨𝑵𝑲𝑺 🔥 
𝑰'𝑳𝑳 𝑨𝑵𝑺𝑾𝑬𝑹 𝑨𝑺 𝑺𝑶𝑶𝑵 𝑨𝑺 𝑷𝑶𝑺𝑰𝑩𝑳𝑬! 
☀️ 𝑨𝑭𝑲 𝑭𝑶𝑹 ~ {time}""")

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    if not event.is_private:
        if not event.mentioned:
            return
    me = await bot.get_me()
    if me.last_name == "📚Studying📖":
        now = datetime.now()
        time = str((now - timeset))[:-6]
        await event.reply(f"""𝑨𝑻 𝑻𝑯𝑬 𝑴𝑶𝑴𝑬𝑵𝑻 𝑰'𝑴 𝑶𝑭𝑭𝑳𝑰𝑵𝑬.
𝑺𝑶 𝑷𝑳𝑬𝑨𝑺𝑬 𝑫𝑶𝑵'𝑻 𝑺𝑷𝑨𝑴 𝑰𝑵 𝑴𝒀 𝑪𝑯𝑨𝑻, 𝑻𝑯𝑨𝑵𝑲𝑺 🔥 
𝑰'𝑳𝑳 𝑨𝑵𝑺𝑾𝑬𝑹 𝑨𝑺 𝑺𝑶𝑶𝑵 𝑨𝑺 𝑷𝑶𝑺𝑰𝑩𝑳𝑬!""")
