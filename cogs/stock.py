import requests
import pandas as pd
import numpy as np
import datetime
from discord.ext import commands
import discord

def conv_to_list(obj):
    '''
    將物件轉換為list
    '''
    if not isinstance(obj, list) :
        results = [obj]
    else:
        results = obj
    return results


def df_conv_col_type(df, cols, to, ignore=False):
    '''
    一次轉換多個欄位的dtype
    '''
    cols = conv_to_list(cols)
    for i in range(len(cols)):
        if ignore :
            try:
                df[cols[i]] = df[cols[i]].astype(to)
            except:
                print('df_conv_col_type - ' + cols[i] + '轉換錯誤')
                continue
        else:
            df[cols[i]] = df[cols[i]].astype(to)
    return df


def date_get_today(with_time=False):
    '''
    取得今日日期，並指定為台北時區
    '''
    import pytz
    central = pytz.timezone('Asia/Taipei')
    
    if with_time == True:
        now = datetime.datetime.now(central)
    else:
        now = datetime.datetime.now(central).date()
    return now


# 下載證交所資料 ------
link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
data = pd.read_csv(link)
 
# ['證券代號', '證券名稱', '成交股數', '成交金額', '開盤價',
#  '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data.columns = ['STOCK_SYMBOL', 'NAME', 'VOLUME', 'TRADE_VALUE', 
                'OPEN', 'HIGH' ,'LOW', 'CLOSE', 'PRICE_CHANGE', 'TRANSACTION']   
# 標註今日日期
data['WORK_DATE'] = date_get_today()

cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]

# 除了證券代號外，其他欄位都是str，且部份資料中有''
data = data.replace('', np.nan, regex=True)

# 將data type轉為float
data = df_conv_col_type(df=data, 
                        cols=['VOLUME', 'TRADE_VALUE', 'OPEN', 'HIGH' ,'LOW',
                              'CLOSE', 'PRICE_CHANGE', 'TRANSACTION'],
                        to='float')

data = data.drop(['TRADE_VALUE', 'OPEN', 'HIGH', 'LOW', 'TRANSACTION'], axis=1)

class stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stock')
    async def stock(self, ctx, stock = None):
        if stock == None: return await ctx.send("🈹，你的股票代碼要給。")
        bruh = ("%.2f%%" % (100 * float(data.loc[data['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False)) / (float(data.loc[data['STOCK_SYMBOL'] == stock].CLOSE.to_string(index=False)) + float(data.loc[data['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False)))))
        embed = discord.Embed(title=(data.loc[data['STOCK_SYMBOL'] == stock].NAME.to_string(index=False)), description= (str(stock)), colour=np.random.randint(0, 16777215))
        embed.add_field(name="日期", value=date_get_today(), inline=False)
        embed.add_field(name="成交股數", value=data.loc[data['STOCK_SYMBOL'] == stock].VOLUME.to_string(index=False), inline=False)
        embed.add_field(name="收盤價", value=data.loc[data['STOCK_SYMBOL'] == stock].CLOSE.to_string(index=False), inline=False)
        embed.add_field(name="漲跌", value=data.loc[data['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False), inline=False)
        embed.add_field(name="漲跌幅", value=bruh, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/852190878951931924/872040448699543582/Ankimochan.png")
        embed.set_footer(text="資料 from 台灣證券交易所,\n整理 by 愛你的小空❤️", icon_url="https://cdn.discordapp.com/attachments/852190878951931924/872039546253082684/sora.jpg")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(stock(bot))