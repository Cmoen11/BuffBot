import discord
from discord.ext import commands
import botconfig
from coins import Coin
from tax import Tax
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='!')

startup_extensions = ['commands', 'voice', 'coins', 'blackjack', 'channel_mangement', 'lottery', 'tax', 'holdem']


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    tax = Tax(bot)
    tax_task = asyncio.ensure_future(tax.wealth_tax())

    coins = Coin(bot)
    await coins.give_coin()

    await tax_task





if __name__ == '__main__':
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))
    bot.run(botconfig.token)

