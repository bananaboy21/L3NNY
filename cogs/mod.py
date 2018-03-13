import discord
import sys
import os
import io
import asyncio
import json
import ezjson
from discord.ext import commands


class mod:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def msg(self, ctx, user: discord.Member, *, msg: str):
        """Message a user as me!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("It has made it. hehehe...")
        except commands.MissingPermissions:
            await ctx.send("rip. You dont have enough perms")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: _msg [tag person] [message]")
            
            

def setup(bot): 
    bot.add_cog(mod(bot))            
            
