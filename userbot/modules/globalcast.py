from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot import CMD_HELP, bot


@bot.on(geezbot_cmd(outgoing=True, pattern="gcast(?: |$)(.*)"))
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")


@bot.on(geezbot_cmd(outgoing=True, pattern="gucast(?: |$)(.*)"))
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan beberapa teks untuk Siaran Global`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "broadcast": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{geez}gcast`\
         \n↳ : Mengirim Pesan Group Secara Global.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{geez}gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global"
    }
)
