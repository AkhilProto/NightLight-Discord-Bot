#Will include the normal commands.

import disnake
from disnake.ext import commands

class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.slash_command(description="Check the bot's ping")
    async def ping(self, inter: disnake.ApplicationCommandInteraction) -> None:
        """Check the bot's latency"""
        latency = self.bot.latency
        await inter.send(f"Pong! Latency: {round(latency * 1000)}ms")
        
    @commands.slash_command(description='Lists all the things that this bot can do')
    async def help(self, inter: disnake.ApplicationCommandInteraction) -> None:
        """Help Command"""
        embed = disnake.Embed(
            title='Help',
            description="WIP",
            color= disnake.Colour.green()       
        )
        embed.set_footer(text='-----')
        embed.add_field(name='Ping', value='Check the bots Latency', inline=True)
        embed.add_field(name='Ban', value="Ban's a particuler User", inline=True)
        
        await inter.response.send_message(embed=embed)
        
    