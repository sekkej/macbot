"""

This is Discord Bot base. You can use it for free.
made by yer#7700

"""

import os
import asyncio
from discord import *
from discord.ext import commands

intents                   = Intents.default()
intents.message_content   = True
intents.members           = True

client_token = os.environ.get("https://cdn.discordapp.com/attachments/936657394962944010/1033768597526421525/unknown.png")

client = commands.Bot(command_prefix = '!', intents = intents)
client.remove_command('help')
client.is_opened_guild = True

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    print("Loading cogs...")
    await load_cogs()
    
    print("Starting client...")
    await client.start(client_token)


# Run Client
asyncio.run(main())