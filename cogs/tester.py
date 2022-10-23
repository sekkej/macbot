import random
from discord import *
from discord.ext import commands

class Tester(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["testme", "test_me"])
    async def test(self, ctx, *, text):
        await ctx.send(f"Я уверен что вы {text} на {random.randint(0,100)}%")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Tester(bot) )