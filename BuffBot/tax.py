from discord.ext import commands
import database
import asyncio
import global_methods




class Tax:
    def __init__(self, bot):
        self.bot = bot
        self.taxable = True
        self.database = database.Database(self.bot)
        self.tax_amount_percentage = 0.20
        self.wealth_tax_percentage = 0.10
        self.is_wealthy = 4000  # Users with this amount of coins or greater has to pay wealthTax
        self.WEALTH_TAX_INTERVAL = 5  # Interval for wealth tax.

    @commands.group(name="tax", pass_context=True, help="Please check the {!help tax} in order to check the commands")
    async def tax(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Please lookup !help tax for commands in this group')

    @tax.command(name="taxmoney", pass_conetxt=True, help="Shows how much tax the bot has collected")
    async def get_tax(self):
        await self.bot.say("I've collected {} coins. These coins shall be fairly used among us all!".format(self.database.get_coins(self.bot.user.id)))

    @tax.command(name="taxon", pass_context=True, help="Enable tax")
    async def set_tax_on(self, ctx):
        user = ctx.message.author


        if not self.taxable:
            await self.bot.say("{} M8, the tax is already enabled!".format(user.mention))
            return None
        self.taxable = True
        await self.bot.say("{} The tax is now enabled!".format(user.mention))

    @tax.command(name="taxoff", pass_context=True, help="Disable tax")
    async def set_tax_off(self, ctx):
        user = ctx.message.author

        if not self.taxable:
            await self.bot.say("{} M8, the tax is already disabled!".format(user.mention))
            return None
        self.taxable = False
        await self.bot.say("{} The tax is now disabled!".format(user.mention))

    @tax.command(name="settax", pass_context=True, help="Set the tax percantage - usage: !settax X%")
    async def set_tax_percentage(self, ctx, tax_percentage):

        user = ctx.message.author
        if float(tax_percentage) <= 0 or float(tax_percentage) >= 1:
            await self.bot.say("{}, please enter a valid amount".format(user.mention))
            return None
        self.tax_amount_percentage = tax_percentage
        await self.bot.say("Amazing! I'm now collecting {}% of your income!".format(self.tax_amount_percentage))
        #TODO: Only get decimals...

    @tax.command(name="setwealthtax", pass_context=True, help="Set the wealth tax percentage - usage: !setwealthtax X%")
    async def set_wealth_tax_percentage(self, ctx, wealth_tax_percentage):

        user = ctx.message.author
        if float(wealth_tax_percentage) <= 0 or float(wealth_tax_percentage) >= 1:
            await self.bot.say("{}, please enter a valid amount".format(user.mention))
            return None
        self.wealth_tax_percentage = wealth_tax_percentage
        await self.bot.say("Amazing! I'm now collecting {}% of your wealthy money!".format(self.wealth_tax_percentage))

    @tax.command(name='wealthylvl', pass_conrext=True, help="Anyone with coins greater than or equal to this has to pay wealth tax")
    async def set_is_wealthy(self, wealthylvl):
        self.is_wealthy = wealthylvl
        await self.bot.say("I'm now taxing anyone with {} or more coins.".format(self.is_wealthy))

    @tax.command(name='taxstatus', pass_context=True, help="Status of tax")
    async def get_taxable(self):
        await self.bot.say(str(self.taxable))

    async def wealth_tax(self):
        while self.taxable:
            for user in self.database.get_rich_users(self.bot.user.id, self.is_wealthy):
            # Calculate how much this user must tax.
                totalTax = user["coins"] * self.wealth_tax_percentage
                self.database.remove_coins(user["userid"], totalTax, user["mention"])
                self.database.insert_coins(self.bot.user.id, totalTax, self.bot.user.mention)
            await self.bot.send_message(self.bot.get_channel(id='298246065780555778'),
                                        'Rich people make me sick! I take your money! Total tax amount is now: %d'
                                        % self.database.get_coins(self.bot.user.id))
            print("hei")
            await asyncio.sleep(self.WEALTH_TAX_INTERVAL)


def setup(bot):
    bot.add_cog(Tax(bot))