from discord.ext import commands
from simpleeval import simple_eval
import math
import random


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.owner = "85431603408420864"
        self.voice = None

    @commands.command(name="bye", pass_context=True)
    async def bye(self, ctx):
        if ctx.message.author.id == self.owner:
            await self.bot.say("Bye bye!")
            await self.bot.logout()

    @commands.command(name="math", pass_context=True)
    async def math(self, ctx, *, params):
        try:
            result = simple_eval(f"{params}", names={"e": math.e, "pi": math.pi, "lol": "retard"},
                                 functions={"log": math.log, "sqrt": math.sqrt, "cos": math.cos, "sin":math.sin,
                                            "tan":math.tan})

        except Exception:
            result = "Read the fucking manual"

        await self.respond(result, ctx.message.author.mention)

    @commands.command(name="doStuff", pass_context=True)
    async def do_stuff(self, ctx):
        pass

    @commands.command(name="summon", pass_context=True)
    async def summon(self, ctx):
        if self.voice:
            if self.voice.channel.id == ctx.message.author.voice.voice_channel.id:
                await self.bot.say("I'm already here ya dingus")
            else:
                await self.voice.move_to(ctx.message.author.voice.voice_channel)
        else:
            self.voice = await self.bot.join_voice_channel(ctx.message.author.voice.voice_channel)

    @commands.command(name="leaveChannel", pass_context=True)
    async def leaveChannel(self, ctx):
        await self.voice.disconnect()
        self.voice = None

    @commands.command(name="8ball", help="you may or may not get a yes or a no answer")
    async def eightball(self):
        await self.bot.say(get_random_line('8ballresponses.txt'))

    @commands.command(name="whoIsTheBuffest", pass_context=True)
    async def whoIsTheBuffest(self, ctx):
        await self.respond("Wiklem", ctx.message.author.mention)

    @commands.command(name="play", pass_context=True)
    async def playAudio(self, ctx):
        pass

    async def respond(self, msg, author):
        await self.bot.say(f"{msg}, {author}")


def get_random_line(file):
    with open(file, 'r') as f:
        line = next(f)
        for num, a in enumerate(f):
            if random.randrange(num + 2): continue
            line = a
    return line.rstrip()



def setup(bot):
    bot.add_cog(Command(bot))