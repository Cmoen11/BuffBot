import discord
from discord.ext import commands

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

@bot.event
async def on_voice_state_update(before):
    connected = []
    if checkconnected(before):
        connected.append(before)
        bot.say("added")
    else:
        connected.remove(before)
        bot.say("removed")
    #before, if the user who triggered is not in the list add him

async def checkconnected(before):
    for channel in before.server.channels:
        if before in channel.voice_members:
            return True

    # Make list of currently connected
    # Update list everytime on_voice_state_update is invoked


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

