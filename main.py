import discord
from discord.ext.commands import Bot
import random as rnd
from private.config import token

from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

# Bot initialization
intents = discord.Intents.default()
description = "A bot that turns your text into SpONGetEXt"
client = Bot(command_prefix='?', intents=intents, description=description)

# Help command embed creation
helpEmbed = discord.Embed()
helpEmbed.title = "List of commands"
helpEmbed.description = "The bot's prefix is `?`"
helpEmbed.add_field(name="Convert to spongetext", value="`?sponge <string>`", inline=False)
helpEmbed.add_field(name="Show help embed", value="`?help`", inline=False)

# Remove the default help command
client.remove_command('help')

# Ready event handler
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="type ?help"))
    print('We have logged in as {0.user}'.format(client))

# Message listener
@client.event
async def on_message(message):
    if message.content.startswith('?'):
        await client.process_commands(message)

# Error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("That command does not exist. Retry.")
    elif isinstance(error, MissingRequiredArgument):
        await ctx.send("That command is missing required arguments. Retry.")
    else:
        raise error

# Commands
@client.command(name='sponge')
async def sponge(ctx, *, str: str):
    "Deletes user message and sends the spongified string"
    str = str.lower()
    for i in range(len(str)):
        sub = str[i:i+1]
        if(rnd.randrange(2) == 1):
            str = str.replace(sub, sub.upper(), 1)
    await ctx.message.delete()
    await ctx.send(str)

@client.command(name='help')
async def help(ctx):
    "Sends a help embed to the user"
    await ctx.send(embed=helpEmbed)

# Run client
client.run(token)