#Will include the moderation commands like ban, kick, timeout etc.
import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #commands start from here.
        
    @commands.has_permissions(ban_members=True)
    @commands.slash_command(name='ban', description='Ban a particuler member.')
    async def ban(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        """Ban the given user"""
        await inter.guild.ban(user, delete_message_days=0)
        await inter.send(f"Banned {user}")
    
    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name='kick', description='Kick a particular member.')
    async def kick(self, inter:disnake.ApplicationCommandInteraction, user:disnake.Member):
        """Kick the given user"""
        await inter.guild.kick(user)
        await inter.send(f"Kicked {user}")
    
    @commands.has_permissions(manage_messages=True)
    @commands.slash_command(name='clear', description='Clear a certain amount of messages.')
    async def clear(self, inter:disnake.ApplicationCommandInteraction, amount: int):
        """Clears messages"""
        
        await inter.channel.purge(limit=amount)
        await inter.response.defer()
        await inter.response.send_message('Messages Cleared.')
        
    
    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name="timeout", description='Timeout a member')
    async def timeout_command(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, duration: int, reason: str):
        """
        Timeouts a user for a specified duration.
        """
        await member.timeout(duration=duration, reason=reason)
        await inter.response.defer()
        await inter.send(f"Successfully timed out {member.name} for {duration} seconds.")