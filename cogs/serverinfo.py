import discord

from discord.ext import commands
from fivem import FiveM

try:
    server = FiveM(ip = 'wyspa.letsrp.pl', port = 30120)
except:
    server = None


class Serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.message.delete()
        info = await server.get_server_info()

        if server is not None:
            embed = discord.Embed(
                title = info.hostname,
                colour = 0x00ff00
            )
            embed.add_field(name = 'IP Serwera', value = 'wyspa.letsrp.pl')
            embed.add_field(name = 'Status', value = 'Online')
        else:
            embed = discord.Embed(
                title = info.hostname,
                colour = 0xff0000
            )
            embed.add_field(name = 'IP Serwera', value = 'wyspa.letsrp.pl')
            embed.add_field(name = 'Status', value = 'Offline')


        embed.add_field(name = 'Graczy', value = f'{info.clients}/{info.max_clients}', inline = False)
        embed.set_footer(text = f'Author {ctx.author}')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Serverinfo(client))
