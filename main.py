# Import modules
import disnake
from disnake.ext import commands
import asyncio 
import time
import discord

# Import functions from files
from moderation import Moderation
from normal import Normal
from exception_handler import Error_handler

import os 
token = os.environ['token']

WELCOME_CHANNEL = {Channel name}
VERIFICATION_CHANNEL = {Channel name}
BOT-COMMANDS_CHANNEL = {Channel name}
intents = disnake.Intents.all()
bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Normal(bot))
    bot.add_cog(Error_handler(bot))
    
    print(f"Bot started with the ID: {bot.user}")
    

# Automatic running events
@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL)
    verification_channel = discord.utils.get(member.guild.channels, name=VERIFICATION_CHANNEL)
    bot-commands_channel = discord.utils.get(member.guild.channels, name=BOT-COMMANDS_CHANNEL)
    await welcome_channel.send(f"Welcome {member.mention}! Please read our rules and verify yourself at <#{verification_channel}> to access the server. Call me with a simple command /help in <#{bot-commands_channel}> channel. Have a great time!!")
    

if __name__ == "__main__":
    bot.run(token)


