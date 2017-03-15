import discord
from discord.ext import commands
import database
import time

client = discord.Client()

bot = commands.Bot(command_prefix='!')
startup_extensions = ['commands']


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


def printtest(ctx):
    print(ctx)

# TODO: make new class and add database to on_voice_state_update
@bot.event
async def on_voice_state_update(before, after):
    connected = []
    if after not in connected:
        if checkifconnected(after):
            connected.append(after)
            print(len(connected))


    if len(connected) != 0:
        for user in connected:
            if not checkifconnected(before):
                connected.remove(before)
                # TODO: Why doesn't this run?
                printtest("test")
                break


def checkifconnected(ctx):
    for channel in ctx.server.channels:
        if ctx in channel.voice_members:
            return True


if __name__ == '__main__':
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))

        # To run: Make a file called key.text in root
        file = open("key.txt", "r")
        bot.run(file.read())

