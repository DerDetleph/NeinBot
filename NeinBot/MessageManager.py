import discord
from discord.ext import commands


class MessageManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.message):
        if "gta" in msg.content.lower():
            await msg.channel.send("Nö")

        elif "brokkoli" in msg.content.lower():
            await msg.delete()

        if "hurensohn" in msg.content.lower():
            await msg.channel.send("Nein DU!")

        elif msg.content.lower().startswith('ich bin'):
            name = msg.content.split()[2:]
            name = [x for x in name][0]
            await msg.channel.send("Hallo %s, Ich bin NeinBot." % name)
