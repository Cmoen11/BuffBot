from discord.ext import commands
from simpleeval import simple_eval
import asyncio
import math
import random


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.owners = ["85431603408420864", "235892294857916417", "269919583899484160"]
        self.voice = None

    @commands.command(name="bye", pass_context=True)
    async def bye(self, ctx):
        if ctx.message.author.id in self.owners:
            await self.bot.say("Bye bye!")
            await self.bot.logout()

    @commands.command(name="math", pass_context=True)
    async def math(self, ctx, *, params):
        try:
            result = simple_eval(f"{params}", names={"e": math.e, "pi": math.pi},
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

    @commands.command(name="patrol", pass_context=True)
    async def kick_non_gamers(self, ctx):
        if ctx.message.author.id in self.owners:
            good_members = []
            jail = None
            #########
            # Collect the jail channel, if no channel found -> create one.
            #########
            for channel in ctx.message.server.channels:
                if channel.name == "Jail":
                    jail = channel
                    break
            if jail is None:  # if no jail exists
                await self.bot.create_channel(name="Jail", server=ctx.message.server, type='voice')  # create jail
                for channel in ctx.message.server.channels:
                    if channel.name == "Jail":
                        jail = channel
                        break

            #########
            # Patrols voice channels
            #########
            for channel in ctx.message.server.channels:
                if channel != jail:
                    # If this returns 0, it means that either the room is empty or it isn't a voice channel
                    if len(channel.voice_members) != 0:
                        voice_members = channel.voice_members

                        for member in voice_members:                        # for each member in the channel
                            if member.game is None:                         # Check if the member is playing
                                await self.bot.move_member(member, jail)    # -> jail the user if not
                            else:
                                good_members.append(member.display_name)    # append the good guys on the good guys list.

            #########
            # Give out info about the good boys.
            #########
            if len(good_members) == 0:
                await self.bot.say("You're all bad boys!")
            elif len(good_members) == 1:
                await self.bot.say("{} is a good boy, the rest of you I will now kick!".format(good_members[0]))
            else:
                await self.bot.say("{} are good boys, the rest I will now kick!".format(", ".join(good_members)))
        else:
            await self.bot.say("You're not a big guy.")

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
