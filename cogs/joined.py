from discord import *
from discord.ext import commands

class Joined(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.client.is_opened_guild:
            guild = await self.client.fetch_guild(1022425443070128218)
            role  = guild.get_role(1022429085667958804)

            await member.add_roles(role)

# Setup cog...
async def setup(bot):
	await bot.add_cog( Joined(bot) )