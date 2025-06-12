import datetime
import discord

AUTH_TOKEN = open("access").read()

BOT_VERSION = open('version').read()

cogs_list = [
    "facts",
    "airquality",
    "fetchip"
]

intents = discord.Intents.default()
discord.Intents.message_reactions = True

bot = discord.Bot(
    allowed_mentions=discord.AllowedMentions(
        everyone=False, users=False, roles=False, replied_user=True
    ),
)

for cog in cogs_list:
    bot.load_extension(f"cogs.{cog}")

class InvLink(discord.ui.View):
    def __init__(self, invlink: str):
        super().__init__()
        self.add_item(discord.ui.Button(label="Invite Link", url=invlink, emoji="🔗"))

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
    print(f" - Bot revision: {BOT_VERSION}")
    print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")


@bot.command(description="Sends the bot's latency.")
async def latency(ctx):
    await ctx.respond(
        f":hourglass: Pong! Latency is **{round(bot.latency, 2)}** seconds (**{round(bot.latency * 1000, 2)}** ms)"
    )

@bot.command(description="Invite the bot to your server.")
async def inviteme(ctx):
    embed = discord.Embed(
        title=f"<:cyndaquil:801649968737157140> Invite the bot to your server!",
        description=f'<:yellowcheck:1091497847846879324> Open the prompt below and select the server \nyou\'d like to invite the bot to, then press **Authorize**.',
        color=discord.Colour.yellow(),
    )

    now = datetime.datetime.now()
    rtime = now.strftime("%B %d, %Y, %H:%M")
    embed.set_footer(text=f"Requested by {ctx.author.display_name} » {rtime} | {BOT_VERSION}")

    await ctx.respond(embed=embed, view=InvLink('https://discord.com/oauth2/authorize?scope=bot+applications.commands&client_id=1151263311946588190'))

bot.run(AUTH_TOKEN)
