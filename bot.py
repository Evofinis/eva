# -*- coding: utf-8 -*-

import asyncio
import datetime
import re
import discord
from discord.ext import commands
import random
import json
import requests
from discord.ext.commands import CheckFailure, MissingRequiredArgument, BadArgument
# import pymysql
import pymysql
from discord.utils import get

TOKEN = 'NDkyODEwNzc3ODI5NTcyNjE4.Dob6Hw.hdJzZRQAR2JigrrKbtvWBk6m5FE'

api_auth = {
    'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTY4MCwiaWR"
            "lbiI6IjE0NTMzODMyNzAzMjI2Njc1MiIsIm1kIjp7InVzZXJuYW1lIjoiRXZvIiwia2V5VmVyc2lvbiI6MywiZGl"
            "zY3JpbWluYXRvciI6IjczMDcifSwidHMiOjE1NDQ4MjY0MzI4MTR9.BOp7L1NQrNv_t432VjeXAqGRgsW-KhNcKq7CBWDH9YM"
}

client = commands.Bot(command_prefix='*')
client.remove_command('help')

dv = discord.__version__


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with Elitists Clan Family'))
    await client.send_message(client.get_channel('492836977335599107'), "Good Morning Master! :kissing_closed_eyes:")
    print("Discord Version: " + dv)


@client.command(pass_context=True)
async def rolemems(ctx, *, r):
    role = discord.utils.get(ctx.message.author.server.roles, name=r)
    memlist = ctx.message.author.server.members

    if 'None' in str(role):
        await client.say("It seems I can't find that role. Please note that roles are __**case sensitive**__")
        return

    await client.say("These members have the __**" + str(role) + "**__ role:")
    for member in memlist:
        if role in member.roles:
            await client.say(member.name)


@client.command(pass_context=True)
@commands.has_any_role('Server Mod', 'Founder', 'Recruiter (CR)')
async def purge(ctx, number=30):
    number = int(number)
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit=number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            # await asyncio.sleep(0.2)


@purge.error
async def check_failure_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Leave this command to the Server Mods :wink: '
                                                               '' + ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
async def bo3(ctx, t, l):
    number = 1

    time = ""
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit=number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            # await asyncio.sleep(0.2)

    if l.lower() == 'h':
        time = "Hours"
    elif l.lower() == 'm':
        time = "Minutes"
    else:
        await client.send_message(ctx.message.author, "Please ensure that you have entered your time "
                                                      "as `H` for hours or `M` for minutes " +
                                  ctx.message.author.mention)
        await client.send_message(ctx.message.author, "Example: `*bo3 3 h` " + ctx.message.author.mention)
        return

    await client.send_message(client.get_channel('536612187226112035'), "__**New battle request has "
                                                                        "been posted <@&537315150009466880>!**__\n")
    await client.send_message(client.get_channel('536612187226112035'),
                              "**Player:** " + ctx.message.author.display_name)
    await client.send_message(client.get_channel('536612187226112035'), "**Availability:** " + t + " " + time)
    await client.send_message(client.get_channel('536612187226112035'), "**Battle Type:** Best of 3")
    await client.send_message(client.get_channel('536612187226112035'), "__**Please DM " + ctx.message.author.mention +
                              " for more info or friend link**__")


@bo3.error
async def missing_req_args(error, ctx):
    if isinstance(error, MissingRequiredArgument):
        number = 1
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit=number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
                # await asyncio.sleep(0.2)
        await client.send_message(ctx.message.author, content='Your command is incomplete. Please try again :wink: '
                                                              + ctx.message.author.mention)
        await client.send_message(ctx.message.author, content='Example: `*bo3 3 h` '
                                                              + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        number = 1
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit=number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
async def bo5(ctx, t, l):
    number = 1

    time = ""
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit=number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            # await asyncio.sleep(0.2)

    if l.lower() == 'h':
        time = "Hours"
    elif l.lower() == 'm':
        time = "Minutes"
    else:
        await client.send_message(ctx.message.author, "Please ensure that you have entered your time "
                                                      "as `H` for hours or `M` for minutes " +
                                  ctx.message.author.mention)
        await client.send_message(ctx.message.author, "Example: `*bo5 3 h` " + ctx.message.author.mention)
        return

    await client.send_message(client.get_channel('537750598662225940'), "__**New battle request has "
                                                                        "been posted <@&537315150009466880>!**__\n")
    await client.send_message(client.get_channel('537750598662225940'),
                              "**Player:** " + ctx.message.author.display_name)
    await client.send_message(client.get_channel('537750598662225940'), "**Availability:** " + t + " " + time)
    await client.send_message(client.get_channel('537750598662225940'), "**Battle Type:** Best of 5")
    await client.send_message(client.get_channel('537750598662225940'), "__**Please DM " + ctx.message.author.mention +
                              " for more info or friend link**__")


@bo5.error
async def missing_req_args(error, ctx):
    if isinstance(error, MissingRequiredArgument):
        number = 1
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit=number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
                # await asyncio.sleep(0.2)
        await client.send_message(ctx.message.author, content='Your command is incomplete. Please try again :wink: '
                                                              + ctx.message.author.mention)
        await client.send_message(ctx.message.author, content='Example: `*bo5 3 h` '
                                                              + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        number = 1
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit=number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
@commands.has_any_role('Recruiter (CR)', 'Founder')
async def wladd(ctx, player, t, c):
    try:
        db = pymysql.connect(host="localhost",  # your host, usually localhost
                             user="evo",  # your username
                             passwd="dwaynemhb1",  # your password
                             db="discord")  # name of the data base

        cur = db.cursor()
        sql = "INSERT INTO waitlist VALUES (%s, %s, %s, %s)"
        val = (0, player, t, c)
        cur.execute(sql, val)
        db.commit()
        cur.close()
        db.close()
        await client.say(player + ' | ' + t + ' has been added to the Waiting List ' + ctx.message.author.mention)
    except pymysql.Error:
        await client.say(
            "There is already a player with that **tag** on the Waiting List " + ctx.message.author.mention)


@wladd.error
async def check_failure_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Baka! This command cannot be used by the likes of '
                                                               'you!!! :angry: ' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel, content='Please ensure that you have entered a **Name**, '
                                                               '**Tag** and **Clan** for this player :thinking: ' +
                                                               ctx.message.author.mention)
        await client.send_message(ctx.message.channel, content='**Example:** `*wladd Username #Tag Clan` ' +
                                                               ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
@commands.has_any_role('Recruiter (CR)', 'Founder')
async def wldel(ctx, t):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()
    val = t

    userlookup = ("SELECT * FROM waitlist where tag = %s")
    rc = cur.execute(userlookup, (val,))

    if rc > 0:
        for player in cur.fetchall():
            playername = player[1]
            ptag = player[2]

            userdelete = "DELETE FROM waitlist WHERE tag = %s"

            cur.execute(userdelete, (val,))
            db.commit()
            await client.say("As you wish. Bye bye **" + playername + " | " + ptag + "**! :smiling_imp: "
                             + ctx.message.author.mention)
            cur.close()
            db.close()
    else:
        await client.say("Player does not exist " + ctx.message.author.mention)
        cur.close()
        db.close()


@wldel.error
async def check_failure_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Baka! This command cannot be used by the likes of '
                                                               'you!!! :angry: ' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel, content='Please ensure that you have entered a '
                                                               '**Tag** for the player :thinking: ' +
                                                               ctx.message.author.mention)
        await client.send_message(ctx.message.channel, content='**Example:** `*wldel #Tag` ' +
                                                               ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
@commands.has_any_role('Recruiter (CR)', 'Founder')
async def showwl(ctx, c):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()
    val = c.lower()

    if val == "all":

        sql = ("SELECT * FROM waitlist")
        rc = cur.execute(sql)
        await client.say("**Elitists Clan Family Waiting List:** \n")

        if rc > 0:
            for player in cur.fetchall():
                await client.say(
                    "**" + player[1] + " | " + player[2] + "** is waiting to join **" + player[3]
                    + ".**\n")
        else:
            await client.say("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBIF7jDQ_DM_"
                             "dpelWOWzjf4p2BxYzNJ2jToJErwF_dAraW5Fm5lg " + ctx.message.author.mention)
    else:
        sql = "SELECT * FROM waitlist WHERE clan = %s"
        rc = cur.execute(sql, (val,))

        await client.say("**__" + c.upper() + "__ Waiting List:** \n")

        if rc > 0:
            for player in cur.fetchall():
                await client.say(
                    "**" + player[1] + " | " + player[2] + "**")
        else:
            await client.say("There are no players on the Waiting List for Main")
            await client.say("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBIF7jDQ_DM_"
                             "dpelWOWzjf4p2BxYzNJ2jToJErwF_dAraW5Fm5lg " + ctx.message.author.mention)
    db.close()
    cur.close()


@showwl.error
async def check_failure_error(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Baka! This command cannot be used by the likes of '
                                                               'you!!! :angry: ' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel, content='Please ensure that you have entered a '
                                                               '**Clan** for the player :thinking: ' +
                                                               ctx.message.author.mention)
        await client.send_message(ctx.message.channel, content='**Example:** `*wldel Clan` ' +
                                                               ctx.message.author.mention)
    raise error


@client.command(pass_context=True)
@commands.has_any_role('Elite Cookie Distributor', 'Elite Boy Scout', 'Founder')
async def givecookie(ctx, user: discord.Member, n=1):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()

    sql = ("SELECT * FROM cookie_jar WHERE name = %s ")
    rc = cur.execute(sql, (user,))

    if rc == 0:
        sql2 = ("INSERT INTO cookie_jar VALUES (%s, %s, %s, %s)")
        values = (0, user, user.display_name, n)

        cur.execute(sql2, values)
        db.commit()

        await client.send_message(ctx.message.channel, "Hooray! You finally got some cookies " + user.mention)
        await client.send_message(ctx.message.channel, user.display_name + " now has " + str(n) + " cookies")
    else:
        retrieve_cookies = ("SELECT cookies FROM cookie_jar WHERE name = %s")
        cookie = cur.execute(retrieve_cookies, (user,))

        for c in cur.fetchall():
            cookie = c[0]

        print(str(cookie))

        new_cookies = int(cookie) + int(n)

        add_cookies = ("UPDATE cookie_jar SET cookies = %s WHERE name = %s ")
        cur.execute(add_cookies, (new_cookies, user,))
        db.commit()

        await client.send_message(ctx.message.channel, user.display_name + " now has " + str(new_cookies) + " cookies")

    db.close()
    cur.close()


@givecookie.error
async def give_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)


@client.command(pass_context=True)
@commands.has_any_role('Elite Cookie Distributor', 'Elite Boy Scout', 'Founder')
async def takecookie(ctx, user: discord.Member, n=1):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()

    sql = ("SELECT * FROM cookie_jar WHERE name = %s ")
    rc = cur.execute(sql, (user,))

    if rc == 0:
        await client.send_message(ctx.message.channel, user.display_name +
                                  " has no cookies <:crbarbyell:488201230552793089>")
        await client.send_message(ctx.message.channel, "Want to give " + user.display_name +
                                  " a cookie so you can **take it away**? :wink:")
    else:
        retrieve_cookies = ("SELECT cookies FROM cookie_jar WHERE name = %s")
        cookie = cur.execute(retrieve_cookies, (user,))

        for c in cur.fetchall():
            cookie = c[0]

        if n > int(cookie):
            await client.send_message(ctx.message.channel, "Woah slow down! " + user.display_name +
                                      " doesn't have all those cookies <a:gifcrpiglol:502560617735913492>")

            return
        else:
            new_cookies = int(cookie) - int(n)

            del_cookies = ("UPDATE cookie_jar SET cookies = %s WHERE name = %s ")
            cur.execute(del_cookies, (new_cookies, user,))
            db.commit()

            await client.send_message(ctx.message.channel, user.display_name +
                                      " now has " + str(new_cookies) + " cookies")

    db.close()
    cur.close()


@takecookie.error
async def take_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)


@client.command(pass_context=True)
async def cookielb(ctx, c=5):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()

    n = 0

    sql = ("SELECT display_name, cookies FROM cookie_jar ORDER BY CAST(cookies AS UNSIGNED) DESC")
    rc = cur.execute(sql)

    if rc == 0:
        await client.send_message(ctx.message.channel,
                                  "No one has any cookies. How sad.")
    else:
        await client.send_message(ctx.message.channel,
                                  "<:blobcookie:539901328118382632> **Elitists Top Cookie Monsters**"
                                  " <:blobcookie:539901328118382632>")

        for player in cur.fetchall():
            display_name = player[0]
            cookie_count = player[1]

            n = n + 1
            if n > c:
                return
            else:
                await client.send_message(ctx.message.channel, str(n) + ". " + display_name + " has "
                                          + cookie_count + " :cookie:")

    db.close()
    cur.close()


@cookielb.error
async def lb_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)


@client.command(pass_context=True)
async def donate(ctx):
    await client.say(
        "Here's the link to make a donation to the **Elitists Clan Family**: https://bit.ly/2Lqfuuy " + ctx.message.author.mention)


@client.command(pass_context=True)
async def kill(ctx):
    if "founder" in [y.name.lower() for y in ctx.message.author.roles]:
        await client.say('Bye bye Master. :hearts:')
        await client.logout()
        return
    await client.say("You do not have the required privileges to use this command " + ctx.message.author.mention)


@client.command(pass_context=True)
@commands.has_any_role('Recruiter (CR)', 'Founder')
async def getstats2(ctx, user: discord.Member, t, change):
    try:
        author = ctx.message.author
        tag = t
        tag = re.sub("[#]", "", tag)
        player_url = "https://api.royaleapi.com/player/" + tag

        response = requests.request("GET", player_url, headers=api_auth)

        # Convert the response (in a text format) into a py dict
        data = json.loads(response.text)

        # Assign variables based on the data loaded
        name = data["name"]

        level = data["stats"]["level"]
        current_trophies = data["trophies"]
        personal_best = data["stats"]["maxTrophies"]
        war_wins = data["games"]["warDayWins"]
        tot_donations = data["stats"]["totalDonations"]
        col_day = data["stats"]["clanCardsCollected"]
        max_wins = data["stats"]["challengeMaxWins"]
        arena = data["arena"]["arenaID"]
        try:
            current_clan = data["clan"]["name"]
        except Exception as e:
            current_clan = "None"

        # Get icon functions
        arena_icon = get_arena_icon(arena)
        pb_icon = get_pb_icon(personal_best)
        trophy_img = get_trophy_image(current_trophies)
        level_icon = get_level_icon(level)

        # Change the user's name if desired
        if change.lower() == 'y':
            await client.send_message(author, "** " + str(user) + "'s** name has been changed to their IGN which is: `"
                                      + str(name) + "`. " + author.mention)
            await client.change_nickname(user, name)
        elif change.lower() == 'n':
            print('Name not changed.')
        else:
            await client.say("Please specify `Y` or `N` when using this command. " + author.mention)
            return

        # Created embed
        embed = discord.Embed()

        embed.set_footer(text='This bot was designed by Evo#7307')
        embed.set_thumbnail(url=arena_icon)
        embed.set_author(name=name + " | #" + tag, icon_url=level_icon)
        embed.add_field(name='Trophies', value=trophy_img + ' `' + str(current_trophies) + "`", inline=True)
        embed.add_field(name='Personal Best', value=pb_icon + " `" + str(personal_best) + "`", inline=True)
        embed.add_field(name='Total Donations', value='<:donations:554329813381283840> `' + str(tot_donations) + "`",
                        inline=True)
        embed.add_field(name='War Day Wins', value='<:cwwarwin:554328276718452736> `' + str(war_wins) + "`", inline=True)
        embed.add_field(name='Clan Cards Collected', value='<:cwcards:554328404477083648> `' + str(col_day) + "`",
                        inline=True)
        embed.add_field(name='Challenge Wins', value='<:maxwins:554328287304745002> `' + str(max_wins) + "`", inline=True)

        # Create an array to hold the different card leagues
        leagues = ['Legendary', 'Gold', 'Silver', 'Bronze', 'UL']

        # Images stored into lists based on the league passed into the function
        ll_card_imgs = get_league_stats(tag, leagues[0])
        gl_card_imgs = get_league_stats(tag, leagues[1])
        sl_card_imgs = get_league_stats(tag, leagues[2])
        bl_card_imgs = get_league_stats(tag, leagues[3])
        ul_card_imgs = get_league_stats(tag, leagues[4])

        # Running count of how many cards the player has in each league
        leg_count = get_league_stats_count(tag, leagues[0])
        gold_count = get_league_stats_count(tag, leagues[1])
        silver_count = get_league_stats_count(tag, leagues[2])
        bronze_count = get_league_stats_count(tag, leagues[3])
        uderlev_count = get_league_stats_count(tag, leagues[4])

        # Neat lil code I found that adds a blank space into an embed
        embed.add_field(name='_ _',
                        value='_ _',
                        inline=False)

        # Conditional statements that determine what gets placed into the embed
        if uderlev_count > 35:
            uderlev_count_remain = uderlev_count - 35

            embed.add_field(
                name='<:crspikeshock:556468230156320770> Unloved Cards ' + str(uderlev_count) + "/91",
                value=(''.join(map(str, ul_card_imgs))) + " (+ **" + str(uderlev_count_remain) + "**)",
                inline=False)
        elif uderlev_count > 0 & uderlev_count < 35:
            embed.add_field(
                name='<:crspikeshock:556468230156320770> Unloved Cards ' + str(uderlev_count) + "/91",
                value=(''.join(map(str, ul_card_imgs))), inline=False)

        # The embed will only have a title if the player has no cards that fit the league's required level
        # else:
        #     embed.add_field(
        #         name='<:crspikeshock:556468230156320770> Unloved Cards ' + "0/91",
        #         value='_ _', inline=False)

        embed.add_field(name='_ _',
                        value='_ _',
                        inline=False)

        if bronze_count > 35:
            bronze_count_remain = bronze_count - 35

            embed.add_field(
                name='<:clanwars_league_bronze:556458077860397086> Bronze League Cards ' + str(bronze_count) + "/91",
                value=(''.join(map(str, bl_card_imgs))) + " (+ **" + str(bronze_count_remain) + "**)",
                inline=False)
        elif bronze_count > 0 & bronze_count < 35:
            embed.add_field(
                name='<:clanwars_league_bronze:556458077860397086> Bronze League Cards ' + str(bronze_count) + "/91",
                value=(''.join(map(str, bl_card_imgs))), inline=True)
        # else:
        #     embed.add_field(
        #         name='<:clanwars_league_bronze:556458077860397086> Bronze League Cards ' + "0/91",
        #         value='_ _', inline=False)

        embed.add_field(name='_ _',
                        value='_ _',
                        inline=False)

        if silver_count > 35:
            silver_count_remain = silver_count - 35

            embed.add_field(name='<:clanwars_league_silver:556458060286001152> Silver League Cards ' + str(silver_count) + "/91",
                            value=(''.join(map(str, sl_card_imgs))) + " (+ **" + str(silver_count_remain) + "**)",
                            inline=False)
        elif silver_count > 0 & silver_count < 35:
            embed.add_field(name='<:clanwars_league_silver:556458060286001152> Silver League Cards ' + str(silver_count) + "/91",
                            value=(''.join(map(str, sl_card_imgs))), inline=True)
        # else:
        #     embed.add_field(
        #         name='<:clanwars_league_silver:556458060286001152> Silver League Cards ' + "0/91",
        #         value='_ _', inline=False)

        embed.add_field(name='_ _',
                        value='_ _',
                        inline=False)

        if gold_count > 35:
            gold_count_remain = gold_count - 35

            embed.add_field(name='<:clanwars_league_gold:556458044502966291> Gold League Cards ' + str(gold_count) + "/91",
                            value=(''.join(map(str, gl_card_imgs))) + " (+ **" + str(gold_count_remain) + "**)", inline=False)
        elif gold_count > 0 & gold_count < 35:
            embed.add_field(name='<:clanwars_league_gold:556458044502966291> Gold League Cards ' + str(gold_count) + "/91",
                            value=(''.join(map(str, gl_card_imgs))), inline=False)
        # else:
        #     embed.add_field(
        #         name='<:clanwars_league_gold:556458044502966291> Gold League Cards ' + "0/91",
        #         value='_ _', inline=False)

        embed.add_field(name='_ _',
                        value='_ _',
                        inline=False)

        if leg_count > 35:
            leg_count_remain = leg_count - 35

            embed.add_field(name='<:clanwars_league_legendary:556458509005357066> Legendary League Cards ' + str(leg_count) + "/91",
                            value=(''.join(map(str, ll_card_imgs))) + " (+ **" + str(leg_count_remain) + "**)", inline=False)
        elif leg_count > 0 & leg_count < 35:
            embed.add_field(name='<:clanwars_league_legendary:556458509005357066> Legendary League Cards ' + str(leg_count) + "/91",
                            value=(''.join(map(str, ll_card_imgs))), inline=False)
        # else:
        #     embed.add_field(
        #         name='<:clanwars_league_legendary:556458509005357066> Legendary League Cards ' + "0/91",
        #         value='_ _', inline=False)

        # This statement will check to see if the player qualifies for the main clan
        main_clan_embed = discord.Embed()

        # embed.set_footer(text='This bot was designed by Evo#7307')
        main_clan_embed.set_thumbnail(url=arena_icon)
        main_clan_embed.set_author(name=name + " | #" + tag, icon_url=level_icon)
        main_clan_embed.add_field(name='Trophies', value=trophy_img + ' `' + str(current_trophies) + "`", inline=True)
        main_clan_embed.add_field(name='Personal Best', value=pb_icon + " `" + str(personal_best) + "`", inline=True)
        main_clan_embed.add_field(name='War Day Wins', value='<:cwwarwin:554328276718452736> `' + str(war_wins) + "`", inline=True)
        main_clan_embed.add_field(name='Current Clan', value='<:Sword_01:554343614113775633> `' + current_clan + "`", inline=True)

        if current_trophies > 4299:
            if personal_best > 4599:
                if war_wins > 60:
                    if leg_count > 10:
                        await client.send_message(author, '**' + name + ' | ' +
                                                  tag + ' meets the requirements to join Main** ' + author.mention)
                        await client.send_message(author, embed=main_clan_embed)

        await client.send_message(ctx.message.channel, embed=embed)
    except Exception as e:
        print(e)


@client.command(pass_context=True)
@commands.has_role('Server Mod')
async def mute(ctx, user: discord.Member):
    d = datetime.datetime.today()

    role = discord.utils.get(ctx.message.author.server.roles, name='All Chat Banned')
    await client.send_message(client.get_channel('527875324344664112'),
                              "**The following roles were removed from __" + user.display_name + "__**")
    for roles in user.roles:
        if "@everyone" in str(roles):
            continue
        else:
            await client.send_message(client.get_channel('527875324344664112'), "```" + str(roles) + "```")
    await client.replace_roles(user, role)
    await client.send_message(client.get_channel('527875324344664112'),
                              "**" + user.display_name + " was muted from all chat on __" + d.strftime(
                                  "%d-%B-%Y %H:%M") + "__**")
    await client.send_message(client.get_channel('527872953132777472'), 'Hello ' + user.mention
                              + ", you have been muted from all chat for repeatedly breaking the rules."
                                " Please contact a <@&514466546933039106> if you have any questions or if you believe "
                                "this was an error.")


# All Clans
# @client.command(pass_context=True)
# @commands.has_any_role('Founder')
# async def agree(ctx):
#     await client.send_message(client.get_channel('449364656855973888'),
#                               "Yea, I have feelings too.")


# All Clans
@client.command(pass_context=True)
@commands.has_any_role('Recruiter (CR)', 'Founder')
async def rcrt(ctx, c, user: discord.Member):
    clan = c.lower()

    if 'main' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists (Main)')
    elif 'royale' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists Royale')
    elif 'inc' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists Inc)')
    elif 'tavern' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists Tavern')
    elif 'canada' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists Canada')
    elif 'kinda' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Elitists Kinda')
    elif 'force' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Atma Force')
    elif 'folks' in clan:
        role = discord.utils.get(ctx.message.author.server.roles, name='Atma Folks')
    else:
        role = discord.utils.get(ctx.message.author.server.roles, name='Atma Forge')

    role2 = discord.utils.get(ctx.message.author.server.roles, name='Tournament Ping')
    role3 = discord.utils.get(ctx.message.author.server.roles, name='Events')
    role4 = discord.utils.get(ctx.message.author.server.roles, name='Battle Practice')
    role5 = discord.utils.get(ctx.message.author.server.roles, name='Clan Member')

    if 'main' in clan:
        cmention = "<@&441739682443821057>"
    elif 'royale' in clan:
        cmention = "<@&441739759627534336>"
    elif 'inc' in clan:
        cmention = "<@&441739726274297856>"
    elif 'tavern' in clan:
        cmention = "<@&503021345911603201>"
    elif 'canada' in clan:
        cmention = "<@&520398979364683796>"
    elif 'kinda' in clan:
        cmention = "<@&527865240910692372>"
    elif 'force' in clan:
        cmention = "<@&473584851476545547>"
    elif 'folks' in clan:
        cmention = "<@&473585085019455489>"
    else:
        cmention = "<@&493273230757462026>"

    await client.replace_roles(user, role)

    await client.change_nickname(user, str(user.display_name) + " | " + str(clan.capitalize()))

    await client.send_message(client.get_channel('441566984086355973'),
                              user.display_name + " has joined our family and is the newest member of "
                              + cmention + "!"
                                           " Please make them feel at home :slight_smile:")
    await client.add_roles(user, role2)
    await client.send_message(client.get_channel('492408861609689098'),
                              "**Great job on recruiting __" + str(
                                  user.display_name) + "__ " + ctx.message.author.mention + "!**")
    await client.add_roles(user, role3)
    await client.send_message(user, "Hello " + user.mention + "! ^.^\n\nI'm a bot created by the Founder of Elitists"
                                                              " - Evo, and he is very happy that you are now a part of"
                                                              " our family. The Discord server is very big and can get"
                                                              " confusing so I've attached some "
                                                              "helpful screenshots to help"
                                                              " you navigate the server. Please don't hesitate to DM my"
                                                              " master (Evo#7307) or one of the Recruiters if you have"
                                                              " any questions/comments!")
    await client.add_roles(user, role4)
    await client.add_roles(user, role5)

    await client.send_message(user, "**Clan and Discord Rules**\n*Please read the rules if you haven't already*")
    await client.send_message(user, "https://s3.amazonaws.com/elitists/discord/spawn.PNG")

    await client.send_message(user, "**Clan**\n*Communicate privately with your clan using these channels*")
    await client.send_message(user, "https://s3.amazonaws.com/elitists/discord/clan.PNG")

    await client.send_message(user, "**Trade Sections**\n*Used for trading between our family clans*")
    await client.send_message(user, "https://s3.amazonaws.com/elitists/discord/tr.PNG")

    await client.send_message(user, "**Coaching**\n*We offer coaching to help our members improve*")
    await client.send_message(user, "https://s3.amazonaws.com/elitists/discord/coach.PNG")

    await client.send_message(user, "**Deck Shop**\n*This area can be used to check your stats, "
                                    "chest cycle and much more!*")
    await client.send_message(user, "https://s3.amazonaws.com/elitists/discord/ds.PNG")


# Strike System
@client.command(pass_context=True)
@commands.has_any_role('Leaders', 'Striker')
async def syncclan(ctx, c):
    clan = c.lower()
    add_count = 0
    skip_count = 0
    author_mention = ctx.message.author.mention

    clan_url = ""

    # Get the correct clan URL based on the name provided
    if 'main' in clan:
        clan_url = "https://api.royaleapi.com/clan/8CGUJ99"
    elif 'royale' in clan:
        clan_url = "https://api.royaleapi.com/clan/QJC2YL8"
    elif 'inc' in clan:
        clan_url = "https://api.royaleapi.com/clan/R9CCGJ2"
    elif 'tavern' in clan:
        clan_url = "https://api.royaleapi.com/clan/PLQLPP9R"
    elif 'canada' in clan:
        clan_url = "https://api.royaleapi.com/clan/POOPJUQL"
    elif 'kinda' in clan:
        clan_url = "https://api.royaleapi.com/clan/Y0CC2UGQ"
    elif 'force' in clan:
        clan_url = "https://api.royaleapi.com/clan/8Y2URQL2"
    elif 'folks' in clan:
        clan_url = "https://api.royaleapi.com/clan/P02RQCYG"
    elif 'forge' in clan:
        clan_url = "https://api.royaleapi.com/clan/99VRJUGO"
    else:
        await client.say("Invalid Clan Name. " + author_mention)
        return

    # Begin DB interaction
    await client.say("Baka!!! This will take some time. I will let you know when I'm done. "
                     + author_mention)

    # Get the data from Royale API
    response = requests.request("GET", clan_url, headers=api_auth)

    # Convert the response (in a text format) into a py dict
    data = json.loads(response.text)

    # Try to establish a connection to the database
    try:
        db = pymysql.connect(host="localhost",  # your host, usually localhost
                             user="evo",  # your username
                             passwd="dwaynemhb1",  # your password
                             db="discord")  # name of the data base

        dt = datetime.datetime.today()
        db_dt = datetime.datetime(dt.year, dt.month, dt.day)
        cur = db.cursor()

        db.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

    except Exception as e:
        print(e)

    # Begin CRUD operations
    for member in data["members"]:
        tag = member["tag"]
        name = member["name"]

        # Update the member if they are still part of the clan
        upd_sql = "UPDATE strike SET syncver = %s WHERE member_tag = %s"
        upd_val = (db_dt, tag)
        cur.execute(upd_sql, upd_val)

        try:
            # If the member is new since last sync, add them
            sql = "INSERT INTO strike VALUES (%s, %s, %s, %s, %s)"
            val = (tag, name, clan, 0, db_dt)
            cur.execute(sql, val)

            add_count += 1

        except Exception as e:
            # If member has been out of the clan for more than 3 days, delete them
            del_sql = "DELETE FROM strike where (DATEDIFF(%s, syncver) > 3) AND member_clan = %s"
            val2 = (db_dt, clan)
            cur.execute(del_sql, val2)

            skip_count += 1

            print(e)

    if add_count > 0:
        await client.say("**" + str(add_count) + "** Members from **" + clan.capitalize() +
                         "** have been successfully synced. You may now add strikes to those players. "
                         + ctx.message.author.mention)

    if skip_count > 0:
        await client.say("**" + str(skip_count) + "** Members from **" + clan.capitalize() +
                         "** have been skipped as they were synced previously. "
                         + ctx.message.author.mention)
    db.commit()
    cur.close()
    db.close()


@syncclan.error
async def sc_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)


@client.command(pass_context=True)
@commands.has_any_role('Leaders', 'Striker')
async def addstrike(ctx, user, clan, n=1):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()

    get_strikes = ("SELECT * FROM strike WHERE member_name LIKE %s AND member_clan = %s")
    user_sql = user + "%"
    strikes = cur.execute(get_strikes, (user_sql, clan,))

    for c in cur.fetchall():
        strikes = c[3]
        user = c[1]
        tag = c[0]

    print(str(strikes))

    new_strikes = int(strikes) + int(n)

    add_strikes = ("UPDATE strike SET member_strikes = %s WHERE member_name LIKE %s AND member_clan = %s")
    cur.execute(add_strikes, (new_strikes, user_sql, clan,))
    db.commit()

    if new_strikes >= 3:
        await client.send_message(ctx.message.channel, user + " (" + clan.capitalize() + ") | " + tag +
                                  " has " + str(new_strikes) + " strikes. Feel free to kick!! "
                                  + ctx.message.author.mention)
    else:
        await client.send_message(ctx.message.channel, user + " (" + clan.capitalize() + ") | " + tag +
                                  " now has " + str(new_strikes) + " strikes")

    db.close()
    cur.close()


@addstrike.error
async def addstrike_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel,
                                  content='You are missing some required fields there buddy :hearts:' + ctx.message.author.mention)


@client.command(pass_context=True)
@commands.has_any_role('Leaders', 'Strikers', 'Founder')
async def delstrike(ctx, user, clan, x):
    if int(x) > 0:
        n = x
    else:
        n = 1

    try:
        db = pymysql.connect(host="localhost",  # your host, usually localhost
                             user="evo",  # your username
                             passwd="dwaynemhb1",  # your password
                             db="discord")  # name of the data base

        cur = db.cursor()

        retrieve_strikes = ("SELECT * FROM strike WHERE member_name LIKE %s AND member_clan = %s")
        user_upd = user + "%"
        strikes = cur.execute(retrieve_strikes, (user_upd, clan,))

        for c in cur.fetchall():
            strikes = c[3]
            tag = c[0]
            user = c[1]

        if int(n) > int(strikes):
            await client.send_message(ctx.message.channel, "Woah slow down! " + user +
                                      " doesn't have that many strikes for you to remove")
            return
        else:
            new_strikes = int(strikes) - int(n)

            del_strikes = ("UPDATE strike SET member_strikes = %s WHERE member_name LIKE %s AND member_clan = %s ")
            cur.execute(del_strikes, (new_strikes, user_upd, clan,))
            db.commit()

            await client.send_message(ctx.message.channel, user + " (" + clan.capitalize() + ") | " + tag +
                                      " now has " + str(new_strikes) + " strikes")

        db.close()
        cur.close()
    except Exception as e:
        print(e)


@delstrike.error
async def delstrike_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel,
                                  content='You are missing some required fields there buddy :hearts: ' + ctx.message.author.mention)
    else:
        print(error)


@client.command(pass_context=True)
@commands.has_any_role('Leaders', 'Strikers', 'Founder')
async def strikelog(ctx, clan):
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base

    cur = db.cursor()

    n = 0

    sql = (
        "SELECT * FROM strike WHERE member_strikes > 0 AND member_clan = %s ORDER BY CAST(member_strikes AS UNSIGNED) DESC")
    rc = cur.execute(sql, (clan,))

    try:
        if rc == 0:
            await client.send_message(ctx.message.channel,
                                      "No one has any strikes for " + clan.capitalize() + ". That's great.")
        else:
            embed = discord.Embed(
                description="[" + clan.capitalize() + "'s Freeloaders](https://royaleapi.com/clan/family/elitists/clans)",
                url='https://royaleapi.com/clan/family/elitists/clans',
                colour=15467841
            )

            for player in cur.fetchall():
                tag = player[0]
                display_name = player[1]
                clan = player[2]
                strikes = player[3]
                n += 1

                # embed.add_field(name="`" + str(n) + '.`', value="**" + display_name + " (" + clan.capitalize()
                #                 + ")" " | " + tag + "** has **"
                #                 + strikes + '** strikes',
                #                 inline=True)
                embed.add_field(name=display_name + " | " + tag,
                                value="__" + strikes + '__ strikes',
                                inline=False)

            await client.send_message(ctx.message.channel, embed=embed)

    except Exception as e:
        print(e)

    db.close()
    cur.close()


@strikelog.error
async def slog_errors(error, ctx):
    if isinstance(error, CheckFailure):
        await client.send_message(ctx.message.channel, content='Sorry, you are not worthy of this command '
                                                               + ctx.message.author.mention)
    elif isinstance(error, BadArgument):
        await client.send_message(ctx.message.channel, content='You are not using the command correctly '
                                                               ':thinking:' + ctx.message.author.mention)
    elif isinstance(error, MissingRequiredArgument):
        await client.send_message(ctx.message.channel,
                                  content='You are missing some required fields there buddy :hearts:' + ctx.message.author.mention)


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        description='[All my commands are below!](https://royaleapi.com/clan/family/elitists/clans)',
        url='https://royaleapi.com/clan/family/elitists/clans',
        colour=discord.Colour.dark_gold()
    )

    embed.set_footer(text='\nPlease feel free to DM Evo#7307 for more info')

    embed.set_author(name='You called, ' + ctx.message.author.display_name + "?",
                     icon_url='https://encrypted-tbn0.gstatic.com/images?q'
                              '=tbn:ANd9GcRj0tmu2WrgetCL4ncPKO2QGPNwKrM12_mpOFtsMFYb0-6ts7XE6w')

    embed.add_field(name='*wladd name tag clan (Recruiters only)', value='Adds a player to the Waiting List for the '
                                                       'specified clan',
                    inline=False)
    embed.add_field(name='*wldel tag (Recruiters only)', value='Removes a player from the Waiting List',
                    inline=False)
    embed.add_field(name='*showwl clan (Recruiters only)', value='Shows all players on the Waiting List for the specified clan'
                                               ' or all clans if none is specified.', inline=False)
    embed.add_field(name='*rolemems rolename', value='List all members with the specified role', inline=False)
    embed.add_field(name='*clear (Administrators only)', value='Deletes messages from a channel.', inline=False)
    embed.add_field(name='*getstats @user tag y/n (Recruiters only)', value='Displays Clash Royale stats that matter.',
                    inline=False)
    embed.add_field(name='*givecookie @user number (Cookie Club only)',
                    value='Gives cookies to the user that you tagged!',
                    inline=False)
    embed.add_field(name='*takecookie @user number (Cookie Club only)',
                    value='Takes cookies from the user that you tagged!',
                    inline=False)
    embed.add_field(name='*cookielb number',
                    value='Shows the top cookie hoarders!',
                    inline=False)
    embed.add_field(name='*syncclan clan (Leaders & Strikers only)',
                    value='Syncs the specified clan for the Strike Log. Clan names are: \n'
                          'Main, Royale, Canada, Forge, Inc, Force, Folks, Kinda, Tavern',
                    inline=False)
    embed.add_field(name='*addstrike user clan number (Leaders & Strikers only)', value='Adds strikes to a user',
                    inline=False)
    embed.add_field(name='*delstrike user clan number (Leaders & Strikers only)', value='Removes strikes from a user',
                    inline=False)
    embed.add_field(name='*strikelog clan (Leaders & Strikers only)',
                    value='Shows the Strike Log for the specified clan',
                    inline=False)
    embed.add_field(name='*donate', value='Allows you to donate to Elitists.', inline=False)
    embed.add_field(name='*help', value='Brings up this interface.', inline=False)

    await client.say(author.mention + ", please check your inbox!")
    await client.send_message(author, embed=embed)


def database_connect():
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="evo",  # your username
                         passwd="dwaynemhb1",  # your password
                         db="discord")  # name of the data base
    return db


def get_pb_icon(personal_best):
    if personal_best >= 6400:
        pb_icon = '<:arena21:554336208113631236> '
    elif personal_best >= 6100:
        pb_icon = '<:arena20:554336201226584075>'
    elif personal_best >= 5800:
        pb_icon = '<:arena19:554336194549252241>'
    elif personal_best >= 5500:
        pb_icon = '<:arena18:554336183438671873>'
    elif personal_best >= 5200:
        pb_icon = '<:arena17:554336171879301160>'
    elif personal_best >= 4900:
        pb_icon = '<:arena16:554336163566059558>'
    elif personal_best >= 4600:
        pb_icon = '<:arena15:554336153239552012>'
    elif personal_best >= 4300:
        pb_icon = '<:arena14:554336144821846017>'
    elif personal_best >= 4000:
        pb_icon = '<:arena13:554336138219880460>'
    elif personal_best >= 3600:
        pb_icon = '<:arena12:554336131345547274>'
    elif personal_best >= 3300:
        pb_icon = '<:arena11:554336009005957160>'
    elif personal_best >= 3000:
        pb_icon = '<:arena10:554335850440425483>'
    elif personal_best >= 2600:
        pb_icon = '<:arena9:554335843511304246>'
    elif personal_best >= 2300:
        pb_icon = '<:arena8:554335838335533057>'
    elif personal_best >= 2000:
        pb_icon = '<:arena7:554335827891716116>'
    elif personal_best >= 1600:
        pb_icon = '<:arena6:554335820459409432>'
    elif personal_best >= 1300:
        pb_icon = '<:arena5:554335813123440692> '
    elif personal_best >= 1000:
        pb_icon = '<:arena4:554335807507529748>'
    elif personal_best >= 600:
        pb_icon = '<:arena3:554335800637128714>'
    elif personal_best >= 300:
        pb_icon = '<:arena2:554335793028530196>'
    else:
        pb_icon = '<:arena1:554335783901724693>'
    return pb_icon


def get_level_icon(level):
    if level == 13:
        level_icon = 'https://www.deckshop.pro/img/bot/data/13.png'
    elif level == 12:
        level_icon = 'https://www.deckshop.pro/img/bot/data/12.png'
    elif level == 11:
        level_icon = 'https://www.deckshop.pro/img/bot/data/11.png'
    elif level == 10:
        level_icon = 'https://www.deckshop.pro/img/bot/data/10.png'
    elif level == 9:
        level_icon = 'https://www.deckshop.pro/img/bot/data/9.png'
    elif level == 8:
        level_icon = 'https://www.deckshop.pro/img/bot/data/8.png'
    elif level == 7:
        level_icon = 'https://www.deckshop.pro/img/bot/data/7.png'
    elif level == 6:
        level_icon = 'https://www.deckshop.pro/img/bot/data/6.png'
    elif level == 5:
        level_icon = 'https://www.deckshop.pro/img/bot/data/5.png'
    elif level == 4:
        level_icon = 'https://www.deckshop.pro/img/bot/data/4.png'
    elif level == 3:
        level_icon = 'https://www.deckshop.pro/img/bot/data/3.png'
    elif level == 2:
        level_icon = 'https://www.deckshop.pro/img/bot/data/2.png'
    else:
        level_icon = 'https://www.deckshop.pro/img/bot/data/1.png'

    return level_icon


def get_trophy_image(current_trophies):
    if current_trophies >= 6400:
        trophy_img = '<:arena21:554336208113631236> '
    elif current_trophies >= 6100:
        trophy_img = '<:arena20:554336201226584075>'
    elif current_trophies >= 5800:
        trophy_img = '<:arena19:554336194549252241>'
    elif current_trophies >= 5500:
        trophy_img = '<:arena18:554336183438671873>'
    elif current_trophies >= 5200:
        trophy_img = '<:arena17:554336171879301160>'
    elif current_trophies >= 4900:
        trophy_img = '<:arena16:554336163566059558>'
    elif current_trophies >= 4600:
        trophy_img = '<:arena15:554336153239552012>'
    elif current_trophies >= 4300:
        trophy_img = '<:arena14:554336144821846017>'
    elif current_trophies >= 4000:
        trophy_img = '<:arena13:554336138219880460>'
    elif current_trophies >= 3600:
        trophy_img = '<:arena12:554336131345547274>'
    elif current_trophies >= 3300:
        trophy_img = '<:arena11:554336009005957160>'
    elif current_trophies >= 3000:
        trophy_img = '<:arena10:554335850440425483>'
    elif current_trophies >= 2600:
        trophy_img = '<:arena9:554335843511304246>'
    elif current_trophies >= 2300:
        trophy_img = '<:arena8:554335838335533057>'
    elif current_trophies >= 2000:
        trophy_img = '<:arena7:554335827891716116>'
    elif current_trophies >= 1600:
        trophy_img = '<:arena6:554335820459409432>'
    elif current_trophies >= 1300:
        trophy_img = '<:arena5:554335813123440692> '
    elif current_trophies >= 1000:
        trophy_img = '<:arena4:554335807507529748>'
    elif current_trophies >= 600:
        trophy_img = '<:arena3:554335800637128714>'
    elif current_trophies >= 300:
        trophy_img = '<:arena2:554335793028530196>'
    else:
        trophy_img = '<:arena1:554335783901724693>'
    return trophy_img


def get_arena_icon(arena):
    if arena == 15:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena15.png'
    elif arena == 14:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena14.png'
    elif arena == 13:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena13.png'
    elif arena == 12:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena12.png'
    elif arena == 11:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena11.png'
    elif arena == 10:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena10.png'
    elif arena == 9:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena9.png'
    elif arena == 8:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena8.png'
    elif arena == 7:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena7.png'
    elif arena == 6:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena6.png'
    elif arena == 5:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena5.png'
    elif arena == 4:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena4.png'
    elif arena == 3:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena3.png'
    elif arena == 2:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena2.png'
    elif arena == 16:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena16.png'
    elif arena == 17:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena17.png'
    elif arena == 18:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena18.png'
    elif arena == 19:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena19.png'
    elif arena == 20:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena20.png'
    elif arena == 21:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena21.png'
    else:
        arena_icon = 'https://royaleapi.com/static/img/arenas/arena1.png'
    return arena_icon


def get_league_stats(tag, league):
    player_url = "https://api.royaleapi.com/player/" + tag

    response = requests.request("GET", player_url, headers=api_auth)

    # Convert the response (in a text format) into a py dict
    data = json.loads(response.text)

    ll_card_imgs_leggy = []
    ll_card_imgs_common = []
    ll_card_imgs_rare = []
    ll_card_imgs_epic = []

    db = database_connect()
    cur = db.cursor()

    # sql = "SELECT * FROM card_images WHERE card_name = %s ORDER BY card_rarity DESC"
    sql = "SELECT card_image_code FROM card_images WHERE card_name = %s"
    n = 0

    # UL League
    if league == 'UL':
        for card in data["cards"]:
            card_name = card["name"]
            cur.execute(sql, (card_name,))
            if (card["rarity"] == "Legendary") & (card["level"] == 1):
                for c in cur.fetchall():
                    card_image = c[0]

                    if n < 35:
                        ll_card_imgs_leggy.append(card_image)
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] < 4):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_epic.append(card_image)
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] < 7):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_rare.append(card_image)
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] < 9):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_common.append(card_image)
                n += 1

    # Bronze League
    if league == 'Bronze':
        for card in data["cards"]:
            card_name = card["name"]
            cur.execute(sql, (card_name,))
            if (card["rarity"] == "Legendary") & (card["level"] == 1):
                for c in cur.fetchall():
                    card_image = c[0]

                    if n < 35:
                        ll_card_imgs_leggy.append(card_image)
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 4):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_epic.append(card_image)
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 7):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_rare.append(card_image)
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 9):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_common.append(card_image)
                n += 1

    # Silver League
    if league == 'Silver':
        for card in data["cards"]:
            card_name = card["name"]
            cur.execute(sql, (card_name,))
            if (card["rarity"] == "Legendary") & (card["level"] == 2):
                for c in cur.fetchall():
                    card_image = c[0]

                    if n < 35:
                        ll_card_imgs_leggy.append(card_image)
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 5):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_epic.append(card_image)
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 8):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_rare.append(card_image)
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 10):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_common.append(card_image)
                n += 1

    # Gold League
    if league == 'Gold':
        for card in data["cards"]:
            card_name = card["name"]
            cur.execute(sql, (card_name,))
            if (card["rarity"] == "Legendary") & (card["level"] == 3):
                for c in cur.fetchall():
                    card_image = c[0]

                    if n < 35:
                        ll_card_imgs_leggy.append(card_image)
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 6):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_epic.append(card_image)
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 9):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_rare.append(card_image)
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 11):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_common.append(card_image)
                n += 1

    # Legendary League
    if league == 'Legendary':
        for card in data["cards"]:
            card_name = card["name"]
            cur.execute(sql, (card_name,))
            if (card["rarity"] == "Legendary") & (card["level"] == 4):
                for c in cur.fetchall():
                    card_image = c[0]

                    if n < 35:
                        ll_card_imgs_leggy.append(card_image)
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] >= 7):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_epic.append(card_image)
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] >= 10):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_rare.append(card_image)
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] >= 12):
                for c in cur.fetchall():
                    card_image = c[0]
                    if n < 35:
                        ll_card_imgs_common.append(card_image)
                n += 1
    cur.close()
    db.close()
    ll_card_imgs = ll_card_imgs_common + ll_card_imgs_rare + ll_card_imgs_epic + ll_card_imgs_leggy

    return ll_card_imgs


def get_league_stats_count(tag, league):
    player_url = "https://api.royaleapi.com/player/" + tag

    response = requests.request("GET", player_url, headers=api_auth)

    # Convert the response (in a text format) into a py dict
    data = json.loads(response.text)

    n = 0

    if league == 'UL':
        for card in data["cards"]:
            if (card["rarity"] == "Epic") & (card["level"] < 4):
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] < 7):
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] < 9):
                n += 1

    if league == 'Bronze':
        for card in data["cards"]:
            if (card["rarity"] == "Legendary") & (card["level"] == 1):
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 4):
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 7):
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 9):
                n += 1

    if league == 'Silver':
        for card in data["cards"]:
            if (card["rarity"] == "Legendary") & (card["level"] == 2):
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 5):
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 8):
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 10):
                n += 1

    if league == 'Gold':
        for card in data["cards"]:
            if (card["rarity"] == "Legendary") & (card["level"] == 3):
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] == 6):
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] == 9):
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] == 11):
                n += 1

    # Legendary League Loop
    if league == 'Legendary':
        for card in data["cards"]:
            if (card["rarity"] == "Legendary") & (card["level"] == 4):
                n += 1
            elif (card["rarity"] == "Epic") & (card["level"] >= 7):
                n += 1
            elif (card["rarity"] == "Rare") & (card["level"] >= 10):
                n += 1
            elif (card["rarity"] == "Common") & (card["level"] >= 12):
                n += 1
    return n


@client.event
async def on_member_update(user, after):
    if "new spawn" in [y.name.lower() for y in user.roles]:

        if "new spawn cr" in [y.name.lower() for y in after.roles]:
            await client.send_message(client.get_channel('475122791197179914'),
                                      content='Thanks for selecting **Clash Royale** as your game ' + str(
                                          user.mention) +
                                              '! A <@&492405351451197455> will be with you shortly.')
            role = get(user.server.roles, name='New Spawn CR')
            await client.replace_roles(user, role)
        elif "new spawn bs" in [y.name.lower() for y in after.roles]:
            await client.send_message(client.get_channel('522778711385178112'),
                                      content='Thanks for selecting **Brawl Stars** as your game ' + str(user.mention) +
                                              '! A <@&540627322013745172> will be with you shortly.')
            role = get(user.server.roles, name='New Spawn BS')
            await client.replace_roles(user, role)


client.run(TOKEN)

# db = database_connect()
#
# cur = db.cursor()
#
# cur.execute('SET NAMES utf8;')
# cur.execute('SET CHARACTER SET utf8;')
# cur.execute('SET character_set_connection=utf8;')
#
# sql = "SELECT * FROM card_images WHERE card_name = %s ORDER BY card_rarity DESC"
# # sql2 = "INSERT INTO card_images(card_name, card_rarity) VALUES (%s, %s)"
# n = 0
# for card in data["cards"]:
#     card_name = card["name"]
#     if (card["rarity"] == "Legendary") & (card["level"] == 4):
#         cur.execute(sql, (card_name,))
#         for c in cur.fetchall():
#             card_image = c[2]
#
#             if n < 35:
#                 ll_card_imgs.append(card_image)
#         n += 1
#     elif (card["rarity"] == "Epic") & (card["level"] >= 7):
#         cur.execute(sql, (card_name,))
#         for c in cur.fetchall():
#             card_image = c[2]
#             if n < 35:
#                 ll_card_imgs.append(card_image)
#         n += 1
#     elif (card["rarity"] == "Rare") & (card["level"] >= 10):
#         cur.execute(sql, (card_name,))
#         for c in cur.fetchall():
#             card_image = c[2]
#             if n < 35:
#                 ll_card_imgs.append(card_image)
#         n += 1
#     elif (card["rarity"] == "Common") & (card["level"] >= 12):
#         cur.execute(sql, (card_name,))
#         for c in cur.fetchall():
#             card_image = c[2]
#             if n < 35:
#                 ll_card_imgs.append(card_image)
#         n += 1

# elif card["rarity"] == "Epic":
#     card_rarity = 3
# elif card["rarity"] == "Rare":
#     card_rarity = 2
# else:
#     card_rarity = 1

# val = (card_name, card_rarity)
#
# cur.execute(sql2, val)
# db.commit()
#     try:
#         if int(card["level"]) > 11:
#             cc += 1
#             card_name = card["name"]
#             cur.execute(sql, (card_name,))
#
#             for c in cur.fetchall():
#                 card_image = c[1]
#                 ll_card_imgs.append(card_image)
#         print(ll_card_imgs)
#     except Exception as e:
#         print(e)
# print(str(cc))
# cur.close()
# db.close()
#     if card["level"] >= 12:
#         # print(card["name"] + " is" + " level " + str(card["level"]))
#         print(card["name"])
#         ll_cards.append(card["name"])
#
