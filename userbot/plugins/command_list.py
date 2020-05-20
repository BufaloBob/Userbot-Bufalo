from userbot import CMD_LIST

@command(pattern="^.help ?(.*)")
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = "𝒀𝒐𝒖 𝒄𝒐𝒏𝒕𝒂𝒄𝒕𝒆𝒅 𝒖𝒃𝒐𝒕 𝒔𝒖𝒑𝒑𝒐𝒓𝒕\n𝑻𝒐 𝒓𝒆𝒗𝒆𝒂𝒍 𝒂𝒍𝒍 𝒕𝒉𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅\n__𝑫𝒐 .𝒉𝒆𝒍𝒑 𝒑𝒍𝒖𝒈𝒊𝒏_𝒏𝒂𝒎𝒆 𝒇𝒐𝒓 𝒄𝒐𝒎𝒎𝒂𝒏𝒅.__"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
