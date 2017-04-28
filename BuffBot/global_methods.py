import asyncio
import discord
#### PERMISSION ####

def is_admin(member) :
    return member.server_permissions.administrator


#### SAY CHANNELS ####

async def say_gambling(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('gambling', server, bot)
    await bot.send_message(channel, msg)

async def say_general(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('general', server, bot)
    await bot.send_message(channel, msg)

async def say_other(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('other', server, bot)
    await send_message(channel, msg, bot)
    #await bot.send_message(channel, msg)

async def say_music(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('music', server, bot)
    await bot.send_message(channel, msg)

async def say_tax(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('tax', server, bot)
    await bot.send_message(channel, msg, bot)


async def send_message(channel, msg, bot):
    embed = discord.Embed()
    embed.title = "Buffbot"
    embed.description = msg
    embed.color = discord.Color.blue()
    await bot.send_message(channel, "", embed=embed)


async def music_playing(player, bot) :
    embed = discord.Embed()
    embed.title = "Music"
    embed.add_field(name="Song name", value=player.title, inline=True)
    embed.add_field(name="Duration", value=str(player.duration/60), inline=True)
    embed.add_field(name="Likes/dislike", value=str(player.likes)+"/"+str(player.dislikes), inline=True)
    embed.add_field(name="Views", value=str(player.views))
    embed.description = "Now playing.. "
    embed.set_footer("Please !queue <youtubelink> to get your song playing!")
    embed.color = discord.Color.dark_green()

    channel = await find_or_create_text_channel("music")

    await bot.send_message(channel, "", embed=embed)


async def find_or_create_text_channel(name, server, bot) :
    channels = server.channels
    for channel in channels:
        if str(channel.type) == 'text' and channel.name == name :
            return channel
    return await bot.create_channel(name=name, server=server, type='text')

