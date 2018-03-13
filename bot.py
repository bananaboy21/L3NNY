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


def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n') 


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name="_help"))       
        
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
    """Gives you a websocket latency."""
    color = discord.Color(value=0xffffff)
    em = discord.Embed(color=color, title='Thanks for the interest! Link:')
    em.description = f"https://discord.gg/zzzJAKM"
    await ctx.send(embed=em)

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
async def nsfw(ctx):
    """TRUST ME WITH THIS"""
    await ctx.send ("Well... Here ya go! https://xvide.... wait a sec... :thinking: WHAT ARE YOU DOING WITH ME? EWWWWW! GET THAT OUTTA HERE!")
   
    
@bot.command()
async def upvote(ctx):
    """Upvote me!"""
    await ctx.send ("Upvote me here! https://discordbots.org/bot/414456650519412747") 
    
@bot.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, num: int = None):
	"""Deletes messages. _purge [number].""" 
	try: 
	    if num is None:
	        await ctx.send("How many messages would you like me to delete? Usage: _purge [number]")
	    else:
	        try:
	            float(num)
	        except ValueError:
	            return await ctx.send("The number is invalid. Make sure it is a number...")
	        await ctx.channel.purge(limit=num+1)
	        msg = await ctx.send(f"Done ( ͡° ͜ʖ ͡°)")
	        await asyncio.sleep(3)
	        await msg.delete()
	except discord.Forbidden:
	    await ctx.send("OoF! I don't have **Manage Messages** permission.")
	
               
@bot.command()
async def say(ctx, *, message:str):
    """Speak as me!"""
    await ctx.message.delete()
    await ctx.send(message)      

    
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.Member = None):
	"""Kicks a member from the server."""
	if user is None:
		await ctx.send("Please tag the rebel to kick them!")
	else:
		try:
			await user.kick()
			await ctx.send(f"The administrator is putting on his boot. He kicks {user.mention} in the rear end. {user.mention} got kicked!.")
		except discord.Forbidden:
			await ctx.send("OoF! I'm missing **kick** permmision.")
	
	
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member = None):
	"""Bans a member from the server."""
	if user is None:
		await ctx.send("Please tag that **intense** rebel to ban!")
	else:
		try:
			await user.ban()
			await ctx.send(f"The administrator is getting the ban hammer out of the case. He swings it at {user.mention}. Ouch! {user.mention} has been banned.")
		except discord.Forbidden:
			await ctx.send("OOOOF! You didn't give me the **ban** permission.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, user: discord.Member = None):
    '''Mutes a user'''
    if user is None:
    	return await ctx.send("Please tag that annoying user to mute them!")
    try:
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"{user.mention} has been muted. FINALLY!")
    except discord.Forbidden:
        return await ctx.send(":x: I don't have **Manage Channel** permmition.")  


@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, user: discord.Member = None):
	'''Un-mutes a user'''
	if user is None:
		return await ctx.send("Please tag a uesr to unmute them!")
	try:
		await ctx.channel.set_permissions(user, send_messages=True)
		await ctx.send(f"{user.mention} is now unmuted. Hope they learned their lesson.")
	except discord.Forbidden:
		await ctx.send(":x: Couldn't unmute the user. I need the **Manage Channels** permission.")
  
@bot.command()
async def github(ctx):
    """Get my github repo"""
    await ctx.send("Here is my github: http://bit.ly/2ogUv2T")

@bot.command()
async def lit(ctx):
    """You lit? Use this command!"""
    await ctx.send("**Only the lit people can listen to this! http://bit.ly/2r3aFyX**")	


if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
