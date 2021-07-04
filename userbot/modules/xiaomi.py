# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez


@bot.on(geezbot_cmd(outgoing=True, pattern="firmware(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = "firmware"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            link1 = await conv.send_message(f'/{firmware} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="fastboot(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            link1 = await conv.send_message(f'/{fboot} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBoot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="recovery(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = "recovery"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            link1 = await conv.send_message(f'/{recovery} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="pb(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = "pb"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            link1 = await conv.send_message(f'/{pitch} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="of(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = "of"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            link1 = await conv.send_message(f'/{ofox} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="eu(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    eu = "eu"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{eu} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="vendor(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = "vendor"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{vendor} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])


@bot.on(geezbot_cmd(outgoing=True, pattern="specs(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = "specs"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{specs} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
            await event.client.delete_messages(conv.chat_id, [response.id, link1.id])

CMD_HELP.update({
    "xiaomi":
    f"For Xiaomeme devices only!\
\n\n`{geez}firmware` (codename)\
     \nUsage : Get lastest Firmware\
\n\n`{geez}pb` (codename)\
     \nUsage : Get latest PitchBlack Recovery\
\n\n`{geez}specs` (codename)\
     \nUsage : Get quick spec information about device\
\n\n`{geez}fastboot` (codename)\
     \nUsage : Get latest fastboot MIUI\
\n\n`{geez}recovery` (codename)\
     \nUsage : Get latest recovery MIUI\
\n\n`{geez}eu` (codename)\
    \nUsage: Get latest xiaomi.eu rom\
\n\n`{geez}vendor` (codename)\
    \nUsage: fetches latest vendor\
\n\n`{geez}of` (codename)\
     \nUsage : Get latest ORangeFox Recovery"})
