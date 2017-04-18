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
        self.generate_tickets(100)



    @commands.command(name="buyticket", pass_context=True, help="Buy tickets for 100 coins for a chance to win loyal guns")
    async def buy_ticket(self, ctx):
        user = ctx.message.author
        if not self.coins.check_balance(user, self.ticketCost):
            await self.bot.say(("{}, You don't have enough coins to buy a ticket \n - Current balance: " +
                                str(self.database.get_coins(user.id))).format(user.mention))
        else:
            self.database.remove_coins(user.id, self.ticketCost, user.mention)
            if self.ticketCounter == self.winningTicket:
                self.generate_tickets(100)
                self.database.insert_coins(user.id, self.prizePool, user.mention)
                await self.bot.say(("{}, Congratulations, you won the lottery with a prizepool of " + str(self.prizePool)
                                    + "\n- Current balance: " + str(self.database.get_coins(user.id))).format(user.mention))
            else:
                self.ticketCounter += 1
                await self.bot.say(("{}, You lost, better luck next time!" + "\n - Current balance: " +
                                    str(self.database.get_coins(user.id))).format(user.mention))

    # Creates a new winning number, while resetting the counter, were the nr_of_tickets represents the odds of winning
    def generate_tickets(self, nr_of_tickets):
        self.ticketCounter = 1
        self.prizePool = nr_of_tickets * int(self.ticketCost * 0.9)
        self.winningTicket = random.randint(1, nr_of_tickets)


def setup(bot):
    bot.add_cog(Lottery(bot))
