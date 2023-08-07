import disnake
from disnake.ext import commands
from disnake import errors

class Error_handler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.CommandInteraction, error) -> None:
        error = getattr(error, 'original', error)
        embed = disnake.Embed(
            description='Hmm....',
            title='Error Message',
            color= disnake.Colour.green()
        )

        # MissingPermissions
        if isinstance(error, commands.errors.MissingPermissions) or isinstance(
            error, errors.Forbidden
        ):
            embed.title = 'Nice try! I don\'t have permission to do that.'

        # MissingRole
        elif isinstance(error, commands.errors.MissingRole) or isinstance(
            error, commands.errors.MissingAnyRole
        ):
            embed.title = 'Whoops! Seems like you are missing something.'

        else:
            embed.title = 'Hmm, an error occured!'
            
        await inter.send(embed=embed)