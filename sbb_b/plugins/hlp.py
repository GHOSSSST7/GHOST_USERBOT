from telethon import functions

from sbb_b import sbb_b

from ..Config import Config
from ..core import CMD_INFO, PLG_INFO
from ..core.cmdinfo import cmdinfo, cmdlist, grpinfo, plugininfo
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

cmdprefix = Config.COMMAND_HAND_LER


plugin_category = "tools"


@sbb_b.ar_cmd(
    pattern="help ?(-c|-p|-t)? ?([\s\S]*)?",
    command=("help", plugin_category),
    info={
        "header": "To get guide for catuserbot.",
        "description": "To get information or guide for the command or plugin",
        "note": "if command name and plugin name is same then you get guide for plugin. So by using this flag you get command guide",
        "flags": {
            "c": "To get info of command.",
            "p": "To get info of plugin.",
            "t": "To get all plugins in text format.",
        },
        "usage": [
            "{tr}help (plugin/command name)",
            "{tr}help -c (command name)",
        ],
        "examples": ["{tr}help help", "{tr}help -c help"],
    },
)
async def _(event):
    "To get guide for catuserbot."
    flag = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if flag and flag == "-c" and input_str:
        outstr = await cmdinfo(input_str, event)
        if outstr is None:
            return
    elif input_str:
        outstr = await plugininfo(input_str, event, flag)
        if outstr is None:
            return
    elif flag == "-t":
        outstr = await grpinfo()
    else:
        results = await event.client.inline_query(Config.TG_BOT_USERNAME, "help")
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
        return
    await edit_or_reply(event, outstr)
