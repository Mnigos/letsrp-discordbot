import os
import discord

from dotenv import load_dotenv, find_dotenv
from discord.ext import commands, tasks
from pymongo import MongoClient


load_dotenv(find_dotenv())

key = os.getenv('CLIENT_SECRET')
client = commands.Bot(command_prefix = 'rp!')
clientDB = MongoClient(os.getenv('MONGO_URI'))
db = clientDB['Letsrp-db']
wlforms = db.wlforms

print('Connected to DB')

@client.event
async def on_ready():
    activity = discord.Game("Let's RP")
    await client.change_presence(activity = activity)
    print('Bot is active!')
    sending_forms.start()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds = 2)
async def sending_forms():
    channel = client.get_channel('694925226697556078')
    formAccepted = wlforms.find_one({ 'status': 'awaiting' })
    formRejected = wlforms.find_one({ 'status': 'awaiting' })

    if (formAccepted != 'none'):
        name = formAccepted['dc']

        embed = discord.Embed(
            title = 'Podanie WL',
            description = f'''Twoje podanie {name} na Whitelist zostało zaakceptowane.
            Zgłoś się jak najszybciej na rozmowę!''',
            colour = '#00ff00'
        )

        await channel.send(embed = embed)

    if (formRejected != 'none'):
        name = formRejected['dc']
        reason = formRejected['reason']

        embed = discord.Embed(
            title = 'Podanie WL',
            description = f'''Twoje podanie {name} na Whitelist zostało odrzucone.
            Możesz napisac następne za 24h''',
            colour = '#ff0000'
        )
        embed.add_field(name = 'Powód:', value = reason)

        await channel.send(embed = embed)


client.run(key)
