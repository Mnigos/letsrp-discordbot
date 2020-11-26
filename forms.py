import discord

from discord.ext import commands, tasks

@tasks.loop(seconds = 2)
async def sending_forms(wlforms, client):
    channel = client.get_channel(694925226697556078)
    guild = client.get_guild(640178024280752158)
    role = guild.get_role(693824755911884831)

    formAccepted = wlforms.find_one({ 'status': 'accepted' })
    formRejected = wlforms.find_one({ 'status': 'rejected' })

    if formAccepted is not None:
        dc = formAccepted['dc']
        user = guild.get_member_named(dc)
        print(user)

        if user is not None:
            embed = discord.Embed(
                title = 'Podanie Whitelist',
                description = f'''Twoje podanie {user.mention} na Whitelist zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            wlforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})

            await channel.send(embed = embed)
            await channel.send(user.mention)
            await client.add_roles(user, role)


    if formRejected is not None:
        name = formRejected['dc']
        reason = formRejected['reason']
        user = guild.get_member_named(dc)

        embed = discord.Embed(
            title = 'Podanie Whitelist',
            description = f'''Twoje podanie {name.mention} na Whitelist zostało odrzucone.
            Możesz napisac następne za 24h''',
            colour = 0xff0000
        )
        embed.add_field(name = 'Powód:', value = f'{reason}')
        wlforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})

        await channel.send(embed = embed)
        await channel.send(user.mention)
