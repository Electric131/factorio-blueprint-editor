import discord, json, datetime, os
from discord.ext import commands
from dotenv import load_dotenv
from generate_train import generate_train, colorFromString
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("Iron Wheel", "Iron Gear Wheel"))

client = discord.Client()
bot = commands.Bot(command_prefix="!")

load_dotenv()

token = os.getenv('TOKEN')

def getTime():
    return datetime.datetime.now.strftime("%m/%d/%Y @%H:%M:%S")

with open("config.json", "r") as f:
    config = json.load(f)

@bot.command(no_pm=True)
async def train(ctx, itemType:str, color:str=""):
    try:
        trainTypeMsg, trainString = generate_train(config, itemType, colorFromString(config, color))
    except Exception as e:
        await ctx.send("An error occured while running this command.")
        with open("log.txt", "a") as f:
            f.write(f"{getTime()} > Error occured when generating train: {e}\n")
        return
    await ctx.send(content=f"{trainTypeMsg}\n**Copy the blueprint string from the attached file:**", file=discord.File(open("message.txt", "rb")))

bot.run(token)