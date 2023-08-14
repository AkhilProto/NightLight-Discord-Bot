# Import modules
import disnake
from disnake.ext import commands

# Import functions from files
from moderation import Moderation
from normal import Normal
from exception_handler import Error_handler


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


