import discord

from discord.ext import commands


class Botinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def botinfo(self, ctx):
        await ctx.message.delete()

        embed = discord.Embed(
            title = "Informacje o bocie Let's RP",
            colour = 0x62ff00
        )
        embed.add_field(name = 'Repozytorium', value = 'https://github.com/MoneyIgos/letsrp-discordbot')
        embed.add_field(name = 'język', value = 'Python')
        embed.set_thumbnail(url = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fc%2Fc3%2FPython-logo-notext.svg%2F1200px-Python-logo-notext.svg.png&f=1&nofb=1')
        embed.set_footer(text = 'Stworzyny przez MoneyIgos#2000')

        await ctx.channel.send(embed = embed)


def setup(client):
    client.add_cog(Botinfo(client))
