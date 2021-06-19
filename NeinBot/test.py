from discord.ext import commands
from Log import log

def new_command(cmd):
    func = cmd()
    @commands.command()
    async def eval(cmd):
        func()
    
return cmd