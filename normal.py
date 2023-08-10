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
            description='''What do you need?''',
            color= disnake.Colour.blue()       
        )
        components= [disnake.ui.Button(label='Description', style=disnake.ButtonStyle.primary, custom_id="1")
                    ,disnake.ui.Button(label='Contribution', style=disnake.ButtonStyle.primary, custom_id="2")]
        
        await inter.response.send_message(embed=embed, components=components)
      
      
    @commands.Cog.listener("on_button_click")
    async def help_listener(self, inter: disnake.MessageInteraction):
        '''Listener for buttons'''
        if inter.component.custom_id not in ["1", "2"]:
            return
        
        if inter.component.custom_id == "1":
            embed = disnake.Embed(
                title='Description:',
                color=disnake.Colour.gold()
            )
            embed.add_field(name="Hey, Hope you are doing well. This is a bot made with disnake and We are trying to create a cool bot which can do most of the moderation and normal stuff. It only uses slash commands and listening commands.", value='\u200b')
            await inter.response.send_message(embed=embed)
            
        elif inter.component.custom_id == "2":
            embed = disnake.Embed(
                title="Contribution:",
                color=disnake.Colour.gold()
            )
            embed.add_field(name="Our bot is open source and you can use the code to make your own bots or contribute which is really appreciated. More slash commands will be added in the future. Check it out: https://github.com/AkhilProto/Akhils-Servant-Discord-Bot", value='\u200b')
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