from discord.ext import commands


class basic_funcs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def who_am_i(self, ctx):
        await ctx.send('Я? Ничего абсолютно. Я умею жрать, что я сейчас и буду делать. Не, хз даже как это сказать... Да не, ну чисто в теории, вот по специальности, умею управдять промышлиными робатами, работать с ролсом я пока что не умею. Могу работать с программами \
по типу матлаба, все кад программы, которые есть, наверное... Я не пробовал только компас 3д. Я пробовал Fusion, T-Flex, я пробовал вообще все что только возможно, из того, что мне нужно\
Ну ардуино я, конечно, работал, но то, что мы сейчас делаем на лабе - это какая-то хератень. Типа мы... блин зачем... я не знаю, это какая-то логика программирования идет.\
Кароче, ладно, давайте, ребят, до завтра. Удачи вам там с проганьем. *Ту-дум*') #FIXED: Спросить у сереги "Что ты умеешь" и его ответ записать как дефолтный ответ бота


async def setup(client):
    await client.add_cog(basic_funcs(client))