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
    await message.answer("Выберите категорию:", reply_markup=keyboard.main_inline_kb)


@dp.callback_query_handler(lambda c: c.data.startswith('computer_peripherals_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите подкатегорию",
                                reply_markup=keyboard.peripherals_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('computer_accessories_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите подкатегорию",
                                reply_markup=keyboard.accessories_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('phone_pad_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите подкатегорию",
                                reply_markup=keyboard.mobile_kb)

@dp.callback_query_handler(lambda c: c.data.startswith('e-cars_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите подкатегорию",
                                reply_markup=keyboard.e_cars_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('bluetooth_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите подкатегорию",
                                reply_markup=keyboard.bluetooth_kb)
    
@dp.callback_query_handler(lambda c: c.data.startswith('back_to_main_data'))
async def category_menu_change(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите категорию:",
                                reply_markup=keyboard.main_inline_kb)

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
