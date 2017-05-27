from discord.ext import commands

from coins import Coin
from db import database


class Holdem:
    def __init__(self, bot):
        self.bot = bot
        self.database = database.Database(self.bot)
        self.holdem_players = []
        self.game_status = 0
        self.deck = []
        self.dealersHand = []
        self.coins = Coin(bot)


        # TODO: Command: holdem new, join, start, Call, raise, fold
        # TODO: Gather players

        @commands.group(name="holdem", pass_context=True)
        async def holdem(self, ctx):
            if ctx.invoked_subcommand is None:
                await self.bot.say("This is not a valid command, please add a subcommand")


        @holdem.command(name = "new", pass_context = True)
        async def new_game(self, ctx):
            if self.game_status != 0:
                self.bot.say("A game is already running, please wait to join")
                return None,
            self.deck = self.generateDeck()
            self.game_status = 1
            welcome_msg =   "_______                   _    _       _     _\n" \
                          " |__   __|                 | |  | |     | |   | |               \n" \
                          "    | | _____  ____ _ ___  | |__| | ___ | | __| | ___ _ __ ___  \n" \
                          "    | |/ _ \ \/ / _` / __| |  __  |/ _ \| |/ _` |/ _ | '_ ` _ \ \n" \
                          "    | |  __/>  | (_| \__ \ | |  | | (_) | | (_| |  __| | | | | |\n" \
                          "    |_|\___/_/\_\__,_|___/ |_|  |_|\___/|_|\__,_|\___|_| |_| |_|\n"
            await self.bot.say(welcome_msg, "A Texas Hold'em table has opened"
                                            "Please use !holdem join <Blind> to join the table")

        @holdem.command(name = "join", pass_context = True)
        async def join_game(self, ctx, bet):
            user = ctx.message.author
            if self.game_status != 1:
                await self.bot.say("No tables are open, please open one to play")
                return None

            if self.players_at_table(ctx.message.author):
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

            if len(self.holdem_players) < 2:
                await self.bot.say("There needs to be at least 2 players at the table")
                return None
            # TODO: Solve this when you use the join command
            elif len(self.holdem_players) > 9 :
                await self.bot.say("There are too many people at the table")
                return None

            self.game_status = 3
            self.dealersHand = [self.drawCard(), self.drawCard()]


            start_msg = "Let's play Texas Hold'em!"
            await self.bot.say(start_msg)

            for player in self.holdem_players:
                self.bot.send_message(player["user"], "This is your hand: " +
                                      player['cards'][0].getStringSymbol() + player['cards'][0].getStringValue())
                pass

            community_cards_msg = "Here are the community cards: " + \
                         self.dealerCards[0].getStringSymbol() + self.dealerCards[0].getStringValue()
            await self.bot.say(community_cards_msg)

        @holdem.command(name = "Call", pass_context = True)
        async def holdem_call(self, ctx):
            player = self.players_at_table(ctx.message.author)
            if player is None:
                await self.bot.say("You're not at this table, " + ctx.message.author.mention)
                return None

            if player["status"] != 0:
                await self.bot.say(ctx.message.author.mention + " is calling the bet")
                return None
            pass

        @holdem.command(name = "raise", pass_context = True)
        async def holdem_stand(self, ctx, bet_raise):
            player = self.players_at_table(ctx.message.author)
            if player is None:
                await self.bot.say("You're not at this table, " + ctx.message.author.mention)
                return None

            if bet_raise <= 0 or None:
                await self.bot.say(ctx.message.author.mention + "You need to specify a bet")
                return None

            for player in self.players_at_table:
                if player["name"] == player:
                    player["bet"] += bet_raise

            await self.bot.say(ctx.message.author.mention + " Raised the bet")


def setup(bot):
    bot.add_cog(Holdem(bot))



