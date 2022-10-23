import random
from discord import *
from discord.ext import commands

class Swear(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.swears = open('swears', 'r', encoding='UTF-8').read().splitlines()
        self.vowels = 'уеыаоэяию'

    @commands.command(aliases=["swr", "genswr"])
    async def swear(self, ctx, word1=None, word2=None):
        if not word1 == None:
            w1 = word1
        else:
            w1 = random.choice(self.swears)

        if not word2 == None:
            w2 = word2
        else:
            w2 = random.choice(self.swears)
        
        if w1[ len(w1)-1 ] in self.vowels:
            result = w1 + w2
        else:
            result = w1 + random.choice(['е', 'о']) + w2
        
        await ctx.send(f"{ctx.author.name}, вот ваша обзывалка: `{result}`")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Swear(bot) )