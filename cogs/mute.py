import re
import datetime
import asyncio
import discord

from discord.ext import commands

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f'{value} jest nieprawidłową jednostką czasu! h|m|s|d są poprawnymi'
                )
            except ValueError:
                raise commands.BadArgument(f'{key} is not a number!')
        return round(time)


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, user: discord.Member = None, time: TimeConverter = None, *, reason = None):
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

            await user.add_roles(muted_role, reason = reason)

            if not time:

                await ctx.channel.send(f'Zmutowano {user.mention}, Powód: {reason}')
                await user.send(f'Zostałeś zmutowany na **{ctx.guild.name}**, Powód: {reason}')

                embed = discord.Embed(
                    title = 'Użytkownik zmutowany',
                    colour = 0xff0000
                )
                embed.add_field(name = 'Moderator', value = ctx.author.mention)
                embed.add_field(name = 'Zmutowany', value = user.mention)
                embed.add_field(name = 'Powód', value = reason)

                await channel.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = 'Użytkownik zmutowany',
                    colour = 0xff0000
                )
                embed.add_field(name = 'Moderator', value = ctx.author.mention)
                embed.add_field(name = 'Zmutowany', value = user.mention)
                embed.add_field(name = 'Powód', value = reason)

                minutes, seconds = divmod(time, 60)
                hours, minutes = divmod(minutes, 60)

                if(int(hours)):
                    await ctx.channel.send(f'Zmutowano {user.mention}, na czas: {hours} godzin, {minutes} minut, i {seconds} sekund. Powód: {reason}')
                    await user.send(f'Zostałeś zmutowany na **{ctx.guild.name}**, na czas: {hours} godzin, {minutes} minut, i {seconds} sekund. Powód: {reason}')
                    embed.add_field(name = 'Czas', value = f'{hours} godzin, {minutes} minut, i {seconds} sekund')
                elif(int(minutes)):
                    await ctx.channel.send(f'Zmutowano {user.mention}, na czas: {minutes} minut, i {seconds} sekund. Powód: {reason}')
                    await user.send(f'Zostałeś zmutowany na **{ctx.guild.name}**, na czas: {minutes} minut, i {seconds} sekund. Powód: {reason}')
                    embed.add_field(name = 'Czas', value = f'{minutes} minut, i {seconds} sekund')
                elif(int(seconds)):
                    await ctx.channel.send(f'Zmutowano {user.mention}, na czas: {seconds} sekund. Powód: {reason}')
                    await user.send(f'Zostałeś zmutowany na **{ctx.guild.name}**, na czas: {minutes} minut, i {seconds} sekund. Powód: {reason}')
                    embed.add_field(name = 'Czas', value = f'{seconds} sekund')

                await channel.send(embed = embed)

                if time and time < 300:
                    await asyncio.sleep(time)

                if muted_role in user.roles:
                    await user.remove_roles(muted_role)
                    await ctx.send(f"Odmutowano {user.mention}")
                    embed = discord.Embed(
                        title = 'Użytkownik odmutowany',
                        colour = 0x00ff00
                    )
                    embed.add_field(name = 'Moderator', value = ctx.author.mention)
                    embed.add_field(name = 'Odmutowany', value = user.mention)

                    await channel.send(embed = embed)









def setup(client):
    client.add_cog(Mute(client))
