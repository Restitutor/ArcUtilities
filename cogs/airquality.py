import discord
import datetime
import requests

from discord.ext import commands
from discord.commands import Option

BOT_VERSION = open('version').read()

api_key = open("aqi").read()

class AirQuality(commands.Cog):
    print('★ Loaded cog: Air Quality')
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def airquality(
        self,
        ctx,
        city: Option(str, 'The name of your city', required=True),
    ):
        """Check air quality for your location. Data provided through the World Air Quality Index project."""
        requestTime = datetime.datetime.now()
        print(f'[{requestTime}] [Air Quality] Requested by {ctx.author.display_name} (ID: {ctx.author.id})')

        try:
            api_data = requests.get(f"https://api.waqi.info/feed/{city}?token={api_key}").json()

            if api_data['status'] == 'error':
                await ctx.respond(f'<:warn:1105998033335898162> The API returned the following error: `{api_data["data"]}`\n*Make sure you entered the name of your city correctly.*', ephemeral=True)
            else:
                if api_data['data']['aqi'] <= 50:
                    embed_color = 0xB9FF72
                    quality = 'Good'
                    fact = 'Air quality is considered satisfactory, and air pollution poses little or no risk.'
                elif api_data['data']['aqi'] <= 100:
                    embed_color = 0xF3F300
                    quality = 'Moderate'
                    fact = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                elif api_data['data']['aqi'] <= 150:
                    embed_color = 0xFF8E1C
                    quality = 'Unhealthy for Sensitive Groups'
                    fact = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                elif api_data['data']['aqi'] <= 200:
                    embed_color = 0xFF8888
                    quality = 'Unhealthy'
                    fact = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
                elif api_data['data']['aqi'] <= 300:
                    embed_color = 0xC994FF
                    quality = 'Very Unhealthy'
                    fact = 'Health alert: The risk of health effects is increased for everyone.'
                elif api_data['data']['aqi'] <= 500:
                    embed_color = 0xB00058
                    quality = 'Hazardous'
                    fact = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                else:
                    embed_color = 0x000000
                    quality = 'Error'
                    fact = 'The air quality index is not available for this location.'

                embed = discord.Embed(
                    title=f':wind_blowing_face: Air Quality for {city} :arrow_right: {api_data["data"]["aqi"]}',
                    description=f'**{quality}**\n{fact}',
                    color=embed_color,
                )

                try:
                    embed.add_field(name='Concentration [PM2.5]', value=f'```{api_data["data"]["iaqi"]["pm25"]["v"]} µg/m³```\n*This is what AQI is based off of.*', inline=False)
                except:
                    embed.add_field(name='Concentration [PM2.5]', value=f'```* Unavailable *```', inline=False)
                
                try:
                    embed.add_field(name='Concentration [O₃]', value=f'```{api_data["data"]["iaqi"]["o3"]["v"]} µg/m³```', inline=True)
                except:
                    embed.add_field(name='Concentration [O₃]', value=f'```* Unavailable *```', inline=True)
                
                try:
                    embed.add_field(name='Concentration [NO₂]', value=f'```{api_data["data"]["iaqi"]["no2"]["v"]} µg/m³```', inline=True)
                except:
                    embed.add_field(name='Concentration [NO₂]', value=f'```* Unavailable *```', inline=True)

                try:
                    embed.add_field(name='Concentration [CO]', value=f'```{api_data["data"]["iaqi"]["co"]["v"]} µg/m³```', inline=True)
                except:
                    embed.add_field(name='Concentration [CO]', value=f'```* Unavailable *```', inline=True)
                
                try:
                    for src in api_data['data']['attributions']:
                        if 'logo' in src:
                            embed.add_field(name='Data Source:', value=f'[{src["name"]}]({src["url"]})', inline=False)
                except:
                    embed.add_field(name='Data Source:', value=f'```* Unavailable *```', inline=False)

                now = datetime.datetime.now()
                rtime = now.strftime("%B %d, %Y, %H:%M")
                embed.set_footer(text=f"Requested by {ctx.author.display_name} » {rtime} | {BOT_VERSION}")

                await ctx.respond(embed=embed)
        except Exception as e:
            await ctx.respond('<:warn:1105998033335898162> An error occurred when processing your command. Please contact `Angry_Pineapple#6926` with what you were attempting to do, along with the date and time.', ephemeral=True)
            print(e)
            pass

def setup(bot):
    bot.add_cog(AirQuality(bot))
