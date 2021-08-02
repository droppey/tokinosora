from discord.ext import commands
import random
import discord
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.content == '雄中電神':
            if msg.author == self.bot.user:
                await msg.channel.send('幹破您娘機掰 宜中,中科御用生,關西電神 一個個都比老子電')
            else:
                await msg.channel.send('您才電 哀')

        if msg.content == '電' or msg.content == '電神' or msg.content == '⚡' or msg.content == 'electric' or msg.content == 'zap' :
            prob = random.randrange(11)
            if prob == 10:
                author = msg.author.id
                await msg.channel.send(f'好了啦<@{author}>, 您別再謙虛啦')
                await msg.channel.send(f'https://cdn.discordapp.com/attachments/870138830949322783/871658780994207784/e59f99e3afae06b6.png')
                await msg.add_reaction('❓')
            else:
                await msg.add_reaction('❓')

        if msg.content == '?' or msg.content == '???' or msg.content == '？':
            prob = random.randrange(11)
            if prob == 10:
                author = msg.author
                await msg.channel.send(f'問號沙小，不會講話？')
                await msg.add_reaction('❓')
            else:
                await msg.add_reaction('❓')
            await msg.add_reaction('❓')

        if msg.content == '嗯' or msg.content == '恩':
            author = msg.author.id
            await msg.channel.send(f'<@{author}>')
            await msg.channel.send(f'https://cdn.discordapp.com/attachments/856549157278842912/871381238018080819/unknown.png')

        if msg.content.find('777') != -1:
            await msg.add_reaction('7️⃣')
            
        if msg.content.find('peko') != -1:
            prob = random.randrange(11)
            if prob == 10:
                await msg.channel.send(f'好油喔，我都不看這些的Peko <:ha:869872948503257101>')
            await msg.add_reaction('🈳')
            await msg.add_reaction('🇵')
            await msg.add_reaction('🇪')
            await msg.add_reaction('🇰')
            await msg.add_reaction('🇴')


def setup(bot):
    bot.add_cog(reaction(bot))