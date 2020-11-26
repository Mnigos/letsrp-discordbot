import discord

from discord.ext import commands


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, user: discord.Member = None, *, reason = None):
        muted_role = discord.utils.get(ctx.guild.roles,  name = 'muted')

        if not muted_role:
            muted_role = await ctx.guild.create_role(name = 'muted')

            for channel in ctx.guild.channels:
                await channel.set_permisions(muted_role, speak = False, send_messages = False, read_message_history = True, read_messages = True)

        if user is None:
            await ctx.message.delete()
            await ctx.channel.send(f"Sorry, You've to specify user to mute", delete_after = 5)
        else:
            if reason is not None:
                await ctx.message.delete()
                await ctx.channel.send(f'Muted {user.mention}, for: {reason}')
                await user.add_roles(muted_role, reason = reason)
                await user.send(f'You were muted in **{ctx.guild.name}**, for: {reason}')
            else:
                await ctx.message.delete()
                await ctx.channel.send(f'Muted {user.mention}, for: No reason')
                await user.add_roles(muted_role, reason = 'No reason given')
                await user.send(f'You were muted in **{ctx.guild.name}**, for: No reason given')




def setup(client):
    client.add_cog(Mute(client))
