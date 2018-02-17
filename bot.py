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
from contextlib import redirect_stdout
from discord.ext import commands
import json
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'),description="TheEmperor™'s Discord bot.\n\nHelp Commands",owner_id=250674147980607488)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name="_help"))
    
    
@bot.command()
async def ping(ctx):
    """Gives you a websocket latency."""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)
    
@bot.command()
async def invite(ctx):
    """lets me join ur clUb"""
    await ctx.send ("Lemme join dat club: https://discordapp.com/api/oauth2/authorize?client_id=414456650519412747&permissions=0&scope=bot")
    
    
    @bot.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, num: int):
    """Deletes msgs. _purge [how many msgs].""" 
    try: 
        if num is None:
            await ctx.send("How many messages would you like me to delete? Usage: _purge [number of msgs]")
        else:
            try:
                float(num)
            except ValueError:
                return await ctx.send("The number is invalid. Make sure it is valid! Usage: *purge [number of msgs]")
            await ctx.channel.purge(limit=num+1)
            await ctx.send("Done :ok_hand:")
    except discord.Forbidden:
        await ctx.send("Unable to purge. I don't have Manage Messages permission.")
    
if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
