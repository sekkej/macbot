import random
from discord import *
from discord.ext import commands

class LuckyPing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["rndping", "lucky_ping"])
    async def luckyping(self, ctx, *, text):
        await ctx.send(f"{ random.choice(ctx.guild.members) } {text}")

# Setup cog...
async def setup(bot):
	await bot.add_cog( LuckyPing(bot) )