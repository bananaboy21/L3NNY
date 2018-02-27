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
        await bot.change_presence(game=discord.Game(name="V 0.0.7"))
        await asyncio.sleep(10)
        
    
    
@bot.event
async def on_guild_join(guild):
    lol = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xffffff))
    em.title = "L3NNY has arrived in a new server!"
    em.description = f"Server: {guild}"
    await lol.send(embed=em)
    await ctx.send(f"Ello, my dudes in **{guild.name}**! Thanks for inviting me! I am L3NNY, you probialy know that already by my name. Try _help for my command list.")
    
@bot.event
async def on_guild_remove(guild):
    lol = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "L3NNY has left a server."
    em.description = f"Server: {guild}"
    await lol.send(embed=em)

    
@bot.command()
async def support(ctx):
    """Join my discord server!"""
    await ctx.send ("Here is our discord: https://discord.gg/zzzJAKM")

@bot.command()
async def ping(ctx):
    """Gives you a websocket latency."""
    color = discord.Color(value=0xffffff)
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
    """Deletes a # of msgs. *purge [# of msgs].""" 
    try: 
        if num is None:
            await ctx.send("Deletes messages. Usage: _purge [number]")
        else:
            try:
                float(num)
            except ValueError:
                return await ctx.send("The number is invalid. Make sure it is valid! Usage: *purge [number of msgs]")
            await ctx.channel.purge(limit=num+1)
            await ctx.send("Done ( ͡° ͜ʖ ͡°)")
    except discord.Forbidden:
        await ctx.send("Purge unsuccessful. The bot does not have Manage Msgs permission.")
	
               
@bot.command()
async def say(ctx, *, message:str):
    """Speak as me!"""
    await ctx.message.delete()
    await ctx.send(message)      

    
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.Member):
    """Kicks a member out of this c00l clUb of yours"""
    await ctx.send(f"The administrator is putting on his boot. He puts it on and kicks **{user.name}** in the rear end. **{user.name}** has been kicked.")
    await user.kick()

    
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member):
    """Bans a member from this c00l club"""
    await ctx.send(f"The administraor is getting a hold of his ban hammer. He swings it at **{user.name}**. **{user.name}** has been banned.")
    await user.ban()

    
@bot.command()
async def github(ctx):
    """Get my github repo"""
    await ctx.send("Here is my github: http://bit.ly/2ogUv2T")

@bot.command()
async def help(ctx, command=None):
	if command is None:
		color = discord.Color(value=0xffffff)
		em = discord.Embed(color=color, title='My Commands')
		em.description = 'Thanks for using me. Here are my commands...'
		em.add_field(name="ping", value="Get a websocket latency.")
		em.add_field(name="ban", value="Bans a member from the server.")
		em.add_field(name="kick", value="Kicks a member from the server.")
                em.add_field(name="invite", value="Invites me to your server.")
                em.add_field(name="say", value="Speak as me! Usage: _say [msg].")
		em.add_field(name="github", value="Gives you my Github repo.")
                em.add_field(name="upvote", value="Upvote me.")
                em.add_field(name="support", value="Joins the support server") 
		em.set_thumbnail(url='https://cdn.discordapp.com/avatars/414456650519412747/ede4bd62db1db6719bbbda4aa78a9344.webp?size=1024')


if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
