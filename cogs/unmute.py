import discord

from discord.ext import commands


class Unmute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def unmute(self, ctx, user: discord.Member = None):
        muted_role = discord.utils.get(ctx.guild.roles,  name = 'muted')
        await ctx.message.delete()

        if user is None:
            await ctx.channel.send(f"Musisz podać użytkownika do odmutowania", delete_after = 5)
        else:
            await ctx.channel.send(f'Odmutowano {user.mention}')
            await user.remove_roles(muted_role)
            await user.send(f'Zostałeś odmutowany na **{ctx.guild.name}**')




def setup(client):
    client.add_cog(Unmute(client))
