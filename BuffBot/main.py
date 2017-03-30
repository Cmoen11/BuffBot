import discord
from discord.ext import commands
from BuffBot import botconfig
from BuffBot.currency import Currency

client = discord.Client()

bot = commands.Bot(command_prefix='!')
currency = Currency()
startup_extensions = ['commands', 'voice', 'currency']


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_voice_state_update(before, after):
    currency.register_activity(before, after)


if __name__ == '__main__':
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))
    bot.run(botconfig.token)

