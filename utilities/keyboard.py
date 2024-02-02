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

main_inline_kb = types.InlineKeyboardMarkup()
main_inline_kb.add(types.InlineKeyboardButton(text="Ноутбуки",callback_data="laptop_data"))
main_inline_kb.add(types.InlineKeyboardButton(text="Компьютерная переферия",callback_data="computer_peripherals_data"))
main_inline_kb.add(types.InlineKeyboardButton(text="Компьютерные комплектующие",callback_data="computer_accessories_data"))
main_inline_kb.add(types.InlineKeyboardButton(text="Смартфоны/телефоны и планшеты",callback_data="phone_pad_data"))
main_inline_kb.add(types.InlineKeyboardButton(text="Bluetooth гарнитура, Smart-часы",callback_data="bluetooth_data"))
main_inline_kb.add(types.InlineKeyboardButton(text="Электро-транспорт",callback_data="e-cars_data"))

peripherals_kb = types.InlineKeyboardMarkup()
peripherals_kb.row(
    types.InlineKeyboardButton(text="Мыши",callback_data="mouse_data"),
    types.InlineKeyboardButton(text="Web камеры",callback_data="camera_data")
)
peripherals_kb.row(
    types.InlineKeyboardButton(text="Кабели",callback_data="cabel_data"),
    types.InlineKeyboardButton(text="Клавиатуры",callback_data="keyboard_data")
)
peripherals_kb.row(
    types.InlineKeyboardButton(text="Вернуться на главную",callback_data="back_to_main_data")
)

accessories_kb = types.InlineKeyboardMarkup(resize_keyboard= True)
accessories_kb.add(types.InlineKeyboardButton(text="Процессоры",callback_data="processor_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Материнские платы",callback_data="motherboard_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Оперативная память",callback_data="ram_data"))
accessories_kb.add(types.InlineKeyboardButton(text="HDD диски",callback_data="hdd_data"))
accessories_kb.add(types.InlineKeyboardButton(text="SSD диски",callback_data="ssd_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Видеокарты",callback_data="video_card_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Блоки питания",callback_data="psu_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Системы охлаждения",callback_data="cooling_system_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Оптические приводы",callback_data="optical_drive_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Звуковые карты",callback_data="sound_card_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Внешние жесткие диски",callback_data="external_drive_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Аксессуары для HDD и SSD",callback_data="drive_accessories_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Контроллеры, USB устройства",callback_data="usb_controller_data"))
accessories_kb.add(types.InlineKeyboardButton(text="Вернуться на главную",callback_data="back_to_main_data"))


e_cars_kb = types.InlineKeyboardMarkup()
e_cars_kb.add(types.InlineKeyboardButton(text="Гироскутеры",callback_data="gyroscuter_data"))
e_cars_kb.add(types.InlineKeyboardButton(text="Электрические самокаты",callback_data="scooter_data"))
e_cars_kb.add(types.InlineKeyboardButton(text="Вернуться на главную",callback_data="back_to_main_data"))

mobile_kb = types.InlineKeyboardMarkup()
mobile_kb.add(types.InlineKeyboardButton(text="Смартфоны и мобильные телефоны",callback_data="phone_data"))
mobile_kb.add(types.InlineKeyboardButton(text="Планшеты",callback_data="pad_data"))
mobile_kb.add(types.InlineKeyboardButton(text="Вернуться на главную",callback_data="back_to_main_data"))

bluetooth_kb = types.InlineKeyboardMarkup()
bluetooth_kb.add(types.InlineKeyboardButton(text="Bluetooth гарнитура",callback_data="bluetooth_ear_data"))
bluetooth_kb.add(types.InlineKeyboardButton(text="Smart-часы",callback_data="smart_clock_data"))
bluetooth_kb.add(types.InlineKeyboardButton(text="Вернуться на главную",callback_data="back_to_main_data"))