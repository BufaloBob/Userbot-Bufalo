import os
if 1 == 1:
    try:
        from userbot.plugins.sql_helper import SESSION, BASE
    except ImportError:
        raise Exception("Hello!")

    from sqlalchemy import Column, String, UnicodeText


    class Chats(BASE):
        __tablename__ = "chats"
        sender = Column(String(14), primary_key=True)

        def __init__(self, chat):
            self.sender = str(chat)


    Chats.__table__.create(checkfirst=True)


    def all_chat():
        try:
            return SESSION.query(Chat).all()
        except:
            return None
        finally:
            SESSION.close()


    def is_chat(chat_id):
        try:
            return True if SESSION.query(Chat).get(chat_id) else None
        except:
            return False
        finally:
            SESSION.close()


    def add_chat(chat_id):
        adder = Chat(str(chat_id))
        SESSION.add(adder)
        SESSION.commit()


    def del_chat(chat_id):
        rem = SESSION.query(Chat).get((str(chat_id)))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()

    @command(pattern=r"^.msg ?(.*)")
    async def msg(event):
    	chats = all_chat()
    	text = event.pattern_match.group(1)
    	chats = chats if chats is not None else []
    	counter = 0
    	for chat in chats:
    		await bot.send_message((chat if not chat.isdigit() else int(chat)), text)
    		counter += 1
    	await event.edit(f"Sent message to {counter} chats")
    
    @command(pattern=r"^.addchat ?(.*)")
    async def addchat(event):
        chat = event.chat_id if event.pattern_match.group(1) == "" else event.pattern_match.group(1)
        if is_chat(chat):
            await event.edit("This chat is already added.")
            return
        add_chat(chat)
        await event.edit(f"{chat} was successfully added.")

    @command(pattern=r"^.removechat ?(.*)")
    async def removechat(event):
        chat = event.chat_id if event.pattern_match.group(1) == "" else event.pattern_match.group(1)
        if not is_chat(chat):
            await event.edit("This chat was not added.")
            return
        del_chat(chat)
        await event.edit(f"{chat} was successfully removed.")
    
    @command(pattern=r"^.chatlist")
    async def chatlist(event):
        chats = all_chat()
        chats = chats if chats is not None else []
        chatlist = "\n".join([f"`{x}` - " + (await bot.get_entity(x)).first_name for x in chats])
        await event.edit(f"You have {len(chats)} chats listed for message sending:\n{chatlist}")