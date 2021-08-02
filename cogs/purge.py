from discord.ext import commands

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amount = 6):
        await ctx.channel.purge(limit = amount + 1)

def setup(bot):
    bot.add_cog(purge(bot))