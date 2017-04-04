from discord.ext import commands
import database
import asyncio



class Coin:
    def __init__(self, bot):
        self.bot = bot                                  # The bot object.
        self.coinActive = True                          # If this is set to false, the coin interval is stopped.
        self.database = database.Database()             # database object -> used to update and get coin amount
        self.COIN_AMOUNT = 0.1                          # amount of coins to be given every interval
        self.COIN_INTERVAL = 30                         # interval in seconds for sending out coins.

    @commands.command(name="coins", pass_context=True, help="Get your coin amount")
    async def get_coins(self, ctx):
        await self.bot.say("You have {} coins".format(self.database.get_coins(ctx.message.author.id)))

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
