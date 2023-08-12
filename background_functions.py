WELCOME_CHANNEL = {Channel name}
VERIFICATION_CHANNEL = {Channel name}
BOT-COMMANDS_CHANNEL = {Channel name}

# Automatic running events
@bot.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL)
    verification_channel = discord.utils.get(member.guild.channels, name=VERIFICATION_CHANNEL)
    bot-commands_channel = discord.utils.get(member.guild.channels, name=BOT-COMMANDS_CHANNEL)
    await welcome_channel.send(f"Welcome {member.mention}! Please read our rules and verify yourself at <#{verification_channel}> to access the server. Call me with a simple command /help in <#{bot-commands_channel}> channel. Have a great time!!")
    
