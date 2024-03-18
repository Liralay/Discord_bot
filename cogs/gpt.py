from discord.ext import commands
from cogs.serega import serega_alive, serega_id
from variables import admin_id
import os
import logging
import db_handler
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
        if db_handler.func(user_id=int(ctx.author.id)) == True:
            try:
                if serega_alive == True or ctx.author.id != serega_id:
                    logger.info('passed conditions')
                    message = arg
                    stream = client_chat_gpt.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[{"role": "user", "content": message}], # Serega LOX
                    stream=True,
                )   
                    logger.info('request sent to OpenAI')
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
        else:
             await ctx.send('Превышен лимит обращений')
             logging.info(f'Limit var is set to {max_q}')

    @commands.command()
    async def max_q(self, ctx, arg):
         if ctx.author.id in admin_id:
              try:
                max_q = int(arg)
                logging.info(f'changed max_q value to {max_q}')
              except Exception as e:
                   ctx.send(f'Ошибка {e}')
        




async def setup(client):
    await client.add_cog(asking(client))