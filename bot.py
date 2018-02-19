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
bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'),description="TheEmperor™'s Discord bot.\n\nHelp Commands",owner_id=250674147980607488)


def dev_check(id):
    if id == 250674147980607488 or id == 277981712989028353:
        return True
    return False


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
    await ctx.send("Here is our discord: https://discord.gg/WewwYV5")

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
    await ctx.send("Lemme join dat club: https://discordapp.com/api/oauth2/authorize?client_id=414456650519412747&permissions=0&scope=bot")
    
    
@bot.command()
async def upvote(ctx):
    """Upvote me!"""
    await ctx.send("Upvote me here! https://discordbots.org/bot/414456650519412747") 
    
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
            msg = await ctx.send("Done :ok_hand:")
            await asyncio.sleep(2)
            await msg.delete()
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
    
    
@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):

    if not dev_check(ctx.author.id):
        return await ctx.send("Only devs can use this command.")

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```') 
   
if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
