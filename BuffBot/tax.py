from discord.ext import commands
import database
import asyncio
import discord


class Tax:
    def __init__(self, bot):
        self.bot = bot
        self.database = database.Database(self.bot)
        self.taxable = True  # Will collect tax if bot in voice channel. Disable this by setting taxable to false.
        self.wealthTaxPercentage = 0.1  # Wealth tax percentage.
        self.WEALTH_TAX_INTERVAL = 5  # Interval for wealth tax.


    @commands.command(name="taxmoney", pass_conetxt=True, help="Shows how much tax the bot has collected")
    async def get_tax(self, ctx):
        await self.bot.say("I've collected {} coins. These coins shall be fairly used among us all!")


    async def wealth_tax(self):
        while self.taxable:
            for user in self.database.get_rich_users(self.bot.user.id):
                # Calculate how much this user must tax.
                totalTax = user["coins"] * self.wealthTaxPercentage
                self.database.remove_coins(user["userid"], totalTax, user["mention"])
                self.database.insert_coins(self.bot.user.id, totalTax, self.bot.user.mention)
            await asyncio.sleep(self.WEALTH_TAX_INTERVAL)