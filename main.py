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
    """Copy pasted from random github repo"""
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()
    async def on_message(self, message):
        if message.content == "hewwo":
           await message.channel.send("hewwo :3")
        
intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(TOKEN)
