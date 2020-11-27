import discord

from discord.ext import commands


class Unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        channel = self.client.get_channel(694652874109485216)

        if user is None:
            await ctx.channel.send(f"Musisz podać użytkownika do odbanowania", delete_after = 5)
        else:
            await ctx.message.delete()
            await ctx.channel.send(f'Odbanowano {user.mention}')
            await user.Unban()

            embed = discord.Embed(
                title = 'Użytkownik odbanowany',
                colour = 0x00ff00
            )
            embed.add_field(name = 'Moderator', value = ctx.author.mention)
            embed.add_field(name = 'Odbanowany', value = user.mention)

            await channel.send(embed = embed)


def setup(client):
    client.add_cog(Unban(client))
