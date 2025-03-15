import discord
from discord.ext import commands
from app.modals.account_creation import AccountButton

def setup_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')
        bot.add_view(AccountButton())
        print('Persistent views loaded')
        print('------')
    
    @bot.command()
    async def register(ctx):
        """Command to display the registration embed with button"""
        embed = discord.Embed(
            title="Registrar Conta - Perfect World",
            description="Clique no botão abaixo para criar uma nova conta",
            color=discord.Color.blue() #cor da embed
        )

        embed.set_footer(text="© 2025 Perfect World. Todos os direitos reservados.")
        embed.set_image(url="https://example.com/your-image.png")
        
        await ctx.send(embed=embed, view=AccountButton())
    
    return bot
