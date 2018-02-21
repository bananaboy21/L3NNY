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
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """DM someone as me!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("They got the message :ok_hand:")
        except discord.ext.commands.MissingPermissions:
            await ctx.send("rip you. you dont got enough permz..")
        except:
            await ctx.send(":x: Error. Make sure your message is shaped in this way: _dm [tag person] [msg]")
