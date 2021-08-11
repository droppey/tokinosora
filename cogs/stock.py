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

link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
data = pd.read_csv(link)
 
data.columns = ['STOCK_SYMBOL', 'NAME', 'VOLUME', 'TRADE_VALUE', 
                'OPEN', 'HIGH' ,'LOW', 'CLOSE', 'PRICE_CHANGE', 'TRANSACTION']   

data['WORK_DATE'] = date_get_today()

cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]

data = data.replace('', np.nan, regex=True)

data = df_conv_col_type(df=data, 
                        cols=['VOLUME', 'TRADE_VALUE', 'OPEN', 'HIGH' ,'LOW',
                              'CLOSE', 'PRICE_CHANGE', 'TRANSACTION'],
                        to='float')

data = data.drop(['TRADE_VALUE', 'OPEN', 'HIGH', 'LOW', 'TRANSACTION'], axis=1)

link2 = 'http://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php?l=zh-tw&o=data'
data2 = pd.read_csv(link2)
 
data2.columns = ['DATE', 'STOCK_SYMBOL', 'NAME', 'CLOSE', 'PRICE_CHANGE', 
                'OPEN', 'HIGH' ,'LOW', 'AVG', 'VOLUME', 'TRADE_VALUE',
                'a', 'b', 'c', 'd', 'e', 'f', 'g']   

data2 = data2.drop(['DATE', 'TRADE_VALUE', 'OPEN', 'HIGH', 'LOW', 'TRADE_VALUE', 'AVG', 'a', 'b', 'c', 'd', 'e', 'f', 'g'], axis=1)
data2['WORK_DATE'] = date_get_today()

cols = data2.columns.tolist()
cols = cols[-1:] + cols[:-1]
data2 = data2[cols]

data2 = data2.replace('', np.nan, regex=True)

data = df_conv_col_type(df=data, 
                        cols=['VOLUME', 'CLOSE', 'PRICE_CHANGE'],
                        to='float')

class stock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stock')
    async def stock(self, ctx, stock = None):
        if stock == None: return await ctx.send("🈹，你的股票代碼要給。")
        if stock in data.values:
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
        elif stock in data2.values:
            bruh = ("%.2f%%" % (100 * float(data2.loc[data2['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False)) / (float(data2.loc[data2['STOCK_SYMBOL'] == stock].CLOSE.to_string(index=False)) + float(data2.loc[data2['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False)))))
            embed = discord.Embed(title=(data2.loc[data2['STOCK_SYMBOL'] == stock].NAME.to_string(index=False)), description= (str(stock)), colour=np.random.randint(0, 16777215))
            embed.add_field(name="日期", value=date_get_today(), inline=False)
            embed.add_field(name="成交股數", value=data2.loc[data2['STOCK_SYMBOL'] == stock].VOLUME.to_string(index=False), inline=False)
            embed.add_field(name="收盤價", value=data2.loc[data2['STOCK_SYMBOL'] == stock].CLOSE.to_string(index=False), inline=False)
            embed.add_field(name="漲跌", value=data2.loc[data2['STOCK_SYMBOL'] == stock].PRICE_CHANGE.to_string(index=False), inline=False)
            embed.add_field(name="漲跌幅", value=bruh, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/852190878951931924/872040448699543582/Ankimochan.png")
            embed.set_footer(text="資料 from 櫃檯買賣中心,\n整理 by 愛你的小空❤️", icon_url="https://cdn.discordapp.com/attachments/852190878951931924/872039546253082684/sora.jpg")
            await ctx.send(embed=embed)
        else:
            await ctx.send('幹！這根本不是股票代碼！')
def setup(bot):
    bot.add_cog(stock(bot))