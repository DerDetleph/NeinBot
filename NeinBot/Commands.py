import discord
from discord.ext import commands
import asyncio
import random
from Log import log
from test import new_command


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("**.__.**")
        await log(ctx)

    @commands.command()
    async def hilfe(self, ctx):
        await ctx.send("Nutze \".hilfe\" wenn du ein Problem hast!\nUse \".help\" if you have a problem!")
        await log(ctx)

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Use \".help\" if you have a problem!\nNutze \".hilfe\" wenn du ein Problem hast!")
        await log(ctx)

    @commands.command()
    async def ok(self, ctx):
        await ctx.send("||:ok_hand:||")
        await log(ctx)

    @commands.command()
    async def nein(self, ctx):
        await ctx.send("Oh NEIN!!! Das kommt nicht in die Tasche")
        await log(ctx)

    @commands.command()
    async def gtav(self, ctx):
        await ctx.send("||@everyone||\nGTA?")
        await log(ctx)

    @commands.command()
    async def ndo(self, ctx):
        await ctx.send("Nein!\nDoch!\nOh!")
        await log(ctx)

    @commands.command()
    async def purge(self, ctx, arg=None):
        if arg == None:
            arg = 1
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            count = int(arg) + 1
            await ctx.channel.purge(limit=count)
            await log(ctx, arg)
        else:
            await ctx.channel.send("**Du hast nicht die Berechtigung für diese Aktion, du Gigaknecht.**")
            await log(ctx, success=False)

    @commands.command()
    async def dm(self, ctx, user: discord.Member, msg: str):
        if ctx.author.permissions_in(ctx.channel).administrator:
            await user.send(msg)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.channel.send("**Du hast nicht die Berechtigung für diese Aktion, du Gigaknecht.**")

    @commands.command()
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        if ctx.author.permissions_in(ctx.channel).administrator:
            await user.remove_roles(role)
            await ctx.send("**Rolle entfernt.**")
            await log(ctx)
        else:
            await ctx.send("**Du hast nicht die Berechtigung für diese Aktion, du Gigaknecht.**")
            await log(ctx, success=False)

    @commands.command()
    async def addrole(self, ctx, user: discord.Member, role: discord.Role):
        if ctx.author.permissions_in(ctx.channel).administrator:
            await user.add_roles(role)
            await ctx.send("**Rolle hinzugefügt.**")
            await log(ctx)
        else:
            await ctx.send("**Du hast nicht die Berechtigung für diese Aktion, du Gigaknecht.**")
            await log(ctx, success=False)

    @commands.command()
    async def scheisse(self, ctx):
        await Commands.media_cmd(self, ctx, "scheisse")

    @commands.command()
    async def garnix(self, ctx):
        await Commands.media_cmd(self, ctx, "garnix")

    @commands.command()
    async def walfleisch(self, ctx):
        await Commands.media_cmd(self, ctx, "Walfleisch aus Island")

    @commands.command()
    async def damage(self, ctx):
        await Commands.media_cmd(self, ctx, "alotofdamage")

    @commands.command()
    async def ssp(self, ctx, arg: str):
        spielzuege = ["Schere", "Stein", "Papier"]
        spielzug = random.choice(spielzuege)
        antworten_unentschieden = ["Du hast schwach angefangen und trotzdem noch unglaublich stark nachgelassen.",
                                   "Mit einem Unentschieden bin ich nicht zufrieden!",
                                   "Unentschieden, Unzufrieden, Ausgeschieden", "Na hööörmal!",
                                   "Nicht so Frech Kollege Schnürschuh"]

        antworten_sieg = ["Pech gehabt du Bot!", "Man kann ja auch nicht immer gewinnen was?", "Haha du Nup!",
                          "Hätteste mal besser nachgedacht!", "Dummheit tut weh!",
                          "Menschen die glauben alles besser zu wissen, sollten besser wissen, dass sie alles nur glauben!",
                          "Imagine man verliert gegen einen Bot lol", "Schachmatt!", "Ez clapped"]

        antworten_niederlage = ["Schiri! Das war Abseits!", "Das war unfair, Wiederholung!", "Abseits!",
                                "Hab nichts gesehen, du etwa?", "Hör auf zu schummeln! Du machst immer nach mir!",
                                "Och menno"]
        if arg.lower() == spielzug.lower():
            await ctx.send(spielzug + ".")
            await ctx.send("Unentschieden. " + random.choice(antworten_unentschieden))

        elif spielzug.lower() == "schere" and arg.lower() == "papier":
            await ctx.send("Schere.")
            await ctx.send("Schere gewinnt. " + random.choice(antworten_sieg))

        elif spielzug.lower() == "schere" and arg.lower() == "stein":
            await ctx.send("Schere.")
            await ctx.send("Stein gewinnt. " + random.choice(antworten_niederlage))

        elif spielzug.lower() == "stein" and arg.lower() == "schere":
            await ctx.send("Stein.")
            await ctx.send("Stein gewinnt. " + random.choice(antworten_sieg))

        elif spielzug.lower() == "stein" and arg.lower() == "papier":
            await ctx.send("Stein.")
            await ctx.send("Papier gewinnt. " + random.choice(antworten_niederlage))

        elif spielzug.lower() == "papier" and arg.lower() == "schere":
            await ctx.send("Papier.")
            await ctx.send("Schere gewinnt. " + random.choice(antworten_niederlage))

        elif spielzug.lower() == "papier" and arg.lower() == "stein":
            await ctx.send("Papier.")
            await ctx.send("Papier gewinnt. " + random.choice(antworten_sieg))
        await log(ctx)

    @commands.command()
    async def rr(self, ctx):
        rr_results = ["Leben", "Leben", "Leben", "Leben", "Leben", "Tod"]
        await ctx.send(random.choice(rr_results))
        await log(ctx)

    @commands.command()
    async def coinflip(self, ctx):
        coin_results = ["Kopf", "Zahl"]
        await ctx.send(random.choice(coin_results))
        await log(ctx)

    @commands.command()
    async def oracle(self, ctx):
        oracle_results = ["Ja", "Nein"]
        await ctx.send(random.choice(oracle_results))
        await log(ctx)

    @commands.command()
    async def lol(self, ctx):
        await ctx.send("lolololol")
        await log(ctx)

    @staticmethod
    async def media_cmd(self, ctx, media):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio("NeinBot/media/%s.mp3" % media))
            while voice.is_playing():
                await asyncio.sleep(1)
            await asyncio.sleep(2)
            await voice.disconnect()
        except Exception as e:
            print(e)
            await ctx.send("**Noob.**")
        finally:
            await log(ctx)

    @commands.command()
    async def msgCount(self, ctx):
        channels = self.bot.get_all_channels()
        sum = 0
        for channel in channels:
            if isinstance(channel, discord.TextChannel):
                history = await channel.history(limit = None).flatten()
                sum += len(history)
        await ctx.send(sum)

    @commands.command()
    async def nick(self, ctx, member:discord.Member, nick:str):
        await ctx.channel.purge(limit = 1)
        await member.edit(nick = nick)

    @new_command
    async def testcmd(self, ctx):
        await ctx.send("test")
    
    


