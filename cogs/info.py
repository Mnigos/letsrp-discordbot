import discord

from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def info(self, ctx):
        await ctx.message.delete()

        embed = discord.Embed(
            title = "Informacje o Let's RP",
            colour = 0x62ff00
        )
        embed.add_field(name = 'IP serwera', value = 'wyspa.letsrp.pl')
        embed.add_field(name = 'Strona Internetowa', value = 'https://letsrp.pl/#/')
        embed.add_field(name = 'Jak połączyć się z serwerem', value = '''Wyszukaj w wyszukiwarce Let's RP,
                                                                        lub wciśnij F8 a następnie w konsoli wpisz `connect wyspa.letsrp.pl`''', inline = False)
        embed.set_footer(text = 'Nadal czegoś nie wiesz? Pisz do administracji')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Info(client))
