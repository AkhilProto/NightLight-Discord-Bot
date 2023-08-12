import disnake
from disnake.ext import commands
import asyncio 
import time
import discord
from moderation import Moderation
from normal import Normal
from exception_handler import Error_handler
from keep_alive import keep_alive
import os 
token = os.environ['token']
WELCOME_CHANNEL = "📫︱join―leave"
intents = disnake.Intents.all()
bot = commands.InteractionBot(intents=intents)
keep_alive()

@bot.event
async def on_ready():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Normal(bot))
    bot.add_cog(Error_handler(bot))
    
    print(f"Bot started with the ID: {bot.user}")
    bot.loop.create_task(send_message_in_private_channel())

# Automatic running events
@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL)
    await welcome_channel.send(f"Welcome {member.mention}! Please read our rules and verify yourself at <#1130116826114826242> to access the server. Call me with a simple command ?ahelp in <#1130116826114826246> channel. Have a great time!!")

async def send_message_in_private_channel():
    await bot.wait_until_ready()
    private_channel_id = 1131217771225681920  
    
    while not bot.is_closed():
        private_channel = bot.get_channel(private_channel_id)
        latency = bot.latency
        now = time.localtime()
        await private_channel.send(f"Reporting Roger!! The time is {now.tm_hour}:{now.tm_min}:{now.tm_sec} now. Latency: {round(latency * 1000)}ms")
        await asyncio.sleep(3600)# Sleep for 1 hour (3600 seconds)

if __name__ == "__main__":
    bot.run(token)


