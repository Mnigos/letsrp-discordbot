import discord

from discord.ext import commands

class Interview(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = self.client.get_guild(640178024280752158)
        interview_role = guild.get_role(780455138686271538)

        if after.channel:
            if after.channel.id == 695967154058690592 or after.channel.id == 695967176724578366 or after.channel.id == 695967207406043146:
                if after.channel.permissions_for(member) < discord.Permissions(permissions = 268435456):
                    await member.add_roles(interview_role, reason = 'Rozmowa Whitelist')


def setup(client):
    client.add_cog(Interview(client))
