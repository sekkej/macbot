import random
from discord import *
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["serverinfo", "guildinfo"])
    async def info(self, ctx):
        embed = Embed(title = f'Статистика по серверу', colour = 0xf2525a)

        embed.add_field(name='Участники:', value=len(ctx.guild.members))
        embed.add_field(name='Бустеры:', value=len(ctx.guild.premium_subscribers))
        embed.add_field(name='Идентификатор:', value=ctx.guild.id)
        embed.add_field(name='Уровень верификации:', value=ctx.guild.verification_level)
        embed.add_field(name='Включено КПП:', value=not self.client.is_opened_guild)
        embed.add_field(name='Создана:', value=ctx.guild.created_at)

        embed.set_footer(text = ctx.author, icon_url = ctx.author.avatar.url)
        await ctx.send(embed=embed)

# Setup cog...
async def setup(bot):
	await bot.add_cog( Info(bot) )