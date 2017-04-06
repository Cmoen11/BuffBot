from discord.ext import commands
import database
import asyncio
import random
import discord


class Coin:
    def __init__(self, bot):
        self.bot = bot                                  # The bot object.
        self.coinActive = True                          # If this is set to false, the coin interval is stopped.
        self.database = database.Database()             # database object -> used to update and get coin amount
        self.COIN_AMOUNT = 1                            # amount of coins to be given every interval
        self.COIN_INTERVAL = 30                         # interval in seconds for sending out coins.

    @commands.command(name="coins", pass_context=True, help="Get your coin amount")
    async def get_coins(self, ctx):
        await self.bot.say("{}, you have {} coins".format(ctx.message.author.mention, self.database.get_coins(ctx.message.author.id)))

    @commands.command(name="roll", pass_context=True, help="Gamble coins, reach over 50 in a random number between 0 - 100")
    async def roll_dice(self, ctx, amount):
        if float(amount) <= 0 :
            await self.bot.say("{}, retard?".format(ctx.message.author.mention))
            return None

        if not self.check_balance(ctx.message.author, float(amount)):
            await self.bot.say("{}, sorry buddy.. you do not have enough coins to do this bet.. You got {}"
                               .format(ctx.message.author.mention, self.database.get_coins(ctx.message.author.id)))
            return None

        rolled = random.randint(0,100)
        if rolled <= 50 :
            self.database.remove_coins(ctx.message.author.id, amount)
            await self.bot.say("{}, you lost.. you rolled {} and lost {} coins".format(ctx.message.author.mention, rolled, amount))
            pass
        else :
            self.database.insert_coins(ctx.message.author.id, amount)
            await self.bot.say(
                "{}, you won! you rolled {} and won {} coins".format(ctx.message.author.mention, rolled, amount))
            pass

    @commands.command(name="donate", pass_context=True)
    async def donate_coins(self, ctx, toUser :discord.Member, coins):
        server = ctx.message.server
        member = toUser
        if member is not None :
            if self.check_balance(ctx.message.author, float(coins)):
                if float(coins) > 0 :
                    # Remove coins from sender
                    self.database.remove_coins(userid=ctx.message.author.id, coins=coins)
                    # give coins to reciver
                    self.database.insert_coins(userid=member.id, coins=coins)

                    await self.bot.say("{}, you donated {} coins to {}".format(ctx.message.author.mention, coins, member.mention))

                else :
                    await self.bot.say("{}, coins needs to be higher than 0.".format(ctx.message.author.mention))
            else :
                await self.bot.say("{}, not enough coins.".format(ctx.message.author.mention))
        else:
            await self.bot.say("Did not find member {}".format(toUser))

    @commands.command(name="toplist", pass_context=False)
    async def get_toplist(self):
        toplist = self.database.get_top_coin_holders();
        output = "On the coin top we got: \n \n"
        count = 1
        for user in toplist :
            user_obj = await self.bot.get_user_info(user["userid"])
            output += "#{} {} with {} coins \n".format(count, user_obj.mention, user["coins"])
            count += 1
        await self.bot.say(output)


    def check_balance(self,user, requestedBalance):
        if self.database.get_coins(user.id) < float(requestedBalance) :
            return False;
        return True;

    async def give_coin(self):
        '''
        this is used to give coins every interval set by object vars...
        '''
        while self.coinActive:
            members = self.get_all_voice_members_except_in_afk()

            for m in members :
                self.database.insert_coins(m.id, self.COIN_AMOUNT)
            await asyncio.sleep(30)


    def get_all_voice_members_except_in_afk(self):
        '''
        get every member of voice channels except channels named AFK.
        :return:    a list of members
        '''
        members = []
        for server in self.bot.servers:
            for channel in server.channels :

                if channel.name != "AFK":
                    # If this returns 0, it means that either the room is empty or it isn't a voice channel
                    if len(channel.voice_members) != 0:
                        voice_members = channel.voice_members
                        for member in voice_members:
                            members.append(member)

        return members


def setup(bot):
    bot.add_cog(Coin(bot))
