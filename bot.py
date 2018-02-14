import discord
import sys
import os
import io
from discord.ext import commands
bot = commands.Bot(command_prefix=('_'),description="A bot made by TheEmperor™\n\nHelp Commands",owner_id=[250674147980607488])


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(game=discord.Game(name=f"with {len(bot.guilds)} servers"))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="_help!"))
        await asyncio.sleep(15)
        
        
@bot.command()
async def invite(ctx):
    """Hit me up in your sever!"""
    await ctx.send("Lemme join that sever:https://discordapp.com/api/oauth2/authorize?client_id=413122600848326676&permissions=0&scope=bot")
          

@bot.command()
async def support(ctx):
  """Joins my support server"""
  await ctx.send("Join my support server: https://discord.gg/WewwYV5")
  
  
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
