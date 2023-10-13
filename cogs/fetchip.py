import discord
import datetime
import requests

from discord.ext import commands

BOT_VERSION = open('version').read()

class FetchIP(commands.Cog):
    print('★ Loaded cog: Fetch Machine IP')
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def fetchip(
        self,
        ctx
    ):
        """Check the IP address of the machine the bot is running on (IPv4 & IPv6)"""
        requestTime = datetime.datetime.now()
        print(f'[{requestTime}] [IP Check] Requested by {ctx.author.display_name} (ID: {ctx.author.id})')

        try:
            ipv4 = requests.get('https://checkip.amazonaws.com/').text.strip()
            ipv6 = requests.get('https://icanhazip.com/').text.strip()

            embed = discord.Embed(
                title=f':globe_with_meridians: Current IP Addresses for the machine the bot is running on',
                description=f'IPv4 fetched with AWS, IPv6 fetched with icanhazip.',
                color=discord.Color.blurple(),
            )
            try:
                embed.add_field(name='IPv4 Address', value=f'```{ipv4}```', inline=False)
            except:
                embed.add_field(name='IPv4 Address', value=f'```* Unavailable *```', inline=False)
            
            try:
                embed.add_field(name='IPv6 Address', value=f'```{ipv6}```', inline=True)
            except:
                embed.add_field(name='IPv6 Address', value=f'```* Unavailable *```', inline=True)
            
            now = datetime.datetime.now()
            rtime = now.strftime("%B %d, %Y, %H:%M")
            embed.set_footer(text=f"Requested by {ctx.author.display_name} » {rtime} | {BOT_VERSION}")

            await ctx.respond(embed=embed)
        except Exception as e:
            await ctx.respond('<:warn:1105998033335898162> An error occurred when processing your command. Please contact `Angry_Pineapple#6926` with what you were attempting to do, along with the date and time.', ephemeral=True)
            print(e)
            pass

def setup(bot):
    bot.add_cog(FetchIP(bot))
