import discord

from discord.ext import commands, tasks

@tasks.loop(seconds = 2)
async def sending_forms(wlforms, client):
    channel = client.get_channel(694925226697556078)
    formAccepted = wlforms.find_one({ 'status': 'accepted' })
    formRejected = wlforms.find_one({ 'status': 'rejected' })

    if formAccepted is not None:
        print('e')
        dc = formAccepted['dc']
        guild = client.get_guild(640178024280752158)
        tag = dc[:dc.length[:-5]]
        user = discord.utils.get(guild.members, name = dc[:-5], discriminator = tag)

        embed = discord.Embed(
            title = 'Podanie Whitelist',
            description = f'''Twoje podanie {user} na Whitelist zostało zaakceptowane.
            Zgłoś się jak najszybciej na rozmowę!''',
            colour = 0x00ff00
        )

        await channel.send(embed = embed)
        await channel.send(user.mention)
        formAccepted.update({ 'status': 'acceptedSent' })

    if formRejected is not None:
        name = formRejected['dc']
        reason = formRejected['reason']
        guild = client.get_guild(640178024280752158)
        tag = dc[:dc.length[:-5]]
        user = discord.utils.get(guild.members, name = dc[:-5], discriminator = tag)

        embed = discord.Embed(
            title = 'Podanie Whitelist',
            description = f'''Twoje podanie {name} na Whitelist zostało odrzucone.
            Możesz napisac następne za 24h''',
            colour = 0xff0000
        )
        embed.add_field(name = 'Powód:', value = f'{reason}')

        await channel.send(embed = embed)
        await channel.send(user.mention)
        formAccepted.update({ 'status': 'rejectedSent' })
