import discord

from discord.ext import commands
from fivem import FiveM

server = FiveM(ip = 'wyspa.letsrp.pl', port = 30120)


class Serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.message.delete()
        info = await server.get_server_info()

        embed = discord.Embed(
            title = info.hostname,
            colour = 0x62ff00
        )
        embed.add_field(name = 'IP Serwera', value = 'wyspa.letsrp.pl')
        embed.add_field(name = 'Graczy', value = f'{info.clients}/{info.max_clients}')
        embed.set_footer(text = f'Author {ctx.author.mention}')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Serverinfo(client))
