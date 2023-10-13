import discord
import datetime

from discord.ext import commands
from discord.commands import Option

BOT_VERSION = open('version').read()

class Facts(commands.Cog):
    print('★ Loaded cog: Angry Daily Facts')
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def facts(
        self,
        ctx,
        fact: Option(str, 'The fact you\'d like to display.', required=True),
        factnum: Option(int, 'The fact number you\'d like to display.', required=True),
    ):
        """Displays a fact about whatever Angry feels like today."""
        requestTime = datetime.datetime.now()
        print(f'[{requestTime}] [Facts] Requested by {ctx.author} (ID: {ctx.author.id})')

        try:
            if ctx.author.id != 304054669372817419:
                await ctx.respond('<:warn:1105998033335898162> You do not have permission to use this command.', ephemeral=True)
            else: 
                embed = discord.Embed(
                    title=f":brain: Angry's Random Fact of the Day [#{factnum}]",
                    description=f'{fact}',
                    color=discord.Colour.red(),
                )

                now = datetime.datetime.now()
                rtime = now.strftime("%B %d, %Y, %H:%M")
                embed.set_footer(text=f"Requested by {ctx.author} » {rtime} | {BOT_VERSION}")

                await ctx.respond('<@&1119870382732759120>', embed=embed)
        except Exception as e:
            await ctx.respond('<:warn:1105998033335898162> An error occurred when processing your command. Please contact `Angry_Pineapple#6926` with what you were attempting to do, along with the date and time.', ephemeral=True)
            print(e)
            pass

def setup(bot):
    bot.add_cog(Facts(bot))
