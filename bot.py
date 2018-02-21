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
    while True:
        await bot.change_presence(game=discord.Game(name=f"with {len(bot.guilds)} servers!"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="_help"))
        await asyncio.sleep(10)
    
@bot.command()
async def server(ctx):
    """Join my discord server!"""
    await ctx.send ("Here is our discord: https://discord.gg/WewwYV5")

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
async def upvote(ctx):
    """Upvote me!"""
    await ctx.send ("Upvote me here! https://discordbots.org/bot/414456650519412747") 
    
@bot.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, num: int):
    """Deletes msgs. Usage: _purge [number]""" 
    try: 
        if num is None:
            await ctx.send("How many messages would you like me to delete? Usage: _purge [number of msgs]")
        else:
            try:
                float(num)
            except ValueError:
                return await ctx.send("The number is invalid. Make sure it is valid! Usage: _purge [number of msgs]")
            await ctx.channel.purge(limit=num+1)
            await ctx.send("Done :ok_hand:")
    except discord.Forbidden:
        await ctx.send("Unable to purge. I don't have Manage Messages permission.")
        
        
@bot.command()
async def say(ctx, *, message:str):
    """Speak as me!"""
    await ctx.message.delete()
    await ctx.send(message)      

    
@bot.command()
async def credits(ctx):
    """Roll thee credits!."""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Credits:')
    em.description = f"TheEmperor™#2644 and a little help from dat banana boi#1982."
    await ctx.send(embed=em)

    
@bot.event
async def on_guild_join(guild):
    lol = bot.get_channel(415660022488367105)
    em = discord.Embed(color=discord.Color(value=0xffffff))
    em.title = "I has joined a server:"
    em.description = guild
    await lol.send(embed=em)

if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
