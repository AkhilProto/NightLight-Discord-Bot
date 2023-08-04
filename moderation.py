#Will include the moderation commands like ban, kick, timeout etc.
import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #commands start from here.
        
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(description='Ban a particuler member.')
    async def ban(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Ban the given user"""
        await inter.guild.ban(user, delete_message_days=0)
        await inter.send(f"Banned {user}")