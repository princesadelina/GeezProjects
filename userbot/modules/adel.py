from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.adel(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Hy**")
    sleep(2)
    await typew.edit("**salken💅🏻**")
    sleep(1)
    await typew.edit("**princess unicorn**")
    sleep(2)
    await typew.edit("**call me princess🦄**")

# Create by myself @localheart





CMD_HELP.update({
    "adel": f"`adel`\
\nUsage: memperkenalkan diri"
})
