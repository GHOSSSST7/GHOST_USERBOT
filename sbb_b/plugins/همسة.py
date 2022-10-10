from telethon import events
import random, re
from sbb_b.utils import admin_cmd
import asyncio 

@sbb_b.on(
    admin_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    jepiqb = event.pattern_match.group(1)
    rrrd7 = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(rrrd7, jepiqb) 
    await tap[0].click(event.chat_id)
    await event.delete()