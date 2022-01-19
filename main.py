import os
import discord
from discord.ext import commands 
import music
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user} is connected to the following server: {GUILD}")

cogs = [music]
for index in range(len(cogs)):
    cogs[index].setup(client)

client.run(TOKEN)