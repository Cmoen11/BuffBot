import discord
from discord.ext import commands
from currency import Currency

client = discord.Client()
currency = Currency()
bot = commands.Bot(command_prefix='!')
startup_extensions = ['commands', 'currency']


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_voice_state_update(before, after):
    currency.checkLogin(before, after)

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

