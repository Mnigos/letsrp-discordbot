import discord

from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None, *, reason = None):

        if user is None:
            await ctx.message.delete()
            await ctx.channel.send(f"Sorry, You've to specify user to ban", delete_after = 5)
        else:
            if reason is not None:
                await ctx.message.delete()
                await ctx.channel.send(f'Banned {user.mention}, for: {reason}')
                await user.send(f'You were banned in {ctx.guild.name}, for: {reason}')
                await user.kick(reason = reason)
            else:
                await ctx.message.delete()
                await ctx.channel.send(f'Banned {user.mention}, for: No reason')
                await user.send(f'You were banned in {ctx.guild.name}, for: No reason given')
                await user.ban(reason = 'No reason given')





def setup(client):
    client.add_cog(Ban(client))
