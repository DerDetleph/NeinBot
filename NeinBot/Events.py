from discord.ext import commands
import discord


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as %s" % self.bot.user)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(796431059150700594)
        channelid = self.bot.get_channel(796431750657474632).mention
        userid = member.mention
        await channel.send("Hi " + userid + ", bitte lies dir die Regeln in " + channelid + " durch!")
        guild = member.guild
        role = discord.utils.get(guild.roles, name="NeinBitteNicht")
        await member.add_roles(role)
