import requests
import time
import json
import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import tasks

f = open("token.sensitive")
TOKEN = f.readline()
f.close()

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()
    async def on_message(self, message):
        if message.content == "add mee6":
           await message.channel.send("I'm better than that bastard.")
        if message.content == "m!furry':
            await message.channel.send(f"You are {str(random.randint(0,100))}% a furry.")
@client.tree.command(description="Tells you how much of a furry you are :3")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def furry(interaction: discord.Interaction,):
   await interaction.response.send_message(content=f"You are {str(random.randint(0,100))}% a furry.")      
intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(TOKEN)
