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
    async def rank(self, ctx, user: discord.Member = None):
        await ctx.message.delete()

        if not user:
            user = ctx.author

        rank = await leaderboard(user)
        query = users.find_one({ 'user': user.id })
        exp = query['exp']
        lvl = query['level']
        sum = 0

        for i in range(lvl + 1):
            sum += 5 * i ** 2 + 50 * i * 5

        embed = discord.Embed(
            title = user.name,
            colour = 0x62ff00
        )
        embed.add_field(name = 'Ranga', value = f'#{rank}', inline = False)
        embed.add_field(name = 'Poziom', value = lvl)
        embed.add_field(name = 'XP', value = f'{exp}/{sum}')
        embed.set_thumbnail(url = user.avatar_url)
        embed.set_footer(text = f'Author {ctx.author}')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Rank(client))

async def leaderboard(member):
    query = users.find().sort('exp', -1)
    ranking = []

    for user in query:
        ranking.append(user['user'])

    for i in range(len(ranking)):
        if member.id == ranking[i]:
            rank = i + 1
            return rank
