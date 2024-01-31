import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from config import BOT_TOKEN

kb = [
    [
        types.KeyboardButton(text="Просмотреть категории"),
        types.KeyboardButton(text="Запросить обратную связь с менеджером")
    ],
    [
        types.KeyboardButton(text="Корзина")
    ]
]



inline_kb = types.InlineKeyboardMarkup()
inline_kb.add(types.InlineKeyboardButton(text="Ноутбуки",callback_data="laptop_data"))
inline_kb.add(types.InlineKeyboardButton(text="Компьютерная переферия",callback_data="computer_peripherals_data"))
inline_kb.add(types.InlineKeyboardButton(text="Компьютерные комплектующие",callback_data="computer_accessories_data"))
inline_kb.add(types.InlineKeyboardButton(text="Смартфоны/телефоны и планшеты",callback_data="phone_data"))
inline_kb.add(types.InlineKeyboardButton(text="Bluetooth гарнитура",callback_data="bluetooth_data"))
inline_kb.add(types.InlineKeyboardButton(text="Электро-транспорт",callback_data="e-cars_data"))
inline_kb.add(types.InlineKeyboardButton(text="Вернуться назад",callback_data="back"))
