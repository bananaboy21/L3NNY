import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class info:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def stats(self, ctx):
        """My Stats"""       
        color = discord.Color(value=0xffffff)
        em = discord.Embed(color=color, title='Bot Stats')
        em.description = "Info:"
        em.set_thumbnail(url="N/A")        
        em.add_field(name='Creator', value='TheEmperor™#2644')
        em.add_field(name='Servers', value=f'{len(self.bot.guilds)} servers') 
        em.add_field(name='Version', value='V 0.0.9')
        em.add_field(name='Date Launched', value='2/08/2018')
        em.add_field(name='Bot Region', value='North America')
        em.add_field(name='Code Platform', value='N/A')
        em.add_field(name='Hosting Platform', value='Heroku')
        em.add_field(name='Coding Language', value='Python, discord.py')      
        await ctx.send(embed=em)
        
        

def setup(bot): 
    bot.add_cog(info(bot))
