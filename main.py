import os
import discord

from dotenv import load_dotenv, find_dotenv
from discord.ext import commands, tasks
from fivem import FiveM
from pymongo import MongoClient
from forms import sending_forms


load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True
key = os.getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!', intents = intents)
cluster = MongoClient(os.getenv('MONGO_URI'))
site_db = cluster['Letsrp-db']
wlforms = site_db.wlforms
server = FiveM(ip = 'wyspa.letsrp.pl', port = 30120)
info = '';

print('Connected to DB')

@client.event
async def on_ready():
    info = await server.get_server_info()
    activity = discord.Game(f'{info.clients}/{info.max_clients}')
    await client.change_presence(activity = activity)
    print('Bot is active!')
    sending_forms.start(site_db, client)
    players_on_server.start()

@tasks.loop(seconds = 2)
async def players_on_server():
    info = await server.get_server_info()
    activity = discord.Game(f'{info.clients}/{info.max_clients}')
    await client.change_presence(activity = activity)

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
