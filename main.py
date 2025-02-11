import requests
import time
import json
import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import tasks

with open("token.sensitive") as f:
    TOKEN = f.readline().strip()

intents = discord.Intents.all()

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        await self.tree.sync()

    async def on_message(self, message):
        if message.content == "add mee6":
           await message.channel.send("I'm better than that bastard.")
        if message.content == "m!help":
            await message.channel.send(f"List of entertainment commands (the prefix is 'm!'. Commands should be typed as following 'm!*command*': furry, d20")
        if message.content == "m!furry":
            await message.channel.send(f"You are {str(random.randint(0,100))}% a furry.")
        if message.content == "m!d20":
            d20r = random.randint(1,20)
            if (d20r == 1):
                await message.channel.send(content=f"Unlucky, you rolled a nat 1...")
            else:
                if (d20r == 20):
                    await message.channel.send(content=f"Damn, that's a nat 20!")
                else:
                    await message.channel.send(content=f"You rolled a {str(d20r)}.")

client = MyClient(intents=intents)

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'Logged in as {client.user}')

@client.tree.command(description="Tells you how much of a furry you are :3")
async def furry(interaction: discord.Interaction):
    furrypercent = random.randint(0,100)
    if interaction.user.name in ["aroacenerd", "tjc472", "tjitalianprosciuttoidk."]:
        furrypercent = 100
    await interaction.response.send_message(content=f"You are {str(furrypercent)}% a furry.")

@client.tree.command(description="Kicks a member")
@commands.has_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    if not interaction.guild.me.guild_permissions.kick_members:
        await interaction.response.send_message(content="I don't have permission to kick members.")
        return
    if member.top_role >= interaction.guild.me.top_role:
        await interaction.response.send_message(content="I cannot kick a user with a role higher than mine")
        return
    await member.kick(reason=reason)
    if reason:
        await interaction.response.send_message(content=f"{member} was kicked for {reason}")
    else:
        await interaction.response.send_message(content=f"{member} was kicked. No reason was provided.")

@kick.error
async def kick_error(interaction: discord.Interaction, error):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(content="You don't have permission to kick members.")

@client.tree.command(description="Bans a member")
@commands.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    if not interaction.guild.me.guild_permissions.ban_members:
        await interaction.response.send_message(content="I don't have permission to ban members.")
        return
    if member.top_role >= interaction.guild.me.top_role:
        await interaction.response.send_message(content="I cannot ban a user with a role higher than mine")
        return
    await member.ban(reason=reason)
    if reason:
        await interaction.response.send_message(content=f"{member} was banned. Reason: {reason}")
    else:
        await interaction.response.send_message(content=f"{member} was banned. No reason was provided.")

@ban.error
async def ban_error(interaction: discord.Interaction, error):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(content="You don't have permission to ban members.")

@client.tree.command(name="uban", description="Unbans a user")
@commands.has_permissions(ban_members=True)
async def uban(interaction: discord.Interaction, user: discord.User, reason: str = None):
    guild = interaction.guild
    if not guild.me.guild_permissions.ban_members:
        await interaction.response.send_message(content="I don't have permission to unban members.")
        return
    await guild.unban(user, reason=reason)
    if reason:
        await interaction.response.send_message(content=f"{user} was unbanned. Admin note: {reason}")
    else:
        await interaction.response.send_message(content=f"{user} was unbanned.")

@uban.error
async def uban_error(interaction: discord.Interaction, error):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(content="You don't have permission to unban members.")

client.run(TOKEN)
