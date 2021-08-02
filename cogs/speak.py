from discord.ext import commands

class speak(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, args):
        await ctx.send(args)

    @commands.command()
    async def sayd(self, ctx, *, args):
        await ctx.channel.purge(limit=1)
        await ctx.send(args)
    
    @commands.command()
    async def spam(self, ctx, amount = 10, *, args):
        i = 0
        while i != amount:
            await ctx.send(f'{args}\n')
            i = i+1
            
def setup(bot):
    bot.add_cog(speak(bot))