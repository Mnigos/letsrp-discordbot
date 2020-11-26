import discord

from discord.ext import commands


class Unmute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def unmute(self, ctx, user: discord.Member = None):
        muted_role = discord.utils.get(ctx.guild.roles,  name = 'muted')

        if user is None:
            await ctx.message.delete()
            await ctx.channel.send(f"Sorry, You've to specify user to unmute", delete_after = 5)
        else:
            await ctx.message.delete()
            await ctx.channel.send(f'Unmuted {user.mention}')
            await user.remove_roles(muted_role)
            await user.send(f'You were unmuted in {ctx.guild.name}')




def setup(client):
    client.add_cog(Unmute(client))
