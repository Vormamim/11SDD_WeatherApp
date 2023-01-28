import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))

client.run("MTA2ODAyNzQzMzUwMjEzMDI1Ng.GGoF0x.wnyjk7c_2a3_dviC_xEcXtFRXLyhjGD6skc2sE")