import os
import discord

from discord.ext import commands
from pymongo import MongoClient
from random import randint

cluster = MongoClient(os.getenv('MONGO_URI'))
db = cluster['Letsrp-DiscordBot']
users = db.users


class Leveling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return

        random = 15 + randint(0, 10)

        await update_data(ctx.author)
        await add_exp(ctx.author, random)
        await level_up(ctx.author, ctx)


def setup(client):
    client.add_cog(Leveling(client))

async def update_data(user):
    query = users.find_one({ 'user': user.id })

    if not query:
        query = users.insert_one({ 'user': user.id, 'exp': 0, 'level': 1 })

async def add_exp(user, exp):
    query = users.find_one({ 'user': user.id })
    user_exp = query['exp']
    user_exp += exp

    users.update_one({ 'user': user.id }, { '$set': { 'exp': user_exp } })

async def level_up(user, message):
    query = users.find_one({ 'user': user.id })
    exp = query['exp']
    lvl = query['level']
    int_emotes = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    sum = 0

    for i in range(lvl + 1):
        sum += 5 * i ** 2 + 50 * i * 5

    if exp >= sum:
        lvl += 1
        users.update_one({ 'user': user.id }, { '$set': { 'level': lvl } })
        await message.add_reaction('🎉');

        for i in range(lvl):
            await message.add_reaction(int_emotes[int(str(lvl)[i:i+1])])
