from discord.ext import commands
import database
import time


class Currency:
    def __init__(self):
        self.name = 0


    def register_activity(self, before, after):
        connected = []

        if check_if_connected(after):
            print("in")
        else:
            print("out")


def check_if_connected(ctx):
    for channel in ctx.server.channels:
        if len(channel.voice_members) != 0:
            voice_members = channel.voice_members
            for member in voice_members:
                if ctx == member:
                    return True
                else:
                    break


def setup(bot):
    bot.add_cog(Currency(bot))