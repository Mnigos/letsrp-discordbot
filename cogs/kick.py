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

            await ctx.channel.send(f"Sorry, You've to specify user to kick", delete_after = 5)
        else:
            if reason is None:
                reason = 'Nieznany'

            await ctx.channel.send(f'Kicked {user.mention}, for: {reason}')
            await user.send(f'You were kicked in **{ctx.guild.name}**, for: {reason}')
            await user.kick(reason = reason)




def setup(client):
    client.add_cog(Kick(client))
