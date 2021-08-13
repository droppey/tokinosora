from discord.ext import commands
import discord
import twstock
import time
        
cmd = True
class rtstock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rtstock(self, ctx, stock=None, times=None):
        if stock==None:
            await ctx.channel.send("?????")
        if stock in twstock.codes:
            if times == None:
                global cmd
                cmd = True

                while cmd == True:
                    if not cmd:
                        break
                    rtstock = twstock.realtime.get(stock)['realtime']
                    await ctx.channel.send(rtstock['latest_trade_price'])
                    time.sleep(5)
            else:
                for i in range(int(times)):
                    rtstock = twstock.realtime.get(stock)['realtime']
                    await ctx.channel.send(rtstock['latest_trade_price'] + ', ' + str(i))
                    time.sleep(5)
        if not stock in twstock.codes and stock != None:
            await ctx.channel.send("???")
    @commands.command()
    async def stoprtstock(self, ctx):
        global cmd
        cmd = False
        await ctx.send('Stopped.')

def setup(bot):
    bot.add_cog(rtstock(bot))