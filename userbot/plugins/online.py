"""Auto Profile Updation Commands
.autoname"""
from telethon import events
import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from uniborg.util import admin_cmd


DEL_TIME_OUT = 70


@borg.on(admin_cmd(pattern="online"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        surname = f"✅ 𝑂𝑁𝐿𝐼𝑁𝐸  "
        logger.info(surname)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=surname
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
    
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Surname"
            # )
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"Auto Surname has been started Master") 
