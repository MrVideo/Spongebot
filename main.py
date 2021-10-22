import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random as rnd
from private.config import token

intents = discord.Intents.default()
description = "A bot that turns your text into SpONGetEXt"
client = Bot(command_prefix='?', intents=intents, description=description)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
async def on_message(message):
    if message.content.startswith('?'):
        await client.process_commands(message)

@client.command(name='sponge')
async def sponge(ctx, *, str: str):
    "Converts text into Spongetext"
    str = str.lower()
    for i in range(len(str)):
        sub = str[i:i+1]
        if(rnd.randrange(2) == 1):
            str = str.replace(sub, sub.upper(), 1)
    await ctx.send('Your spongified string is: ' + str)

client.run(token)