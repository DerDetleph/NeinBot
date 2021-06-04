import discord
from discord.ext import commands
from discord.utils import get


class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        msgid = payload.message_id
        if msgid == 803242125219201034:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            if payload.emoji.name == "__":
                role = discord.utils.get(guild.roles, name=".__.")
                member = get(guild.members, id=payload.user_id)
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        msgid = payload.message_id
        if msgid == 803242125219201034:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            if payload.emoji.name == "__":
                role = discord.utils.get(guild.roles, name=".__.")
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            if role is not None:
                await self.bot.wait_until_ready()
                member = get(guild.members, id=payload.user_id)
                await member.remove_roles(role)
