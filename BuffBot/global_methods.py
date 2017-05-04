import asyncio

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
    await bot.send_message(channel, msg)

async def say_music(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('music', server, bot)
    await bot.send_message(channel, msg)

async def say_tax(ctx, msg, bot):
    server = ctx.message.server
    channel = await find_or_create_text_channel('tax', server, bot)
    await bot.send_message(channel, msg)


async def find_or_create_text_channel(name, server, bot) :

    channels = server.channels
    for channel in channels  :
        if str(channel.type) == 'text' and channel.name == name :
            return channel
    return await bot.create_channel(name=name, server=server, type='text')

