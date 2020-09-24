@bot.command()
async def osu(ctx, action, *, inp):
    if action == "user":
    	# User search
        try:
            url = f"https://osu.ppy.sh/api/get_user?u={inp}&k=apiheregoeshere"
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
            }

            r = requests.get(url, headers=headers)
            s = r.json()

            user_id = (s[0]['user_id'])
            username = (s[0]['username'])
            join_date = (s[0]['join_date'])
            ranked_score = (s[0]['ranked_score'])
            total_score = (s[0]['total_score'])
            pp_rank = (s[0]['pp_rank'])
            accuracy = (s[0]['accuracy'])
            count_rank_ss = (s[0]['count_rank_ss'])
            total_seconds_played = (s[0]['total_seconds_played'])
            country = (s[0]['country'])
            pp_country_rank = (s[0]['pp_country_rank'])
            playcount = (s[0]['playcount'])
            
            lowercountry = (country.lower())
            
            icon_url = f"http://s.ppy.sh/a/{user_id}"
            time = int(total_seconds_played) / 3600

            embed=discord.Embed(title="User search", description=username)
            embed.set_author(name="Osu!", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Osu%21Logo_%282015%29.png/600px-Osu%21Logo_%282015%29.png")
            embed.set_thumbnail(url=icon_url)
            embed.add_field(name="User ID", value=user_id, inline=True)
            embed.add_field(name="Username", value=username, inline=True)
            embed.add_field(name="Join Date", value=join_date, inline=True)
            embed.add_field(name="Ranked Score", value=ranked_score, inline=True)
            embed.add_field(name="Total Score", value=total_score, inline=True)
            embed.add_field(name="PP Rank", value=pp_rank, inline=True)
            embed.add_field(name="Accuracy", value=accuracy, inline=True)
            embed.add_field(name="Count rank SS", value=count_rank_ss, inline=True)
            embed.add_field(name="Total seconds played", value=f"{total_seconds_played} ({round(time)} hours)", inline=True)
            embed.add_field(name="Country", value=f"{country} :flag_{lowercountry}:", inline=True)
            embed.add_field(name="PP Country rank", value=pp_country_rank, inline=True)
            embed.add_field(name="Play Count", value=playcount, inline=True)
            embed.set_footer(text="Funny cat - Powered by Osu! API")
            await ctx.send(embed=embed)
        except Exception as x:
            await ctx.send(f"An error occured ```{x}```")
            
    elif action == "beatmap" or action == "map":
    	# Beatmap search
        try:
            url = f"https://osu.ppy.sh/api/get_beatmaps?b={inp}&k=apikeygoeshere"
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
            }



            r = requests.get(url, headers=headers)
            s = r.json()

            beatmap_id = (s[0]['beatmap_id'])
            approved = (s[0]['approved'])
            total_length = (s[0]['total_length'])
            hit_length = (s[0]['hit_length'])
            version = (s[0]['version'])
            diff_size = (s[0]['diff_size'])
            count_normal = (s[0]['count_normal'])
            count_slider = (s[0]['count_slider'])
            count_spinner = (s[0]['count_spinner'])
            title = (s[0]['title'])
            artist = (s[0]['artist'])
            source = (s[0]['source'])
            bpm = (s[0]['bpm'])
            submit_date = (s[0]['submit_date'])
            creator = (s[0]['creator'])
            favourite_count = (s[0]['favourite_count'])
            rating = (s[0]['rating'])
            playcount = (s[0]['playcount'])
            passcount = (s[0]['passcount'])
            difficultyrating = (s[0]['difficultyrating'])
            tags = (s[0]['tags'])

            cover = f"https://assets.ppy.sh/beatmaps/{beatmap_id}/covers/cover.jpg"
            thumb = f"https://b.ppy.sh/thumb/{beatmap_id}l.jpg"

            embed=discord.Embed(title="Beatmap search", description="5456156")
            embed.set_author(name="Osu!", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Osu%21Logo_%282015%29.png/600px-Osu%21Logo_%282015%29.png")
            embed.set_thumbnail(url=thumb)
            embed.add_field(name="Beatmap ID", value=beatmap_id, inline=True)
            embed.add_field(name="Approved", value=approved, inline=True)
            embed.add_field(name="Total Length", value=total_length, inline=True)
            embed.add_field(name="Hit Length", value=hit_length, inline=True)
            embed.add_field(name="Difficulty", value=version, inline=True)
            embed.add_field(name="Diff Size", value=diff_size, inline=True)
            embed.add_field(name="Circle Count", value=count_normal, inline=True)
            embed.add_field(name="Slider Count", value=count_slider, inline=True)
            embed.add_field(name="Spinner Count", value=count_spinner, inline=True)
            embed.add_field(name="Song Title", value=title, inline=True)
            embed.add_field(name="Song Artist", value=artist, inline=True)
            embed.add_field(name="Source", value=source, inline=True)
            embed.add_field(name="BPM", value=bpm, inline=True)
            embed.add_field(name="Submit date", value=submit_date, inline=True)
            embed.add_field(name="Creator", value=creator, inline=True)
            embed.add_field(name="Favourite Count", value=favourite_count, inline=True)
            embed.add_field(name="Rating", value=rating, inline=True)
            embed.add_field(name="Play Count", value=playcount, inline=True)
            embed.add_field(name="Pass Count", value=passcount, inline=True)
            embed.add_field(name="Difficulty Rating", value=difficultyrating, inline=True)
            embed.add_field(name="Tags", value=tags, inline=True)
            embed.set_image(url=cover)
            embed.set_footer(text="Funny cat - Powered by Osu! API")
            await ctx.send(embed=embed)
        except Exception as x:
            await ctx.send(f"An error occured ```{x}```")
