import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
TOKEN = os.getenv('DISCORD_API_KEY')



import discord
from discord.ext import commands

# Создаём объект Intents для получения намерений бота
intents = discord.Intents.default()
intents.message_content = True

# Создаём объект бота
client = commands.Bot(command_prefix='/', intents=intents)


@client.event
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')


@client.command(name='gpt')
async def echo(ctx, *, arg):

    client = OpenAI(
  organization=os.getenv("Personal"),
)


    message = arg
    stream = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[{"role": "user", "content": message}], # Serega LOX
    stream=True,
)   
    data = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            
            data = data + (chunk.choices[0].delta.content)
            print(data)
    if data:
            await ctx.send(data)
    else:
            await ctx.send('error')





# Запустить бота с вашим токеном
client.run(TOKEN)