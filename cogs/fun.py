import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class mod:
    def init(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def test(self, ctx, user: discord.Member, *, msg: str):
        """test"""
        try:
            await user.send(msg)
            await ctx.message.delete()
            await ctx.send("works")
        except discord.ext.commands.MissingPermissions:
            await ctx.send("rip you dont got perms")
        except:
            await ctx.send("It did not make it.")
def setup(bot):
    bot.add_cog(fun.py(bot))
