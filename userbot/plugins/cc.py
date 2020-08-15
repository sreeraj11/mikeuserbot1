import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

@borg.on(admin_cmd(pattern="cc ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    reply_text = "hi"
    await event.edit(reply_text) 

