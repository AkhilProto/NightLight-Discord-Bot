#Will include the normal commands.

import disnake
from disnake.ext import commands

class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name='help', description='Lists all the things that this bot can do')
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        """Help Command"""
        embed = disnake.Embed(
            title='Help',
            description='''**Hello, This is a discord bot made using disnake and
            is open source. 
            Our bot is open for contribution and you can use it yourself easily. 
            It is made to have slash commands and more will be added in the future**.
            Check it out: https://github.com/AkhilProto/Akhils-Servant-Discord-Bot''',
            color= disnake.Colour.blue()       
        )
        await inter.response.send_message(embed=embed)
      
    @commands.slash_command(name='ping', description="Check the bot's ping")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Check the bot's latency"""
        latency = self.bot.latency
        await inter.send(f"Pong! Latency: {round(latency * 1000)}ms")   
        
    @commands.slash_command(name="avatar", description="Check someones avatar.")
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        """Check someones avatar"""
        embed = disnake.Embed(
            title='Here is what I found:',
            color= disnake.Colour.darker_grey(),
        )
        if member == None:
            embed.set_image(inter.author.avatar)
        else:
            embed.set_image(member.avatar)

        await inter.send(embed=embed)