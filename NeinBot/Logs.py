import discord
from discord.ext import commands


client = commands.Bot(command_prefix="/")


async def log(ctx, success: bool = True):
    logchannel = discord.utils.get(ctx.guild.channels, name="log")
    author = ctx.author
    channel = ctx.channel.mention
    msg = ctx.message.content
    if success:
        await logchannel.send("%s hat in %s %s benutzt" % (str(author), str(channel), str(msg)))
    else:
        await logchannel.send("%s hat in %s versucht %s zu benutzen." % (str(author), str(channel), str(msg)))
