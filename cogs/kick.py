import discord

from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member = None, *, reason = None):
        await ctx.message.delete()

        if user is None:

            await ctx.channel.send(f"Musisz podać użytkownika do wyrzucenia", delete_after = 5)
        else:
            if reason is None:
                reason = 'Nieznany'

            await ctx.channel.send(f'Wyrzucono {user.mention}, Powód: {reason}')
            await user.send(f'Zostałeś wyrzucony z **{ctx.guild.name}**, Powód: {reason}')
            await user.kick(reason = reason)




def setup(client):
    client.add_cog(Kick(client))
