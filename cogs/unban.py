import discord

from discord.ext import commands


class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.Member = None):

        if user is None:
            await ctx.message.delete()
            await ctx.channel.send(f"Sorry, You've to specify user to unban", delete_after = 5)
        else:
            await ctx.message.delete()
            await ctx.channel.send(f'Unbanned {user.mention}')
            await user.send(f'You were Unbanned in **{ctx.guild.name}**, for: No reason given')
            await user.Unban()





def setup(client):
    client.add_cog(Unban(client))
