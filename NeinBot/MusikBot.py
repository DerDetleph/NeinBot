import discord
import youtube_dl as yt_dl
from discord.ext import commands
from discord.utils import get
import re
import asyncio


class Musikbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.pause()

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and not voice.is_playing():
            try:
                voice.resume()
            except Exception as e:
                ctx.send(e)

    @commands.command(aliases=["disconnect"])
    async def leave(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice:
            await voice.disconnect()

    @commands.command()
    async def play(self, ctx, url: str = None):
        if not url or not url_verifier(url):
            ctx.send("Url benötigt.")
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        channel = ctx.author.voice.channel
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        self.queue.append(url)
        if voice.is_playing():
            return
        await Musikbot.play_queue(self, ctx, voice)

    @commands.command()
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and len(self.queue) > 0:
            voice.stop()
        Musikbot.play_queue(self, ctx, voice)

    @commands.command(aliases=["addqueue"])
    async def queueadd(self, ctx, url: str = None):
        if not url or not url_verifier(url):
            ctx.send("Url benötigt.")
            return
        self.queue.append(url)
        ctx.send("Url zur Queue hinzugefügt.")

    @commands.command(aliases=["queueclear", "clearqueue"])
    async def clear(self, ctx):
        self.queue.clear()
        ctx.send("Queue wurde geleert")

    async def play_queue(self, ctx, voice):
        while len(self.queue) > 0:
            with yt_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
                info = ydl.extract_info(self.queue[0], download=False)
                URL = info['formats'][0]['url']
                voice.play(discord.FFmpegPCMAudio(URL))
                await ctx.send("Now playing %s" % info["title"])
                del self.queue[0]
                while voice.is_playing():
                    await asyncio.sleep(1)


def url_verifier(msg):
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg)
