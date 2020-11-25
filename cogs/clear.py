import discord

from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=0):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        await ctx.channel.send(f'Deleted {amount} message(s)', delete_after=5)


def setup(client):
    client.add_cog(Clear(client))

