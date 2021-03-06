import numpy as np
import scipy.stats as si
import sympy as sy
from sympy import init_printing
from tkinter import *
from functools import partial
from discord.ext import commands

def fcall(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = format((S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)), '.2f')
    
    return call

def fput(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    put = format((K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0)), '.2f')
    
    return put

def fdty(D):

    Y = format(D/365, '.5f')
    return Y

class optionpricing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def call(self, ctx, S: float, K: float, T: float, r: float, sigma: float):
        await ctx.send(f'Price: {fcall(S, K, T, r, sigma)}')

    @commands.command()
    async def put(self, ctx, S: float, K: float, T: float, r: float, sigma: float):
        await ctx.send(f'Price: {fput(S, K, T, r, sigma)}')


    @commands.command()
    async def dty(self, ctx, d : float):
        await ctx.send(f'{fdty(d)}')

def setup(bot):
    bot.add_cog(optionpricing(bot))


