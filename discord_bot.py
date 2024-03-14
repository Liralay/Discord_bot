import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_API_KEY')



from openai import OpenAI

client_chat_gpt = OpenAI(
  organization=os.getenv("Personal"),
)


import discord
from discord.ext import commands

# Создаём объект Intents для получения намерений бота
intents = discord.Intents.default()
intents.message_content = True

# Создаём объект бота
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.command(name = 'help')
async def help(ctx):
     await ctx.send('') #TODO Спросить у сереги "Что ты умеешь" и его ответ записать как дефолтный ответ бота


@client.command(name = 'gpt')
async def gpt(ctx, *, arg):
    serega_id = 252109360526786562
    if ctx.author.id != serega_id:
        message = arg
        stream = client_chat_gpt.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": message}], # Serega LOX
        stream=True,
    )   
        data = []
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                
                data.append(chunk.choices[0].delta.content)
                data_string = ''.join(map(str, data))
        if data:
                await ctx.send(data_string)
        else:
                await ctx.send('error')
    else:
         await ctx.send('Я сам с собой не общаюсь')


# Запустить бота с вашим токеном
client.run(TOKEN)