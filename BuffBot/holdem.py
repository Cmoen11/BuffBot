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
        self.dealersHand = []
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
            start_msg =   "  _______                   _    _       _     _\n" \
                          " |__   __|                 | |  | |     | |   | |               \n" \
                          "    | | _____  ____ _ ___  | |__| | ___ | | __| | ___ _ __ ___  \n" \
                          "    | |/ _ \ \/ / _` / __| |  __  |/ _ \| |/ _` |/ _ | '_ ` _ \ \n" \
                          "    | |  __/>  | (_| \__ \ | |  | | (_) | | (_| |  __| | | | | |\n" \
                          "    |_|\___/_/\_\__,_|___/ |_|  |_|\___/|_|\__,_|\___|_| |_| |_|\n"
            await self.bot.say(start_msg, "A Texas Hold'em table has opened"
                                          "Please use !holdem join <Blind> to join the table")

        @holdem.command(name = "join", pass_context = True)
        async def join_game(self, ctx, bet):
            user = ctx.message.author
            if self.game_status != 1:
                await self.bot.say("No tables are open, please open one to play")

            if self.player_at_table(ctx.message.author):
                await  self.bot.say(user.mention + "You're seated and ready to play")
                return None

            if float(bet) <= 0 and not self.coins.check_balance(bet):
                await self.bot.say(user.mention + " please make sure your bet is higher"
                                                  "than 0 and that you've got enough coins")
                return None

            self.database.remove_coins(userid = user.id, coins = float(bet), mention = user.mention)

            # TODO : Make drawcard Dynamic
            self.holdem_players.append({
                "user": user, "cards":[self.drawCard(), self.drawCard()], "bet": float(bet), "Status": 0
            })

            await self.bot.say(user.mention + " You've joined the table, please wait for the game to start,")


        @holdem.command(name = "start", pass_context = True)
        async def start_game(self, ctx):
            self.game_status = 3
            self.dealersHand = [self.drawCard(), self.drawCard()]

