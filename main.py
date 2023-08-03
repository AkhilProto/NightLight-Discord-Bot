
import os
import random
import discord
import asyncio
import time
from discord.ext import commands
from keep_alive import keep_alive



keep_alive()
TOKEN = os.environ['TOKEN']
WELCOME_CHANNEL = "📫︱join―leave"
NICKS = ["Akhil's Mega Friend", "Akhil's Best Friend", "Akhil's Friend"]

intents = discord.Intents.all()
prefix = "?"

bot = commands.Bot(command_prefix = prefix, intents=intents)


@bot.event
async def on_ready():
    print("Bot started")
    bot.loop.create_task(send_message_in_private_channel())

@bot.command()
async def mathsolver(ctx):
    await calculator.main(ctx)


@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL)
    await welcome_channel.send(f"Welcome {member.mention}! Please read our rules and verify yourself at <#1130116826114826242> to access the server. Call me with a simple command ?ahelp in <#1130116826114826246> channel. Have a great time!!")


@commands.has_permissions(ban_members=True)
@bot.command()

async def ban(ctx, user: discord.Member):
    """Ban the given user"""
    await ctx.guild.ban(user, delete_message_days=0)
    await ctx.send(f"Banned {user}")

@bot.command()
async def invite(ctx):
    """Gives an already generated invite link"""
    invite_link = os.environ['INVITE_LINK']
    await ctx.send(f"Hey Mate!! Invite your friends to join our server using this link! {invite_link}")

@bot.command()
async def invitebot(ctx):
    """Gives an already generated invite link"""
    link = os.environ['BOT_INVITE_LINK']
    embed = discord.Embed(
      title="Invite me to your Server!!",
      url=link,
      description="This is a link to invite me to your server.",
    )
    await ctx.send(embed=embed)




@bot.command()
async def ahelp(ctx):
    embed = discord.Embed(title="Custom Bot Help", description="List of available commands:")
    embed.add_field(name=f"{prefix}ban <user>", value="Ban the given user.", inline=False)
    embed.add_field(name=f"{prefix}unban <user>", value="Unban the given user.", inline=False)
    embed.add_field(name=f"{prefix}kick <user>", value="Kick the given user.", inline=False)
    embed.add_field(name=f"{prefix}random_nick", value="Set your nickname to a random one.", inline=False)
    embed.add_field(name=f"{prefix}change_nick <user> <new_nick>", value="Change somebody else's nickname.", inline=False)
    embed.add_field(name=f"{prefix}ping", value="Check the bot's latency.", inline=False)
    
    await ctx.send(embed=embed)


async def send_message_in_private_channel():
    await bot.wait_until_ready()
    private_channel_id = 1131217771225681920  
    
    while not bot.is_closed():
        private_channel = bot.get_channel(private_channel_id)
        latency = bot.latency
        now = time.localtime()
        await private_channel.send(f"Reporting Roger!! The time is {now.tm_hour}:{now.tm_min}:{now.tm_sec} now. Latency: {round(latency * 1000)}ms")
        await asyncio.sleep(3600)# Sleep for 1 hour (3600 seconds)



@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, user: discord.User):
    """Unban the given user"""
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user}")


ban.autocomplete = ["ban", "kick", "mute", "deafen"]

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.User):
    """Kick the given user"""
    await ctx.guild.kick(user)
    await ctx.send(f"Kicked {user}")


@bot.command(aliases=["rnick"])
async def random_nick(ctx):
    """Set your nickname to a random one"""
    new_nick = random.choice(NICKS)
    await ctx.author.edit(nick=new_nick)
    await ctx.send(f"Your new nickname is {new_nick}")


@commands.has_permissions(manage_nicknames=True)
@bot.command(aliases=["change_name"])
async def change_nick(ctx, user: discord.Member, *, new_nick):
    """Change somebody else's nickname"""
    await user.edit(nick=new_nick)
    await ctx.send(f"Changed the nickname of {user.mention} to `{new_nick}`")


@bot.command()
async def ping(ctx):
    """Check the bot's latency"""
    latency = bot.latency
    await ctx.send(f"Pong! Latency: {round(latency * 1000)}ms")




if __name__ == "__main__":
    bot.run(TOKEN)


