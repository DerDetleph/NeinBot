import datetime
from discord.ext import commands, tasks
from discord.utils import get
import pytz
import pickle
import re


class Task():
    def __init__(self, task, time):
        self.time = time
        self.run = task
        self.name = task.__name__


class ScheduledEvents():
    @staticmethod
    async def nnetdim(bot):
        await bot.wait_until_ready()
        channel = get(bot.get_all_channels(), id=796454540764774401)
        await channel.send("Nur noch ein Tag, dann ist Morgen!")


class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = [
            Task(ScheduledEvents.nnetdim, "20:15"),
            ]
        self.run_tasks.start()

    @staticmethod
    def get_hours_and_minutes():
        timezone = pytz.timezone('Europe/Berlin')
        now = datetime.datetime.now(timezone)
        return f"{now.hour}:{now.minute}"

    @tasks.loop(seconds=5)
    async def run_tasks(self):
        task_dict = self.load_config()
        for task in self.tasks:
            if task.time == self.get_hours_and_minutes():
                if not task_dict[task.name]:
                    await task.run(self.bot)
                    task_dict[task.name] = True
        self.write_config(task_dict)
        if re.match(r"00:\d{2}", self.get_hours_and_minutes()):
            await self.reset_config()

    @staticmethod
    def load_config():
        with open("NeinBot/Schedules.pickle", "rb") as f:
            dict = pickle.load(f)
            return dict

    @staticmethod
    def write_config(dict):
        with open("NeinBot/Schedules.pickle", "wb+") as f:
            pickle.dump(dict, f)

    @commands.command(aliases=["resetconfig"])
    async def reset_config(self, ctx = None):
        dict = {task.name: False for task in self.tasks}
        with open("NeinBot/Schedules.pickle", "wb+") as f:
            pickle.dump(dict, f)
        if ctx:
            await ctx.send("config reset")
    
    @commands.command(aliases = ["printdict"])
    async def print_dict(self, ctx):
        dict = self.load_config()
        await ctx.send(str(dict))
