from discord import *
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Ready(bot) )