import discord
from discord.ext import commands
import re

class MessageManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.message):
        if msg.author != self.bot.user and not msg.author.bot:
            if "gta" in msg.content.lower():
                await msg.channel.send("Nö")

            elif "brokkoli" in msg.content.lower():
                await msg.delete()

            elif "hurensohn" in msg.content.lower():
                await msg.channel.send("Nein DU!")

            elif msg.content.lower().startswith('ich bin'):
                name = msg.content.split()[2:]
                name = [x for x in name][0]
                await msg.channel.send("Hallo %s, Ich bin NeinBot." % name)
            
            #match .__. or .\_\_.
            if re.match(r"(^\._+\.$)|(^\.(\\_)+\.$)", msg.content):
                await msg.channel.send(msg.content)
