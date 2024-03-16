from discord.ext import commands
from cogs.serega import serega_alive, serega_id
import os
import logging
logger = logging.getLogger(__name__)


from openai import OpenAI


client_chat_gpt = OpenAI(
  organization = os.getenv("Personal"),
)

class asking(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gpt(self, ctx, arg):
        try:
            if serega_alive == True or ctx.author.id != serega_id:
                logger.info('passed conditions')
                message = arg
                stream = client_chat_gpt.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[{"role": "user", "content": message}], # Serega LOX
                stream=True,
            )   
                logger.info('sent request')
                data = []
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        
                        data.append(chunk.choices[0].delta.content)
                        data_string = ''.join(map(str, data))
                if data:
                        print(data_string)
                        await ctx.send(data_string)
                        data = []
                else:
                        await ctx.send('error')
            else:
                await ctx.send('Я сам с собой не общаюсь')
        except Exception as e:
             await ctx.send(e)
        


    


async def setup(client):
    await client.add_cog(asking(client))