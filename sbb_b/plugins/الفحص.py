import random
import time
from datetime import datetime

from telethon import Button, events, version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from sbb_b import StartTime, sbb_b

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@sbb_b.ar_cmd(pattern="فحص$")
async def iq(iqthonevent):
    reply_to_id = await reply_id(iqthonevent)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    iqevent = await edit_or_reply(iqthonevent, "جاري فحص السورس ....")
    end = datetime.now()
    (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or ""
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ""
    IQTHON_IMG = "https://telegra.ph/file/e9c27e7dfb0b1835d23ce.mp4"
    tg_bot = Config.TG_BOT_USERNAME
    me = await iqthonevent.client.get_me()
    me.last_name
    my_mention = f"[{me.last_name}](tg://user?id={me.id})"
    TM = time.strftime("%I:%M")
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or fahs
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        my_mention=my_mention,
        TM=TM,
        tg_bot=tg_bot,
    )
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        PIC = random.choice(CAT)
        try:
            await iqthonevent.client.send_file(
                iqthonevent.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await iqevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(iqevent)
    else:
        await edit_or_reply(iqevent, caption)


fahs = """𝐌𝐄 {mention}.
𝐓𝐈𝐌𝐄 {TM}.
𝐌𝐘 𝐁𝐎𝐓 {tg_bot}.
𝐃𝐕 :  @SA3ED_IT."""
