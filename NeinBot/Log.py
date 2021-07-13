import discord
from discord.ext import commands


client = commands.Bot(command_prefix=".")


async def log(ctx):
    logchannel = discord.utils.get(ctx.guild.channels, name="log")
    author = ctx.author
    channel = ctx.channel.mention
    msg = ctx.message.content
    await logchannel.send("%s hat in %s %s benutzt" % (str(author), str(channel), str(msg)))
    
