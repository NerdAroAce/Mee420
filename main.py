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

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        await self.tree.sync()

    async def on_message(self, message):
        if message.content == "add mee6":
           await message.channel.send("I'm better than that bastard.")
        if message.content == "m!furry":
            await message.channel.send(f"You are {str(random.randint(0,100))}% a furry.")

intents = discord.Intents.all()
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
    await member.kick(reason=reason)
    if reason:
        await interaction.response.send_message(content=f"{member} was kicked for {reason}")
    else:
        await interaction.response.send_message(content=f"{member} was kicked. No reason was provided.")

@client.tree.command(description="Bans a member")
@commands.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    await member.ban(reason=reason)
    if reason:
        await interaction.response.send_message(content=f"{member} was banned for {reason}")
    else:
        await interaction.response.send_message(content=f"{member} was banned. No reason was provided.")

@client.tree.command(description="Unbans a user")
@commands.has_permissions(administrator=True)
async def uban(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    await member.unban
    if reason:
        await interaction.response.send_message(content=f"{member} was unbanned. Admin note: {reason}")
    else:
        await interaction.response.send_message(content=f"{member} was unbanned.")
        
client.run(TOKEN)
