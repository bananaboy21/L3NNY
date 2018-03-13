import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class mod:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def msg(self, ctx, user: discord.Member, *, msg: str):
        """DM someone as the bot!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("The DM has made it. hehehe... ")
        except commands.MissingPermissions:
            await ctx.send("rip you dont have enough permmisions")
        except:
            await ctx.send("ERROR:x:ERROR Make sure your message is in this format: _msg [user tagged] [message]")              
        
        
         
        
def setup(bot): 
    bot.add_cog(mod(bot))        
