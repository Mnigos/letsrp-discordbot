import os
import discord

from dotenv import load_dotenv, find_dotenv
from discord.ext import commands


load_dotenv(find_dotenv())

key = os.getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!')

@client.event
async def on_ready():
    activity = discord.Game("Let's RP")
    await client.change_presence(activity = activity)
    print('Bot is active!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(key)
