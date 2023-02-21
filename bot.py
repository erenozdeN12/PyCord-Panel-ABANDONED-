import discord
from discord.ext import commands
from configparser import ConfigParser
import time

intents = discord.Intents.default()
intents.members = True
config = ConfigParser()
config.read('outputs.ini')
bot = commands.Bot(command_prefix=',', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')


TOKEN = config.get("BOTSETTINGS", "Bot_Token")
bot.run(TOKEN)