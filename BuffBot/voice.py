from discord.ext import commands
from simpleeval import simple_eval
import math
import os
import random
import aiohttp
import hashlib
import database
import playlist as p
import botconfig



class Voice:
    def __init__(self, bot):
        self.bot = bot
        self.owners = botconfig.owners
        self.voice = None
        self.player = None
        self.volume = 1.0
        self.database = database.Database()
        self.playlist = None

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

    @commands.command(name="play", pass_context=True, help="Play some music!")
    async def play_audio(self, ctx, link):
        self.play_music(ctx, link)

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
    async def flag_channel(self, ctx):
        self.database.flag_gaming_channel(ctx.message.author.voice.voice_channel.id, ctx.message.author.game, 1)
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
                            print(self.database.get_flagged_games(channel.id))

                            if member.game not in self.database.get_flagged_games(channel.id):
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

    @commands.command(name="queue", pass_context=True)
    async def add_to_queue(self, link):
        # TODO: find better solution for extracting link from message
        song = link.message.content[7:]
        if self.playlist is None:
            self.playlist = p.Queue(song)
            print("Added:" + self.playlist.current.get_song())
        else:
            self.playlist.current.queue_next(self.playlist.current, song)

    @commands.command(name="next", pass_context=True)
    async def play_next(self, ctx):
        if self.playlist.current.has_next():
            self.play_music(ctx, self.playlist.pop())

    @commands.command(name="start", pass_context=True)
    async def start_queue(self, ctx):
        if self.playlist is None:
            await self.respond("Nothing added to queue", ctx.message.author)
            return
        else:
            link = self.playlist.pop()
            await self.play_music(ctx, link)

    async def play_music(self, ctx, link):
        if ctx.message.author.id not in self.owners:
            return None
        # Get the voice channel the commanding user is in
        trigger_channel = ctx.message.author.voice.voice_channel
        # Return with a message if the user is not in a voice channel
        if trigger_channel is None:
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




def setup(bot):
    bot.add_cog(Voice(bot))
