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
from background_functions import *

import os 
token = os.environ['token']


intents = disnake.Intents.all()
bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Normal(bot))
    bot.add_cog(Error_handler(bot))
    
    print(f"Bot started with the ID: {bot.user}")
    



if __name__ == "__main__":
    bot.run(token)


