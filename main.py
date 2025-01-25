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
        if message.content == "m!furry":
            await message.channel.send(f"You are {str(random.randint(0,100))}% a furry.")

intents = discord.Intents.all()
client = MyClient(intents=intents)

@client.tree.command(description="Tells you how much of a furry you are :3")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def furry(interaction: discord.Interaction):
    furrypercent = random.randint(0,100)
    if interaction.user.name == "aroacenerd" or interaction.user.name == "tjc472" or interaction.user.name == "tjitalianprosciuttoidk." :
        furrypercent = 100
    await interaction.response.send_message(content=f"You are {str(furrypercent)}% a furry.")
    
client.run(TOKEN)

#below this point nothin is guaranteed to work, this is an abomination of stack overflow code and modifications i made without knowing wether they work or no

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await message.channel.send('Syntax error')
    if isinstance(error, commands.MissingPermissions):
        await message.channel.send("Admin permission required")


@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run(TOKEN)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason = None):\
    if not reason:
        await user.kick()
        await ctx.send(f"{user} has been kicked. No reason was provided.")
    else:
        await user.kick()
        await ctx.send(f"{user} has been kicked for {reason}")

client.run(TOKEN)


        
