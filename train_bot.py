import discord, json, datetime, os
from discord.ext import commands
from dotenv import load_dotenv

client = discord.Client()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

load_dotenv()

token = os.getenv('TOKEN')

