import time
import database
import datetime

class Currency:
    def __init__(self):
        self.name = 0

    # TODO Make a session persist between voice room changes if not in AFK
    def register_activity(self, before, after):

        if check_if_connected(after) and not member_in_channel("AFK", after):
            print("You're in", after.name)
            print(time.time())
            database.Database().set_coin_count_session_end(before.id, time_now(), 0)
            database.Database().set_coin_count_session_start(after.id, time_now(), 0, 1)
        elif not member_in_channel("AFK", after):
            print("You're out", after.name)
            database.Database().set_coin_count_session_end(before.id, time_now(), 0)

        # If user is in a channel named AFK, end session. IE: not get coins for being afk
        if member_in_channel("AFK", after):
            print("You're afk")
            database.Database().set_coin_count_session_end(before.id, time_now(), 0)


def time_now():
    # Epochtime
    return time.time()


def member_in_channel(channel_name, member):
    for channel in member.server.channels:
        if channel.name == channel_name:
            for member_result in channel.voice_members:
                if member == member_result:
                    return True


def check_if_connected(ctx):
    members = get_all_members_in_all_channels(ctx)
    if members != 0:
        if ctx in members:
            return True
        else:
            return False


def get_all_members_in_all_channels(ctx):
    members = []
    for channel in ctx.server.channels:
        if len(channel.voice_members) != 0:
            voice_members = channel.voice_members
            for member in voice_members:
                members.append(member)
            return members
    return 0


def setup(bot):
    bot.add_cog(Currency(bot))