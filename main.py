import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_API_KEY')


import discord
from discord.ext import commands

# Создаём объект Intents для получения намерений бота
intents = discord.Intents.default()
intents.message_content = True

# Создаём объект бота
client = commands.Bot(command_prefix='/', intents=intents)

serega_alive = False
serega_id = 234258286533148673

admin_id = [242344024726437888, 252109360526786562]


usage = {}


from openai import OpenAI

client_chat_gpt = OpenAI(
  organization=os.getenv("Personal"),
)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.command(name = 'who_am_i')
async def help(ctx):
     await ctx.send('Я? Ничего абсолютно. Я умею жрать, что я сейчас и буду делать. Не, хз даже как это сказать... Да не, ну чисто в теории, вот по специальности, умею управдять промышлиными робатами, работать с ролсом я пока что не умею. Могу работать с программами \
                    по типу матлаба, все кад программы, которые есть, наверное... Я не пробовал только компас 3д. Я пробовал Fusion, T-Flex, я пробовал вообще все что только возможно, из того, что мне нужно\
                    Ну ардуино я, конечно, работал, но то, что мы сейчас делаем на лабе - это какая-то хератень. Типа мы... блин зачем... я не знаю, это какая-то логика программирования идет.\
                     Кароче, ладно, давайте, ребят, до завтра. Удачи вам там с проганьем. *Ту-дум*') #TODO Спросить у сереги "Что ты умеешь" и его ответ записать как дефолтный ответ бота

@client.command(name = 'serega')
async def serega(ctx):
    if ctx.author.id in admin_id:     
        global serega_alive 
        serega_alive = not serega_alive
        await ctx.send(f'Done. serega_alive set to {serega_alive}')
    else:
        await ctx.send('C лохами не общаюсь (сам с собой не общаюсь)')

@client.command(name = 'gpt')
async def gpt(ctx, *, arg):
    await get_chat_gpt_responce(ctx=ctx, arg=arg)

         
    

async def get_chat_gpt_responce(ctx, arg):
    if serega_alive == True or ctx.author.id != serega_id:
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


if __name__ == '__main__':
    client.run(TOKEN)