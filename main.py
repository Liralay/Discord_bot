import asyncio
import os
from dotenv import load_dotenv

import logging
logger = logging.getLogger(__name__)

load_dotenv()

import discord
from discord.ext import commands

# Создаём объект Intents для получения намерений бота
intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='/', intents=intents)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

async def main():
        await load()
        TOKEN = os.getenv('DISCORD_API_KEY')
        await client.start(TOKEN)

if __name__ == '__main__':
    logging.basicConfig( level=logging.INFO)
    logger.info('Started')
    asyncio.run(main())
