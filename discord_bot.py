import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_API_KEY')



import discord
from discord.ext import commands

# Создаём объект Intents для получения намерений бота
intents = discord.Intents.default()
intents.messages = True

# Создаём объект бота
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Bot has logged in as {bot.user}')

@client.event
async def on_message(message):
    # Не отвечать на сообщения от самого бота
    if message.author == bot.user:
        return

    # Эхо-ответ: повторяем сообщение пользователя
    await message.channel.send("Hello")


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
# Запустить бота с вашим токеном
client.run(TOKEN)