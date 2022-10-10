import random

from razan.strings.fun import *
from sbb_b import sbb_b
from sbb_b.core.managers import edit_or_reply
from sbb_b.helpers import get_user_from_event

from . import *


@sbb_b.ar_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه بقلبك ♥️ "
    )


@sbb_b.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجك روحوا خلفوا 🤤😂",
    )


@sbb_b.ar_cmd(pattern="رفع علق(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفـعه علق  😂"
    )


@sbb_b.ar_cmd(pattern="رفع مراتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـها مـࢪاتك الف مبروك 😹🤤",
    )


@sbb_b.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه كلب خليه يقعد يهوهو 😂🐶",
    )


@sbb_b.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@sbb_b.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
        if user.id == 1824749880:
        return await edit_or_reply(mention, f"اهين مين يا مره دا المطور 😏")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@sbb_b.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza}"
    )


@sbb_b.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1824749880:
        return await edit_or_reply(mention, f"دا ارجل من الجابوك دا")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الانوثة لـ [{muh}](tg://user?id={user.id})هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@sbb_b.ar_cmd(pattern="رفع جاموسة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـها جاموسة\nوهى جاموسه اصلا 😂🦬"
    )


@sbb_b.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه قرد هاتوله موزة 🐒🍌",
    )


@sbb_b.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@sbb_b.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@sbb_b.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1824749880:
        return await edit_or_reply(mention, f"ارجل من بلدك دا 😂")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه حيوان 🐏"
    )


@sbb_b.ar_cmd(pattern="رفع بشخة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه طفل بشخه 😂\nهاتوله بامبرز بسرعه 😂💔"
    )


@sbb_b.ar_cmd(pattern="رفع معرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه معرص 😒"
    )


@sbb_b.on(admin_cmd(pattern="زاوج(?:\s|$)([\s\S]*)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    await edit_or_reply(mention, f"**نتجوز وماتباوع على غيري 🥺💞 ܰ**")


@sbb_b.on(admin_cmd(pattern="طلاق(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    await edit_or_reply(mention, f"**انتى طالق بالعشرة 😹😭💕 ܰ**")
