import discord

from discord.ext import commands


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, user: discord.Member = None, *, reason = None):
        muted_role = discord.utils.get(ctx.guild.roles,  name = 'muted')
        channel = self.client.get_channel(694652874109485216)

        await ctx.message.delete()

        if not muted_role:
            muted_role = await ctx.guild.create_role(name = 'muted')

            for channel in ctx.guild.channels:
                await channel.set_permisions(muted_role, speak = False, send_messages = False, read_message_history = True, read_messages = True)

        if user is None:
            await ctx.channel.send(f"Musisz podać użytkownika do zmutowania", delete_after = 5)
        else:
            if reason is None:
                reason = 'Nieznany'

            await ctx.channel.send(f'Zmutowano {user.mention}, Powód: {reason}')
            await user.add_roles(muted_role, reason = reason)
            await user.send(f'Zostałeś zmutowany na **{ctx.guild.name}**, Powód: {reason}')

            embed = discord.Embed(
                title = 'Użytkownik zmutowany',
                colour = 0xff0000
            )
            embed.add_field(name = 'Moderator', value = ctx.author.mention)
            embed.add_field(name = 'Zmutowany', value = user.mention)
            embed.add_field(name = 'Powód', value = reason)

            await channel.send(embed = embed)




def setup(client):
    client.add_cog(Mute(client))
