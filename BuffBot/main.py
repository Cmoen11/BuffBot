import discord
from discord.ext import commands
import botconfig
from currency import Currency
from coins import Coin
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='!')
currency = Currency()

startup_extensions = ['commands', 'voice', 'coins', 'gambling']


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    coins = Coin(bot)
    await coins.give_coin()


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


