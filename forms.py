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
            await user.add_roles(role)
            db.wlforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})


    if wl_form_rejected is not None:
        dc = wl_form_rejected['dc']
        reason = wl_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Whitelist zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Whitelist',
                description = f'''Twoje podanie {user.mention} na Whitelist zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
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
        dc = sup_form_rejected['dc']
        reason = sup_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Supporta zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Supporta',
                description = f'''Twoje podanie {user.mention} na Supporta zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.supforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # Firm forms

    firm_form_accepted = db.firmforms.find_one({ 'status': 'accepted' })
    firm_form_rejected = db.firmforms.find_one({ 'status': 'rejected' })

    if firm_form_accepted is not None:
        dc = firm_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Firmę',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Firmę zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Firmę',
                description = f'''Twoje podanie {user.mention} na Firmę zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.firmforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if firm_form_rejected is not None:
        dc = firm_form_rejected['dc']
        reason = firm_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Firmę',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Firmę zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Firmę',
                description = f'''Twoje podanie {user.mention} na Firmę zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.firmforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # Org forms

    org_form_accepted = db.orgforms.find_one({ 'status': 'accepted' })
    org_form_rejected = db.orgforms.find_one({ 'status': 'rejected' })

    if org_form_accepted is not None:
        dc = org_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Organizację przestępczą',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Organizację przestępczą zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Organizację przestępczą',
                description = f'''Twoje podanie {user.mention} na Organizację przestępczą zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.orgforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if org_form_rejected is not None:
        dc = org_form_rejected['dc']
        reason = org_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Organizację przestępczą',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Organizację przestępczą zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Organizację przestępczą',
                description = f'''Twoje podanie {user.mention} na Organizację przestępczą zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.orgforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # EMS forms

    ems_form_accepted = db.emsforms.find_one({ 'status': 'accepted' })
    ems_form_rejected = db.emsforms.find_one({ 'status': 'rejected' })

    if ems_form_accepted is not None:
        dc = ems_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na frakcję EMS',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na frakcję EMS zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na frakcję EMS',
                description = f'''Twoje podanie {user.mention} na frakcję EMS zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.emsforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if ems_form_rejected is not None:
        dc = ems_form_rejected['dc']
        reason = ems_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na frakcję EMS',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na frakcję EMS zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na frakcję EMS',
                description = f'''Twoje podanie {user.mention} na frakcję EMS zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.emsforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # LSPD forms

    lspd_form_accepted = db.lspdforms.find_one({ 'status': 'accepted' })
    lspd_form_rejected = db.lspdforms.find_one({ 'status': 'rejected' })

    if lspd_form_accepted is not None:
        dc = lspd_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na frakcję LSPD',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na frakcję LSPD zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na frakcję LSPD',
                description = f'''Twoje podanie {user.mention} na frakcję LSPD zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.lspdforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if lspd_form_rejected is not None:
        dc = lspd_form_rejected['dc']
        reason = lspd_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na frakcję LSPD',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na frakcję LSPD zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na frakcję LSPD',
                description = f'''Twoje podanie {user.mention} na frakcję LSPD zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.lspdforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})


    # LSCM forms

    lscm_form_accepted = db.lscmforms.find_one({ 'status': 'accepted' })
    lscm_form_rejected = db.lscmforms.find_one({ 'status': 'rejected' })

    if lscm_form_accepted is not None:
        dc = lscm_form_accepted['dc']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Mechanika',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Mechanika zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Mechanika',
                description = f'''Twoje podanie {user.mention} na Mechanika zostało zaakceptowane.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0x00ff00
            )
            await channel.send(embed = embed)
            await channel.send(user.mention)


        db.lscmforms.update_one({ 'dc': dc }, { '$set': { 'status': 'acceptedSent' }})
        await client.add_roles(user, role)


    if lscm_form_rejected is not None:
        dc = lscm_form_rejected['dc']
        reason = lscm_form_rejected['reason']
        user = guild.get_member_named(dc)

        if user is None:
            embed = discord.Embed(
                title = 'Podanie na Mechanika',
                description = f'''Twoje podanie (Nie znaleziono użytkownika) na Mechanika zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
        else:
            embed = discord.Embed(
                title = 'Podanie na Mechanika',
                description = f'''Twoje podanie {user.mention} na Mechanika zostało odrzucone.
                Zgłoś się jak najszybciej na rozmowę!''',
                colour = 0xff0000
            )
            embed.add_field(name = 'Powód:', value = f'{reason}')
            await channel.send(embed = embed)
            await channel.send(user.mention)

        db.lscmforms.update_one({ 'dc': dc }, { '$set': { 'status': 'rejectedSent' }})
