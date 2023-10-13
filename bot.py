import datetime
import discord

AUTH_TOKEN = open("access").read()

cogs_list = [
    "facts",
    #'quote',
    "airquality",
    "fetchip"
    #'troll'
]

intents = discord.Intents.default()
discord.Intents.message_reactions = True

bot = discord.Bot()

for cog in cogs_list:
    bot.load_extension(f"cogs.{cog}")


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="Beethoven"
        )
    )
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
    print("Arcator General Utilities - Written by Angry_Pineapple")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(" - Bot revision: 0.1.2")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")


@bot.command(description="Sends the bot's latency.")
async def latency(ctx):
    botLatency = round(bot.latency, 2)
    botLatencyMs = round(bot.latency * 1000, 2)
    await ctx.respond(
        f":hourglass: Pong! Latency is **{botLatency}** seconds (**{botLatencyMs}** ms)"
    )

@bot.command(description="Invite the bot to your server.")
async def inviteme(ctx):
    embed = discord.Embed(
        title=f"<:cyndaquil:801649968737157140> Invite the bot to your server!",
        description=f'You can invite the bot using this [link](https://discord.com/oauth2/authorize?scope=bot+applications.commands&client_id=1151263311946588190).\n\n <:yellowcheck:1091497847846879324> Open the prompt and select the server you\'d like\n to invite the bot to, then press **Authorize**.',
        color=discord.Colour.yellow(),
    )

    now = datetime.datetime.now()
    rtime = now.strftime("%B %d, %Y, %H:%M")
    embed.set_footer(text=f"Requested by {ctx.author.display_name} » {rtime} | Rev. 0.1.2 (Build A)")

    await ctx.respond(embed=embed)

bot.run(AUTH_TOKEN)
