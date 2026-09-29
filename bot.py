import os, discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! 👋 I am online!")

@bot.event
async def on_message(msg):
    if msg.author != bot.user and msg.content.lower() == "hello":
        await msg.channel.send("Hello! 👋 I am online!")
    await bot.process_commands(msg)

bot.run(os.getenv("DISCORD_TOKEN"))