import random
import json
from transliterate import translit
from discord import *
from discord.ext import commands

class NeegorLanguage(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open('neegor_language', 'r', encoding='utf-8') as language:
            self.lang = json.loads(language.read())

    async def translate(self, *, text):
        result = text.lower()

        for syl, trn in self.lang.items():
            result = result.replace(syl, trn)

        result = translit(result, 'ru', reversed=True).replace('\'', '')

        return result

    @commands.command(aliases=["ne_egor", "nglang"])
    async def neegor(self, ctx, *, text):
        translated = await self.translate(text)

        await ctx.send(translated)

# Setup cog...
async def setup(bot):
	await bot.add_cog( NeegorLanguage(bot) )