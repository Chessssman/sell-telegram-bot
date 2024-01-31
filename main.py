import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from config import BOT_TOKEN
from utilities import keyboard
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

TOKEN = BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

hello_messages ={
    "day": "Добрый день! Рады видеть Вас в нашем профиле Доктор Гаджет! \n🔹Наш менеджер поможет вам с выбором гаджетов и аксессуаров \n🔹Наш сервис “Доктор Гаджет” находится по адресу: \nг.Донецк ул.Полоцкая 17 (оринетир: Майский рынок) \n🔹Работаем со Вторника по Воскресенье \n🔹Время работы: с 09:00 до 16:00\n🔹Тел: +7 949 (504) 22-88",
    "morning":"Доброе утро! Рады видеть Вас в нашем профиле Доктор Гаджет! \n🔹Наш менеджер поможет вам с выбором гаджетов и аксессуаров \n🔹Наш сервис “Доктор Гаджет” находится по адресу: \nг.Донецк ул.Полоцкая 17 (оринетир: Майский рынок) \n🔹Работаем со Вторника по Воскресенье \n🔹Время работы: с 09:00 до 16:00\n🔹Тел: +7 949 (504) 22-88",
    "night": "Добрый вечер! Рады видеть Вас в нашем профиле Доктор Гаджет! \n🔹Наш менеджер поможет вам с выбором гаджетов и аксессуаров \n🔹Наш сервис “Доктор Гаджет” находится по адресу: \nг.Донецк ул.Полоцкая 17 (оринетир: Майский рынок) \n🔹Работаем со Вторника по Воскресенье \n🔹Время работы: с 09:00 до 16:00\n🔹Тел: +7 949 (504) 22-88"
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=keyboard.kb,
        resize_keyboard=True,
    )
    print(get_greeting())
    await message.answer(str(get_greeting()), reply_markup=kb)

   
@dp.message_handler(Text(equals = "Просмотреть категории"))
async def get_category(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=keyboard.inline_kb)


@dp.inline_handler(lambda query: query.query == 'test_inline')
async def process_inline_query(query: InlineQuery):
    results = [
        InlineQueryResultArticle(
            id='1',
            title='Test Article',
            input_message_content=InputTextMessageContent(message_text='This is a test article.')
        )
    ]
    await bot.answer_inline_query(query.id, results=results, cache_time=1)

def get_greeting():
    now = datetime.datetime.now()
    current_hour = int(now.strftime("%H"))
    if 6 <= current_hour < 12:
        return hello_messages["morning"]
    elif 12 <= current_hour < 18:
        return hello_messages["day"]
    else:
        return hello_messages["night"]
    

if __name__ == '__main__':
    executor.start_polling(dp)
