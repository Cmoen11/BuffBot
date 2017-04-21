import botconfig
from discord.ext import commands
import database
import botconfig
import global_methods
'''
    This module is for handling for channel management. 
    
'''

class Channel_manager:
    def __init__(self, bot):
        self.bot = bot  # The bot object.
        self.database = database.Database(self.bot)  # database object -> used to update and get coin amount
        self.owners = botconfig.owners
    pass

    @commands.group(name="man", pass_context=True, help="Please check {!help man} in order to check the commands")
    async def channel_mangement(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Please lookup !help man for commands in this group')

    @channel_mangement.group(name="flags", pass_context=True, help="Will give you a list of all flagged games for this channel")
    async def get_channel_flags(self, ctx):
        trigger_channel = ctx.message.author.voice.voice_channel
        if trigger_channel == None :
            await self.respond("You're not in a voice channel", ctx.message.author.mention)
            return None
        games = self.database.get_flagged_games(trigger_channel.id)

        output = "This channel is flagged for these games: \n"
        for game in games : output += game + "\n"

        await self.bot.say(output)
        pass

    @channel_mangement.command(name="patrol", pass_context=True, help="Will start the patrolling")
    async def patrol_channels(self, ctx):
        '''Patrol all voice channels from the calling channel.
                This method will go trough every channel and check each user. 
                    -> check if listed game is in the database
                        -> if not: move player to move queue.
                        -> if it is: Do nothing.
        '''

        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None

        # User is authorised to perform command.. -> now perform actions.

        good_members = []
        move_queue = []  # to store the queue for later to move them.
        jail = self.get_jail(ctx)  # grab the jail, if not jail.. create one.

        # start to check channels.
        for channel in ctx.message.server.channels:
            if channel != jail:
                # If this returns 0, it means that either the room is empty or it isn't a voice channel
                if len(channel.voice_members) != 0:
                    voice_members = channel.voice_members

                    for member in voice_members:  # for each member in the channel
                        if (len(self.database.get_flagged_games(channel_id=channel.id)) > 0) \
                                and self.database.get_flagged_games(channel_id=channel.id)[0] == "free":
                            # member is allowed.
                            pass
                        else:
                            print(self.database.get_flagged_games(channel.id))

                            if member.game not in self.database.get_flagged_games(channel.id):

                                if (not move_queue.__contains__(member)):
                                    move_queue.append(member)
                                    print("added to move")

                            else:
                                good_members.append(member.mention)  # Add member too good boy list

        await self.sort_members_to_channels(members=move_queue, jail=jail)

    @channel_mangement.command(name="wipe", pass_context=True, help="Will wipe clean all flags from this channel")
    async def remove_channel_flags(self, ctx):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        self.database.remove_flagged_games(ctx.message.author.voice.voice_channel.id)

    @channel_mangement.command(name="addgame", pass_context=True,
                      help="Flag channels for games only. If you enter free, there is no restriction on the selected channel")
    async def flag_channel(self, ctx, free=None):
        if not global_methods.is_admin(ctx.message.author):
            await self.bot.say("You're not a big boy")
            return None
        if (free == "free"):
            # remove all restriction on selected channel and parse in free.
            self.database.remove_flagged_games(ctx.message.author.voice.voice_channel.id)

            # add free in as a title.
            self.database.flag_gaming_channel(ctx.message.author.voice.voice_channel.id, "free", 1)
            pass

        else:
            self.database.flag_gaming_channel(ctx.message.author.voice.voice_channel.id, ctx.message.author.game, 1)
        pass

    async def sort_members_to_channels(self, members, jail):
        '''For handling the move queue for patrol_channels..
           Move queue
           this is a queue for members that need to be moved to other channels because their has broken the game rule. 
                -> For each item of the move queue. Grab the game title and check it up with the database.
                    -> if no game match
                        -> move to jail.
                    -> if game match one channel..
                        -> move member to that channel.    

        :param members:     The move queue
        :param jail:        Jail channel
        :return:            amount of moved members.
        '''
        for member in members:
            print("Handling " + member.mention)
            channel = self.database.get_game_channel(title=member.game)
            if (len(channel) == 0):
                await self.bot.move_member(member, jail)
            else:
                await self.bot.move_member(member, self.bot.get_channel(channel[0]))
        pass

    async def respond(self, msg, author):
        await self.bot.say("{}, {}".format(msg, author))

    # To check if the channel got a jail, return the channel. If channel do not have a jail voice channel.. create one.
    def get_jail(self, ctx):
        #########
        # Collect the jail channel, if no channel found -> create one.
        #########
        jail = None
        for channel in ctx.message.server.channels:
            if channel.name == "Jail":
                jail = channel
                break
        if jail is None:  # if no jail exists
            self.bot.create_channel(name="Jail", server=ctx.message.server, type='voice')  # create jail
            for channel in ctx.message.server.channels:  # find the new channel
                if channel.name == "Jail":
                    jail = channel
                    break
        return jail

def setup(bot):
    bot.add_cog(Channel_manager(bot))