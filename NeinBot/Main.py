from MusikBot import Musikbot
from MessageManager import MessageManager
from Commands import Commands
import discord
from discord.ext import commands
from Listeners import Listeners
from online import keep_alive
import os
from ReactionRole import ReactionRole
from Schedules import Scheduler



intents = discord.Intents.all()
intents.members = True
prefixes = [".", "!", "/", ",", ";", "?", "NeinBot ", "^", ":"]

bot = commands.Bot(command_prefix=prefixes, intents=intents)
bot.remove_command("help")


bot.add_cog(Commands(bot))
bot.add_cog(Listeners(bot))
bot.add_cog(MessageManager(bot))
bot.add_cog(ReactionRole(bot))
bot.add_cog(Musikbot(bot))
bot.add_cog(Scheduler(bot))


keep_alive()
bot.run(os.environ['token'])
