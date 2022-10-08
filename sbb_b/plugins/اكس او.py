import re
import os
from sbb_b import sbb_b
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

IQMOG = re.compile(
    "[" 
    "\U0001F1E0-\U0001F1FF"      "\U0001F300-\U0001F5FF"      "\U0001F600-\U0001F64F"   "\U0001F680-\U0001F6FF"  
    "\U0001F700-\U0001F77F"      "\U0001F780-\U0001F7FF"      "\U0001F800-\U0001F8FF"     "\U0001F900-\U0001F9FF"      "\U0001FA00-\U0001FA6F"  
    "\U0001FA70-\U0001FAFF"      "\U00002702-\U000027B0"      
    "]+")


def iqtfy(inputString: str) -> str:
    return re.sub(IQMOG, "", inputString)


@sbb_b.ar_cmd(pattern="اكس او(?: |$)(.*)")
async def iq(sbb_b):
    kn = sbb_b.pattern_match.group(1)
    if not kn:
        if sbb_b.is_reply:
            (await sbb_b.get_reply_message()).message

            return
    LLL5L = await bot.inline_query("xobot", f"{(iqtfy(kn))}")
    await LLL5L[0].click(
        sbb_b.chat_id,
        reply_to=sbb_b.reply_to_msg_id,
        silent=True if sbb_b.is_reply else False,
        hide_via=True)