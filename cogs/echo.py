import discord

from discord.ext import commands


class Echo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def echo(self, ctx, *, args):
        await ctx.message.delete()
        await ctx.channel.send(args)


def setup(client):
    client.add_cog(Echo(client))
