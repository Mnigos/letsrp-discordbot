import discord

from discord.ext import commands
from fivem import FiveM

server = FiveM(ip = 'wyspa.letsrp.pl', port = 30120)


class Getplayers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def getplayers(self, ctx):
        await ctx.message.delete()
        info = await server.get_server_info()
        players = await server.get_players()

        embed = discord.Embed(
            title = "Aktualnie aktywni gracze na Let's RP",
            colour = 0x62ff00,
            description = f'Graczy {info.clients}/{info.max_clients}'
        )

        id = ''
        name = ''
        dc = ''

        for player in players:
            id += f'{player.id}\n'
            name += f'{player.name}\n'
            dc += f'{self.client.get_user(int(player.discord_id)).mention}\n'

        embed.add_field(name = 'ID', value = id)
        embed.add_field(name = 'Nazwa', value = name)
        embed.add_field(name = 'Discord', value = dc)

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Getplayers(client))
