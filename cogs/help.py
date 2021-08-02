from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("```Copypasta類：cbt , jojo , meme , wtm , 約嗎\n\n實用類：purge , say , sayd , spam , help\n\n選擇權評價(Black Scholes)：call , put (Spot , Strike , Time_to_Maturity , Interest_Rate , Sigma)\n\n數學：dty (Day to Year)\n\n你也許用不了類：load , reload , unload```")

def setup(bot):
    bot.add_cog(help(bot))