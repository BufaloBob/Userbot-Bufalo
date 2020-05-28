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
            help_string = """𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙃𝙚𝙡𝙥𝙚𝙧.. 𝙄'𝙢 𝙃𝙚𝙡𝙥𝙞𝙣𝙜 𝙔𝙤𝙪 \n
'𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐇𝐞𝐥𝐩𝐞𝐫 𝐭𝐨 𝐫𝐞𝐯𝐞𝐚𝐥 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬'\n__𝘿𝙤 .𝙝𝙚𝙡𝙥 𝙥𝙡𝙪𝙜𝙞𝙣_𝙣𝙖𝙢𝙚 𝙛𝙤𝙧 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨, 𝙞𝙣 𝙘𝙖𝙨𝙚 𝙥𝙤𝙥𝙪𝙥 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙖𝙥𝙥𝙚𝙖𝙧."""
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
