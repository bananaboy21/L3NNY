import discord
import sys
import os
import io
import asyncio
import json
from discord.ext import commands


class mod:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """Escort your DM to someone thru the bot. Usage: *dm [tag person] [msg]"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("SuccESS! Your DM has made it! :white_check_mark: ")
        except commands.MissingPermissions:
            await ctx.send("Aw, come on! You thought you could get away with DM'ing people without permissions.")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: *dm [tag person] [msg]")



def setup(bot): 
    bot.add_cog(mod(bot))   
