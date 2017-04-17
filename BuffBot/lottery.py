import random
import math
from discord.ext import commands
import discord
import database
from coins import Coin

class Lottery:
    def __init__(self, bot):
        self.bot = bot
        self.database = database.Database(self.bot)
        self.coins = Coin(bot)
        # self.lotteryTickets = {} // Different implementation
        self.ticketCost = 100
        self.winningTicket = 0
        self.ticketCounter = 0
        self.prizePool = 0
        self.generate_winning_number(100)



    @commands.command(name="buyticket", pass_context=True)
    async def buy_ticket(self, ctx):
        user = ctx.message.author
        if self.check_balance(user.id) < self.ticketCost:
            await self.bot.say("You don't have enough coins to buy a ticket", user.mention)
        else:
            self.database.remove_coins(ctx.message.author.id, self.ticketCost)
            if self.ticketCounter == self.winningTicket:
                self.generate_winning_number(100)
                self.database.insert_coins(user.id, self.prizePool, user.mention)
                await self.bot.say("Congratulation, you won the lottery with a prizepool of " + str(self.prizePool),
                                   user.mention)
            else:
                self.ticketCounter += 1
                await self.bot.say("Better luck next time", user.mention)

    # Creates a new winning number, while resetting the counter, were the nr_of_tickets represents the odds of winning
    def generate_winning_number(self, nr_of_tickets):
        self.ticketCounter = 0
        self.prizePool = nr_of_tickets * int(self.ticketCost / 2.2)
        self.winningTicket = random.randrange(1, nr_of_tickets)
