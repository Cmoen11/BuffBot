import asyncio

import discord
from discord.ext import commands

import global_methods
import playlist
from db import database


class Voice:
    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.volume = 1.0
        self.database = database.Database()
        self.playlist = playlist.Queue()
        self.people_voted = []
        self.seconds_to_next = 0
        self.music_server = None
        

    @commands.command(name="summon", pass_context=True)
    async def summon(self, ctx):
        if self.voice:
            if self.voice.channel.id == ctx.message.author.voice.voice_channel.id:
                await self.bot.say("I'm already here ya dingus")
            else:
                await self.voice.move_to(ctx.message.author.voice.voice_channel)
                self.music_server = self.voice.channel
        else:
            self.voice = await self.bot.join_voice_channel(ctx.message.author.voice.voice_channel)
            self.music_server = self.voice.channel


    @commands.command(name="leaveChannel", pass_context=True)
    async def leaveChannel(self, ctx):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        await self.voice.disconnect()
        self.voice = None

    @commands.command(name="play", pass_context=True, help="Play some music!")
    async def play_audio(self, ctx, link):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        await self.bot.say("Please use !queue instead..")
        song = link
        # link added to next field in current song
        self.playlist.add_song(song)
        self.seconds_to_next = 0


    @commands.command(name="votenext", pass_context=True)
    async def vote_next_song(self, ctx):
        if self.voice.channel.id != ctx.message.author.voice.voice_channel.id:
            await self.bot.say("You're not in the required voice channel to request to skip song, lil boy " + ctx.message.author.mention)
            return None
        
        if ctx.message.author.id in self.people_voted:
            await self.bot.say("You've already voted to skip this song, " + ctx.message.author.mention)
        else:
            self.people_voted.append(ctx.message.author.id)
            
            if len(self.people_voted) == (len(self.voice.channel.voice_members) // 2) + 1:
                self.people_voted.clear()
                # if there is an item at the front of the queue, play it and get the next item
                if self.playlist.current:
                    self.seconds_to_next = 0
                # nothing in queue
                elif self.playlist.current is None:
                    self.seconds_to_next = 0
            else:
                number = (len(self.voice.channel.voice_members) // 2) + 1 - len(self.people_voted)
                await self.bot.say(str(number) + " more votes needed")


    @commands.command(name="stop", pass_context=True, help="Stop the audio player")
    async def stop_audio(self, ctx):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        if self.player:
            self.player.stop()
        else:
            await self.bot.say("I'm not playing anything right now")

    @commands.command(name="setvolume", pass_context=True, help="Set the bot's volume (in percent)")
    async def set_volume(self, ctx, volume: int):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
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

    async def respond(self, msg, author):
        await self.bot.say("{}, {}".format(msg, author))

    @commands.command(name="queue", pass_context=True, help="Add youtube link to music queue")
    async def add_to_queue(self, ctx, link):
        # TODO: find better solution for extracting link from message
        song = link
        # link added to next field in current song
        self.playlist.add_song(song)
        self.database.add_music_to_db(song)
        if not self.music_server :
            self.music_server = self.get_or_take_member_channel(ctx)
        if self.seconds_to_next <= 0:
            self.people_voted.clear()
            if self.playlist.current is None:
                pass
            else:
                await self.play_music(self.playlist.pop())

    @commands.command(name="next", pass_context=True, help="Skip to next song in music queue")
    async def play_next(self, ctx):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None

        self.seconds_to_next = 0
        # nothing in queue

    def get_requested_server(self, ctx):
        trigger_channel = ctx.message.author.voice.voice_channel
        return trigger_channel

    @commands.command(name="start", pass_context=True, help="Start the music queue")
    async def start_queue(self, ctx):
        self.music_server = self.get_or_take_member_channel(ctx)
        self.people_voted.clear()
        if self.playlist.current is None:
            await self.play_music(link=self.database.get_random_music(), ctx=self.music_server)
        else:
            await self.play_music(ctx, self.playlist.pop())

    @commands.command(name="peter", pass_context=True)
    async def peter(self, ctx):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        await self.play_music(ctx, self.playlist.peter())

    @commands.command(name="timeleft", pass_context=True)
    async def time_left(self, ctx):
        await self.respond(str(self.seconds_to_next), ctx.message.author.mention)

    async def play_music(self, link):
        # Get the voice channel the commanding user is in
        trigger_channel = self.music_server
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

        await global_methods.music_playing(self.player, self.bot, self.music_server.server)   # print out music information

        self.player.volume = self.volume                                                # set the volume
        self.player.start()                                                             # starts the song
        await self.bot.change_presence(game=discord.Game(name=self.player.title))       # change bot presence

        self.seconds_to_next = self.player.duration
        await self.queue_is_alive()

    async def queue_is_alive(self):
        while self.seconds_to_next > 0:
            self.seconds_to_next -= 1
            await asyncio.sleep(1)

        self.people_voted.clear()
        # if there is an item at the front of the queue, play it and get the next item
        if self.playlist.current:
            await self.play_music(self.playlist.pop())
            await asyncio.sleep(5)

        elif self.playlist.current is None:
            await self.play_music(link=self.database.get_random_music())
            #await self.bot.change_presence(game=discord.Game(name='Queue is empty'))

    def get_or_take_member_channel(self, ctx):
        if ctx.message.author.voice.voice_channel.id == self.music_server: return self.music_server
        else: return ctx.message.author.voice.voice_channel

    @commands.command(name='playlist', help='Output the current playlist')
    async def print_playlist(self):
        await self.bot.say(self.playlist.prepare_playlist())




def setup(bot):
    bot.add_cog(Voice(bot))
