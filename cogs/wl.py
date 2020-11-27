import discord

from discord.ext import commands


class Wl(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def wl(self, ctx, type, user: discord.Member = None):
        await ctx.message.delete()
        channel = self.client.get_channel(694652874109485216)
        interview_role = ctx.guild.get_role(780455138686271538)
        form_role = ctx.guild.get_role(693824755911884831)
        immigrant_role = ctx.guild.get_role(687689642664788021)
        citizen_role = ctx.guild.get_role(640182372289085452)

        if user is None:
            await ctx.channel.send(f'Musisz podać użytkownika do rozpatrzenia rozmowy', delete_after = 5)
        else:
            if interview_role in user.roles:
                await user.remove_roles(interview_role)

            if type == 'accept':
                await ctx.channel.send(f'{user.mention} udało ci się przejść rozmowę na wl!')
                if immigrant_role in user.roles:
                    await user.remove_roles(immigrant_role)
                if form_role in user.roles:
                    await user.remove_roles(form_role)
                if not citizen_role in user.roles:
                    await user.add_roles(citizen_role)

                embed = discord.Embed(
                    title = 'Rozmowa zatwierdzona',
                    colour = 0x00ff00
                )
                embed.add_field(name = 'WlChecker', value = ctx.author.mention)
                embed.add_field(name = 'Użytkownik', value = user.mention)

                await channel.send(embed = embed)
            if type == 'reject':
                await ctx.channel.send(f'{user.mention} niestety, nie udało ci się przejść rozmowę na wl.')

                embed = discord.Embed(
                    title = 'Rozmowa odrzucona',
                    colour = 0xff0000
                )
                embed.add_field(name = 'WlChecker', value = ctx.author.mention)
                embed.add_field(name = 'Użytkownik', value = user.mention)

                await channel.send(embed = embed)



def setup(client):
    client.add_cog(Wl(client))
