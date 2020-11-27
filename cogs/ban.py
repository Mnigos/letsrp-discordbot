import discord

from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None, *, reason = None):
        await ctx.message.delete()
        channel = self.client.get_channel(694652874109485216)

        if user is None:
            await ctx.channel.send(f"Musisz podać użytkownika do zbanowania", delete_after = 5)
        else:
            if reason is None:
                reason = 'Nieznany'

            await ctx.channel.send(f'Zbanowano {user.mention}, Powód: {reason}')
            await user.send(f'Zostałeś zbanowany na **{ctx.guild.name}**, Powód: {reason}')
            await user.kick(reason = reason)

            embed = discord.Embed(
                title = 'Użytkownik zbanowany',
                colour = 0xff0000
            )
            embed.add_field(name = 'Moderator', value = ctx.author.mention)
            embed.add_field(name = 'Zbanowany', value = user.mention)
            embed.add_field(name = 'Powód', value = reason)

            await channel.send(embed = embed)


def setup(client):
    client.add_cog(Ban(client))
