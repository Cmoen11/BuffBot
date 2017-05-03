import random
import database
from coins import Coin
import time
import botconfig
import global_methods

class Holdem
    def __init__(self, bot):
        self.bot = bot
        self.database = database.Database(self, bot)
        self.holdem_players = []
        self.game_status = 0
        self.deck = []
        self.coins = Coin(bot)

        # TODO: Command: holdem new, join, start, Call, raise, fold
        # TODO: Gather players

        @commands.group(name = "holdem", pass_context = True)
        async def holdem (self, ctx)
            if ctx.invoked_suvcommand is None:
                await self.bot.say("This is not a valid command, please add a subcommand")

        @holdem.command(name = "new", pass_context = True)
        async def new_game(self, ctx):
            if self.game_status != 0:
                self.bot.say("A game is already running, please wait to join")
                return None,
            self.deck = self.generateDeck()
            self.game_status = 1
            await self.bot.say("A Texas Hold'em table has opened"
                               "Please use !holdem join <Blind> to join the table")

        @holdem.command(name = "join", pass_context = True)
        async def join_game(self, ctx, bet):
            user = ctx.message.author
            if self.game_status != 1:
                await self.bot.say("No tables are open, please open one to play")