from discord.ext import commands
from simpleeval import simple_eval
import asyncio
import math
import os
import random
import dataset
import aiohttp
import hashlib

class Command:
    def __init__(self, bot):
        self.bot = bot
        self.owners = ["85431603408420864", "235892294857916417", "269919583899484160", "95596654194855936", "125307006260084736"]
        self.voice = None
        self.player = None
        self.volume = 1.0

    @commands.command(name="bye", pass_context=True)
    async def bye(self, ctx):
        if ctx.message.author.id in self.owners:
            await self.bot.say("Bye bye!")
            await self.bot.logout()

    @commands.command(name="math", pass_context=True)
    async def math(self, ctx, *, params):
        try:
            result = simple_eval("{}".format(params), names={"e": math.e, "pi": math.pi},
                                 functions={"log": math.log, "sqrt": math.sqrt, "cos": math.cos, "sin": math.sin,
                                            "tan": math.tan})
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

    @commands.command(name="play", pass_context=True, help="Play some music!")
    async def play_audio(self, ctx, link):
        if ctx.message.author.id not in self.owners:
            return None
        # Get the voice channel the commanding user is in
        trigger_channel = ctx.message.author.voice.voice_channel
        # Return with a message if the user is not in a voice channel
        if trigger_channel == None:
            await self.bot.say("You're not in a voice channel right now")
            return
        if self.voice:
            if self.voice.channel.id != trigger_channel.id:
                # If the bot is in voice, but not in the same channel, move to the commanding user
                await self.voice.move_to(trigger_channel)
        else:
            # If the bot is not in a voice channel, join the commanding user
            self.voice = await self.bot.join_voice_channel(trigger_channel)
        # Stop the player if it is running, to make room for the next one
        if self.player:
            self.player.stop()
        # Create a StreamPlayer with the requested link
        self.player = await self.voice.create_ytdl_player(link)
        # Set the volume to the bot's volume value
        self.player.volume = self.volume
        self.player.start()

    @commands.command(name="stop", pass_context=True, help="Stop the audio player")
    async def stop_audio(self, ctx):
        if ctx.message.author.id not in self.owners:
            return None
        if self.player:
            self.player.stop()
        else:
            await self.bot.say("I'm not playing anything right now")

    @commands.command(name="setvolume", pass_context=True, help="Set the bot's volume (in percent)")
    async def set_volume(self, ctx, volume: int):
        if ctx.message.author.id not in self.owners:
            return None
        # Ensure the volume argument is between 0 and 100.
        if 0 > volume or volume > 100:
            await self.bot.say("I don't want to blow out your ears")
            return
        # Set the bot's volume value
        self.volume = float(volume/100)
        if self.player:
            # Set the volume to the player if it exists
            self.player.volume = self.volume
        else:
            await self.bot.say("I'm not playing anything right now, but I set the volume to {}% for next time".format(volume))

    @commands.command(name="flagChan", pass_context=True, help="Flag channels for games only. If you enter free, there is no restriction on the selected channel")
    async def flag_channel(self, ctx, game_title):

        pass
    
    @commands.command(name="smugadd", pass_context=True)
    async def add_smug(self, ctx, path):
        allowed_content = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/gif': 'gif'}
        async with aiohttp.get(path) as r:
            if r.status == 200:
                file = await r.content.read()
                type = r.headers['Content-Type']
        if type not in allowed_content:
            await self.bot.say("That kind of file is not allowed")
            return
        else:
            hash = hashlib.md5(file).hexdigest()
            filename = "smug-anime-faces/{}.{}".format(hash, allowed_content[type])
            with open(filename, 'wb') as f:
                f.write(file)
            await self.bot.say("Smugness levels increased")
        
        
    
    @commands.command(name="smug", pass_context=True)
    async def smug(self, ctx):
        path = 'smug-anime-faces' # The folder in which smug anime face images are contained
        face = os.path.join(path, random.choice(os.listdir(path))) # Generate path to a random face
        # Send the image to the channel where the smug command was triggered
        await self.bot.send_file(ctx.message.channel, face)

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
                for channel in ctx.message.server.channels:   # find the new channel
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
                                good_members.append(member.mention)         # Add member too good boy list

            #########
            # Give out info about the good boys.
            #########
            if len(good_members) == 0:
                await self.bot.say("You're all bad boys! :wink: ")
            elif len(good_members) == 1:
                await self.bot.say("{} is a good boy, the rest of you I will now kick!".format(good_members[0]))
            else:
                await self.bot.say("{} are good boys, the rest I will now kick!".format(", ".join(good_members)))
        else:
            await self.bot.say("You're not a big guy. :thinking: ")

    async def respond(self, msg, author):
        await self.bot.say("{}, {}".format(msg, author))


def get_random_line(file):
    with open(file, 'r') as f:
        line = next(f)
        for num, a in enumerate(f):
            if random.randrange(num + 2): continue
            line = a
    return line.rstrip()


def setup(bot):
    bot.add_cog(Command(bot))
