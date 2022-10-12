from telethon.tl import functions

from .. import sbb_b
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..utils.tools import create_supergroup


@sbb_b.ar_cmd(pattern="صنع (مجموعة|قناة) ([\s\S]*)")
async def _(event):
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "قناة":
        descript = ""
    else:
        descript = ""
    if type_of_group == "مجموعة عادية":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.TG_BOT_USERNAME],
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event,
                f"تم صنع المجموعه بنجاح ✓\nاسم المجموعه : `{group_name}`\nالرابط : {result.link}"
            )
        except Exception as e:
            await edit_delete(event, f"**Error:**\n{str(e)}")
    elif type_of_group == "قناة":
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=False,
                )
            )
            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event,
                f"تم صنع القناة بنجاح ✓\nاسم القناة : `{group_name}`\nالرابط : {result.link}",
            )
        except Exception as e:
            await edit_delete(event, f"**Error:**\n{e}")
    elif type_of_group == "مجموعة":
        answer = await create_supergroup(
            group_name, event.client, Config.TG_BOT_USERNAME, descript
        )
        if answer[0] != "error":
            await edit_or_reply(
                event,
                f"تم صنع المجموعه بنجاح ✓\nاسم المجموعه : `{group_name}`\nالرابط : {result.link}",
            )
        else:
            await edit_delete(event, f"**خطأ:**\n{answer[1]}")
    else:
        await edit_delete(event, "استخدم الامر بشكل صحيح")