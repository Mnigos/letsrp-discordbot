import discord

from dotenv import load_dotenv, find_dotenv
from os import getenv
from discord.ext import commands

load_dotenv(find_dotenv())

key = getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!')

@client.event
async def on_ready():
    print('Bot is active!')


client.run(key)
