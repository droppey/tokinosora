from discord.ext import commands
import random

class ctx(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(ctx(bot))