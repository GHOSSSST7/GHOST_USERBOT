import heroku3
import urllib3
from urlextract import URLExtract
from validators.url import url
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
extractor = URLExtract()

from sbb_b import sbb_b

from ..Config import Config
from ..core.managers import edit_delete
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

vlist = [
    "ALIVE_PIC",
    "ALIVE_PICC",
    "TI_FN",
    "ALIVE_TELETHONIQ",
    "ALIVE_TEXT",
    "ALLOW_NSFW",
    "HELP_EMOJI",
    "HELP_TEXT",
    "IALIVE_PIC",
    "PM_PIC",
    "PM_TEXT",
    "PM_BLOCK",
    "MAX_FLOOD_IN_PMS",
    "START_TEXT",
    "NO_OF_ROWS_IN_HELP",
    "NO_OF_COLUMNS_IN_HELP",
    "CUSTOM_STICKER_PACKNAME",
    "AUTO_PIC",
    "DEFAULT_BIO",
    "FONTS_AUTO",
    "OR_ALIVE",
    "OR_UPDATE",
    "OR_ORDERS",
    "OR_MUTE",
    "OR_TFLASH",
    "OR_UNMUTE",
    "OR_ADD",
    "OR_ALLGROUB",
    "OR_UNBAND",
    "OR_BAND",
    "OR_UNADMINRAISE",
    "OR_ADMINRAISE",
    "OR_LINK",
    "OR_REMOVEBAN",
    "OR_LEFT",
    "OR_AUTOBIO",
    "OR_NAMEAUTO",
    "OR_ID",
    "OR_UNPLAG",
    "OR_PLAG",
    "OR_FOTOAUTO",
    "OR_MUQT",
    "OR_FOTOSECRET",
    "OR_ALLPRIVATE",
    "MODSLEEP",
    "OR_SLEEP",
    "OR_UNMUQT",
]
oldvars = {
    "PM_PIC": "pmpermit_pic",
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}


@sbb_b.ar_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)")
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(
            event,
            f"**♛︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}",
            time=60,
        )
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"♛")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(
                    event,
                    f"قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك",
                )
            if not vinfo:
                return await edit_delete(event, f"يـجب وضع القـيمـة الصحـيحه")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "يـجـب وضـع رابـط صحـيح")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID, f"**♛︙ اضف فـار\n♛︙ {vname} الفارالذي تم تعديله :"
                )
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(
                event,
                f"📑 القيـمة لـ {vname} \n♛︙   تـم تغييـرها لـ : `{vinfo}`",
                time=20,
            )
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(
                event, f"📑 قيـمة الـ {vname}** \n   هى  `{var_data}`", time=20
            )
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**♛︙ حـذف فـار **\n**♛︙ {vname}** تـم حـذف هـذا الفـار **",
                )
            await edit_delete(
                event,
                f"**♛︙  📑 قيـمة الـ {vname}** \n**♛︙   تم حذفها ووضع القيمه الاصلية لها**",
                time=20,
            )
    else:
        await edit_delete(
            event,
            f"**♛︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",
            time=60,
        )
