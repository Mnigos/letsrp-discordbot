import discord

from discord.ext import commands, tasks

@tasks.loop(seconds = 2)
async def sending_forms(db, client):
    channel = client.get_channel(694925226697556078)
    guild = client.get_guild(640178024280752158)


    # Whitelist forms

    role = guild.get_role(693824755911884831)

    wl_form_accepted = db.wlforms.find_one({ 'status': 'accepted' })
    wl_form_rejected = db.wlforms.find_one({ 'status': 'rejected' })

    if wl_form_accepted is not None:
        dc = wl_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Whitelist zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie {user.mention} na Whitelist zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)
            await client.add_roles(user, role)
            db.wlforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})


    if wl_form_rejected is not None:
        name = wl_form_rejected['dc']
        reason = wl_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Whitelist zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie {user.mention} na Whitelist zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)
        db.wlforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # Support forms

    sup_form_accepted = db.supforms.find_one({ 'status': 'accepted' })
    sup_form_rejected = db.supforms.find_one({ 'status': 'rejected' })

    if sup_form_accepted is not None:
        dc = sup_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Supporta zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie {user.mention} na Supporta zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.supforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if sup_form_rejected is not None:
        name = sup_form_rejected['dc']
        reason = sup_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Supporta zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie {user.mention} na Supporta zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.supforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})
