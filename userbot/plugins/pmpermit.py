import asyncio
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, LESS_SPAMMY
from userbot.utils import admin_cmd

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
CACHE = {}


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No name set yet nibba, check pinned message in** @TheKillerBob"
USER_BOT_WARN_ZERO = "𝖸𝗈𝗎 𝖶𝖾𝗋𝖾 𝖲𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝖬𝗒 𝖡𝗈𝗌𝗌'𝗌 𝖨𝗇𝖻𝗈𝗑, 𝖧𝖾𝗇𝖼𝖾𝖿𝗈𝗋𝗍𝗁 𝖸𝗈𝗎𝗋 𝗋𝖾𝗍𝖺𝗋𝖽𝖾𝖽 𝖠𝗌𝗌 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖡𝗅𝗈𝖼𝗄𝖾𝖽 𝖡𝗒 𝖬𝗒 𝖡𝗈𝗌𝗌'𝗌 𝖴𝗌𝖾𝗋𝖻𝗈𝗍."
USER_BOT_NO_WARN = ("𝑺𝑻𝑶𝑷 𝑺𝑷𝑨𝑴𝑴𝑰𝑵𝑮 𝑶𝑹 𝑰'𝑳𝑳 𝑩𝑳𝑶𝑪𝑲 𝒀𝑶𝑼\n\n"
                    "__ 𝐻𝑒𝑙𝑙𝑜, 𝑡ℎ𝑖𝑠 𝑖𝑠 𝐾𝑖𝑙𝑙𝑒𝑟'𝑠 𝑆𝑒𝑐𝑢𝑟𝑖𝑡𝑦 𝑆𝑒𝑟𝑣𝑖𝑐𝑒.\n 𝑌𝑜𝑢'𝑟𝑒 𝑇𝑟𝑦𝑖𝑛𝑔 𝑇𝑜 𝐶𝑜𝑛𝑡𝑎𝑐𝑡 𝑀𝑦 𝐵𝑜𝑠𝑠.__"
                    f"{DEFAULTUSER}'s` inbox.\n\n"
                    "**Send /start so that we can decide why you're here.**")


if Var.PRIVATE_GROUP_ID is not None:
    @command(pattern="^.approve ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("You Approved [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()


    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "__𝑇ℎ𝑖𝑠 𝑁𝑜𝑜𝑏 𝑊𝑎𝑠 𝐴𝑝𝑝𝑟𝑜𝑣𝑒𝑑 𝐵𝑒𝑐𝑎𝑢𝑠𝑒 𝑌𝑜𝑢 𝑊𝑟𝑜𝑡𝑒 𝑇𝑜 𝐻𝑖𝑚__"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()


    @command(pattern="^.block ?(.*)")
    async def block_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("𝖮𝖪𝖤𝖸 𝖡𝖫𝖮𝖢𝖪𝖨𝖭𝖦... \n\n𝖥𝗎𝖼𝗄 𝖮𝖿𝖿 𝖡𝗂𝗍𝖼𝗁, 𝖭𝗈𝗐 𝖸𝗈𝗎 𝖢𝖺𝗇'𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖬𝖾..[{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))


    @command(pattern="^.listapproved")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        if event.from_id in CACHE:
            sender = CACHE[event.from_id]
        else:
            sender = await bot.get_entity(event.from_id)
            CACHE[event.from_id] = sender

        if chat_id == bot.uid:

            # don't log Saved Messages

            return


        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return
          
        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_P_M_s:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except:
                return
        r = await event.reply(USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
