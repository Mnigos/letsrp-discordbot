import os
import discord

from discord.ext import commands
from pymongo import MongoClient
from random import randint

cluster = MongoClient(os.getenv('MONGO_URI'))
db = cluster['Letsrp-DiscordBot']
users = db.users

class Rank(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx):
        await ctx.message.delete()
        query = users.find_one({ 'user': ctx.author.id })
        exp = query['exp']
        lvl = query['level']
        sum = 0

        for i in range(lvl + 1):
            sum += 5 * i ** 2 + 50 * i * 5

        embed = discord.Embed(
            title = ctx.author.name,
            colour = 0x62ff00
        )
        embed.add_field(name = 'Ranga', value = '#1', inline = False)
        embed.add_field(name = 'Poziom', value = lvl)
        embed.add_field(name = 'XP', value = f'{exp}/{sum}')
        embed.set_thumbnail(url = ctx.author.avatar_url)
        embed.set_footer(text = f'Author {ctx.author}')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Rank(client))

async def leaderboard():
    query = users.find().sort('exp', -1)
    ranking = []

    for user in query:
        ranking.append(user['user'])

    print(ranking)
