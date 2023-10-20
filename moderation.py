#Will include the moderation commands like ban, kick, timeout etc.
import disnake
import asyncio
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
    async def timeout(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, duration: int, reason: str):
        """
        Timeouts a user for a specified duration.
        """
        await member.timeout(duration=duration, reason=reason)
        await inter.response.defer()
        await inter.send(f"Successfully timed out {member.name} for {duration} seconds.")

    @commands.has_permissions(manage_channels=True)
    @commands.slash_command(name="create_text_channel", description='Create a text channel.')
    async def create_text_channel(self, inter: disnake.ApplicationCommandInteraction, name: str):
        """
        Create a text channel
        """
        await inter.guild.create_text_channel(name=name)
        await inter.response.defer()
        await inter.send(f"Successfully created a text channel named **{name}**.")
        
    @commands.has_permissions(manage_channels=True)
    @commands.slash_command(name="create_voice_channel", description='Create a voice channel.')
    async def create_voice_channel(self, inter: disnake.ApplicationCommandInteraction, name: str):
        """
        Create a voice channel
        """
        await inter.guild.create_voice_channel(name=name)
        await inter.response.defer()
        await inter.send(f"Successfully created a voice channel named **{name}**.")
    
    @commands.has_permissions(manage_channels=True)
    @commands.slash_command(name="create_stage_channel", description='Create a stage channel.')
    async def create_stage_channel(self, inter: disnake.ApplicationCommandInteraction, name: str):
        """
        Create a stage channel
        """
        await inter.guild.create_stage_channel(name=name)
        await inter.response.defer()
        await inter.send(f"Successfully created a stage channel named **{name}**.")

    @commands.has_permissions(manage_roles=True)
    @commands.slash_command(name="mute", description="Mute a member for a duration.")
    async def mute(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, duration: int, reason: str = "No reason provided"):
        """
        Mute a user for a specified duration.
        """
        mute_role = disnake.utils.get(inter.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await inter.guild.create_role(name="Muted", reason="Mute role needed.")
            # Add overwrites to prevent the muted role from sending messages or adding reactions.
            for channel in inter.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False, add_reactions=False)
        
        await member.add_roles(mute_role, reason=reason)
        await inter.send(f"Muted {member.name} for {duration} seconds due to: {reason}")
        
        await asyncio.sleep(duration)  # make sure to import asyncio
        await member.remove_roles(mute_role, reason="Mute duration ended.")

       
     
    
