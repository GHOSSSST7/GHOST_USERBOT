import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from .. import CMD_HELP, LOGS
from ..utils import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="userinfo(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        return await edit_or_reply(event, f"`{str(error_i_a)}`")
    user_id = replied_user.user.id
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    # inspired by https://telegram.dog/afsaI181
    common_chats = replied_user.common_chats_count
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except:
        dc_id = "Couldn't fetch DC ID!"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**AɴᴛɪSᴘᴀᴍ (CAS) Bᴀɴɴᴇᴅ**: `Tʀᴜᴇ`"
        else:
            cas = "**AɴᴛɪSᴘᴀᴍ (CAS) Bᴀɴɴᴇᴅ**: `Fᴀʟsᴇ`"
    else:
        cas = "**AɴᴛɪSᴘᴀᴍ (CAS) Bᴀɴɴᴇᴅ**: `Cᴏᴜʟᴅɴ'ᴛ Fᴇᴛᴄʜ`"
    caption = """**Exᴛʀᴀᴄᴛᴇᴅ Usᴇʀ Iɴғᴏ Bʏ UʟᴛʀᴀX**\n
   **┏━━━━━━━━━━━━━━━━━━━━━**
   **┣ Lɪɴᴋ Tᴏ Pʀᴏғɪʟᴇ**: [{}](tg://user?id={})
   **┣ Usᴇʀ Iᴅ**: `{}`
   **┣ Gʀᴏᴜᴘs Iɴ Cᴏᴍᴍᴏɴ**: `{}`
   **┣ Dᴄ Iᴅ**: `{}`
   **┣ Rᴇsᴛʀɪᴄᴛᴇᴅ**: `{}`
   **┣** {}
   **┣** {}
   **┗━━━━━━━━━━━━━━━━━━━━━**
""".format(
        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.user.restricted,
        sw,
        cas,
    )
    await event.edit(caption)


async def get_full_user(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        try:
            try:
                input_str = int(input_str)
            except:
                pass
            user_object = await event.client.get_entity(input_str)
            user_id = user_object.id
            replied_user = await event.client(GetFullUserRequest(user_id))
            return replied_user, None
        except Exception as e:
            return None, e
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.sender_id
                    or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
        return replied_user, None
    if event.is_private:
        try:
            user_id = event.chat_id
            replied_user = await event.client(GetFullUserRequest(user_id))
            return replied_user, None
        except Exception as e:
            return None, e
    return None, "No input is found"

@borg.on(admin_cmd(pattern="link(?: |$)(.*)"))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})")


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
