from telethon import events
import subprocess
import asyncio
import time


@command(pattern="^.cmds", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins:**\n{o}\n\n**TIP:** 𝑰𝒇 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒌𝒏𝒐𝒘 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝒇𝒐𝒓 𝒂 𝒑𝒍𝒖𝒈𝒊𝒏, 𝒅𝒐:- \n .𝒉𝒆𝒍𝒑 <𝒑𝒍𝒖𝒈𝒊𝒏 𝒏𝒂𝒎𝒆>` **𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒕𝒉𝒆 < > 𝒃𝒓𝒂𝒄𝒌𝒆𝒕𝒔.**\n 𝑨𝒍𝒍 𝒑𝒍𝒖𝒈𝒊𝒏𝒔 𝒎𝒊𝒈𝒉𝒕 𝒏𝒐𝒕 𝒘𝒐𝒓𝒌 𝒅𝒊𝒓𝒆𝒄𝒕𝒍𝒚."
    await event.edit(OUTPUT)
