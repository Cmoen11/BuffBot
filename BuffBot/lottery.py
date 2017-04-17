import random
import discord
from discord.ext import commands
import database
from coins import Coin

class Lottery:
    def __init__(self, bot):
        self.bot = bot
        self.database = database.Database(self.bot)
        self.coins = Coin(bot)
        # self.lotteryTickets = {} // Different implementation
        self.ticketCost = 1
        self.winningTicket = 0
        self.ticketCounter = 0
        self.generate_winning_number(10)



    @commands.command(name="buyticket", pass_context=True)
    async def buy_ticket(self, ctx):
        user = ctx.message.author
        if self.check_balance(user.id) < self.ticketCost:
            await self.bot.say("You don't have enough coins", user.mention)
        else:
            self.database.remove_coins(ctx.message.author.id, self.ticketCost)
            if self.ticketCounter == self.winningTicket:
                self.generate_winning_number(10)
                self.database.insert_coins(user.id, self.ticketCost * 4, user.mention)
            else:
                await self.bot.say("Better luck next time", user.mention)

    def generate_winning_number(self, nr_of_tickets):
        self.ticketCounter = 0
        self.winningTicket = random.randrange(0, nr_of_tickets)
