import discord

from dotenv import load_dotenv, find_dotenv
from os import getenv, listdir
from discord.ext import commands


load_dotenv(find_dotenv())

key = getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!')

@client.event
async def on_ready():
    print('Bot is active!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


client.run(key)
