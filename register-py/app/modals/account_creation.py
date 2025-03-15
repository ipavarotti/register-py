import discord
from discord import ui
from app.database import create_user
from utils.password_utils import hash_password

class AccountCreationModal(ui.Modal, title='Criar uma nova conta'):
    name_input = ui.TextInput(label='Informe seu nome', placeholder='Informe seu nome', required=True)
    login_input = ui.TextInput(label='Informe seu login', placeholder='Informe seu login', required=True)
    email_input = ui.TextInput(label='Informe seu email', placeholder='Informe seu email', required=True)
    password_input = ui.TextInput(label='Informe uma senha', placeholder='Informe uma senha', required=True, style=discord.TextStyle.short)
    confirm_password = ui.TextInput(label='Confirme sua senha', placeholder='Confirme sua senha', required=True, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        if self.password_input.value != self.confirm_password.value:
            await interaction.response.send_message("As senhas não coincidem. Tente novamente.", ephemeral=True)
            return

        hashed_password = hash_password(self.password_input.value)
        
        success, result = create_user(
            name=self.login_input.value,
            passwd=hashed_password,
            truename=self.name_input.value,
            email=self.email_input.value,
            passwd2=hashed_password
        )
        
        if success:
            await interaction.response.send_message(f"Conta criada com sucesso! Sua ID de conta é: {result}", ephemeral=True)
        else:
            await interaction.response.send_message(f"Erro ao criar a conta: {result}", ephemeral=True)

class AccountButton(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @ui.button(label="Criar Conta", style=discord.ButtonStyle.primary, custom_id="create_account")
    async def create_account(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.send_modal(AccountCreationModal())