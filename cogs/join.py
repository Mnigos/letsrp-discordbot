import os
import discord

from discord.ext import commands

class Join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.client.get_guild(640178024280752158)
        role = guild.get_role(687689642664788021)
        await member.add_roles(role, reason = 'User joined')


def setup(client):
    client.add_cog(Join(client))
