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
async def test(ctx, *, str: str):
    "Deletes user message and sends the spongified string"
    str = str.lower()
    for i in range(len(str)):
        sub = str[i:i+1]
        if(rnd.randrange(2) == 1):
            str = str.replace(sub, sub.upper(), 1)
    await ctx.message.delete()
    await ctx.send(str)

client.run(token)