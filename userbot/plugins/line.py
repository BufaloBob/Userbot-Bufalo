from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from datetime import datetime

timeset = datetime.now()

@command(pattern=r"^.online")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="✅ 𝑂𝑁𝐿𝐼𝑁𝐸"))
        await event.edit("✅ 𝑂𝑁𝐿𝐼𝑁𝐸 right now.")

@command(pattern=r"^.offline")
async def name(event):
    style = "online"
    if style == "online":
        await bot(UpdateProfileRequest(last_name="🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸"))
        await event.edit("🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸 right now.")
        timeset = datetime.now()

@command(pattern=r"^.standby ?(.*)")
async def name(event):
    style = "online"
    standby = event.pattern_match.group(1)
    if style == "online":
        await bot(UpdateProfileRequest(last_name=standby))
        await event.edit(standby + " right now.")

@bot.on(events.NewMessage(incoming=True))
async def alert(event):
    if not event.is_private:
        if not event.mentioned:
            return
    me = await bot.get_me()
    if me.last_name == "🚫 𝑂𝐹𝐹𝐿𝐼𝑁𝐸":
        now = datetime.now()
        time = str((now - timeset))[:-6]
        await event.reply(f"""⚠️ 𝐀𝐓 𝐓𝐇𝐄 𝐌𝐎𝐌𝐄𝐍𝐓 𝐈'𝐌 𝐎𝐅𝐅𝐋𝐈𝐍𝐄.
𝐒𝐎 𝐏𝐋𝐄𝐀𝐒𝐄 𝐃𝐎𝐍'𝐓 𝐒𝐏𝐀𝐌 𝐈𝐍 𝐌𝐘 𝐂𝐇𝐀𝐓, 𝐓𝐇𝐀𝐍𝐊𝐒 🔥 
I'LL ANSWER AS SOON AS POSIBLE! 
☀️ OFFLINE FOR ~ {time}""")
