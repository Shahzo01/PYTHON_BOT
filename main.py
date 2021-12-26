from aiogram import Bot, Dispatcher, executor, types
import wikipedia

bot = Bot(token='5073367745:AAFpBeT73Xy43uEIJVL8JxycBZw8GfK8q8Y')
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Salom! Men Wikibotman, Meni Shahzo01_07 nick nomidagi shaxs yaratdi!!!\nXush kelibsiz!!!")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!!!")


executor.start_polling(dp)
