import random
from discord import *
from discord.ext import commands

class Checkpoint(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def open_server(self, ctx):
        try:
            self.client.is_opened_guild = True
        except Exception as e:
            print(e)

        await ctx.send("Сервер открыт!")
    
    @commands.command()
    @commands.is_owner()
    async def close_server(self, ctx):
        try:
            self.client.is_opened_guild = False
        except Exception as e:
            print(e)
        
        await ctx.send("Сервер закрыт!")

# Setup cog...
async def setup(bot):
	await bot.add_cog( Checkpoint(bot) )