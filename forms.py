import discord

from discord.ext import commands, tasks

@tasks.loop(seconds = 2)
async def sending_forms(wlforms, client):
    channel = client.get_channel(694925226697556078)
    formAccepted = wlforms.find_one({ 'status': 'accepted' })
    formRejected = wlforms.find_one({ 'status': 'rejected' })

    if formAccepted is not None:
        print('e')
        name = formAccepted['dc']

        embed = discord.Embed(
            title = 'Podanie WL',
            description = f'''Twoje podanie {name} na Whitelist zostało zaakceptowane.
            Zgłoś się jak najszybciej na rozmowę!''',
            colour = 0x00ff00
        )

        await channel.send(embed = embed)

    if formRejected is not None:
        name = formRejected['dc']
        reason = formRejected['reason']

        embed = discord.Embed(
            title = 'Podanie WL',
            description = f'''Twoje podanie {name} na Whitelist zostało odrzucone.
            Możesz napisac następne za 24h''',
            colour = 0xff0000
        )
        embed.add_field(name = 'Powód:', value = f'{reason}')

        await channel.send(embed = embed)
