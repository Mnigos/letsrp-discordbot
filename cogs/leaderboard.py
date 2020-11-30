import os
import discord

from discord.ext import commands
from pymongo import MongoClient
from random import randint

cluster = MongoClient(os.getenv('MONGO_URI'))
db = cluster['Letsrp-DiscordBot']
users = db.users

class Leaderboard(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def leaderboard(self, ctx):
        await ctx.message.delete()
        query = users.find().sort('exp', -1)
        ranking = []

        for user in query:
            ranking.append(user['user'])

        embed = discord.Embed(
            title = f'Tablica wyników servera {ctx.guild.name}',
            colour = 0x62ff00
        )

        for i in range(len(ranking)):
            user = users.find_one({ 'user': ranking[i] })
            sum = 0

            for j in range(user['level'] + 1):
                sum += 5 * j ** 2 + 50 * j * 5

            embed.add_field(name = '᲼', value = f'''**{i + 1}.** {ctx.guild.get_member(user["user"]).mention} ({ctx.guild.get_member(user["user"])})
                                                Poziom: **{user["level"]}** Exp: **{user["exp"]}/{sum}**''', inline = False)

        embed.set_footer(text = f'Author {ctx.author}')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Leaderboard(client))

async def leaderboard(member):
    query = users.find().sort('exp', -1)
    ranking = []

    for user in query:
        ranking.append(user['user'])

    for i in range(len(ranking)):
        if member.id == ranking[i]:
            rank = i + 1
            return rank
