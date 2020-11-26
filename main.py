import os
import discord

from dotenv import load_dotenv, find_dotenv
from discord.ext import commands, tasks
from pymongo import MongoClient
from forms import sending_forms


load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True
key = os.getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!', intents = intents)
clientDB = MongoClient(os.getenv('MONGO_URI'))
db = clientDB['Letsrp-db']
wlforms = db.wlforms

print('Connected to DB')

@client.event
async def on_ready():
    activity = discord.Game('Write rp!info for server informations')
    await client.change_presence(activity = activity)
    print('Bot is active!')
    sending_forms.start(wlforms, client)

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
