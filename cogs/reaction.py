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

        if msg.content == '相比西南第一高中的大學長，輸了輸了QQ':
                await msg.channel.send('幹破您娘機掰 高雄學店被您屌虐')
                await msg.add_reaction('🖕')
                await msg.add_reaction('<:Seya0:871252213488582676>')
                
        if msg.content == '您真愛說笑，關西電神':
                await msg.channel.send('宜中電神瘋起來連自己都嘲諷 哀')
                await msg.add_reaction('<:ran:869589093372289084>')
        
        if msg.content == '切嚕':
            prob = random.randrange(11)
            if prob == 10:
                await msg.channel.send("再吵琪愛兒就把你們的切嚕洞塞進切嚕讓你們切嚕齒打顫得切嚕切嚕\n切嚕切嚕，切嚕啪，切嚕嚕嚕嚕♪\n切啦嚕咧，切啦切啦，切嚕切啵啪嗶~♪\n切嚕~☆切啦哩咧，切嚕啵嗶，切啦嚕啵啵\n切嚕切嚕，切嚕啪，切嚕嚕嚕嚕♪\n切嚕☆切嚕☆切嚕☆\n切嚕切嚕，切嚕啪，切嚕嚕嚕嚕♪\n切嚕~☆切啦哩咧，切嚕啵嗶，切啦嚕啵啵")
            else: 
                await msg.channel.send('切啦嚕咧，切啦切啦，切嚕切啵啪嗶~♪')


        if msg.content == '電' or msg.content == '電神' or msg.content == '⚡' or msg.content == 'electric' or msg.content == 'zap' :
            prob = random.randrange(11)
            author = msg.author.id
            if author == 366865049949569024:
                await msg.channel.send("⚡⚡電⚡⚡")
            elif prob == 10:
                await msg.channel.send(f'好了啦<@{author}>, 您別再謙虛啦')
                await msg.channel.send(f'https://cdn.discordapp.com/attachments/870138830949322783/871658780994207784/e59f99e3afae06b6.png')
                await msg.add_reaction('❓')
            else:
                await msg.add_reaction('❓')


        if msg.content == 'tf':
            author = msg.author.id
            await msg.channel.send(f'<@{author}>講人話喇幹')
            await msg.add_reaction('❓')

        if msg.content == '?' or msg.content == '???' or msg.content == '？':
            prob = random.randrange(11)
            if prob == 10:
                author = msg.author
                await msg.channel.send(f'問號沙小，不會講話？')
                await msg.add_reaction('❓')
            else:
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
                await msg.channel.send(f'好油ㄛ，我都不看這些的Peko <:ha:869872948503257101>')
            await msg.add_reaction('🈳')
            await msg.add_reaction('🇵')
            await msg.add_reaction('🇪')
            await msg.add_reaction('🇰')
            await msg.add_reaction('🇴')


def setup(bot):
    bot.add_cog(reaction(bot))