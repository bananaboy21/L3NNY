    import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
import textwrap
from .utils.paginator import Pages
from discord.ext import commands


class Utility:
    def __init__(self, bot):
       self.bot = bot
       

    @commands.command()
    async def urban(self, ctx, *, word=None):
        if word is None:
            await ctx.send("The great Urban Dictonary. Usage: _urban (word)")
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://api.urbandictionary.com/v0/define?term={word}') as resp:
                    r = await resp.json()
                    color = discord.Color(value=0xffffff)
                    em = discord.Embed(color=color, title=f'Urban Dictionary: {word}')
                    lol = []
                    for x in r['list']:
                        lol.append(f"{x['definition']} \n\n*{x['example']}* \n\n**Votes**\n:thumbsup: {x['thumbs_up']}  :thumbsdown: {x['thumbs_down']} \n\nDefinition written by {x['author']}")
                    ud = Pages(ctx, entries=lol, per_page=1)
                    await ud.paginate()
            
        
            
            
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.Member = None):
        """Returns a user's profile picture. Usage: _av [user tag]."""
        if user is None:
            av = ctx.message.author.avatar_url
            if '.gif' in av:
                av += "&f=.gif"
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=ctx.message.author.name)
            em.set_author(name='Profile Picture')
            em.set_image(url=av)
            await ctx.send(embed=em)                  
        else:
            av = user.avatar_url
            if '.gif' in av:
                av += "&f=.gif"
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=user.name)
            em.set_author(name='Profile Picture')
            em.set_image(url=av)
            await ctx.send(embed=em)
            
            
    @commands.command()
    async def userinfo(self, ctx, user: discord.Member = None):
        """Finf out info on someone. Usage: _userinfo [tag user]"""
        if user is None:
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=f'User Info: {ctx.message.author.name}')
            em.add_field(name='Status', value=f'{ctx.message.author.status}')       
            em.add_field(name='Account Created', value=ctx.message.author.created_at.__format__('%A, %B %d, %Y'))
            em.add_field(name='ID', value=f'{ctx.message.author.id}')
            if ctx.message.author.bot is True:
                type = 'Bot'
            else:
                type = 'Human'
            em.add_field(name='Profile Type', value=type)
            em.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.send(embed=em)
        else:
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=f'User Info: {user.name}')
            em.add_field(name='Status', value=f'{user.status}')       
            em.add_field(name='Account Created', value=user.created_at.__format__('%A, %B %d, %Y'))
            em.add_field(name='ID', value=f'{user.id}')
            if user.bot is True:
                type = 'Bot'
            else:
                type = 'Human'
            em.add_field(name='Profile Type', value=type)
            em.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=em)    
        
              
              
def setup(bot): 
    bot.add_cog(Utility(bot))              
