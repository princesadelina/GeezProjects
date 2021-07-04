import os

from telegraph import Telegraph
from telegraph import upload_file as uf


# Telegraph Things
telegraph = Telegraph()
try:
    telegraph.create_account(short_name=OWNER_NAME)

except BaseException:
    telegraph.create_account(short_name="Geez")

_copied_msg = {}


@bot.on(geezbot_cmd(outgoing=True, pattern="tg"))
async def telegraphcmd(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        getmsg = await event.get_reply_message()
        if getmsg.photo or getmsg.video or getmsg.gif:
            getit = await bot.download_media(getmsg)
            try:
                variable = uf(getit)
                os.remove(getit)
                nn = "https://telegra.ph" + variable[0]
                amsg = f"Uploaded to [Telegraph]({nn}) !"
            except Exception as e:
                amsg = f"Error - {e}"
            await eor(event, amsg)
        elif "pic" in mediainfo(getmsg.media):
            getit = await bot.download_media(getmsg)
            try:
                variable = uf(getit)
                os.remove(getit)
                nn = "https://telegra.ph" + variable[0]
                amsg = f"Uploaded to [Telegraph]({nn}) !"
            except Exception as e:
                amsg = f"Error - {e}"
            await eor(event, amsg)
        elif getmsg.document:
            getit = await bot.download_media(getmsg)
            ab = open(getit)
            cd = ab.read()
            ab.close()
            if input_str:
                tcom = input_str
            else:
                tcom = "Geez"
            makeit = telegraph.create_page(title=tcom, content=[f"{cd}"])
            war = makeit["url"]
            os.remove(getit)
            await event.edit(f"Pasted to Telegraph : [Telegraph]({war})")
        elif getmsg.text:
            if input_str:
                tcom = input_str
            else:
                tcom = "Geez"
            makeit = telegraph.create_page(
                title=tcom, content=[f"{getmsg.text}"])
            war = makeit["url"]
            await event.edit(f"Pasted to Telegraph : [Telegraph]({war})")
        else:
            await event.edit("Reply to a Media or Text !")
    else:
        await event.edit("Reply to a Message !")


CMD_HELP.update({"telegraph": f">`{geez}tg`"
                 "\nUsage: Upload (text) or (media) on Telegraph."})
