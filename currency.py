from discord.ext import commands
import database
import time


class Currency:
    def __init__(self):
        self.name = 0


    def checkLogin(self, before, after):
        connected = []
        if after not in connected:
            if checkifconnected(after):
                connected.append(after)
                print(len(connected))
        elif after in connected:
            if not checkifconnected(before):
                connected.remove(before)
                # TODO: Why does this not run?
                printtest("test")


def printtest(ctx):
    print(ctx)


def checkifconnected(ctx):
    for channel in ctx.server.channels:
        if ctx in channel.voice_members:
            return True


def setup(bot):
    bot.add_cog(Currency(bot))