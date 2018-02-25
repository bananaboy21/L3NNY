    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.Member = None):
        """Gives you a avatar"""
        if user is None:
            av = ctx.message.author.avatar_url
            if '.gif' in av:
                av += "&f=.gif"
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=ctx.message.author.name)
            em.set_author(name='Profile Picture (pfp)')
            em.set_image(url=av)
            await ctx.send(embed=em)                  
        else:
            av = user.avatar_url
            if '.gif' in av:
                av += "&f=.gif"
            color = discord.Color(value=0xffffff)
            em = discord.Embed(color=color, title=user.name)
            em.set_author(name='Profile Picture')
            em.set_image(url=av)
            await ctx.send(embed=em) 
