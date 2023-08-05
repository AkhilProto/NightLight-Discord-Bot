import disnake
from disnake.ext import commands
from moderation import Moderation
from normal import Normal

intents = disnake.Intents.all()
bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    bot.add_cog(Moderation(bot))
    bot.add_cog(Normal(bot))
    
    print(f"Bot started with the ID: {bot.user}")



if __name__ == "__main__":
    bot.run(token)


