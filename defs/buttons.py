from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_menu_buttons() -> ReplyKeyboardMarkup:
    buttons = [
        [
            KeyboardButton(text="Добавить затраты"),
            KeyboardButton(text="Добавить доходы"),
        ],
        [KeyboardButton(text="Отчёт за время")],
        [KeyboardButton(text="Поставить автоматический отчёт")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, 
        resize_keyboard=True)
    return keyboard

def get_periods() -> ReplyKeyboardMarkup:
    buttons = [
        [
            KeyboardButton(text="сегодня"),
            KeyboardButton(text="другой день"),
        ],
        [
            KeyboardButton(text="неделю"),
            KeyboardButton(text="месяц"),
        ],
        [KeyboardButton(text="произвольный промежуток"),]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons,
        resize_keyboard=True)
    return keyboard
