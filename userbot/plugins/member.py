from telethon.tl.functions.channels import InviteToChannelRequest
import os

@command(pattern=r"^.steal ?(.*)?")
async def steal(event):
    await event.edit("Processing...")
    to_channel = os.environ.get("TO_CHANNEL")
    if to_channel is None:
        await event.edit("Please setup your channel in TO_CHANNEL")
        return
    to_channel = to_channel if not to_channel.isdigit() else int(to_channel)
    input_str = event,pattern_match.group(1)
    input_str = "" if input_str is None else input_str
    input_str = int(input_str) if input_str.isdigit() else input_str
    if not input_str:
        input_str = event.chat_id
    async for user in client.iter_participants(input_str, aggressive=True):
        try:
            await client(InviteToChannelRequest(to_channel, [user.id]))
        except:
            continue
    await event.edit("Finish.")