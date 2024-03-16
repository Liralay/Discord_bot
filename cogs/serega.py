from discord.ext import commands
from variables import admin_id

serega_alive = False
serega_id = 234258286533148673
# 

class Allow_usage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serega(self, ctx):
        if ctx.author.id in admin_id:     
            global serega_alive 
            serega_alive = not serega_alive
            await ctx.send(f'Done. serega_alive set to {serega_alive}')
        else:
            await ctx.send('C лохами не общаюсь (сам с собой не общаюсь)')


async def setup(client):
    await client.add_cog(Allow_usage(client))